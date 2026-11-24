# -*- coding: utf-8 -*-
"""人名第二十七批（2026-11-24，中文源补证）：Sugden、Galston 取中译本署名定名。"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
EV = 'people-cnweb-2026-11-24-b27.md'

# (键, 新译法, 追加依据)
FIX = [
    ('Robert Sugden', '罗伯特·萨格登',
     '中文定名补证：中译本《权利、合作与福利的经济学》（方钦译，上海财经大学出版社 2008 初版；'
     '复旦大学出版社 2022 新译版，ISBN 9787309159622）作者署名“罗伯特·萨格登”，'
     '澎湃新闻·上海书评方钦文、中华读书报 2023-03-15 均同（2026-11-24 查，凭证 %s）' % EV),
    ('William Galston', '威廉·盖尔斯敦',
     '中文定名补证：中译本《自由多元主义》（佟德志译，江苏人民出版社 2005，ISBN 9787214040213）'
     '作者署名“威廉·A·盖尔斯敦”；《自由多元主义的实践》（江苏人民 2010）同；《浙江学刊》2006'
     ' 年第 4 期佟德志文作“盖尔斯顿”异写（2026-11-24 查，凭证 %s）' % EV),
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
for key, zh, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    cells[2] = zh
    if note not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    print('改行', key, '|', cells[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
