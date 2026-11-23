# -*- coding: utf-8 -*-
"""术语第十二批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('quantifier expressions', '量词表达式', ''),
    ('alter ego', '他我', ''),
    ('vital activities', '生命活动', ''),
    ('negative introspection', '负内省', ''),
    ('subgame perfect equilibrium', '子博弈完美均衡（审定作“子博弈完美纳什均衡”）', 'T'),
    ('collective consciousness', '集体意识', ''),
    ('modal profile', '模态轮廓', ''),
    ('perfect set property', '完美集性质', ''),
    ('repeated games', '重复博弈', 'T'),
    ('coordination games', '协调博弈', ''),
    ('elementarily equivalent', '初等等价', 'T'),
    ('existence property', '存在性性质', ''),
    ('function variables', '函数变元', ''),
    ('prudential concern', '审慎关切', ''),
    ('speech time', '说话时间', ''),
    ('knowledge source', '知识源', 'T'),
    ('weighing reasons', '权衡理由', ''),
    ('internal realism', '内在实在论', 'T'),
    ('personal knowledge', '个人知识', 'T'),
    ('qualitative identity', '质的同一性', ''),
    ('basic modal logic', '基本模态逻辑', ''),
    ('evolutionarily stable strategy', '进化稳定策略（审定作“进化稳定对策”）', 'T'),
    ('general justification', '一般证成', ''),
    ('product update', '乘积更新', ''),
    ('supervenience physicalism', '随附性物理主义', ''),
    ('workplace democracy', '工作场所民主', ''),
    ('matrix semantics', '矩阵语义学', ''),
    ('reduction sentences', '还原语句', ''),
    ('relational equality', '关系平等', ''),
    ('belief ascriptions', '信念归属', ''),
    ('characteristica universalis', '普遍字符', ''),
    ('epistemic certainty', '认知确定性', ''),
    ('late preemption', '后期抢占', ''),
    ('constitutional patriotism', '宪法爱国主义', ''),
    ('language of thought', '思想语言（审定作“思维语言假说”）', 'T'),
    ('reliable cognition', '可靠认知', ''),
    ('state function', '态函数', 'T'),
    ('distributed knowledge', '分布式知识', 'T'),
    ('evidence-based medicine', '循证医学', 'T'),
    ('expert knowledge', '专家知识', ''),
    ('logical values', '逻辑值', ''),
    ('primary social goods', '基本善', ''),
    ('first-order modal logic', '一阶模态逻辑', ''),
    ('epistemic necessity', '认知必然性', ''),
    ('ergodic hypothesis', '遍历假说', 'T'),
    ('feminist postmodernism', '女性主义后现代主义', ''),
    ('hard information', '硬信息', ''),
    ('priority pluralism', '优先性多元论', ''),
    ('complete lattice', '完全格', 'T'),
    ('constitutive luck', '构成性运气', ''),
    ('science of man', '人的科学', ''),
    ('regulative control', '调节性控制', ''),
    ('demonstrative reference', '指示性指称', ''),
    ('methodological holism', '方法论整体主义', 'T'),
    ('vector potential', '矢量势', 'T'),
    ('conditional stroke', '条件线', ''),
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
out = os.path.join(RES, 'rowspec-batch20-terms.json')
json.dump({'batch': '058-batch20-terms', 'date': '2026-11-23',
           'scope': '术语第十二批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
