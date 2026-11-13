# -*- coding: utf-8 -*-
r"""019 分析：align-zh.jsonl 汇总（按词条/类别），供逐条定性。"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, '..', 'results')
PATH = os.path.join(RESULTS, 'align-zh.jsonl')

BAD = ('extra-in-zh', 'missing-in-zh', 'structural', 'kind-mismatch')


def main():
    rows = [json.loads(l) for l in open(PATH, encoding='utf-8')]
    by_file = collections.Counter()
    only_in = collections.Counter()
    samples = collections.defaultdict(list)
    for r in rows:
        if r['v'] in BAD:
            by_file[r['key']] += 1
            samples[r['key']].append((r['i'], r['v'], r['note'][:160]))
        if r['v'] in ('extra-in-zh', 'missing-in-zh'):
            only_in[(r['key'], r['v'])] += 1
    print('|词条|问题数|')
    for f, n in by_file.most_common(15):
        print(f'{f}\t{n}\tsamples={samples[f][:2]}')
    print('\n== 完全只有增/缺的文件（无 structural）')
    for (f, v), n in only_in.most_common(10):
        print(f, v, n)


if __name__ == '__main__':
    main()
