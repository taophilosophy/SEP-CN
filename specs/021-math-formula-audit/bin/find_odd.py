# -*- coding: utf-8 -*-
r"""021 定位器：列出指定文件中 $ 计数为奇数的行（错配源头）。"""
import sys

path = sys.argv[1]
lines = open(path, encoding='utf-8').read().split('\n')
for i, l in enumerate(lines):
    # 去掉 \$ 与 $$ 再计数
    t = l.replace('\\$', '')
    n = 0
    j = 0
    while j < len(t):
        if t[j] == '$':
            if j + 1 < len(t) and t[j + 1] == '$':
                j += 2
                continue
            n += 1
        j += 1
    if n % 2:
        print(f'L{i+1} (odd={n}): {l}')
