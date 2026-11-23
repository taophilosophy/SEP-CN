# -*- coding: utf-8 -*-
"""人名别名补记（2026-11-24）：Herschel / Price 两条既有行补语料形别名。

两行分别在 2026-11-14、2026-11-12 落册，键为规范标目形；058 语料按
“John Herschel”“H. H. Price” 出现，别名列原为“—”，故补记，键与译法不动。
"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

# 键 -> 追加别名
FIX = {
    'Herschel, John F. W.': 'John Herschel',
    'Price, Henry Habberley': 'H. H. Price',
}
EV = 'people-wikidata-2026-11-24-b9.tsv'
QID = {'Herschel, John F. W.': 'Q14278', 'Price, Henry Habberley': 'Q3751249'}

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
n = 0
for i, l in enumerate(lines):
    if not l.startswith('| '):
        continue
    cells = [c.strip() for c in l.strip().strip('|').split('|')]
    if len(cells) != 8:
        continue
    key = FIX.get(cells[0])
    if key is None:
        continue
    if key in cells[1]:
        print('已含别名，跳过', cells[0])
        continue
    cells[1] = key if cells[1] in ('—', '') else cells[1] + ' / ' + key
    ev = ('别名为 058 语料形，与前项同一人，Wikidata %s（2026-11-24 查，'
          '凭证 %s）' % (QID[cells[0]], EV))
    if 'alias' not in cells[6] and '别名' not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + ev
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    n += 1
    print('%-28s 别名 -> %s' % (cells[0], cells[1]))
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('written', n)
