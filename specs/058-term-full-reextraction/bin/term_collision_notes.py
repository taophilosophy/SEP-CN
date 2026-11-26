#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""撞形记录机检（P1-10，2026-11-26）：把两登记册的「撞形」留痕与同译法多键组对上。

口径：
  * 记录句式（2026-11-26 表头注）：`撞形{豁免|改定|处置|残余并键} YYYY-MM-DD：{理由}`
    历史变体一并识别：`（YYYY-MM-DD 撞形处置）`、`撞形批 B1 已并`、`撞形已并`。
  * 理由词受控集：同概念异语／同形异语／同概念异形／同形异源／同形异义／同形异书／
    同形异域／同语异义／同形异角色／同著作异形／异人／同人异键；裸说明（如
    「多义占位行」「与 stuff 分列」「两派名称并存」）判为“说明型”，单列。
  * 未留痕组：术语表同一主译法对应多键、且组内无一行带撞形记录——这是真缺口。

用法：
  python specs/058-term-full-reextraction/bin/term_collision_notes.py [--json]
退出码：0 完成（告警档；不入 check_all）。
"""
import argparse
import collections
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

REC = re.compile(r'撞形(?:豁免|改定|处置|残余并键)\s*(\d{4}-\d{2}-\d{2})?\s*[：:；;]')
REC_ALT = re.compile(r'(?:（|，|,)\s*(\d{4}-\d{2}-\d{2})?\s*撞形处置\s*）')
REC_MERGE = re.compile(r'撞形(?:批\s*B1\s*已[并与]|[^，。；|]{0,6}已并)')
REASONS = ('同概念异语', '同形异语', '同概念异形', '同形异源', '同形异义',
           '同形异书', '同形异域', '同语异义', '同形异角色', '同著作异形',
           '异人', '同人异键')


def parse(path, ncols, trans_idx=2, basis_idx=4):
    rows = []
    for ln, line in enumerate(open(path, encoding='utf-8'), 1):
        s = line.rstrip('\n')
        if not s.startswith('|') or s.startswith('| ---') or s.startswith('| 键') \
                or s.startswith('| 原文'):
            continue
        c = [x.strip() for x in s.strip().strip('|').split('|')]
        if len(c) != ncols:
            continue
        rows.append({'line': ln, 'key': c[0], 'trans': c[trans_idx],
                     'basis': c[basis_idx]})
    return rows


def rec_kind(basis):
    if '撞形' not in basis:
        return None
    for name in ('豁免', '改定', '处置', '残余并键'):
        if re.search(r'撞形' + name, basis):
            return name
    for m in (REC_ALT.search(basis), REC_MERGE.search(basis)):
        if m:
            return '合并'
    return '裸'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    term = parse(os.path.join(ROOT, 'shu-yu-biao.md'), 6, 2, 4)
    pers = parse(os.path.join(ROOT, 'ren-ming-biao.md'), 8, 2, 6)

    stats = collections.Counter()
    kinds = collections.Counter()
    dates = collections.Counter()
    bare, note_form = [], []
    for r in term + pers:
        if '撞形' not in r['basis']:
            continue
        stats['rows'] += 1
        k = rec_kind(r['basis'])
        kinds[k] += 1
        m = re.search(r'(\d{4}-\d{2}-\d{2})', r['basis'])
        if m:
            dates[m.group(1)] += 1
        if k in ('裸', '合并'):
            bare.append((r['line'], r['key'], k))
            continue
        if any(w in r['basis'] for w in REASONS):
            continue
        tail = r['basis'].split('撞形', 1)[1]
        if len(re.findall(r'[\u4e00-\u9fff]', tail)) >= 2:
            note_form.append((r['line'], r['key']))
        else:
            bare.append((r['line'], r['key'], 'k=%s 无说明' % k))

    # 同主译法多键组：组内无撞形记录 = 未留痕（跳过“保留原文”类元译法；
    # 书名同译名是常见合法现象，按 2026-11-26 分类判为工具误报，不计）
    META = {'保留原文', '拉丁原文保留', '保留英文', '保留梵文', '保留拉丁形'}
    groups = collections.defaultdict(list)
    for r in term:
        main = re.split(r'[（(]', r['trans'])[0].strip()
        if main and main not in META and not main.startswith('《'):
            groups[main].append(r)
    untraced = []
    for main, items in groups.items():
        if len({i['key'].casefold() for i in items}) < 2:
            continue
        if any('撞形' in i['basis'] for i in items):
            continue
        untraced.append((main, sorted({i['key'] for i in items})))
    untraced.sort(key=lambda x: -len(x[1]))

    out = {
        '撞形记录行': stats['rows'],
        '句式分布': dict(kinds),
        '日期分布': dict(dates.most_common(6)),
        '无受控理由但有中文说明': len(note_form),
        '真裸（无任何理由/说明）': len(bare),
        '未留痕撞形组': len(untraced),
        '未留痕组样本': untraced[:20],
    }
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        print('撞形记录行: %d' % stats['rows'])
        print('句式分布:', dict(kinds))
        print('日期分布:', dict(dates.most_common(6)))
        print('无受控理由但有中文说明: %d（不报，供统计）' % len(note_form))
        print('真裸（无任何理由/说明）: %d' % len(bare))
        for x in bare[:15]:
            print('  L%d %s [%s]' % x)
        print('同主译法多键但无撞形留痕: %d 组' % len(untraced))
        for main, keys in untraced[:15]:
            print('  %s: %s' % (main, keys))
    return 0


if __name__ == '__main__':
    sys.exit(main())
