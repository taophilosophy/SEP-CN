# -*- coding: utf-8 -*-
"""按词条生成术语表（重译就绪用，2026-11-25）。

全库置空（ADR-0081）后，重译 rv-01 需要「该词条原文里出现过哪些已登记术语」。
本脚本只读 `yuanwen/<letter>/<slug>.md`（英文侧，未受置空影响）与登记册，
用 Aho–Corasick 一次扫描全部词条，输出按词条分组的术语清单。

匹配归一：小写、连字符→空格、空白折叠；命中后再验词边界，避免 art∈part。
只收 ASCII 键（长度≥4），非拉丁键（IAST／阿拉伯／梵文）不参与。

用法：
  python -I specs/058-term-full-reextraction/bin/entry_glossary.py [--min 3] [--cap 250]
产物：
  specs/058-term-full-reextraction/results/entry-glossary-2026-11-25.tsv
"""
import argparse
import glob
import io
import os
import re
import sys
from collections import deque

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')


def norm(s):
    s = s.lower().replace('’', "'").replace('–', '-').replace('—', '-')
    s = s.replace('-', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def load_registry():
    out = {}
    for l in io.open('shu-yu-biao.md', encoding='utf-8'):
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 6:
            continue
        key, zh = c[0], c[2]
        if zh in ('—', ''):
            continue
        for p in key.split('/'):
            p = p.strip()
            if len(p) < 4 or any(ord(ch) > 127 for ch in p):
                continue
            k = norm(p)
            if len(k) < 4:
                continue
            out.setdefault(k, (p, zh))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min', type=int, default=3, help='词条内最少出现次数')
    ap.add_argument('--cap', type=int, default=250, help='每词条最多输出条数')
    ap.add_argument('--out', default='specs/058-term-full-reextraction/results/'
                                    'entry-glossary-2026-11-25.tsv')
    a = ap.parse_args()

    reg = load_registry()
    pats = list(reg)
    print('登记键（可匹配）', len(pats))

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
                counts[p] = counts.get(p, 0) + 1
        items = [(n, p) for p, n in counts.items() if n >= a.min]
        items.sort(reverse=True)
        entry = path.replace('yuanwen/', '').replace('yuanwen\\', '')
        entry = entry.replace('.md', '').replace('\\', '/')
        for n, p in items[:a.cap]:
            en, zh = reg[p]
            rows.append((entry, n, en, zh))
        if (fi + 1) % 400 == 0:
            print('  已扫', fi + 1)

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with io.open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('entry\tcount\ten\tzh\n')
        for e, n, en, zh in rows:
            f.write('%s\t%d\t%s\t%s\n' % (e, n, en, zh))
    entries = len({r[0] for r in rows})
    print('输出', a.out, '｜行', len(rows), '｜有术语的词条', entries)


if __name__ == '__main__':
    main()
