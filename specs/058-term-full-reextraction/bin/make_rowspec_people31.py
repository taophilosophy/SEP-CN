# -*- coding: utf-8 -*-
"""人名第三十一批（2026-11-24，中文源补证）：阿克曼、霍尔。"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
EV = 'people-cnweb-2026-11-24-b31.md'

FIX = [
    ('Ackermann, Wilhelm', '阿克曼', None,
     '中文定名补证：中译本《数理逻辑基础》（希尔柏脱、阿克曼著，莫绍揆译，科学出版社 1958，'
     '统一书号 13031-750）作者署名“阿克曼”；北京大学哲学系逻辑学科史（2024-10-20）作'
     '“希尔伯特和阿克曼的《理论逻辑基础》”（2026-11-24 查，凭证 %s）' % EV),
    ('Hoare, C. A. R.', '托尼·霍尔', '霍尔',
     '中文定名补证：其 1969 年论文中文译介（JOVANA Education 文献馆 hoare-1969）署名'
     '“C. A. R. 霍尔（托尼·霍尔）”；中文计算机科学文献通行“霍尔逻辑”“霍尔三元组”，'
     '与本条一致（2026-11-24 查，凭证 %s；本条以通行术语为主证，权重低于中译本署名类）' % EV),
]

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0]:
            idx.setdefault(norm_key_quote(cells[0]), i)
n = 0
for key, zh, alias, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    cells[2] = zh
    if alias:
        cells[1] = alias if cells[1] in ('—', '') else cells[1] + ' / ' + alias
    if note not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    print('改行', key, '->', cells[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
