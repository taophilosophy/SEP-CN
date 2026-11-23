# -*- coding: utf-8 -*-
"""人名第二十二批 rowspec（2026-11-24）：认知与语言学、进化论、STS 6 人。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b22.tsv'

PEOPLE = [
    ('Eleanor Rosch', '埃莉诺·罗施', '美国', '1938–', 'Q132475',
     '范畴心理学（原型理论、基本层级）'),
    ('Angelika Kratzer', '安杰利卡·克拉策', '德国／美国', '1948–', 'Q4762710',
     '模态语义学（条件句与 must/can 的 Kratzer 分析）'),
    ('Alison Wylie', '艾莉森·怀利', '加拿大', '1954–', 'Q4727229',
     '考古哲学与社会认识论'),
    ('Niles Eldredge', '奈尔斯·埃尔德雷奇', '美国', '1943–', 'Q451437',
     '间断平衡论（与 Stephen Jay Gould 合提）'),
    ('Steve Woolgar', '史蒂夫·伍尔加', '英国', '1950–', 'Q521895',
     '科学知识社会学（与 Latour 合著《实验室生活》）'),
    ('Paul Slovic', '保罗·斯洛维奇', '美国', '1938–', 'Q2062481',
     '风险感知与判断心理（psychometric paradigm）'),
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
out = os.path.join(RES, 'rowspec-batch48-people.json')
json.dump({'batch': '058-batch48-people', 'date': '2026-11-24',
           'scope': '人名第二十二批（6 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
