# -*- coding: utf-8 -*-
"""著作名第十五批 rowspec（2026-11-24）：后殖民与西方马克思主义经典 6 部。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

WORKS = [
    ('The Wretched of the Earth', '《全世界受苦的人》',
     '万冰译，译林出版社 2005', '台版作《大地上的受苦者》（杨碧川译，心灵工坊 2009）'),
    ('The Souls of Black Folk', '《黑人的灵魂》',
     '维群译，人民文学出版社 1959 初版 / 2024 再版', ''),
    ('For Marx', '《保卫马克思》',
     '顾良译，商务印书馆 2010（汉译名著本 11）', ''),
    ('Reading Capital', '《读〈资本论〉》',
     '李其庆、冯文光译，中央编译出版社 2000 / 2017（第二版）', ''),
    ('Pedagogy of the Oppressed', '《被压迫者教育学》',
     '顾建新、赵友华、何曙荣译，华东师范大学出版社 2001（30 周年纪念版）', ''),
    ('Discourse on Colonialism', '《论殖民主义》',
     '施雪莹译，人民文学出版社 2024（与《还乡笔记》合刊）', ''),
]

rows = []
for en, zh, src, note in WORKS:
    basis = '权威译本（%s；2026-11-24 联网核对，凭证 works-batch15-2026-11-24.md）' % src
    if note:
        basis += '；' + note
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch56-works.json')
json.dump({'batch': '058-batch56-works', 'date': '2026-11-24',
           'scope': '著作名第十五批（6 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
