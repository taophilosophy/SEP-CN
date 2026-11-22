#!/usr/bin/env python3
"""specs/057 s2 盘点：列出指定 H1 区内"有≥2 直接条目且无子节"的节点及其条目，
供逐节设计 H4 分组。输出 Markdown。"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")

def slug_of(h):
    return h.rsplit("/", 1)[-1][:-3]

h1 = sys.argv[1]
lines = (ROOT / "mu-lu-s.md").read_text(encoding="utf-8").splitlines()
stack = []
heads = []
for i, l in enumerate(lines):
    m = HEADING.match(l)
    if m:
        lv, t = len(m.group(1)), m.group(2).strip()
        stack = stack[: lv - 1] + [t]
        heads.append((i, lv, tuple(stack)))

out = [f"# s2 盘点：{h1}", ""]
for idx, (li, lv, path) in enumerate(heads):
    if path[0] != h1:
        continue
    end = len(lines)
    for li2, lv2, p2 in heads[idx + 1:]:
        if lv2 <= lv:
            end = li2
            break
    hassub = any(li < li2 < end and lv2 == lv + 1 for li2, lv2, p2 in heads)
    direct = [(k, ENTRY.match(lines[k])) for k in range(li + 1, end)
              if (ENTRY.match(lines[k]) and len(ENTRY.match(lines[k]).group(1)) == 0)]
    if len(direct) < 2 or hassub:
        continue
    out.append(f"## {'／'.join(path)}（{len(direct)}）")
    for k, m in direct:
        kids = []
        j = k + 1
        while j < end and (mm := ENTRY.match(lines[j])) and len(mm.group(1)) > 0:
            kids.append(slug_of(mm.group(3)))
            j += 1
        out.append(f"- `{slug_of(m.group(3))}`｜{m.group(2)}" +
                   (f"　［簇成员：{'、'.join(kids) or '有子条'}］" if j > k + 1 else ""))
    out.append("")

p = ROOT / f"specs/057-mulu-fine-split/results/s2-{h1.replace('、', '')}-inventory.md"
p.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("写出", p, "节点数", sum(1 for l in out if l.startswith("## ")))
