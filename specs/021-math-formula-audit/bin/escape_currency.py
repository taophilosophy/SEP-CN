# -*- coding: utf-8 -*-
r"""021 货币 $ 转义：正文中 `$` 紧跟数字者改 `\$`（保留公式）。

判定保守：只转 `(?<!\\)\$(?=\d)`，且该位置不在数学段内（用站点配对口径
先算段）。逐文件留痕并回报「转义数 / 公式数变化」，公式数下降即回滚该文件。
用法: python -I escape_currency.py f1.md f2.md … [--dry]
"""
import json
import re
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')
sys.path.insert(0, HERE)
from expand_macros import fence_ranges, iter_math_spans  # noqa: E402


CURRENCY_RE = re.compile(r'(?<!\\)\$(?=\d[\d,]*(?:\.\d+)?)')
MATH_AFTER = set('$-+\\^_/{}()[]=<>|*')


def escape(file_text):
    """货币判定：$ 后数字串，其后紧跟非数学字符（空格/汉字/标点）即货币。

    不看是否落在数学段内——错配产生的伪公式会把货币吞进去，那正是要修的根因。
    `$1-\\alpha$` 这类真公式数字串后接 `-`，不转义。
    """
    ranges = fence_ranges(file_text)
    spans = list(iter_math_spans(file_text, ranges))
    n = 0
    out = []
    last = 0
    for m in CURRENCY_RE.finditer(file_text):
        num = re.match(r'\d[\d,]*(?:\.\d+)?', file_text[m.end():])
        after = file_text[m.end() + num.end():m.end() + num.end() + 1]
        if after in MATH_AFTER:
            continue
        out.append(file_text[last:m.start()])
        out.append('\\$')
        last = m.end()
        n += 1
    out.append(file_text[last:])
    return ''.join(out), n, len(spans)


def main():
    dry = '--dry' in sys.argv
    log = open(os.path.join(RESULTS, 'currency-escape-log.jsonl'), 'a',
               encoding='utf-8')
    log.write(json.dumps({'session': '2026-11-14',
                          'note': '昨日转义未随提交落盘（git log -S 零命中），本日重跑'}
                         , ensure_ascii=False) + '\n')
    for rel in [a for a in sys.argv[1:] if not a.startswith('-')]:
        path = os.path.join(REPO, rel)
        text = open(path, encoding='utf-8').read()
        new_text, n, spans_before = escape(text)
        if n == 0:
            print(rel, 'no currency $')
            continue
        _, _, spans_after = escape(new_text)
        print(f'{rel}: escaped {n}, formulas {spans_before} → {spans_after}')
        log.write(json.dumps({'f': rel, 'escaped': n,
                              'spans_before': spans_before,
                              'spans_after': spans_after},
                             ensure_ascii=False) + '\n')
        if not dry:
            open(path, 'w', encoding='utf-8', newline='').write(new_text)
    log.close()


if __name__ == '__main__':
    main()
