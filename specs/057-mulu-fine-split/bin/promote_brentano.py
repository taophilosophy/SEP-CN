#!/usr/bin/env python3
"""specs/057 s3j：布伦塔诺升格为 H3「描述心理学（现象学前驱）」，置于现象学运动之上。

用户 2026-11-22 裁定：节名“描述心理学（现象学前驱）”，放到现象学同级（H3）上面。
- 取出现象学运动下 H4「现象学前驱」条目块（布伦塔诺母条＋判断理论簇）；
- 在 H3「现象学运动」之前插入新 H3「描述心理学（现象学前驱）」＋该条目块；
- 现象学运动下不再有布伦塔诺节。
守恒断言：链接行 1883；brentano 母条恰一处；无「现象学前驱」H4 残留。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULUS = ROOT / "mu-lu-s.md"
HEADING = re.compile(r"^(#{1,6}) (.+?)\s*$")
ENTRY = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")


def find(lines, path):
    hits, stack = [], []
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


def main():
    lines = MULUS.read_text(encoding="utf-8").splitlines()
    base = ("西方哲学史", "现代哲学", "现象学运动")

    # 1) 取出 H4「现象学前驱」块
    li, lv, end = find(lines, base + ("现象学前驱",))
    assert lv == 4, f"预期 H4，实际 H{lv}"
    block = lines[li + 1:end]
    while block and block[0] == "":
        block.pop(0)
    while block and block[-1] == "":
        block.pop()
    assert sum(1 for l in block if "brentano.md" in l) == 1, "块内 brentano 母条应恰一处"
    # 删除（连同其后空行）
    del lines[li:end]
    while li < len(lines) and lines[li] == "":
        del lines[li]

    # 2) 在 H3「现象学运动」前插入新 H3
    tli, tlv, _ = find(lines, base)
    ins = ["### 描述心理学（现象学前驱）", ""] + block + ["", ""]
    lines[tli:tli] = ins

    # 断言
    assert sum(1 for l in lines if ENTRY.match(l) and "brentano.md" in l) == 1
    assert not any(re.match(r"^#{1,6} 现象学前驱\s*$", l) for l in lines), "旧 H4 残留"
    n = sum(1 for l in lines if ENTRY.match(l))
    assert n == 1883, f"守恒破坏：{n}"
    MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"布伦塔诺升格为 H3「描述心理学（现象学前驱）」，链接守恒 {n}")


if __name__ == "__main__":
    sys.exit(main())
