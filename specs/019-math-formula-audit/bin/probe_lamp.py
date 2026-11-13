# -*- coding: utf-8 -*-
r"""019 一次性探针：\lamp 宏在 SEP 页的定义来源。"""
import re

txt = open(r'en/actualism-possibilism-ethics/index.html', encoding='utf-8',
           errors='replace').read()
hits = list(re.finditer(re.escape('\\lamp'), txt))
print('lamp occurrences:', len(hits))
for m in hits[:3]:
    print(repr(txt[max(0, m.start() - 90):m.start() + 60]))
print('---- def/macros/MathJax config:')
for m in list(re.finditer(r'\\def\b[^<]{0,120}|macros\b[^<]{0,120}|MathJax\.Hub[^<]{0,60}', txt))[:6]:
    print(repr(m.group(0)[:160]))
