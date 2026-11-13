# -*- coding: utf-8 -*-
r"""021 宏表解析：从各词条 local.js 提取 MathJax.TeX.Macros 定义。

支持两种写法：
  name: "替换文本"                 （零参）
  name: ["替换文本含 #1..#n", n]    （带参，n 为参数个数）

数学段展开由 expand_macros.py 消费；本文件只负责解析与汇总。
产 results/macro-table.json: {slug: {name: {"tmpl": str, "n": int}}}，
并兼容零参简写为字符串（调用方统一走 dict 形式）。
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')
MACRO_DIR = os.path.join(REPO, 'state', 'mathval', 'macros')

KEY_RE = re.compile(r'([A-Za-z][A-Za-z0-9_]*)\s*:\s*')
# 支持双引号与单引号 JS 字符串（logic-propositional 等词条用单引号）
STR_RE = re.compile(r'''(["'])((?:[^"'\\]|\\[\s\S])*?)\1''')
NUM_RE = re.compile(r'\s*,\s*(\d+)\s*\]')


def _unescape(val):
    return val.replace('\\\\', '\x00').replace('\\"', '"').replace('\x00', '\\')


def _extract_object_block(text, start):
    """从 start 后第一个 { 起，按引号感知配平花括号，返回块内文本。"""
    i = text.find('{', start)
    if i < 0:
        return None
    depth = 0
    j = i
    in_str = False
    while j < len(text):
        ch = text[j]
        if in_str:
            if ch == '\\':
                j += 2
                continue
            if ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    return text[i + 1:j]
        j += 1
    return None


def parse_macros(text):
    m = re.search(r'(?i)\bMacros\s*:', text)
    if not m:
        return {}
    body = _extract_object_block(text, m.end())
    if body is None:
        return {}
    out = {}
    pos = 0
    while True:
        km = KEY_RE.search(body, pos)
        if not km:
            break
        name = km.group(1)
        rest = body[km.end():]
        if rest.startswith('['):
            am = re.match(r'''\[\s*(["'])((?:[^"'\\]|\\[\s\S])*?)\1''', rest)
            if not am:
                pos = km.end()
                continue
            tmpl = _unescape(am.group(2))
            nm = NUM_RE.match(rest, am.end())
            nargs = int(nm.group(1)) if nm else tmpl.count('#')
            out[name] = {'tmpl': tmpl, 'n': nargs}
            pos = km.end() + (nm.end() if nm else am.end())
        else:
            sm = STR_RE.match(rest.lstrip())
            if not sm:
                pos = km.end()
                continue
            out[name] = {'tmpl': _unescape(sm.group(2)), 'n': 0}
            pos = km.end() + (len(rest) - len(rest.lstrip())) + sm.end()
    return out


def main():
    table = {}
    if os.path.isdir(MACRO_DIR):
        for name in sorted(os.listdir(MACRO_DIR)):
            if not name.endswith('.js'):
                continue
            slug = name[:-3]
            text = open(os.path.join(MACRO_DIR, name), encoding='utf-8',
                        errors='replace').read()
            macros = parse_macros(text)
            if macros:
                table[slug] = macros
    json.dump(table, open(os.path.join(RESULTS, 'macro-table.json'), 'w',
                          encoding='utf-8'), ensure_ascii=False, indent=1,
              sort_keys=True)
    names = collections.Counter()
    param = 0
    for slug, macros in table.items():
        for k, spec in macros.items():
            names[k] += 1
            if spec['n']:
                param += 1
    print('entries with macros:', len(table), 'distinct macros:', len(names),
          'parameterized defs:', param)
    for k, n in names.most_common(12):
        spec = next(m for s in table.values() for kk, m in s.items() if kk == k)
        print(f"  {k:10s} {n:3d}  n={spec['n']}  {spec['tmpl'][:60]!r}")


if __name__ == '__main__':
    main()
