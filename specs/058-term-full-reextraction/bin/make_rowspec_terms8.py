# -*- coding: utf-8 -*-
"""术语第八批 rowspec（2026-11-23）：审定对口者采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('outer quantifiers', '外量词', ''),
    ('priority argument', '优先性论证', ''),
    ('procedural rationality', '程序合理性', ''),
    ('Scandinavian realism', '斯堪的纳维亚实在论', ''),
    ('substitutivity principles', '可替换性原则', ''),
    ('type-type reduction', '类型-类型还原', ''),
    ("victors' justice", '胜利者正义', ''),
    ('weak dualism', '弱二元论', ''),
    ('aesthetic empiricism', '审美经验主义', ''),
    ('applied metaphysics', '应用形而上学', ''),
    ("Darwin's argument", '达尔文论证', ''),
    ('fundamental obligation', '基本义务', ''),
    ('genuine modal realism', '真正的模态实在论', ''),
    ('model-theoretic truth', '模型论真理', ''),
    ('preferential entailment', '偏好蕴涵', ''),
    ("Putnam's paradox", '普特南悖论', ''),
    ('Quine-Duhem thesis', '蒯因-迪昂论题（审定作“迪昂-诺伊拉特-蒯因命题”）', ''),
    ('strong reduction', '强还原', ''),
    ('Temporal parts theory', '时间部分理论', ''),
    ('term logics', '词项逻辑', ''),
    ('veil of perception', '知觉之幕', ''),
    ('weak anthropic principle', '弱人择原理（审定只收“人择原理”）', ''),
    ('Benthamite utilitarianism', '边沁式功利主义', ''),
    ('Cartesian Skeptical Argument', '笛卡尔式怀疑论论证', ''),
    ('complex reference', '复合指称', ''),
    ('Composition Theorem', '组合定理', ''),
    ('cultural naturalism', '文化自然主义', ''),
    ('dynamic consistency', '动态一致性', ''),
    ('functional completeness', '功能完备性', ''),
    ('gauge argument', '规范论证', ''),
    ('general correspondence principle', '一般对应原理（审定作“对应原理”）', ''),
    ('Generic Realism', '一般实在论', ''),
    ('Gibbard-Satterthwaite theorem', '吉伯德-萨特思韦特定理', ''),
    ('identity reduction', '同一性还原', ''),
    ('inner sensation', '内感觉', ''),
    ("Liar's paradox", '说谎者悖论', ''),
    ('metaphysical causation', '形而上学因果', ''),
    ('non-radical reductionism', '非激进还原论', ''),
    ('normative agency', '规范性能动性', ''),
    ('occasional identity', '偶然同一性', ''),
    ('Parity Principle', '对等原则', ''),
    ('pluralistic relativism', '多元相对主义', ''),
    ('priority thesis', '优先性论题', ''),
    ("Quine's paradox", '蒯因悖论', ''),
    ('reasons holism', '理由整体论', ''),
    ('relevant alternatives theory', '相关选项理论', ''),
    ('Responsibility Principle', '责任原则', ''),
    ('structuralist thesis', '结构主义论题', ''),
    ('subjective consequentialism', '主观后果主义', ''),
    ('unalienable rights', '不可让与权利', ''),
    ('Unconditional belief', '无条件信念', ''),
    ('uniform continuity theorem', '一致连续性定理', ''),
    ('weak holism', '弱整体论', ''),
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
out = os.path.join(RES, 'rowspec-batch16-terms.json')
json.dump({'batch': '058-batch16-terms', 'date': '2026-11-23',
           'scope': '术语第八批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
