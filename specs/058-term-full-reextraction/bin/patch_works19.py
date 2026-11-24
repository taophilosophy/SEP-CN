# -*- coding: utf-8 -*-
"""著作名第十九批补丁（2026-11-24）：Defensor Pacis 补语料短形“保卫者”。"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key, term_path  # noqa: E402

EV = 'works-batch19-2026-11-24.md'
NOTE = '语料短形作《保卫者》（35 处，2026-11-24 查，凭证 %s）' % EV

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
n = 0
for i, l in enumerate(lines):
    if not l.startswith('| '):
        continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) != 6 or norm_key(c[0]) != norm_key('Defensor Pacis / Defender of Peace'):
        continue
    if '亦作“保卫者”' not in c[2]:
        c[2] = c[2] + '（亦作“保卫者”）'
    if NOTE not in c[4]:
        c[4] = c[4].rstrip('；') + '；' + NOTE
    lines[i] = '| ' + ' | '.join(c) + ' |'
    print('改行', c[0], '->', c[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
