# -*- coding: utf-8 -*-
"""术语第十六批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('eliminative induction', '消除性归纳', ''),
    ('epistemic permissivism', '认知允准主义', ''),
    ('existential interpretation', '存在诠释', ''),
    ('grounding physicalism', '奠基物理主义', ''),
    ('improper part', '非真部分', ''),
    ('indirect speech acts', '间接言语行为', 'T'),
    ('inductive principle', '归纳原则', ''),
    ('inquisitive logic', '探询逻辑', ''),
    ('likelihood principle', '似然原则', ''),
    ('metalogical properties', '元逻辑性质', ''),
    ('metasemantic theory', '元语义理论', ''),
    ('naked singularities', '裸奇异性', 'T'),
    ('normative necessity', '规范必然性', ''),
    ('open texture', '开放结构', ''),
    ('ordinal representation system', '序数表示系统', ''),
    ('permutation symmetry', '置换对称', 'T'),
    ('presentational phenomenology', '呈现现象学', ''),
    ('psychological realism', '心理现实主义', ''),
    ('public values', '公共价值', ''),
    ('ramified analysis', '分支分析', ''),
    ('sampling error', '抽样误差', 'T'),
    ('sex roles', '性别角色', 'T'),
    ('social surplus', '社会剩余', ''),
    ('sour grapes', '酸葡萄', ''),
    ('strict compliance', '严格服从', ''),
    ('unconscious inferences', '无意识推理', 'T'),
    ('conditioned response', '条件反应', 'T'),
    ('cooperative surplus', '合作剩余', ''),
    ('deliberate practice', '刻意练习', ''),
    ('imagined community', '想象的共同体', ''),
    ('scientific socialism', '科学社会主义', 'T'),
    ('epistemic friction', '认知摩擦', ''),
    ('evidence function', '证据函数', ''),
    ('extended phenotype', '延伸表现型', ''),
    ('extrinsic denomination', '外在命名', ''),
    ('species taxa', '物种分类单元', ''),
    ('paradoxes of material implication', '实质蕴涵悖论', ''),
    ('propensity interpretation', '倾向性诠释（审定作“概率的倾向解释”）', ''),
    ('survival of the fittest', '适者生存', 'T'),
    ('classical valuation', '经典赋值', ''),
    ('constructive reverse mathematics', '构造性反推数学', ''),
    ('direct representation', '直接表象', ''),
    ('dual character concepts', '双重特征概念', ''),
    ('full publicity', '充分公开性', ''),
    ('posteriori necessities', '后验必然', ''),
    ('public political culture', '公共政治文化', ''),
    ('revenge problem', '报复问题', ''),
    ('success theory', '成功论', ''),
    ('systematic power', '系统力', ''),
    ('unequal exchange', '不等交换', 'T'),
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
out = os.path.join(RES, 'rowspec-batch24-terms.json')
json.dump({'batch': '058-batch24-terms', 'date': '2026-11-23',
           'scope': '术语第十六批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
