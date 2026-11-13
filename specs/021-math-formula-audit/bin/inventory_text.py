# -*- coding: utf-8 -*-
r"""021 公式内文字清单：\text{} 等内嵌串的去重词表（按频次）。

输出 results/text-in-math-inventory.json：{inner: {n, files:[...], kind}}，
kind ∈ connective（连接语，须译）/ name（专名/示例谓词，保留）/ acronym
（缩写记号，保留）/ cjk（已译）/ punct（标点/空白）。
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, '..', 'results')
sys.path.insert(0, HERE)
from align import load, strip_delims  # noqa: E402

TEXTCMD_RE = re.compile(
    r'\\(text|mbox|textnormal|textrm|textup|textbf|textit|textsf|texttt|'
    r'operatorname\*?|hbox)\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}')
CJK_RE = re.compile(r'[\u4e00-\u9fff]')
# 连接语白名单（须译）
CONNECTIVES = {
    'and', 'or', 'not', 'iff', 'if', 'then', 'else', 'if and only if',
    'if, and only if,', 'for all', 'for some', 'for every', 'for each',
    'where', 'when', 'whenever', 'such that', 'if and only if,', 'only if',
    'at', 'in', 'on', 'with', 'without', 'is', 'are', 'be', 'hold', 'holds',
    'true', 'false', 'yes', 'no', 'other', 'otherwise', 'otherwise,',
    'provided', 'provided that', 'unless', 'given', 'let', 'suppose',
    'for', 'the', 'of', 'to', 'by', 'from', 'as', 'that', 'which',
    'for all x', 'for some x', 'for all n', 'for every n',
    'ground state', 'excited state', 'rest', 'rest frame',
    'dom', 'range', 'rank', 'card', 'supp',
}
PUNCT_RE = re.compile(r'^[\s\-–—,.;:()\[\]{}/\\|]+$')


def kind_of(inner):
    s = inner.strip()
    if not s:
        return 'punct'
    if CJK_RE.search(s):
        return 'cjk'
    if PUNCT_RE.match(s):
        return 'punct'
    low = s.lower()
    if low in CONNECTIVES:
        return 'connective'
    if re.fullmatch(r'[A-Za-z]{1,6}', s) and (s.isupper() or len(s) <= 3):
        return 'acronym'
    if re.fullmatch(r'[A-Za-z][a-z]{2,}', s):
        return 'name'  # Donkey / Farmer / toast 等示例词
    return 'phrase'


def main(mode='render-zh'):
    seq = load(os.path.join(RESULTS, f'{mode}.jsonl'))
    inv = {}
    for f, items in seq.items():
        for kind, body in items:
            bare = strip_delims(kind, body)
            for m in TEXTCMD_RE.finditer(bare):
                inner = m.group(2).strip()
                if not inner:
                    continue
                rec = inv.setdefault(inner, {'n': 0, 'files': set(),
                                             'kind': kind_of(inner)})
                rec['n'] += 1
                rec['files'].add(f)
    out = {k: {'n': v['n'], 'kind': v['kind'], 'files': sorted(v['files'])[:8]}
           for k, v in sorted(inv.items(), key=lambda kv: -kv[1]['n'])}
    json.dump(out, open(os.path.join(RESULTS, 'text-in-math-inventory.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False, indent=1)
    by_kind = collections.Counter(v['kind'] for v in out.values())
    print(json.dumps(by_kind, ensure_ascii=False, indent=1))
    for k, v in out.items():
        if v['kind'] in ('connective', 'phrase'):
            print(f"  {v['kind']:10s} {v['n']:4d}  {k[:60]!r}  {v['files'][:2]}")


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'render-zh')
