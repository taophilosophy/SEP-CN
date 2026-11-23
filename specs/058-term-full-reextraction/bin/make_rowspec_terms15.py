# -*- coding: utf-8 -*-
"""术语第十五批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('legal phenomena', '法律现象', ''),
    ('memory criterion', '记忆标准', ''),
    ('transcendental illusion', '先验幻相', ''),
    ('analogical extension', '类比扩展', ''),
    ('base rate fallacy', '基率谬误', 'T'),
    ('bivalent semantics', '二值语义学', ''),
    ('causally sufficient condition', '因果充分条件', ''),
    ('degrees of belief', '信念度', 'T'),
    ('esoteric morality', '秘传道德', ''),
    ('extensional type theory', '外延类型论', ''),
    ('game forms', '博弈形式', ''),
    ('island universes', '岛宇宙', 'T'),
    ('matters of fact', '事实问题', ''),
    ('missing heritability', '缺失遗传率', ''),
    ('protophenomenal properties', '原现象性质', ''),
    ('received opinions', '公认意见', ''),
    ('strong objectivity', '强客观性', ''),
    ('adventitious ideas', '外来的观念', ''),
    ('appraisal respect', '评价性尊重', ''),
    ('belief box', '信念盒', ''),
    ('calculus ratiocinator', '推理演算', ''),
    ('characterization theorems', '刻画定理', ''),
    ('domain specificity', '领域特殊性（审定收“领域特殊理论”）', ''),
    ('explanatory autonomy', '说明自主性', ''),
    ('identification problem', '识别问题', 'T'),
    ('intuition pumps', '直觉泵', ''),
    ('mind reading', '读心术', 'T'),
    ('molecular clock', '分子钟', 'T'),
    ('negative analogy', '否定类比', ''),
    ('plural voting', '复数投票', ''),
    ('soft paternalism', '软家长主义', ''),
    ('strange attractor', '奇怪吸引子', 'T'),
    ('universal algebra', '泛代数', 'T'),
    ('universal rights', '普遍权利', ''),
    ('appearance properties', '显象性质', ''),
    ('disposition terms', '倾向词项', ''),
    ('pairwise majority voting', '两两多数投票', ''),
    ('prior odds', '先验几率', ''),
    ('pure perfections', '纯粹完善性', ''),
    ('abstract individualism', '抽象个人主义', ''),
    ('epigenetic landscape', '表观遗传景观', ''),
    ('narrative self', '叙事自我', ''),
    ('normative positions', '规范立场', ''),
    ('reduction strategy', '还原策略', ''),
    ('safe belief', '安全信念', ''),
    ('stochastic dominance', '随机占优（审定收“随机优势决策”）', ''),
    ('analytical hierarchy', '解析分层', 'T'),
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
out = os.path.join(RES, 'rowspec-batch23-terms.json')
json.dump({'batch': '058-batch23-terms', 'date': '2026-11-23',
           'scope': '术语第十五批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
