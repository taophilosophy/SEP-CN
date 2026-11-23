# -*- coding: utf-8 -*-
"""术语第二十二批 rowspec（2026-11-24）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('multiple modernities', '多重现代性', ''),
    ('neutral analogy', '中立类比', ''),
    ('non-overlapping magisteria', '互不重叠的权威领域', ''),
    ('phi phenomenon', '似动现象', ''),
    ('philosophical atomism', '哲学原子论', ''),
    ('positional goods', '位置性商品', ''),
    ('primitive ontology', '原初本体论', ''),
    ('reasonable person standard', '理性人标准', ''),
    ('root verses', '根本颂', ''),
    ('sensible matter', '可感质料', ''),
    ('strong internalism', '强内在主义', ''),
    ('subjective motivational set', '主观动机集', ''),
    ('subjective principle', '主观原则', ''),
    ('theological science', '神学科学', ''),
    ('theological turn', '神学转向', ''),
    ('unconditioned response', '无条件反应', 'T'),
    ('unperceived objects', '未被知觉的对象', ''),
    ('weak negation', '弱否定', ''),
    ('wretched subterfuge', '卑劣的遁词', ''),
    ('physical divisibility', '物理可分性', ''),
    ('puzzle boxes', '迷箱', ''),
    ('quantitative hedonism', '定量享乐主义', ''),
    ('reflection axiom', '反射公理', ''),
    ('backpropagation algorithm', '反向传播算法', ''),
    ('common fate', '共同命运', ''),
    ('comparative similarity', '比较相似性', ''),
    ('default assumptions', '默认假设', ''),
    ('causal transmission', '因果传递', ''),
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
out = os.path.join(RES, 'rowspec-batch32-terms.json')
json.dump({'batch': '058-batch32-terms', 'date': '2026-11-24',
           'scope': '术语第二十二批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
