# -*- coding: utf-8 -*-
"""池 held 结算第二批（2026-11-24）：六条术语立册，Del Medigo 等结算。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch35-2026-11-24.md'

ROWS = [
    ('likelihood', '似然', '统计与贝叶斯认识论文献通行术语；语料 58 处一致；在册仅有 likelihood principle／ratio 复合行'),
    ('particularism', '特殊主义', '学界通行；道德特殊主义（moral particularism）已在册，本行为伞形词，道德／知识论两义按语境；语料 29 处一致'),
    ('incremental evidence', '增量证据', '贝叶斯认识论文献通行术语；语料 38 处一致'),
    ('candidate explanations', '候选解释', '溯因与科学解释文献通行术语；语料 16 处一致'),
    ('hosshin seppō', '法身说法', '本库译名（空海论学名题；语料 18 处一致）'),
    ('yogyatā', '适切性', '本库译名（新胜论组合关系术语；语料 5 处一致）'),
]

rows = []
for en, zh, src in ROWS:
    basis = '%s（2026-11-24 语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works35.json')
json.dump({'batch': '058-batch58-works35', 'date': '2026-11-24',
           'scope': '池 held 结算第二批（术语立册 6 条）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
