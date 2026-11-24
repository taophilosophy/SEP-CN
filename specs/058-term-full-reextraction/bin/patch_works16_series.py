# -*- coding: utf-8 -*-
"""著作名第十六批补丁（2026-11-24）：哲学新课题译丛 5 册与既有概念行同键者，补译本依据与亦作形。

physicalism、consequentialism、analyticity 书名与现译一致，仅补依据；
self-knowledge、moral epistemology 书名用另一通行译形，译法列补“亦作”。
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key, term_path  # noqa: E402

EV = 'works-batch16-2026-11-24.md'

# 键 -> (译法, 追加依据)
FIX = {
    'physicalism': (None,
        '华夏“哲学新课题”译丛斯图尔加《物理主义》（王华平、张文俊、赵斌译，华夏出版社 2014-03）书名同'
        '（2026-11-24 核，凭证 %s）' % EV),
    'self-knowledge': ('自我认识（亦作“自我知识”）',
        '译本《自我知识》（布瑞·格特勒著，徐竹译，华夏出版社 2013-05）书名作“自我知识”'
        '（2026-11-24 核，凭证 %s）' % EV),
    'consequentialism': (None,
        '译本德莱夫《后果主义》（余露译，华夏出版社 2016-03）书名作“后果主义”，与译法亦作形一致'
        '（2026-11-24 核，凭证 %s）' % EV),
    'analyticity': (None,
        '译本祖尔、卢米斯《分析性》（徐韬译，华夏出版社 2016-08）书名同'
        '（2026-11-24 核，凭证 %s）' % EV),
    'moral epistemology': ('道德认识论（亦作“道德知识论”）',
        '译本齐默尔曼《道德知识论》（叶磊蕾译，华夏出版社 2019-06）书名作“道德知识论”'
        '（2026-11-24 核，凭证 %s）' % EV),
}

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and c[0]:
            idx.setdefault(norm_key(c[0]), i)
n = 0
for key, (zh, note) in FIX.items():
    i = idx.get(norm_key(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [x.strip() for x in lines[i].strip().strip('|').split('|')]
    if zh:
        cells[2] = zh
    if note not in cells[4]:
        cells[4] = cells[4].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    print('改行', key, '->', cells[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
