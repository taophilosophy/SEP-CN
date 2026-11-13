# -*- coding: utf-8 -*-
r"""021 预览：公式内文字翻译前后对照（不写盘）。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
from translate_text_in_math import process_file  # noqa: E402


def main():
    for rel in sys.argv[1:]:
        path = os.path.join(REPO, rel)
        old = open(path, encoding='utf-8').read()
        new, used = process_file(path)
        print(f'===== {rel} {dict(used)}')
        ol, nl = old.split('\n'), new.split('\n')
        shown = 0
        for i, (a, b) in enumerate(zip(ol, nl)):
            if a != b:
                # 只打印差异片段
                print(f'  L{i+1}: {b[:160]}')
                shown += 1
                if shown >= 3:
                    break


if __name__ == '__main__':
    main()
