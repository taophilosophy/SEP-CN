# -*- coding: utf-8 -*-
"""著作名第三十一批 rowspec（2026-11-24）：6–7 频次段余项 16 部。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch31-2026-11-24.md'

WORKS = [
    ('Shōji jissōgi', '《声字实相义》',
     '本库译名（空海著，三部书之一；语料 7 处一致）'),
    ('Huayan fajie guanmen', '《华严法界观门》',
     '本库译名（杜顺著；英译 Discernments of the Dharmadhatu of Avatamsaka；语料 7 处一致）'),
    ('Confessio philosophi', '《哲人自白》',
     '本库译名（莱布尼茨著，1672–73；语料 7 处一致）'),
    ('Was heißt: sich im Denken orientiren?', '《什么叫做在思维中定向？》',
     '本库译名（康德著，1786；语料 7 处一致）'),
    ('De aeternitate mundi', '《论世界的永恒》',
     '本库译名（波爱修·达契亚著；语料 6 处一致）'),
    ('De summo bono', '《论至善》',
     '本库译名（波爱修·达契亚著；语料 7 处一致）'),
    ('Liber de causis', '《原因书》',
     '本库译名（佚名阿拉伯—拉丁著作，曾归亚里士多德；语料 6 处一致）'),
    ('De somniis', '《论梦》',
     '本库译名（亚里士多德《自然诸短篇》之一；波爱修·达契亚同名小著作按语境分指；语料 7 处一致）'),
    ('The Mathematical Analysis of Logic', '《逻辑的数学分析》',
     '本库译名（布尔著，1847；语料 6 处一致）'),
    ('De partibus animalium', '《论动物的部分》',
     '本库译名（亚里士多德著；语料 6 处一致）'),
    ('Le Système du Monde', '《世界体系》',
     '本库译名（迪昂十卷本科学史，1913–1959；语料 6 处一致）'),
    ('Cratylus', '《克拉底鲁篇》',
     '本库译名（柏拉图对话；语料 6 处一致）'),
    ('Alcibiades', '《阿尔喀比亚德篇》',
     '本库译名（柏拉图对话；语料 7 处一致）'),
    ('Platonic Theology', '《柏拉图神学》',
     '本库译名（普罗克洛斯著；语料 6 处一致）'),
    ('Liberalism and Social Action', '《自由主义与社会行动》',
     '本库译名（杜威著，1935；语料 7 处一致）'),
    ('Œuvres théologiques', '《神学著作集》',
     '本库译名（奥卡姆神学著作编本；语料 6 处一致，正文多作卷页引）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works31.json')
json.dump({'batch': '058-batch58-works31', 'date': '2026-11-24',
           'scope': '著作名第三十一批（6–7 频次段余项 16 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
