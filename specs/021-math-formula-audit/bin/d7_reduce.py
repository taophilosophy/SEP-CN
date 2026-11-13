# -*- coding: utf-8 -*-
r"""019 D7 归并器：把「切分差异」与「真内容差异」分开。

同一词条内，en 缺失多重集 M 与 zh 多出多重集 X 常由公式切分点不同造成：
  - zh 把 en 的相邻两条合为一条（X 的一条 ≈ M 两条拼接）
  - zh 把 en 的一条拆为两条（反之）
本脚本在词条内做贪心归并：若某条 zh 额外体等于某几条 en 缺失体的顺序拼接
（允许其间出现空白），判 merge/swap；归不掉的留作真差异（residual）。
产 results/d7-residual.jsonl 与汇总。
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, '..', 'results')
sys.path.insert(0, HERE)
from align import load, norm  # noqa: E402


def try_concat(pieces, target):
    """pieces 的某个顺序拼接是否等于 target（允许片段间空白）。"""
    s = ''.join(p.strip() for p in pieces)
    t = re.sub(r'\s+', '', target)
    return re.sub(r'\s+', '', s) == t


def main():
    en = load(os.path.join(RESULTS, 'en-formulas.jsonl'))
    zh = load(os.path.join(RESULTS, 'render-zh.jsonl'))
    rows = [json.loads(l) for l in open(os.path.join(RESULTS, 'zh-defects.jsonl'),
                                        encoding='utf-8')]
    per = collections.defaultdict(lambda: {'missing': collections.Counter(),
                                           'extra': collections.Counter()})
    for r in rows:
        if r['code'] == 'D7-missing':
            per[r['f']]['missing'][norm(r['x'])] += r.get('n', 1)
        elif r['code'] == 'D7-extra':
            per[r['f']]['extra'][norm(r['x'])] += r.get('n', 1)
    summary = collections.Counter()
    out = open(os.path.join(RESULTS, 'd7-residual.jsonl'), 'w', encoding='utf-8')
    for f, d in sorted(per.items()):
        miss = d['missing']
        extra = d['extra']
        merged = 0
        # 贪心：extra 中被 en 缺失集拼接命中的，从两侧移除
        for body, n in list(extra.items()):
            for _ in range(n):
                hit = None
                # 尝试 2..4 条拼接
                keys = list(miss)
                for size in (2, 3, 4):
                    for combo in _combos(keys, size):
                        if all(miss[k] > 0 for k in combo) and try_concat(combo, body):
                            hit = combo
                            break
                    if hit:
                        break
                if hit:
                    for k in hit:
                        miss[k] -= 1
                        if miss[k] == 0:
                            del miss[k]
                    extra[body] -= 1
                    merged += 1
        summary['merged'] += merged
        for body, n in miss.items():
            if n > 0:
                summary['missing_residual'] += n
                out.write(json.dumps({'f': f, 'code': 'missing', 'n': n,
                                      'x': body[:200]}, ensure_ascii=False) + '\n')
        for body, n in extra.items():
            if n > 0:
                summary['extra_residual'] += n
                out.write(json.dumps({'f': f, 'code': 'extra', 'n': n,
                                      'x': body[:200]}, ensure_ascii=False) + '\n')
    out.close()
    print(json.dumps(summary, ensure_ascii=False, indent=1))


def _combos(keys, size):
    import itertools
    return itertools.combinations(keys, size)


if __name__ == '__main__':
    main()
