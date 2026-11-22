#!/usr/bin/env python3
"""specs/057 s3 取证：抽取 en/<slug>/index.html 正文首段纯文本，核实条目主题归属。

用法：python firstpara.py <slug> [<slug> ...]
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def first_paras(slug, n=2, width=420):
    p = ROOT / "en" / slug / "index.html"
    if not p.exists():
        return [f"（无 en/{slug}/index.html）"]
    t = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<div id="main-text">(.*?)$', t, re.S)
    if m:
        t = m.group(1)
    t = re.sub(r"<(script|style|math)[^>]*>.*?</\1>", " ", t, flags=re.S)
    paras = []
    for pm in re.finditer(r"<p[^>]*>(.*?)</p>", t, re.S):
        s = re.sub(r"<[^>]+>", "", pm.group(1))
        s = html.unescape(s).replace("\u200b", " ")
        s = re.sub(r"\s+", " ", s).strip()
        if len(s) > 120:
            paras.append(s[:width])
        if len(paras) >= n:
            break
    return paras or ["（未取到首段）"]


for slug in sys.argv[1:]:
    print(f"=== {slug}")
    for i, p in enumerate(first_paras(slug), 1):
        print(f"  [{i}] {p}")
