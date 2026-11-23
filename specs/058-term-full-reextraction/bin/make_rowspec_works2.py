# -*- coding: utf-8 -*-
"""著作名 rowspec：包含式查重 + 权威译本依据（可传 --tsv/--out/--batch）。"""
import argparse
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.register_lib import norm_key_quote, parse_registry_full, term_path  # noqa: E402

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
keys = {}
for r in parse_registry_full(term_path())[0]:
    for p in r[0].split('/'):
        keys.setdefault(norm_key_quote(p.strip()), r[2])


def dupe(k):
    """精确同名，或与已登记「书名行」（译法以《 开头）构成包含关系时判重。

    概念行（译法非书名）不计包含式：'natural history' 是概念，
    不挡 'Universal Natural History'（康德著作）。连字符内不切词：
    'Political Treatise' 不撞 'Theological-Political Treatise'。
    """
    for rk, zh in keys.items():
        if rk == k:
            return rk
        if not zh.startswith('《'):
            continue
        if re.search(r'(?<![a-z-])' + re.escape(k) + r'(?![a-z])', rk) \
                and len(rk) >= len(k) * 0.8:
            return rk
        if re.search(r'(?<![a-z-])' + re.escape(rk) + r'(?![a-z])', k) \
                and len(k) - len(rk) <= 15 and len(rk.split()) >= 2:
            return rk
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tsv', default='curated-works2.tsv')
    ap.add_argument('--out', default='rowspec-batch4-works.json')
    ap.add_argument('--batch', default='058-batch4-works')
    ap.add_argument('--scope', default='著作名批次（术语在线无对口命中，依据权威译本）')
    ap.add_argument('--date', default='2026-11-22')
    args = ap.parse_args()
    rows, skipped = [], []
    for line in open(os.path.join(RES, args.tsv), encoding='utf-8'):
        if not line.strip():
            continue
        en, rest = line.rstrip('\n').split('\t')
        zh, note = rest.split('|', 1)
        hit = dupe(en.casefold())
        if hit:
            skipped.append('%s（已登记：%s）' % (en, hit))
            continue
        rows.append({'en': en, 'zh': zh, 'table': 'term',
                     'first_seen': '语料回收（specs/058 全库提取）',
                     'basis': ('权威译本（%s；审定库无对口条目，%s）；'
                               '凭证 %s' % (note, args.date, args.date)),
                     'date': args.date})
    json.dump({'batch': args.batch, 'date': args.date, 'scope': args.scope,
               'rows': rows},
              open(os.path.join(RES, args.out), 'w',
                   encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    print('rows=%d skipped=%d' % (len(rows), len(skipped)))
    for s in skipped:
        print('  skip', s)


if __name__ == '__main__':
    main()
