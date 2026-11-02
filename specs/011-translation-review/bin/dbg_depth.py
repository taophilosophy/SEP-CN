# -*- coding: utf-8 -*-
"""调试指定行单引号 depth 流。只读。用法：python dbg_depth.py <file> <lineno>"""
import io
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)

f, ln = sys.argv[1], int(sys.argv[2])
line = io.open(f, encoding="utf-8").read().splitlines()[ln - 1]
stripped = re.sub(r"(?<![\u4e00-\u9fff])[^\W\d_]['‘’][^\W\d_](?![\u4e00-\u9fff])", "AA", line)
stripped = re.sub(r"(?<![\u4e00-\u9fff\w])['‘’](?=[^\W\d_])(?![\u4e00-\u9fff])", "A", stripped)
stripped = re.sub(r"\$\$.+?\$\$|\$[^$\n]+?\$", "\x00", stripped)
depth = 0
for ch in stripped:
    if ch == "‘":
        depth += 1
    elif ch == "’":
        depth -= 1
        if depth < 0:
            print("右先于左 @", )
            depth = 0
print("final depth", depth)
# 打印每个单引号前 8 字符
for m in re.finditer(r"[‘’]", stripped):
    print(repr(stripped[max(0, m.start() - 9):m.end() + 3]))
