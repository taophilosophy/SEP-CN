# -*- coding: utf-8 -*-
"""著作名第二十批 rowspec（2026-11-24）：稀见／单条目著作 8 部。

此类多无中译本，依据记“本库译名”并注明语料一致处数与英译题名；有外部学界用例者记学界通行。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch20-2026-11-24.md'

WORKS = [
    ('Sefer Tiqqun ha deʿot', '《意见之矫正》',
     '本库译名（阿尔巴拉格唯一论著；从 Manekin 英译 The Emendation of the Opinions 汉译；'
     '未见中译本，语料 71 处一致）'),
    ('Maqāṣid al-Falāsifah', '《哲学家的宗旨》',
     '学界通行（马玉龙《安萨里对哲学的批判》，兰州大学博士论文 2017，用《哲学家的宗旨》；'
     '语料 20 处一致）'),
    ('Sefer Milhamot Ha-Shem', '《上帝之战》',
     '本库译名（吉尔松尼德主著，1329；Feldman 英译 The Wars of the Lord；'
     '中文未见通行定名，语料 17 处一致）'),
    ('Examen vanitatis', '《虚妄之检验》',
     '本库译名（詹弗朗切斯科·皮科，1520；未见中译本，语料 13 处一致）'),
    ('De regimine principum', '《论君主统治》',
     '本库译名（罗马的吉尔斯，约 1277–1280；未见中译本，语料 12 处一致）'),
    ('An Essay Towards a New Theory of Vision', '《视觉新论》',
     '关文运译，商务印书馆 1957-10；2018-11 汉译世界学术名著本（ISBN 9787100164023）'),
    ('Institutions de physique', '《物理学奠基》',
     '本库译名（夏特莱侯爵夫人，1740；未见中译本，语料 39 处一致，含短形《奠基》）'),
    ('De veritate', '《论真理》',
     '本库译名（阿奎那 disputed questions；未见全译本，语料 14 处一致）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works20.json')
json.dump({'batch': '058-batch58-works20', 'date': '2026-11-24',
           'scope': '著作名第二十批（稀见／单条目著作 8 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
