# -*- coding: utf-8 -*-
r"""021 维护脚本：把战役目录内残留的旧编号路径替换为新编号。"""
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
OLD = '021-math-formula-audit'
NEW = '021-math-formula-audit'
changed = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    for name in filenames:
        if not name.endswith(('.py', '.mjs', '.js', '.md', '.json')):
            continue
        path = os.path.join(dirpath, name)
        try:
            text = open(path, encoding='utf-8').read()
        except UnicodeDecodeError:
            continue
        if OLD in text:
            open(path, 'w', encoding='utf-8').write(text.replace(OLD, NEW))
            changed.append(os.path.relpath(path, ROOT))
print('updated:', len(changed))
for c in changed:
    print('  ', c)
