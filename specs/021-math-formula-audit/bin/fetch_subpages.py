# -*- coding: utf-8 -*-
r"""019 上游子页抓取（notes/补篇/其他非 index html，禁抽样要求全量）。

对 en/<slug>/<name>.html（name≠index.html 且含公式）抓
https://plato.stanford.edu/entries/<slug>/<name>，落
state/mathval/upstream/<slug>/<name>。礼仪同 upstream_fetch.py
（tools/fetch.get，≥5s Pacer，4xx 显式登记，断点续跑）。

用法: python -I specs/021-math-formula-audit/bin/fetch_subpages.py
"""
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, REPO)

from tools import fetch as tf  # noqa: E402

FORMULAS = os.path.join(REPO, 'specs', '021-math-formula-audit', 'results',
                        'en-formulas.jsonl')
DEST = os.path.join(REPO, 'state', 'mathval', 'upstream')
LOG = os.path.join(REPO, 'specs', '021-math-formula-audit', 'results',
                   'upstream-fetch-sub.jsonl')


def main():
    rels = set()
    with open(FORMULAS, encoding='utf-8') as fh:
        for line in fh:
            f = json.loads(line)['f']
            if not f.endswith('/index.html'):
                rels.add(f)
    seen = {}
    if os.path.exists(LOG):
        with open(LOG, encoding='utf-8') as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                seen[rec.get('rel')] = rec.get('status')
    pacer = tf.Pacer(5.0)
    n_new = n_ok = n_4xx = n_err = 0
    with open(LOG, 'a', encoding='utf-8') as logf:
        for rel in sorted(rels):
            prev = seen.get(rel)
            if prev in ('ok', 'http4xx', 'error'):
                continue
            slug, name = rel.split('/', 1)
            url = f'https://plato.stanford.edu/entries/{slug}/{name}'
            dest = os.path.join(DEST, slug, name)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            rec = {'rel': rel, 'url': url}
            try:
                status, _ = tf.get(url, dest=dest, pacer=pacer)
                if status == 200 and os.path.exists(dest) and os.path.getsize(dest) > 1000:
                    rec['status'] = 'ok'
                    rec['bytes'] = os.path.getsize(dest)
                    n_ok += 1
                elif 400 <= (status or 0) < 500:
                    rec['status'] = 'http4xx'
                    rec['code'] = status
                    n_4xx += 1
                else:
                    rec['status'] = 'error'
                    rec['code'] = status
                    n_err += 1
            except tf.FetchError as exc:
                rec['status'] = 'error'
                rec['status_code'] = getattr(exc, 'status', None)
                rec['detail'] = str(exc)[:200]
                n_err += 1
            logf.write(json.dumps(rec, ensure_ascii=False) + '\n')
            logf.flush()
            n_new += 1
            if n_new % 50 == 0:
                print(f'{n_new} attempted (ok={n_ok} 4xx={n_4xx} err={n_err})',
                      flush=True)
    print('new attempts:', n_new, f'(ok={n_ok} 4xx={n_4xx} err={n_err})',
          'total subpages:', len(rels))


if __name__ == '__main__':
    main()
