# -*- coding: utf-8 -*-
"""人名第三批 rowspec：10 位真缺项。"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-22-b3.tsv'
DATA = [
    ('Kristeva, Julia / Julia Kristeva', 'Julia Kristeva', '朱莉娅·克里斯蒂娃',
     '法国／保加利亚／哲学与精神分析', '1941–', 'Q159876', ''),
    ('von Mises, Ludwig / Ludwig von Mises', 'Ludwig von Mises',
     '路德维希·冯·米塞斯', '奥地利／美国／经济学', '1881–1973', 'Q84233', ''),
    ('Haeckel, Ernst / Ernst Haeckel', 'Ernst Haeckel', '恩斯特·海克尔',
     '德国／生物学', '1834–1919', 'Q48246', ''),
    ('Gongsun Long', '公孙龙', '公孙龙', '中国（战国）／名家',
     '约前325–前250', 'Q1362266', '生卒据 Wikidata 前325／前250，取约数'),
    ('Llull, Ramon / Ramon Llull', 'Ramon Llull', '拉蒙·柳利',
     '马略卡／哲学与神学', '1232–1316', 'Q193660', ''),
    ('Mally, Ernst / Ernst Mally', 'Ernst Mally', '恩斯特·马利',
     '奥地利／哲学与逻辑', '1879–1944', 'Q90003', ''),
    ('Frank, Philipp / Philipp Frank', 'Philipp Frank', '菲利普·弗兰克',
     '奥地利／科学哲学', '1884–1966', 'Q79177', ''),
    ('Hill Collins, Patricia / Patricia Hill Collins', 'Patricia Hill Collins',
     '帕特里夏·希尔·柯林斯', '美国／社会学与哲学', '1948–', 'Q465252', ''),
    ('Den Uyl, Douglas / Douglas Den Uyl', 'Douglas Den Uyl',
     '道格拉斯·登·厄伊尔', '美国／政治哲学', '1950–', 'Q5301409', ''),
    ('Davies, Stephen / Stephen Davies', 'Stephen Davies', '斯蒂芬·戴维斯',
     '新西兰／美学', '1950–', 'Q7609025', ''),
]
rows, ev = [], ['en\tqid\tlabel\tdates\tdescription']
for en, alias, zh, aff, dates, qid, note in DATA:
    basis = ('学界通行音译；籍属/生卒联网查证：Wikidata %s（2026-11-22 查，'
             '凭证 %s）' % (qid, EV))
    if note:
        basis += '；' + note
    rows.append({'en': en, 'alias': alias, 'zh': zh, 'table': 'person',
                 'affiliation': aff, 'dates': dates,
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-22'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (alias, qid, alias, dates, aff))
json.dump({'batch': '058-batch7-people', 'date': '2026-11-22',
           'scope': '人名第三批：真缺项 10 人（含公孙龙）',
           'evidence': 'specs/058-term-full-reextraction/results/' + EV,
           'rows': rows},
          open(os.path.join(RES, 'rowspec-batch7-people.json'), 'w',
               encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
open(os.path.join(RES, EV), 'w', encoding='utf-8', newline='\n').write(
    '\n'.join(ev) + '\n')
print('rows', len(rows))
