# -*- coding: utf-8 -*-
r"""021 辅助：打印文件内 `$` 紧跟数字的上下文（货币判定复核）。"""
import re
import sys

CUR = re.compile(r'(?<!\\)\$(?=\d[\d,]*(?:\.\d+)?)')
for path in sys.argv[1:]:
    text = open(path, encoding='utf-8').read()
    print('=====', path)
    for m in CUR.finditer(text):
        s = max(0, m.start() - 55)
        print('  ', repr(text[s:m.start() + 75]))
