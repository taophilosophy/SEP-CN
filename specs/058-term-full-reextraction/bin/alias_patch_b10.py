# -*- coding: utf-8 -*-
"""人名别名补记（2026-11-24，第十批配套）：既有行补语料形别名。

这些行早已登记（多为姓键或倒序键），但 058 语料按“名＋姓”“缩写＋姓”等
形出现，别名列为“—”，导致候选池反复报缺。本补丁只动别名列与依据列，
键、译法、籍属、生卒一律不改。逐条同一性判据见 evidence TSV。
"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import person_path

EV = 'people-alias-2026-11-24-b10.tsv'
# 现有键 -> (追加别名, 同一性判据)
FIX = [
    ('Gassendi', 'Pierre Gassendi', '姓键；法国哲学家皮埃尔·伽桑狄'),
    ('Maimonides', 'Moses Maimonides', '姓键；迈蒙尼德全名摩西·迈蒙尼德'),
    ('Fichte', 'Johann Gottlieb Fichte', '姓键；J. G. 费希特'),
    ('Scanlon, T. M.', 'Thomas Scanlon', 'T. M.＝Thomas Malcolm，同一人'),
    ('F.A. Hayek', 'Friedrich Hayek', '名形异写；弗里德里希·奥古斯特·冯·哈耶克'),
    ('Mackie, J. L.', 'John Mackie', 'J. L.＝John Leslie，同一人'),
    ('Anscombe, Elizabeth', 'G. E. M. Anscombe',
     '全名 Gertrude Elizabeth Margaret Anscombe，通行缩写形'),
    ('Twain, Mark', 'Samuel Clemens', '马克·吐温本名塞缪尔·克莱门斯'),
    ('Albert the Great', 'Albertus Magnus', '同名的拉丁形与英文称号形'),
    ('Hempel, Carl G.', 'Carl Hempel', '中间名缩写省略形'),
    ('Wolff, R. P.', 'Robert Paul Wolff', 'R. P.＝Robert Paul，同一人'),
    ('Strawson, P.F.', 'Peter Strawson', 'P. F.＝Peter Frederick，同一人'),
    ('Lewis, C.I.', 'C. I. Lewis', '缩写形空格异写'),
    ('Laozi', 'Lao Dan', '老聃即老子（史记谥名），语料形“Lao Dan”'),
    ('van Norden, B.W.', 'Bryan Van Norden', '名形全写；汉名万百安'),
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
        print('已含别名', key, alias)
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
