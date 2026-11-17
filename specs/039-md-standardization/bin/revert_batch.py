# -*- coding: utf-8 -*-
"""P8 批量受控回退驱动（specs/039，ADR-0063 决策 8）。

消费 `results/revert-ledger-20261117.json` 的绿行（三轴机检通过者），逐件调用
`task_ops.revert_state --to s2.4_termchecked`；红行跳过并留清单（须先修再退）。
默认 dry-run；`--execute` 才写状态。幂等：已处于 s2.4_termchecked 的任务跳过。

回退只置状态位次（append-only 记 revert-state 步），**不迁正文**；重走由翻译会话
按 s24 三轴 → s25（三轴机检已并挂）→ s3 → r 链执行。

用法:
  python specs/039-md-standardization/bin/revert_batch.py            # dry-run
  python specs/039-md-standardization/bin/revert_batch.py --execute  # 执行
  python specs/039-md-standardization/bin/revert_batch.py --execute --limit 3  # 试金石
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from tools import task_ops  # noqa: E402

REASON = ("中文体例归一全量回退（specs/039 P8，ADR-0063）：s2.4 三轴硬门上线后"
          "在途件一律回退重走；机检凭证 results/revert-ledger-20261117.json")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--actor", default="P8-revert-20261117")
    args = ap.parse_args(argv)

    lpath = os.path.join(ROOT, "specs", "039-md-standardization", "results",
                         "revert-ledger-20261117.json")
    ledger = json.load(open(lpath, encoding="utf-8"))
    green = [r for r in ledger["rows"] if r["status"] == "green"]
    red = [r for r in ledger["rows"] if r["status"] != "green"]
    if args.limit:
        green = green[:args.limit]

    done, skipped, failed = [], [], []
    for r in green:
        slug = r["slug"]
        task = task_ops.load_task(slug)
        if not task:
            skipped.append((slug, "no-task")); continue
        if task["state"] == "s2.4_termchecked":
            skipped.append((slug, "already-reverted")); continue
        if not args.execute:
            done.append(slug); continue
        try:
            task_ops.revert_state(slug, "s2.4_termchecked", REASON, actor=args.actor)
            done.append(slug)
        except Exception as exc:  # 显式失败，禁静默
            failed.append((slug, repr(exc)[:160]))

    out = {"mode": "execute" if args.execute else "dry-run",
           "ledger_total": ledger["total"], "green": len(ledger["rows"]) - len(red),
           "red_skipped": len(red), "reverted": len(done), "skipped": len(skipped),
           "failed": failed, "red_slugs": [r["slug"] for r in red],
           "skipped_detail": skipped[:40]}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
