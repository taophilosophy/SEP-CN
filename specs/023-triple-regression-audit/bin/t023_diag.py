# -*- coding: utf-8 -*-
"""逐行诊断：对指定 slug 的丢失行，打印 en 行 norm 与 yw norm 的最近上下文。

用法: python -I specs/023.../bin/t023_diag.py <slug> <行首片段>...
"""
import re
import sys

sys.path.insert(0, '.')
BIN = 'specs/023-triple-regression-audit/bin'
sys.path.insert(0, BIN)
import importlib.util

spec = importlib.util.spec_from_file_location('tc', BIN + '/t023_containment.py')
tc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tc)

slug = sys.argv[1]
frag = sys.argv[2]

rows = tc.en_rows(slug)
yn = tc.yw_norm(slug)
for ti, ri, txt in rows:
    if frag not in txt:
        continue
    n = tc.norm(txt)
    print('行原文:', txt[:120])
    print('en norm :', n)
    # 在 yw norm 里找最长公共前缀断点
    lo, hi = 0, len(n)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if n[:mid] in yn:
            lo = mid
        else:
            hi = mid - 1
    print('yw 中可匹配前缀长 %d / %d' % (lo, len(n)))
    if lo < len(n):
        pos = yn.find(n[:lo])
        print('yw 上下文 ...%s[N_break]%s...' % (yn[max(0, pos - 30):pos + lo], yn[pos + lo:pos + lo + 60]))
        print('en 断点后  :', n[lo:lo + 60])
    print()
