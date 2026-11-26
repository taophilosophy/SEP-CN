# -*- coding: utf-8 -*-
"""量测：131 条非英语原文缺口，能否从 en/ 正文取到显式配对的原文文字（2026-11-26）。

对每条：取首现 slug 的 en/ 正文，找键（IAST／转写）出现处，在其前后 120 字内找非拉丁
文字（希腊、天城体、藏文、阿拉伯、希伯来等）。命中即输出上下文供人工核；ADR-0087 口径
不变——只采页面显式配对，查无留“—”为终态。
"""
import html
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
OUT = 'script/tmp/orig-script-harvest.tsv'
SCRIPTS = re.compile(r'[\u0370-\u03ff\u1f00-\u1fff\u0900-\u097f\u0f00-\u0fff'
                     r'\u0600-\u06ff\u0590-\u05ff\u4e00-\u9fff]')


def clean(t):
    t = html.unescape(t)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t)


def load(slug):
    for name in ('index.html', 'notes.html'):
        p = os.path.join('en', slug, name)
        if os.path.exists(p):
            return clean(io.open(p, encoding='utf-8', errors='replace').read())
    return ''


def main():
    rows = []
    # 术语表：键|原文|译法|首现|依据|日期
    for l in io.open('shu-yu-biao.md', encoding='utf-8', newline=''):
        if not l.startswith('|'):
            continue
        c = [x.strip() for x in l.split('|')]
        if len(c) < 8 or not c[1] or c[1] == '键':
            continue
        key, orig, first = c[1], c[2], c[4]
        if orig not in ('—', ''):
            continue
        if re.match(r'^[\x00-\x7f]+$', key):
            continue          # 纯 ASCII 键本就不缺原文
        if not re.match(r'^[A-Za-z0-9_.-]+$', first or ''):
            continue
        rows.append((key, first))
    got = 0
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('键\t首现\t原文候选\t上下文\n')
        for key, slug in rows:
            txt = load(slug)
            if not txt:
                continue
            core = re.sub(r'\s*/\s*', '|', key)
            pat = re.compile(r'[\\s(](' + '|'.join(re.escape(x) for x in core.split('|')) + r')[\s),;.]',
                             re.I)
            for m in pat.finditer(txt):
                lo, hi = max(0, m.start() - 120), m.end() + 120
                w = txt[lo:hi]
                if SCRIPTS.search(w):
                    # 取窗口里第一段非拉丁文字
                    s = SCRIPTS.search(w)
                    start = max(0, s.start() - 2)
                    cand = w[start:start + 24].strip()
                    f.write('%s\t%s\t%s\t%s\n' % (key, slug, cand.replace('\t', ' '), w.strip()))
                    got += 1
                    break
    print('缺口行 %d，取到原文候选 %d' % (len(rows), got))


if __name__ == '__main__':
    main()
