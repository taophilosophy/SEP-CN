# -*- coding: utf-8 -*-
"""specs/011：列出指定词条 check_style 的非 MISSING 引号/修复类残余。用法：python resid.py c/condemnation [more...]"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
FIX = ("italic-cjk", "bold-spacing", "cjk-spacing")

for slug in sys.argv[1:]:
    r = subprocess.run([sys.executable, "tools/check_style.py", slug + ".md"],
                       capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except Exception:
        print(slug, "JSON 解析失败:", r.stdout[:120], r.stderr[:120])
        continue
    items = d if isinstance(d, list) else d.get("items", d.get("issues", []))
    zh_curly = [x for x in items if x["rule"] == "curly-quotes"
                and "MISSING" not in x["detail"]]
    fix_res = [x for x in items if x["rule"] in FIX]
    print("%s: 修复类 %d | 中文行引号 %d" % (slug, len(fix_res), len(zh_curly)))
    for x in zh_curly[:8]:
        print("   L%s %s" % (x["line"], x["detail"][:96]))
