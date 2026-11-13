# -*- coding: utf-8 -*-
r"""021 D1 归一：显示/行内公式内的 \(…\) 统一为家法记法。

裁定口径（rules/02：真公式一律 $…$；站点只按 $/$$/\(\)/\[\] 配 delimiter，
但库内体例统一）：
  * 文本类命令（\text \textrm \mbox \textbf \textit \textsf \texttt
    \textnormal \hbox …）内：\( → $ ，\) → $（数学段内文本中的内联数学）
  * \tag{\(X\)} 内：去掉冗余定界符（tag 内容本就是数学模式）
只处理数学段内，围栏代码块跳过；逐处留痕、幂等。

用法: python -I fix_d1.py [--dry]
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

TEXTCMD_OPEN_RE = re.compile(
    r'\\(?:text|textrm|mbox|textnormal|textbf|textit|textsf|texttt|textup|hbox)'
    r'\s*\{')
TAG_RE = re.compile(r'\\tag\*?\s*\{\s*\\\((.+?)\\\)\s*\}')


def _text_command_ranges(span):
    """返回 span 内文本类命令花括号内容区间（配平）。"""
    out = []
    i = 0
    n = len(span)
    while True:
        m = TEXTCMD_OPEN_RE.search(span, i)
        if not m:
            break
        start = m.end() - 1  # '{' 位置
        depth = 0
        j = start
        while j < n:
            ch = span[j]
            if ch == '\\':
                j += 2
                continue
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        out.append((start + 1, j))
        i = m.end()
    return out


def fix_span(span, stats):
    # 1) \tag{\(X\)} → \tag{X}
    def tag_repl(m):
        stats['tag'] += 1
        return '\\tag{' + m.group(1) + '}'

    cur = TAG_RE.sub(tag_repl, span)
    # 2) 文本类命令内 \( → $ ，\) → $
    ranges = _text_command_ranges(cur)
    if not ranges:
        return cur
    chars = list(cur)
    for start, end in ranges:
        seg = ''.join(chars[start:end])
        if '\\(' not in seg and '\\)' not in seg:
            continue
        new = seg.replace('\\(', '$').replace('\\)', '$')
        stats['text_inline'] += (seg.count('\\(') + seg.count('\\)')) // 2
        chars[start:end] = list(new)
    return ''.join(chars)


def process_file(path):
    text = open(path, encoding='utf-8').read()
    ranges = fence_ranges(text)
    stats = collections.Counter()
    pieces = []
    last = 0
    for start, end, disp in iter_math_spans(text, ranges):
        if last < start:
            pieces.append(text[last:start])
        pieces.append(fix_span(text[start:end], stats))
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
    log = open(os.path.join(RESULTS, 'd1-normalize-log.jsonl'), 'w',
               encoding='utf-8')
    n_files = 0
    total = collections.Counter()
    for path in iter_zh_files():
        rel = os.path.relpath(path, REPO).replace('\\', '/')
        new_text, stats = process_file(path)
        if not stats:
            continue
        n_files += 1
        total.update(stats)
        log.write(json.dumps({'f': rel, **stats}, ensure_ascii=False) + '\n')
        if not dry:
            open(path, 'w', encoding='utf-8', newline='').write(new_text)
    log.close()
    print(f'files: {n_files}, {dict(total)}' + (' (dry run)' if dry else ''))


if __name__ == '__main__':
    main()
