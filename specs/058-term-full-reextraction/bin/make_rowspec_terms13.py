# -*- coding: utf-8 -*-
"""术语第十三批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('copy theory', '模写论', ''),
    ('descriptive functions', '描述函数', ''),
    ('historical entitlement', '历史资格', ''),
    ('inner models', '内模型', ''),
    ('interventionist counterfactuals', '干预主义反事实', ''),
    ('non-normative facts', '非规范事实', ''),
    ('cumulative culture', '累积文化', ''),
    ('experimental mathematics', '实验数学', ''),
    ('classical foundationalism', '古典基础主义', ''),
    ('contextual integrity', '语境完整性', ''),
    ('epistemic relevance', '认知相关性', ''),
    ('fundamental reasons', '根本理由', ''),
    ('lexical entries', '语词条目', 'T'),
    ('moral formation', '道德养成', ''),
    ('presupposition triggers', '预设触发语', ''),
    ('ramified hierarchy', '分支层级', ''),
    ('eternal present', '永恒现在', ''),
    ('general recursive functions', '一般递归函数', ''),
    ('linguistic relativity', '语言相对论', 'T'),
    ('scientific materialism', '科学唯物主义', ''),
    ('logical content', '逻辑内容', ''),
    ('bare plurals', '裸复数', ''),
    ('ancient theology', '古代神学', ''),
    ('decent peoples', '正派民族', ''),
    ('epistemic oppression', '认知压迫', ''),
    ('wrongful exploitation', '不当剥削', ''),
    ('centered world', '中心化世界', ''),
    ('composite substances', '复合实体', ''),
    ('generative grammar', '生成语法', 'T'),
    ('infinite attributes', '无限属性', ''),
    ('nonexistent object', '不存在对象', ''),
    ('event calculus', '事件演算', 'T'),
    ('judgeable contents', '可判断内容', ''),
    ('analytic sets', '解析集', 'T'),
    ('judgement stroke', '判断线', ''),
    ('particle interpretation', '粒子诠释', ''),
    ('set variables', '集合变元', ''),
    ('social transmission', '社会传递', ''),
    ('causal past', '因果过去', ''),
    ('conceptual coherence', '概念融贯', ''),
    ('machine table', '机器表', ''),
    ('reverse engineering', '逆向工程', 'T'),
    ('third realm', '第三领域', ''),
    ('cognitive revolution', '认知革命', 'T'),
    ('free play', '自由游戏（审定收“游戏活动”，属幼教义）', ''),
    ('smooth infinitesimal analysis', '光滑无穷小分析（审定收“无穷小分析”）', ''),
    ('expected utility maximization', '期望效用最大化（审定只收“期望效用”基形）', ''),
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
out = os.path.join(RES, 'rowspec-batch21-terms.json')
json.dump({'batch': '058-batch21-terms', 'date': '2026-11-23',
           'scope': '术语第十三批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
