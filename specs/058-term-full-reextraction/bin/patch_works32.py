# -*- coding: utf-8 -*-
"""著作名主形改定批（2026-11-24，批三十二）：册内主形与语料实际用法倒挂的 12 行改定。

判据：精确书名号形语料计数（非子串），新主形计数 ≥5 且高于旧主形。
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key, term_path  # noqa: E402

EV = 'works-batch32-2026-11-24.md'

# (键, 新译法, 新主形计数, 旧主形计数, 旧主形)
FIX = [
    ('Defensor Pacis / Defender of Peace', '《保卫者》（亦作“和平的保卫者”）', 35, 11, '和平的保卫者'),
    ('Democracy and Education', '《民主与教育》（亦作“民主主义与教育”）', 8, 1, '民主主义与教育'),
    ('Discourse on Metaphysics', '《形而上学谈话》（亦作“形而上学论”）', 12, 0, '形而上学论'),
    ('Either/Or', '《非此即彼》（全题《非此即彼：一个生命的残片》）', 11, 0, '非此即彼：一个生命的残片'),
    ('Elements of Theology', '《神学要素论》（亦作“神学要义”）', 23, 4, '神学要义'),
    ('Fear and Trembling', '《恐惧与战栗》（亦作“恐惧与颤栗”）', 11, 0, '恐惧与颤栗'),
    ('Matter and Memory', '《物质与记忆》（亦作“材料与记忆”）', 15, 0, '材料与记忆'),
    ('Meditations on First Philosophy', '《沉思集》（亦作“第一哲学沉思集”）', 48, 7, '第一哲学沉思集'),
    ('On Generation and Corruption', '《论生成与毁灭》（亦作“论生灭”）', 9, 8, '论生灭'),
    ('Phaedo', '《斐多》（亦作“斐多篇”）', 35, 14, '斐多篇'),
    ('Proslogion', '《宣讲篇》（亦作“宣讲”）', 15, 2, '宣讲'),
    ('Sophist', '《智者篇》（亦作“智者”）', 9, 6, '智者'),
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
    for key, new_zh, nc, oc, old in FIX:
        if norm_key(c[0]) != norm_key(key):
            continue
        if c[2] == new_zh:
            continue
        c[2] = new_zh
        note = '主形改定：语料精确形 %d 处，旧主形《%s》%d 处（2026-11-24 查，凭证 %s）' % (nc, old, oc, EV)
        if note not in c[4]:
            c[4] = c[4].rstrip('；') + '；' + note
        lines[i] = '| ' + ' | '.join(c) + ' |'
        print('改行', key, '->', c[2])
        n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
