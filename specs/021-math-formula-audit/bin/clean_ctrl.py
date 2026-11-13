# -*- coding: utf-8 -*-
r"""021 修复：清除译文文件里的控制字符残留（\x01 \x02 \x03）。

来源：expand_macros v1 的行内代码掩码（CODE_MASK='\x01' + '\x02N\x03'）在
还原时只还原了 \x02N\x03，遗留 \x01，进入 md 后使 MathJax 崩溃
（Cannot read properties of null）。本脚本逐文件清除并留痕。

用法: python -I clean_ctrl.py [--dry]
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')
CTRL = {'\x01': 'SOH', '\x02': 'STX', '\x03': 'ETX'}


def main():
    dry = '--dry' in sys.argv
    log = open(os.path.join(RESULTS, 'ctrl-clean-log.jsonl'), 'w', encoding='utf-8')
    files = 0
    total = 0
    for letter in sorted(os.listdir(REPO)):
        d = os.path.join(REPO, letter)
        if not (len(letter) == 1 and letter.isalpha() and os.path.isdir(d)):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith('.md'):
                continue
            path = os.path.join(d, name)
            text = open(path, encoding='utf-8').read()
            if not any(c in text for c in CTRL):
                continue
            cnt = collections.Counter(ch for ch in text if ch in CTRL)
            files += 1
            total += sum(cnt.values())
            log.write(json.dumps({'f': f'{letter}/{name}',
                                  'counts': {CTRL[k]: v for k, v in cnt.items()}},
                                 ensure_ascii=False) + '\n')
            if not dry:
                for c in CTRL:
                    text = text.replace(c, '')
                open(path, 'w', encoding='utf-8', newline='').write(text)
    log.close()
    print(f'files: {files}, control chars removed: {total}'
          + (' (dry run)' if dry else ''))


if __name__ == '__main__':
    main()
