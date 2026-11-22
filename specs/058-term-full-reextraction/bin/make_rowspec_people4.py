# -*- coding: utf-8 -*-
"""人名第四批 rowspec：14 位真缺项。"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-22-b4.tsv'
DATA = [
    ('van Heijenoort, Jean / Jean van Heijenoort', 'Jean van Heijenoort',
     '让·范·海杰诺特', '法国／美国／数学史与逻辑史', '1912–1986', 'Q449711', ''),
    ('Van Gulick, Robert / Robert Van Gulick', 'Robert Van Gulick',
     '罗伯特·范·古利克', '美国／心灵哲学', '1949–', 'Q93226438', ''),
    ('Carroll, Lewis / Lewis Carroll', 'Lewis Carroll', '刘易斯·卡罗尔',
     '英国／作家与逻辑学家', '1832–1898', 'Q38082', ''),
    ('Maxwell, James Clerk / James Clerk Maxwell', 'James Clerk Maxwell',
     '詹姆斯·克拉克·麦克斯韦', '英国（苏格兰）／物理学', '1831–1879', 'Q9095', ''),
    ('Skinner, Quentin / Quentin Skinner', 'Quentin Skinner', '昆廷·斯金纳',
     '英国／思想史', '1940–', 'Q465807', ''),
    ('Enoch, David / David Enoch', 'David Enoch', '大卫·伊诺克',
     '以色列／元伦理学', '1971–', 'Q6871095', ''),
    ('Churchland, Patricia / Patricia Churchland', 'Patricia Churchland',
     '帕特里夏·丘奇兰德', '加拿大／美国／神经哲学', '1943–', 'Q242616', ''),
    ('Laudan, Larry / Larry Laudan', 'Larry Laudan', '拉里·劳丹',
     '美国／科学哲学', '1941–2022', 'Q1370686', ''),
    ('Ganeri, Jonardon / Jonardon Ganeri', 'Jonardon Ganeri', '乔纳登·加内里',
     '英国／印度哲学', '1963–', 'Q54495633', ''),
    ('Bealer, George / George Bealer', 'George Bealer', '乔治·比勒',
     '美国／哲学与逻辑', '1944–2025', 'Q120979102', ''),
    ('Hart, H. L. A. / H. L. A. Hart', 'H. L. A. Hart', '哈特',
     '英国／法哲学', '1907–1992', 'Q374834', ''),
    ('Le Poidevin, Robin / Robin Le Poidevin', 'Robin Le Poidevin',
     '罗宾·勒·普瓦德万', '英国／形而上学', '1962–', 'Q7352609', ''),
    ('De Brigard, Felipe / Felipe De Brigard', 'Felipe De Brigard',
     '费利佩·德·布里加德', '哥伦比亚／美国／心灵哲学', '—', 'Q87886940',
     '生卒未详（Wikidata 无生卒数据）'),
    ('van Roojen, Mark / Mark van Roojen', 'Mark van Roojen', '马克·范·罗延',
     '美国／元伦理学', '1958–', 'Q107121659', ''),
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
json.dump({'batch': '058-batch8-people', 'date': '2026-11-22',
           'scope': '人名第四批：真缺项 14 人',
           'evidence': 'specs/058-term-full-reextraction/results/' + EV,
           'rows': rows},
          open(os.path.join(RES, 'rowspec-batch8-people.json'), 'w',
               encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
open(os.path.join(RES, EV), 'w', encoding='utf-8', newline='\n').write(
    '\n'.join(ev) + '\n')
print('rows', len(rows))
