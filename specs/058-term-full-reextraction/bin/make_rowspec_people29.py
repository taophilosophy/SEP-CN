# -*- coding: utf-8 -*-
"""人名第二十九批（2026-11-24，中文源补证）：Chang、Stoljar、Zack 取中文文献/中译本定名。"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
EV = 'people-cnweb-2026-11-24-b29.md'

# (键, 新译法, 追加依据)
FIX = [
    ('Hasok Chang', '张夏硕',
     '中文定名补证：中国人民大学科技哲学前沿讲座第 61 讲页面（pstruc.org，2023-06-14）作'
     '“张夏硕（Hasok Chang）”，并述其专著《发明温度》《水是 H2O 吗？》；韩国姓名汉字对应'
     '（2026-11-24 查，凭证 %s；百度百科“哈索克·张”为音译形，不采）' % EV),
    ('Daniel Stoljar', '丹尼尔·斯图嘉',
     '中文定名补证：中国社会科学院哲学研究所“哲学中国网”《意识的认知理论》一文作'
     '“澳大利亚哲学家丹尼尔·斯图嘉（Daniel Stoljar）”，并译其书为《无知与想象：意识问题的'
     '认知根源》（2026-11-24 查，凭证 %s）' % EV),
    ('Naomi Zack', '内奥米·扎克',
     '中文定名补证：中译本《智慧百科·智慧的声音：探索哲学之谜》（李哲等译，上海科学技术文献'
     '出版社 2025，ISBN 9787543993198）作者署名“内奥米·扎克”（2026-11-24 查，凭证 %s）' % EV),
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
for key, zh, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    cells[2] = zh
    if note not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    print('改行', key, '|', cells[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
