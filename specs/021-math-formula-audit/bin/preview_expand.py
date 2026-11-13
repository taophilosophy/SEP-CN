# -*- coding: utf-8 -*-
r"""021 展开预览：打印指定文件展开前后的数学段差异（不写盘）。"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')
sys.path.insert(0, HERE)
from expand_macros import process_file  # noqa: E402


def main():
    table = json.load(open(os.path.join(RESULTS, 'macro-table.json'),
                           encoding='utf-8'))
    for rel in sys.argv[1:]:
        path = os.path.join(REPO, rel)
        slug = os.path.basename(rel)[:-3].split('.')[0]
        macros = table.get(slug, {})
        if not macros:
            print(f'{rel}: 无宏表')
            continue
        old = open(path, encoding='utf-8').read()
        new, used = process_file(path, macros)
        print(f'===== {rel}  macros={list(macros)[:8]}  used={dict(used)}')
        if old == new:
            print('  （无变化）')
            continue
        # 打印变化行
        ol, nl = old.split('\n'), new.split('\n')
        shown = 0
        for i, (a, b) in enumerate(zip(ol, nl)):
            if a != b:
                print(f'  L{i+1} 前: {a[:150]}')
                print(f'  L{i+1} 后: {b[:150]}')
                shown += 1
                if shown >= 4:
                    break


if __name__ == '__main__':
    main()
