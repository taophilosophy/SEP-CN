# -*- coding: utf-8 -*-
"""人名第十七批 rowspec（2026-11-24）：印度传统 8 人、日本古学 4 人、
女性主义经典 6 人，Wikidata 取证。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b17.tsv'
EN = '（无通行汉名，保留英文原名）'

PEOPLE = [
    ('Bhartṛhari', '伐致呵利', '古印度（吠檀多·语言哲学）',
     '约5–7世纪（诸说，Wikidata 记 570–651）', 'Q335161',
     '《句艺论》（Vākyapadīya）；纪年诸说不合，取通说区间'),
    ('Bādarāyaṇa', '跋陀罗衍那', '古印度（吠檀多）', '约前2世纪（活动期）',
     'Q4840620', '《梵经》作者；Wikidata 占位前350 不取'),
    ('Bhāvaviveka', '清辨', '印度（中观自续派）', '约500–约578', 'Q2357245',
     '经英文维基“Bhaviveka”确证，另名 Bhavyaviveka；Wikidata 记 c.500–c.578'),
    ('Ānandavardhana', '欢增（阿难陀伐陀那）', '克什米尔', '约820–约890',
     'Q2551244', '《韵光》（Dhvanyāloka）'),
    ('Abhinavagupta', '阿毗那婆笈多', '克什米尔（湿婆派）', '约950–约1016',
     'Q320619', '《美之诫》（Abhinavabhāratī）与湿婆非二元论'),
    ('Rāmānuja', '罗摩奴阇', '印度（吠檀多限定不二论）', '1017–1137', 'Q1741798',
     '经英文维基“Ramanuja”反查得 QID'),
    ('Prabhākara', 'Prabhākara' + EN, '古印度（弥曼差）', '约7世纪（活动期）',
     '—', '弥曼差「言者不二」学派；英文维基“Prabhakara”条目无 Wikidata 项，'
     '生卒不传只记活动期'),
    ('Viśvanātha Kavirāja', 'Viśvanātha Kavirāja' + EN, '印度（美学）',
     '约1300–1384', 'Q7936667', '《韵宝》（Sāhityadarpaṇa）作者'),
    ('Ogyū Sorai', '荻生徂徠', '日本（江户古学）', '1666–1728', 'Q369158',
     '《萱园茶话》；古文辞学派'),
    ('Itō Jinsai', '伊藤仁斋', '日本（江户古义学）', '1627–1705', 'Q640808',
     '《论语古义》；堀河塾'),
    ('Yamaga Sokō', '山鹿素行', '日本（江户）', '1622–1685', 'Q1095270',
     '武士道思想（《山鹿语类》）'),
    ('Kaibara Ekken', '贝原益轩', '日本（江户）', '1630–1714', 'Q1721396',
     '儒学博物学（《大和本草》）'),
    ('Kimberlé Crenshaw', '金伯利·克伦肖', '美国', '1959–', 'Q6409990',
     '交叉性（intersectionality）理论'),
    ('bell hooks', '贝尔·胡克斯', '美国', '1952–2021', 'Q259507',
     '黑人女性主义（《女权主义理论：从边缘到中心》）'),
    ('Mary Daly', '玛丽·戴利', '美国', '1928–2010', 'Q241392',
     '激进女性主义神哲学（《超越父神》）'),
    ('Shulamith Firestone', '舒拉米斯·费尔斯通', '加拿大／美国', '1945–2012',
     'Q271551', '《性的辩证法》'),
    ('Monique Wittig', '莫妮克·威蒂格', '法国／美国', '1935–2003', 'Q263201',
     '异性恋规范批判（《直人思维》）'),
    ('Sara Ruddick', '萨拉·鲁迪克', '美国', '1935–2011', 'Q7421755',
     '母性伦理学（《母性思维》）'),
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
out = os.path.join(RES, 'rowspec-batch43-people.json')
json.dump({'batch': '058-batch43-people', 'date': '2026-11-24',
           'scope': '人名第十七批（18 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
