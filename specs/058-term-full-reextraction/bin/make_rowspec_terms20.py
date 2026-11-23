# -*- coding: utf-8 -*-
"""术语第二十批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('chilling effect', '寒蝉效应', 'T'),
    ('descriptive names', '描述性名称', ''),
    ('effortless action', '无为', ''),
    ('file drawer', '文件抽屉', ''),
    ('functional biology', '功能生物学', ''),
    ('legal fiction', '法律拟制', ''),
    ('logical independence', '逻辑独立性', ''),
    ('mathematical sublime', '数学崇高', ''),
    ('minimally conscious state', '微小意识状态', 'T'),
    ('moral grammar', '道德语法', ''),
    ('non-deterministic matrices', '非确定性矩阵', ''),
    ('non-reductive materialism', '非还原唯物主义', ''),
    ('organized beings', '有机存在者', ''),
    ('possibility proof', '可能性证明', ''),
    ('proprioceptive experiences', '本体感受经验', ''),
    ('recursive sets', '递归集', 'T'),
    ('reflexive-transitive closure', '自反传递闭包', ''),
    ('seeing as', '看作', ''),
    ('situationist challenge', '情境主义挑战', ''),
    ('subjective universality', '主观普遍性', ''),
    ('substantial universals', '实体共相', ''),
    ('supernatural revelation', '超自然启示', ''),
    ('transmission genetics', '传递遗传学', ''),
    ('bare demonstratives', '裸指示词', ''),
    ('betting quotient', '赌商', ''),
    ('blind variation', '盲目变异', ''),
    ('causal anomalies', '因果异常', ''),
    ('classical recapture', '经典回收', ''),
    ('closed world assumption', '封闭世界假设', 'T'),
    ('club goods', '俱乐部物品', ''),
    ('collective defeat', '集体挫败', ''),
    ('conditioned stimulus', '条件刺激', 'T'),
    ('conversational score', '会话记分', ''),
    ('defeating condition', '挫败条件', ''),
    ('design stance', '设计立场', ''),
    ('democratic discussion', '民主讨论', ''),
    ('dualistic thinking', '二元思维', ''),
    ('epistemic counterpart', '认知对应物', ''),
    ('invisible agent', '无形行动者', ''),
    ('minimal definition', '最简定义', ''),
    ('social friction', '社会摩擦', ''),
    ('structural characterization', '结构刻画', ''),
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
out = os.path.join(RES, 'rowspec-batch30-terms.json')
json.dump({'batch': '058-batch30-terms', 'date': '2026-11-23',
           'scope': '术语第二十批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
