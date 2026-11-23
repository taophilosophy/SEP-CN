# -*- coding: utf-8 -*-
"""人名第七批 rowspec（2026-11-23）：四人，Wikidata 取证，汉名联网核证。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-23-b7.tsv'

PEOPLE = [
    ('Thomas Hurka', 'Thomas Hurka（无通行汉名，保留英文原名）', '加拿大',
     '1952–', 'Q7790919',
     '多伦多大学道德哲学家，至善论（perfectionism）代表；著作有中译但汉名未通行'),
    ('Tim Crane', '蒂姆·克兰', '英国', '1962–', 'Q7803365',
     '心灵哲学家；《机械的心灵》商务印书馆中译（2021）用「蒂姆·克兰」'),
    ('Allen W. Wood', '艾伦·伍德', '美国', '1942–', 'Q14509268',
     '康德与德国观念论学者；《费希特的伦理思想》商务印书馆中译（2022）用「艾伦·伍德」；与 Ellen Meiksins Wood（艾伦·梅克辛斯·伍德）异人'),
    ('Eric Voegelin', '埃里克·沃格林', '美国／德国', '1901–1985', 'Q704039',
     '政治哲学家；《秩序与历史》译林出版社五卷本（2010–2019）用「埃里克·沃格林」'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行音译；籍属/生卒联网查证：Wikidata %s'
                          '（2026-11-23 查，凭证 %s）；%s' % (qid, EV, note),
                 'date': '2026-11-23'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch28-people.json')
json.dump({'batch': '058-batch28-people', 'date': '2026-11-23',
           'scope': '人名第七批（Wikidata 逐人取证）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
