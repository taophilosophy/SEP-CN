# -*- coding: utf-8 -*-
"""同日重复登记合并（2026-11-23）：新行删去，旧行键追加合写别名并留痕。"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, term_path

PAIRS = [
    ('act utilitarianism', 'act-utilitarianism'),
    ('storehouse consciousness', 'ālayavijñāna'),
    ("Bertrand's Paradox", 'Bertrand paradox'),
    ('Black Skin, White Masks', 'Black Skin White Masks'),
    ('Book of Lord Shang', 'Shangjunshu'),
    ('Defender of Peace', 'Defensor Pacis'),
    ('Discourse on the Method', 'Discourse on Method'),
    ('discourse representation structures', 'discourse representation structure (DRS)'),
    ('effortless action', 'wuwei'),
    ('received opinions', 'endoxa'),
    ('four beginnings', 'si duan'),
    ('free play', 'free play (of cognitive faculties)'),
    ('Guide for the Perplexed', 'Guide of the Perplexed'),
    ('inductive principle', 'induction principle'),
    ("Liar's paradox", 'Liar Paradox'),
    ('Lives of the Philosophers', 'Lives of Eminent Philosophers'),
    ('living forces', 'vis viva'),
    ('Political Treatise', 'Tractatus Politicus'),
    ('somatic markers', 'somatic marker'),
    ('wu xing', 'wuxing'),
]

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')


def find(key):
    k = norm_key_quote(key)
    for i, l in enumerate(lines):
        if not l.startswith('| '):
            continue
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) != 6:
            continue
        parts = [norm_key_quote(x.strip()) for x in cells[0].split('/')]
        if k in parts:
            return i, cells
    return None, None


removed = 0
merged = 0
for new_en, old_en in PAIRS:
    i_new, c_new = find(new_en)
    i_old, c_old = find(old_en)
    if i_new is None or i_old is None:
        print('缺行 %-42s new=%s old=%s' % (new_en, i_new, i_old))
        continue
    if i_new == i_old:
        print('同行为一体，跳过', new_en)
        continue
    old_key = c_old[0]
    if norm_key_quote(new_en) in [norm_key_quote(x.strip()) for x in old_key.split('/')]:
        print('已含别名，跳过', new_en)
        continue
    c_old[0] = old_key + ' / ' + new_en
    note = '2026-11-23 合并同日重复登记形（同概念异拼写：%s）' % new_en
    if note not in c_old[4]:
        c_old[4] = c_old[4].rstrip('；') + '；' + note
    lines[i_old] = '| ' + ' | '.join(c_old) + ' |'
    del lines[i_new]
    removed += 1
    merged += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('merged=%d removed=%d' % (merged, removed))
