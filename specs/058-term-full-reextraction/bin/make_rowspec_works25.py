# -*- coding: utf-8 -*-
"""著作名第二十五批 rowspec（2026-11-24）：稀见题第四组 9 部。

含池 held 项 Tamhīdāt 的解禁（语料作《铺路集》34 处）。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch25-2026-11-24.md'

WORKS = [
    ('Tamhīdāt', '《铺路集》',
     '本库译名（艾因·古达特波斯语杰作，1127；英译选本见 Rustom 2023；语料 34 处一致；'
     '池 held 项随之解禁）'),
    ('In calumniatorem Platonis', '《驳柏拉图的诽谤者》',
     '本库译名（贝萨里翁著；语料 24 处一致）'),
    ('Sefer Yesira', '《创世书》',
     '本库译名（佚名希伯来论著；语料 11 处一致）'),
    ('Adversus Logicos', '《驳逻辑学家》',
     '本库译名（塞克斯都·恩披里柯《驳数学家》第七至八卷；语料 11 处一致）'),
    ('Stromateis', '《杂记》',
     '本库译名（亚历山大的克莱门特著；伪普鲁塔克同名《杂记》按语境分指；语料 11 处一致）'),
    ('De Corpore', '《论物体》',
     '本库译名（霍布斯著，1655；哲学三部曲第一部；语料 14 处一致）'),
    ('Hsin Lun', '《新论》',
     '本库译名（桓谭著，东汉；今存残篇，Pokora 英译 1975；语料 13 处一致）'),
    ('Transcendental Aesthetic', '《感性论》',
     '学界通行（康德《纯粹理性批判》第一部分，通称《先验感性论》；语料 18 处一致，含短形）'),
    ('The Fable of the Bees', '《蜜蜂的寓言》',
     '肖聿译，商务印书馆 2016-12（两册，ISBN 9787100126168）；2019-04 精装（ISBN 9787100158817）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works25.json')
json.dump({'batch': '058-batch58-works25', 'date': '2026-11-24',
           'scope': '著作名第二十五批（稀见题第四组 9 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
