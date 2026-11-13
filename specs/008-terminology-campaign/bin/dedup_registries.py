# -*- coding: utf-8 -*-
"""两册同人/同词重复合并（ADR-0036 后续，2026-11-13）。

口径（用户裁定）：
  * 人名表：同人重复合并为一行，键形以「倒装键」为主，并自然语序/拼写变体为别名形；
  * 术语表：只并纯变体（单复数、连字符、变音符拼写），带语域括注的多义分工行不动；
  * 冗余行删除，保留行依据列记「重复行合并（旧键 …）」并更新裁定日期。

用法:
  python specs/008-terminology-campaign/bin/dedup_registries.py dry    # 干跑出清单
  python specs/008-terminology-campaign/bin/dedup_registries.py apply  # 写回（守恒门）
"""
import collections
import difflib
import io
import json
import re
import sys
import unicodedata

ROOT = '.'
PERSON = 'ren-ming-biao.md'
TERM = 'shu-yu-biao.md'
REPORT = 'specs/008-terminology-campaign/results/dedup-2026-11-13.json'
DATE = '2026-11-13'
PART = {'of', 'de', 'van', 'von', 'der', 'al', 'ibn', 'bin', 'du', 'le', 'la',
        'di', 'da', 'del', 'den', 'the', 'st'}


def fold(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    for ch in 'ʿʾʻʼ':
        s = s.replace(ch, '')
    return re.sub(r'\s+', ' ', s).strip().casefold()


def squash(s):
    return re.sub(r'[^a-z0-9]+', '', fold(s))


def toks(k):
    return frozenset(t for t in fold(k).replace(',', ' ').split()
                     if t and t not in PART)


def main_zh(t):
    return re.split(r'（|\(|；|;', t)[0].strip()


def load(path):
    lines = io.open(path, encoding='utf-8', newline='').read().split('\n')
    rows = []
    for i, line in enumerate(lines):
        if not line.startswith('|'):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 3 or not c[0] or set(c[0]) <= set(':-: '):
            continue
        rows.append({'idx': i, 'cells': c})
    return lines, rows


def inverted(key):
    k = key.split(' / ')[0]
    return ',' in k


def is_deprecated(cells):
    return '已废弃' in cells[2]


def cluster_person(rows):
    tk = [toks(r['cells'][0]) if not is_deprecated(r['cells']) else frozenset()
          for r in rows]
    zh = [main_zh(r['cells'][2]) for r in rows]
    par = list(range(len(rows)))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    def uni(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            par[ra] = rb

    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            a, b = tk[i], tk[j]
            if not a or not b:
                continue
            if a == b:
                uni(i, j)
                continue
            if zh[i] != zh[j]:
                continue
            big, small = (a, b) if len(a) >= len(b) else (b, a)
            if sorted(big)[-1] != sorted(small)[-1]:
                continue
            gbig, gsmall = big - {sorted(big)[-1]}, small - {sorted(small)[-1]}
            if gbig & gsmall:
                uni(i, j)
                continue
            if gbig and gsmall:
                x, y = sorted(gbig)[0], sorted(gsmall)[0]
                if difflib.SequenceMatcher(None, x, y).ratio() > 0.8:
                    uni(i, j)
    groups = collections.defaultdict(list)
    for i in range(len(rows)):
        groups[find(i)].append(i)
    return [v for v in groups.values() if len(v) > 1]


def cluster_term(rows):
    groups = collections.defaultdict(list)
    for i, r in enumerate(rows):
        key = r['cells'][0]
        if '（' in key or '(' in key or is_deprecated(r['cells']):
            continue                      # 语域分工行与废弃行不参与
        groups[re.sub(r's$', '', squash(key))].append(i)
    out = []
    for v in groups.values():
        if len(v) < 2:
            continue
        if len({rows[i]['cells'][0] for i in v}) < 2:
            continue
        if len({main_zh(rows[i]['cells'][2]) for i in v}) != 1:
            continue                      # 译法不同＝另有分工/冲突，不动
        out.append(v)
    return out


def merge_group(rows, idxs, is_person):
    """返回 (保留行 cells, 被删键列表)。"""
    group = [rows[i] for i in idxs]
    if is_person:
        inv = [g for g in group if inverted(g['cells'][0])]
        base = inv[0] if inv else group[0]
    else:
        lower = [g for g in group if g['cells'][0] == g['cells'][0].lower()]
        base = lower[0] if lower else group[0]
    cells = list(base['cells'])
    variants = []
    for g in [base] + [g for g in group if g is not base]:
        for part in re.split(r'\s*/\s*', g['cells'][0]):
            p = part.strip()
            if p and all(fold(p) != fold(v) for v in variants):
                variants.append(p)
    cells[0] = ' / '.join(variants)
    # 原文：取首个非「—」
    for g in group:
        if g['cells'][1] not in ('—', ''):
            cells[1] = g['cells'][1]
            break
    # 译法：主译一致（聚类已保证）；保留 base 的亦作信息，若他行有亦作而 base 无，则并入
    base_zh = base['cells'][2]
    extra = []
    for g in group:
        if g is base:
            continue
        if '亦作' not in base_zh and '亦作' in g['cells'][2]:
            extra.append(re.search(r'亦作[“"]([^”"]+)[”"]', g['cells'][2]))
    if extra:
        v = '、'.join('“%s”' % m.group(1) for m in extra if m)
        if v:
            cells[2] = base_zh.rstrip('）)') + ('（亦作%s）' % v if not base_zh.endswith('）') else '；亦作%s）' % v)
    # 籍属/生卒：取首个非「—」
    for col in (3, 4):
        if is_person:
            for g in group:
                if g['cells'][col] not in ('—', ''):
                    cells[col] = g['cells'][col]
                    break
    FIRST = 5 if is_person else 3
    BASIS = 6 if is_person else 4
    DATE_COL = 7 if is_person else 5
    # 首现：并集
    seen = []
    for g in group:
        for part in re.split(r'[；;]', g['cells'][FIRST]):
            p = part.strip()
            if p and p not in seen:
                seen.append(p)
    if seen:
        cells[FIRST] = '；'.join(seen)
    # 依据 + 旧键留痕
    dropped = [g['cells'][0] for g in group if g is not base]
    note = '；%s 重复行合并（旧键 %s）' % (DATE, '、'.join('`%s`' % d for d in dropped))
    cells[BASIS] = cells[BASIS].rstrip('；;') + note
    cells[DATE_COL] = DATE
    return cells, dropped


def run(mode):
    report = {'date': DATE, 'person': [], 'term': []}
    for path, is_person, key in ((PERSON, True, 'person'), (TERM, False, 'term')):
        lines, rows = load(path)
        groups = cluster_person(rows) if is_person else cluster_term(rows)
        delete_idx = set()
        for g in groups:
            new_cells, dropped = merge_group(rows, g, is_person)
            base = rows[g[0]]
            # 保留行取组内倒装/小写基准行
            keep_row = None
            if is_person:
                inv = [rows[i] for i in g if inverted(rows[i]['cells'][0])]
                keep_row = inv[0] if inv else rows[g[0]]
            else:
                lower = [rows[i] for i in g if rows[i]['cells'][0] == rows[i]['cells'][0].lower()]
                keep_row = lower[0] if lower else rows[g[0]]
            lines[keep_row['idx']] = '| %s |' % ' | '.join(new_cells)
            for i in g:
                if rows[i] is not keep_row:
                    delete_idx.add(rows[i]['idx'])
            report[key].append({'keep': keep_row['cells'][0], 'merged_key': new_cells[0],
                                'dropped': dropped})
        kept = [l for i, l in enumerate(lines) if i not in delete_idx]
        report[key + '_deleted'] = len(delete_idx)
        print('%s: 合并 %d 组，删冗余 %d 行' % (path, len(groups), len(delete_idx)))
        if mode == 'apply':
            io.open(path, 'w', encoding='utf-8', newline='').write('\n'.join(kept))
    json.dump(report, io.open(REPORT, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('报告 →', REPORT)


if __name__ == '__main__':
    run(sys.argv[1] if len(sys.argv) > 1 else 'dry')
