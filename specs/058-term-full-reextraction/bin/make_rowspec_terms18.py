# -*- coding: utf-8 -*-
"""术语第十八批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('thick description', '厚描', ''),
    ('socialist calculation debate', '社会主义计算争论', ''),
    ('affective disposition', '情感倾向', ''),
    ('amor fati', '命运之爱', ''),
    ('autonoetic consciousness', '自传体意识', ''),
    ('black nationalism', '黑人民族主义', ''),
    ('computational architecture', '计算架构', ''),
    ('consistency preservation', '一致性保持', ''),
    ('critical disability studies', '批判残障研究', ''),
    ('dogmatic idealism', '独断唯心论', ''),
    ('dynamic doxastic logic', '动态信念逻辑', ''),
    ('evidential symmetry', '证据对称性', ''),
    ('experimental metaphysics', '实验形而上学', ''),
    ('explanatory dependence', '说明性依赖', ''),
    ('extensive magnitudes', '广延量', ''),
    ('folk theorem', '民间定理', ''),
    ('fork asymmetry', '叉形不对称', ''),
    ('great self', '大我', ''),
    ('inner imitation', '内模仿', ''),
    ('intervention variable', '干预变量', ''),
    ('inverse probabilities', '逆概率', ''),
    ('joint strategy', '联合策略', ''),
    ('locutionary acts', '以言表意行为', ''),
    ('metaphysical disjunctivism', '形而上学析取论', ''),
    ('motor theory', '运动理论', ''),
    ('neural reuse', '神经重用', ''),
    ('non-wellfounded sets', '非良基集合', ''),
    ('normal systems', '正规系统', ''),
    ('objective consequentialism', '客观后果主义', ''),
    ('philosophical necessity', '哲学必然性', ''),
    ('plastic natures', '可塑本性', ''),
    ('pointed graph', '带点图', ''),
    ('posteriori physicalism', '后验物理主义', ''),
    ('pre-reflective self-awareness', '前反思自我意识', ''),
    ('primal impressions', '原初印象', ''),
    ('primary intelligibles', '第一可理解物', ''),
    ('proper sensible', '特有可感物', ''),
    ('regulae philosophandi', '哲学规则', ''),
    ('risk imposition', '风险施加', ''),
    ('savings principle', '储蓄原则', ''),
    ('sceptical solution', '怀疑论解决', ''),
    ('social ecology', '社会生态学', 'T'),
    ('somatic markers', '躯体标记', ''),
    ('supreme emergencies', '极端紧急状态', ''),
    ('terror bombing', '恐怖轰炸', ''),
    ('transcendental ground', '先验根据', ''),
    ('truth maker', '真值制造者', ''),
    ('weak completeness', '弱完全性', ''),
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
out = os.path.join(RES, 'rowspec-batch26-terms.json')
json.dump({'batch': '058-batch26-terms', 'date': '2026-11-23',
           'scope': '术语第十八批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
