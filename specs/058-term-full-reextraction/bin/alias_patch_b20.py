# -*- coding: utf-8 -*-
"""人名别名补记（2026-11-24，第二十批配套）：Mengzi 补拉丁化语料形 Mencius。"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import person_path

FIX = [('Mengzi', 'Mencius', '拉丁化名 Mencius 即孟子（Mengzi）')]
EV = 'people-alias-2026-11-24-b20.tsv'

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
n = 0
ev = ['key\talias\t判据']
for i, l in enumerate(lines):
    if not l.startswith('| '):
        continue
    cells = [c.strip() for c in l.strip().strip('|').split('|')]
    if len(cells) != 8:
        continue
    hit = [x for x in FIX if x[0] == cells[0]]
    if not hit:
        continue
    _, alias, why = hit[0]
    if alias in cells[1]:
        continue
    cells[1] = alias if cells[1] in ('—', '') else cells[1] + ' / ' + alias
    note = '别名“%s”为 058 语料形，与前项同一人（2026-11-24 核对，凭证 %s）；%s' % (
        alias, EV, why)
    cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    ev.append('%s\t%s\t%s' % (cells[0], alias, why))
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
io.open('specs/058-term-full-reextraction/results/' + EV, 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('别名补记', n)
