# -*- coding: utf-8 -*-
"""著作名第十七批补丁（2026-11-24）：Theory of Justice 已在册，补中译本依据与 SEP 题名异形。"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key, term_path  # noqa: E402

EV = 'works-batch17-2026-11-24.md'
NOTE = ('权威译本（何怀宏、何包钢、廖申白译，中国社会科学出版社 1988-03；2009-07 修订版 '
        'ISBN 9787500479543）；SEP 正文题名作 A Theory of Justice'
        '（2026-11-24 联网核对，凭证 %s）' % EV)

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
n = 0
for i, l in enumerate(lines):
    if not l.startswith('| '):
        continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) != 6 or norm_key(c[0]) != norm_key('Theory of Justice'):
        continue
    if NOTE not in c[4]:
        c[4] = c[4].rstrip('；') + '；' + NOTE
    lines[i] = '| ' + ' | '.join(c) + ' |'
    print('改行', c[0], '->', c[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
