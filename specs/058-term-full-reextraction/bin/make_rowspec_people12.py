# -*- coding: utf-8 -*-
"""人名第十二批 rowspec（2026-11-24）：欧陆与后殖民 18 人，Wikidata 逐人取证。

发现通道转换：候选池按类型分类漏掉一批高频人名（池内标 person 者只覆盖
“名＋姓”形，姓氏单独出现的形被归入其他型），故改用“语料原文计数＋登记册
反查”双向筛：先取 yuanwen/ 全库出现次数，再核登记册键与译法列（含变音符）。
入选门槛：≥8 次且登记册确无（键、别名、译法三列皆不含该姓）。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b12.tsv'

# (键, 译法, 籍属, 生卒, QID, 备注)
PEOPLE = [
    ('Luce Irigaray', '露西·伊利加雷', '比利时／法国', '1930–', 'Q28918',
     '女性主义哲学与精神分析（《此性非一》）'),
    ('Pierre Hadot', '皮埃尔·阿多', '法国', '1922–2010', 'Q972152',
     '古代哲学作为生活方式；《哲学作为生活方式》'),
    ('Ilsetraut Hadot', '伊尔塞特劳特·阿多', '德国／法国', '1928–2026',
     'Q29453535', '斯多亚与亚历山大学派注释研究；语料形“I. Hadot”'),
    ('Félix Guattari', '费利克斯·加塔利', '法国', '1930–1992', 'Q352465',
     '精神分析政治家与哲学（与德勒兹合著《反俄狄浦斯》）'),
    ('Bruno Latour', '布鲁诺·拉图尔', '法国', '1947–2022', 'Q355237',
     '科学知识社会学与行动者本体论（《我们从未现代过》）'),
    ('Chandra Talpade Mohanty', '钱德拉·塔尔帕德·莫汉蒂', '印度／美国', '1955–',
     'Q1086920', '后殖民女性主义（《Under Western Eyes》）'),
    ('J. N. Mohanty', 'J. N. 莫汉蒂', '印度／美国', '1928–2023', 'Q6203267',
     '现象学与印度哲学比较研究；本名 Jitendra Nath Mohanty'),
    ('Giorgio Agamben', '乔尔乔·阿甘本', '意大利', '1942–', 'Q311687',
     '牲人（homo sacer）与例外状态'),
    ('Alain Badiou', '阿兰·巴迪欧', '法国', '1937–', 'Q311005',
     '存在、事件与主体理论（《存在与事件》）'),
    ('Slavoj Žižek', '斯拉沃热·齐泽克', '斯洛文尼亚', '1949–', 'Q184750',
     '黑格尔—拉康式意识形态批判'),
    ('Jacques Rancière', '雅克·朗西埃', '法国', '1940–', 'Q467470',
     '政治美学与歧感（dissensus）'),
    ('Étienne Balibar', '艾蒂安·巴利巴尔', '法国', '1942–', 'Q289333',
     '马克思主义政治哲学（公民权与种族问题）'),
    ('Hélène Cixous', '埃莱娜·西苏', '法国（生于阿尔及利亚）', '1937–', 'Q234964',
     '女性写作（écriture féminine）'),
    ('Catherine Malabou', '凯瑟琳·马拉布', '法国', '1959–', 'Q432690',
     '可塑性（plasticity）与神经哲学'),
    ('Homi K. Bhabha', '霍米·K·巴巴', '印度／英国', '1949–', 'Q325741',
     '后殖民理论（模拟、暧昧性、第三空间）'),
    ('Walter Mignolo', '瓦尔特·米尼奥洛', '阿根廷／美国', '1941–', 'Q497968',
     '殖民性差异与去殖民选项'),
    ('Achille Mbembe', '阿希勒·姆本贝', '喀麦隆', '1957–', 'Q340234',
     '死亡政治（necropolitics）与后殖民政治理论'),
    ('Bernard Stiegler', '贝尔纳·斯蒂格勒', '法国', '1952–2020', 'Q822727',
     '技术与第三代持存（tertiary retention）'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行音译；籍属/生卒联网查证：Wikidata %s'
                          '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note),
                 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch38-people.json')
json.dump({'batch': '058-batch38-people', 'date': '2026-11-24',
           'scope': '人名第十二批（欧陆与后殖民 18 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))
