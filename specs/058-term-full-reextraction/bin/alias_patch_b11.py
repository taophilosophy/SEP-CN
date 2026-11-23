# -*- coding: utf-8 -*-
"""人名别名补记（2026-11-24，第十一批配套）：语料形别名并入既有行。"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import person_path

EV = 'people-alias-2026-11-24-b11.tsv'
FIX = [
    ('Ross, W. D.', 'William David Ross', 'W. D.＝William David，同一人'),
    ('Hamilton, William / William Hamilton', 'Sir William Hamilton',
     '爵士称号形；苏格兰哲学家（1788–1856）'),
    ('King, Martin Luther', 'Martin Luther King Jr',
     'Jr 后缀形；与已登记行同一人'),
    ('Novalis', 'Friedrich von Hardenberg', '诺瓦利斯本名弗里德里希·冯·哈登贝格'),
    ('Delmedigo, Elijah', 'Elijah Del Medigo', '姓氏连写／分写异形'),
    ('Collingwood, R.G.', 'Robin George Collingwood', '名形全写'),
    ('Lotze, Hermann', 'Rudolf Hermann Lotze', '中间名补全形'),
    ('Eliot, George', 'Mary Ann Evans', '本名形（该行译法已注“本名玛丽·安·埃文斯”）'),
    ('Newton, Isaac', 'Sir Isaac Newton', '爵士称号形'),
    ('Moore, G. E.', 'George Edward Moore', '名形全写'),
    ('Butler, Joseph / Joseph Butler', 'Bishop Joseph Butler', '主教头衔形'),
]

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0]:
            idx.setdefault(cells[0], i)
ev = ['key\talias\t判据']
n = miss = 0
for key, alias, why in FIX:
    i = idx.get(key)
    if i is None:
        print('未找到行', key)
        miss += 1
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    if alias in cells[1]:
        print('已含别名', key)
        continue
    cells[1] = alias if cells[1] in ('—', '') else cells[1] + ' / ' + alias
    note = '别名“%s”为 058 语料形，与前项同一人（2026-11-24 核对，凭证 %s）；%s' % (
        alias, EV, why)
    if note not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    ev.append('%s\t%s\t%s' % (key, alias, why))
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
res = io.open('specs/058-term-full-reextraction/results/' + EV, 'w',
              encoding='utf-8', newline='\n')
res.write('\n'.join(ev) + '\n')
res.close()
print('别名补记', n, '缺行', miss)
