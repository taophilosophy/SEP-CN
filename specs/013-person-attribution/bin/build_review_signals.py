# -*- coding: utf-8 -*-
"""为 review 候选中“缺年份或缺职业”的 158 条取身份旁证（2026-11-26）。

对每条候选：取键的姓氏（"Last, First" 取 Last；单名用全名），在本条首现的
`en/<slug>/index.html` 与 `notes.html` 里找出现处，截 130 字上下文。旁证只用于判“这个
姓氏是否在该条目里被引证”，不据此填生卒。

输出 script/tmp/review-signals.tsv：键 候选 生卒 职业 GND 首现 命中 上下文
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
SRC = 'specs/013-person-attribution/results/gnd-review-short-2026-11-26.tsv'
OUT = 'script/tmp/review-signals.tsv'

first = {}
for l in io.open('ren-ming-biao.md', encoding='utf-8', newline=''):
    if l.startswith('|'):
        c = [x.strip() for x in l.split('|')]
        if len(c) >= 9 and c[1] and c[1] != '键':
            first[c[1]] = c[6]


def surname(key):
    if ',' in key:
        return key.split(',')[0].strip()
    return key.strip()


def search(slug, needle):
    for name in ('index.html', 'notes.html'):
        p = os.path.join('en', slug, name)
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        txt = re.sub(r'<[^>]+>', ' ', txt)
        txt = re.sub(r'&[a-z]+;|&#\d+;', ' ', txt)
        txt = re.sub(r'\s+', ' ', txt)
        m = re.search(re.escape(needle), txt, re.I)
        if m:
            lo = max(0, m.start() - 70)
            return '%s: %s' % (name, txt[lo:m.start() + 90].strip())
    return ''


def main():
    rows = []
    for l in io.open(SRC, encoding='utf-8'):
        x = l.rstrip('\n').split('\t')
        if len(x) < 7 or x[0] == '键' or x[1] != 'review':
            continue
        key, cand, years, pob, occ, gnd = x[0], x[2], x[3], x[4], x[5], x[6]
        if years and occ:
            continue          # 102 条已判
        slug = first.get(key, '')
        sn = surname(key)
        ctx = search(slug, sn) if slug and sn and len(sn) >= 4 else ''
        rows.append((key, cand, years, pob, occ, gnd, slug, 'Y' if ctx else 'N', ctx))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('键\t候选名\t生卒\t出生地\t职业\tGND\t首现\t命中\t上下文\n')
        for r in sorted(rows, key=lambda r: (r[7] != 'Y', r[6], r[0])):
            f.write('\t'.join(r) + '\n')
    print('信号表 %d 行，命中 %d' % (len(rows), sum(1 for r in rows if r[7] == 'Y')))


if __name__ == '__main__':
    main()
