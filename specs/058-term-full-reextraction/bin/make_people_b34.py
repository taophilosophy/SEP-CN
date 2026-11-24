# -*- coding: utf-8 -*-
"""人名第三十四批（2026-11-24，中文源补证）：七人取汉名。

Batson、Beauchamp、Childress、Longuenesse、Brian Ellis、Bostock、Burgess；
Beckner、Amundson、Boehner 三人查无，留英文并记凭证。
"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
EV = 'people-cnweb-2026-11-24-b34.md'

FIX = [
    ('Batson, C. Daniel', 'C. 丹尼尔·巴特森', None,
     '中文定名补证：中译本《利他实验：人类真的只关心自己吗》（白学军译，中国人民大学出版社 '
     '2024-07，ISBN 9787300328836）作者署名“C.丹尼尔·巴特森”，三民书局简体书目页同'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Beauchamp, Tom', '汤姆·比彻姆', None,
     '中文定名补证：《生命医学伦理原则》第 5 版（李伦译，北京大学出版社 2014-08）与第 8 版'
     '（刘星等译，科学出版社 2022-09，ISBN 9787030730527）作者署名“汤姆·比彻姆”'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Childress, James', '詹姆士·邱卓思', None,
     '中文定名补证：同上两版中译本作者署名“詹姆士·邱卓思”（第 8 版图书在版编目题名责任者项'
     '作 James F. Childress 对应“邱卓思”）（2026-11-24 查，凭证 %s）' % EV),
    ('Béatrice Longuenesse', '贝亚特丽斯·隆格内斯', None,
     '中文定名补证：王策、金延《从康德到弗雷格——论先验逻辑对现代逻辑的奠基》，'
     '《科学技术哲学研究》2016 年第 4 期作“B·隆格内斯（Béatrice Longuenesse）”；'
     '豆瓣《黑格尔的逻辑学与形而上学》书评（2025-06）作“贝亚特丽斯·隆格内斯”'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Brian Ellis', '布雷恩·埃利斯', None,
     '中文定名补证：金吾伦《埃利斯的内在实在论》（1989 年第 6 期）作“布雷恩·D. 埃利斯”；'
     '张建琴《新本质主义研究》（九州出版社 2024-03，ISBN 9787522524917）通篇作“埃利斯”'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Bostock, David', '戴维·波斯托克', None,
     '中文定名补证：刘胜利、张卜天《位置的不动性——亚里士多德位置学说的理论困难》，'
     '《中国科技史杂志》2011 年第 3 期作“波斯托克（David Bostock）”'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Burgess, John P.', '约翰·P. 伯吉斯', None,
     '中文定名补证：薄谋《基于限制版第五基本定律的抽象主义集合论》（2022 年第 7 期）'
     '作“伯吉斯”（2026-11-24 查，凭证 %s）' % EV),
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
