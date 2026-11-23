# -*- coding: utf-8 -*-
"""人名第十九批 rowspec（2026-11-24）：人工智能、道德心理学与公共选择 9 人。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b19.tsv'

PEOPLE = [
    ('John McCarthy', '约翰·麦卡锡', '美国', '1927–2011', 'Q92739',
     '人工智能奠基者（Lisp、“人工智能”名称）；经英文维基“John McCarthy '
     '(computer scientist)”反查得 QID'),
    ('Jonathan Haidt', '乔纳森·海特', '美国', '1963–', 'Q845573',
     '道德基础理论（《正义之心》）'),
    ('Gerd Gigerenzer', '格尔德·吉仁泽', '德国', '1947–', 'Q108184',
     '生态理性与启发式（《简捷启发式》）'),
    ('Gordon Tullock', '戈登·塔洛克', '美国', '1922–2014', 'Q518859',
     '公共选择理论（与 Buchanan 合作）'),
    ('Hugo Mercier', '雨果·梅西耶', '法国', '1980–', 'Q57410912',
     '论证理论（与 Sperber 合著《The Enigma of Reason》）'),
    ('Geoffrey Brennan', '杰弗里·布伦南', '澳大利亚', '1944–2022', 'Q4096295',
     '公共选择与民主理论（与 Lomasky 合著《Democracy and Decision》）'),
    ('William MacAskill', '威廉·麦卡斯基尔', '英国', '1987–', 'Q20684655',
     '有效利他主义与长期主义（《What We Owe the Future》）'),
    ('Joshua Greene', '约书亚·格林', '美国', '1974–', 'Q16224624',
     '道德心理学与神经伦理学（《Moral Tribes》）；经英文维基'
     '“Joshua Greene (psychologist)”反查得 QID'),
    ('Max Velmans', '马克斯·维尔曼斯', '英国', '1942–', 'Q1399051',
     '意识研究（反身一元论）'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行译名；籍属/生卒联网查证：Wikidata %s'
                          '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note),
                 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch45-people.json')
json.dump({'batch': '058-batch45-people', 'date': '2026-11-24',
           'scope': '人名第十九批（9 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
