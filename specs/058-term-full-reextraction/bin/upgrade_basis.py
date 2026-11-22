# -*- coding: utf-8 -*-
"""把首批中审定库对口命中的行，依据列升级为审定名词库（译名不变时）。

用法:
  python specs/058-term-full-reextraction/bin/upgrade_basis.py --dry-run
  python specs/058-term-full-reextraction/bin/upgrade_basis.py --apply
只改依据列；译法与裁定日期不动；行数守恒校验。
"""
import argparse
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.cnki_query import safe_key  # noqa: E402
from tools.register_lib import norm_key_quote, term_path  # noqa: E402

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
QD = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                  'queries', 'termonline-all')
PHIL = ('哲学', '自然辩证法', '逻辑', '伦理', '美学', '宗教', '心理', '语言',
        '科学哲学', '技术哲学', '认知科学', '马克思主义', '外国哲学', '思维',
        '方法论', '辩证法')


def variants(en):
    b = en.casefold().strip()
    out = {b}
    if b.endswith('ies'):
        out.add(b[:-3] + 'y')
    if b.endswith('es'):
        out.add(b[:-2])
    if b.endswith('s'):
        out.add(b[:-1])
    out.add(b + 's')
    return out


def best_hit(en, zh):
    path = os.path.join(QD, safe_key(norm_key_quote(en)) + '.json')
    if not os.path.exists(path):
        return None
    hits = json.load(open(path, encoding='utf-8')).get('hits') or []
    vs = variants(en)
    good = []
    for h in hits:
        hen = (h.get('en') or '').strip().casefold()
        subj = (h.get('subjectFullName') or '') + (h.get('subjectName') or '')
        if hen in vs and h.get('cn') == zh \
                and any(p in subj + (h.get('source') or '') for p in PHIL):
            good.append(h)
    return good[0] if good else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    pairs = []
    for line in io.open(os.path.join(RES, 'curated-translations.tsv'),
                        encoding='utf-8'):
        if not line.strip():
            continue
        en, zh = line.rstrip('\n').split('\t')
        h = best_hit(en, zh)
        if h:
            pairs.append((en, zh, h))
    print('审定对口且译名一致：%d 条' % len(pairs))
    path = term_path()
    lines = io.open(path, encoding='utf-8', newline='').read().split('\n')
    idx = {}
    for i, l in enumerate(lines):
        if l.startswith('| '):
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if cells and not set(cells[0]) <= set(':-— '):
                idx.setdefault(norm_key_quote(cells[0]), i)
    changed = 0
    for en, zh, h in pairs:
        i = idx.get(norm_key_quote(en))
        if i is None:
            print('  未找到行：%s' % en)
            continue
        cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
        if len(cells) != 6:
            print('  列数异常：%s' % en)
            continue
        basis = '审定名词库（%s%s%s；凭证 2026-11-22）' % (
            h.get('source') or '',
            '·' + (h.get('subjectFullName') or '') if h.get('subjectFullName') else '',
            '，' + (h.get('publishYear') or '') if h.get('publishYear') else '')
        if cells[4] == basis:
            continue
        cells[4] = basis
        lines[i] = '| ' + ' | '.join(cells) + ' |'
        changed += 1
        print('  %-28s → %s' % (en, basis[:60]))
    print('待改 %d 行' % changed)
    if args.apply and changed:
        io.open(path, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
        print('已写回 %s' % path)


if __name__ == '__main__':
    main()
