# -*- coding: utf-8 -*-
"""著作名第二十一批短形补丁（2026-11-24）：Phaedo／Timaeus／Meditations 三行补语料短形。"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key, term_path  # noqa: E402

EV = 'works-batch21-2026-11-24.md'

FIX = [
    ('Phaedo', '《斐多篇》', '《斐多篇》（亦作“斐多”）', '斐多', 35),
    ('Timaeus', '《蒂迈欧篇》', '《蒂迈欧篇》（亦作“蒂迈欧”）', '蒂迈欧', 19),
    ('Meditations on First Philosophy', '《第一哲学沉思集》',
     '《第一哲学沉思集》（亦作“沉思集”）', '沉思集', 48),
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
    for key, _zh, want, alias, freq in FIX:
        if norm_key(c[0]) != norm_key(key):
            continue
        if '亦作“%s”' % alias not in c[2]:
            c[2] = want
            note = '语料短形作《%s》（%d 处，2026-11-24 查，凭证 %s）' % (alias, freq, EV)
            if note not in c[4]:
                c[4] = c[4].rstrip('；') + '；' + note
            lines[i] = '| ' + ' | '.join(c) + ' |'
            print('改行', key, '->', c[2])
            n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
