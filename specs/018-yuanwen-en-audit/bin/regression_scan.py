# -*- coding: utf-8 -*-
"""018 重转回归扫描器：重转前后 yuanwen 逐文件逐行差异分类。

差异只允许落入三类预期（specs/018 spec.md A4）：
  BR    — 引块内 <br> 行结构还原：1 行 → 多行 `> ` 引行，拼回后无空格差
  SPACE — em/strong 标签内空白外移：两侧去空格后逐字符一致
  STAR  — 纯 <b> 转 md 粗体：两侧去空格去星号后一致
出现任何 OTHER 类差异 = 转换器行为漂移（含手修被覆盖、内容丢失），
必须逐条查明后才允许收口。文件级增删单独计数。

用法: python specs/018-yuanwen-en-audit/bin/regression_scan.py <备份目录> <现行目录>
输出: stdout 摘要；明细 JSON 落 specs/018-yuanwen-en-audit/results/。
"""
import json
import os
import re
import sys

IMG_EXT = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.pdf')


def nospace(s):
    return s.replace(' ', '')


def nostar(s):
    return s.replace('*', '').replace(' ', '')


QUOTE_PREFIX_RE = re.compile(r'^(?:>[ \t]*)+')


ASCII_WS = ' \t\r\n\f\v'


def collapse_quotes(lines):
    """连续 `>` 引行（含嵌套）折叠为单行，空引行为引内段界；两侧同法归一。
    仅去 ASCII 空白：`\\xa0`（&nbsp; 缩进）是正文内容，参与比较。"""
    out, buf = [], []
    for ln in lines:
        ln = ln.rstrip(ASCII_WS)
        if ln.startswith('>'):
            t = QUOTE_PREFIX_RE.sub('', ln).strip(ASCII_WS)
            if t:
                buf.append(t)
            elif buf:
                out.append(' '.join(buf))
                buf = []
        else:
            if buf:
                out.append(' '.join(buf))
                buf = []
            out.append(ln)
    if buf:
        out.append(' '.join(buf))
    return out


def file_verdict(old_lines, new_lines):
    """整文件归一链：引块折叠（BR 类）→ 去星去空格（SPACE/STAR 类）。仍不等=OTHER。"""
    a = collapse_quotes(old_lines)
    b = collapse_quotes(new_lines)
    if a == b:
        return 'BR'
    if ''.join(nostar(x) for x in a) == ''.join(nostar(x) for x in b):
        return 'SPACE-STAR'
    return 'OTHER'


def char_delta(a, b, span=90):
    """OTHER 明细：在归一文本上定位首处真实差异（非对齐假象）。"""
    sa = ''.join(nostar(x) for x in a)
    sb = ''.join(nostar(x) for x in b)
    i = 0
    while i < min(len(sa), len(sb)) and sa[i] == sb[i]:
        i += 1
    return sa[max(0, i - span):i + span], sb[max(0, i - span):i + span]


def scan_tree(old_root, new_root):
    files_old, files_new = {}, {}
    for root, dirs, names in os.walk(old_root):
        for n in names:
            if n.endswith('.md'):
                p = os.path.join(root, n)
                files_old[os.path.relpath(p, old_root).replace('\\', '/')] = p
    for root, dirs, names in os.walk(new_root):
        for n in names:
            if n.endswith('.md'):
                p = os.path.join(root, n)
                files_new[os.path.relpath(p, new_root).replace('\\', '/')] = p

    verdicts = {'BR': 0, 'SPACE-STAR': 0, 'OTHER': 0}
    other_details, added, removed = [], [], []
    unchanged = 0
    all_files = sorted(set(files_old) | set(files_new))
    for rel in all_files:
        if rel not in files_old:
            added.append(rel)
            continue
        if rel not in files_new:
            removed.append(rel)
            continue
        with open(files_old[rel], encoding='utf-8') as fh:
            old = fh.read().splitlines()
        with open(files_new[rel], encoding='utf-8') as fh:
            new = fh.read().splitlines()
        if old == new:
            unchanged += 1
            continue
        cls = file_verdict(old, new)
        verdicts[cls] += 1
        if cls == 'OTHER':
            a = collapse_quotes(old)
            b = collapse_quotes(new)
            o, n = char_delta(a, b)
            other_details.append({'file': rel, 'old': [o], 'new': [n]})
    return {'verdicts': verdicts, 'unchanged': unchanged, 'added': added,
            'removed': removed, 'other_details': other_details,
            'total_files': len(all_files)}


def main(argv):
    if len(argv) != 2:
        print('用法: regression_scan.py <备份目录> <现行目录>')
        return 2
    rep = scan_tree(argv[0], argv[1])
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(here, 'results', 'regression-scan-20261113.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as fh:
        json.dump(rep, fh, ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in rep.items() if k != 'other_details'},
                     ensure_ascii=False))
    print('OTHER 条数: %d（明细见 %s）' % (len(rep['other_details']), out))
    return 1 if (rep['other_details'] or rep['added'] or rep['removed']) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
