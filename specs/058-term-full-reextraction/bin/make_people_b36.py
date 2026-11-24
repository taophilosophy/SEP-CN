# -*- coding: utf-8 -*-
"""人名第三十六批（2026-11-24，中文源补证）：四人取汉名。

Haslanger、Mackie、Lycan、Fish；Tremain、Wasserman、Merricks、Hurka 查无留证。
"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

EV = 'people-cnweb-2026-11-24-b36.md'

FIX = [
    ('Haslanger, Sally', '萨利·哈斯兰格', '萨莉·哈斯兰格',
     '中文定名补证：王立秋译访《萨利·哈斯兰格：演化的女性主义》（Matters，2020-11-12）作'
     '“萨利·哈斯兰格（Sally Haslanger）”；FemRes 论文导读（Haslanger 2000）作“萨莉·'
     '哈斯兰格”，异形入别名（2026-11-24 查，凭证 %s）' % EV),
    ('Mackie, J. L.', '约翰·L. 麦凯', None,
     '中文定名补证：中译本《伦理学：发明对与错》（丁三东译，上海译文出版社 2007-12，'
     'ISBN 9787532743346）作者简介“约翰·L·麦凯（John L. Mackie，1917—1981），澳大利亚'
     '哲学家”（2026-11-24 查，凭证 %s）' % EV),
    ('Lycan, William G.', '威廉·莱肯', None,
     '中文定名补证：中译本《当代语言哲学导论》（陈波、冯艳译，中国人民大学出版社 2011，'
     '国外经典哲学教材译丛）著者“莱肯（Lycan, William G.）”；《华文哲学百科》〈意识〉'
     '（洪裕宏 2023）作“萊肯”，异形同源（2026-11-24 查，凭证 %s）' % EV),
    ('Stanley Fish', '斯坦利·费什', None,
     '中文定名补证：中译本《读者反应批评：理论与实践》（文楚安译，中国社会科学出版社 1998-02，'
     'ISBN 9787500421962）作者署名“（美）斯坦利·费什”；《如何遣词造句》（杨逸译，译林出版社 '
     '2020-10，ISBN 9787544783866）同（2026-11-24 查，凭证 %s）' % EV),
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
