# -*- coding: utf-8 -*-
"""021 探针：按行号 dump 涉案行字节，供逐处定性（货币 $ / $__ / $* / 空段）。"""
import os
import sys

BS = chr(92)

TARGETS = {
    'c/cancer.md': [5, 151],
    'f/fuller-margaret.md': [15],
    'g/gregory-rimini.md': [109],
    'h/heritability.md': [133, 139, 140, 141, 142, 143],
    'j/justice-moral-psych.md': [96, 281, 307],
    'm/moral-demands-permissions.md': [25, 47, 61],
    'o/organs-sale.md': [61, 161],
    'r/risk.md': [211],
}

for rel, lines in TARGETS.items():
    text = open(rel.replace('/', os.sep), encoding='utf-8').read().split('\n')
    print('=' * 20, rel)
    for n in lines:
        if n - 1 < len(text):
            print(f'[{n}]', repr(text[n - 1][:400]))

import os  # noqa: E402
