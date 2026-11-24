# -*- coding: utf-8 -*-
"""著作名第二十一批 rowspec（2026-11-24）：收口批，新立 5 行。

另有 Phaedo／Timaeus／Meditations on First Philosophy 三行短形补丁（patch_works21.py）。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch21-2026-11-24.md'

WORKS = [
    ('The Symposium', '《会饮篇》',
     '朱光潜译《柏拉图文艺对话集》收《会饮篇》，人民文学出版社 1959-12（ISBN 9787020066681）；'
     '键取冠词形以避开概念行 symposium（希腊宴饮，同形异义）'),
    ('Avatamsaka Sutra', '《华严经》',
     '汉译佛典通行经题（实叉难陀译《大方广佛华严经》，八十卷本；非抉择项，语料 38 处一致）'),
    ('Mahāvairocana Sūtra', '《大日经》',
     '汉译佛典通行经题（善无畏、一行译《大毗卢遮那成佛神变加持经》之简称；'
     '非抉择项，语料 16 处一致）'),
    ('Matter and Memory', '《物质与记忆》',
     '肖聿译本，题作《材料与记忆》，华夏出版社 1999-01（ISBN 9787508016405）；'
     '译林出版社 2014-10 汉译经典（ISBN 9787544749664）；语料通行形《物质与记忆》'),
    ('Of Tragedy', '《论悲剧》',
     '李贯峰译《人性的高尚与卑劣》收《论悲剧》，湖南文艺出版社 2024-10（ISBN 9787572621079）；'
     '吴兴华译收入《石头与星宿：译文集》，广西师范大学出版社 2017'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works21.json')
json.dump({'batch': '058-batch58-works21', 'date': '2026-11-24',
           'scope': '著作名第二十一批（收口批：会饮篇、华严经、大日经等 5 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
