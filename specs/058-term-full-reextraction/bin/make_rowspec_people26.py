# -*- coding: utf-8 -*-
"""人名第二十六批（2026-11-24，中文源补证）：5 人取中文定名，Kamm 同人异键合并。"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
EV = 'people-cnweb-2026-11-24-b26.md'

# (键, 新译法或 None, 新别名或 None, 追加依据)
FIX = [
    ('Susan Bordo', '苏珊·鲍尔多', None,
     '中文定名补证：中译本《不能承受之重：女性主义、西方文化与身体》（綦亮、赵育春译，'
     '江苏人民出版社 2009，ISBN 9787214058652）作者署名“苏珊·鲍尔多”；豆瓣读书、查字典'
     '图书频道同（2026-11-24 查，见 %s）' % EV),
    ('Berys Gaut', '贝里斯·高特', None,
     '中文定名补证：李桢、沈语冰《“道德美”的可能性在分析美学框架下的建构》，'
     '《文艺理论研究》2023 年第 6 期作“贝里斯·高特（Berys Gaut）”，并译其书为'
     '《艺术、情感与伦理》；豆瓣该书条目作者字段并作“贝里斯·高特”（2026-11-24 查，见 %s）' % EV),
    ('Michael Ayers', '迈克尔·艾尔斯', None,
     '中文定名补证：台译本《洛克》（麥可·艾爾斯著，陳瑞麟譯，麥田出版 1999，'
     'ISBN 957708866X）作者署名“麥可·艾爾斯”，臺北市立大學圖書館 MARC 著录 '
     'Ayers, Michael；简体作“迈克尔·艾尔斯”（2026-11-24 查，见 %s）' % EV),
    ('Neil Levy', '尼尔·利维', None,
     '中文定名补证：中译本《坏信念：为什么人们会相信那些不合理的“谬论”》'
     '（傅婧瑛译，人民邮电出版社 2025-11，ISBN 9787115684516）作者署名“尼尔·利维”'
     '（2026-11-24 查，见 %s；出版方标“[英]”与实际籍属不合，籍属列不动）' % EV),
    ('Frances Kamm', '弗朗西丝·卡姆', '弗朗西丝·默纳·卡姆',
     '中文定名补证：中译本《电车难题之谜》（常云云译，北京大学出版社 2019-02，'
     'ISBN 9787301301364）作者署名“弗朗西丝·默纳·卡姆”（2026-11-24 查，见 %s）；'
     '2026-11-24 合并（同人异键）：删去“Kamm, F.M.／F.M.卡姆”重复行，其键与译形入别名列、'
     '来源 slug ethics-deontological 并入首现列' % EV),
]

DEL_KEYS = ['Kamm, F.M.']

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0]:
            idx.setdefault(norm_key_quote(cells[0]), i)

# 先取出待删行的首现 slug
del_slug = ''
del_idx = set()
for k in DEL_KEYS:
    i = idx.get(norm_key_quote(k))
    if i is None:
        print('未找到待删行', k)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    del_slug = cells[5]
    del_idx.add(i)
    print('删行', k, '| 首现', cells[5])

n = 0
for key, zh, alias, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None or i in del_idx:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    if zh:
        cells[2] = zh
    if alias:
        cells[1] = alias if cells[1] in ('—', '') else cells[1] + ' / ' + alias
    if key == 'Frances Kamm' and del_slug:
        cells[5] = cells[5] + '；' + del_slug
    if note not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    print('改行', key, '|', cells[2], '| alias:', cells[1][:30], '| 首现:', cells[5])
    n += 1

lines = [l for i, l in enumerate(lines) if i not in del_idx]
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d del=%d' % (n, len(del_idx)))
