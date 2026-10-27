# -*- coding: utf-8 -*-
"""全库 A–Z 审阅战役驱动器（specs/007-review-campaign，用户 2026-10-28 指令）。

按网页 A–Z 顺序逐词条执行三步审阅（用户已批准批量比较，不计成本）：
  1. 抓取+比较本地HTML：tools/compare.py <slug>（在线快照 vs en/<slug>/index.html，
     变更由工具自动落盘 specs/001-sep-sync-pipeline/compare/<slug>.json，本驱动仅登记）；
  2. en/ 包深度复核：tools/en_integrity.py <slug>（页面真实性/引用闭包/数学形态/游离件）；
  3. 英语markdown复核：tools/check_math.py <slug>（yuanwen md 公式保真）。

礼貌抓取：对齐 fetch_all.py 路通道语义（Pacer），每路通道两次抓取间隔 ≥5 秒；
默认 8 路（配置 A=16路×5秒 的用户先例之内，本战役取保守半速）。

凭证：
  specs/007-review-campaign/results/review-log.jsonl   一行一词条
  specs/007-review-campaign/results/status.json        检查点（每 25 条）
  specs/007-review-campaign/results/integrity/<slug>.json   硬问题完整明细
  specs/007-review-campaign/results/math/<slug>.json        公式失真完整明细

续跑：review-log.jsonl 中已有 done 行的 slug 跳过；瞬时错误（无 JSON 的崩溃/
超时）不记 done，重跑自动重试。

已知例外：6 条撤稿留存词条在线软 404 → 标 expected_offline_404，记 done
（保留依据为归档版基线，c75cc794/2eecf911 裁定）。

用法:
  python script/review_campaign.py [--workers 8] [--limit N] [--only slug ...]
输出: stderr 进度；stdout JSON 汇总。
退出码: 0 全部 done 且无 error；1 有 error/finding；2 用法错误。
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from tools.common import load_json, repo_path, utcnow_iso

RESULTS = ("specs", "007-review-campaign", "results")
CHANNEL_GAP = 5.0  # 每路通道最小间隔（秒），对齐 fetch.MIN_DELAY
POLITE_SLEEP_BEFORE_FIRST = False  # 首请求不等待（Pacer 语义：last=0 直接放行）

WITHDRAWN = {"continental-rationalism", "pineal-gland", "qm-action-distance",
             "scientific-explanation", "time-experience", "wisdom"}

_stdout_lock = threading.Lock()


def ordered_slugs():
    """网页 A–Z 顺序 = baseline/catalog.json items 序；6 条非目录撤稿留存按字母序殿后。"""
    cat = load_json(repo_path("baseline", "catalog.json"))
    base = load_json(repo_path("baseline", "entries.json"))
    base_slugs = {r["slug"] for r in base["entries"]}
    ordered, seen = [], set()
    for it in cat["items"]:
        s = it["slug"]
        if s in base_slugs:
            ordered.append(s)
            seen.add(s)
    tail = sorted(base_slugs - seen)
    return ordered + tail, len(ordered), len(tail)


def done_slugs():
    path = repo_path(*RESULTS, "review-log.jsonl")
    done = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("done"):
                    done.add(rec["slug"])
    return done


def run_tool(args, timeout):
    """跑子进程工具；返回 (exit_code, stdout_json 或 None, stderr 尾部)。"""
    try:
        p = subprocess.run([sys.executable] + args, capture_output=True,
                           timeout=timeout, cwd=repo_path("."))
        code = p.returncode
        out, err = p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")
    except subprocess.TimeoutExpired as e:
        return None, None, "TIMEOUT %ss" % timeout
    js = None
    try:
        js = json.loads(out)
    except (json.JSONDecodeError, TypeError):
        pass
    return code, js, err[-500:] if err else ""


def step_compare(slug):
    code, js, err = run_tool(["tools/compare.py", slug], timeout=300)
    rec = {"exit": code}
    if js is not None:
        r = (js.get("results") or [{}])[0]
        if r.get("error"):
            m = re.search(r"HTTP (\d+)", r["error"])
            if m and m.group(1) in ("404", "410") and slug in WITHDRAWN:
                rec["status"] = "expected_offline_404"
            else:
                rec["status"] = "error"
            rec["error"] = r["error"]
        else:
            rec["status"] = "changed" if r.get("changed") else "ok"
            rec["sections_changed"] = r.get("sections_changed", 0)
            if r.get("changes_file"):
                rec["changes_file"] = r["changes_file"]
            if r.get("note"):
                rec["note"] = r["note"]
    else:
        rec["status"] = "transient"
        rec["error"] = (err or "no output").strip() or "exit=%s" % code
    return rec


def step_integrity(slug):
    code, js, err = run_tool(["tools/en_integrity.py", slug], timeout=300)
    if js is None:
        return {"status": "transient", "error": (err or "no output").strip() or "exit=%s" % code}
    hard = js.get("with_hard_issues", 0) + len(js.get("errors") or [])
    rec = {"status": "ok" if hard == 0 else "finding",
           "clean": js.get("clean", 0), "hard_findings": js.get("hard_findings", 0),
           "mathjax": js.get("mathjax_entries", 0), "math_inline": js.get("math_inline_entries", 0)}
    if hard:
        outdir = repo_path(*RESULTS, "integrity")
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, slug + ".json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(js, f, ensure_ascii=False, indent=1)
        rec["detail"] = "results/integrity/%s.json" % slug
    return rec


def step_math(slug):
    # 退出码语义（contracts/cli.md）：只由 missing（公式丢失/占位残留）驱动；
    # unbalanced 仅为渲染歧义警告，单列 warn，不计 finding。
    code, js, err = run_tool(["tools/check_math.py", slug], timeout=300)
    if js is None:
        return {"status": "transient", "error": (err or "no output").strip() or "exit=%s" % code}
    missing = len(js.get("missing") or [])
    unbal = len(js.get("unbalanced") or [])
    rec = {"status": "finding" if missing else ("warn" if unbal else "ok"),
           "formulas": js.get("formulas", 0), "missing": missing, "unbalanced": unbal}
    if missing or unbal:
        outdir = repo_path(*RESULTS, "math")
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, slug + ".json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(js, f, ensure_ascii=False, indent=1)
        rec["detail"] = "results/math/%s.json" % slug
    return rec


class Writer:
    def __init__(self):
        self.lock = threading.Lock()
        self.path = repo_path(*RESULTS, "review-log.jsonl")
        self.status_path = repo_path(*RESULTS, "status.json")
        self.count = 0

    def write(self, rec):
        with self.lock:
            with open(self.path, "a", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            self.count += 1
            if self.count % 25 == 0:
                self.checkpoint(rec)

    def checkpoint(self, rec):
        tmp = {"updated_at": utcnow_iso(), "last_slug": rec.get("slug"),
               "lines": self.count}
        with open(self.status_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(tmp, f, ensure_ascii=False, indent=1)


def worker(slots, writer, total, started):
    last_fetch = 0.0
    while True:
        try:
            idx, slug = next(slots)
        except StopIteration:
            return
        gap = time.time() - last_fetch
        if last_fetch > 0 and gap < CHANNEL_GAP:
            time.sleep(CHANNEL_GAP - gap)
        rec = {"idx": idx, "slug": slug, "at": utcnow_iso()}
        rec["compare"] = step_compare(slug)
        last_fetch = time.time()
        rec["integrity"] = step_integrity(slug)
        rec["math"] = step_math(slug)
        transient = any(rec[s].get("status") == "transient"
                        for s in ("compare", "integrity", "math"))
        rec["done"] = not transient
        writer.write(rec)
        with _stdout_lock:
            el = int(time.time() - started)
            sys.stderr.write("[%s/%d %ds] %s: %s / %s / %s\n" % (
                idx, total, el, slug, rec["compare"].get("status"),
                rec["integrity"].get("status"), rec["math"].get("status")))
            sys.stderr.flush()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=None, help="只跑前 N 个待审词条（冒烟/分批）")
    ap.add_argument("--only", nargs="*", default=None, help="只跑指定 slug（冒烟）")
    args = ap.parse_args(argv)

    ordered, n_cat, n_tail = ordered_slugs()
    done = done_slugs()
    if args.only:
        todo = [(i + 1, s) for i, s in enumerate(ordered) if s in set(args.only)]
    else:
        todo = [(i + 1, s) for i, s in enumerate(ordered) if s not in done]
    if args.limit:
        todo = todo[:args.limit]

    total_all = len(ordered)
    sys.stderr.write("词序：目录内 %d + 撤稿留存 %d = %d；已完成 %d；本次待审 %d（%d 路 × 每路 %gs）\n"
                     % (n_cat, n_tail, total_all, len(done), len(todo),
                        args.workers, CHANNEL_GAP))
    if not todo:
        print(json.dumps({"todo": 0, "already_done": len(done), "total": total_all},
                         ensure_ascii=False))
        return 0

    results_dir = repo_path(*RESULTS)
    os.makedirs(results_dir, exist_ok=True)
    writer = Writer()
    started = time.time()
    slots = iter(todo)
    findings, errors, transient = [], [], []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = [pool.submit(worker, slots, writer, len(todo), started)
                for _ in range(args.workers)]
        for f in as_completed(futs):
            f.result()

    # 汇总：读回全量 JSONL 统计
    stats = {"total": total_all, "done": 0, "ok": 0, "changed": [], "findings": [],
             "warnings": [], "errors": [], "transient_left": 0}
    with open(writer.path, encoding="utf-8") as f:
        for line in f:
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not r.get("done"):
                stats["transient_left"] += 1
                continue
            stats["done"] += 1
            c = r.get("compare", {})
            st = c.get("status")
            if st == "ok":
                stats["ok"] += 1
            elif st == "changed":
                stats["changed"].append(r["slug"])
            elif st == "error":
                stats["errors"].append({"slug": r["slug"], "error": c.get("error")})
            if r.get("integrity", {}).get("status") == "finding" or \
               r.get("math", {}).get("status") == "finding":
                stats["findings"].append(r["slug"])
            elif r.get("math", {}).get("status") == "warn":
                stats["warnings"].append(r["slug"])
    print(json.dumps(stats, ensure_ascii=False))
    return 0 if not (stats["errors"] or stats["findings"] or stats["transient_left"]) else 1


if __name__ == "__main__":
    if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.exit(main())
