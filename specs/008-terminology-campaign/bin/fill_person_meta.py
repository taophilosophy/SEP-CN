# -*- coding: utf-8 -*-
"""补齐并网新增人名行的籍属/生卒（2026-11-13，ADR-0030/0031 口径）。"""
import io
import re

PATH = 'ren-ming-biao.md'
INFO = {
    'Abd al-Latif': ('阿拔斯王朝（巴格达）／医学、哲学与史学', '1162–1231'),
    'Albert Camus': ('法国（阿尔及利亚生）', '1913–1960'),
    'Allan Ramsay': ('苏格兰', '1686–1758'),
    'Callicles': ('非历史人物（柏拉图《高尔吉亚》对话人物）', '不适用'),
    'Charles Leslie Stevenson': ('美国', '1908–1979'),
    'Donald Cary Williams': ('美国', '1899–1983'),
    'Hermeias': ('埃及（亚历山大里亚）／新柏拉图主义哲学家', 'c. 410–c. 450'),
    'Hugh Blair': ('苏格兰', '1718–1800'),
    'James Dunbar': ('苏格兰', 'c. 1742–1798'),
    'Jean Baudrillard': ('法国', '1929–2007'),
    'John Cook Wilson': ('英国', '1849–1915'),
    'Margarete Susman': ('德国', '1872–1966'),
    'Nicolaus Taurellus': ('德国', '1547–1606'),
    'Sophie de Grouchy': ('法国', '1764–1822'),
    'Syrianus': ('希腊（亚历山大里亚生，雅典卒）／新柏拉图主义', 'd. c. 437'),
    'Thomas of Erfurt': ('德国（埃尔福特）／语法学家与逻辑学家', 'fl. c. 1300'),
    'William of Champeaux': ('法国', 'c. 1070–1122'),
}

lines = io.open(PATH, encoding='utf-8', newline='').read().split('\n')
hit = 0
for i, line in enumerate(lines):
    if not line.startswith('|'):
        continue
    cells = [c.strip() for c in line.strip('|').split('|')]
    if not cells or cells[0] not in INFO:
        continue
    guo, dates = INFO[cells[0]]
    if cells[3] not in ('—', '') and cells[4] not in ('—', ''):
        continue
    cells[3], cells[4] = guo, dates
    if '2026-11-13 补籍属' not in cells[6]:
        cells[6] = cells[6].rstrip('；;') + '；籍属/生卒据学界通行（2026-11-13 补）'
        cells[7] = '2026-11-13'
    lines[i] = '| %s |' % ' | '.join(cells)
    hit += 1
io.open(PATH, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('补写 %d 行' % hit)
