# -*- coding: utf-8 -*-
"""中文语料频次审计（2026-11-25）：池中 new 候选对中文译文语料计数。

用法：python -I specs/058-term-full-reextraction/bin/audit_zh_corpus.py [min_freq]
产物：specs/058-term-full-reextraction/results/zh-corpus-audit-2026-11-25.tsv

已知偏差（2026-11-25 首轮，见 results/pool-harvest-b6-2026-11-25.md §2）：
登记册的合并键（`a / b / c`）只按整串进 reg_keys，拆形不在内，故
`relevant logic`、`future contingent`、`moral sentiments`、`non-classical logics`
这类「旧键并入围」的词会被判成缺口。下轮应先按 `/` 拆形并加单复数变体，
再比对；本轮以一次性二次筛查代替，TSV 未重算。
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key  # noqa: E402

ROOT = '.'
MIN_FREQ = int(sys.argv[1]) if len(sys.argv) > 1 else 35

# ---- 已登记集合 ----
reg_keys = set()
reg_zh = set()
for l in io.open('shu-yu-biao.md', encoding='utf-8'):
    if not l.startswith('| '):
        continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) != 6:
        continue
    reg_keys.add(norm_key(c[0]))
    if c[2] != '—':
        reg_zh.add(c[2])
for l in io.open('ren-ming-biao.md', encoding='utf-8'):
    if not l.startswith('| '):
        continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) != 8:
        continue
    reg_keys.add(norm_key(c[0]))
    reg_keys.add(norm_key(c[2]))


def base_norm(s):
    s = s.lower().replace('’', "'")
    s = re.sub(r'\s+', ' ', s).strip()
    return s


# ---- 候选 ----
d = json.load(io.open('tasks/term-pool.json', encoding='utf-8'))
cands = []
seen = set()
for c in d['candidates']:
    if not str(c.get('status', '')).startswith('new'):
        continue
    en = (c.get('en') or '').strip()
    if not en or len(en) < 4 or len(en) > 60:
        continue
    if c.get('freq', 0) < MIN_FREQ:
        continue
    if c.get('type') not in ('term', 'phrase'):
        continue
    if norm_key(en) in reg_keys:
        continue
    k = base_norm(en)
    if k in seen:
        continue
    seen.add(k)
    cands.append((en, c.get('freq', 0)))

print('候选', len(cands))

# ---- AC 自动机（大小写不敏感：输入与模式统一 lower） ----
patterns = {base_norm(en): en for en, _ in cands}
goto = [{}]
fail = [0]
out = [[]]
for p, en in patterns.items():
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
# BFS fail links
from collections import deque  # noqa: E402
q = deque()
for ch, n in goto[0].items():
    q.append(n)
while q:
    r = q.popleft()
    for ch, n in goto[r].items():
        q.append(n)
        f = fail[r]
        while f and ch not in goto[f]:
            f = fail[f]
        fail[n] = goto[f].get(ch, 0) if goto[f].get(ch, 0) != n else 0
        out[n] = out[n] + out[fail[n]]

counts = {p: 0 for p in patterns}

# ---- 语料 ----
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
total_bytes = 0
for letter in LETTERS:
    dpath = os.path.join(ROOT, letter)
    if not os.path.isdir(dpath):
        continue
    for fn in os.listdir(dpath):
        if not fn.endswith('.md'):
            continue
        fp = os.path.join(dpath, fn)
        try:
            with open(fp, 'rb') as f:
                raw = f.read()
        except OSError:
            continue
        total_bytes += len(raw)
        text = raw.decode('utf-8', 'ignore').lower().replace('’', "'")
        node = 0
        for ch in text:
            while node and ch not in goto[node]:
                node = fail[node]
            node = goto[node].get(ch, 0)
            if out[node]:
                for p in out[node]:
                    counts[p] += 1

print('语料字节', total_bytes)

rows = []
for p, n in counts.items():
    if n < 6:
        continue
    en = patterns[p]
    if en in reg_zh:
        continue
    rows.append((n, en))
rows.sort(reverse=True)
os.makedirs('specs/058-term-full-reextraction/results', exist_ok=True)
outp = 'specs/058-term-full-reextraction/results/zh-corpus-audit-2026-11-25.tsv'
with io.open(outp, 'w', encoding='utf-8', newline='\n') as f:
    f.write('zh_count\ten\tpool_freq\n')
    pf = {en: fr for en, fr in cands}
    for n, en in rows:
        f.write('%d\t%s\t%d\n' % (n, en, pf.get(en, 0)))
print('输出', outp, '行数', len(rows))
for n, en in rows[:40]:
    print(n, en)
