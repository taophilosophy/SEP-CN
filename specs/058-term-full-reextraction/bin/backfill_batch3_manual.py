# -*- coding: utf-8 -*-
"""第三批人工复核后的定点回填（只写确证项，撞名项记排除）。"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

EV = 'backfill-auto-2026-11-23.tsv'
# (键, 籍属, 生卒, QID, 备注)
FIX = [
    ('Melissus', '古希腊', '约前5世纪（活动期）', 'Q233711',
     '生卒依条目描述“前5世纪爱利亚哲学家”改记活动期'),
    ('Menedemus of Pyrrha', '古希腊', '约前350–', 'Q981586',
     'Wikidata 生年约前350，卒年缺，记活动期起讫'),
    ('Metrodorus of Chios', '古希腊', '约前4世纪（活动期）', 'Q535769',
     '生卒依条目描述“前4世纪哲学家”改记活动期'),
    ('Michael Smith', '澳大利亚', '1954–', 'Q6828096',
     '换条目：道德哲学家 Michael A. Smith（原命中记者条目）'),
    ('Moltmann, Friederike', '德国／法国', '—', 'Q42253399',
     '描述称德国语言学家与哲学家，P27 记法国籍'),
    ('Omori, Hitoshi', '日本', '—', 'Q137382146', '日本逻辑学家，无生卒数据'),
    ('Paroush, Jacob', '以色列', '—', 'Q134706625',
     '生年 2000 为 Wikidata 占位值，不写生卒'),
    ('Phaedo of Elis', '古希腊', '约前4世纪（活动期）', 'Q380190',
     '生卒依条目描述“前4世纪哲学家”改记活动期'),
    ('Retoré, Christian', '—', '1964–', 'Q57417373', 'P27 缺籍，只记生年'),
    ('Robert Adams', '美国', '1937–2024', 'Q5254926',
     '换条目：哲学家 Robert Merrihew Adams（原命中科幻小说家）'),
    ('Roush, Sherrilyn', '美国', '—', 'Q7495367', '美国认识论学家，无生卒数据'),
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
for key, aff, dates, qid, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    if cells[3] in ('—', '') and aff != '—':
        cells[3] = aff
    if cells[4] in ('—', '') and dates != '—':
        cells[4] = dates
    ev = '籍属/生卒联网查证：Wikidata %s（2026-11-23 查，凭证 %s）%s' % (
        qid, EV, '；' + note if note else '')
    if 'Wikidata %s' % qid not in cells[6]:
        cells[6] = cells[6].rstrip('|') + '；' + ev
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    n += 1
    print('%-24s %s｜%s' % (key, cells[3], cells[4]))
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('written', n)
