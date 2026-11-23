# -*- coding: utf-8 -*-
"""术语第二十三批 rowspec（2026-11-24）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('hedonic tone', '享乐基调', ''),
    ('higher-order reasoning', '高阶推理', ''),
    ('how-possibly explanations', '如何可能说明', 'T'),
    ('implicit conventions', '隐含约定', ''),
    ('inductive strategy', '归纳策略', ''),
    ('inequity aversion', '不公平厌恶', ''),
    ('inner negation', '内否定', ''),
    ('invariance condition', '不变性条件', ''),
    ('leaf node', '叶节点', 'T'),
    ('legal accountability', '法律问责', ''),
    ('mechanism sketch', '机制草图', ''),
    ('mental dictionary', '心理词典', ''),
    ('mental time-travel', '心理时间旅行', ''),
    ('non-collapse interpretation', '非坍缩诠释', ''),
    ('nuisance parameters', '冗余参数', 'T'),
    ('peace education', '和平教育', 'T'),
    ('pluralist cosmopolitanism', '多元世界主义', ''),
    ('political moralism', '政治道德主义', ''),
    ('private government', '私人政府', ''),
    ('private object', '私人对象', ''),
    ('problem of the many', '多一问题', ''),
    ('projection rules', '投影规则', ''),
    ('projective determinacy', '投影确定性', 'T'),
    ('psychological altruists', '心理利他主义者', ''),
    ('public purpose', '公共目的', ''),
    ('purposiveness without purpose', '无目的的合目的性', ''),
    ('quinque voces', '五谓', ''),
    ('random walk', '随机游走（审定作“无规行走”）', 'T'),
    ('read-write head', '读写头（审定作“读写磁头”）', 'T'),
    ('species problem', '物种问题', ''),
    ('split brain', '裂脑（审定亦作“分裂脑”）', 'T'),
    ('taxonomic incommensurability', '分类学不可通约性', ''),
    ('temporal authority', '世俗权威', ''),
    ('vita contemplativa', '沉思生活', ''),
    ('wrongful threats', '不当威胁', ''),
]

rows = []
for en, zh, db in ROWS:
    if db == 'T':
        basis = '审定名词库（termonline-all，凭证 2026-11-24）'
    else:
        basis = '学界通行译名（审定库无对口命中，2026-11-24）；凭证 2026-11-24'
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch33-terms.json')
json.dump({'batch': '058-batch33-terms', 'date': '2026-11-24',
           'scope': '术语第二十三批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
