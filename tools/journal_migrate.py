# -*- coding: utf-8 -*-
"""事件日志一次性迁移（ADR-0068 W1）：tasks/*.json 的 steps+state → journal/<letter>/<slug>.ndjson。

只读换算：本脚本**只读 tasks/，不改任何任务文件**；产物写入 journal/（新目录）。
忠实原则（P5/P6）：不推断中间节点，无法归类的 step 保留在 tasks 原文件，不硬造事件。
无历史（steps 无阶段节点）的条目合成 import{synthetic:true}，basis 记清来源。

节点映射（task_ops 步名 → pipeline 节点 id；ADR-0068 三存储一视图）：
  s0→s0, draft→draft, s1→s1, s2→s2, s24→s2.4, s25→global, s3→S3,
  r1→R1, r2→R2, r3→R3
非节点动作：
  clear / done → import{synthetic:true, basis:clear|done}
  revert-state / reopen / rework-* → rework{from_node, reason}
  block / unblock / source-audit / 其他 → 跳过（保留在 tasks）

用法: python tools/journal_migrate.py [--dry-run] [--json PATH]
退出码: 0 成功；1 判据未满足；2 输入缺失。
"""
import argparse
import io
import json
import os
import re
import sys
from collections import Counter

if getattr(sys.stdout, "encoding", None) and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASKS = os.path.join(ROOT, "tasks")
JOURNAL = os.path.join(ROOT, "journal")

NODE_MAP = {
    "s0": "s0", "draft": "draft", "s1": "s1", "s2": "s2",
    "s24": "s2.4", "s25": "global", "audit": "global", "s3": "S3",
    "r1": "R1", "r2": "R2", "r3": "R3",
}
ENTRY_KINDS = ("retranslate", "update")


def _map_step(step_name, evidence=""):
    """把 step 名映射为 (type, payload)；无法映射返回 None（跳过）。"""
    if step_name in NODE_MAP:
        return ("pass", {"node": NODE_MAP[step_name], "gate": []})
    if step_name == "revert-state":
        # 从 evidence "回退到 X" 提取目标态（解析，非推断），映射为 rework 的 from_node
        to = None
        m = re.search(r"回退到\s*([A-Za-z0-9._]+)", evidence or "")
        if m:
            to = {"s2.4_termchecked": "s2.4", "s2.5_checked": "global"}.get(m.group(1))
        return ("rework", {"from_node": to})
    if step_name == "reopen":
        return ("rework", {"from_node": None})
    if step_name and step_name.startswith("rework"):
        return ("rework", {"from_node": None})
    # clear / done / reset / block / unblock / source-audit / 其他 → 跳过：
    # done 是派生量（饱和由 pass 集合推导，不落盘）；clear 是入口动作非节点事件。
    return None


def _derive(task):
    """把单个任务派生为事件列表（不含 done/clear 等非节点动作）。"""
    events = []
    seq = 0
    pin = task.get("version_pin")
    if pin and pin.get("sha256"):
        seq += 1
        events.append({"seq": seq, "at": task.get("created_at", ""), "actor": "migrate",
                       "type": "lock", "attempt": "main",
                       "sha256": pin["sha256"],
                       "pubinfo_date": pin.get("pubinfo_date"),
                       "edition": pin.get("archive_edition")})

    has_node = False
    for s in task.get("steps", []):
        m = _map_step(s.get("step"), s.get("evidence", ""))
        if m is None:
            continue
        seq += 1
        ev = {"seq": seq, "at": s.get("at", ""), "actor": s.get("actor", "migrate"),
              "type": m[0], "attempt": "main"}
        ev.update(m[1])
        if m[0] == "pass":
            has_node = True
        if m[0] == "rework":
            ev["reason"] = (s.get("evidence") or "")[:200]
        events.append(ev)

    if not has_node:
        # 无阶段记录：合成快照，basis 记 state（P6 承认历史不可考，不推断）
        seq += 1
        events.append({"seq": seq, "at": task.get("created_at", ""), "actor": "migrate",
                       "type": "import", "synthetic": True,
                       "basis": "state:%s" % task.get("state", "?"), "attempt": "main"})
    return events


def _iter_tasks():
    for dirpath, _, filenames in os.walk(TASKS):
        if os.path.basename(dirpath) == "manifests":
            continue
        for fn in filenames:
            if not fn.endswith(".json"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, "rb") as f:
                    d = json.loads(f.read().decode("utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            if not (isinstance(d, dict) and d.get("slug") and d.get("kind") in ENTRY_KINDS):
                continue
            yield d, p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    if not os.path.isdir(TASKS):
        print("输入缺失: tasks/", file=sys.stderr)
        return 2

    stat = Counter()
    done_slugs = []
    synthetic_slugs = []
    total_events = 0

    if not args.dry_run and os.path.exists(JOURNAL):
        # 只清 ndjson 事件文件，保留 README.md（索引，layout.json 的 index 指向它）
        for dirpath, _, filenames in os.walk(JOURNAL):
            for fn in filenames:
                if fn.endswith(".ndjson"):
                    os.remove(os.path.join(dirpath, fn))

    for task, _ in _iter_tasks():
        events = _derive(task)
        total_events += len(events)
        stat["tasks"] += 1
        slug = task["slug"]
        letter = slug[0] if slug and slug[0].isalnum() else "0"
        # done 在位：扫原始 steps 的 done step（去重）；done 是派生量，不落 journal
        if any(s.get("step") == "done" for s in task.get("steps", [])):
            done_slugs.append(slug)
        if any(e.get("synthetic") for e in events):
            synthetic_slugs.append(slug)

        if args.dry_run:
            continue
        d = os.path.join(JOURNAL, letter)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, slug + ".ndjson"), "w", encoding="utf-8", newline="\n") as f:
            for e in events:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")

    report = {
        "tasks": stat["tasks"],
        "events": total_events,
        "done": len(done_slugs),
        "synthetic": len(synthetic_slugs),
        "done_slugs": done_slugs,
        "synthetic_slugs": synthetic_slugs,
    }
    print("任务 %d｜事件 %d｜done 在位 %d｜synthetic %d"
          % (report["tasks"], report["events"], report["done"], report["synthetic"]))

    if args.json:
        dst = args.json if os.path.isabs(args.json) else os.path.join(ROOT, args.json)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8", newline="\n") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
            f.write("\n")

    # W1 判据（词条任务口径；journal 不迁 glossary-maintenance/daily-check 等例行任务）：
    # 事件数 ≥ 4993、done 在位 ≥ 385、synthetic ≥ 766（reset_audit 的 768 含 2 非词条任务）
    ok = (report["events"] >= 4993 and report["done"] >= 385
          and report["synthetic"] >= 766)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
