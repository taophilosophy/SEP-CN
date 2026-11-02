# -*- coding: utf-8 -*-
"""调试 L169 的引号遮蔽处理。只读。"""
import io
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

line = io.open("i/intrinsic-extrinsic.md", encoding="utf-8").read().splitlines()[168]
seg = line
stripped = re.sub(r"[^\W\d_]['‘’][^\W\d_]", "AA", seg)
stripped = re.sub(r"[^\W\d_]['‘’](?![\u4e00-\u9fff])", "A", stripped)
stripped = re.sub(r"(?<![\u4e00-\u9fff])['‘’][^\W\d_]", "A", stripped)
stripped = re.sub(r"\$\$.+?\$\$|\$[^$\n]+?\$", "\x00", stripped)
print("单 ‘: %d ’: %d" % (stripped.count("‘"), stripped.count("’")))
print("双 “: %d ”: %d" % (stripped.count("“"), stripped.count("”")))
for m in re.finditer(r"[‘’]", stripped):
    print(repr(stripped[max(0, m.start() - 8):m.end() + 8]))
