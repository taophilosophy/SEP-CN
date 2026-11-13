# -*- coding: utf-8 -*-
"""递归追踪 li/dd 内表的流失点：walk 块树 → 定位表所在容器链。"""
import re
import sys

sys.path.insert(0, '.')
from tools import parser, yuanwen  # noqa: E402
from tools.common import read_text, repo_path  # noqa: E402


def walk(blocks, path, slug, depth=0):
    for bi, b in enumerate(blocks):
        n = len(re.findall(r'<table[\s>]', b['inner'], re.I))
        if n:
            print('  ' * depth + f'块#{bi} type={b["type"]} attrs={b["attrs"][:60]!r} 表数={n}')
            if b['type'] in ('ul', 'ol'):
                items = re.split(r'<li[^>]*>', b['inner'], flags=re.I)[1:]
                hits = ['<table' in it for it in items]
                print('  ' * depth + f'  li 项数={len(items)} 含表分布={hits}')
                idx = hits.index(True) if True in hits else -1
                if idx >= 0:
                    it = re.sub(r'</li>\s*$', '', items[idx].strip(), flags=re.I)
                    sm = re.search(r'(<ul[^>]*>.*</ul>|<ol[^>]*>.*</ol>)\s*$', it, re.S | re.I)
                    print('  ' * depth + f'  项尾有子列表: {bool(sm)}; 项内 <table 前 100 字符:')
                    ti = it.find('<table')
                    print('  ' * depth + '   ', repr(it[max(0, ti - 160):ti + 40]))
            if b['type'] in ('figure', 'blockquote', 'bib-container', 'preamble'):
                walk(yuanwen.extract_blocks_raw(b['inner']),
                     path + [f'{b["type"]}#{bi}'], slug, depth + 1)
            if b['type'] == 'dl':
                for dm in re.finditer(r'<dt[^>]*>(.*?)</dt>|<dd[^>]*>(.*?)</dd>',
                                      b['inner'], re.S | re.I):
                    seg = dm.group(1) if dm.group(1) is not None else dm.group(2)
                    if '<table' in seg:
                        print('  ' * depth + f'  dl {"dt" if dm.group(1) is not None else "dd"} 内含表')


for slug in sys.argv[1:]:
    print(f'===== {slug} =====')
    html = read_text(repo_path('en', slug, 'index.html'))
    m, e = parser.HEAD_RE.search(html), parser.TAIL_RE.search(html)
    article = html[m.end():e.start()]
    article = yuanwen.strip_closed_comments(article)
    article, stash = yuanwen.protect_cross_block_math(article)
    walk(yuanwen.extract_blocks_raw(article), [], slug)
