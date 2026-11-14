# -*- coding: utf-8 -*-
"""多点差异定性：backup vs 现行，nospace 归一后列出全部差异区段。"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regression_scan import collapse_quotes, nostar  # noqa: E402

old_root, new_root = sys.argv[1], sys.argv[2]
for rel in sys.argv[3:]:
    a = io.open(os.path.join(old_root, rel), encoding='utf-8').read().splitlines()
    b = io.open(os.path.join(new_root, rel), encoding='utf-8').read().splitlines()
    sa = ''.join(nostar(x) for x in collapse_quotes(a))
    sb = ''.join(nostar(x) for x in collapse_quotes(b))
    print(f'=== {rel} len {len(sa)} vs {len(sb)}')
    i = j = 0
    spots = 0
    while spots < 6:
        k = 0
        while k < min(len(sa) - i, len(sb) - j) and sa[i + k] == sb[j + k]:
            k += 1
        if k == min(len(sa) - i, len(sb) - j) and (len(sa) - i == len(sb) - j):
            break
        print(f'  diff@{i}/{j}: OLD {sa[max(0,i-40):i+70]!r}')
        print(f'            NEW {sb[max(0,j-40):j+70]!r}')
        # 跳过这段差异（找重新同步点：简单前进 1）
        i += k + 1
        j += k + 1
        spots += 1
