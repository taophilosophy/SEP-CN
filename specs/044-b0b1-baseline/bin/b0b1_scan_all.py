# -*- coding: utf-8 -*-
"""B0+B1 全库统一扫描（specs/044 落地，ADR-0072 边界内只读审计）。

求值视图（specs/044 §1，2026-11-18 修正）：
  B0 在**转换输入视图**（en ⊕ patches）求值——b0_ok 内部先 apply_en_patches，
  与 yuanwen.convert_entry 同源；B1 的 I3 源流亦用补丁后 HTML（html_text
  apply_patches=True）。不写 en/、不改 yuanwen/、不产译文。

三态（失败件对账 en-errata.md）：
  known-errata = 失败件已在 en-errata.md 登记；
  new          = 失败件未登记（新发现）。
（"已补丁覆盖"态由交集验证承担：补丁件补丁前/后 B0 对比，见 state/verify_patch_view.py 留档。）

用法: python -I specs/044-b0b1-baseline/bin/b0b1_scan_all.py [--json PATH]
退出码: 0 扫描完成；1 输入异常。
"""
import argparse
import io
import json
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools.common import repo_path  # noqa: E402
from verify_b0b1 import check_slug  # noqa: E402

_HDR = {"slug", "位置", "上游原文", "缺陷定性", "参考读法", "中文承载", "凭证"}


def load_errata_slugs():
    """读 en-errata.md 表格第一列，返回已登记 slug 集合。"""
    path = repo_path("specs", "001-sep-sync-pipeline", "results", "en-errata.md")
    if not os.path.exists(path):
        return set()
    out = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^\|\s*([a-z0-9][a-z0-9-]*)\s*\|", line)
            if m and m.group(1) not in _HDR:
                out.add(m.group(1))
    return out


def scan():
    d = json.load(open(repo_path("baseline", "entries.json"), encoding="utf-8"))
    slugs = [e["slug"] for e in d.get("entries", [])]
    rows = []
    for k, slug in enumerate(slugs):
        rows.append(check_slug(slug))
        if (k + 1) % 200 == 0:
            sys.stderr.write("[b0b1_scan] 进度 %d/%d\n" % (k + 1, len(slugs)))
    errata = load_errata_slugs()
    b0_fail = [r for r in rows if not r["b0"]]
    b1_fail = [r for r in rows if not r["b1"]]
    both_ok = [r for r in rows if r["b0"] and r["b1"]]
    asym = [r for r in rows if r.get("b1_token_asym")]
    for r in b0_fail:
        r["b0_status"] = "known-errata" if r["slug"] in errata else "new"
    for r in b1_fail:
        r["b1_status"] = "known-errata" if r["slug"] in errata else "new"
    summary = {
        "schema": "sep-cn-b0b1-scan/2",
        "total": len(slugs),
        "both_ok": len(both_ok),
        "b0_fail": len(b0_fail),
        "b1_fail": len(b1_fail),
        "b1_token_asym": len(asym),
        "b0_known_errata": sum(1 for r in b0_fail if r["b0_status"] == "known-errata"),
        "b0_new": sum(1 for r in b0_fail if r["b0_status"] == "new"),
        "b1_known_errata": sum(1 for r in b1_fail if r["b1_status"] == "known-errata"),
        "b1_new": sum(1 for r in b1_fail if r["b1_status"] == "new"),
        "b0_predicate_fail_count": dict(sorted(Counter(
            p for r in b0_fail for p in (r.get("b0_failed") or [])).items())),
        "errata_slugs_loaded": len(errata),
    }
    return summary, rows


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None)
    args = ap.parse_args(argv)
    summary, rows = scan()
    print("B0+B1 全库扫描（求值视图＝补丁后）")
    print("  总 %d ｜ 双过 %d ｜ B0 失败 %d（已知勘误 %d / 新发现 %d）｜ "
          "B1 失败 %d（已知勘误 %d / 新发现 %d）｜ asym 判据不适用 %d"
          % (summary["total"], summary["both_ok"],
             summary["b0_fail"], summary["b0_known_errata"], summary["b0_new"],
             summary["b1_fail"], summary["b1_known_errata"], summary["b1_new"],
             summary["b1_token_asym"]))
    print("  B0 失败谓词:", json.dumps(summary["b0_predicate_fail_count"], ensure_ascii=False))
    print("  勘误表已登记 slug 数:", summary["errata_slugs_loaded"])
    print("\nB0 失败（[已知勘误]/[新发现]）:")
    for r in rows:
        if not r["b0"]:
            print("  [%s] %-30s %s" % (r.get("b0_status"), r["slug"],
                                       r.get("b0_failed") or r.get("b0_error")))
    print("\nB1 失败（[已知勘误]/[新发现]）:")
    for r in rows:
        if not r["b1"]:
            print("  [%s] %-30s pin_bad=%s token_diff=%s"
                  % (r.get("b1_status"), r["slug"], bool(r.get("b1_pin_bad")),
                     json.dumps(r.get("b1_token_diff"), ensure_ascii=False)[:120]
                     if r.get("b1_token_diff") else "无"))
    out = {"summary": summary, "rows": rows}
    path = args.json or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "results", "b0b1-scan-all.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("\n落盘:", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
