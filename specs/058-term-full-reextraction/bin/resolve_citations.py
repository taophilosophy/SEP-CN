# -*- coding: utf-8 -*-
"""审定条目全局索引 + 逐行复核（2026-11-25）。

缓存是按查询词落盘的：同一部审定条目可能出现在别的键的缓存里。对“首屏未见”
的 78 行，先在全局索引里找同名条目，找到即说明该条目确有审定出处，可据实补引；
找不到才留待翻页复核。

输出：results/termonline-citation-resolve-2026-11-25.tsv（key｜译法｜结论｜出处）
"""
import glob
import io
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

QD = 'specs/008-terminology-campaign/results/queries/termonline-all'
AUDIT = 'specs/058-term-full-reextraction/results/termonline-citation-audit-2026-11-25.tsv'
OUT = 'specs/058-term-full-reextraction/results/termonline-citation-resolve-2026-11-25.tsv'


def strong(s):
    s = unicodedata.normalize('NFKD', str(s or '').casefold())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s)


def main():
    idx = {}
    files = glob.glob(os.path.join(QD, '*.json'))
    print('缓存文件', len(files))
    for p in files:
        try:
            j = json.load(io.open(p, encoding='utf-8'))
        except Exception:
            continue
        for h in j.get('hits') or []:
            cn = strong(h.get('cn'))
            if not cn or cn in idx:
                continue
            idx[cn] = (h.get('cn'), h.get('standard'), h.get('subject'),
                       h.get('code'), os.path.basename(p)[:-5])
    print('条目索引', len(idx))

    rows = []
    for line in io.open(AUDIT, encoding='utf-8'):
        c = line.rstrip('\n').split('\t')
        if len(c) < 3 or c[2] != 'page1-miss':
            continue
        key, zh = c[0], c[1]
        main_zh = strong(zh.split('（')[0].strip('《》'))
        cited = [strong(x) for x in re.findall(r'审定作[“"]([^”"]+)[”"]', c[1] + ' ' + c[4] if len(c) > 4 else zh)]
        hit = idx.get(main_zh) or (idx.get(cited[0]) if cited else None)
        if hit:
            rows.append((key, zh, 'found', '｜'.join(str(x) for x in hit[:4])))
        else:
            rows.append((key, zh, 'unresolved', ''))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('key\tzh\tverdict\tevidence\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    found = sum(1 for r in rows if r[2] == 'found')
    print('复核 %d 行：找到同名审定条目 %d，未决 %d → %s'
          % (len(rows), found, len(rows) - found, OUT))


if __name__ == '__main__':
    main()
