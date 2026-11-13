# -*- coding: utf-8 -*-
r"""019 上游公式联网比对抓取器：对含公式的 en/ 词条抓当前上游页快照。

礼仪（rules/05）：复用 tools/fetch.get（项目 UA、串行 Pacer ≥5s、指数退避
重试、4xx 返回码显式登记、FetchError 显式化）；逐条 JSONL 留痕
results/upstream-fetch.jsonl；断点续跑以日志为准（ok/4xx 均不重抓）。
快照落 state/mathval/upstream/（gitignore 不入库）。

用法: python -I specs/019-math-formula-audit/bin/upstream_fetch.py
"""
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, REPO)

from tools import fetch as tf  # noqa: E402

CENSUS = os.path.join(REPO, 'specs', '019-math-formula-audit', 'results',
                      'en-census.json')
DEST = os.path.join(REPO, 'state', 'mathval', 'upstream')
LOG = os.path.join(REPO, 'specs', '019-math-formula-audit', 'results',
                   'upstream-fetch.jsonl')


def main():
    with open(CENSUS, encoding='utf-8') as fh:
        data = json.load(fh)
    slugs = sorted({rel.split('/')[0] for rel, v in data['per_file'].items()
                    if v.get('inline') or v.get('display')})
    os.makedirs(DEST, exist_ok=True)
    seen = {}
    if os.path.exists(LOG):
        with open(LOG, encoding='utf-8') as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                seen[rec.get('slug')] = rec.get('status')
    pacer = tf.Pacer(5.0)
    n_new = n_ok = n_4xx = n_err = 0
    with open(LOG, 'a', encoding='utf-8') as logf:
        for slug in slugs:
            prev = seen.get(slug)
            dest = os.path.join(DEST, slug + '.html')
            if prev == 'ok' and os.path.exists(dest) and os.path.getsize(dest) > 1000:
                continue
            if prev in ('http4xx', 'error'):
                continue
            url = f'https://plato.stanford.edu/entries/{slug}/'
            rec = {'slug': slug, 'url': url}
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
          'total slugs:', len(slugs))


if __name__ == '__main__':
    main()
