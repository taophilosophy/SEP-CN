# -*- coding: utf-8 -*-
"""术语第十批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('cognitive success', '认知成功', ''),
    ('collective self-determination', '集体自决', ''),
    ('intentional stance', '意向立场', ''),
    ('imperfect information', '不完美信息（审定收“不完美信息博弈”）', 'T'),
    ('meaning postulates', '意义公设', ''),
    ('normative expectations', '规范性期待', ''),
    ('correspondence rules', '对应规则', 'T'),
    ('nominal essence', '名义本质', ''),
    ('modus vivendi', '权宜之计', ''),
    ('normative cognition', '规范认知', ''),
    ('res extensa', '广延实体', ''),
    ('abstract structures', '抽象结构', 'T'),
    ('perceptual learning', '知觉学习', ''),
    ('logical expressions', '逻辑表达式', 'T'),
    ('syntactic view', '句法观（审定作“理论的句法观”）', 'T'),
    ('growing block', '增长块', ''),
    ('propositional form', '命题形式', ''),
    ('existential dependence', '存在依赖', ''),
    ('relationship goods', '关系善', ''),
    ('surplus value', '剩余价值', 'T'),
    ('natural goodness', '自然善', ''),
    ('shared activity', '共享活动', ''),
    ('strong emergence', '强涌现', ''),
    ('symmetry breaking', '对称性破缺', 'T'),
    ('internal reasons', '内在理由', ''),
    ('directed graph', '有向图', 'T'),
    ('replicator dynamics', '复制者动力学', ''),
    ('multiply realized', '多重实现', ''),
    ('strategy profile', '策略组合', ''),
    ('incomplete symbols', '不完全符号', ''),
    ('state descriptions', '状态描述', ''),
    ('mutual belief', '相互信念', ''),
    ('metaphysical foundationalism', '形而上学基础主义', ''),
    ('explanatory reduction', '说明性还原（审定作“说明的还原论”）', 'T'),
    ('deep ecology', '深层生态学', 'T'),
    ('civic friendship', '公民友谊', ''),
    ('comprehensive doctrine', '完备性学说', ''),
    ('inertial mass', '惯性质量', 'T'),
    ('institutional practice', '制度实践', ''),
    ('recognition respect', '承认性尊重', ''),
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
out = os.path.join(RES, 'rowspec-batch18-terms.json')
json.dump({'batch': '058-batch18-terms', 'date': '2026-11-23',
           'scope': '术语第十批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
