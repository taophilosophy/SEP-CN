# -*- coding: utf-8 -*-
r"""021 公式内文字翻译：只译连接语，专名/示例谓词/缩写保留（裁定 A4）。

作用面：数学段内 \text{} \textrm{} \mbox{} \textbf{} \textit{} \textsf{}
\texttt{} \textnormal{} \operatorname{} \hbox{} 的内容。
判定：内嵌串去空白后精确命中 CONNECTIVE_MAP 才替换（大小写敏感，含首字母
大写条目）；人名（Peter/Donald/Joe Biden）、示例谓词（Donkey/Farmer/toast）、
缩写（ST/MTL/DPL/PA/ASSIGN/diag）与书名法名不进表 → 保留。
纪律：幂等（译后为中文，不再命中）；逐处留痕 results/text-translate-log.jsonl。

用法: python -I translate_text_in_math.py [--dry]
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

TEXTCMD_RE = re.compile(
    r'\\(?:text|mbox|textnormal|textrm|textup|textbf|textit|textsf|texttt|'
    r'operatorname\*?|hbox)\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}')

CONNECTIVE_MAP = {
    'and': '且',
    'And': '且',
    'or': '或',
    'Or': '或',
    'not': '非',
    'Not': '非',
    'iff': '当且仅当',
    'if and only if': '当且仅当',
    'if, and only if,': '当且仅当',
    'if and only if,': '当且仅当',
    'if and only if for all realizations': '当且仅当对所有实现',
    'if one knows': '若知道',
    'one knows': '知道',
    'if': '若',
    'If': '若',
    'then': '则',
    'Then': '则',
    'else': '否则',
    'at': '在',
    'in': '在',
    'In': '在',
    'on': '在',
    'with': '与',
    'without': '不含',
    'for all': '对所有',
    'for every': '对每个',
    'for each': '对每个',
    'for': '对于',
    'For': '对于',
    'By': '由',
    'by': '由',
    'where': '其中',
    'when': '当',
    'whenever': '每当',
    'such that': '使得',
    'is true': '为真',
    'is false': '为假',
    'holds': '成立',
    'hold': '成立',
    'Dom': '定义域',
    'dom': '定义域',
    'range': '值域',
    'ground state': '基态',
    'spin up': '自旋向上',
    'spin down': '自旋向下',
    'provided that': '前提是',
    'provided': '前提是',
    'otherwise': '否则',
    'otherwise,': '否则，',
    'for large': '对大',
    'excited state': '激发态',
}


def translate_span(span, used):
    def repl(m):
        inner = m.group(1)
        core = inner.strip()
        if core not in CONNECTIVE_MAP:
            return m.group(0)
        idx = inner.find(core)
        new_inner = inner[:idx] + CONNECTIVE_MAP[core] + inner[idx + len(core):]
        used[(core, CONNECTIVE_MAP[core])] += 1
        return m.group(0)[:m.start(1) - m.start(0)] + new_inner + '}'

    return TEXTCMD_RE.sub(repl, span)


def process_file(path):
    text = open(path, encoding='utf-8').read()
    ranges = fence_ranges(text)
    used = collections.Counter()
    pieces = []
    last = 0
    for start, end, disp in iter_math_spans(text, ranges):
        if last < start:
            pieces.append(text[last:start])
        pieces.append(translate_span(text[start:end], used))
        last = end
    pieces.append(text[last:])
    return ''.join(pieces), used


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
    log = open(os.path.join(RESULTS, 'text-translate-log.jsonl'), 'w',
               encoding='utf-8')
    n_files = n = 0
    for path in iter_zh_files():
        rel = os.path.relpath(path, REPO).replace('\\', '/')
        new_text, used = process_file(path)
        if not used:
            continue
        n_files += 1
        n += sum(used.values())
        for (src, dst), cnt in used.items():
            log.write(json.dumps({'f': rel, 'from': src, 'to': dst,
                                  'count': cnt}, ensure_ascii=False) + '\n')
        if not dry:
            open(path, 'w', encoding='utf-8', newline='').write(new_text)
    log.close()
    print(f'files: {n_files}, translated text in math: {n}'
          + (' (dry run)' if dry else ''))


if __name__ == '__main__':
    main()
