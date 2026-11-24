# -*- coding: utf-8 -*-
"""人名第三十批（2026-11-24，中文源补证）：逻辑学书目作者六人取中译本/中文期刊定名。"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
EV = 'people-cnweb-2026-11-24-b30.md'

# (键, 新译法, 新别名或 None, 追加依据)
FIX = [
    ('Bocheński, Józef M.', '鲍亨斯基', '波亨斯基',
     '中文定名补证：中译本《当代思维方法》（上海人民出版社 1987，ISBN 9787208000056）'
     '作者署名“J.M.鲍亨斯基”；中国社会科学网 2025-02-12 李杜白、王克喜文作“波亨斯基（J. M. '
     'Bochenski）”并引其《形式逻辑史》，臺北市立大學圖書館 MARC 亦作“波亨斯基”，异形入别名'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Burge, Tyler', '泰勒·伯奇', None,
     '中文定名补证：蒋薇《知觉表征及其界限——泰勒·伯奇的知觉观探究》，《外国哲学》2016 年第 2 期'
     '作“泰勒·伯奇（Tyler Burge）”（2026-11-24 查，凭证 %s）' % EV),
    ('Belnap, Nuel', '贝尔纳普', None,
     '中文定名补证：程京德（南京大学现代逻辑与逻辑应用研究所）科学网“相关逻辑”系列博文'
     '（2024-06-18）作“安德森和贝尔纳普”，述《蕴涵：相关性与必要性的逻辑》（2026-11-24 查，'
     '凭证 %s）' % EV),
    ('Anderson, Alan Ross', '安德森', None,
     '中文定名补证：同程京德“相关逻辑”系列博文作“安德森”（系统 E 的提出者之一）'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Barwise, Jon', '乔恩·巴威斯', None,
     '中文定名补证：中译本《说谎者悖论：真与循环》（贾国恒译，南京大学出版社 2022，'
     'ISBN 9787305250996）作者署名“乔恩·巴威斯”；澎湃新闻 2022-05-24 书摘同'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Etchemendy, John', '约翰·埃切曼迪', None,
     '中文定名补证：同书中译本作者署名“约翰·埃切曼迪”；三民书局简体书目页同'
     '（2026-11-24 查，凭证 %s）' % EV),
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
