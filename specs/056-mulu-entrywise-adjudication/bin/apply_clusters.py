#!/usr/bin/env python3
"""specs/056 b12 应用器：把"属于人物的概念条目"归入人物簇。

用户裁定（2026-11-22）："概念属于人物的应归类到人物，有问题读取原文"。
裁定字：
  CLUS      同节簇化（缩进 2，移入母条簇末尾）
  MOVECLUS  跨节移入母条簇（缩进 2），母条为库内人物条
台账 b12 的「新节」列＝母条 slug。整簇条目（母条带嵌套子条）随簇搬运。

卡钉：链接集合守恒 1883 进=出；母条须存在且 ind=0；块内每行统一缩进 2。
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RES = ROOT / "specs/056-mulu-entrywise-adjudication/results"
MULUS = ROOT / "mu-lu-s.md"

ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")

def slug_of(href):
    return href.rsplit("/", 1)[-1][:-3]

# ---- 读 b12 ----
rows = []
with (RES / "adjudication-b12.tsv").open(encoding="utf-8", newline="") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        assert r["裁定"] in ("CLUS", "MOVECLUS"), r["裁定"]
        rows.append((int(r["seq"]), r["slug"], r["裁定"], r["新节"].strip()))

lines = MULUS.read_text(encoding="utf-8").splitlines()

def find_entry(slug):
    hits = []
    for i, l in enumerate(lines):
        m = ENTRY.match(l)
        if m and slug_of(m.group(3)) == slug:
            hits.append((i, m))
    assert len(hits) == 1, f"{slug} 条目行数 {len(hits)}"
    return hits[0]

report = []
for seq, slug, kind, mother in sorted(rows, key=lambda x: x[0]):
    i, m = find_entry(slug)
    assert len(m.group(1)) == 0, f"{slug} 已是簇成员？ind={len(m.group(1))}"
    j = i + 1
    while j < len(lines):
        mm = ENTRY.match(lines[j])
        if mm and len(mm.group(1)) > 0:
            j += 1
        else:
            break
    block = [l for l in lines[i:j]]
    del lines[i:j]
    # 母条定位
    mi, mm2 = find_entry(mother)
    assert len(mm2.group(1)) == 0, f"母条 {mother} 非顶层条目"
    # 母条簇末尾：紧跟的 ind>0 条目行之后
    k = mi + 1
    while k < len(lines):
        me = ENTRY.match(lines[k])
        if me and len(me.group(1)) > 0:
            k += 1
        else:
            break
    new_block = []
    for b in block:
        bm = ENTRY.match(b)
        assert bm, f"块内非条目行：{b!r}"
        new_block.append("  * [%s](%s)" % (bm.group(2), bm.group(3)))
    lines[k:k] = new_block
    report.append((slug, kind, mother, len(block)))

n = len([l for l in lines if ENTRY.match(l)])
assert n == 1883, f"守恒破坏：{n}"

MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print(f"簇化 {len(report)} 条（含随簇子条），条目守恒 {n}")
for slug, kind, mother, nb in report:
    print(f"  [{kind:8s}] {slug:26s} → {mother}（{nb} 行）")
