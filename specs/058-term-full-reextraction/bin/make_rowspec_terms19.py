# -*- coding: utf-8 -*-
"""术语第十九批 rowspec（2026-11-23）：审定对口采审定形，其余 A 档。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

ROWS = [
    ('second-order volitions', '二阶意愿', ''),
    ('singular spacetimes', '奇异时空', ''),
    ('uniformity amidst variety', '多样中的齐一', ''),
    ('unrestricted comprehension principle', '无限制概括原则', ''),
    ('artificial persons', '人造人格', ''),
    ('canonical models', '典范模型', ''),
    ('causal necessitation', '因果必然化', ''),
    ('classical particle mechanics', '经典质点力学（审定收“经典力学”）', ''),
    ('collective commitment', '集体承诺', ''),
    ('computational learning theory', '计算学习理论', ''),
    ('discourse representation structures', '话语表现结构', 'T'),
    ('formal intuition', '形式直观', ''),
    ('hard determinism', '硬决定论（审定“硬技术决定论”属技术决定论义）', ''),
    ('incomplete descriptions', '不完全描述', ''),
    ('inference tickets', '推论票券', ''),
    ('inner morality', '内在道德', ''),
    ('limiting concept', '限制性概念', ''),
    ('potential parts', '潜在部分', ''),
    ('successor ordinal', '后继序数', ''),
    ('time discounting', '时间贴现', ''),
    ('toxin puzzle', '毒素难题', ''),
    ('truth set', '真值集', ''),
    ('wu xing', '五行', 'T'),
    ('adaptive preference formation', '适应性偏好形成', ''),
    ('epistemically possible worlds', '认知可能世界', ''),
    ('equivalential calculus', '等价演算', ''),
    ('focus imaginarius', '想象焦点', ''),
    ('force indicator', '力量指示词', ''),
    ('latent variable', '潜变量', ''),
    ('legislative intent', '立法意图', ''),
    ('moral consistency reasoning', '道德一致性推理', ''),
    ('secondary intelligible', '次级可理解物', ''),
    ('transcendent ought', '超越的应当', ''),
    ('transition costs', '转换成本', ''),
    ('dialectical laws', '辩证规律', ''),
    ('emotional intelligence', '情绪智力', 'T'),
    ('intentional design', '有意设计', ''),
    ('justification problem', '证成难题', ''),
    ('universal interest', '普遍利益', ''),
    ('curved space', '弯曲空间', ''),
    ('esoteric teachings', '秘传教义', ''),
    ('mass man', '大众人', ''),
    ('perfect duplicate', '完全复制', ''),
    ('real evidence', '实物证据', ''),
    ('loyal opposition', '忠诚反对', ''),
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
out = os.path.join(RES, 'rowspec-batch27-terms.json')
json.dump({'batch': '058-batch27-terms', 'date': '2026-11-23',
           'scope': '术语第十九批（审定形优先；A 档直裁）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))
