# -*- coding: utf-8 -*-
"""021 探针：打印 yuanwen 各涉案美元记号的紧邻上下文。"""
import re

BS = chr(92)

CASES = [
    ('yuanwen/j/justice-moral-psych.md', ['__']),
    ('yuanwen/r/risk.md', ['times', '4,000,000', '10,000']),
    ('yuanwen/h/heritability.md', ['PGS_j', 'beta']),
    ('yuanwen/g/gregory-rimini.md', ['$', ]),
    ('yuanwen/f/fuller-margaret.md', ['$200']),
    ('yuanwen/c/cancer.md', ['5.74', '79 million', '150,000', '458']),
]

for rel, pats in CASES:
    t = open(rel.replace('/', BS), encoding='utf-8').read()
    print('=' * 16, rel)
    for pat in pats:
        for m in re.finditer(re.escape(pat), t):
            s = max(0, m.start() - 70)
            print(f'[{pat}]', repr(t[s:m.end() + 70]))
            break
