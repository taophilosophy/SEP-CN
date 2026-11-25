# -*- coding: utf-8 -*-
"""按词条生成人名表（重译就绪用，2026-11-25）。

人名表键是「姓, 名」倒序，直接匹配英文正文会大面积漏。本脚本先把键还原成
「名 姓」形（保留 van／von／de 等粒子），并收别名列的 ASCII 形，再用
Aho–Corasick 扫 `yuanwen/*/*.md`，输出「词条 × 人名 × 次数」。

只用「名 姓」双词以上形，避免单姓撞普通词（Mill、Price 一类）。

用法：
  python -I specs/058-term-full-reextraction/bin/entry_person_index.py [--min 2]
产物：
  specs/058-term-full-reextraction/results/entry-person-index-2026-11-25.tsv.gz
"""
import argparse
import glob
import gzip
import io
import os
import re
import sys
import unicodedata
from collections import deque

sys.stdout.reconfigure(encoding='utf-8')


def fold(ch):
    # 长度保持的变音符折叠：Nāgārjuna→nagarjuna，索引仍与原文对齐
    base = unicodedata.normalize('NFKD', ch)[0]
    return base.lower()


def norm(s):
    s = ''.join(fold(ch) for ch in s)
    s = s.replace('’', "'").replace('–', '-').replace('—', '-')
    return s.replace('-', ' ')


COMMON_UPPER = set(
    'David Young White Brown Black Green Hill Wood Stone Field House King '
    'Knight Pope Bishop Abbott Banks Rice Fish Bird Fox Wolf Winter Summer '
    'May March April June Hope Faith Grace Rose Price Miles Short Long Small '
    'Little Strong Wise Good Best Sharp Smart Sweet Rich Poor West East North '
    'South Love Joy Peace Wisdom Truth Being Nature Reason Mark Luke John '
    'Paul Peter James Thomas George Henry '
    'Charles William Edward Richard Robert Michael Martin'.split())


def variants(key, alias):
    out = []
    k = key.split(' / ')[0].strip()
    if ',' in k:
        last, first = [x.strip() for x in k.split(',', 1)]
        if first and last:
            out.append(first + ' ' + last)
        if last and len(last) >= 4 and last.split()[0] not in COMMON_UPPER:
            # 裸姓（Kant、Hegel 一类，正文里最常见的指称形）
            out.append(last)
    else:
        out.append(k)
    for a in (alias or '').split('/'):
        a = a.strip()
        if a and a != '—' and not any(ord(ch) > 127 for ch in a):
            out.append(a)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min', type=int, default=2)
    ap.add_argument('--out', default='specs/058-term-full-reextraction/results/'
                                    'entry-person-index-2026-11-25.tsv.gz')
    a = ap.parse_args()

    table = {}
    for l in io.open('ren-ming-biao.md', encoding='utf-8'):
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 8:
            continue
        key, alias, zh = c[0], c[1], c[2]
        if zh in ('—', ''):
            continue
        for v in variants(key, alias):
            if len(v) < 4:
                continue
            if not re.search(r'[A-Za-z]', v):
                continue
            table.setdefault(norm(v), (key, zh))
    pats = list(table)
    print('人名匹配形', len(pats))

    goto, fail, out = [{}], [0], [[]]
    for p in pats:
        node = 0
        for ch in p:
            nxt = goto[node].get(ch)
            if nxt is None:
                nxt = len(goto)
                goto[node][ch] = nxt
                goto.append({})
                fail.append(0)
                out.append([])
            node = nxt
        out[node].append(p)
    q = deque(goto[0].values())
    while q:
        r = q.popleft()
        for ch, n in goto[r].items():
            q.append(n)
            f = fail[r]
            while f and ch not in goto[f]:
                f = fail[f]
            cand = goto[f].get(ch, 0)
            fail[n] = cand if cand != n else 0
            out[n] = out[n] + out[fail[n]]

    files = sorted(glob.glob('yuanwen/*/*.md'))
    print('词条文件', len(files))
    rows = []
    for fi, path in enumerate(files):
        raw = io.open(path, encoding='utf-8', errors='ignore').read()
        text = norm(raw)
        counts = {}
        node = 0
        for i, ch in enumerate(text):
            while node and ch not in goto[node]:
                node = fail[node]
            node = goto[node].get(ch, 0)
            for p in out[node]:
                b = i - len(p) + 1
                before = text[b - 1] if b > 0 else ' '
                after = text[i + 1] if i + 1 < len(text) else ' '
                if before.isalnum() or after.isalnum():
                    continue
                if not raw[b].isupper():
                    continue
                counts[p] = counts.get(p, 0) + 1
        agg = {}
        for p, n in counts.items():
            if n < a.min:
                continue
            key, zh = table[p]
            k2 = (key, zh)
            agg[k2] = agg.get(k2, 0) + n
        entry = path.replace('yuanwen/', '').replace('yuanwen\\', '')
        entry = entry.replace('.md', '').replace('\\', '/')
        for (key, zh), n in sorted(agg.items(), key=lambda x: -x[1]):
            rows.append((entry, n, key, zh))
        if (fi + 1) % 600 == 0:
            print('  已扫', fi + 1)

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with gzip.open(a.out, 'wt', encoding='utf-8', newline='\n') as f:
        f.write('entry\tcount\tname_key\tzh\n')
        for e, n, k, z in rows:
            f.write('%s\t%d\t%s\t%s\n' % (e, n, k, z))
    print('输出', a.out, '｜行', len(rows),
          '｜有命中词条', len({r[0] for r in rows}))


if __name__ == '__main__':
    main()
