# -*- coding: utf-8 -*-
"""q1 引文锁定扫描器（ADR-0079；机检为筛，人审为判）。

用法:
  python tools/cite_audit.py [路径...] [--init] [--gate] [--check-hash] [--json] [--out PATH]
  python tools/cite_audit.py --all --init           # 全库生成清单骨架（state/axis/）

行为:
  默认    抽直引（成句/成短语，术语级不入清单），输出计数与候选，退出码 0。
  --init  为每件写 state/axis/<slug>.cite.json（已有则合并，不覆盖人工字段）。
  --gate  q1 校次门禁（T0 最小档）：清单存在、条数与文中直引一致、字段齐全、
          anchor 非空、hash 与当前文本一致。任一项不满足退出码 1。
  --check-hash 只校验 hash 守恒（q2–q6 出口用）。

判据依据: specs/060-six-axis-quality-gates/checklists/q1-cite.md（C-1…C-8）。
退出码: 0 通过/仅报告；1 --gate 未通过；2 用法错误。
"""
import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import axis_lib as ax  # noqa: E402

STATE_DIR = os.path.join(ax.ROOT, "state", "axis")
FIELDS = ("id", "loc", "form", "quote_lang", "origin_lang", "original",
          "original_status", "english", "english_source", "register_system",
          "anchor", "hash", "verdict", "reviewer")
VALID = {
    "form": {"block", "inline", "note"},
    "original_status": {"na", "present", "verifiable", "unavailable"},
    "english_source": {"self", "sep-inline", "sep-paraphrase", "published",
                       "editorial", "—"},
    "verdict": {"pass", "fail", "waived", "pending"},
}


def sha16(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def is_quote_level(inner):
    """引文级门槛：中文 ≥6 字，或西文 ≥12 字符且 ≥3 词；短术语归术语轴（C-4c）。"""
    if len(re.findall("[\u4e00-\u9fff]", inner)) >= 6:
        return True
    return len(inner) >= 12 and len(inner.split()) >= 3


def scan(path):
    text = ax.read_doc(path)
    slug = ax.slug_of(path)
    items = []
    for i, (line_no, start, inner) in enumerate(ax.quotes(text), 1):
        if not is_quote_level(inner):
            continue
        qlang = ax.lang_of(inner)
        items.append({
            "id": "c-%s-%03d" % (slug, i),
            "loc": "L%d" % line_no,
            "form": "block" if line_no and text.splitlines()[line_no - 1].lstrip().startswith(">") else "inline",
            "quote_lang": ax.bcp47(qlang),
            "origin_lang": "unknown",
            "original": "—",
            "original_status": "unavailable",
            "english": inner if qlang in ("none", "unclassified-latin") else "—",
            "english_source": "self" if qlang in ("none", "unclassified-latin") else "—",
            "register_system": "—",
            "anchor": "",
            "hash": sha16(inner),
            "verdict": "pending",
            "reviewer": "",
        })
    return slug, items


def manifest_path(slug):
    return os.path.join(STATE_DIR, slug + ".cite.json")


def load_manifest(slug):
    p = manifest_path(slug)
    if not os.path.exists(p):
        return None
    with open(p, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def merge_manifest(slug, fresh):
    """合并：保留人工字段（anchor/verdict/reviewer/origin_lang 等），只补 hash 与位置。"""
    old = load_manifest(slug) or {"slug": slug, "items": []}
    by_hash = {it["hash"]: it for it in old.get("items", [])}
    merged, added = [], 0
    for it in fresh:
        prev = by_hash.get(it["hash"])
        if prev:
            it["id"] = prev.get("id", it["id"])
            for k in ("origin_lang", "original", "original_status", "english",
                      "english_source", "register_system", "anchor", "verdict",
                      "reviewer"):
                if prev.get(k) not in (None, ""):
                    it[k] = prev[k]
        else:
            added += 1
        merged.append(it)
    return {"slug": slug, "schema": "cite-manifest/v1", "items": merged}, added


def gate(slug, items, text):
    """T0 最小硬档：C-1 完备、C-2 字段、C-3/C-4 枚举、C-6 anchor、C-7 hash。"""
    m = load_manifest(slug)
    problems = []
    if m is None:
        return ["清单缺失：先跑 --init（%s）" % os.path.relpath(manifest_path(slug), ax.ROOT)]
    mi = m.get("items", [])
    have = {}
    for it in mi:
        have[it.get("hash")] = it
    for it in items:
        got = have.get(it["hash"])
        if not got:
            problems.append("C-1 未登记直引 %s" % it["loc"])
            continue
        miss = [k for k in FIELDS if k not in got]
        if miss:
            problems.append("C-2 %s 缺字段 %s" % (it["id"], ",".join(miss)))
        for k, allowed in VALID.items():
            if got.get(k) not in allowed:
                problems.append("C-2 %s 字段 %s 取值非法：%r" % (it["id"], k, got.get(k)))
        if got.get("quote_lang") != "en" and not str(got.get("anchor") or "").strip():
            problems.append("C-6 %s 缺 anchor" % it["id"])
        if got.get("verdict") == "pending":
            problems.append("C-4 %s 未裁定（verdict=pending）" % it["id"])
    if len(mi) != len(items):
        problems.append("C-1 清单条数 %d ≠ 文中直引 %d" % (len(mi), len(items)))
    for it in mi:
        h = it.get("hash")
        if h and h not in {x["hash"] for x in items}:
            problems.append("C-7 %s 引文已变动（hash 不在当前文本）" % it.get("id"))
    return problems


def check_hash(slug, items):
    m = load_manifest(slug)
    if m is None:
        return ["清单缺失"]
    cur = {x["hash"] for x in items}
    return ["C-7 %s 引文已变动" % it.get("id") for it in m.get("items", [])
            if it.get("hash") and it["hash"] not in cur]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true", help="全库已译件")
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--check-hash", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    args = ap.parse_args()
    if args.all:
        args.paths = ax.target_paths(None)
    if not args.paths:
        ap.error("需要路径或 --all")

    report = {"schema": "cite-audit/v1", "files": [], "problems": []}
    for p in ax.target_paths(args.paths):
        slug, items = scan(p)
        rep = {"path": os.path.relpath(p, ax.ROOT).replace("\\", "/"),
               "slug": slug, "quote_level": len(items),
               "by_lang": {}, "added": 0}
        for it in items:
            rep["by_lang"][it["quote_lang"]] = rep["by_lang"].get(it["quote_lang"], 0) + 1
        if args.init:
            data, added = merge_manifest(slug, items)
            os.makedirs(STATE_DIR, exist_ok=True)
            with open(manifest_path(slug), "w", encoding="utf-8", newline="\n") as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
            rep["added"] = added
        if args.gate or args.check_hash:
            probs = check_hash(slug, items) if args.check_hash else gate(slug, items, None)
            for x in probs:
                report["problems"].append("%s: %s" % (slug, x))
        report["files"].append(rep)

    if args.out:
        ax.emit(report, args.out)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print("文件 %d；直引级候选 %d；问题 %d"
              % (len(report["files"]), sum(f["quote_level"] for f in report["files"]),
                 len(report["problems"])))
        for x in report["problems"][:50]:
            print("  -", x)
    return 1 if (args.gate and report["problems"]) else 0


if __name__ == "__main__":
    sys.exit(main())
