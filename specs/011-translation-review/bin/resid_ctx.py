# -*- coding: utf-8 -*-
"""specs/011：打印指定词条残余引号报错的原文片段（非 MISSING），供人工定点修。只读。"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)

for slug in sys.argv[1:]:
    r = subprocess.run([sys.executable, "tools/check_style.py", slug + ".md"],
                       capture_output=True, text=True)
    d = json.loads(r.stdout)
    items = d if isinstance(d, list) else d.get("items", d.get("issues", []))
    lines = io.open(slug + ".md", encoding="utf-8").read().splitlines()
    seen_line = set()
    for x in items:
        if x["rule"] != "curly-quotes" or "MISSING" in x["detail"]:
            continue
        if x["line"] in seen_line:
            continue
        seen_line.add(x["line"])
        l = lines[x["line"] - 1]
        # 找引号字符周围片段
        import re
        frags = []
        for m in re.finditer(r"[“”‘’'\"「」『』]", l):
            frags.append(l[max(0, m.start() - 10):m.end() + 10])
        print("%s L%s（%d 个引号字符）" % (slug, x["line"], len(frags)))
        for fr in frags[:6]:
            print("    …%s…" % fr)
