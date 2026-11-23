# -*- coding: utf-8 -*-
"""人名第五批 rowspec（2026-11-23）：Wikidata 取籍属/生卒，汉名按通行音译。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-23-b5.tsv'

PEOPLE = [
    ('Iris Marion Young', '艾丽斯·马里恩·扬', '美国', '1949–2006', 'Q543381',
     '政治哲学家（PU），正义与差异政治'),
    ('Saunders Mac Lane', '桑德斯·麦克莱恩', '美国', '1909–2005', 'Q441223',
     '数学家，范畴论创立者之一（与 Eilenberg）'),
    ('Frans van Eemeren', '弗兰斯·范·埃默伦', '荷兰', '1946–', 'Q1445486',
     '语用论辩学（pragma-dialectics）奠基者'),
    ('Francisco Miró Quesada', '弗朗西斯科·米罗·克萨达', '秘鲁', '1918–2019',
     'Q5483714', '秘鲁哲学家，逻辑学与“无墙之城”'),
    ('Abraham ibn Daud', '亚伯拉罕·伊本·达乌德', '西班牙（安达卢斯）',
     '约1110–约1180', 'Q330821', '《传统之冠》作者，亚里士多德主义犹太哲学家'),
]

rows = []
ev = ['en\tqid\tlabel\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行音译；籍属/生卒联网查证：Wikidata %s'
                          '（2026-11-23 查，凭证 %s）；%s' % (qid, EV, note),
                 'date': '2026-11-23'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch12-people.json')
json.dump({'batch': '058-batch12-people', 'date': '2026-11-23',
           'scope': '人名第五批（Wikidata 逐人取证）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results',
                     EV), 'w', encoding='utf-8', newline='\n').write(
    '\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
