# -*- coding: utf-8 -*-
r"""019 公式内文字清点：\text{}/\textrm{} 等内嵌文字，区分中文/英文/记号。"""
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
    r'operatorname\*?|hbox|mathrm)\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}')
CJK_RE = re.compile(r'[\u4e00-\u9fff]')


def main(mode='render-zh'):
    seq = load(os.path.join(RESULTS, f'{mode}.jsonl'))
    stats = collections.Counter()
    english = collections.Counter()
    per_file = collections.defaultdict(list)
    for f, items in seq.items():
        for kind, body in items:
            bare = strip_delims(kind, body)
            for m in TEXTCMD_RE.finditer(bare):
                inner = m.group(2).strip()
                if not inner:
                    continue
                if CJK_RE.search(inner):
                    stats['cjk'] += 1
                elif re.fullmatch(r'[A-Za-z]', inner):
                    stats['single-letter'] += 1
                elif re.fullmatch(r'[A-Za-z\\{}^_0-9\-\s,]{0,12}', inner):
                    stats['short-latin'] += 1
                    english[inner] += 1
                else:
                    stats['english-phrase'] += 1
                    english[inner] += 1
                    per_file[f].append(inner)
    print(mode, dict(stats))
    print('\n== 英文短语（需翻译）频次 top40')
    for text, n in english.most_common(40):
        print(f'  {n:4d}  {text[:80]}')
    print('\n== 含英文短语的文件 top10')
    for f, items in sorted(per_file.items(), key=lambda kv: -len(kv[1]))[:10]:
        print(f, len(items), items[:3])


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'render-zh')
