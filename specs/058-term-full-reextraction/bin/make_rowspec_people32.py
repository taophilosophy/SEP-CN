# -*- coding: utf-8 -*-
"""人名第三十二批（2026-11-24，中文源补证）：Cappelen、Lepore、Tiwald 取中译本/期刊署名。"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
EV = 'people-cnweb-2026-11-24-b32.md'
FIX = [
    ('Herman Cappelen', '赫尔曼·卡珀朗', '开普兰',
     '中文定名补证：中译本《语义最小论与语用多元论》（刘龙根、杨枫译，上海交通大学出版社 2015，'
     'ISBN 9787313125125）署名“赫尔曼·卡珀朗”；《自足语义学》（周允程译，译林出版社 2009）作'
     '“开普兰”，入别名（2026-11-24 查，凭证 %s）' % EV),
    ('Ernest Lepore', '厄尼·莱波雷', '利珀尔 / 勒坡',
     '中文定名补证：中译本《语义最小论与语用多元论》（2015）、《想象与规约》（刘龙跟、朱晓真译，'
     '中国人民大学出版社 2017，ISBN 9787300248578）均署“厄尼·莱波雷”；《语言与价值》（江怡、氏主编，'
     '中国社会科学出版社 2017）作“勒坡”，2009 译林版作“利珀尔”，并入别名（2026-11-24 查，凭证 %s）' % EV),
    ('Justin Tiwald', '贾斯汀·提沃尔德', None,
     '中文定名补证：其论文《作为“备用机制”的儒家权利》中译（梁涛、匡钊译，《学术月刊》2013 年第 11 期；'
     '收入《美德与权利》，中国社会科学出版社 2016）署名“（美）贾斯汀·提沃尔德（Justin Tiwald）”'
     '（2026-11-24 查，凭证 %s）' % EV),
]

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 8 and c[0]:
            idx.setdefault(norm_key_quote(c[0]), i)
n = 0
for key, zh, alias, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key); continue
    c = [x.strip() for x in lines[i].strip().strip('|').split('|')]
    c[2] = zh
    if alias:
        c[1] = alias if c[1] in ('—', '') else c[1] + ' / ' + alias
    if note not in c[6]:
        c[6] = c[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(c) + ' |'
    print('改行', key, '->', c[2]); n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)
