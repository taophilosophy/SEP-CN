#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""状态重放诊断：从 journal 折叠每个词条的状态，与 tasks 的 state 逐条对照（ADR-0080）。

定位：**诊断器，不是门禁**。ADR-0068 说“日志为事实、状态为视图”，本工具检验这条
主张的可操作边界。2026-11-25 复核（1200 条）实测：严格重放不能 100% 复现视图，
原因已分类且可归因——

  * cleared 不是事件（clear 动作经 task_ops 写 steps，不落 journal）→ 只能由
    import 的 basis=state:cleared 或“无 pass 且无正文”间接识别；
  * done 不是事件（派生量）→ 只能由强制集 pass 判定；
  * 回补 pass 不迁移状态（specs/052、ADR-0075：判据收紧后重算记账）→ 日志会
    “跑在”视图前面；
  * 跨机收编的 import 快照（specs/052）承认历史不可考，只给当时状态。

因此命名迁移的验收不依赖重放，而用“映射双档”：迁移前后逐条对照 == state_aliases
的像；重放只作漂移体检（本工具退出码 0，异常分类列在报告里）。

用法: python tools/replay_state.py [--json] [--limit N]
退出码: 0 完成（诊断器恒 0）；2 输入缺失。
"""
import argparse
import json
import os
import sys
from collections import Counter

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools import naming_lib  # noqa: E402
from tools.journal_lib import NODE_TO_STATE, read_events  # noqa: E402


def _order():
    """pipeline 的节点链 → 状态序（用于判定“日志在前/视图在前”）。"""
    with open(os.path.join(ROOT, "rules", "pipeline.json"), "rb") as f:
        pipe = json.loads(f.read().decode("utf-8"))
    nodes = {n["id"]: n for n in pipe.get("nodes", [])}
    heads = [i for i in nodes if not nodes[i].get("prev")]
    chain, cur = [], heads[0] if heads else None
    while cur:
        chain.append(cur)
        nxt = [i for i in nodes if nodes[i].get("prev") == cur]
        cur = nxt[0] if len(nxt) == 1 else None
    return [NODE_TO_STATE[n] for n in chain if n in NODE_TO_STATE]


ORDER = _order()
_RANK = {s: i for i, s in enumerate(ORDER)}


def replay(slug):
    """折叠事件 → (state, 依据列表)。state 为新状态名或 pending／cleared／None。"""
    cur, why = None, []
    for ev in sorted(read_events(slug), key=lambda e: e.get("seq", 0)):
        t = ev.get("type")
        if t == "import":
            st = ev.get("state_at_import")
            if not st:
                basis = str(ev.get("basis") or "")
                st = basis.split(":", 1)[1] if basis.startswith("state:") else None
            if st:
                cur = naming_lib.normalize_state(st)
                why.append("import:%s" % st)
        elif t == "pass":
            nid = naming_lib.try_identifier(ev.get("node"))
            st = NODE_TO_STATE.get(nid) if nid else None
            if st:
                cur = st
                why.append("pass:%s" % nid)
        elif t == "rework":
            fn = naming_lib.try_identifier(ev.get("from_node")) if ev.get("from_node") else None
            cur = NODE_TO_STATE.get(fn) if fn in NODE_TO_STATE else "pending"
            why.append("rework:%s" % (fn or "reopen"))
    return cur, why


def classify(state, cur):
    if state == cur:
        return "match"
    if cur is None:
        return "no-journal-evidence"
    if state in ("pending", "cleared", "done") or cur in ("pending", "cleared", "done"):
        if state == "done":
            return "done-not-evented"
        return "terminal-vs-node"
    a, b = _RANK.get(state), _RANK.get(cur)
    if a is None or b is None:
        return "unknown-state"
    if b > a:
        return "state-behind-journal（多为回补 pass 不迁移状态）"
    return "state-ahead-of-journal（缺 pass 事件）"


def iter_tasks():
    tdir = os.path.join(ROOT, "tasks")
    for dirpath, _, files in os.walk(tdir):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
                    t = json.load(f)
            except (OSError, ValueError):
                continue
            if isinstance(t, dict) and t.get("state") \
                    and str(t.get("kind") or "") == "retranslate":
                yield t


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--limit", type=int, default=5, help="每类列出前 N 条")
    args = ap.parse_args(argv)

    if not os.path.isdir(os.path.join(ROOT, "tasks")):
        print("输入缺失: tasks/", file=sys.stderr)
        return 2

    rows, classes = [], Counter()
    for t in iter_tasks():
        state = naming_lib.normalize_state(t["state"])
        cur, why = replay(t["slug"])
        cls = classify(state, cur)
        classes[cls] += 1
        rows.append({"slug": t["slug"], "state": state, "replay": cur,
                     "class": cls, "last": why[-3:]})

    print("重放诊断：%d 条｜%s" % (len(rows), json.dumps(dict(classes), ensure_ascii=False)))
    for cls in classes:
        if cls == "match":
            continue
        ex = [r for r in rows if r["class"] == cls][:args.limit]
        for r in ex:
            print("  [%s] %-24s state=%-16s replay=%-16s %s"
                  % (cls, r["slug"], r["state"], r["replay"], ",".join(r["last"])))
    if args.json:
        print(json.dumps({"total": len(rows), "classes": dict(classes), "rows": rows},
                         ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
