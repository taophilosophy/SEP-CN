# -*- coding: utf-8 -*-
"""第五批人工复核后的定点回填＋两行籍属污染修正。"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

EV = 'backfill-auto-2026-11-23.tsv'
FIX = [
    ('Shakespeare', '英国', '1564–1616', 'Q692', '剧作家与诗人，与本条目人物一致'),
    ('Stephen Schiffer', '美国', '1940–', 'Q7610475', '哲学家'),
    ('Swartz, Norman', '—', '1939–', 'Q7052835', 'P27 缺籍，只记生年'),
    ('Tartaglia', '意大利', '1499–1557', 'Q201543', '数学家'),
    ('Theocritus', '古希腊', '约前3世纪（活动期）', 'Q219484',
     '生卒依条目描述“前3世纪诗人”改记活动期'),
    ('von Fintel, Kai', '德国', '—', 'Q141310016', '语言学家'),
    ('Weber, Zach', '新西兰', '—', 'Q102394819', '逻辑学家与哲学家'),
    ('Wetzel, Linda', '美国', '1951–', 'Q120670188', '哲学家'),
    ('Wheeler, Michael', '英国', '1960–', 'Q95330452', '哲学家'),
    ('Schubert, Lenhart', '美国', '—', 'Q15995453', '人工智能研究者'),
]
# 籍属列误并入学科词的两行（本线 2026-11-22 登记时带入）
CLEAN = [('Van Cleve, James / James Van Cleve', '美国'),
         ('van Gelder, Tim / Tim van Gelder', '澳大利亚')]
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
    ev = '籍属/生卒联网查证：Wikidata %s（2026-11-23 查，凭证 %s）；%s' % (
        qid, EV, note)
    if 'Wikidata %s' % qid not in cells[6]:
        cells[6] = cells[6].rstrip('|') + '；' + ev
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    n += 1
    print('%-22s %s｜%s' % (key, cells[3], cells[4]))
for key, aff in CLEAN:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    if cells[3] != aff:
        print('籍属修正 %-38s %s → %s' % (key, cells[3], aff))
        cells[3] = aff
        lines[i] = '| ' + ' | '.join(cells) + ' |'
        n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('written', n)
