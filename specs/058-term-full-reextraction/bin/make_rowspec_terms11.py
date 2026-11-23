# -*- coding: utf-8 -*-
"""术语第十一批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('infinite intellect', '无限理智', ''),
    ('living forces', '活力', ''),
    ('contextual values', '语境价值', ''),
    ('absolute conception', '绝对构想', ''),
    ('plural subject', '复数主体', ''),
    ('bargaining problem', '讨价还价问题', ''),
    ('ontological idealism', '本体论唯心论', ''),
    ('constitutive explanation', '构成性说明', ''),
    ('enabling condition', '使能条件', ''),
    ('qualitative probability', '定性概率', ''),
    ('wide content', '宽内容', ''),
    ('ultimate ends', '终极目的', ''),
    ('thought style', '思维风格', ''),
    ('deep self', '深层自我', ''),
    ('random drift', '随机漂变', ''),
    ('special revelation', '特殊启示', ''),
    ('via negativa', '否定法', ''),
    ('skillful means', '方便善巧', ''),
    ('information channels', '信息通道', 'T'),
    ('statistical relevance', '统计相关性', ''),
    ('perfect recall', '完美记忆', 'T'),
    ('relative clause', '关系从句（审定只收“子句”基形）', ''),
    ('simple natures', '简单性质', ''),
    ('empirical consciousness', '经验意识', ''),
    ('origin essentialism', '起源本质主义', ''),
    ('quantum chaos', '量子混沌', 'T'),
    ('critical idealism', '批判唯心论', ''),
    ('intelligible matter', '可理解质料', ''),
    ('implicit premise', '隐含前提', ''),
    ('mathematical structuralism', '数学结构主义', ''),
    ('moral absolutism', '道德绝对主义', ''),
    ('straight rule', '直接规则', ''),
    ('basic desert', '基本应得', ''),
    ('induction scheme', '归纳模式', ''),
    ('exclusionary reason', '排他性理由', ''),
    ('secondary substance', '第二实体', ''),
    ('social capital', '社会资本', 'T'),
    ('ability hypothesis', '能力假说', ''),
    ('guidance control', '引导控制', ''),
    ('norm psychology', '规范心理学', ''),
    ('view from nowhere', '无源之见', ''),
    ('genuine option', '真实选择', ''),
    ('institutional facts', '制度事实', ''),
    ('non-conceptual content', '非概念内容', ''),
    ('replication crisis', '重复危机', ''),
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
out = os.path.join(RES, 'rowspec-batch19-terms.json')
json.dump({'batch': '058-batch19-terms', 'date': '2026-11-23',
           'scope': '术语第十一批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
