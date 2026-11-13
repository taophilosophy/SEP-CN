# -*- coding: utf-8 -*-
"""021 探针：在 en/<slug>/index.html 中定位含 \`\\\\ \$\` 分裂形态的公式原文上下文。"""
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else 'en/logic-dynamic/index.html'
h = open(path, encoding='utf-8').read()

# 形态：LaTeX 命令后接反斜杠+空格+$(即 \<space>$ 或 \\<space>$)
for m in re.finditer(r'.{140}\\[ \t]*\$\$? *\$', h, re.S):
    print('---', m.start())
    print(repr(m.group(0)))
print('== count of backslash-dollar-like:', len(re.findall(r'\\[ \t]*\$\$? *\$', h)))
