#!/usr/bin/env python3
"""J 组 38 路子代理滚动监控器（长线任务，避免死等）。

用法：
  python specs/005-translation-campaign/bin/j_batch_monitor.py            # 聚合进度
  python specs/005-translation-campaign/bin/j_batch_monitor.py --watch 30  # 每 30s 聚合一次（Ctrl-C 停）
  python specs/005-translation-campaign/bin/j_batch_monitor.py --stall 15  # 标记停滞词条（最后 advance 距今 >N 分钟）

设计要点（对齐 e-batch 监控器，e 为其母本）：
  * 状态源 = tasks/j/*.json（task_ops 状态机单一事实源），零写入。
  * 每次聚合写 JSONL 断点凭证（specs/005/results/j-batch-progress.jsonl），一行一快照，可续跑。
  * 停滞检测：某词条 state 非终态且最后一步 advance 时间距今 > --stall 分钟 → 标记 STALL。
  * 终态判据：done（翻译波完成）；s3_checked（可进复核波）。

退出码：0 = 正常聚合；1 = 存在 STALL 词条。
"""
import argparse
import glob
import json
import os
import sys
import time
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
TASKS_DIR = os.path.join(REPO, "tasks", "j")
RESULT_DIR = os.path.join(REPO, "specs", "005-translation-campaign", "results")
PROGRESS_LOG = os.path.join(RESULT_DIR, "j-batch-progress.jsonl")

# 状态机顺序（对齐 tools/task_ops.py ORDER["retranslate"]）
ORDER = ["pending", "cleared", "drafted", "s1_checked", "s2_checked",
         "s3_checked", "r1_reviewed", "r2_reviewed", "r3_reviewed", "done"]
TERMINAL = {"done"}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def last_advance_at(task):
    steps = task.get("steps", [])
    for st in reversed(steps):
        if st.get("step") != "unblock" and st.get("at"):
            return st["at"]
    return task.get("created_at")


def parse_iso(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def load_tasks():
    out = {}
    for f in glob.glob(os.path.join(TASKS_DIR, "*.json")):
        slug = os.path.splitext(os.path.basename(f))[0]
        if slug.startswith("_"):  # 跳过子代理草稿（_tr_*.json 等非任务文件）
            continue
        try:
            out[slug] = json.load(open(f, encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            out[slug] = {"slug": slug, "state": "CORRUPT", "error": str(e)}
    return out


def aggregate(tasks, stall_minutes=None):
    from collections import Counter
    state_counter = Counter(t["state"] for t in tasks.values())
    stalls = []
    now = datetime.now(timezone.utc)
    for slug, t in tasks.items():
        if t["state"] in TERMINAL:
            continue
        if stall_minutes is None:
            continue
        last = parse_iso(last_advance_at(t))
        if last is None:
            stalls.append((slug, t["state"], "no-timestamp"))
            continue
        age = (now - last).total_seconds() / 60.0
        if age > stall_minutes:
            stalls.append((slug, t["state"], "%.0fmin" % age))
    return state_counter, stalls


def snapshot(state_counter):
    return {
        "ts": now_iso(),
        "total": sum(state_counter.values()),
        "done": state_counter.get("done", 0),
        "s3_checked": state_counter.get("s3_checked", 0),
        "states": dict(state_counter),
    }


def write_progress(snap):
    os.makedirs(RESULT_DIR, exist_ok=True)
    with open(PROGRESS_LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(snap, ensure_ascii=False) + "\n")


def print_report(snap, stalls):
    print("=" * 60)
    print("J 组进度  %s" % snap["ts"])
    print("  总数 %d | done %d | s3_checked %d | 翻译波在途 %d"
          % (snap["total"], snap["done"], snap["s3_checked"],
             snap["total"] - snap["done"] - snap["s3_checked"]))
    for st in ORDER:
        if snap["states"].get(st):
            print("  %-12s %d" % (st, snap["states"][st]))
    for st, n in sorted(snap["states"].items()):
        if st not in ORDER:
            print("  %-12s %d  <-- 非常规" % (st, n))
    if stalls:
        print("  STALL %d 条（最后 advance 距今超阈值，需重派）：" % len(stalls))
        for slug, st, age in stalls[:20]:
            print("    - %-34s %-12s %s" % (slug, st, age))
        if len(stalls) > 20:
            print("    ... 共 %d 条" % len(stalls))
    else:
        print("  停滞：无（全部在推进）")
    print("=" * 60)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--watch", type=int, default=0, help="每 N 秒循环聚合（0=单次）")
    ap.add_argument("--stall", type=int, default=0, help="停滞阈值（分钟），0=不检测")
    ap.add_argument("--log", action="store_true", help="写断点凭证 JSONL")
    args = ap.parse_args()

    rc = 0
    while True:
        tasks = load_tasks()
        state_counter, stalls = aggregate(tasks, args.stall or None)
        snap = snapshot(state_counter)
        print_report(snap, stalls)
        if args.log:
            write_progress(snap)
        if stalls:
            rc = 1
        if not args.watch:
            return rc
        time.sleep(args.watch)


if __name__ == "__main__":
    sys.exit(main())
