# -*- coding: utf-8 -*-
"""阶段 1.2 复核凭证：旧池对新页面重判（specs/062 R-5）。

背景：`page-scan-all.json` 的 `--build` 重冻会覆盖池目录，导致“旧池 judge”
（pool 1780／gap 48／stale 45）只剩叙述、无落盘凭证。本脚本把第 43 批池
（802db20da）导出到临时目录后，以内存替换 `assembly_pool.load_pool`，
对当前 en/ 页面重判一次，凭证落 `results/phase12-oldpool-judge.json`。

用法：
  git archive 802db20da baseline/en-template/assembly-patches | tar -x -C <tmp>
  python specs/062-phase12-recheck/bin/oldpool_judge.py --pool-dir <tmp>/baseline/en-template/assembly-patches

只读判官：不改 en/、不改池、不写 baseline。
"""
import argparse
import io
import json
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "specs", "053-en-template-audit", "bin"))

import page_assemble as PA  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool-dir", required=True,
                    help="旧池目录（含 <slug>.json）")
    ap.add_argument("--out", default=os.path.join(
        ROOT, "specs", "062-phase12-recheck", "results",
        "phase12-oldpool-judge.json"))
    args = ap.parse_args(argv)

    pool_dir = os.path.abspath(args.pool_dir)

    def load_old(slug):
        p = os.path.join(pool_dir, "%s.json" % slug)
        if not os.path.exists(p):
            return []
        return json.load(io.open(p, encoding="utf-8"))["patches"]

    PA.POOL.load_pool = load_old   # 内存替换，不落盘
    lib = PA.Library()
    slugs = sorted(lib.base)
    counts = Counter()
    entries = []
    for i, s in enumerate(slugs, 1):
        try:
            r = PA.judge(lib, s)
        except Exception as ex:                     # 单件异常不中止全量
            r = {"slug": s, "status": "gap", "why": "error: %s" % ex}
        counts[r.get("status", "gap")] += 1
        entries.append({k: r[k] for k in ("slug", "status", "why")
                        if k in r})
        if i % 250 == 0:
            sys.stderr.write("[oldpool] %d/%d ...\n" % (i, len(slugs)))

    report = {"schema": "sep-cn-oldpool-judge/1",
              "pool_dir": pool_dir,
              "pool_files": len([f for f in os.listdir(pool_dir)
                                 if f.endswith(".json")]) if os.path.isdir(pool_dir) else 0,
              "total": len(slugs), "counts": dict(counts),
              "entries": entries}
    with io.open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(report, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({"total": len(slugs), "counts": dict(counts),
                      "out": args.out}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
