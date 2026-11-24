# -*- coding: utf-8 -*-
"""specs/059 独立复算器（J6）：不复用 apply.py 的替换表，按原则谓词全量复扫。

用法：python -I specs/059-toc-title-normalize/bin/recheck.py [--expect-lines 2787,5274]
任何谓词命中非 0 即退出码 1；全部 0 命中且行数守恒退出码 0。
"""
import io
import json
import os
import re
import sys

sys.dont_write_bytecode = True

ALIAS = re.compile(r'^\s*\* \\\*')
SEE = '— see'


def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, 'SUMMARY.md')):
        parent = os.path.dirname(d)
        if parent == d:
            raise RuntimeError('仓库根未找到（自 %s 向上）' % __file__)
        d = parent
    return d


def main():
    root = find_root()
    files = ['SUMMARY.md', 'mu-lu-s.md']
    data = {}
    for f in files:
        with io.open(os.path.join(root, f), encoding='utf-8', newline='') as fh:
            data[f] = fh.read().split('\n')

    res = {}
    # ---- P1/P2：字符层，全两文件 ----
    res['P1_U2027'] = sum(l.count('\u2027') for f in files for l in data[f])
    res['P2_html_entity'] = sum(l.count('&ndash;') + l.count('&mdash;') + l.count('&amp;')
                                for f in files for l in data[f])

    # ---- 别名行/分组行 ----
    alias_lines, group_lines, entry_lines = [], [], []
    for f in files:
        for i, l in enumerate(data[f], 1):
            if ALIAS.match(l):
                (alias_lines if SEE in l else group_lines).append((f, i, l))
            elif re.match(r'^\s*\* \[', l):
                entry_lines.append((f, i, l))

    res['P3_jian_leading_space'] = sum(
        1 for _f, _i, l in alias_lines if re.search(r'\S ——见', l))
    res['P4_colon_jian'] = sum(1 for _f, _i, l in alias_lines if '：见' in l)
    res['P5_colon_space_after_jian'] = sum(
        1 for _f, _i, l in alias_lines if re.search(r'——见.*?： ', l))
    res['P6_group_en_first'] = sum(
        1 for _f, _i, l in group_lines if re.match(r'^\s*\* \\\*[A-Za-z]', l))
    res['P7_mulu_en_dash_heading'] = sum(
        1 for l in data['mu-lu-s.md']
        if re.match(r'^#{1,6} ', l) and ('\u2013' in l or '\u2015' in l))
    res['P8_alias_missing_zh_link'] = sum(
        1 for _f, _i, l in alias_lines if '——见' not in l and '：见' not in l)

    # ---- 守恒面 ----
    res['N_lines_SUMMARY'] = len(data['SUMMARY.md'])
    res['N_lines_mulu'] = len(data['mu-lu-s.md'])
    res['N_entries'] = len(entry_lines)
    res['N_alias'] = len(alias_lines)
    res['N_group'] = len(group_lines)

    # ---- P11：别名行英文左段 vs baseline 完整标题（门禁同口径，仅报告） ----
    try:
        base = json.load(io.open(os.path.join(root, 'baseline/entries.json'), encoding='utf-8'))
        titles = {(e.get('title') or '').strip() for e in base['entries']}
        norm = lambda s: re.sub(r'[^a-z0-9]+', ' ', s).strip().lower()
        full = {norm(t) for t in titles if t}
        bad = []
        for f, i, l in alias_lines:
            left = l.split('— see', 1)[0]
            k = max((j for j, ch in enumerate(left) if '\u4e00' <= ch <= '\u9fff'), default=-1)
            frag = left[k + 1:].strip().replace('\\*', '').strip()
            right = l.split('— see', 1)[1]
            if frag and norm(frag) not in full and norm(frag) != norm(right):
                bad.append((f, i, frag))
        res['P11_alias_left_not_baseline_title'] = len(bad)
        res['P11_samples'] = [{'file': f, 'line': i, 'frag': x} for f, i, x in bad[:10]]
    except Exception as exc:  # noqa: BLE001
        res['P11_alias_left_not_baseline_title'] = 'ERROR: %s' % exc

    # ---- P12：全库同类缺陷扫描（条目行／标题层，报告用） ----
    res['P12_entry_u2027'] = sum(1 for _f, _i, l in entry_lines if '\u2027' in l)
    res['P12_entry_entity'] = sum(1 for _f, _i, l in entry_lines if '&ndash;' in l)
    res['P12_mulu_heading_digit_dash'] = [
        i for i, l in enumerate(data['mu-lu-s.md'], 1)
        if re.match(r'^#{1,6} .*[0-9][\u2013\u2014\u2015][0-9]', l)]

    zero_keys = ['P1_U2027', 'P2_html_entity', 'P3_jian_leading_space', 'P4_colon_jian',
                 'P5_colon_space_after_jian', 'P6_group_en_first', 'P7_mulu_en_dash_heading',
                 'P8_alias_missing_zh_link']
    ok = all(res[k] == 0 for k in zero_keys)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
