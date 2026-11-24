# -*- coding: utf-8 -*-
"""著作名第二十二批 rowspec（2026-11-24）：Optics 同形两书分键（批二十一开口项收口）。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch22-2026-11-24.md'

WORKS = [
    ('Book of Optics', '《光学》',
     '学界通行（伊本·海赛姆 Kitāb al-Manāẓir，约 1011–1021；中文科学史文献多径作《光学》，'
     '亦作《光学书》；语料一致）'),
    ('La Dioptrique', '《光学》',
     '学界通行（笛卡尔 1637 年论文，与《几何学》《气象学》随《方法谈》合刊；'
     '中文科学史文献亦通行《屈光学》；语料作《光学》）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '学界通行（%s；2026-11-24 联网核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works22.json')
json.dump({'batch': '058-batch58-works22', 'date': '2026-11-24',
           'scope': '著作名第二十二批（Optics 同形两书分键）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
