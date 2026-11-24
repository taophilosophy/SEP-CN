# -*- coding: utf-8 -*-
"""中文语料频次审计 v2（2026-11-25）：强归一版。

相对 v1 的三处修正（v1 偏差见 results/pool-harvest-b6-2026-11-25.md §2）：
1. 登记册排除改用强归一（去非字母数字、大小写、撇号），合并键按 `/` 拆形，
   并展开单复数——`relevant logic`／`non-classical logics` 一类不再误判缺口。
2. 加残片黑名单前缀（`van der`、`von `、`der `、`Grundlagen der` 等），
   跨词残片不再占据清单头部。
3. 参数化：--min-freq（池英文侧频次）、--min-zh（中文侧命中下限）、--out。

用法：
  python -I specs/058-term-full-reextraction/bin/audit_zh_corpus2.py \
      --min-freq 20 --min-zh 6 \
      --out specs/058-term-full-reextraction/results/zh-corpus-audit-f20-2026-11-25.tsv
"""
import argparse
import io
import json
import os
import re
import sys
from collections import deque

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

BLACK_PREFIX = (
    'van der', 'van den', 'van ', 'von ', 'della ', 'der ', 'und die', 'sur les',
    'super librum', 'grundlagen der', 'quod non', 'non est', 'libero arbitrio',
    'contra gentiles', 'philosophical studies', 'philosophical perspective',
    'philosophical papers', 'philosophical topics', 'philosophical writings',
    'philosophical essays', 'philosophical inquiry', 'philosophical issue',
    'philosophical work', 'philosophical text', 'philosophical thought',
    'philosophical problem', 'philosophical debate', 'philosophical tradition',
    'collected works', 'complete works', 'primary source', 'secondary literature',
    'originally published', 'english translations', 'doctoral dissertation',
    'lecture notes', 'published work', 'recent development', 'critical reflection',
    'case study', 'world health', 'international congress',
)


def strong(s):
    s = s.lower().replace('’', "'")
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s)


def reg_keys():
    keys = set()
    for fn, ncol in (('shu-yu-biao.md', 6), ('ren-ming-biao.md', 8)):
        for l in io.open(fn, encoding='utf-8'):
            if not l.startswith('| '):
                continue
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if len(c) != ncol:
                continue
            for p in c[0].split('/'):
                k = strong(p)
                if not k:
                    continue
                keys.add(k)
                keys.add(k + 's')
                keys.add(k[:-1] if k.endswith('s') else k)
    return keys


def base(s):
    s = s.lower().replace('’', "'")
    return re.sub(r'\s+', ' ', s).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min-freq', type=int, default=20)
    ap.add_argument('--min-zh', type=int, default=6)
    ap.add_argument('--out', default='specs/058-term-full-reextraction/results/'
                                    'zh-corpus-audit-f20-2026-11-25.tsv')
    a = ap.parse_args()

    keys = reg_keys()
    pool = json.load(io.open('tasks/term-pool.json', encoding='utf-8'))
    cands, seen = [], set()
    for c in pool['candidates']:
        if not str(c.get('status', '')).startswith('new'):
            continue
        en = (c.get('en') or '').strip()
        if not en or not (4 <= len(en) <= 60):
            continue
        if c.get('freq', 0) < a.min_freq or c.get('type') not in ('term', 'phrase'):
            continue
        low = en.lower()
        if any(low.startswith(p) for p in BLACK_PREFIX):
            continue
        if strong(en) in keys:
            continue
        k = base(en)
        if k in seen:
            continue
        seen.add(k)
        cands.append((en, c.get('freq', 0)))
    print('候选', len(cands))

    pats = {base(en): en for en, _ in cands}
    goto, fail, out = [{}], [0], [[]]
    for p in pats:
        node = 0
        for ch in p:
            nxt = goto[node].get(ch)
            if nxt is None:
                nxt = len(goto)
                goto[node][ch] = nxt
                goto.append({})
                fail.append(0)
                out.append([])
            node = nxt
        out[node].append(p)
    q = deque(goto[0].values())
    while q:
        r = q.popleft()
        for ch, n in goto[r].items():
            q.append(n)
            f = fail[r]
            while f and ch not in goto[f]:
                f = fail[f]
            cand = goto[f].get(ch, 0)
            fail[n] = cand if cand != n else 0
            out[n] = out[n] + out[fail[n]]

    counts = {p: 0 for p in pats}
    total = 0
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if not os.path.isdir(letter):
            continue
        for fn in sorted(os.listdir(letter)):
            if not fn.endswith('.md'):
                continue
            raw = open(os.path.join(letter, fn), 'rb').read()
            total += len(raw)
            text = raw.decode('utf-8', 'ignore').lower().replace('’', "'")
            node = 0
            for ch in text:
                while node and ch not in goto[node]:
                    node = fail[node]
                node = goto[node].get(ch, 0)
                for p in out[node]:
                    counts[p] += 1
    print('语料字节', total)

    pf = {en: fr for en, fr in cands}
    rows = sorted(((n, pats[p], pf[pats[p]]) for p, n in counts.items()
                   if n >= a.min_zh), reverse=True)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with io.open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('zh_count\ten\tpool_freq\n')
        for n, en, fr in rows:
            f.write('%d\t%s\t%d\n' % (n, en, fr))
    print('输出', a.out, '行数', len(rows))


if __name__ == '__main__':
    main()
