#!/usr/bin/env python3
"""specs/057 s3m+：给“已有子节”的父节补充分组，只重排直属条目，保留现有子节。

设计 JSON：{"父节路径": [["新子节名", "slug,slug"], ...]}

规则：
- 父节唯一命中；新子节为父级+1 层标题，按设计顺序排在现有子节之前；
- 设计的 slug 集合必须等于父节当前的直属母条集合（不含现有子节内条目与簇子条）；
- 现有子节（含更深子节）原样保留在新区块之后；
- 父标题下的节注（> 行）保留；链接行守恒 1883。

用法：python group_direct.py <design.json>
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
H = re.compile(r"^(#{1,6}) (.+?)\s*$")
E = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")


def parse(lines):
    heads, stack = [], []
    for i, l in enumerate(lines):
        m = H.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            p = tuple(x[1] for x in stack) + (t,)
            heads.append((i, lv, p))
            stack.append((lv, t))
    return heads


def main():
    design = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    lines = MULUS.read_text(encoding="utf-8").splitlines()
    heads = parse(lines)
    targets = []
    for path, groups in design.items():
        tpath = tuple(path.split("／"))
        hits = [(i, lv) for i, lv, p in heads if p == tpath]
        assert len(hits) == 1, f"{path} 命中 {len(hits)} 处"
        targets.append((hits[0], tpath, groups))
    for (li, lv), tpath, groups in sorted(targets, reverse=True):
        end = len(lines)
        for i, l2, _ in heads:
            if i > li and l2 <= lv:
                end = i
                break
        subpos = [i for i, l2, _ in heads if li < i < end and l2 == lv + 1]
        dstart = subpos[0] if subpos else end
        blocks, order, prefix = {}, [], []
        i = li + 1
        while i < dstart:
            m = E.match(lines[i])
            if m and len(m.group(1)) == 0:
                s = m.group(3).rsplit("/", 1)[-1][:-3]
                blk = [lines[i]]
                j = i + 1
                while j < dstart and (mm := E.match(lines[j])) and len(mm.group(1)) > 0:
                    blk.append(lines[j])
                    j += 1
                blocks[s] = blk
                order.append(s)
                i = j
                continue
            if lines[i].strip():
                prefix.append(lines[i])
            i += 1
        want = []
        for name, slugs in groups:
            assert name.strip(), f"{tpath} 空子节名"
            for s in [x for x in slugs.split(",") if x.strip()]:
                assert s in blocks, f"{tpath}：直属条目中无 {s}"
                assert s not in want, f"{tpath}：重复 {s}"
                want.append(s)
        assert set(want) == set(order), \
            f"{tpath}：设计 {len(set(want))} vs 直属 {len(set(order))}；" \
            f"缺 {sorted(set(order) - set(want))} 多 {sorted(set(want) - set(order))}"
        out = []
        notes = [l for l in prefix if l.lstrip().startswith(">")]
        if notes:
            out += [""] + notes
        for name, slugs in groups:
            out += ["", "#" * (lv + 1) + " " + name, ""]
            for s in [x for x in slugs.split(",") if x.strip()]:
                out += blocks[s]
        out.append("")
        rest = lines[dstart:end]
        if rest:
            out += rest
        lines[li + 1:end] = out
    n = sum(1 for l in lines if E.match(l))
    assert n == 1883, f"守恒破坏：{n}"
    MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"分组 {len(targets)} 节，链接守恒 {n}")


if __name__ == "__main__":
    sys.exit(main())
