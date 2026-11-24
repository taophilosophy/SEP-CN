# -*- coding: utf-8 -*-
"""人名第二十八批（2026-11-24，中文源补证）：Pippin、Kornblith、Stratton-Lake 取中译本/期刊定名。"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
EV = 'people-cnweb-2026-11-24-b28.md'

# (键, 新译法, 新别名或 None, 追加依据)
FIX = [
    ('Robert Pippin', '罗伯特·皮平', None,
     '中文定名补证：中译本《黑格尔的观念论：自意识的满足》（陈虎平译，华夏出版社 2006，'
     'ISBN 9787508039541）作者署名“罗伯特·皮平”；卿文光评论文（《博览群书》2007 年第 7 期）'
     '同（2026-11-24 查，凭证 %s）' % EV),
    ('Hilary Kornblith', '希拉里·科恩布里斯', None,
     '中文定名补证：《世界哲学》2014 年第 4 期“直觉、自然主义与认识论——H. 科恩布里斯教授访谈”'
     '（方环非访译）作“科恩布里斯”；无中译本专书，取期刊定名（2026-11-24 查，凭证 %s）' % EV),
    ('Philip Stratton-Lake', '菲利普·斯特拉顿-莱克', '斯特拉顿·莱克',
     '中文定名补证：中译本《正当与善》（罗斯著，氏编，林南译，上海译文出版社 2008／2016，'
     'ISBN 9787532771035）CIP 著录“斯特拉顿·莱克（Stratton-Lake, P.）编”，封面作'
     '“菲利普·斯特拉顿-莱克”（2026-11-24 查，凭证 %s）' % EV),
]

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0]:
            idx.setdefault(norm_key_quote(cells[0]), i)
n = 0
for key, zh, alias, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    cells[2] = zh
    if alias:
        cells[1] = alias if cells[1] in ('—', '') else cells[1] + ' / ' + alias
    if note not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    print('改行', key, '|', cells[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
