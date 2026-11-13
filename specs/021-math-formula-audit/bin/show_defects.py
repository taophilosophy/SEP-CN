# -*- coding: utf-8 -*-
r"""019 缺陷清单打印：按 code 分组，供逐条人眼定性。"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, '..', 'results', 'zh-defects.jsonl')


def main():
    codes = sys.argv[1:] or None
    rows = [json.loads(l) for l in open(PATH, encoding='utf-8')]
    grouped = collections.defaultdict(list)
    for r in rows:
        key = r['code'].split('-')[0]
        if codes and key not in codes:
            continue
        grouped[key].append(r)
    for key in sorted(grouped):
        items = grouped[key]
        print(f'\n===== {key} ({len(items)}) =====')
        for r in items[:int(os.environ.get('LIMIT', '40'))]:
            print(f"{r['f']}#{r.get('i','-')} {r.get('n','')} {r['x'][:180]!r}")


if __name__ == '__main__':
    main()
