# -*- coding: utf-8 -*-
"""术语第十七批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('collective mind', '集体心灵', ''),
    ('discursive formations', '话语构型', ''),
    ('finitist mathematics', '有穷主义数学', ''),
    ('intentional systems', '意向系统', ''),
    ('legal facts', '法律事实', 'T'),
    ('physical collapse', '物理坍缩', ''),
    ('rectifying names', '正名', ''),
    ('second-order reasons', '二阶理由', ''),
    ('selfish genes', '自私基因', 'T'),
    ('sensitivity analysis', '敏感性分析', 'T'),
    ('structural equation models', '结构方程模型', 'T'),
    ('transcendent self', '超越自我', ''),
    ('triviality results', '平凡性结果', ''),
    ('unrestricted mereological composition', '无限制的部分-整体组合', ''),
    ('tragedy of the commons', '公地悲剧', 'T'),
    ('equational calculus', '等式演算', ''),
    ('esse est percipi', '存在即被感知', ''),
    ('ethical non-naturalism', '伦理非自然主义', ''),
    ('exciting reasons', '激发性理由', ''),
    ('faultless disagreement', '无错分歧', ''),
    ('genic selection', '基因选择', ''),
    ('imperative sentences', '祈使句', 'T'),
    ('incongruent counterparts', '不重合对应物', ''),
    ('intuitive induction', '直觉归纳', ''),
    ('linguistic ersatzism', '语言学替代主义', ''),
    ('materialist conception', '唯物主义构想', ''),
    ('null hypotheses', '零假设', ''),
    ('outer models', '外模型', ''),
    ('phase averages', '相平均', ''),
    ('phonological form', '音系形式', ''),
    ('plausibility relations', '可信性关系', ''),
    ('possibility spaces', '可能性空间', ''),
    ('threat advantage', '威胁优势', ''),
    ('transmission model', '传递模型', 'T'),
    ('context change potentials', '语境改变潜能', ''),
    ('contributory injustice', '贡献性不正义', ''),
    ('dark patterns', '暗黑模式', ''),
    ('disease burden', '疾病负担', 'T'),
    ('embodied minds', '具身心智', ''),
    ('mandate of heaven', '天命', 'T'),
    ('market societies', '市场社会', ''),
    ('materia prima', '原初质料', ''),
    ('moral deference', '道德顺从', ''),
    ('manifest contradiction', '显明矛盾', ''),
    ('right reason', '正确理性', ''),
    ('cogent argument', '有说服力论证', ''),
    ('collective property', '集体财产（审定“集束性”对应 collection property，非同一概念）', ''),
]

rows = []
for en, zh, db in ROWS:
    if db == 'T':
        basis = '审定名词库（termonline-all，凭证 2026-11-23）'
    else:
        basis = '学界通行译名（审定库无对口命中，2026-11-23）；凭证 2026-11-23'
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-23'})
out = os.path.join(RES, 'rowspec-batch25-terms.json')
json.dump({'batch': '058-batch25-terms', 'date': '2026-11-23',
           'scope': '术语第十七批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
