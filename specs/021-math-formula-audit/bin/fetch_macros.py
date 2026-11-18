# -*- coding: utf-8 -*-
r"""019 宏表收割：抓全部含公式词条的 local.js（SEP 每词条宏定义的唯一事实源）。

SEP 页头 <script src="local.js"> 内的 window.MathJax.TeX.Macros 定义该词条
专属宏（如实证：lamp:"\\mathbin{\\&}"、at:"\\textrm{ at }"、rO:"\\mathrm{O}"）。
公式正文里的 \lamp \rO \at \bA \osim 等未定义于 MathJax 标准包，缺此表即
红字。本脚本为 019 校验与修复提供权威宏字典。

纪律同 upstream_fetch.py（tools/fetch.get、4xx 显式登记、
断点续跑）。落 state/mathval/macros/<slug>.js（gitignore），日志
results/macro-fetch.jsonl。

用法: python -I specs/021-math-formula-audit/bin/fetch_macros.py
"""
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, REPO)
from tools import fetch as tf  # noqa: E402

RESULTS = os.path.join(REPO, 'specs', '021-math-formula-audit', 'results')
DEST = os.path.join(REPO, 'state', 'mathval', 'macros')
LOG = os.path.join(RESULTS, 'macro-fetch.jsonl')


def main():
    slugs = set()
    with open(os.path.join(RESULTS, 'en-formulas.jsonl'), encoding='utf-8') as fh:
        for line in fh:
            slugs.add(json.loads(line)['f'].split('/')[0])
    # 译文侧词条亦须覆盖（其英文源同名）
    with open(os.path.join(RESULTS, 'render-zh.jsonl'), encoding='utf-8') as fh:
        for line in fh:
            slugs.add(os.path.basename(json.loads(line)['f']).split('.')[0])
    slugs = sorted(slugs)
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
    n_new = n_ok = n_4xx = n_err = 0
    with open(LOG, 'a', encoding='utf-8') as logf:
        for slug in slugs:
            if seen.get(slug) in ('ok', 'http4xx', 'error'):
                continue
            url = f'https://plato.stanford.edu/entries/{slug}/local.js'
            dest = os.path.join(DEST, slug + '.js')
            rec = {'slug': slug, 'url': url}
            try:
                status, data = tf.get(url, dest=dest)
                if status == 200:
                    rec['status'] = 'ok'
                    rec['bytes'] = len(data or b'')
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
                rec['code'] = getattr(exc, 'status', None)
                n_err += 1
            logf.write(json.dumps(rec, ensure_ascii=False) + '\n')
            logf.flush()
            n_new += 1
            if n_new % 50 == 0:
                print(f'{n_new} attempted (ok={n_ok} 4xx={n_4xx} err={n_err})',
                      flush=True)
    print('new attempts:', n_new, f'(ok={n_ok} 4xx={n_4xx} err={n_err})',
          'slugs:', len(slugs))


if __name__ == '__main__':
    main()
