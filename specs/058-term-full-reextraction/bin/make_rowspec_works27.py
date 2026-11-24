# -*- coding: utf-8 -*-
"""著作名第二十七批 rowspec（2026-11-24）：经典补漏第二组 9 部。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch27-2026-11-24.md'

WORKS = [
    ('The Prince', '《君主论》',
     '潘汉典译，商务印书馆 1985（汉译世界学术名著，ISBN 9787100016483）；'
     '2016-08 权威全译本（ISBN 9787100115490）'),
    ('Freedom of the Will', '《论意志的自由》',
     '本库译名（爱德华兹著，1754；语料 10 处一致；未见中译本）'),
    ('Monologion', '《独语篇》',
     '本库译名（安瑟尔谟著，1075–76；与在册《宣讲》配对；语料 9 处一致）'),
    ('Syncategoremata', '《非范畴词论》',
     '本库译名（中世纪逻辑论著体裁名；语料 10 处一致）'),
    ('Of the Nature of Virtue', '《论德性》',
     '本库译名（巴特勒《宗教的类比》附录论文，语料用简称；语料 10 处一致）'),
    ('De imaginatione', '《论想象》',
     '本库译名（詹弗朗切斯科·皮科著，1501；语料 10 处一致）'),
    ('Fundamenta physices', '《自然哲学基础》',
     '本库译名（雷吉乌斯著，1646；语料 10 处一致）'),
    ('De rerum natura iuxta propria principia', '《论物性》',
     '本库译名（特莱西奥著；长键避开在册卢克莱修 De rerum natura《物性论》行；语料 10 处一致）'),
    ('Fons Vitae', '《生命之源》',
     '本库译名（伊本·盖比鲁勒著；语料 9 处一致）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works27.json')
json.dump({'batch': '058-batch58-works27', 'date': '2026-11-24',
           'scope': '著作名第二十七批（经典补漏第二组 9 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
