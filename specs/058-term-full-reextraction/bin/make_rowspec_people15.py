# -*- coding: utf-8 -*-
"""人名第十五批 rowspec（2026-11-24）：分析哲学各分支 20 人，Wikidata 取证。

名单来源：按分支（数学哲学、物理学哲学、认知科学、语言哲学、宗教哲学、
现象学、法律与政治哲学）列权威人名，再以 yuanwen/ 计数≥3 与登记册三列
（键／别名／译法，NFKD 折叠）反查取缺口。当代学者无通行汉名者按体例留英文。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b15.tsv'
EN = '（无通行汉名，保留英文原名）'

PEOPLE = [
    ('Dan Zahavi', '丹·扎哈维', '丹麦', '1967–', 'Q2896505',
     '现象学与自我研究（《Self and Other》）'),
    ('Herman Cappelen', 'Herman Cappelen' + EN, '挪威', '1967–', 'Q5739617',
     '语义外部论与哲学实验批判'),
    ('Daniel Stoljar', 'Daniel Stoljar' + EN, '澳大利亚', '1967–', 'Q56043537',
     '物理主义（《Physicalism》）；籍属据条目描述'),
    ('Ernest Lepore', 'Ernest Lepore' + EN, '美国', '1950–', 'Q5393458',
     '语言哲学（与 Ramsey 合编语义学文集）；语料形“Ernie Lepore”'),
    ('Manuel García-Carpintero', 'Manuel García-Carpintero' + EN, '—', '1957–',
     'Q58882017', '意义与真理（普鲁斯特讲座）；Wikidata 无 P27，籍属留白'),
    ('Mark Colyvan', 'Mark Colyvan' + EN, '澳大利亚', '—', 'Q29625150',
     '数学不可或缺性论证与环境伦理学'),
    ('Michael Bergmann', 'Michael Bergmann' + EN, '美国', '1964–', 'Q16821240',
     '本体论与例子（thick particular）理论'),
    ('Ofra Magidor', 'Ofra Magidor' + EN, '以色列', '1976–', 'Q55761305',
     '形而上学逻辑与矛盾论（《Contradiction in the Law of Non-Contradiction》）'),
    ('Trent Dougherty', 'Trent Dougherty' + EN, '美国', '1971–', 'Q93222615',
     '证据主义与邪恶问题（《The Problem of Evil》）'),
    ('Matthew Ratcliffe', 'Matthew Ratcliffe' + EN, '—', '1973–', 'Q42425210',
     '现象学与精神病理学（《Feelings of Being》）；Wikidata 无 P27'),
    ('François Recanati', '弗朗索瓦·雷卡纳蒂', '法国', '1952–', 'Q3085655',
     '语义学与言语行为（最小语境主义）'),
    ('N. David Mermin', 'N. 戴维·默明', '美国', '1935–', 'Q1959634',
     '物理学基础与量子力学教学；本名 Nathaniel David Mermin'),
    ('Allen Newell', '艾伦·纽厄尔', '美国', '1927–1992', 'Q439245',
     '认知架构与人工智能（与 Simon 合作）'),
    ('Jeff Speaks', 'Jeff Speaks' + EN, '—', '1975–', 'Q93429192',
     '形而上学与元伦理学；Wikidata 无 P27'),
    ('Eugene Wigner', '尤金·维格纳', '匈牙利／美国', '1902–1995', 'Q155790',
     '量子力学测量问题与“数学不合理的有效性”；本名 Eugene Paul Wigner'),
    ('Wes Morriston', 'Wes Morriston' + EN, '—', '—', 'Q16513471',
     '宗教哲学（邪恶问题与有神论论证）；Wikidata 无 P27 与生年'),
    ('Robyn Carston', 'Robyn Carston' + EN, '新西兰', '1950–', 'Q26702712',
     '关联论与明示推理（《Thoughts and Utterances》）'),
    ('Richard Heck', 'Richard Heck' + EN, '—', '1963–', 'Q112354949',
     '基础主义语义学与弗雷格研究；Wikidata 无 P27'),
    ('Agustín Rayo', 'Agustín Rayo' + EN, '墨西哥', '1973–', 'Q29555978',
     '逻辑哲学与数学哲学（《On Plurals, Empty Names》）'),
    ('Lawrence Barsalou', 'Lawrence Barsalou' + EN, '美国', '1951–', 'Q6504697',
     '知觉符号系统（perceptual symbols）；本名 Lawrence W. Barsalou'),
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
out = os.path.join(RES, 'rowspec-batch41-people.json')
json.dump({'batch': '058-batch41-people', 'date': '2026-11-24',
           'scope': '人名第十五批（分析哲学各分支 20 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
