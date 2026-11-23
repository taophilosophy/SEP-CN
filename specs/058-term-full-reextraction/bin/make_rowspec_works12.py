# -*- coding: utf-8 -*-
"""著作名第十二批 rowspec（2026-11-24）：6 部。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

WORKS = [
    ('Reasons and Persons', '《理与人》',
     '王新生译，上海译文出版社 2005 / 2017（二十世纪西方哲学经典）'),
    ('Theory of Communicative Action', '《交往行为理论》',
     '曹卫东译，上海人民出版社 2004 / 2018（哈贝马斯文集）'),
    ('Proofs and Refutations', '《证明与反驳：数学发现的逻辑》',
     '方刚、兰钊译，复旦大学出版社 2007'),
    ('Works of Love', '《爱的作为》',
     '京不特译，中国社会科学出版社 2014（克尔凯郭尔文集 7）'),
    ('Introduction to Mathematical Philosophy', '《数理哲学导论》',
     '商务印书馆“汉译世界学术名著丛书”1000 种书目·哲学第 174 号'),
    ('System of Nature', '《自然的体系》',
     '商务印书馆“汉译世界学术名著丛书”1000 种书目·哲学第 241 号（上下卷）'),
]

rows = []
for en, zh, src in WORKS:
    if src.startswith('商务印书馆'):
        basis = '权威译本（%s；2026-11-24 查，凭证 works-batch10-2026-11-24.md）' % src
    else:
        basis = ('权威译本（%s；2026-11-24 联网核对，凭证 '
                 'works-batch12-2026-11-24.md）' % src)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch53-works.json')
json.dump({'batch': '058-batch53-works', 'date': '2026-11-24',
           'scope': '著作名第十二批（6 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
