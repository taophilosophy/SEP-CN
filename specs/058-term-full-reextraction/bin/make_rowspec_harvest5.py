# -*- coding: utf-8 -*-
"""候选池收割第五批 rowspec（2026-11-24）：分域审计真缺 6 条。

evidence 文档：results/pool-harvest-b5-2026-11-24.md。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'pool-harvest-b5-2026-11-24.md'

ROWS = [
    ('problem of evil', '恶的问题',
     '学界通行（宗教哲学文献通行译名；语料 50 处一致；在册仅有 argument from evil 恶的论证与诸恶论变体行，伞形词缺）'),
    ('historical explanation', '历史解释',
     '学界通行（历史哲学文献通行译名；语料 11 处一致）'),
    ('theory choice', '理论选择',
     '学界通行（科学哲学文献通行译名；语料 9 处一致）'),
    ('collective action', '集体行动',
     '学界通行（社会科学哲学文献通行译名；语料 9 处一致）'),
    ('artworld', '艺术界',
     '学界通行（丹托艺术理论通行译名；语料 8 处一致）'),
    ('theory-ladenness', '理论负载',
     '学界通行（科学哲学文献通行译名；语料 6 处一致，含“观察的理论负载”变体）'),
]

rows = []
for en, zh, src in ROWS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-harvest5.json')
json.dump({'batch': '058-batch58-harvest5', 'date': '2026-11-24',
           'scope': '候选池收割第五批（分域审计真缺 6 条）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
