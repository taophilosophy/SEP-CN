# -*- coding: utf-8 -*-
"""B0 全库遍历（specs/044 落地，ADR-0072 决策 1）：对全部词条求 B0 十谓词，产出疏漏清单。

只读审计：不写 en/、不改 yuanwen/、不动 baseline、不产译文、不改勘误表。
“不进行全量翻译”边界：本脚本只判 HTML 格式，不做任何翻译。

用法:
  python -I specs/044-b0b1-baseline/bin/b0_scan_all.py [--json PATH]
退出码: 0 扫描完成（有 B0 失败也是 0——失败是发现不是错误）；1 输入异常。
"""
import argparse
import io
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # bin 目录，含 verify_b0b1
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools.common import repo_path  # noqa: E402
from verify_b0b1 import b0_ok  # noqa: E402


def scan():
    d = json.load(open(repo_path("baseline", "entries.json"), encoding="utf-8"))
    slugs = [e["slug"] for e in d.get("entries", [])]
    failed, errors = [], []
    pred_count = Counter()
    for slug in slugs:
        r = b0_ok(slug)
        if r.get("b0"):
            continue
        if r.get("error"):
            errors.append({"slug": slug, "error": r["error"]})
        else:
            failed.append({"slug": slug, "failed": r.get("failed", [])})
            pred_count.update(r.get("failed", []))
    summary = {
        "schema": "sep-cn-b0-scan/1",
        "total": len(slugs),
        "b0_pass": len(slugs) - len(failed) - len(errors),
        "b0_fail": len(failed),
        "no_snapshot": len(errors),
        "predicate_fail_count": dict(sorted(pred_count.items())),
    }
    return summary, failed, errors


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None,
                    help="机读结果落盘路径（默认 specs/044/results/b0-scan-all.json）")
    args = ap.parse_args(argv)
    summary, failed, errors = scan()
    print("B0 全库遍历：总 %d，通过 %d，失败 %d，无快照 %d"
          % (summary["total"], summary["b0_pass"], summary["b0_fail"],
             summary["no_snapshot"]))
    print("失败谓词分布:", json.dumps(summary["predicate_fail_count"], ensure_ascii=False))
    if failed:
        print("\nB0 失败词条（前 40）：")
        for f in failed[:40]:
            print("  %-30s %s" % (f["slug"], f["failed"]))
    if errors:
        print("\n无快照词条（前 20）：", [e["slug"] for e in errors[:20]])
    out = {"summary": summary, "failed": failed, "no_snapshot": errors}
    path = args.json or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "results", "b0-scan-all.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("\n落盘:", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
