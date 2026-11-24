# -*- coding: utf-8 -*-
"""概念行主形改定批（2026-11-24，批三十三）：语料主导形与册内主形倒挂的 7 行。

经语境核身确认漂移（排除子串／泛义假漂移），按语料主导形改定。
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key, term_path  # noqa: E402

EV = 'works-batch33-2026-11-24.md'

# (键, 新译法, 核身处)
FIX = [
    ('anomalous monism', '变异一元论（亦作“异常一元论”）',
     '戴维森条目通篇用“变异一元论”；册内原“异常一元论”全库 0 处'),
    ('conditional analysis', '条件句分析（亦作“条件分析”）',
     'abilities 条目作“条件句分析”（36 处）；原“条件分析”仅 6 处'),
    ('Peano arithmetic', '皮亚诺算术（亦作“佩亚诺算术”）',
     'deductivism 等条目作“皮亚诺算术”（15 处）；原“佩亚诺算术”0 处'),
    ('tea ceremony', '茶道（亦作“茶道仪式”）',
     'aesthetics-of-everyday 条目作“茶道”（22 处）；原“茶道仪式”0 处'),
    ('samavāyi-kāraṇa', '依处因（亦作“和合因”）',
     'early-modern-india 条目作“依处因”，括注“即和合因”；原“和合因”仅 7 处'),
    ('ceteris paribus', '其余条件相同（亦作“其他条件不变”）',
     'justep-coherence 等条目作“其余条件相同”（34 处）；原“其他条件不变”仅 11 处'),
    ('knowing how', '知道如何（knowledge how）',
     'abilities 条目作“知道如何”；原“技能知识”全库 0 处'),
]

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
n = 0
for i, l in enumerate(lines):
    if not l.startswith('| '):
        continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) != 6:
        continue
    for key, new_zh, why in FIX:
        if norm_key(c[0]) != norm_key(key):
            continue
        if c[2] == new_zh:
            continue
        c[2] = new_zh
        note = '主形改定：%s（2026-11-24 语料核对，凭证 %s）' % (why, EV)
        if note not in c[4]:
            c[4] = c[4].rstrip('；') + '；' + note
        lines[i] = '| ' + ' | '.join(c) + ' |'
        print('改行', key, '->', c[2])
        n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
