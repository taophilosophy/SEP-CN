# -*- coding: utf-8 -*-
"""术语第四批 rowspec：审定库对口命中优先，其余 A 档直裁（2026-11-23）。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

# (en, zh, 审定学科; 空串＝A 档)
ROWS = [
    ('Naturalistic Fallacy', '自然主义谬误', '自然辩证法'),
    ('conversational implicature', '会话含义（亦作“会话隐含”，审定形）', '语言学'),
    ('discourse ethics', '商谈伦理', '自然辩证法'),
    ('chaos theory', '混沌理论', '生物物理学'),
    ('Chinese Room argument', '中文屋论证', '自然辩证法'),
    ('Cooperative Principle', '合作原则', '语言学'),
    ('Uncertainty Principle', '不确定性原理', '自然辩证法'),
    ('vicious circle principle', '恶性循环原则', '自然辩证法'),
    ('act utilitarianism', '行为功利主义（亦作“行动效用论”，审定形）', ''),
    ("Church's thesis", '丘奇论题', ''),
    ("Mach's Principle", '马赫原理', ''),
    ('context principle', '语境原理', '自然辩证法'),
    ('political obligation', '政治义务', ''),
    ("Hume's Principle", '休谟原则', ''),
    ('harm principle', '伤害原则', ''),
    ('moral skepticism', '道德怀疑论', ''),
    ('common notions', '共同概念', ''),
    ('practical syllogism', '实践三段论', ''),
    ("Frege's Theorem", '弗雷格定理', ''),
    ('mutual knowledge', '相互知识', ''),
    ('group rights', '群体权利', ''),
    ('moral naturalism', '道德自然主义', ''),
    ('methodological naturalism', '方法论自然主义', ''),
    ('phenomenal intentionality', '现象意向性', ''),
    ("Skolem's Paradox", '斯科伦悖论', ''),
    ('Humean supervenience', '休谟式随附性', ''),
    ('theory reduction', '理论还原', ''),
    ('metaphysical modality', '形而上学模态', ''),
    ('radical empiricism', '彻底经验主义', ''),
    ('abstraction principles', '抽象原则', ''),
    ('double consciousness', '双重意识', ''),
    ('Transcendental Logic', '先验逻辑', ''),
    ('dependence logic', '依赖逻辑', ''),
    ('meaning holism', '意义整体论', ''),
    ('Moral Perception', '道德知觉', ''),
    ('approximate truth', '近似真', ''),
    ('moral necessity', '道德必然性', ''),
    ('transcendental realism', '先验实在论', ''),
    ("Simpson's Paradox", '辛普森悖论', ''),
    ('actual causation', '实际因果', ''),
    ('Pareto principle', '帕累托原则', ''),
    ('historical epistemology', '历史认识论', ''),
    ('Inquisitive Semantics', '探询语义学', ''),
    ('situation theory', '情境理论', ''),
    ("Turing's thesis", '图灵论题', ''),
]

rows = []
for en, zh, db in ROWS:
    if db:
        basis = '审定名词库（termonline-all·%s，凭证 2026-11-23）' % db
    else:
        basis = '学界通行译名（审定库无对口命中，2026-11-23）；凭证 2026-11-23'
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-23'})
out = os.path.join(RES, 'rowspec-batch10-terms.json')
json.dump({'batch': '058-batch10-terms', 'date': '2026-11-23',
           'scope': '术语第四批（审定库优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
