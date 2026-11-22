#!/usr/bin/env python3
"""specs/057 块重排：按设计 JSON 重排某父节的直接子节顺序（整块搬运）。

设计格式（UTF-8 JSON）：
  {"父节路径／子节路径": ["子标题 1", "子标题 2", ...], ...}

规则：
- 父节在 mu-lu-s.md 中唯一命中；
- 设计列出的子标题集合必须与现状直接子节集合完全相等（不丢不增）；
- 每块＝子标题行至下一个同级/更高级标题前的全部内容（含条目、簇子条、更深子节）；
- 父节标题下的直属内容（节注、直属条目）原样保留在最前；
- 写回前断言链接行守恒（1883）。

用法：python reorder_blocks.py <design.json>
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")


def main():
    design = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    lines = MULUS.read_text(encoding="utf-8").splitlines()

    # 标题索引与路径
    heads = []
    stack = []
    for i, l in enumerate(lines):
        m = HEADING.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            path = tuple(x[1] for x in stack) + (t,)
            heads.append((i, lv, path))
            stack.append((lv, t))
    by_path = {}
    for h in heads:
        by_path.setdefault("／".join(h[2]), []).append(h)

    # 逆序处理，避免行号漂移
    targets = []
    for path, order in design.items():
        hits = by_path.get(path, [])
        assert len(hits) == 1, f"{path} 命中 {len(hits)} 处"
        targets.append((hits[0], order))
    for (li, lv, path), order in sorted(targets, reverse=True):
        end = len(lines)
        for li2, lv2, _ in heads:
            if li2 > li and lv2 <= lv:
                end = li2
                break
        # 直接子节位置
        kids = [(i, p[-1]) for i, l2, p in heads if li < i < end and l2 == lv + 1]
        names = [t for _, t in kids]
        assert sorted(names) == sorted(order), \
            f"{'／'.join(path)}：子节集合不符\n  现状 {names}\n  设计 {order}"
        # 父节直属前缀（父标题后、首个子节前的内容）
        first = kids[0][0]
        prefix = lines[li + 1:first]
        blocks = {}
        for k, (ki, t) in enumerate(kids):
            stop = kids[k + 1][0] if k + 1 < len(kids) else end
            blocks[t] = lines[ki:stop]
        new_body = list(prefix)
        for t in order:
            new_body.extend(blocks[t])
        lines[li + 1:end] = new_body
        print(f"重排 {'／'.join(path)}：{len(order)} 块")

    n = sum(1 for l in lines if ENTRY.match(l))
    assert n == 1883, f"守恒破坏：{n}"
    MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"写出 {MULUS.name}，链接行守恒 {n}")


if __name__ == "__main__":
    sys.exit(main())
