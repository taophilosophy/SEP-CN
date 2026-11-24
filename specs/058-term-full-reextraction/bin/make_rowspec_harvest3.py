# -*- coding: utf-8 -*-
"""候选池收割第三批 rowspec（2026-11-24）：核心术语真缺 8 条。

筛选法：池 new 高频 × 单复数归一在册差集 × 中文语料频次复核（≥6 处）。
evidence 文档：results/pool-harvest-b3-2026-11-24.md。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'pool-harvest-b3-2026-11-24.md'

ROWS = [
    ('conceptual analysis', '概念分析', '学界通行（分析哲学文献通行术语；语料 19 处一致；审定库无对口条目）'),
    ('mental properties', '心理属性', '学界通行（心灵哲学文献通行术语；语料 31 处一致）'),
    ('moral truths', '道德真理', '学界通行（元伦理学文献通行术语；语料 35 处一致）'),
    ('rational agents', '理性行动者', '学界通行（行动哲学与伦理学通行术语；语料 17 处一致）'),
    ('logical space', '逻辑空间', '学界通行（维特根斯坦《逻辑哲学论》通行汉译；语料 8 处一致）'),
    ('empty names', '空名', '学界通行（语言哲学文献通行术语；语料 6 处一致）'),
    ('Kyoto School', '京都学派',
     '学界通行（吴汝钧《绝对无的哲学：京都学派哲学导论》，台湾商务印书馆 1998；'
     '《绝对无诠释学：京都学派的批判性研究》，学生书局 2012；语料 6 处一致）'),
    ('ethical theory', '伦理学理论', '学界通行（伦理学文献通行术语；语料 8 处一致）'),
]

rows = []
for en, zh, src in ROWS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-harvest3.json')
json.dump({'batch': '058-batch58-harvest3', 'date': '2026-11-24',
           'scope': '候选池收割第三批（核心术语真缺 8 条）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
