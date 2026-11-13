# -*- coding: utf-8 -*-
r"""021 扫描：反斜杠被吞的痕迹（\frac→rac{、\right→ight) 等）。

只在数学段内判定，避免误伤英文单词。输出 results/bs-eaten.jsonl。
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

PATTERNS = {
    'frac': re.compile(r'(?<![\\A-Za-z])rac\s*\{'),
    'right': re.compile(r'(?<![\\A-Za-z])ight\s*[\)\]\}.|]'),
    'left': re.compile(r'(?<![\\A-Za-z])eft\s*[\(\[\{|]'),
    'rho': re.compile(r'(?<![\\A-Za-z])ho\b'),
    'rangle': re.compile(r'(?<![\\A-Za-z])angle\b'),
    'label': re.compile(r'(?<![\\A-Za-z])abel\s*\{'),
}


def main():
    out = open(os.path.join(RESULTS, 'bs-eaten.jsonl'), 'w', encoding='utf-8')
    total = collections.Counter()
    files = collections.Counter()
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
            for start, end, disp in iter_math_spans(text, ranges):
                span = text[start:end]
                for key, pat in PATTERNS.items():
                    for m in pat.finditer(span):
                        total[key] += 1
                        files[rel] += 1
                        out.write(json.dumps(
                            {'f': rel, 'kind': key,
                             'x': span[max(0, m.start() - 50):m.end() + 30]},
                            ensure_ascii=False) + '\n')
    out.close()
    print('counts:', dict(total))
    print('files:', len(files), 'total hits:', sum(total.values()))
    for f, n in files.most_common(15):
        print(f'  {n:3d}  {f}')


if __name__ == '__main__':
    main()
