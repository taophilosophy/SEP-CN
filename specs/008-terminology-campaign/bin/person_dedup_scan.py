# -*- coding: utf-8 -*-
"""人名表同人重复聚类（只读）：token 相等 / 子集同姓 / 同译名＋同姓＋given 近似。"""
import collections
import difflib
import io
import re
import unicodedata

PART = {'of', 'de', 'van', 'von', 'der', 'al', 'ibn', 'bin', 'du', 'le', 'la',
        'di', 'da', 'del', 'den', 'the', 'st'}


def fold(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    for ch in 'ʿʾʻʼ':
        s = s.replace(ch, '')
    return re.sub(r'\s+', ' ', s).strip().casefold()


def toks(k):
    return frozenset(t for t in fold(k).replace(',', ' ').split()
                     if t and t not in PART)


rows = []
for n, line in enumerate(io.open('ren-ming-biao.md', encoding='utf-8'), 1):
    if not line.startswith('|'):
        continue
    c = [x.strip() for x in line.strip().strip('|').split('|')]
    if len(c) < 3 or not c[0] or set(c[0]) <= set(':-: '):
        continue
    rows.append((n, c))

TK = [toks(c[0]) for _, c in rows]
ZH = [re.split(r'（|\(|；|;', c[2])[0].strip() for _, c in rows]

par = list(range(len(rows)))


def find(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


def uni(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        par[ra] = rb


for i in range(len(rows)):
    for j in range(i + 1, len(rows)):
        a, b = TK[i], TK[j]
        if not a or not b:
            continue
        if a == b:
            uni(i, j)
            continue
        if ZH[i] != ZH[j]:
            continue
        big, small = (a, b) if len(a) >= len(b) else (b, a)
        sbig, ssmall = sorted(big)[-1], sorted(small)[-1]
        if sbig != ssmall:
            continue
        gbig, gsmall = big - {sbig}, small - {ssmall}
        if gbig & gsmall:
            uni(i, j)
            continue
        if gbig and gsmall:
            x, y = sorted(gbig)[0], sorted(gsmall)[0]
            if difflib.SequenceMatcher(None, x, y).ratio() > 0.8:
                uni(i, j)

groups = collections.defaultdict(list)
for i in range(len(rows)):
    groups[find(i)].append(i)
dups = [v for v in groups.values() if len(v) > 1]
print('可合并组:', len(dups), '涉及行:', sum(len(v) for v in dups),
      '可删冗余行:', sum(len(v) - 1 for v in dups))
for v in sorted(dups, key=lambda x: -len(x))[:12]:
    print('  ', ' | '.join('%s(%d)' % (rows[i][1][0], rows[i][0]) for i in v)[:160])
