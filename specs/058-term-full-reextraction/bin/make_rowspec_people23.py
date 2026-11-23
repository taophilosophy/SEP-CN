# -*- coding: utf-8 -*-
"""人名第二十三批 rowspec（2026-11-24）：希腊罗马、中世纪与近代女性思想家、
美国自然主义 14 人。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b23.tsv'

PEOPLE = [
    ('Prodicus', '普罗狄科', '古希腊（凯奥斯）', '约前465–约前395', 'Q297402',
     '智者派，语言与同义词研究；Wikidata 记前460–前380，取条目描述区间'),
    ('Panaetius', '帕奈提乌斯', '古希腊（罗德岛）', '约前185–约前110', 'Q297420',
     '中期斯多亚，西塞罗的思想来源'),
    ('Aedesia', '埃德西亚', '古罗马（亚历山大里亚）', '约5世纪（活动期）',
     'Q2382393', '新柏拉图主义女哲学家；Wikidata 生卒为占位值不取'),
    ('Perpetua', '佩尔佩图阿', '古罗马（迦太基）', '？–203', '—',
     '《佩尔佩图阿与菲利西塔斯行传》主人公；无 Wikidata 人格项，'
     '生年不传只记卒年（2026-11-24 查证）'),
    ('Hildegard of Bingen', '宾根的希尔德加德', '神圣罗马帝国（宾根）',
     '1098–1179', 'Q70991', '修道院长、神秘神学与博物学著作'),
    ('Heloise', '爱洛伊丝', '法国（阿让特伊）', '约1101–1164', '—',
     '与阿伯拉尔的书信与伦理思想；无 Wikidata 人格项，生卒取学界通说'
     '（2026-11-24 查证）'),
    ('Marie de Gournay', '玛丽·德·古尔奈', '法国', '1565–1645', 'Q469087',
     '《论男女平等》，蒙田文集编者'),
    ('Mary Hays', '玛丽·海斯', '英国', '1759–1843', 'Q1797831',
     '《为女性权利辩护》（Appeal to the Men of Great Britain）'),
    ('Frances Power Cobbe', '弗朗西丝·鲍尔·科布', '爱尔兰', '1822–1904',
     'Q466162', '女性主义与动物伦理（《The Duties of Women》）'),
    ('Aron Gurwitsch', '阿伦·古尔维奇', '立陶宛／美国', '1901–1973', 'Q215031',
     '现象学与格式塔心理学（《意识场论》）'),
    ('Justus Buchler', '贾斯特斯·布克勒', '美国', '1914–1991', 'Q16012573',
     '自然主义形而上学（《Toward a General Theory of Human Judgment》）'),
    ('Paul Horwich', '保罗·霍里奇', '英国／美国', '1947–', 'Q7151387',
     '真之紧缩论（《Truth》）'),
    ('Rebecca Kukla', '丽贝卡·库克拉', '加拿大／美国', '1969–',
     'Q57313575', '医学伦理与认识论（《Mass Hysteria》）'),
    ('Mark Lance', '马克·兰斯', '美国', '1959–', 'Q15492092',
     '实用主义语义学与规范表述（与 Kukla 合作）'),
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
out = os.path.join(RES, 'rowspec-batch49-people.json')
json.dump({'batch': '058-batch49-people', 'date': '2026-11-24',
           'scope': '人名第二十三批（14 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
