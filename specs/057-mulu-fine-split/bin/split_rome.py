#!/usr/bin/env python3
"""specs/057 s3h：拆分“罗马哲学与拜占庭”混合块并按年代嵌入希腊化序列。

- 原 H4「罗马哲学与拜占庭」名不副实（无拜占庭条目——拜占庭哲学已在中世纪区单列）；
- 三个 H5（罗马折衷主义＝西塞罗／逍遥派评注＝亚历山大／医学与哲学＝盖伦）拆为：
  H4「罗马共和国哲学」（罗马折衷主义）
  H4「罗马帝国学术与医学」（逍遥派评注＋医学与哲学）
- 插入位置：「怀疑主义与新学园」之后、「新柏拉图主义」之前（年代序：
  伊壁鸠鲁 → 斯多亚 → 怀疑主义与新学园 → 西塞罗 前1世纪 → 亚历山大/盖伦 2–3世纪 → 普罗提诺 3世纪）。
- 守恒断言：链接行 1883；原 H4 区间删除后必须零残条。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")


def heading_span(lines, path):
    """唯一命中路径，返回 (li, lv, end)。"""
    hits = []
    stack = []
    for i, l in enumerate(lines):
        m = HEADING.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            p = tuple(x[1] for x in stack) + (t,)
            stack.append((lv, t))
            if p == path:
                hits.append((i, lv))
    assert len(hits) == 1, f"{'／'.join(path)} 命中 {len(hits)} 处"
    li, lv = hits[0]
    end = len(lines)
    for j in range(li + 1, len(lines)):
        m = HEADING.match(lines[j])
        if m and len(m.group(1)) <= lv:
            end = j
            break
    return li, lv, end


def sub_blocks(lines, li, lv, end):
    """区间内 lv+1 级直接子节块列表 [(标题名, [行...])]。"""
    pos = []
    for i in range(li + 1, end):
        m = HEADING.match(lines[i])
        if m and len(m.group(1)) == lv + 1:
            pos.append((i, m.group(2).strip()))
    out = []
    for k, (i, t) in enumerate(pos):
        stop = pos[k + 1][0] if k + 1 < len(pos) else end
        out.append((t, lines[i:stop]))
    return out, (pos[0][0] if pos else None)


def main():
    lines = MULUS.read_text(encoding="utf-8").splitlines()

    zone = ("西方哲学史", "古代哲学", "希腊化与罗马哲学")
    old = tuple(zone) + ("罗马哲学与拜占庭",)
    oli, olv, oend = heading_span(lines, old)
    subs, _ = sub_blocks(lines, oli, olv, oend)
    names = [t for t, _ in subs]
    assert sorted(names) == sorted(["罗马折衷主义", "逍遥派评注", "医学与哲学"]), \
        f"原块子节意外：{names}"
    by = dict(subs)

    new_block = []
    for head, kids in (
            (("罗马共和国哲学",), ["罗马折衷主义"]),
            (("罗马帝国学术与医学",), ["逍遥派评注", "医学与哲学"])):
        new_block.append("#" * (olv) + " " + head[0])
        for t in kids:
            new_block.append("")
            new_block.extend(by[t])
        new_block.append("")

    # 删除原区间（含其后的空行）
    tail_blank = 0
    j = oend
    while j < len(lines) and lines[j] == "":
        tail_blank += 1
        j += 1
    del lines[oli:oend + tail_blank]

    # 插到「新柏拉图主义」前
    target = tuple(zone) + ("新柏拉图主义",)
    tli, tlv, tend = heading_span(lines, target)
    lines[tli:tli] = new_block

    n = sum(1 for l in lines if ENTRY.match(l))
    assert n == 1883, f"守恒破坏：{n}"
    # 原混合块残留检查
    assert not any("罗马哲学与拜占庭" == t for t in re.findall(r"^#{1,6} (.+)$",
                   "\n".join(lines), re.M)), "原标题残留"
    MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"拆分写入：新 H4 ×2（罗马共和国哲学／罗马帝国学术与医学），链接守恒 {n}")


if __name__ == "__main__":
    sys.exit(main())
