# -*- coding: utf-8 -*-
"""著作名第十三批 rowspec（2026-11-24）：10 部（5 商务书目＋4 已核译本）。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

WORKS = [
    ('Dreams of Spirit-Seer', '《通灵者之梦》',
     '商务印书馆“汉译世界学术名著丛书”1000 种书目·哲学第 300 号（康德）', ''),
    ('Time and Free Will', '《时间与自由意志》',
     '商务印书馆“汉译世界学术名著丛书”1000 种书目·哲学第 164 号（柏格森）', ''),
    ('Science and Hypothesis', '《科学与假设》',
     '商务印书馆“汉译世界学术名著丛书”1000 种书目·哲学第 67 号（彭加勒）', ''),
    ('Principles of Human Knowledge', '《人类知识原理》',
     '商务印书馆“汉译世界学术名著丛书”1000 种书目·哲学第 141 号（贝克莱）', ''),
    ('General Theory of Knowledge', '《普通认识论》',
     '商务印书馆“汉译世界学术名著丛书”1000 种书目·哲学第 129 号（石里克）', ''),
    ('Matter and Memory', '《材料与记忆》',
     '肖聿译，华夏出版社 1999 / 译林出版社 2011',
     '通行别译《物质与记忆》'),
    ('Eros and Civilization', '《爱欲与文明》',
     '黄勇、薛民译，上海译文出版社 1987 / 2012', ''),
    ('Art and Illusion', '《艺术与错觉：图画再现的心理学研究》',
     '林夕、李本正、范景中译，浙江摄影出版社 1987 / 湖南科学技术出版社 2002',
     ''),
    ('Ethics and Language', '《伦理学与语言》',
     '姚新中、秦志华等译，中国社会科学出版社 1997（外国伦理学名著译丛）',
     ''),
    ('Enumeration of the Sciences', '《科学分类》',
     '法拉比著作通行书名（Enumeration of the Sciences，学界通译“科学的分类”）',
     '书名体例译，无单独汉译本；依据为学界通行'),
]

rows = []
for en, zh, src, note in WORKS:
    if src.startswith('商务印书馆'):
        basis = '权威译本（%s；2026-11-24 查，凭证 works-batch10-2026-11-24.md）' % src
    elif src.startswith('法拉比'):
        basis = ('学界通行书名（%s；2026-11-24 查，凭证 '
                 'works-batch13-2026-11-24.md）' % src)
    else:
        basis = ('权威译本（%s；2026-11-24 联网核对，凭证 '
                 'works-batch13-2026-11-24.md）' % src)
    if note:
        basis += '；' + note
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch54-works.json')
json.dump({'batch': '058-batch54-works', 'date': '2026-11-24',
           'scope': '著作名第十三批（10 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
