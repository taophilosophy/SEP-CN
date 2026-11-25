#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""置空翻译历史（用户 2026-11-25 追加授权：“允许置空翻译历史”）。

范围（与置空正文互补）：
  * journal/<letter>/<slug>.ndjson → 清空为 0 字节（事件历史全部移除；文件保留，
    条目仍在账内，seq 从 1 重新计）。
  * `tasks.steps` → 置 []（过程凭证清空）；保留 state（`cleared`）、version_pin、
    zh_doc、created_at、state_migrated 等非过程字段。
  * `state/axis/*` 六轴工单 → 删除（旧译文的工作产物；重译时由 `--init` 重建，
    留着会让门禁对着不存在的正文误判）。
不在此范围：`en/`、`yuanwen/`、`baseline/`（源钉与登记）、`tasks` 的版本钉。

配套：`rules/epoch.json` 与 `tools/epoch_lib.py` 一并撤除（历史既已为空，纪元
过滤器失去对象）；ADR-0081 由 ADR-0082 取代。

用法: python tools/wipe_history.py [--apply]
退出码: 0 完成。
"""
import argparse
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools.common import write_text_verified, write_json_verified  # noqa: E402

REPORT = os.path.join(ROOT, "specs", "060-six-axis-quality-gates", "results",
                      "wipe-history-2026-11-25.json")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    jfiles = []
    for dirpath, _, files in os.walk(os.path.join(ROOT, "journal")):
        for fn in files:
            if fn.endswith(".ndjson"):
                jfiles.append(os.path.join(dirpath, fn))

    tasks, step_total, kept = [], 0, []
    for dirpath, _, files in os.walk(os.path.join(ROOT, "tasks")):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8") as f:
                    t = json.load(f)
            except (OSError, ValueError):
                continue
            if not isinstance(t, dict) or str(t.get("kind") or "") != "retranslate":
                continue
            if t.get("state") != "cleared":
                kept.append((t.get("slug"), t.get("state")))
                continue
            tasks.append((p, t, len(t.get("steps") or [])))
            step_total += len(t.get("steps") or [])

    axis = os.path.join(ROOT, "state", "axis")
    axis_files = [os.path.join(axis, x) for x in os.listdir(axis)] if os.path.isdir(axis) else []

    print("journal %d 文件｜tasks %d 条（steps %d）｜state/axis %d 文件｜非 cleared 跳过 %d"
          % (len(jfiles), len(tasks), step_total, len(axis_files), len(kept)))
    if not args.apply:
        print("干跑：未写任何文件（--apply 执行）")
        return 0

    for p in jfiles:
        write_text_verified(p, "")
    for p, t, _n in tasks:
        t["steps"] = []
        write_json_verified(p, t)
    for p in axis_files:
        try:
            os.remove(p)
        except OSError:
            pass

    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    write_json_verified(REPORT, {
        "schema": "wipe-history/v1",
        "reason": "用户 2026-11-25 追加授权：允许置空翻译历史",
        "journal_files": len(jfiles), "tasks": len(tasks), "steps_removed": step_total,
        "axis_files_removed": len(axis_files), "skipped": kept[:20],
        "adr": "0082",
    })
    print("已清空：journal %d、steps %d、axis %d；报告 %s"
          % (len(jfiles), step_total, len(axis_files), os.path.relpath(REPORT, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
