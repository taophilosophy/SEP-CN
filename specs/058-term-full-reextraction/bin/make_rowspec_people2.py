# -*- coding: utf-8 -*-
"""人名第二批 rowspec：15 位真缺项（Anne Conway 已登记为 Conway, Lady Anne，剔除）。"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-22-b2.tsv'
DATA = [
    ('van Gelder, Tim / Tim van Gelder', 'Tim van Gelder', '蒂姆·范海尔德',
     '澳大利亚／认知科学', '—', 'Q7804551', '生卒未详（Wikidata 无生卒数据）'),
    ('van Lambalgen, Michiel / Michiel van Lambalgen', 'Michiel van Lambalgen',
     '米希尔·范·兰巴尔根', '荷兰／逻辑与认知科学', '1954–', 'Q6837395', ''),
    ('Rosen, Gideon / Gideon Rosen', 'Gideon Rosen', '吉迪恩·罗森',
     '美国／哲学', '1962–', 'Q20732338', ''),
    ('Darwall, Stephen / Stephen Darwall', 'Stephen Darwall', '斯蒂芬·达沃尔',
     '美国／道德哲学', '1946–', 'Q7609017', ''),
    ('Price, Huw / Huw Price', 'Huw Price', '休·普莱斯',
     '澳大利亚／哲学', '1953–', 'Q11710343', ''),
    ('Shelby, Tommie / Tommie Shelby', 'Tommie Shelby', '汤米·谢尔比',
     '美国／政治哲学', '1967–', 'Q7819130', ''),
    ('Elster, Jon / Jon Elster', 'Jon Elster', '约恩·埃尔斯特',
     '挪威／美国／政治哲学', '1940–', 'Q468043', ''),
    ('Schroeder, Mark / Mark Schroeder', 'Mark Schroeder', '马克·施罗德',
     '美国／哲学', '1977–', 'Q93387536', ''),
    ('Barry, Brian / Brian Barry', 'Brian Barry', '布赖恩·巴里',
     '英国／美国／政治哲学', '1936–2009', 'Q911833', ''),
    ('Tye, Michael / Michael Tye', 'Michael Tye', '迈克尔·泰',
     '美国／心灵哲学', '1950–', 'Q708836', ''),
    ('Lugones, María / María Lugones', 'María Lugones', '玛丽亚·卢戈内斯',
     '阿根廷／美国／哲学', '1944–2020', 'Q6761379', ''),
    ('Shafer-Landau, Russ / Russ Shafer-Landau', 'Russ Shafer-Landau',
     '拉斯·谢弗-兰多', '美国／元伦理学', '1963–', 'Q7381231', ''),
    ('Boghossian, Paul / Paul Boghossian', 'Paul Boghossian', '保罗·博格霍西安',
     '美国／亚美尼亚裔／哲学', '1957–', 'Q2625853', ''),
    ('Wolf, Susan / Susan Wolf', 'Susan Wolf', '苏珊·沃尔夫',
     '美国／道德哲学', '1952–', 'Q7648308', ''),
    ('Martini Bonadeo, Cecilia / Cecilia Martini Bonadeo',
     'Cecilia Martini Bonadeo', '切契莉娅·马尔蒂尼·博纳代奥',
     '意大利／阿拉伯哲学', '1973–', 'Q109449315', ''),
]
rows = []
ev = ['en\tqid\tlabel\tdates\tdescription']
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
json.dump({'batch': '058-batch6-people', 'date': '2026-11-22',
           'scope': '人名第二批：真缺项 15 人（合写键别名去重后）',
           'evidence': 'specs/058-term-full-reextraction/results/' + EV,
           'rows': rows},
          open(os.path.join(RES, 'rowspec-batch6-people.json'), 'w',
               encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
open(os.path.join(RES, EV), 'w', encoding='utf-8', newline='\n').write(
    '\n'.join(ev) + '\n')
print('rows', len(rows))
