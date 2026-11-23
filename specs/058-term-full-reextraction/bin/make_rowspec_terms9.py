# -*- coding: utf-8 -*-
"""术语第九批 rowspec（2026-11-23）：审定形与通行形并存的记「亦作」，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('neural networks', '神经网络', 'T'),
    ('civil disobedience', '公民不服从（审定作“公民抗命”）', 'T'),
    ('metaphysical explanation', '形而上学说明', ''),
    ('political liberalism', '政治自由主义', ''),
    ('collective responsibility', '集体责任（审定收“集体伦理责任”）', 'T'),
    ('social class', '社会阶级（审定作“社会阶层”）', 'T'),
    ('sexual desire', '性欲', 'T'),
    ('evolutionary psychology', '进化心理学', 'T'),
    ('semantic view', '语义观（审定作“理论的语义观”）', 'T'),
    ('narrow content', '窄内容', ''),
    ('conventional truth', '世俗谛（conventional truth）', ''),
    ('bad faith', '自欺', ''),
    ('sensory qualities', '感性性质', ''),
    ('legal positivism', '法律实证主义', ''),
    ('higher-order evidence', '高阶证据', ''),
    ('credence function', '信念度函数', ''),
    ('doxastic states', '信念状态', ''),
    ('fictional objects', '虚构对象', ''),
    ('real essence', '实在本质', ''),
    ('logical construction', '逻辑构造', ''),
    ('common belief', '共同信念', ''),
    ('methodological individualism', '方法论个人主义（审定作“方法论个体主义”）', 'T'),
    ('mathematical propositions', '数学命题', ''),
    ('polynomial time', '多项式时间', ''),
    ('mental disorder', '精神障碍', 'T'),
    ('human animal', '人类动物', ''),
    ('inheritance systems', '遗传系统', ''),
    ('large cardinal axioms', '大基数公理', ''),
    ('political representation', '政治代表', ''),
    ('ad hominem', '人身攻击', ''),
    ('active powers', '主动能力', ''),
    ('defeasible reasoning', '可废止推理', 'T'),
    ('legal interpretation', '法律解释', 'T'),
    ('salva veritate', '保持真值', ''),
    ('semantic correctness', '语义正确性', ''),
    ('appearance beliefs', '显象信念', ''),
    ('option value', '选项价值', ''),
    ('dynamic object', '动态对象', ''),
    ('moral responsibility skepticism', '道德责任怀疑论', ''),
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
out = os.path.join(RES, 'rowspec-batch17-terms.json')
json.dump({'batch': '058-batch17-terms', 'date': '2026-11-23',
           'scope': '术语第九批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
