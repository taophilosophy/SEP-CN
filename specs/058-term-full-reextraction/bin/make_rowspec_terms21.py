# -*- coding: utf-8 -*-
"""术语第二十一批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('inductive leap', '归纳跳跃', ''),
    ('jian bai', '坚白', ''),
    ('justificatory liberalism', '证成自由主义', ''),
    ('looping effect', '循环效应', ''),
    ('ming jia', '名家', 'T'),
    ('modal base', '模态基', ''),
    ('noble lie', '高贵的谎言', ''),
    ('objective attitude', '客观态度', ''),
    ('obligation dilemmas', '义务两难', ''),
    ('ontological turn', '本体论转向', ''),
    ('opaque context', '晦暗语境', ''),
    ('outlaw states', '法外国家', ''),
    ('potential outcome', '潜在结果', ''),
    ('rewrite rules', '重写规则', 'T'),
    ('ruling ideas', '统治观念', ''),
    ('social trinitarianism', '社会三一论', ''),
    ('true moral worth', '真正的道德价值', ''),
    ('zoon politikon', '政治动物', ''),
    ('beings of reason', '理性存在物', ''),
    ('five ways', '五路', ''),
    ('innocent threat', '无辜威胁', ''),
    ('mere exposure effect', '纯粹曝光效应', 'T'),
    ('mixed syllogisms', '混合三段论', ''),
    ('altruistic punishment', '利他惩罚', ''),
    ('cognitive gadgets', '认知装置', ''),
    ('color spaces', '颜色空间', 'T'),
    ('componential analysis', '成分分析法', 'T'),
    ('dead metaphors', '死隐喻', ''),
    ('dipolar theism', '双极神论', ''),
    ('ecosystem health', '生态系统健康', 'T'),
    ('emotional empathy', '情感共情', ''),
    ('empirical substructures', '经验子结构', ''),
    ('context-free grammars', '上下文无关文法', 'T'),
    ('conjugate momentum', '共轭动量', ''),
    ('crisis tendencies', '危机倾向', ''),
    ('knot diagrams', '纽结图', ''),
    ('direct self-reference', '直接自我指涉', ''),
    ('impartial care', '兼爱', ''),
    ('iconic signs', '像似符号', 'T'),
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
out = os.path.join(RES, 'rowspec-batch31-terms.json')
json.dump({'batch': '058-batch31-terms', 'date': '2026-11-23',
           'scope': '术语第二十一批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
