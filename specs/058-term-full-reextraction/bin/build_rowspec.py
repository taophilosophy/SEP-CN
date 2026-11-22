# -*- coding: utf-8 -*-
"""specs/058 补登批次：把审定库凭证转成 term_flow rowspec。

用法:
  python specs/058-term-full-reextraction/bin/build_rowspec.py \
      --queue specs/058-term-full-reextraction/results/register-queue-terms.json \
      --out specs/058-term-full-reextraction/results/rowspec-batch1.json

只取审定库命中且学科属哲学的条目；未命中的列 misses 清单，不自动登记。
"""
import argparse
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.cnki_query import safe_key  # noqa: E402
from tools.register_lib import norm_key_quote  # noqa: E402

QD = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                  'queries', 'termonline-all')
PHIL = ('哲学', '自然辩证法', '逻辑', '伦理', '美学', '宗教', '心理', '语言',
        '科学哲学', '技术哲学', '认知科学', '马克思主义', '中国哲学',
        '外国哲学', '思维', '方法论', '辩证法')


def pick(term, hits):
    """只取英文形完全一致的命中；同学科命中优先哲学类。宁缺勿错义。"""
    exact = [h for h in hits if (h.get('en') or '').strip().casefold()
             == term.strip().casefold()]
    if not exact:
        return None
    phil = [h for h in exact if any(p in ((h.get('subjectFullName') or '')
                                          + (h.get('subjectName') or '')
                                          + (h.get('source') or '')) for p in PHIL)]
    return (phil or exact)[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--queue', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--misses', default='')
    args = ap.parse_args()
    queue = json.load(open(args.queue, encoding='utf-8'))
    rows, misses = [], []
    review = ['en\tzh\tsource\tsubject\tyear\tdefinition']
    for item in queue:
        term = item['en']
        fn = safe_key(norm_key_quote(term)) + '.json'
        path = os.path.join(QD, fn)
        if not os.path.exists(path):
            misses.append((term, '无凭证'))
            continue
        doc = json.load(open(path, encoding='utf-8'))
        if doc.get('status') != 'ok' or not doc.get('hits'):
            misses.append((term, doc.get('status', 'empty')))
            continue
        h = pick(term, doc['hits'])
        if not h or not h.get('cn'):
            misses.append((term, '无可用命中'))
            continue
        src = h.get('source') or ''
        subj = h.get('subjectFullName') or h.get('subjectName') or ''
        year = h.get('publishYear') or ''
        num = h.get('wordNumber') or ''
        basis = '审定名词库（%s%s%s%s；凭证 2026-11-22）' % (
            src, '·' + subj if subj else '',
            '，' + year if year else '', '，' + num if num else '')
        rows.append({'en': term, 'zh': h['cn'], 'table': 'term',
                     'first_seen': 'specs/058 全库提取',
                     'basis': basis, 'date': '2026-11-22'})
        review.append('%s\t%s\t%s\t%s\t%s\t%s' % (
            term, h['cn'], src, subj, year,
            (h.get('definition') or '').replace('\t', ' ')[:80]))
    out = {'batch': '058-batch1', 'date': '2026-11-22',
           'evidence': 'specs/008-terminology-campaign/results/queries/termonline-all/',
           'rows': rows}
    json.dump(out, open(args.out, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    with open(args.out + '.review.tsv', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(review) + '\n')
    if args.misses:
        with open(args.misses, 'w', encoding='utf-8', newline='\n') as f:
            for t, why in misses:
                f.write('%s\t%s\n' % (t, why))
    print('rows=%d misses=%d' % (len(rows), len(misses)))


if __name__ == '__main__':
    main()
