# -*- coding: utf-8 -*-
"""人名专批 rowspec：13 位真缺项，依据=学界通行音译＋Wikidata 生卒籍属。"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-22.tsv'
DATA = [
    ('Berlin, Isaiah / Isaiah Berlin', 'Isaiah Berlin', '以赛亚·伯林',
     '拉脱维亚生，英国／政治哲学', '1909–1997', 'Q205162', ''),
    ('Blackburn, Simon / Simon Blackburn', 'Simon Blackburn', '西蒙·布莱克本',
     '英国／哲学', '1944–', 'Q287357', ''),
    ('Korsgaard, Christine / Christine Korsgaard', 'Christine Korsgaard',
     '克里斯蒂娜·科尔斯戈德', '美国／哲学', '1952–', 'Q467518', ''),
    ('Strawson, Galen / Galen Strawson', 'Galen Strawson', '盖伦·斯特劳森',
     '英国／哲学', '1952–', 'Q1491810', ''),
    ('Dancy, Jonathan / Jonathan Dancy', 'Jonathan Dancy', '乔纳森·丹西',
     '英国／哲学', '1946–', 'Q2460022', ''),
    ('Fricker, Miranda / Miranda Fricker', 'Miranda Fricker', '米兰达·弗里克',
     '英国／哲学', '1966–', 'Q13522475', ''),
    ('Feinberg, Joel / Joel Feinberg', 'Joel Feinberg', '乔尔·范伯格',
     '美国／法律哲学', '1926–2004', 'Q1691712', ''),
    ('Van Parijs, Philippe / Philippe Van Parijs', 'Philippe Van Parijs',
     '菲利普·范帕里斯', '比利时／政治哲学', '1951–', 'Q1345191', ''),
    ('Van Cleve, James / James Van Cleve', 'James Van Cleve', '詹姆斯·范·克利夫',
     '美国／哲学', '—', 'Q133999881', '生卒未详（Wikidata 无生卒数据）'),
    ('Della Rocca, Michael / Michael Della Rocca', 'Michael Della Rocca',
     '迈克尔·德拉·罗卡', '美国／哲学', '—', 'Q105592457',
     '生卒未详（Wikidata 无生卒数据）'),
    ('Dutilh Novaes, Catarina / Catarina Dutilh Novaes',
     'Catarina Dutilh Novaes', '卡塔琳娜·杜蒂尔·诺瓦埃斯',
     '巴西／荷兰／哲学', '1976–', 'Q93221508', ''),
    ('Barcan Marcus, Ruth / Ruth Barcan Marcus', 'Ruth Barcan Marcus',
     '露丝·巴坎·马库斯', '美国／逻辑与哲学', '1921–2012', 'Q437943', ''),
    ('Suppes, Patrick / Patrick Suppes', 'Patrick Suppes', '帕特里克·苏佩斯',
     '美国／科学哲学', '1922–2014', 'Q323107', ''),
]
rows = []
for en, alias, zh, aff, dates, qid, note in DATA:
    basis = ('学界通行音译；籍属/生卒联网查证：Wikidata %s（2026-11-22 查，'
             '凭证 %s）' % (qid, EV))
    if note:
        basis += '；' + note
    rows.append({'en': en, 'alias': alias, 'zh': zh, 'table': 'person',
                 'affiliation': aff, 'dates': dates,
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-22'})
json.dump({'batch': '058-batch5-people', 'date': '2026-11-22',
           'scope': '人名专批：真缺项 13 人（合写键别名去重后）',
           'evidence': 'specs/058-term-full-reextraction/results/' + EV,
           'rows': rows},
          open(os.path.join(RES, 'rowspec-batch5-people.json'), 'w',
               encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('rows', len(rows))
