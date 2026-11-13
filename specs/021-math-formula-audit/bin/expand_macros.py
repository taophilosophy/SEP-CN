# -*- coding: utf-8 -*-
r"""021 宏展开器 v2：按各词条 local.js 宏表把 \macro 就地展开为纯 LaTeX。

裁定 A3（2026-11-13）：站点 MathJax 3 无 SEP 宏表，译文须自包含。
支持零参与带参宏（["模板含 #1..#n", n]，花括号配平取参）。

纪律（rules/05 批量改写）：
  * 幂等：重复运行不再改变产物；
  * 逐处留痕：results/macro-expand-log.jsonl 记 {f, macro, count}；
  * 只在数学段（$…$ / $$…$$）内展开，围栏代码块整段跳过；行内反引号
    不做掩码（TeX 反引号是合法开引号，v1 掩码曾破坏公式段定位）；
  * 展开到不动点（宏值可引用表中其他宏），上限 10 轮；
  * 只展开表内宏，不猜、不造。

用法:
  python -I expand_macros.py --dry     # 只报告，不写盘
  python -I expand_macros.py           # 写盘
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')

FENCE_RE = re.compile(r'(```|~~~)[^\n]*\n(?:[\s\S]*?\n\1[^\n]*|[\s\S]*$)')


def fence_ranges(text):
    return [m.span() for m in FENCE_RE.finditer(text)]


def in_ranges(pos, ranges):
    return any(a <= pos < b for a, b in ranges)


def iter_math_spans(text, ranges):
    """产出 (start, end, is_display) 数学段。$ 转义（\\$）不参与。"""
    n = len(text)
    i = 0
    while i < n:
        ch = text[i]
        if ch == '\\':
            i += 2
            continue
        if ch != '$' or in_ranges(i, ranges):
            i += 1
            continue
        if i + 1 < n and text[i + 1] == '$':
            close = text.find('$$', i + 2)
            if close < 0:
                i += 2
                continue
            yield i, close + 2, True
            i = close + 2
            continue
        # 单 $：内容允许换行但不允许空行；内容不含未转义 $
        j = i + 1
        while j < n:
            cj = text[j]
            if cj == '\\':
                j += 2
                continue
            if cj == '$':
                break
            if cj == '\n' and text[j:j + 3] == '\n\n':
                break
            j += 1
        if j < n and text[j] == '$' and j > i + 1:
            yield i, j + 1, False
            i = j + 1
        else:
            i += 1


def _read_args(text, pos, k):
    """从 pos 起读 k 个 TeX 参数：{…}（配平）或单 token。返回 (args, end)。"""
    args = []
    i = pos
    n = len(text)
    while len(args) < k:
        while i < n and text[i] in ' \t\n':
            i += 1
        if i >= n:
            return None, pos
        if text[i] == '{':
            depth = 0
            j = i
            while j < n:
                if text[j] == '\\':
                    j += 2
                    continue
                if text[j] == '{':
                    depth += 1
                elif text[j] == '}':
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if depth != 0:
                return None, pos
            args.append(text[i + 1:j])
            i = j + 1
        elif text[i] == '\\':
            m = re.match(r'\\[a-zA-Z]+|\\.', text[i:])
            if not m:
                return None, pos
            args.append(m.group(0))
            i += m.end()
        else:
            args.append(text[i])
            i += 1
    return args, i


def _substitute(tmpl, args):
    out = tmpl
    for idx in range(len(args), 0, -1):
        out = out.replace(f'#{idx}', args[idx - 1])
    return out


def expand_once(cur, specs, used):
    """单向扫描：命中宏名后自行消费参数（sub 只换宏名不吞参数，v2 曾重复输出）。"""
    if not specs:
        return cur
    pat = re.compile(r'\\(?:' + '|'.join(re.escape(nm) for nm, _ in specs)
                     + r')(?![a-zA-Z])')
    spec_map = dict(specs)
    out = []
    i = 0
    while True:
        m = pat.search(cur, i)
        if not m:
            break
        name = m.group(0)[1:]
        spec = spec_map[name]
        tmpl = spec['tmpl'] if isinstance(spec, dict) else spec
        nargs = spec['n'] if isinstance(spec, dict) else 0
        if nargs == 0:
            out.append(cur[i:m.start()])
            out.append(tmpl)
            used[name] += 1
            i = m.end()
            continue
        args, end = _read_args(cur, m.end(), nargs)
        if args is None:
            out.append(cur[i:m.end()])
            i = m.end()
            continue
        out.append(cur[i:m.start()])
        out.append(_substitute(tmpl, args))
        used[name] += 1
        i = end
    out.append(cur[i:])
    return ''.join(out)


def expand_span(span, macros, used):
    """单个数学段内展开到不动点（宏值可引用表中其他宏）。"""
    cur = span
    specs = sorted(macros.items(), key=lambda kv: -len(kv[0]))
    for _ in range(10):
        new = expand_once(cur, specs, used)
        if new == cur:
            break
        cur = new
    return cur


def process_file(path, macros):
    text = open(path, encoding='utf-8').read()
    ranges = fence_ranges(text)
    used = collections.Counter()
    pieces = []
    last = 0
    for start, end, disp in iter_math_spans(text, ranges):
        if last < start:
            pieces.append(text[last:start])
        pieces.append(expand_span(text[start:end], macros, used))
        last = end
    pieces.append(text[last:])
    return ''.join(pieces), used


def iter_zh_files():
    for letter in sorted(os.listdir(REPO)):
        d = os.path.join(REPO, letter)
        if not (len(letter) == 1 and letter.isalpha() and os.path.isdir(d)):
            continue
        for name in sorted(os.listdir(d)):
            if name.endswith('.md'):
                yield os.path.join(d, name)


def main():
    dry = '--dry' in sys.argv
    table = json.load(open(os.path.join(RESULTS, 'macro-table.json'),
                           encoding='utf-8'))
    log = open(os.path.join(RESULTS, 'macro-expand-log.jsonl'), 'w',
               encoding='utf-8')
    n_files = n_changes = 0
    for path in iter_zh_files():
        rel = os.path.relpath(path, REPO).replace('\\', '/')
        base = os.path.basename(path)[:-3]
        slug = base.split('.')[0]
        macros = table.get(slug)
        if not macros:
            continue
        new_text, used = process_file(path, macros)
        if not used:
            continue
        n_files += 1
        n_changes += sum(used.values())
        for name, cnt in used.items():
            spec = macros[name]
            log.write(json.dumps({'f': rel, 'macro': name,
                                  'to': spec['tmpl'] if isinstance(spec, dict)
                                  else spec, 'n': spec.get('n', 0)
                                  if isinstance(spec, dict) else 0,
                                  'count': cnt}, ensure_ascii=False) + '\n')
        if not dry:
            open(path, 'w', encoding='utf-8', newline='').write(new_text)
    log.close()
    print(f'files touched: {n_files}, macro replacements: {n_changes}'
          + (' (dry run)' if dry else ''))


if __name__ == '__main__':
    main()
