# -*- coding: utf-8 -*-
r"""019 定量：译文公式内的中文标点/零宽/异常字符分类计数。"""
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
    r'\\(?:text|mbox|textnormal|textrm|textup|textbf|textit|textsf|texttt|'
    r'operatorname\*?|hbox)\s*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}')
PUNCT = '（）【】《》「」『』，。；：？！、“”‘’—…·'


def main():
    zh = load(os.path.join(RESULTS, 'render-zh.jsonl'))
    cnt = collections.Counter()
    per_file = collections.defaultdict(collections.Counter)
    for f, seq in zh.items():
        for kind, body in seq:
            bare = TEXTCMD_RE.sub('', strip_delims(kind, body))
            for ch in bare:
                if ch in PUNCT or ch in '\u200b\u200c\u200d\ufeff\u00a0':
                    cnt[ch] += 1
                    per_file[f][ch] += 1
    print('char counts:', {repr(k): v for k, v in cnt.most_common(20)})
    print('\nfiles (top):')
    for f, c in sorted(per_file.items(), key=lambda kv: -sum(kv[1].values()))[:12]:
        print(f, sum(c.values()), {repr(k): v for k, v in c.most_common(6)})


if __name__ == '__main__':
    main()
