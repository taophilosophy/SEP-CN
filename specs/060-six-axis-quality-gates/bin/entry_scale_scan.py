#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""词条长度与格式复杂度扫描（只读，specs/060 试金石池凭证）。

用法: python specs/060-six-axis-quality-gates/bin/entry_scale_scan.py [--top N]
输出: stdout 摘要＋ specs/060-six-axis-quality-gates/results/entry-scale-scan.json

对象: <letter>/<slug>.md（字母目录 a–z 与 1；不含作者控制台页面）
口径: 机检出数，不作裁判（ADR-0070）。
  长度   总字符、汉字数、正文汉字数（“参考文献”节前）
  复杂度 14 类构件存在性（variety）＋对数压缩加权密度（complexity）；
         权重只用于排序候选，不构成质量判定
  计量   units＝无歧义真实单位串命中数（人名与词内字已剔除，见 UNIT_LITERALS 注）
豁免: 无。参考文献节只从“正文汉字数”中剔除，仍计入总字符与全篇汉字。
退出码: 0（分析工具，不做门禁）。
"""
import argparse
import json
import math
import os
import re
import sys

if (getattr(sys.stdout, "encoding", "") or "").lower().replace("-", "") != "utf8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, "specs", "060-six-axis-quality-gates",
                   "results", "entry-scale-scan.json")
LETTERS = set("abcdefghijklmnopqrstuvwxyz") | {"1"}

CJK_RE = re.compile(r"[\u4e00-\u9fff]")
HEAD_RE = re.compile(r"^(#{1,6})\s+\S")
BIB_RE = re.compile(r"^##\s*(参考文献|参考书目|Bibliography|Works Cited)\s*$", re.I)
FN_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:")
LINK_RE = re.compile(r"\]\(([^)]*)\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(")
TBL_ROW_RE = re.compile(r"^\s*\|.+\|\s*$")
QUOTE_RE = re.compile(r"^\s*>")
LI_RE = re.compile(r"^(\s*)[-*+]\s+")
BEGIN_RE = re.compile(r"\\begin\{")
FENCE_RE = re.compile(r"^\s*```")

# q5 计量轴取样用：只列无歧义的真实单位串。
# “马赫”“摩尔”“吨”“升”“度”“克”“米”已剔除——实测多为人名（恩斯特·马赫、
# 摩尔根）与词内字（提升、精度、米尔恩）误匹配，不作计量证据。
UNIT_LITERALS = [
    "平方米", "立方米", "公里", "千米", "厘米", "毫米", "微米", "纳米",
    "千克", "公斤", "毫克", "毫秒", "微秒", "摄氏度", "华氏", "英里",
    "英尺", "英寸", "盎司", "加仑", "毫升", "赫兹", "焦耳", "瓦特",
    "电子伏", "光年", "开尔文", "m/s", "km/h", "mph", "GeV", "MeV",
    "keV", "Hz", "°C", "°F",
]

# 复杂度权重：多样性 3/类；密度按 log1p 压缩，避免长文单纯靠体量占优。
WEIGHTS = {
    "h3plus": 1.0, "footnotes": 1.2, "links": 0.4, "images": 2.0,
    "table_blocks": 1.5, "quotes": 0.8, "list_items": 0.4, "list_nest": 1.5,
    "math_inline": 0.8, "math_display": 1.5, "latex_envs": 1.5,
    "code_blocks": 1.5, "bold": 0.2,
}

SHORTLIST = [
    "e/environmental-aesthetics", "l/logic-preference", "i/intrinsic-extrinsic",
    "c/computing-history", "h/habermas", "n/newton-principia", "a/action",
    "a/axiom-choice", "i/imprecise-probabilities", "j/japanese-aesthetics",
    "k/kokugaku-school", "d/digital-art", "f/falaquera",
]


def scan_file(path, rel):
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    lines = text.splitlines()
    bib_at = next((i for i, l in enumerate(lines) if BIB_RE.match(l)), None)
    body = "\n".join(lines[:bib_at]) if bib_at is not None else text

    heads = [len(m.group(1)) for l in lines for m in [HEAD_RE.match(l)] if m]
    footnotes = len({m.group(1) for l in lines for m in [FN_DEF_RE.match(l)] if m})
    links = sum(len(LINK_RE.findall(l)) for l in lines)
    images = sum(len(IMG_RE.findall(l)) for l in lines)
    table_rows = sum(1 for l in lines if TBL_ROW_RE.match(l))
    table_blocks = 0
    in_table = False
    for l in lines:
        if TBL_ROW_RE.match(l) and not in_table:
            table_blocks += 1
            in_table = True
        elif not TBL_ROW_RE.match(l):
            in_table = False
    quotes = sum(1 for l in lines if QUOTE_RE.match(l))
    indents = [len(m.group(1)) for l in lines for m in [LI_RE.match(l)] if m]
    list_items = len(indents)
    list_nest = max(((i - indents[0]) // 2 + 1 for i in indents), default=0) if indents else 0
    dollars = sum(l.count("$") for l in lines)
    dbl = sum(1 for l in lines if l.strip().startswith("$$"))
    math_display = dbl // 2
    math_inline = max(0, dollars - dbl * 2) // 2
    latex_envs = sum(len(BEGIN_RE.findall(l)) for l in lines)
    code_blocks = sum(1 for l in lines if FENCE_RE.match(l)) // 2
    bold = sum(l.count("**") // 2 for l in lines)
    units = sum(text.count(u) for u in UNIT_LITERALS)

    metrics = dict(
        path=rel, slug=os.path.splitext(os.path.basename(path))[0],
        chars=len(text), cjk=len(CJK_RE.findall(text)),
        body_cjk=len(CJK_RE.findall(body)), lines=len(lines),
        h2=sum(1 for d in heads if d == 2), h3plus=sum(1 for d in heads if d >= 3),
        footnotes=footnotes, links=links, images=images,
        table_blocks=table_blocks, table_rows=table_rows, quotes=quotes,
        list_items=list_items, list_nest=list_nest,
        math_inline=math_inline, math_display=math_display,
        latex_envs=latex_envs, code_blocks=code_blocks, bold=bold,
        units=units,
    )
    variety = sum(1 for k in WEIGHTS if metrics[k] > 0)
    complexity = variety * 3 + sum(
        w * math.log1p(metrics[k]) for k, w in WEIGHTS.items())
    metrics["variety"] = variety
    metrics["complexity"] = round(complexity, 2)
    return metrics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=15)
    args = ap.parse_args()

    rows = []
    for letter in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, letter)
        if not (os.path.isdir(d) and letter in LETTERS):
            continue
        for name in sorted(os.listdir(d)):
            if name.endswith(".md") and name.lower() not in (
                    "summary.md", "readme.md", "index.md"):
                rows.append(scan_file(os.path.join(d, name), f"{letter}/{name}"))

    def top(key):
        return sorted(rows, key=lambda r: r[key], reverse=True)[:args.top]

    result = {
        "schema": "entry-scale-scan/v1",
        "scope": "<letter>/<slug>.md（a–z 与 1）",
        "note": "机检出数，不作裁判；复杂度权重仅用于排序候选。",
        "generated": "2026-11-25",
        "files_scanned": len(rows),
        "metrics": ["chars", "cjk", "body_cjk", "complexity", "variety"],
        "top": {k: top(k) for k in ("chars", "cjk", "body_cjk", "complexity", "variety")},
        "extremes": {
            k: sorted(rows, key=lambda r: r[k], reverse=True)[:5]
            for k in ("images", "table_rows", "latex_envs", "math_inline",
                      "math_display", "footnotes", "code_blocks", "units")
        },
        "shortlist": [r for r in rows if r["path"][:-3] in SHORTLIST],
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
        fh.write("\n")

    print(f"scanned={len(rows)}  -> {os.path.relpath(OUT, ROOT)}")
    for key in ("chars", "cjk", "body_cjk", "complexity"):
        r = top(key)[0]
        print(f"top {key:10s} {r[key]:>8}  {r['path']}")
    print("shortlist:")
    for r in sorted(result["shortlist"], key=lambda r: -r["chars"]):
        print(f"  {r['chars']:>7} chars  {r['cjk']:>6} cjk  var={r['variety']:>2} "
              f"fn={r['footnotes']:>3} units={r['units']:>3}  {r['path']}")
    print("units top5:", [(r["units"], r["path"])
                          for r in sorted(rows, key=lambda r: -r["units"])[:5]])


if __name__ == "__main__":
    sys.exit(main())
