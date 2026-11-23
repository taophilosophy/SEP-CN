# -*- coding: utf-8 -*-
"""人名第二十四批 rowspec（2026-11-24）：中国哲学英语学界与当代 3 人。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b24.tsv'

PEOPLE = [
    ('Wm. Theodore de Bary', '狄百瑞', '美国', '1919–2017', '—',
     '新儒学研究奠基者（哥伦比亚大学，EALAC 讣告记 2017-07-14 卒，'
     '2026-11-24 查）；无 Wikidata 项'),
    ('Tu Weiming', '杜维明', '中国（生于昆明）', '1940–', 'Q710092',
     '第三代新儒家（《论道》）与哈佛燕京学社'),
    ('Chen Guying', '陈鼓应', '中国（福建）', '1935–', '—',
     '道家文献学与「道家主干说」（《老子今注今译》）；人民网／光明网记 1935 年'
     '生于福建长汀，北京大学哲学系人文讲席教授（2026-11-24 查）；无 Wikidata 项'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    if qid == '—':
        basis = ('学界通行译名；籍属/生卒联网查证（2026-11-24 查，凭证 %s）；%s'
                 % (EV, note))
    else:
        basis = ('学界通行译名；籍属/生卒联网查证：Wikidata %s'
                 '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note))
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates, 'basis': basis, 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch50-people.json')
json.dump({'batch': '058-batch50-people', 'date': '2026-11-24',
           'scope': '人名第二十四批（3 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
