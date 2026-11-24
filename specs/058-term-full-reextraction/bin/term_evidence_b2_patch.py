# -*- coding: utf-8 -*-
"""批次 2：ALIGNED_SAME 26 行补审定凭证；Axiom of Reducibility 按审定改定主译。"""
import io, sys
sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, term_path

TSV = 'termonline-b2-2026-11-24.tsv'
p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and c[0]:
            idx.setdefault(norm_key_quote(c[0]), i)

same, diff = [], []
for row in io.open('specs/058-term-full-reextraction/results/' + TSV, encoding='utf-8'):
    parts = row.rstrip('\n').split('\t')
    if len(parts) < 5 or parts[0] == 'en':
        continue
    en, cn, st, verdict, hits = parts[:5]
    (same if verdict == 'ALIGNED_SAME' else diff if verdict == 'ALIGNED_DIFF' else []).append((en, hits))

def cite(hits):
    h = hits.split(' ; ')[0]
    try:
        cn, rest = h.split('<=', 1)
        en, source, num, year = rest.split('|')
    except ValueError:
        return None
    num = '' if num in ('None', '') else ' ' + num
    year = '' if year in ('None', '暂无年份', '') else '，' + year
    return '审定名词库（termonline-all·%s%s%s）作“%s”，与本行一致（2026-11-24 JWT 直连，凭证 %s）' % (
        source, num, year, cn, TSV)

n = 0
for en, hits in same:
    i = idx.get(norm_key_quote(en))
    if i is None:
        print('未找到', en); continue
    note = cite(hits)
    if not note:
        print('解析失败', en); continue
    c = [x.strip() for x in lines[i].strip().strip('|').split('|')]
    if note not in c[4]:
        c[4] = c[4].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(c) + ' |'
    n += 1

# 唯一改定：Axiom of Reducibility
i = idx[norm_key_quote('Axiom of Reducibility')]
c = [x.strip() for x in lines[i].strip().strip('|').split('|')]
c[2] = '还原公理（亦作“可还原性公理”）'
note = ('2026-11-24 审定改定：审定名词库（termonline-all·自然辩证法名词 03.273，2024）作“还原公理”，'
        '旧形降为亦作（凭证 %s）' % TSV)
if note not in c[4]:
    c[4] = c[4].rstrip('；') + '；' + note
lines[i] = '| ' + ' | '.join(c) + ' |'
print('改定 Axiom of Reducibility')
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('cited=%d' % n)
