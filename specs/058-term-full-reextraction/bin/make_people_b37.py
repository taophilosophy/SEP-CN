# -*- coding: utf-8 -*-
"""人名第三十七批（2026-11-24，中文源补证）：二人取汉名。

Klima、Carston；Grene、Kretzmann、Spade、Pruss、Ofra Magidor、Grabmann 查无留证。
"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

EV = 'people-cnweb-2026-11-24-b37.md'

FIX = [
    ('Klima, Gyula', 'G. 克里马', None,
     '中文定名补证：G. 克里马《奎因、怀曼与布里丹：本体论约定的三种方法》（胡龙彪、鲁旭东译），'
     '《世界哲学》2012 年第 1 期作者署名“G.克里马”；胡龙彪《布里丹的有效推论思想的逻辑分析》'
     '（2015）述“布里丹问题研究专家G. 克里马（Klima）”（2026-11-24 查，凭证 %s）' % EV),
    ('Robyn Carston', '罗宾·卡斯顿', None,
     '中文定名补证：何自然、冉永平《〈关联性：交际与认知〉导读》（外语教学与研究出版社 2001）'
     '作“罗宾•卡斯顿（Robyn Carston）”；《新编语用学概论》作“英国的语用学者卡斯顿'
     '（Carston, 1998）”（2026-11-24 查，凭证 %s）' % EV),
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
    print('改行', key, '->', cells[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
