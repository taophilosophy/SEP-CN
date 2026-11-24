# -*- coding: utf-8 -*-
"""著作名第三十批修正（2026-11-24）：并入在册 System of Nature，另立 Cosmogony (Ehrenfels)。"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key, term_path  # noqa: E402

EV = 'works-batch30-2026-11-24.md'

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
out = []
removed = 0
patched = 0
for l in lines:
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and norm_key(c[0]) == norm_key('The System of Nature'):
            removed += 1
            print('删行', c[0], c[2])
            continue
        if len(c) == 6 and norm_key(c[0]) == norm_key('System of Nature'):
            note = '英文亦作 The System of Nature（全题 The System of Nature, or Laws of the Moral and Physical World；2026-11-24 查，凭证 %s）' % EV
            if note not in c[4]:
                c[4] = c[4].rstrip('；') + '；' + note
                l = '| ' + ' | '.join(c) + ' |'
                patched += 1
                print('改行 System of Nature（并记英文全题）')
    out.append(l)
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(out))
print('removed=%d patched=%d' % (removed, patched))
