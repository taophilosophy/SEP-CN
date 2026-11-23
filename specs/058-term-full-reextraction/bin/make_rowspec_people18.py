# -*- coding: utf-8 -*-
"""人名第十八批 rowspec（2026-11-24）：认识论、美学、社会理论、法哲学 12 人。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b18.tsv'
EN = '（无通行汉名，保留英文原名）'

PEOPLE = [
    ('John Greco', '约翰·格雷科', '美国', '1961–', 'Q6236141',
     '德性认识论（reliabilism 与 virtue epistemology）'),
    ('José Medina', '何塞·梅迪纳', '西班牙／美国', '1968–', 'Q27983588',
     '认知不正义（《The Epistemology of Resistance》）'),
    ('Hilary Kornblith', 'Hilary Kornblith' + EN, '美国', '1954–', 'Q5761008',
     '自然主义认识论（《Knowledge and its Place in Nature》）'),
    ('Thomas Luckmann', '托马斯·卢克曼', '美国／奥地利', '1927–2016', 'Q60412',
     '与社会建构论（与 Berger 合著《现实的社会建构》）'),
    ('Pierre Bourdieu', '皮埃尔·布尔迪厄', '法国', '1930–2002', 'Q156268',
     '场域、惯习与文化资本（《区分》）'),
    ('Dorothy Emmet', '多萝西·埃米特', '英国', '1904–2000', 'Q1250294',
     '形而上学与社会哲学（《Rules and Processes》）'),
    ('Crispin Sartwell', 'Crispin Sartwell' + EN, '美国', '1958–', 'Q5186051',
     '美学与政治哲学（《Six Names of Beauty》）'),
    ('Marcel Mauss', '马塞尔·莫斯', '法国', '1872–1950', 'Q295393',
     '人类学（《论馈赠》），涂尔干学派'),
    ('George Lakoff', '乔治·莱考夫', '美国', '1941–', 'Q313772',
     '概念隐喻理论（《我们赖以生存的隐喻》）'),
    ('Stephen C. Pepper', '斯蒂芬·佩珀', '美国', '1891–1972', 'Q7610222',
     '形而上学的世界假说（World Hypotheses）'),
    ('Richard Foley', '理查德·福利', '—', '1947–', 'Q134705595',
     '认识论（工作信念与理智自主）；Wikidata 无 P27，籍属留白'),
    ('Neil MacCormick', '尼尔·麦考密克', '英国（苏格兰）', '1941–2009',
     'Q2136132', '制度法理论与法律实证主义'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行音译；籍属/生卒联网查证：Wikidata %s'
                          '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note),
                 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch44-people.json')
json.dump({'batch': '058-batch44-people', 'date': '2026-11-24',
           'scope': '人名第十八批（12 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
