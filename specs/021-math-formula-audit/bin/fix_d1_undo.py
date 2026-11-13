# -*- coding: utf-8 -*-
r"""021 D1 撤销：把文本类命令内我引入的 $…$ 还原为 \(…\)。

教训：math-plugin 的保护正则先于 MathJax 配对定界符，\text{…$x$…} 会把
显示公式截断（站点渲染真值口径下不可用 $ 嵌套）。rules/02「公式内部用
LaTeX 记法，不适用本条」的深因即此。tag 剥壳保留（无定界符引入）。

用法: python -I fix_d1_undo.py
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')
sys.path.insert(0, HERE)
from expand_macros import fence_ranges, iter_math_spans  # noqa: E402
from fix_d1 import _text_command_ranges  # noqa: E402


def undo_span(span, stats):
    ranges = _text_command_ranges(span)
    if not ranges:
        return span
    chars = list(span)
    for start, end in ranges:
        seg = ''.join(chars[start:end])
        if '$' not in seg:
            continue
        out = []
        open_next = True
        i = 0
        while i < len(seg):
            ch = seg[i]
            if ch == '\\':
                out.append(seg[i:i + 2])
                i += 2
                continue
            if ch == '$':
                out.append('\\(' if open_next else '\\)')
                open_next = not open_next
                stats['undone'] += 1
                i += 1
                continue
            out.append(ch)
            i += 1
        chars[start:end] = out
    return ''.join(chars)


def main():
    log = open(os.path.join(RESULTS, 'd1-undo-log.jsonl'), 'w', encoding='utf-8')
    n_files = 0
    total = collections.Counter()
    for letter in sorted(os.listdir(REPO)):
        d = os.path.join(REPO, letter)
        if not (len(letter) == 1 and letter.isalpha() and os.path.isdir(d)):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith('.md'):
                continue
            path = os.path.join(d, name)
            rel = f'{letter}/{name}'
            text = open(path, encoding='utf-8').read()
            ranges = fence_ranges(text)
            stats = collections.Counter()
            pieces = []
            last = 0
            for start, end, disp in iter_math_spans(text, ranges):
                if last < start:
                    pieces.append(text[last:start])
                pieces.append(undo_span(text[start:end], stats))
                last = end
            pieces.append(text[last:])
            if not stats:
                continue
            n_files += 1
            total.update(stats)
            log.write(json.dumps({'f': rel, **stats}, ensure_ascii=False) + '\n')
            open(path, 'w', encoding='utf-8', newline='').write(''.join(pieces))
    log.close()
    print(f'files: {n_files}, undone: {dict(total)}')


if __name__ == '__main__':
    main()
