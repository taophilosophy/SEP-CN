# -*- coding: utf-8 -*-
"""术语第五批 rowspec（2026-11-23）：审定对口者采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('primary obligation', '初级义务', ''),
    ('general semantics', '普通语义学', '语言学'),
    ('mathematical intuition', '数学直觉', '自然辩证法'),
    ('Copy Principle', '临摹性原则（亦作“拷贝原则”）', '自然辩证法'),
    ('analytic naturalism', '分析自然主义', ''),
    ('no-classes theory', '无类理论', '自然辩证法'),
    ('premise semantics', '前提语义学', ''),
    ("Church's theorem", '丘奇定理', ''),
    ('empirical realism', '经验实在论', ''),
    ('representative realism', '表象实在论', ''),
    ("Fitch's Paradox", '菲奇悖论', ''),
    ('forward induction', '前向归纳', ''),
    ('binding theory', '约束理论', '语言学'),
    ('multiple relation theory', '多元关系理论', ''),
    ('perspectival realism', '视角实在论', ''),
    ('strategic rationality', '策略合理性', ''),
    ('storehouse consciousness', '阿赖耶识（藏识）', ''),
    ('well-ordering principle', '良序原则', '数学'),
    ("Bohr's correspondence principle", '玻尔对应原理（审定作“对应原理”）', '物理学'),
    ('immanent realism', '内蕴实在论', ''),
    ('miracle argument', '奇迹论证', ''),
    ('team semantics', '团队语义学', ''),
    ('combinatorial argument', '组合论证', ''),
    ('recursive function theory', '递归函数论', ''),
    ("Bertrand's Paradox", '伯特兰悖论', ''),
    ('default theory', '缺省理论', ''),
    ('entity realism', '实体实在论', '自然辩证法'),
    ('epistemological idealism', '认识论唯心论', ''),
    ('Phenomenal Principle', '现象原则', ''),
    ('monadic second-order logic', '一元二阶逻辑', ''),
    ('critical rationalism', '批判理性主义', '自然辩证法'),
    ('gauge principle', '规范原理', ''),
    ('adaptive logics', '适应逻辑', ''),
    ('empirical idealism', '经验唯心论', ''),
    ('diagonal proposition', '对角命题', ''),
    ('genetic fallacy', '发生学谬误', ''),
    ('token causation', '个例因果', ''),
    ("Cantor's paradox", '康托尔悖论', ''),
    ('logical connection argument', '逻辑关联论证', ''),
    ('effective field theory', '有效场理论（亦作“有效场论”）', '物理学'),
    ('radical pluralism', '激进多元论', ''),
    ("Yablo's paradox", '亚布洛悖论', ''),
    ('Knowability Paradox', '可知性悖论', ''),
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
out = os.path.join(RES, 'rowspec-batch11-terms.json')
json.dump({'batch': '058-batch11-terms', 'date': '2026-11-23',
           'scope': '术语第五批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
