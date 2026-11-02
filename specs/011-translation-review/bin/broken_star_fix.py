# -*- coding: utf-8 -*-
"""specs/011：intensional 等词条的原始星号畸形修复。

族 A：***X** *  →  **X**        （粗斜错乱三连星+孤立星，取粗体意图）
族 C：** *(n) ** / ***(n)**  →  **(n)**   （编号行）
每处替换后验证 star_ok，不健康则不替换并报告。
"""
import io
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "specs", "011-translation-review", "bin"))
from style_fix import star_ok  # noqa: E402


def segtext(line):
    return "".join(p for idx, p in enumerate(line.split("`")) if idx % 2 == 0)


def main():
    path = "i/intensional-trans-verbs.md"
    t = io.open(path, encoding="utf-8").read()
    lines = t.split("\n")
    fixed = skipped = 0
    for i, line in enumerate(lines):
        seg = segtext(line)
        if star_ok(seg):
            continue
        orig = line
        # 族 C：编号行
        line = re.sub(r"\*\*\s*\*+\((\d+[a-z]?)\)\s*\*\*+", "**(\\1)**", line)
        line = re.sub(r"\*\*\*\((\d+[a-z]?)\)\*\*", "**(\\1)**", line)
        # 族 A：***X** *  →  **X**（X≤24 字符非星）
        line = re.sub(r"\*\*\*([^*\n]{1,24}?)\*\*\s*\*(?![\*])", r"**\1**", line)
        # 族 A 变体：***X** **  →  **X**
        line = re.sub(r"\*\*\*([^*\n]{1,24}?)\*\*\s*\*\*(?!\*)", r"**\1**", line)
        # 收尾：** X **（星号内侧空格，ADR-0019 违例）→ **X**
        line = re.sub(r"\*\* ([^*\n]{1,40}?) \*\*", r"**\1**", line)
        if star_ok(segtext(line)):
            if line != orig:
                lines[i] = line
                fixed += 1
        else:
            skipped += 1
    io.open(path, "w", encoding="utf-8", newline="").write("\n".join(lines))
    print("修 %d 行，仍畸形 %d 行" % (fixed, skipped))


if __name__ == "__main__":
    main()
