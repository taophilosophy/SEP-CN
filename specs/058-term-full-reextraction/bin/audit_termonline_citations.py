# -*- coding: utf-8 -*-
"""审定依据对账（2026-11-25，只读）：依据列声称的审定命中，是否真有缓存凭证支撑。

背景：登记册有 1400+ 行依据写“审定名词库（termonline-all·学科，日期）”。凭证在
本地缓存里，但缓存可能被覆盖、词条可能被改译法，若依据与凭证脱节就是“凭证失实”
——比没依据更坏。本脚本逐行核对：

  1. 缓存文件在不在（A 引号折叠键 / B 基础折叠键两口径都试）；
  2. 缓存里的 hits 有没有一条 cn 与本行译法主形一致；
  3. 依据里出现“审定作‘X’”时，X 是否也在 hits 里。

输出四档：ok（有对口命中）、cn-mismatch（有凭证但无同形命中）、no-cache、no-hits。
只报不写。
"""
import io
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools.cnki_query import safe_key  # noqa: E402
from tools.register_lib import norm_key, norm_key_quote  # noqa: E402

QD = 'specs/008-terminology-campaign/results/queries/termonline-all'
OUT = 'specs/058-term-full-reextraction/results/termonline-citation-audit-2026-11-25.tsv'


def strong(s):
    s = unicodedata.normalize('NFKD', str(s or '').casefold())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s)


def main():
    rows, stats = [], {'ok': 0, 'page1-miss': 0, 'no-cache': 0, 'no-hits': 0}
    for line in io.open('shu-yu-biao.md', encoding='utf-8'):
        if not line.startswith('| '):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) != 6 or '审定名词库' not in c[4]:
            continue
        key, zh = c[0], c[2]
        main_zh = strong(zh.split('（')[0].strip('《》'))
        cited = [strong(x) for x in re.findall(r'审定作[“"]([^”"]+)[”"]', c[4])]
        # 并键/改名后缓存可能落在旧键名下：键的每个“/”分段都试一遍
        path = None
        cands = [key, re.sub(r'\s*[（(][^）)]*[）)]', '', key)]  # 整键→去括注→分段
        for part in key.split(' / '):
            cands += [part, part.strip()]
        for part in cands:
            for name in (safe_key(norm_key_quote(part)), safe_key(norm_key(part))):
                p = os.path.join(QD, name + '.json')
                if os.path.exists(p):
                    path = p
                    break
            if path:
                break
        if not path:
            stats['no-cache'] += 1
            rows.append((key, zh, 'no-cache', '', ''))
            continue
        j = json.load(io.open(path, encoding='utf-8'))
        hits = j.get('hits') or []
        if not hits:
            stats['no-hits'] += 1
            rows.append((key, zh, 'no-hits', j.get('status', ''), (j.get('note') or '')[:60]))
            continue
        cns = {strong(h.get('cn')) for h in hits}
        raw = strong(j.get('raw') or '')
        # hits 只存每库前 20 条；对口条目可能落在页外，故同时看原始回包全文
        ok = (main_zh in cns or (cited and all(x in cns for x in cited))
              or (main_zh and main_zh in raw)
              or (cited and all(x in raw for x in cited)))
        grade = 'ok' if ok else 'page1-miss'
        stats[grade] += 1
        if not ok:
            rows.append((key, zh, grade, '|'.join(sorted({str(h.get('cn')) for h in hits})[:6])[:80],
                         '引作' + '/'.join(cited) if cited else ''))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('key\tzh\tgrade\thit_cn\tcited\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print(stats, '输出异常/缺失行', len(rows), '→', OUT)


if __name__ == '__main__':
    main()
