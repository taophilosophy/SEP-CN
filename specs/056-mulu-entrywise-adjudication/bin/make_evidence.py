#!/usr/bin/env python3
"""specs/056 逐条研判：批次证据包生成器。

用法：python make_evidence.py <批号 1..10>
每批 ≈188 行（按 mu-lu-s.md 文档序全局编号 seq）。证据包每行含：
  slug／题名／现节／010 PP 映射（咨询锚＋区域冲突旗）／本地镜像首段摘要（≤220 字符）。
只读分析；输出 results/evidence-b<N>.md。
"""
import html
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
PP_TSV = ROOT / "specs/010-mulu-recategorize/results/philpapers-mapping.tsv"
OUT = ROOT / "specs/056-mulu-entrywise-adjudication/results"
BATCH = int(sys.argv[1]) if len(sys.argv) > 1 else 1
SIZE = 188

HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")
P_RE = re.compile(r"<p>(.*?)</p>", re.S)
TAG_RE = re.compile(r"<[^>]+>")

def unesc(t):
    return t.replace("\\*", "*").replace("\\[", "[").replace("\\]", "]")

def slug_of(href):
    return href.rsplit("/", 1)[-1][:-3]

# 行清单（文档序）
rows = []
stack = []
for line in MULUS.read_text(encoding="utf-8").splitlines():
    m = HEADING.match(line)
    if m:
        lv, t = len(m.group(1)), unesc(m.group(2).strip())
        stack = stack[: lv - 1]
        stack.append(t)
        continue
    m = ENTRY.match(line)
    if m:
        rows.append({"slug": slug_of(m.group(3)), "href": m.group(3),
                     "title": m.group(2), "path": tuple(stack)})

# PP 映射（咨询锚）
PP = {}
if PP_TSV.exists():
    import csv
    with PP_TSV.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            PP[row["slug"]] = (row.get("PP大类", "").strip(), row.get("PP子类", "").strip())

REGION_PP = {
    "西方哲学史": {"History of Western Philosophy"},
    "哲学传统": {"Philosophical Traditions", "Asian Philosophy", "African/Africana Philosophy",
             "Philosophy of the Americas", "Continental Philosophy"},
    "形而上学与认识论": {"Metaphysics and Epistemology"},
    "价值理论": {"Value Theory"},
    "科学、逻辑与数学": {"Science, Logic, and Mathematics"},
}

def abstract(slug):
    f = ROOT / "en" / slug / "index.html"
    if not f.exists():
        return "（本地镜像无此页）"
    txt = f.read_text(encoding="utf-8", errors="replace")
    m = P_RE.search(txt)
    if not m:
        return "（无摘要段）"
    s = TAG_RE.sub("", m.group(1))
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:220]

lo = (BATCH - 1) * SIZE
batch = rows[lo: lo + SIZE]
conflict_n = 0
lines = ["# specs/056 证据包 b%d（seq %d–%d，共 %d 行）" % (
    BATCH, lo + 1, lo + len(batch), len(batch)), ""]
for i, r in enumerate(batch, lo + 1):
    pp = PP.get(r["slug"], ("", ""))
    region = r["path"][0]
    flag = ""
    if pp[0] and region in REGION_PP and pp[0] not in REGION_PP[region]:
        flag = "  **[区域冲突→%s]**" % pp[0]
        conflict_n += 1
    lines.append("### %d | %s | %s" % (i, r["slug"], "／".join(r["path"])))
    lines.append("题：%s" % unesc(r["title"]))
    if pp[0]:
        lines.append("PP：%s／%s%s" % (pp[0], pp[1], flag))
    else:
        lines.append("PP：—（010 之后接入，无映射）")
    lines.append("摘：%s" % abstract(r["slug"]))
    lines.append("")
lines.insert(4, "区域冲突旗行数：%d（旗≠必错，PP 映射有噪音；旗行须细看，无旗行也逐条过）" % conflict_n)
(OUT / ("evidence-b%d.md" % BATCH)).write_text("\n".join(lines) + "\n",
                                               encoding="utf-8", newline="\n")
print("b%d：%d 行（seq %d–%d），冲突旗 %d → evidence-b%d.md" % (
    BATCH, len(batch), lo + 1, lo + len(batch), conflict_n, BATCH))
