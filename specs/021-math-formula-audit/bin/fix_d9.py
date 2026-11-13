# -*- coding: utf-8 -*-
r"""021 D9：行内 $ 定界符内侧空白（站点保护正则不认，会漏配并吞正文）。

math-plugin 的单 $ 分支要求：内容首字符非空白（或为「空白+反斜杠」），
末字符非空白。故 `$ t_0 $`、`$1- \alpha $` 之类不参与配对，残留裸 $ 连锁
错配。本脚本把行内公式定界符内侧空白移除（块级 $$ 不动），逐处留痕。

用法: python -I fix_d9.py [--dry]
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')
sys.path.insert(0, HERE)
from expand_macros import fence_ranges, iter_math_spans  # noqa: E402

INLINE_RE = re.compile(r'(?<![\\$])\$(?!\$)([^$\n]+?)(?<!\\)\$(?!\$)')


def fix_span(span, stats):
    def repl(m):
        inner = m.group(1)
        core = inner.strip()
        if core and core != inner:
            stats['trimmed'] += 1
            return '$' + core + '$'
        return m.group(0)
    return INLINE_RE.sub(repl, span)


def process_file(path):
    text = open(path, encoding='utf-8').read()
    ranges = fence_ranges(text)
    stats = collections.Counter()
    pieces = []
    last = 0
    for start, end, disp in iter_math_spans(text, ranges):
        if last < start:
            pieces.append(text[last:start])
        seg = text[start:end]
        if not disp:
            seg = fix_span(seg, stats)
        pieces.append(seg)
        last = end
    pieces.append(text[last:])
    return ''.join(pieces), stats


def iter_zh_files():
    for letter in sorted(os.listdir(REPO)):
        d = os.path.join(REPO, letter)
        if not (len(letter) == 1 and letter.isalpha() and os.path.isdir(d)):
            continue
        for name in sorted(os.listdir(d)):
            if name.endswith('.md'):
                yield os.path.join(d, name)


def main():
    dry = '--dry' in sys.argv
    log = open(os.path.join(RESULTS, 'd9-trim-log.jsonl'), 'w', encoding='utf-8')
    files = 0
    total = 0
    for path in iter_zh_files():
        rel = os.path.relpath(path, REPO).replace('\\', '/')
        new_text, stats = process_file(path)
        if not stats:
            continue
        files += 1
        total += stats['trimmed']
        log.write(json.dumps({'f': rel, **stats}, ensure_ascii=False) + '\n')
        if not dry:
            open(path, 'w', encoding='utf-8', newline='').write(new_text)
    log.close()
    print(f'files: {files}, trimmed: {total}' + (' (dry run)' if dry else ''))


if __name__ == '__main__':
    main()
