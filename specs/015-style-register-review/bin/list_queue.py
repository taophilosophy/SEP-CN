#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""枚举 done 词条生成复核队列（只读元数据，不做任何语体判定）。

用法: python specs/015-style-register-review/bin/list_queue.py [--out results/queue.jsonl]

输出 JSONL：{slug, path, bytes, done_at, letter}，按 done_at 升序。
语体结论一律由复核人通读后写入 results/verdicts.jsonl，本脚本不产生 verdict。
"""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))


def main(argv=None):
    argv = argv or sys.argv[1:]
    out = os.path.join(ROOT, "specs/015-style-register-review/results/queue.jsonl")
    if "--out" in argv:
        out = argv[argv.index("--out") + 1]
    rows = []
    for fp in glob.glob(os.path.join(ROOT, "tasks/*/*.json")):
        try:
            with open(fp, encoding="utf-8") as fh:
                task = json.load(fh)
        except (OSError, ValueError):
            continue
        if not isinstance(task, dict) or task.get("state") != "done":
            continue
        zh = task.get("zh_doc") or ""
        full = os.path.join(ROOT, zh) if zh else ""
        done_at = next((str(s.get("at") or "") for s in reversed(task.get("steps") or [])
                        if s.get("step") == "done"), "")
        rows.append({
            "slug": task.get("slug"),
            "path": zh,
            "bytes": os.path.getsize(full) if zh and os.path.exists(full) else 0,
            "done_at": done_at,
            "letter": (zh.split("/")[0] if "/" in zh else ""),
        })
    rows.sort(key=lambda r: (r["done_at"], r["slug"] or ""))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("wrote %d rows -> %s" % (len(rows), os.path.relpath(out, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
