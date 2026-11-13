# -*- coding: utf-8 -*-
"""全库普查两类真实缺陷的完整波及面（仅 en/<slug>/index.html，注释区忽略）：
A. 表格嵌在 <li>/<dd>/<dt> 内——被行内剥壳丢失。
B. 嵌套表（table 内 table）——被降级为（嵌套表：…）。
另统计嵌套表内非白名单标签清单（Fix B 消毒范围）。
"""
import os
import re
from collections import Counter

TAG_RE = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>', re.I)
SAFE = set('a abbr b blockquote br caption cite code dd del details div dl dt em '
           'figcaption figure h1 h2 h3 h4 h5 h6 hr i img ins kbd li mark ol p pre '
           'q s samp small span strong sub summary sup table tbody td tfoot th '
           'thead tr u ul var video audio source iframe'.split())
CONTAINERS = {'li', 'dd', 'dt', 'blockquote', 'figure', 'div', 'td', 'th', 'table',
              'ul', 'ol', 'dl', 'p'}


def visible(html):
    out, last = [], 0
    for m in re.finditer(r'<!--.*?-->', html, re.S):
        out.append((last, m.start()))
        last = m.end()
    out.append((last, len(html)))
    return ''.join(html[a:b] for a, b in out)


def scan(html):
    """栈扫描全部容器 → [(depth, ctx, table_html)]。"""
    stack = []
    out = []
    for m in TAG_RE.finditer(html):
        close, name, selfclose = m.group(1), m.group(2).lower(), m.group(3)
        if name not in CONTAINERS:
            continue
        if close:
            if stack and stack[-1][0] == name:
                nm, st = stack.pop()
                if nm == 'table':
                    out.append((len([1 for n, _ in stack if n == 'table']) + 1,
                                _ctx_of(stack), html[st:m.end()]))
        elif not selfclose:
            stack.append((name, m.start()))
    return out


def _ctx_of(stack):
    for nm, _ in reversed(stack):
        if nm in ('li', 'dd', 'dt', 'blockquote', 'figure'):
            return nm
        if nm == 'table':
            return 'td'
        if nm == 'div':
            return 'div'
        if nm == 'p':
            return 'p'
    return 'body'


badA = {}
badB = {}
tagset = Counter()
slugs = 0
for root, dirs, fns in os.walk('en'):
    if 'index.html' not in fns:
        continue
    slug = os.path.basename(root)
    slugs += 1
    html = visible(open(os.path.join(root, 'index.html'), encoding='utf-8', errors='replace').read())
    tabs = scan(html)
    for d, ctx, seg in tabs:
        if d == 1 and ctx in ('li', 'dd', 'dt'):
            badA.setdefault(slug, Counter())[ctx] += 1
        rest = re.sub(r'^<table[^>]*>', '', seg, count=1, flags=re.I)
        if '<table' in rest:
            badB[slug] = badB.get(slug, 0) + 1
            for tm in re.finditer(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)', rest, re.I):
                nm = tm.group(2).lower()
                if nm not in SAFE and nm != 'table':
                    tagset[nm] += 1

print('扫描词条数:', slugs)
print('== A: li/dd/dt 内顶层表 ==')
for s, ctxs in sorted(badA.items()):
    print(f'  {s}: {dict(ctxs)}')
print('合计词条:', len(badA), '表数:', sum(sum(c.values()) for c in badA.values()))
print()
print('== B: 嵌套表 ==')
for s, n in sorted(badB.items()):
    print(f'  {s}: {n}')
print('合计词条:', len(badB), '嵌套表数:', sum(badB.values()))
print()
print('== 嵌套表内非白名单标签 ==', dict(tagset))
