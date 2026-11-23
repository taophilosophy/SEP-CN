# -*- coding: utf-8 -*-
"""术语第六批 rowspec（2026-11-23）：审定对口者采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('probabilistic causality', '概率因果性', ''),
    ('aggregation theorem', '聚合定理', ''),
    ('dependent choice', '依赖选择', ''),
    ('epistemological reduction', '认识论还原', ''),
    ('maximal propositions', '极大命题', ''),
    ('primitive propositions', '初始命题', ''),
    ('signal detection theory', '信号检测理论', 'T'),
    ('symmetry arguments', '对称性论证', ''),
    ('top-down causation', '下行因果', ''),
    ('constitution thesis', '构成论题', ''),
    ('existential second-order logic', '存在二阶逻辑', ''),
    ('limiting reduction', '极限还原', ''),
    ('pragmatic contradiction', '语用矛盾', ''),
    ('stream of consciousness', '意识流', ''),
    ('classical semantic theories', '经典语义理论', ''),
    ('property theories', '属性理论', ''),
    ("Suszko's Thesis", '苏什科论题', ''),
    ("Berry's paradox", '贝里悖论', ''),
    ('cut elimination theorem', '切消定理', ''),
    ('objectual knowledge', '对象性知识', ''),
    ('Characterization Principle', '刻画原则', ''),
    ('conceptual realism', '概念实在论', ''),
    ('control rights', '控制权', ''),
    ('Equivalence Thesis', '等价论题', ''),
    ('network epistemology', '网络认识论', ''),
    ('token-token reduction', '个例-个例还原', ''),
    ('confirmation holism', '确证整体论', ''),
    ('practical moral skepticism', '实践道德怀疑论', ''),
    ('privacy paradox', '隐私悖论', ''),
    ('Reality Principle', '现实原则', ''),
    ('simple mapping account', '简单映射说明', ''),
    ('active perception', '主动知觉', ''),
    ('general causation', '一般因果', ''),
    ('mechanistic knowledge', '机制性知识', ''),
    ('modal monism', '模态一元论', ''),
    ('assertional logic', '断言逻辑', ''),
    ('Category Theory', '范畴论', 'T'),
    ('cumulative prospect theory', '累积前景理论', ''),
    ("Hilbert's thesis", '希尔伯特论题', ''),
    ('memory argument', '记忆论证', ''),
    ('minimal rationality', '最低合理性', ''),
    ('Moving Spotlight Theory', '移动聚光灯理论', ''),
]

rows = []
for en, zh, db in ROWS:
    if db == 'T':
        basis = '审定名词库（termonline-all，凭证 2026-11-23）'
    elif db:
        basis = '审定名词库（termonline-all·%s，凭证 2026-11-23）' % db
    else:
        basis = '学界通行译名（审定库无对口命中，2026-11-23）；凭证 2026-11-23'
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-23'})
out = os.path.join(RES, 'rowspec-batch12-terms.json')
json.dump({'batch': '058-batch12-terms', 'date': '2026-11-23',
           'scope': '术语第六批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
