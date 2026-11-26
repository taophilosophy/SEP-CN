# -*- coding: utf-8 -*-
"""首现含词审计：术语登记册的「首现」词条，正文里到底有没有这个词（只读，2026-11-26）。

用法：python -I specs/058-term-full-reextraction/bin/audit_first_contains.py
产出：specs/058-term-full-reextraction/results/first-contains-2026-11-26.tsv

口径：
* 首现只取裸 slug、`<letter>/<slug>`、`<slug>.supplement` 三类；散文标注（语料回收（…）、
  待核（…））不判。
* 正文取该词条目录下**全部** HTML（index、notes、supplement、further-discussion…），
  Unicode NFC 归一后小写。
* 键取拉丁词（≥4 字母）逐个比对：任一 5 字前缀命中即算“含该词”（容复数与词形变化）；
  含 CJK 的键另按汉字串比对，不打拉丁前缀。
* 只列“全部词都不命中”的行，供人工回源；不判“首现是否应为该条”（语义另判）。
"""
import html
import io
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')
OUT = 'specs/058-term-full-reextraction/results/first-contains-2026-11-26.tsv'
SLUG_RE = re.compile(r'(?=.*[a-z])[A-Za-z0-9][A-Za-z0-9_.-]*$')
PATH_RE = re.compile(r'[a-z]/([A-Za-z0-9][A-Za-z0-9_.-]*)$')
_cache = {}


def load(base):
    if base in _cache:
        return _cache[base]
    t = ''
    d = os.path.join('en', base)
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.endswith('.html'):
                t += io.open(os.path.join(d, f), encoding='utf-8', errors='replace').read()
    t = unicodedata.normalize('NFC', html.unescape(re.sub(r'<[^>]+>', ' ', t)))
    _cache[base] = fold(t)
    return _cache[base]


def fold(s):
    """去变音符后小写：IAST／阿拉伯转写的 ā、ṇ、ʿ 等归一，避免正则与比对漏配。"""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    s = s.replace('ʿ', '').replace('ʾ', '').replace('’', "'")
    return re.sub(r'\s+', ' ', s).lower()


def main():
    rows = []
    for lineno, line in enumerate(io.open('shu-yu-biao.md', encoding='utf-8', newline=''), 1):
        if not line.startswith('|'):
            continue
        c = [x.strip() for x in line.split('|')]
        if len(c) < 7 or not c[1] or c[1] == '键':
            continue
        fs = c[4]
        base = None
        if SLUG_RE.match(fs):
            base = fs.split('.')[0]
        else:
            m = PATH_RE.match(fs)
            if m:
                base = m.group(1)
        if not base or not os.path.isdir(os.path.join('en', base)):
            continue
        txt = load(base)
        fkey = fold(c[1])
        words = [w for w in re.findall(r"[a-z][a-z'’-]+", fkey) if len(w) >= 4]
        cjk = re.findall(r'[\u4e00-\u9fff]{2,}', c[1])
        hit = any(w[:5] in txt for w in words) or any(fold(x) in txt for x in cjk)
        if not hit:
            rows.append((lineno, c[1], base, c[3]))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('行\t键\t首现\t译法\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')
    print('首现含词审计：不命中 %d 行 → %s' % (len(rows), OUT))


if __name__ == '__main__':
    main()
