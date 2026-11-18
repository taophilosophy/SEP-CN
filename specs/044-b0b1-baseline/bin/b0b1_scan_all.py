# -*- coding: utf-8 -*-
"""B0+B1 全库统一扫描（specs/044 落地，ADR-0072 边界内只读审计）。

求值视图（specs/044 §1.0，2026-11-18 修正）：
  B0 在**转换输入视图**（en ⊕ patches）求值——b0_ok 内部先 apply_en_patches，
  与 yuanwen.convert_entry 同源；B1 的 I3 源流亦用补丁后 HTML（html_text
  apply_patches=True）。不写 en/、不改 yuanwen/、不产译文。
  交集验证（补丁前/后 B0 对比）见 bin/verify_patch_intersection.py。

对账律（doctrine 10，ADR-0073）：
  失败清单必须 join **全部已知账**，否则"新发现"里混着已定性项，账不可消费。
  已知账共两本：
    ① `baseline/en-errata/en-errata.md`           —— 上游文字层疏漏（translation-side，ADR-0076 迁址）
    ② `specs/039/results/i3-deep-*.json`          —— 已逐件定性的转换器缺陷/合法移位
  故 B1 失败三态：known-errata / known-converter / new；`b1_new` 必须为 0
  才算账本闭合（未闭合时逐条列出 `b1_unaccounted`）。

用法: python -I specs/044-b0b1-baseline/bin/b0b1_scan_all.py [--json PATH]
退出码: 0 扫描完成；1 输入异常；2 账本未闭合（存在 new 且未被任何账覆盖）。
"""
import argparse
import glob
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

# 转换器账里"已被逐件定性"的判据名（i3-deep issues[].rule）
_CONVERTER_RULES = ("text-stream-diff", "math-asymmetric-diff", "no-baseline")


def load_errata_slugs():
    """读 en-errata.md 表格第一列，返回 {slug: kind}。

    kind 区分两种登记性质（对账精度所需）：
      "defect"    —— 确证疏漏（文字层误植/漏字），译文按参考读法承载；
      "ambiguity" —— 判据歧义（机检与语义不一致，留待人审裁定），登记在案但
                     **不等于缺陷成立**。二者混为一谈会把"可能是判据误报"读成
                     "已知缺陷"，故单列。
    """
    path = repo_path("baseline", "en-errata", "en-errata.md")
    if not os.path.exists(path):
        return {}
    out = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^\|\s*([a-z0-9][a-z0-9-]*)\s*\|", line)
            if not m or m.group(1) in _HDR:
                continue
            slug = m.group(1)
            kind = "ambiguity" if ("判据歧义" in line or "误报" in line) else "defect"
            # 同一 slug 若既有一处确证疏漏又有一处歧义，以确证疏漏为准（更强结论）
            if out.get(slug) != "defect":
                out[slug] = kind
    return out


def load_converter_ledger():
    """读 specs/039 最新深档报告，返回 (by_rule, path, meta)。

    该报告是 specs/039 §3/§5 逐件定性后的机读快照：text-stream-diff 47 件
    （三族转换器缺陷已修 + 白名单合法移位）、math-asymmetric-diff 273 件
    （判据不适用且有可报字母差）、no-baseline 2 件（孤儿镜像）。

    **层级注意**：报告顶层 `math_asymmetric=320` 是"判据不适用"总面（只存计数），
    而 issues 里的 `math-asymmetric-diff=273` 是其中有可报字母差的子集。
    故 320 = 273（有差可报）+ 47（两侧对称、无差可报）。交叉核对必须按层对照，
    直接拿 273 与扫描的 320 求差集会把 47 件误读成"仅扫描有"。
    """
    cands = sorted(glob.glob(repo_path(
        "specs", "039-md-standardization", "results", "i3-deep-*.json")))
    if not cands:
        return {}, None, {}
    path = cands[-1]
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    by_rule = {}
    for issue in d.get("issues", []):
        by_rule.setdefault(issue.get("rule"), set()).add(issue.get("slug"))
    meta = {"math_asymmetric_total": d.get("math_asymmetric"),
            "deep_checked": d.get("deep_checked"),
            "issue_total": d.get("issue_total")}
    return by_rule, path, meta


def scan():
    d = json.load(open(repo_path("baseline", "entries.json"), encoding="utf-8"))
    slugs = [e["slug"] for e in d.get("entries", [])]
    rows = []
    for k, slug in enumerate(slugs):
        rows.append(check_slug(slug))
        if (k + 1) % 200 == 0:
            sys.stderr.write("[b0b1_scan] 进度 %d/%d\n" % (k + 1, len(slugs)))

    errata = load_errata_slugs()
    ledger, ledger_path, ledger_meta = load_converter_ledger()
    conv_all = set()
    for rule in _CONVERTER_RULES:
        conv_all |= ledger.get(rule, set())
    conv_text = ledger.get("text-stream-diff", set())
    conv_asym = ledger.get("math-asymmetric-diff", set())

    b0_fail = [r for r in rows if not r["b0"]]
    b1_fail = [r for r in rows if not r["b1"]]
    both_ok = [r for r in rows if r["b0"] and r["b1"]]
    asym = [r for r in rows if r.get("b1_token_asym")]
    with_diff = {r["slug"] for r in asym if r.get("b1_token_diff")}

    # --- 四态：确证勘误 → 判据歧义（登记待裁定）→ 已知转换器账 → 新发现（对账律）---
    def _errata_status(slug):
        kind = errata.get(slug)
        if kind == "defect":
            return "known-errata"
        if kind == "ambiguity":
            return "known-errata-ambiguity"
        return None

    for r in b0_fail:
        r["b0_status"] = _errata_status(r["slug"]) or "new"
    for r in b1_fail:
        st = _errata_status(r["slug"])
        if st:
            r["b1_status"] = st
        elif r["slug"] in conv_all:
            r["b1_status"] = "known-converter"
            r["b1_ledger_rule"] = sorted(
                rule for rule in _CONVERTER_RULES
                if r["slug"] in ledger.get(rule, set()))
        else:
            r["b1_status"] = "new"

    b1_new = [r for r in b1_fail if r["b1_status"] == "new"]
    b1_fail_slugs = {r["slug"] for r in b1_fail}

    summary = {
        "schema": "sep-cn-b0b1-scan/3",
        "total": len(slugs),
        "both_ok": len(both_ok),
        "b0_fail": len(b0_fail),
        "b1_fail": len(b1_fail),
        "b1_token_asym": len(asym),
        "b0_known_errata": sum(1 for r in b0_fail if r["b0_status"] == "known-errata"),
        "b0_new": sum(1 for r in b0_fail if r["b0_status"] == "new"),
        "b1_known_errata": sum(1 for r in b1_fail if r["b1_status"] == "known-errata"),
        "b1_known_converter": sum(1 for r in b1_fail if r["b1_status"] == "known-converter"),
        "b1_new": len(b1_new),
        "b0_predicate_fail_count": dict(sorted(Counter(
            p for r in b0_fail for p in (r.get("b0_failed") or [])).items())),
        "errata_slugs_loaded": len(errata),
        # 对账律凭证：B1 失败集与 specs/039 text-stream-diff 账的双向差集
        "converter_ledger": {
            "path": os.path.relpath(ledger_path, os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
            .replace("\\", "/") if ledger_path else None,
            "rules_loaded": {k: len(v) for k, v in sorted(ledger.items())},
            "b1_fail_inter_039text": len(b1_fail_slugs & conv_text),
            "b1_fail_only": sorted(b1_fail_slugs - conv_text),
            "ledger_only": sorted(conv_text - b1_fail_slugs),
        },
        # asym 与 039 账的**分层**对照（见 load_converter_ledger 的层级说明）：
        #   总面 = 判据不适用件数（计数核对）
        #   diff 面 = 其中有可报字母差者（集合双向核对，与 039 的 273 对齐）
        #   残差面 = 两侧对称、无差可报者（= 总面 − diff 面，只按计数核对）
        "asym_crosscheck": {
            "scan_asym_total": len(asym),
            "scan_asym_with_diff": len(with_diff),
            "ledger_asym_total": ledger_meta.get("math_asymmetric_total"),
            "ledger_asym_diff": len(conv_asym),
            "total_match": len(asym) == (ledger_meta.get("math_asymmetric_total") or -1),
            "diff_face_scan_only": sorted(with_diff - conv_asym),
            "diff_face_ledger_only": sorted(conv_asym - with_diff),
            "residual_sym_no_diff": len(asym) - len(with_diff),
        },
        "b1_unaccounted": sorted(r["slug"] for r in b1_new),
    }
    return summary, rows


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None)
    args = ap.parse_args(argv)
    summary, rows = scan()
    print("B0+B1 全库扫描（求值视图＝补丁后；对账律＝勘误表 ∪ 转换器账）")
    print("  总 %d ｜ 双过 %d ｜ B0 失败 %d（已知勘误 %d / 新发现 %d）"
          % (summary["total"], summary["both_ok"],
             summary["b0_fail"], summary["b0_known_errata"], summary["b0_new"]))
    print("  B1 失败 %d（已知勘误 %d / 已知转换器账 %d / 新发现 %d）｜ asym 判据不适用 %d"
          % (summary["b1_fail"], summary["b1_known_errata"],
             summary["b1_known_converter"], summary["b1_new"], summary["b1_token_asym"]))
    print("  B0 失败谓词:", json.dumps(summary["b0_predicate_fail_count"], ensure_ascii=False))
    print("  勘误表已登记 slug 数:", summary["errata_slugs_loaded"])
    cc = summary["converter_ledger"]
    print("  转换器账 %s：%s" % (cc["path"], json.dumps(cc["rules_loaded"], ensure_ascii=False)))
    print("  B1 失败 ∩ 039-text-stream-diff = %d ｜ 仅 B1 = %s ｜ 仅 039 = %s"
          % (cc["b1_fail_inter_039text"],
             cc["b1_fail_only"] or "无", cc["ledger_only"] or "无"))
    ac = summary["asym_crosscheck"]
    print("  asym 分层核对：总面 扫描 %d ／ 039 账 %s（一致=%s）｜ diff 面 扫描 %d ／ 039 %d"
          "（仅扫描 %s ／ 仅账 %s）｜ 残差对称面无差 %d"
          % (ac["scan_asym_total"], ac["ledger_asym_total"], ac["total_match"],
             ac["scan_asym_with_diff"], ac["ledger_asym_diff"],
             ac["diff_face_scan_only"] or "无", ac["diff_face_ledger_only"] or "无",
             ac["residual_sym_no_diff"]))

    print("\nB0 失败（[已知勘误]/[新发现]）:")
    for r in rows:
        if not r["b0"]:
            print("  [%s] %-30s %s" % (r.get("b0_status"), r["slug"],
                                       r.get("b0_failed") or r.get("b0_error")))
    print("\nB1 失败（[已知勘误]/[已知转换器账]/[新发现]）:")
    for r in rows:
        if not r["b1"]:
            print("  [%s] %-30s pin_bad=%s rule=%s token_diff=%s"
                  % (r.get("b1_status"), r["slug"], bool(r.get("b1_pin_bad")),
                     ",".join(r.get("b1_ledger_rule") or []) or "-",
                     json.dumps(r.get("b1_token_diff"), ensure_ascii=False)[:100]
                     if r.get("b1_token_diff") else "无"))

    out = {"summary": summary, "rows": rows}
    path = args.json or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "results", "b0b1-scan-all.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("\n落盘:", path)

    if summary["b1_unaccounted"] or summary["b0_new"]:
        print("账本未闭合：B1 未对账 %d ／ B0 未对账 %d"
              % (len(summary["b1_unaccounted"]), summary["b0_new"]), file=sys.stderr)
        return 2
    print("账本闭合：全部失败件均可归属已知账（对账律满足）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
