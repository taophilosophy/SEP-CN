# -*- coding: utf-8 -*-
"""021 探针：yuanwen 对应形态核对（$ 记号类）。"""
BS = chr(92)

CASES = [
    ('yuanwen/j/justice-moral-psych.md', '__'),
    ('yuanwen/r/risk.md', BS + 'times'),
    ('yuanwen/h/heritability.md', 'PGS'),
    ('yuanwen/h/heritability.md', 'beta'),
    ('yuanwen/g/gregory-rimini.md', '$100'),
    ('yuanwen/f/fuller-margaret.md', '$200'),
    ('yuanwen/o/organs-sale.md', '$30,000'),
    ('yuanwen/c/cancer.md', '$5.74'),
    ('yuanwen/m/moral-demands-permissions.md', '$1000'),
]

for rel, pat in CASES:
    t = open(rel.replace('/', BS), encoding='utf-8').read()
    hit = False
    for i, line in enumerate(t.split(chr(10)), 1):
        if pat in line:
            print(rel, i, repr(line[:200]))
            hit = True
            break
    if not hit:
        print(rel, 'PATTERN NOT FOUND:', pat)
