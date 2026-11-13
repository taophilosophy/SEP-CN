# -*- coding: utf-8 -*-
r"""019 探针：raw HTML 里 \amp \osim \eqdf 等可疑宏的实际上下文。"""
import re
import sys

path = sys.argv[1]
names = sys.argv[2:] or ['amp', 'osim', 'eqdf', 'lamp', 'IC', 'PA', 'sH']
txt = open(path, encoding='utf-8', errors='replace').read()
for name in names:
    pat = re.compile(r'\\' + name + r'(?![a-zA-Z])')
    hits = list(pat.finditer(txt))
    print(f'== {name}: {len(hits)}')
    for m in hits[:2]:
        print('   ', repr(txt[max(0, m.start() - 70):m.start() + 60]))
