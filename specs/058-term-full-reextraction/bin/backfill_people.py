# -*- coding: utf-8 -*-
"""人名表存量缺口回填：籍属/生卒补齐 + 依据列追加 Wikidata 凭证（幂等）。

用法:
  python specs/058-term-full-reextraction/bin/backfill_people.py --dry-run
  python specs/058-term-full-reextraction/bin/backfill_people.py --apply
"""
import argparse
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.register_lib import norm_key_quote, person_path  # noqa: E402

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-23-backfill.tsv'
TARGETS = [
    ('Aëtius', '古希腊（罗马帝国时期）', '约1–2世纪（活动期）', 'Q794615'),
    ('Anderson, A.R.', '美国', '1925–1973', 'Q3268033'),
    ('Lewis, David / David Lewis', '美国', '1941–2001', 'Q384522'),
    ('Wolff, R. P.', '美国', '1933–2025', 'Q739540'),
    ('Williamson', '英国', '1955–', 'Q984380'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    path = person_path()
    lines = io.open(path, encoding='utf-8', newline='').read().split('\n')
    idx = {}
    for i, l in enumerate(lines):
        if l.startswith('| '):
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if len(cells) == 8 and cells[0] \
                    and not set(cells[0]) <= set(':-— '):
                idx.setdefault(norm_key_quote(cells[0]), i)
    ev_rows = ['en\tqid\tlabel\tdates']
    changed = 0
    for key, aff, dates, qid in TARGETS:
        i = idx.get(norm_key_quote(key))
        if i is None:
            print('  未找到行：%s' % key)
            continue
        cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
        ev = '籍属/生卒联网查证：Wikidata %s（2026-11-23 查，凭证 %s）' % (qid, EV)
        if ev in cells[6]:
            print('  已有凭证，跳过：%s' % key)
            continue
        if cells[3] in ('—', ''):
            cells[3] = aff
        if cells[4] in ('—', ''):
            cells[4] = dates
        cells[6] = cells[6].rstrip('|') + '；' + ev
        lines[i] = '| ' + ' | '.join(cells) + ' |'
        changed += 1
        print('  %-28s %s｜%s' % (key, cells[3], cells[4]))
        ev_rows.append('%s\t%s\t%s\t%s' % (key, qid, key, dates))
    print('待改 %d 行' % changed)
    if args.apply and changed:
        io.open(path, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
        with io.open(os.path.join(RES, EV), 'a', encoding='utf-8',
                     newline='\n') as f:
            for r in ev_rows[1:]:
                f.write(r + '\n')
        print('已写回 %s' % path)


if __name__ == '__main__':
    main()
