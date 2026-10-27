# -*- coding: utf-8 -*-
"""全局统计表与批次调度（specs/005 parallel-design，2026-10-27 用户指令）。

大流程按 a–z 批次拆分（数字开头归批次 1，共 27 批），每批独立无耦合；
账本 specs/005-translation-campaign/ledger.json 只存意图与认领（phase/
claimed_by/at/note），计数从仓库实时推导——账本与事实零漂移。
本工具只记账不重做：各阶段与既有工具一一对应（见 parallel-design.md）。

用法:
  campaign.py init                        # 建/补账本（幂等，不覆盖已有认领）
  campaign.py status [--batch a]          # 全局统计表（计数实时推导）
  campaign.py claim <batch> [--session ID] [--force]
  campaign.py release <batch>
  campaign.py advance <batch> <phase> [--note N]
  campaign.py next [--phase P]            # 建议下一批次（未完成且未认领）
退出码: 0 成功；2 用法错误。
"""
import argparse
import io
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import load_json, repo_path

if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

LEDGER = repo_path("specs", "005-translation-campaign", "ledger.json")
PHASES = ["pending", "intake", "fetch", "convert", "translate", "done"]
BATCHES = ["1"] + [c for c in "abcdefghijklmnopqrstuvwxyz"]
STALE_DAYS = 7


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_ledger():
    if os.path.isfile(LEDGER):
        return load_json(LEDGER)
    return {"version": 1, "batches": {}}


def save_ledger(d):
    d["updated_at"] = now_iso()
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")


def batch_of(slug):
    c = slug[0].lower()
    return c if (c.isalpha() or c.isdigit()) else "1"


def batch_counts(letter):
    """从仓库实时推导批次计数（账本不存计数，零漂移）。"""
    slugs = []
    for line in open(repo_path("SUMMARY.md"), encoding="utf-8"):
        m = re.match(r"^\s*\* \[(.+)\]\(([a-z0-9]/[A-Za-z0-9][A-Za-z0-9.\-]*)\.md\)$", line.rstrip("\n"))
        if not m:
            continue
        title, path = m.group(1), m.group(2)
        if "— see" in title or "——见" in title:
            continue
        if batch_of(path.split("/")[1]) != letter:
            continue
        slugs.append((path.split("/")[1], title.lstrip("* ").strip()))
    total = len(slugs)
    fetched = converted = done = 0
    base = {e["slug"] for e in load_json(repo_path("baseline", "entries.json"))["entries"]}
    for slug, _t in slugs:
        if slug in base:
            fetched += 1
        if os.path.isfile(repo_path("yuanwen", letter, slug + ".md")):
            converted += 1
        tp = repo_path("tasks", letter, slug + ".json")
        if os.path.isfile(tp):
            try:
                if json.load(open(tp, encoding="utf-8")).get("state") == "done":
                    done += 1
            except (OSError, ValueError):
                pass
    return {"total": total, "baseline": fetched, "yuanwen": converted, "done": done}


def cmd_init():
    d = load_ledger()
    added = 0
    for b in BATCHES:
        if b not in d["batches"]:
            d["batches"][b] = {"phase": "pending", "claimed_by": None,
                               "claimed_at": None, "note": ""}
            added += 1
    save_ledger(d)
    print(json.dumps({"batches": len(d["batches"]), "added": added}, ensure_ascii=False))
    return 0


def cmd_status(args):
    d = load_ledger()
    keys = [args.batch] if args.batch else [b for b in BATCHES if b in d["batches"]] or BATCHES
    total = sum(batch_counts(b)["total"] for b in keys)
    done = sum(batch_counts(b)["done"] for b in keys)
    print("%-4s %-9s %-7s %-6s %-6s %-8s %-14s %s" %
          ("批次", "phase", "总词条", "基线", "镜像", "done", "认领者", "认领时间"))
    for b in keys:
        meta = d["batches"].get(b, {})
        c = batch_counts(b)
        print("%-4s %-9s %-7d %-6d %-6d %-8d %-14s %s" %
              (b, meta.get("phase", "pending"), c["total"], c["baseline"],
               c["yuanwen"], c["done"], meta.get("claimed_by") or "-", meta.get("claimed_at") or "-"))
    print("\n全局：批次 %d | 词条 %d | done %d（%.1f%%）" %
          (len(keys), total, done, 100.0 * done / total if total else 0))
    return 0


def cmd_claim(args):
    if not re.fullmatch(r"[a-z0-9]", args.batch):
        print(json.dumps({"error": "批次必须是 1 或 a–z"}))
        return 2
    d = load_ledger()
    meta = d["batches"].setdefault(args.batch, {"phase": "pending", "claimed_by": None,
                                                "claimed_at": None, "note": ""})
    if meta.get("claimed_by") and not args.force:
        age = None
        try:
            age = datetime.now(timezone.utc) - datetime.fromisoformat(
                meta["claimed_at"].replace("Z", "+00:00"))
        except ValueError:
            pass
        if age is None or age < timedelta(days=STALE_DAYS):
            print(json.dumps({"error": "批次已认领 by %s（%s）；抢占用 --force" %
                                       (meta["claimed_by"], meta.get("claimed_at"))}))
            return 1
    meta["claimed_by"] = args.session or "anonymous"
    meta["claimed_at"] = now_iso()
    save_ledger(d)
    print(json.dumps({"claimed": args.batch, "session": meta["claimed_by"],
                      "next_phase": meta.get("phase", "pending")}, ensure_ascii=False))
    return 0


def cmd_release(args):
    d = load_ledger()
    meta = d["batches"].get(args.batch)
    if not meta or not meta.get("claimed_by"):
        print(json.dumps({"error": "批次未认领"}))
        return 1
    meta["claimed_by"] = None
    meta["claimed_at"] = None
    save_ledger(d)
    print(json.dumps({"released": args.batch}))
    return 0


def cmd_advance(args):
    if args.phase not in PHASES:
        print(json.dumps({"error": "phase 必须是 %s" % "/".join(PHASES)}))
        return 2
    d = load_ledger()
    meta = d["batches"].setdefault(args.batch, {"phase": "pending", "claimed_by": None,
                                                "claimed_at": None, "note": ""})
    cur = PHASES.index(meta.get("phase", "pending"))
    if PHASES.index(args.phase) < cur:
        print(json.dumps({"error": "阶段只能前进：当前 %s" % meta["phase"]}))
        return 1
    meta["phase"] = args.phase
    meta["note"] = args.note or meta.get("note", "")
    meta["advanced_at"] = now_iso()
    save_ledger(d)
    print(json.dumps({"batch": args.batch, "phase": args.phase, "note": meta["note"]},
                     ensure_ascii=False))
    return 0


def cmd_next(args):
    d = load_ledger()
    want = args.phase
    for b in BATCHES:
        meta = d["batches"].get(b, {})
        if meta.get("claimed_by"):
            continue
        c = batch_counts(b)
        if c["done"] >= c["total"] and c["total"] > 0:
            continue  # 已完成
        if want and PHASES.index(meta.get("phase", "pending")) != PHASES.index(want):
            continue
        print(json.dumps({"batch": b, "phase": meta.get("phase", "pending"),
                          "counts": c, "tool": "见 specs/005/parallel-design.md 阶段-工具表"},
                         ensure_ascii=False))
        return 0
    print(json.dumps({"note": "无可建议批次（全部完成或已认领）"}))
    return 0


def batch_slugs(letter):
    """批次词条清单（SUMMARY 实时推导，单一事实源）。"""
    pat = re.compile(r"^(\s*)\* \[(.+)\]\(([a-z0-9]/[A-Za-z0-9][A-Za-z0-9.\-]*)\.md\)$")
    out = []
    for line in open(repo_path("SUMMARY.md"), encoding="utf-8"):
        m = pat.match(line.rstrip("\n"))
        if not m:
            continue
        title, path = m.group(2), m.group(3)
        slug = path.split("/")[1]
        if batch_of(slug) != letter:
            continue
        if "— see" in title or "——见" in title:
            continue
        out.append(slug)
    return out


def cmd_slugs(args):
    if not re.fullmatch(r"[a-z0-9]", args.batch):
        print(json.dumps({"error": "批次必须是 1 或 a–z"}))
        return 2
    for slug in batch_slugs(args.batch):
        print(slug)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?")
    ap.add_argument("batch", nargs="?")
    ap.add_argument("phase", nargs="?")
    ap.add_argument("--batch", dest="batch_opt")
    ap.add_argument("--session", dest="session")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--note", dest="note")
    args = ap.parse_args(argv)
    cmd = args.cmd or ""
    if cmd == "init":
        return cmd_init()
    if cmd == "status":
        return cmd_status(type("A", (), {"batch": args.batch_opt})())
    if cmd == "claim":
        if not args.batch:
            print(json.dumps({"error": "用法: claim <batch> [--session ID]"}))
            return 2
        return cmd_claim(type("A", (), {"batch": args.batch, "session": args.session,
                                        "force": args.force})())
    if cmd == "release":
        if not args.batch:
            print(json.dumps({"error": "用法: release <batch>"}))
            return 2
        return cmd_release(type("A", (), {"batch": args.batch})())
    if cmd == "advance":
        if not args.batch or not args.phase:
            print(json.dumps({"error": "用法: advance <batch> <phase> [--note N]"}))
            return 2
        return cmd_advance(type("A", (), {"batch": args.batch, "phase": args.phase,
                                          "note": args.note})())
    if cmd == "slugs":
        if not args.batch:
            print(json.dumps({"error": "用法: slugs <batch>"}))
            return 2
        return cmd_slugs(type("A", (), {"batch": args.batch})())
    if cmd == "next":
        return cmd_next(type("A", (), {"phase": args.batch if args.batch in PHASES else None})())
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
