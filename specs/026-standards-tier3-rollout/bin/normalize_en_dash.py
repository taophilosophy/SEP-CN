# -*- coding: utf-8 -*-
"""Tier 3 连接号归一：正文年代/区间 en-dash（U+2013）→ 一字线（U+2014）。

依据：ADR-0041 用户裁定（一字线=时间与地域起止）+ GB/T 15834-2011 §4.13；
用户全面批准（2026-11-14，specs/026）。纯符号层归一（ADR-0041 明示不涉句法语义）。

判据（机械替换边界）：
* 只处理 connector-scan 基线（bin/connector-scan-baseline-20261114.json）flagged 的行；
* 只替换**两侧均为数字**的 en-dash（正则 (?<=\\d)–(?=\\d)）；
* 非数字邻接（罗马数字区间等）不动，进待人工判定清单；
* 幂等：转换后行内无 en-dash，重跑零改动；
* 逐行追踪：manifest 记录每处 (path, line, before, after)。

用法：
  python normalize_en_dash.py --only a/abhidharma.md,...   # 试金石（相对路径）
  python normalize_en_dash.py                              # 铺量（全部 flagged 行）
"""
import argparse
import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(BASE)))
BASELINE = os.path.join(BASE, "connector-scan-baseline-20261114.json")
EN_DASH = "\u2013"
EM_DASH = "\u2014"
PATTERN = re.compile(r"(?<=\d)\u2013(?=\d)")


def load_flagged():
    raw = io.open(BASELINE, encoding="utf-8").read()
    data = json.loads(raw[raw.find("{"):])
    pairs = set()
    for w in data.get("warnings", []):
        if w.get("rule") == "connector-form":
            pairs.add((w["path"], int(w["line"])))
    return sorted(pairs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="逗号分隔的相对路径白名单（试金石）")
    ap.add_argument("--out", default=os.path.join(REPO, "specs", "026-standards-tier3-rollout", "results", "en-dash-manifest.json"))
    args = ap.parse_args()

    only = {p.replace("\\", "/") for p in args.only.split(",") if p.strip()}
    flagged = load_flagged()
    if only:
        flagged = [(p, l) for (p, l) in flagged if p.replace("\\", "/") in only]
        if len(flagged) != len(only):
            missing = only - {p.replace("\\", "/") for p, _ in flagged}
            print("警告：白名单中不在基线的路径：%s" % missing)

    manifest = []
    manual = []  # flagged 行上非数字邻接的 en-dash，禁机械、留人工
    touched = set()
    total = 0
    for rel, lineno in flagged:
        path = os.path.join(REPO, rel.replace("\\", "/"))
        lines = io.open(path, encoding="utf-8", newline="").read().split("\n")
        if lineno < 1 or lineno > len(lines):
            print("跳过越界：%s:%d" % (rel, lineno))
            continue
        old = lines[lineno - 1]
        if EN_DASH not in old:
            continue  # 幂等：已转换
        leftovers = PATTERN.sub(EM_DASH, old)
        # 非数字邻接的 en-dash 仍在 leftovers 中 → 登记
        if EN_DASH in leftovers:
            for m in re.finditer(r"\u2013", leftovers):
                a = leftovers[max(0, m.start() - 1): m.start()]
                b = leftovers[m.end(): m.end() + 1]
                manual.append({"path": rel.replace("\\", "/"), "line": lineno,
                               "context": leftovers[max(0, m.start() - 15): m.end() + 15]})
        n = len(PATTERN.findall(old))
        if n == 0:
            continue
        lines[lineno - 1] = leftovers
        io.open(path, "w", encoding="utf-8", newline="").write("\n".join(lines))
        manifest.append({"path": rel.replace("\\", "/"), "line": lineno, "count": n,
                         "before": old[:160], "after": leftovers[:160]})
        touched.add(rel)
        total += n
    changed_files = len(touched)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    suffix = "-pilot.json" if only else ".json"
    out = args.out.replace(".json", suffix)
    io.open(out, "w", encoding="utf-8", newline="").write(json.dumps(
        {"scope": sorted(only) if only else "all", "files": changed_files, "conversions": total,
         "lines": manifest, "manual_review": manual}, ensure_ascii=False, indent=1))
    print("转换 %d 处 / %d 文件；待人工 %d 处；manifest → %s" % (total, changed_files, len(manual), out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
