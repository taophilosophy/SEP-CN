# -*- coding: utf-8 -*-
r"""019 en/ 快照与上游快照的公式抽取（check_math 同口径 + 实体反解）。

抽取自原始 HTML 文本中的 $$…$$ / \[…\] / \(…\)，公式体 html.unescape 反解、
保留原序与位置。单 $ 已定性为货币非公式，不抽。上游快照
state/mathval/upstream/<slug>.html 与 en/<slug>/index.html 同脚本同口径处理，
产 results/en-formulas.jsonl 每行 {f,i,k,x,s}（s: snapshot|upstream）。

用法: python -I specs/019-math-formula-audit/bin/extract_en.py
"""
import html
import json
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, '..', 'results')

MATH_RE = re.compile(r'(\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\))', re.S)
KINDS = {'$$': 'display', '\\[': 'display', '\\(': 'inline'}


def kind_of(tok):
    if tok.startswith('$$'):
        return 'display'
    if tok.startswith('\\['):
        return 'display'
    return 'inline'


def scan(path, src, slug, out):
    with open(path, encoding='utf-8', errors='replace') as fh:
        txt = fh.read()
    i = 0
    for m in MATH_RE.finditer(txt):
        tok = m.group(1)
        body = html.unescape(tok)
        out.write(json.dumps({'f': f'{slug}/{os.path.basename(path)}', 'i': i,
                              'k': kind_of(tok), 'x': body, 's': src},
                             ensure_ascii=False) + '\n')
        i += 1
    return i


def main():
    en_path = os.path.join(RESULTS, 'en-formulas.jsonl')
    up_path = os.path.join(RESULTS, 'upstream-formulas.jsonl')
    os.makedirs(RESULTS, exist_ok=True)
    total = files = up_total = 0
    with open(en_path, 'w', encoding='utf-8') as out:
        en_dir = os.path.join(REPO, 'en')
        for slug in sorted(os.listdir(en_dir)):
            d = os.path.join(en_dir, slug)
            if not os.path.isdir(d):
                continue
            for name in sorted(os.listdir(d)):
                if name.endswith('.html'):
                    n = scan(os.path.join(d, name), 'snapshot', slug, out)
                    total += n
                    files += 1 if n else 0
    with open(up_path, 'w', encoding='utf-8') as out:
        up_dir = os.path.join(REPO, 'state', 'mathval', 'upstream')
        if os.path.isdir(up_dir):
            for name in sorted(os.listdir(up_dir)):
                if name.endswith('.html'):
                    up_total += scan(os.path.join(up_dir, name), 'upstream',
                                     name[:-5], out)
    print(f'snapshot: {files} files, {total} formulas → {en_path}')
    print(f'upstream: {up_total} formulas → {up_path}')


if __name__ == '__main__':
    main()
