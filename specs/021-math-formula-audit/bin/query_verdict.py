# -*- coding: utf-8 -*-
r"""021 查询：在 verdicts.jsonl 里按子串查编译判定。"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, '..', 'results', 'verdicts.jsonl')
needle = sys.argv[1]
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
n = 0
with open(PATH, encoding='utf-8') as fh:
    for line in fh:
        r = json.loads(line)
        if needle in r['x']:
            print(r['ok'], r['k'], (r['err'] or '')[:90])
            print('   ', r['x'][:220].replace('\n', ' '))
            n += 1
            if n >= limit:
                break
print('shown', n)
