# -*- coding: utf-8 -*-
"""021 探针：zh 与 yuanwen 中 PDL 拆行公式的精确字节对照。"""
BS = chr(92)

zh = open('l/logic-dynamic.md', encoding='utf-8').read().split('\n')
yw = open('yuanwen/l/logic-dynamic.md', encoding='utf-8').read().split('\n')

for n in (181, 183, 184, 305, 307):
    line = zh[n - 1]
    k = line.find('leftrightarrow' + BS)
    if k < 0:
        k = line.find('rightarrow' + BS)
    print('ZH', n, repr(line[k + 14:k + 50]))

pat1 = 'leftrightarrow' + BS
pat2 = 'rightarrow' + BS
for n, line in enumerate(yw, 1):
    for pat in (pat1, pat2):
        k = line.find(pat)
        if k >= 0 and ('| 1. |' in line or '| 2. |' in line or '| 3. |' in line
                       or '| 10. |' in line or '| 12. |' in line):
            print('YW', n, repr(line[k + 14:k + 50]))
            break
