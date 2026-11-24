# -*- coding: utf-8 -*-
"""候选池收割第四批 rowspec（2026-11-24）：核心术语真缺第二组 5 条。

evidence 文档：results/pool-harvest-b4-2026-11-24.md。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'pool-harvest-b4-2026-11-24.md'

ROWS = [
    ('reflective equilibrium', '反思平衡',
     '学界通行（罗尔斯《正义论》通行汉译；语料 114 处一致；在册仅有 full／narrow 变体行，伞形词缺）'),
    ('theoretical reason', '理论理性',
     '学界通行（康德实践哲学文献通行译名；语料 44 处一致；在册仅《实践理性批判》书名行）'),
    ('modal realism', '模态实在论',
     '学界通行（刘易斯形而上学文献通行译名；语料 21 处一致；在册仅有 genuine modal realism 行）'),
    ('Gettier problem', '盖梯尔问题',
     '学界通行（知识论文献通行译名；语料 15 处一致；在册仅有 gettier cases 案例行）'),
    ('public reason', '公共理性',
     '学界通行（罗尔斯晚期政治哲学通行译名；语料 11 处一致；审定库无对口条目）'),
]

rows = []
for en, zh, src in ROWS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-harvest4.json')
json.dump({'batch': '058-batch58-harvest4', 'date': '2026-11-24',
           'scope': '候选池收割第四批（核心术语真缺第二组 5 条）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
