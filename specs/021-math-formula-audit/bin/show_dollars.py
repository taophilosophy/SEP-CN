# -*- coding: utf-8 -*-
r"""021 辅助：列出文件内所有 $ 的位置与上下文，供逐处判定货币/公式。"""
import sys

path = sys.argv[1]
text = open(path, encoding='utf-8').read()
for i, line in enumerate(text.split('\n'), 1):
    if '$' not in line:
        continue
    print(f'L{i}:')
    j = 0
    while True:
        j = line.find('$', j)
        if j < 0:
            break
        print('   …', line[max(0, j - 45):j + 45].replace('\n', ' '))
        j += 1
