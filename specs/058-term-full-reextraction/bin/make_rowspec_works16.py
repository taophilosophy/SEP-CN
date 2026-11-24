# -*- coding: utf-8 -*-
"""著作名第十六批 rowspec（2026-11-24）：华夏出版社「哲学新课题」译丛 4 部新目。

该丛书本批共核 9 册；另 5 册书名与既有概念行同键（physicalism、self-knowledge、
consequentialism、analyticity、moral epistemology），不另立行，改在概念行补译本依据/别名，
见 patch_works16_series.py。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

WORKS = [
    ('Fiction and Fictionalism', '《虚构与虚构主义》',
     '赛恩斯伯里著，万美文译，华夏出版社 2015-12（哲学新课题丛书）'),
    ('Noncognitivism in Ethics', '《伦理学中的非认知主义》',
     '马克·施罗德著，张婉译，华夏出版社 2017-01（哲学新课题丛书）'),
    ('Embodied Cognition', '《具身认知》',
     '劳伦斯·夏皮罗著，李恒威、董达译，华夏出版社 2014-05（哲学新课题丛书）'),
    ('Semantic Externalism', '《语义外在论》',
     '杰斯帕·凯勒斯特拉普著，李美译，华夏出版社 2016-08（哲学新课题丛书）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '权威译本（%s；2026-11-24 联网核对，凭证 works-batch16-2026-11-24.md）' % src
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch57-works.json')
json.dump({'batch': '058-batch57-works', 'date': '2026-11-24',
           'scope': '著作名第十六批（哲学新课题译丛，4 部新目）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
