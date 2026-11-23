# -*- coding: utf-8 -*-
"""术语第七批 rowspec（2026-11-23）：审定对口者采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('pure perception', '纯粹知觉', ''),
    ('transcendental reduction', '先验还原', ''),
    ('counterfactual fallacies', '反事实谬误', ''),
    ('maximising expected utility', '最大化期望效用', ''),
    ('mystical perception', '神秘知觉', ''),
    ('no-overlap principle', '不重叠原则', ''),
    ('racial skepticism', '种族怀疑论', ''),
    ('alternative set theories', '替代集合论', ''),
    ('classification theory', '分类理论', ''),
    ('hybrid expressivism', '混合表达主义', ''),
    ('internal validity', '内部效度', 'T'),
    ('local realism', '定域实在论', ''),
    ('logical identity', '逻辑同一性', ''),
    ('nonclassical logics', '非经典逻辑', ''),
    ('physical Church-Turing thesis', '物理丘奇-图灵论题（审定作“丘奇-图灵论题”）', ''),
    ('theory of meaning', '意义理论', ''),
    ('uniform reflection principle', '统一反射原则', ''),
    ('coalescent theory', '溯祖理论', 'T'),
    ('Conditional Entailment', '条件蕴涵', ''),
    ('cultural consciousness', '文化意识', ''),
    ('definite proposition', '确定命题', ''),
    ('easy knowledge', '轻易知识', ''),
    ('Epistemic emotions', '认知情感', ''),
    ('functional abstraction', '功能抽象', ''),
    ('Intentional realism', '意向实在论', ''),
    ('molecular propositions', '分子命题', ''),
    ('number operator', '粒子数算符', 'T'),
    ('ordinal logics', '序数逻辑', ''),
    ('ordinary quantifiers', '普通量词', ''),
    ('problem of induction', '归纳问题', 'T'),
    ('surplus meaning', '剩余意义', ''),
    ('yogic perception', '瑜伽知觉', ''),
    ('computation tree logic', '计算树逻辑', 'T'),
    ('eternal necessity', '永恒必然性', ''),
    ('evidence logic', '证据逻辑', ''),
    ('methodological reduction', '方法论还原', ''),
    ('motivation argument', '动机论证', ''),
    ('pragmatic truth', '实用真理', ''),
    ('preference utilitarianism', '偏好功利主义', ''),
    ('radical reductionism', '激进还原论', ''),
    ('recursive semantics', '递归语义学', ''),
    ('resemblance thesis', '相似论题', ''),
    ('Socratic Fallacy', '苏格拉底谬误', ''),
    ('structural knowledge', '结构知识', ''),
    ('type causation', '类型因果', ''),
    ('deliberative freedom', '审议自由', ''),
    ('dual inheritance theory', '双重继承理论', ''),
    ('experimental epistemology', '实验认识论', ''),
    ('formal social epistemology', '形式社会认识论', ''),
    ('pragmatic presupposition', '语用预设', ''),
    ('racial naturalism', '种族自然主义', ''),
    ('restricted propositions', '限制命题', ''),
    ('Substitutional quantifiers', '代入量词', 'T'),
    ('awareness logic', '觉知逻辑', ''),
    ('Back-Door Criterion', '后门准则', ''),
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
out = os.path.join(RES, 'rowspec-batch15-terms.json')
json.dump({'batch': '058-batch15-terms', 'date': '2026-11-23',
           'scope': '术语第七批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
