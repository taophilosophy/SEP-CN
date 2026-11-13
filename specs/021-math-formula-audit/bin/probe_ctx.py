# -*- coding: utf-8 -*-
r"""019 探针：按模式在 en html 与 zh md 里定位上下文，双侧对照。"""
import re
import sys

en_path, zh_path, pattern = sys.argv[1], sys.argv[2], sys.argv[3]
for label, path in (('EN', en_path), ('ZH', zh_path)):
    txt = open(path, encoding='utf-8', errors='replace').read()
    print(f'===== {label} {path}')
    for m in list(re.finditer(re.escape(pattern), txt))[:3]:
        s = max(0, m.start() - 160)
        print(repr(txt[s:m.end() + 160]))
