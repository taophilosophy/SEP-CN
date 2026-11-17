# -*- coding: utf-8 -*-
"""重置面体检：把"当前 state"与"历史事件"两套读数对出来（只读判官）。

为何需要：`state` 是单游标，被 revert 覆盖后只剩最后一格；`steps` 是追加日志，
保留全部经过。两者对读，才能回答"到底有多少条目真的走完过全链"。

判据（本脚本自身，便于复算）：
  A. 历史最高节点 = steps 中最后一个属于 KNOWN 的 step 名；
  B. 无记录 = steps 为空但 state 非 pending；
  C. 回退归因 = revert-state 事件按 evidence 前 40 字归并（口径变更成组出现）。

用法: python specs/042-progress-model-v2/bin/reset_audit.py [--json PATH]
退出码: 0 恒为 0（判官不阻断）；2 根目录不符。
"""
import argparse
import collections
import glob
import io
import json
import os
import sys

if getattr(sys.stdout, "encoding", None) and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
KNOWN = ["s0", "draft", "s1", "s2", "s24", "s25", "s3", "r1", "r2", "r3", "done"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None, help="写出机读产物路径")
    args = ap.parse_args()

    if not os.path.isdir(os.path.join(ROOT, "tasks")):
        print("根目录不符：未找到 tasks/", file=sys.stderr)
        return 2

    states = collections.Counter()
    kinds = collections.Counter()
    step_names = collections.Counter()
    last_node = collections.Counter()
    no_record = collections.Counter()
    cross = collections.Counter()
    revert_by_cause = collections.Counter()
    revert_total = 0
    total = 0
    steps_total = 0
    missing_doc = []
    done_events = 0

    for path in glob.glob(os.path.join(ROOT, "tasks", "**", "*.json"), recursive=True):
        try:
            with open(path, encoding="utf-8") as fh:
                d = json.load(fh)
        except Exception:
            continue
        if not (isinstance(d, dict) and "state" in d):
            continue
        total += 1
        states[d["state"]] += 1
        kinds[d.get("kind")] += 1

        zdoc = d.get("zh_doc")
        if zdoc and not os.path.exists(os.path.join(ROOT, zdoc)):
            missing_doc.append(zdoc)

        last = None
        for s in d.get("steps") or []:
            steps_total += 1
            nm = s.get("step")
            step_names[nm] += 1
            if nm == "done":
                done_events += 1
            if nm in KNOWN:
                last = nm
            if nm == "revert-state":
                revert_total += 1
                ev = (s.get("evidence") or "")[:40]
                revert_by_cause[ev] += 1

        if last:
            last_node[last] += 1
            cross[(d["state"], last)] += 1
        else:
            no_record[d["state"]] += 1

    reached_done_by_state = collections.Counter()
    for (st, last), v in cross.items():
        if last == "done":
            reached_done_by_state[st] += v

    out = {
        "root": ROOT,
        "totals": {
            "tasks": total,
            "steps_events": steps_total,
            "tasks_with_history": total - sum(no_record.values()),
            "tasks_without_history": sum(no_record.values()),
            "done_events": done_events,
            "revert_events": revert_total,
            "zh_doc_missing": len(missing_doc),
        },
        "state_distribution": dict(states.most_common()),
        "kind_distribution": dict(kinds.most_common()),
        "highest_node_reached": dict(last_node.most_common()),
        "no_history_state": dict(no_record.most_common()),
        "reached_done_by_current_state": dict(reached_done_by_state.most_common()),
        "revert_by_cause": dict(revert_by_cause.most_common()),
        "step_names": dict(step_names.most_common()),
        "zh_doc_missing_list": missing_doc,
    }

    if args.json:
        dst = args.json if os.path.isabs(args.json) else os.path.join(ROOT, args.json)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
            fh.write("\n")

    t = out["totals"]
    print("任务 %d｜事件 %d｜有史 %d｜无史 %d"
          % (t["tasks"], t["steps_events"], t["tasks_with_history"], t["tasks_without_history"]))
    print("done 事件 %d｜revert 事件 %d｜译文缺失 %d"
          % (t["done_events"], t["revert_events"], t["zh_doc_missing"]))
    print("\n当前 state 分布：")
    for k, v in out["state_distribution"].items():
        print("  %-22s %d" % (k, v))
    print("\n历史最高节点：")
    for k, v in out["highest_node_reached"].items():
        print("  %-10s %d" % (k, v))
    print("\n曾达 done 的条目，现今 state：")
    for k, v in out["reached_done_by_current_state"].items():
        print("  %-22s %d" % (k, v))
    print("\nrevert 归因（前 40 字）：")
    for k, v in out["revert_by_cause"].items():
        print("  %-42s %d" % (k or "(空)", v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
