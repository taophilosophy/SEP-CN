# -*- coding: utf-8 -*-
"""第九批补记（2026-11-24）：Levy / Stilz / Risse 三人籍属与生卒定点回填。

三人在 batch35 落册时 Wikidata 项缺 P27（Levy 亦缺网页前未核），
经补充取证（results/people-wikidata-2026-11-24-b9-supplement.md）回填。
"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

EV = 'people-wikidata-2026-11-24-b9.tsv'
SUP = 'people-wikidata-2026-11-24-b9-supplement.md'
# (键, 籍属, 生卒, 追加依据)
FIX = [
    ('Neil Levy', '澳大利亚（生于南非）', '1967–',
     'Contemporary Authors（encyclopedia.com）记 1967-11-06 生于约翰内斯堡、'
     '澳大利亚籍；Macquarie 官页记 Professor in Philosophy（2026-11-24 查，'
     '见 %s）' % SUP),
    ('Anna Stilz', '—', '1976–',
     'Princeton/UC Berkeley 官页未载国籍与生年，籍属不猜；生年取 Wikidata '
     'Q112555472（2026-11-24 查，见 %s）' % SUP),
    ('Mathias Risse', '德国／美国', '1970–',
     '本人 CV 记生于帕德博恩、2008 年入美国籍并保留德国籍；生年取 Wikidata '
     'Q112487296（2026-11-24 查，见 %s）' % SUP),
]

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0] and not set(cells[0]) <= set(':-— '):
            idx[norm_key_quote(cells[0])] = i
n = 0
for key, aff, dates, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    if aff != '—' and cells[3] in ('—', ''):
        cells[3] = aff
    if dates != '—' and cells[4] in ('—', ''):
        cells[4] = dates
    if 'supplement' not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；补记：' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    n += 1
    print('%-16s %s｜%s' % (key, cells[3], cells[4]))
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('written', n)
