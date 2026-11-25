# -*- coding: utf-8 -*-
"""登记形 vs 文本形偏离扫描（2026-11-25）。

用途：登记册译法列常带「（亦作“X”）」异形。若译文里用的是异形而非主形，
就出现 D1 偏离（文本未采登记形）。本脚本把异形逐一回中文语料计数，
输出「异形在用而主形也用／不用」的清单，供逐条回源研判（**不做机械替换**）。

用法：
  python -I specs/058-term-full-reextraction/bin/audit_zh_variants.py [--min 3]
产物：
  specs/058-term-full-reextraction/results/zh-variant-deviation-2026-11-25.tsv
"""
import argparse
import glob
import io
import os
import re
import sys
from collections import Counter

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

VARIANT_RE = re.compile(r'亦作\s*[“「]([^”」]+)[”」]')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min', type=int, default=3, help='异形命中的最小次数')
    ap.add_argument('--out', default='specs/058-term-full-reextraction/results/'
                                    'zh-variant-deviation-2026-11-25.tsv')
    a = ap.parse_args()

    rows = []
    for l in io.open('shu-yu-biao.md', encoding='utf-8'):
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 6:
            continue
        key, zh = c[0], c[2]
        if zh in ('—', ''):
            continue
        main = re.split(r'[（(]', zh)[0].strip().strip('《》')
        if not main:
            continue
        variants = [v.strip().strip('《》') for v in VARIANT_RE.findall(zh)]
        variants = [v for v in variants if v and v != main and len(v) >= 2]
        if not variants:
            continue
        rows.append((key, main, sorted(set(variants))))

    files = {}
    texts = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if not os.path.isdir(letter):
            continue
        for fn in sorted(os.listdir(letter)):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(letter, fn)
            texts[p] = io.open(p, encoding='utf-8', errors='ignore').read()

    out = []
    for key, main, variants in rows:
        m = sum(t.count(main) for t in texts.values())
        for v in variants:
            n = sum(t.count(v) for t in texts.values())
            if n < a.min:
                continue
            where = [(p, t.count(v)) for p, t in texts.items() if v in t]
            where.sort(key=lambda x: -x[1])
            out.append((n, m, key, main, v, ', '.join('%s(%d)' % (p, k) for p, k in where[:3])))
    out.sort(reverse=True)

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with io.open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('variant_count\tmain_count\tkey\tmain_zh\tvariant\ttop_files\n')
        for n, m, key, main, v, where in out:
            f.write('%d\t%d\t%s\t%s\t%s\t%s\n' % (n, m, key, main, v, where))
    print('登记行带异形', len(rows), '｜异形在用', len(out), '｜输出', a.out)
    print('%-24s %-10s %-10s %s' % ('key', 'main(n)', 'variant(n)', 'variant'))
    for n, m, key, main, v, where in out[:25]:
        print('%-24s %-10s %-10s %s' % (key[:24], '%s(%d)' % (main, m), '%s(%d)' % (v, n), v))


if __name__ == '__main__':
    main()
