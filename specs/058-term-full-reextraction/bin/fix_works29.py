# -*- coding: utf-8 -*-
"""著作名第二十九批收尾修正（2026-11-24）。

1. 删除重复行 The Four Books（与在册 Sishu 同概念），英文异键记入 Sishu 依据。
2. Democracy and Education 补语料异形“民主与教育”。
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key, term_path  # noqa: E402

EV = 'works-batch29-2026-11-24.md'

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
out = []
removed = 0
patched = 0
for l in lines:
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and norm_key(c[0]) == norm_key('The Four Books'):
            removed += 1
            print('删行', c[0], c[2])
            continue
        if len(c) == 6 and norm_key(c[0]) == norm_key('Sishu'):
            note = '英文亦作 The Four Books（2026-11-24 查，凭证 %s）' % EV
            if note not in c[4]:
                c[4] = c[4].rstrip('；') + '；' + note
                l = '| ' + ' | '.join(c) + ' |'
                patched += 1
                print('改行 Sishu（并记英文异键）')
        if len(c) == 6 and norm_key(c[0]) == norm_key('Democracy and Education'):
            if '亦作“民主与教育”' not in c[2]:
                c[2] = '《民主主义与教育》（亦作“民主与教育”）'
                note = '语料形作《民主与教育》（8 处，2026-11-24 查，凭证 %s）' % EV
                if note not in c[4]:
                    c[4] = c[4].rstrip('；') + '；' + note
                l = '| ' + ' | '.join(c) + ' |'
                patched += 1
                print('改行 Democracy and Education ->', c[2])
    out.append(l)
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(out))
print('removed=%d patched=%d' % (removed, patched))
