# -*- coding: utf-8 -*-
"""著作名第二十六批 rowspec（2026-11-24）：经典补漏 7 部。

《非此即彼》《恐惧与颤栗》两行异形由 patch_works26.py 补。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch26-2026-11-24.md'

WORKS = [
    ('The Varieties of Religious Experience', '《宗教经验之种种》',
     '唐钺译，商务印书馆 2002-06（ISBN 9787100043205；1947 初版）；尚新建新译本；'
     '蔡怡佳、刘宏信译，广西师范大学出版社 2008（ISBN 9787563379799）'),
    ('Creative Evolution', '《创造进化论》',
     '姜志辉译，商务印书馆 2004-01（ISBN 9787100037730）；陈圣生译，漓江出版社 2012'),
    ('The Public and Its Problems', '《公众及其问题》',
     '复旦大学出版社 2015-03（本书翻译组译，新闻学与传播学经典丛书，ISBN 9787309112160）；'
     '新华出版社 2018（魏晓慧译，ISBN 9787516634561）'),
    ('Commentary on the Timaeus', '《蒂迈欧注》',
     '本库译名（普罗克洛斯著；语料 11 处一致）'),
    ('Traité de l’Esprit de l’Homme', '《论人的心灵》',
     '本库译名（拉弗尔热著，1666；语料 11 处一致）'),
    ('Commentary on the Categories', '《范畴篇注》',
     '本库译名（阿莫尼俄斯、辛普里丘、波爱修等同名注疏按语境分指；语料 15 处一致）'),
    ('Tractatus de motu', '《论运动》',
     '本库译名（海特斯伯里等同名论著按语境分指；语料 17 处一致）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works26.json')
json.dump({'batch': '058-batch58-works26', 'date': '2026-11-24',
           'scope': '著作名第二十六批（经典补漏 7 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
