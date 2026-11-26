# -*- coding: utf-8 -*-
"""量测：人名表缺生卒的行，能否从 en/ 正文括注直接补捞（2026-11-26）。

做法：取该行首现 slug 的 en/<slug>/{index,notes}.html，实体还原后去标签，找键的姓氏
（或全名）出现处，在其后 60 字内找「YYYY–YYYY / YYYY-YYYY / 单年」括注。只作候选，
写表前须逐条看上下文（同句他人年份、书名年份、在位年都是假源，见人名线旧记）。
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
OUT = 'script/tmp/person-date-harvest.tsv'
ENT = re.compile(r'&(?:ndash|mdash);|&#82(?:11|12);')
YEAR = re.compile(r'(?<!\d)(1[0-9]{3}|[1-9][0-9]{2})\s*[–—-]\s*(1[0-9]{3}|[1-9][0-9]{2})(?!\d)')


def clean(t):
    t = ENT.sub('–', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'&[a-z]+;|&#\d+;', ' ', t)
    return re.sub(r'\s+', ' ', t)


def load(slug):
    out = []
    for name in ('index.html', 'notes.html'):
        p = os.path.join('en', slug, name)
        if os.path.exists(p):
            out.append((name, clean(io.open(p, encoding='utf-8', errors='replace').read())))
    return out


def surname(key):
    k = key.strip()
    return k.split(',')[0].strip() if ',' in k else k


def main():
    rows = []
    for l in io.open('ren-ming-biao.md', encoding='utf-8', newline=''):
        if not l.startswith('|'):
            continue
        c = [x.strip() for x in l.split('|')]
        if len(c) < 9 or not c[1] or c[1] == '键':
            continue
        key, years, slug = c[1], c[5], c[6]
        if years not in ('—', ''):
            continue
        if not re.match(r'^[A-Za-z0-9_.-]+$', slug or ''):
            continue
        rows.append((key, slug))
    got = 0
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('键\t首现\t年份候选\t上下文\n')
        for key, slug in rows:
            sn = surname(key)
            if len(sn) < 4:
                continue
            for name, txt in load(slug):
                hits = list(re.finditer(re.escape(sn), txt, re.I))
                done = False
                for m in hits:
                    tail = txt[m.end():m.end() + 70]
                    ym = YEAR.search(tail)
                    if ym:
                        lo = max(0, m.start() - 50)
                        ctx = txt[lo:m.end() + 70].strip()
                        f.write('%s\t%s\t%s\t%s: %s\n'
                                % (key, slug, ym.group(0), name, ctx))
                        got += 1
                        done = True
                        break
                if done:
                    break
    print('缺生卒行 %d，捞到年份候选 %d' % (len(rows), got))


if __name__ == '__main__':
    main()
