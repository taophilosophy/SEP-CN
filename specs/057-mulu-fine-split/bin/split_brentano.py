#!/usr/bin/env python3
"""specs/057 s3i：布伦塔诺单列为“现象学前驱”，不再算作布伦塔诺学派/早期现象学。

- 原 H4「布伦塔诺学派与早期现象学」下的 H5「布伦塔诺」其实是“##### 布伦塔诺 + * 布伦塔诺”，
  双重列名（违 s2 判据②）；且布伦塔诺本人是现象学先驱而非现象学家。
- 新结构：H4「现象学前驱」直接列布伦塔诺母条（含判断理论簇），置于「现象学总论」之后；
  原 H4 保留「布伦塔诺学派与早期现象学」，内含斯图姆夫与马蒂／厄棱费尔与迈农／特瓦尔多夫斯基。
- 守恒断言：链接行 1883；brentano 母条恰一处；无 H5 标题“布伦塔诺”。
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
    # 原 H4：布伦塔诺学派与早期现象学
    li, lv, end = find(lines, base + ("布伦塔诺学派与早期现象学",))
    # 其中 H5「布伦塔诺」块
    bi = None
    for i in range(li + 1, end):
        m = HEADING.match(lines[i])
        if m and len(m.group(1)) == lv + 1 and m.group(2).strip() == "布伦塔诺":
            bi = i
            break
    assert bi is not None, "未找到 H5「布伦塔诺」"
    bend = end
    for j in range(bi + 1, end):
        m = HEADING.match(lines[j])
        if m and len(m.group(1)) <= lv + 1:
            bend = j
            break
    block = lines[bi + 1:bend]           # H5 标题后的条目行（含簇）
    while block and block[0] == "":
        block.pop(0)
    # 去掉块尾空行，插入时统一补
    while block and block[-1] == "":
        block.pop()
    assert any("brentano.md" in l for l in block), "布伦塔诺块内无 brentano.md"
    # 删除 H5 块（连同其后至下一个 H5/H4 前的空行）
    del lines[bi:bend]
    while bi < len(lines) and lines[bi] == "":
        del lines[bi]

    # 在「现象学总论」H4 之后插入新 H4
    sli, slv, send = find(lines, base + ("现象学总论",))
    ins = ["", "#" * slv + " 现象学前驱", ""] + block + [""]
    lines[send:send] = ins

    # 断言
    assert sum(1 for l in lines if ENTRY.match(l) and "brentano.md" in l) == 1
    assert not any(re.match(r"^#{1,6} 布伦塔诺\s*$", l) for l in lines), "H5「布伦塔诺」残留"
    n = sum(1 for l in lines if ENTRY.match(l))
    assert n == 1883, f"守恒破坏：{n}"
    MULUS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"布伦塔诺单列为现象学前驱，链接守恒 {n}")


if __name__ == "__main__":
    sys.exit(main())
