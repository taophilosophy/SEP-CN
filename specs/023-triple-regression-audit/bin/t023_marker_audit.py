# -*- coding: utf-8 -*-
"""标记邻接性审计：对正文每个 [^key] 标记，检查其键的人名/年份片段
是否出现在标记前 ~90 字符内（引用组语境）。无邻接者列为幻键候选，
人工回源定性。"""
import re
import sys

text = open(sys.argv[1], encoding='utf-8').read()
body = text.split('## 脚注')[0].split('## Notes（原文脚注）')[0]
body = body.split('## 参考文献')[0]

# defs 键 → 线索串（姓氏 + 年份）
defs = dict(re.findall(r'\[\^([^\]]+)\]:\s*([^\n]*)', text))
for k in defs:
    m = re.match(r'^(.*?) coming', '')
    defs[k] = defs[k][:110]

markers = list(re.finditer(r'\[\^([^\]\s]+)\](?!:)', body))
suspects = []
for m in markers:
    key = m.group(1)
    ctx = body[max(0, m.start() - 90):m.start()]
    base = key.rstrip('0123456789-')
    year = re.search(r'(\d{4}[a-b]?)$', key)
    clues = []
    if year:
        clues.append(year.group(1))
    # 键首词（转 ASCII、去撇号）
    first = re.sub(r'[^a-z]', '', key.split('-')[0].lower().replace(chr(8217), ''))
    surname = None
    dm = re.match(r'[^,]*?([A-Z][A-Za-z\u00C0-\u017F\'-]+),', defs.get(key, ''))
    if dm:
        surname = dm.group(1)
    hit = False
    for c in filter(None, [year.group(1) if year else None, surname, first if len(first) >= 4 else None]):
        if c and c.lower() in ctx.lower():
            hit = True
            break
    if not hit:
        suspects.append((key, ctx[-60:].replace('\n', ' ')))
print('标记总数', len(markers), '| 幻键候选', len(suspects))
for k, c in suspects:
    print('  ', k, '| 语境…' + c)
