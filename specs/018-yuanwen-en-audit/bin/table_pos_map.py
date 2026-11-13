# -*- coding: utf-8 -*-
"""把每个顶层表的容器链与块模型对账：栈扫容器链 + 逐块定位。"""
import re
import sys

sys.path.insert(0, '.')
from tools import parser, yuanwen  # noqa: E402
from tools.common import read_text, repo_path  # noqa: E402

CONTAINERS = {'li', 'dd', 'dt', 'blockquote', 'figure', 'div', 'td', 'th', 'table',
              'ul', 'ol', 'dl', 'p'}
TAG_RE = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>', re.I)

slug = sys.argv[1]
html = read_text(repo_path('en', slug, 'index.html'))
m, e = parser.HEAD_RE.search(html), parser.TAIL_RE.search(html)
article = html[m.end():e.start()]
article = yuanwen.strip_closed_comments(article)
article, _ = yuanwen.protect_cross_block_math(article)

stack = []
print('--- 栈扫：每个 <table 的容器链 ---')
for mm in TAG_RE.finditer(article):
    close, name, selfclose = mm.group(1), mm.group(2).lower(), mm.group(3)
    if name not in CONTAINERS:
        continue
    if close:
        if stack and stack[-1][0] == name:
            stack.pop()
    elif not selfclose:
        stack.append((name, mm.start()))
        if name == 'table':
            chain = [n for n, _ in stack]
            print(f'@{mm.start():7d} 链: {" > ".join(chain[-6:])}')

print('--- 块模型：table 开标签落点 ---')
blocks = yuanwen.extract_blocks_raw(article)
for bi, b in enumerate(blocks):
    st = None
    for tm in re.finditer(r'<table[\s>]', b['inner'], re.I):
        # 计算该表在 article 中的绝对位置（块 inner 是原文切片）
        print(f'块#{bi} type={b["type"]}  inner 相对表@{tm.start()}')
