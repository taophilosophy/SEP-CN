# -*- coding: utf-8 -*-
"""018 排查辅助：打印两棵树中指定文件的归一化首处差异。"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regression_scan import collapse_quotes, nostar  # noqa: E402


def show(old_root, new_root, rel, span=80):
    old = io.open(os.path.join(old_root, rel), encoding='utf-8').read().splitlines()
    new = io.open(os.path.join(new_root, rel), encoding='utf-8').read().splitlines()
    a, b = collapse_quotes(old), collapse_quotes(new)
    sa = ''.join(nostar(x) for x in a)
    sb = ''.join(nostar(x) for x in b)
    i = 0
    while i < min(len(sa), len(sb)) and sa[i] == sb[i]:
        i += 1
    print('===', rel, 'len', len(sa), len(sb), 'first diff at', i)
    print('  OLD:', repr(sa[max(0, i - span):i + span].replace('\xa0', '~')))
    print('  NEW:', repr(sb[max(0, i - span):i + span].replace('\xa0', '~')))


if __name__ == '__main__':
    old_root, new_root = sys.argv[1], sys.argv[2]
    for rel in sys.argv[3:]:
        show(old_root, new_root, rel)
