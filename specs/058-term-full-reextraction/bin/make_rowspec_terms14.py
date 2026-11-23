# -*- coding: utf-8 -*-
"""术语第十四批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('decisional privacy', '决策性隐私', 'T'),
    ('event time', '事件时间', 'T'),
    ('game formalism', '游戏形式主义', ''),
    ('operational analysis', '操作分析', ''),
    ('surrogative reasoning', '替代推理', ''),
    ('controlled experiment', '对照实验', ''),
    ('dynamically sublime', '力学崇高', ''),
    ('grand narratives', '宏大叙事', ''),
    ('local contexts', '局部语境', ''),
    ('tode ti', '这一个', ''),
    ('absent qualia', '缺失感质', ''),
    ('artificial agent', '人工行动者', ''),
    ('consistency conditions', '相容条件', 'T'),
    ('coordinative definitions', '协调定义', ''),
    ('design hypothesis', '设计假说', ''),
    ('egalitarian ethos', '平等主义风气', ''),
    ('four beginnings', '四端', ''),
    ('predicative functions', '谓述函数', ''),
    ('quantum object', '量子对象', ''),
    ('strict conditionals', '严格条件句', ''),
    ('surveillance capitalism', '监控资本主义', ''),
    ('transcendental object', '先验对象', ''),
    ('unarticulated constituents', '未言明成分', ''),
    ('constrained maximization', '约束最大化', ''),
    ('epistemic entitlement', '认知资格', ''),
    ('first-order structure', '一阶结构', ''),
    ('non-eliminative structuralism', '非消除性结构主义', ''),
    ('plenitudinous platonism', '丰饶柏拉图主义', ''),
    ('abstract artifact', '抽象人造物', ''),
    ('color line', '肤色界线', ''),
    ('directed acyclic graph', '有向无环图', 'T'),
    ('discourse anaphora', '话语照应（审定只收“回指／指代”）', ''),
    ('essential indexical', '本质索引词', ''),
    ('ethical community', '伦理共同体', ''),
    ('faith seeking understanding', '信仰寻求理解', ''),
    ('folk biology', '民间生物学', ''),
    ('justice as fairness', '作为公平的正义', ''),
    ('money pump', '货币泵', ''),
    ('phenomenal contrast', '现象对比', ''),
    ('prenex form', '前束范式', 'T'),
    ('sensible representations', '感性表象', ''),
    ('single negation', '单否定', ''),
    ('third dogma', '第三教条', ''),
    ('token physicalism', '个例物理主义', ''),
    ('extended simple', '延展简单物', ''),
    ('inertial system', '惯性系统', 'T'),
    ('knowing how', '技能知识（亦作“知道如何”）', 'T'),
    ('complete problems', '完全问题', 'T'),
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
out = os.path.join(RES, 'rowspec-batch22-terms.json')
json.dump({'batch': '058-batch22-terms', 'date': '2026-11-23',
           'scope': '术语第十四批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
