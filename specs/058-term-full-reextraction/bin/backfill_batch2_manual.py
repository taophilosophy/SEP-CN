# -*- coding: utf-8 -*-
"""第二批人工复核后的定点回填（只写 5 条确证项）。"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

EV = 'backfill-auto-2026-11-23.tsv'
FIX = [
    ('Gale, George', '—', '1943–', 'Q133521156'),
    ('Gopal Sreenivasan', '加拿大', '—', 'Q108581195'),
    ('Hippobotus', '希腊', '—', 'Q2614752'),
    ('Kolodny, Niko', '美国', '—', 'Q16403824'),
    ('Lorki, Joshua', '西班牙／犹太改宗者', '1400–1419', 'Q462009'),
]
p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0] and not set(cells[0]) <= set(':-— '):
            idx.setdefault(norm_key_quote(cells[0]), i)
n = 0
for key, aff, dates, qid in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    if cells[3] in ('—', '') and aff != '—':
        cells[3] = aff
    if cells[4] in ('—', '') and dates != '—':
        cells[4] = dates
    ev = '籍属/生卒联网查证：Wikidata %s（2026-11-23 查，凭证 %s）' % (qid, EV)
    if ev not in cells[6]:
        cells[6] = cells[6].rstrip('|') + '；' + ev
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    n += 1
    print('%-24s %s｜%s' % (key, cells[3], cells[4]))
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('written', n)
