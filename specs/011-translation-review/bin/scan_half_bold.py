# -*- coding: utf-8 -*-
"""specs/011：全库扫描半粗体形态族（*X** / **X*），统计规模与分布。只读不写。"""
import glob
import io
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)

SINGLE_OPEN = re.compile("(?<![\\*`])\\*([^*\\n]{1,40}?)\\*\\*(?!\\*)")
DOUBLE_OPEN = re.compile("(?<!\\*)\\*\\*([^*\\n]{1,40}?)\\*(?!\\*)")

hit = {}
for f in glob.glob("[a-z]/*.md"):
    if f.startswith(("yi-", "ren-", "mu-")):
        continue
    try:
        t = io.open(f, encoding="utf-8").read()
    except Exception:
        continue
    for kind, p in (("single-open-double-close", SINGLE_OPEN),
                    ("double-open-single-close", DOUBLE_OPEN)):
        for m in p.finditer(t):
            hit.setdefault(kind, []).append((f, m.group(0)[:44]))

for k, v in sorted(hit.items()):
    print(k, len(v))
    for f, s in v[:15]:
        print("  ", f, repr(s))
