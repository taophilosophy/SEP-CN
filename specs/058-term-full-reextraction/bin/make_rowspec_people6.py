# -*- coding: utf-8 -*-
"""人名第六批 rowspec（2026-11-23）：三人，Wikidata 取证，汉名联网核证。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-23-b6.tsv'

PEOPLE = [
    ('Andrew von Hirsch', '安德烈亚斯·冯·赫希（亦作“安德鲁·冯·赫希”）',
     '英国（生于瑞士苏黎世）', '1934–2026', 'Q4759036',
     '量刑该当模式；汉名据《该当量刑概论》译者与公众号文章（2026-11-23 检索）'),
    ('Evelyn Fox Keller', '伊夫林·福克斯·凯勒', '美国', '1936–2023',
     'Q239131', '科学哲学家、女性主义科学研究者'),
    ('Leon van der Torre', 'Leon van der Torre（无通行汉名，保留英文原名）',
     '荷兰', '1968–', 'Q23038082', '道义逻辑与规范系统研究者'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '籍属/生卒联网查证：Wikidata %s（2026-11-23 查，凭证 %s）；%s'
                          % (qid, EV, note),
                 'date': '2026-11-23'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch13-people.json')
json.dump({'batch': '058-batch13-people', 'date': '2026-11-23',
           'scope': '人名第六批（Wikidata 逐人取证）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
