# -*- coding: utf-8 -*-
"""汇总界面“精确匹配”核验结果并逐行比对术语表（2026-11-25）。

输入：界面核验批次 JSON（tl_ui2_b*.json，机器本地临时目录；不入库）
输出：results/ui-check-2026-11-25.tsv（key｜译法｜结论｜界面证据）
      results/ui-check-rows-2026-11-25.tsv（key｜译法｜现依据｜界面结论）

结论档：
  hit       界面“精确匹配”有同形条目且学科义与词条相合 → 审定主张复核成立
  homonym   界面有同形条目但学科义不同（如 recognition→再认） → 不作对口凭证
  other-lib 命中来自海峡两岸库或标准文件库，不是审定公布库 → 须改记库名
  miss      界面“精确匹配”明示未审定 → 审定主张不成立，依据须改
  unresolved 页面未落到稳定态 → 待复检
"""
import glob
import io
import json
import os
import sys

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

TMP = os.path.join(os.environ.get('LOCALAPPDATA', '.'), 'Temp')
TERMS = 'shu-yu-biao.md'
KEYS = 'specs/058-term-full-reextraction/results/ui-check-keys-2026-11-25.json'
OUT = 'specs/058-term-full-reextraction/results/ui-check-2026-11-25.tsv'
OUT2 = 'specs/058-term-full-reextraction/results/ui-check-rows-2026-11-25.tsv'

# 学科义与词条不合作同形处理的键（人工判定，逐条留档在 results 文档里）
HOMONYM = {
    'argumentation', 'Chancellor', 'golden rule', 'recognition', 'natural theology',
    'folk psychology', 'microworld', 'world community', 'selection function',
}
# 命中来自非审定库（来源名以“海峡两岸”“国家标准文件”开头等）
OTHER_LIB = ('海峡两岸', '国家标准')


def load_batches():
    best = {}
    for p in sorted(glob.glob(os.path.join(TMP, 'tl_ui2_b*.json'))):
        for r in json.load(io.open(p, encoding='utf-8')):
            k = r.get('key')
            try:
                n = len(r.get('cards') or [])
            except Exception:
                n = 0
            r['_n'] = n
            old = best.get(k)
            if old is None or (n, r.get('found') or 0) >= (old['_n'], old.get('found') or 0):
                best[k] = r
    return best


def load_terms():
    rows = {}
    for line in io.open(TERMS, encoding='utf-8'):
        if not line.startswith('|'):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 6 or c[0] in ('键', '') or set(c[0]) <= set('-: '):
            continue
        rows.setdefault(c[0], (c[2], c[4]))
    return rows


def verdict(r):
    cards = r.get('cards') or []
    if cards:
        srcs = [c.get('src', '') for c in cards]
        if all(s.startswith(OTHER_LIB) for s in srcs):
            return 'other-lib'
        if r.get('key') in HOMONYM:
            return 'homonym'
        return 'hit'
    if r.get('absent'):
        return 'miss'
    if r.get('found') == 0:
        return 'miss'
    return 'unresolved'


def main():
    best = load_batches()
    terms = load_terms()
    keys = json.load(io.open(KEYS, encoding='utf-8'))
    out, out2 = [], []
    for k in keys:
        r = best.get(k)
        if not r:
            out.append((k, '', 'unresolved', 'no-ui-record'))
            continue
        v = verdict(r)
        cards = r.get('cards') or []
        ev = '；'.join('%s｜%s｜%s' % (c.get('cn', ''), c.get('sub', ''), c.get('src', '')) for c in cards)
        if not ev:
            ev = '精确匹配：未审定' if v == 'miss' else ('found=%s' % r.get('found'))
        zh, basis = terms.get(k, ('', ''))
        out.append((k, zh, v, ev))
        out2.append((k, zh, basis, v))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('key\tzh\tverdict\tevidence\n')
        for row in out:
            f.write('\t'.join(row) + '\n')
    with io.open(OUT2, 'w', encoding='utf-8', newline='\n') as f:
        f.write('key\tzh\tbasis\tverdict\n')
        for row in out2:
            f.write('\t'.join(row) + '\n')
    from collections import Counter
    c = Counter(x[2] for x in out)
    print('61 行结论：', dict(c))
    print('→', OUT, '|', OUT2)


if __name__ == '__main__':
    main()
