# -*- coding: utf-8 -*-
"""术语一致性检查器（specs/002 FR-001..005；ADR-0012/specs/008 扩展三表）。

用法:
  python tools/check_terms.py                       # 三表冲突 + 两登记册自洽（门禁）
  python tools/check_terms.py --docs a/某词条.md …   # 定点核销：登记册"首现"驱动的正文核对
  python tools/check_terms.py --registry <路径> --glossary <路径>   # 测试注入（单表模式）
  python tools/check_terms.py --registry2 <路径>    # 注入第二登记册（人名表）

三表:
  - 术语登记册 yi-zhe-shuo-ming.md（原文|译法|首现|依据|裁定日期，五列）
  - 人名登记册 ren-ming-biao.md（同五列，ADR-0012 自术语表拆出）
  - 发布词汇表 qian-yan/ci-hui-biao.md（英语|中文|备注，发布视图）

规则:
  - 键规范化：剥 * 斜体标记、去首尾空格、比对用 casefold，展示保留原样。
  - 译法集合：取"（"前主形，并按 / 与 ／ 拆分为变体；两侧集合互斥 = 冲突（硬错误）；
    一侧为另一侧真子集 = 词汇表滞后（告警）。
  - 登记册自洽：废弃行须有同键非废弃行；裁定日期缺失、依据列缺失 = 告警
    （数据欠账，登记会话补齐）；同键同译法重复 = 硬错误。
退出码: 0 无硬错误；1 有冲突或自洽违例（--docs 模式仅告警，恒 0）。
"""
import io
import os
import re
import sys
from collections import defaultdict

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, 'yi-zhe-shuo-ming.md')
REGISTRY2 = os.path.join(ROOT, 'ren-ming-biao.md')
GLOSSARY = os.path.join(ROOT, 'qian-yan', 'ci-hui-biao.md')
DEPRECATED_MARK = '已废弃'
HEADER_WORDS = {'原文', '译法', '首现', '依据', '裁定日期', '人名', '文献',
                '条目', 'term'}


def norm_key(text):
    """术语键：剥斜体标记与空白，casefold 比对。"""
    return re.sub(r'\s+', ' ', text.replace('*', '').strip()).casefold()


def translations(cell):
    """译法集合：取"（"注记前主形，按 / ／ ； 、 ; ， 拆分变体。"""
    head = cell.split('（')[0].strip()
    variants = re.split(r'[/／；、;，]', head)
    return {v.strip() for v in variants if v.strip()}


def split_row(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def is_data_row(cells):
    return (len(cells) >= 2 and cells[0] and cells[1]
            and cells[0].casefold() not in HEADER_WORDS
            and not set(cells[0]) <= set(':-— '))


def parse_registry(path):
    """返回 rows=[(term, trans, first_seen, basis, date, lineno)] 与解析告警。

    五列（原文|译法|首现|依据|裁定日期）为标准格式；旧四列（无依据）容忍并告警。
    """
    rows, warns = [], []
    if not path or not os.path.exists(path):
        return rows, warns
    for lineno, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.startswith('|'):
            continue
        cells = split_row(line)
        if not is_data_row(cells):
            continue
        term, trans = cells[0], cells[1]
        first_seen = cells[2] if len(cells) >= 3 else ''
        if len(cells) >= 5:
            basis, date = cells[3], cells[4]
            if not basis:
                warns.append('缺依据列（告警）：%s（第 %d 行）' % (term, lineno))
        elif len(cells) == 4:
            basis, date = '', cells[3]
            warns.append('缺依据列（告警）：%s（第 %d 行）' % (term, lineno))
        else:
            basis, date = '', ''
            warns.append('第 %d 行仅 %d 列（应为 5）：%s'
                         % (lineno, len(cells), term))
        rows.append((term, trans, first_seen, basis, date, lineno))
    return rows, warns


def parse_glossary(path):
    """返回 rows=[(term, trans, lineno)] 与解析告警。"""
    rows, warns = [], []
    for lineno, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.startswith('|'):
            continue
        cells = split_row(line)
        if not is_data_row(cells):
            continue
        rows.append((cells[0], cells[1], lineno))
    return rows, warns


def collect(rows):
    """key -> {translation_set, display_key, linenos}"""
    table = {}
    for row in rows:
        term, trans, lineno = row[0], row[1], row[-1]
        key = norm_key(term)
        entry = table.setdefault(key, {'key': key, 'display': term,
                                       'trans': set(), 'lines': []})
        entry['trans'] |= translations(trans)
        entry['lines'].append(lineno)
    return table


def check_registry_self(rows):
    """自洽性：废弃链、重复 = 硬错误；缺裁定日期/缺依据 = 告警（数据欠账）。"""
    errors, warns = [], []
    by_key = defaultdict(list)
    for term, trans, _fs, _basis, date, lineno in rows:
        by_key[norm_key(term)].append((term, trans, date, lineno))
    for key, items in by_key.items():
        live = [it for it in items if DEPRECATED_MARK not in it[1]]
        deprecated = [it for it in items if DEPRECATED_MARK in it[1]]
        if deprecated and not live:
            errors.append('废弃链断裂：%s 仅剩废弃行（第 %s 行），无有效新行'
                          % (deprecated[0][0], '/'.join(str(it[3]) for it in deprecated)))
        seen = {}
        for term, trans, date, lineno in items:
            if not date or set(date) <= set(':- '):
                warns.append('缺裁定日期（告警）：%s（第 %d 行）' % (term, lineno))
            sig = (norm_key(term), trans.strip())
            if sig in seen:
                errors.append('重复行：%s|%s 第 %d 行与第 %d 行重复'
                              % (term, trans, seen[sig], lineno))
            else:
                seen[sig] = lineno
    return errors, warns


def check_conflicts(reg, glos, label):
    """登记册↔词汇表：互斥 = 冲突（硬错误），真子集 = 滞后（告警）。"""
    conflicts, lagging = [], []
    for key in sorted(set(reg) & set(glos)):
        rt, gt = reg[key]['trans'], glos[key]['trans']
        if rt and gt and not (rt & gt):
            conflicts.append((label, reg[key]['display'], sorted(rt), sorted(gt),
                              reg[key]['lines'], glos[key]['lines']))
        elif rt and gt and (rt < gt or gt < rt):
            lagging.append((label, reg[key]['display'], sorted(rt), sorted(gt)))
    return conflicts, lagging


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    reg_path, glos_path, docs = REGISTRY, GLOSSARY, []
    reg2_path = REGISTRY2
    injected = False
    i = 0
    while i < len(argv):
        if argv[i] == '--docs':
            docs = argv[i + 1:]
            break
        if argv[i] == '--registry':
            reg_path, i, injected = argv[i + 1], i + 1, True
        elif argv[i] == '--registry2':
            reg2_path, i = argv[i + 1], i + 1
        elif argv[i] == '--glossary':
            glos_path, i = argv[i + 1], i + 1
        i += 1
    if injected and '--registry2' not in argv:
        reg2_path = ''  # 注入单表模式：跳过人名表，保证测试密闭

    conflicts, lagging = [], []
    all_self_errors, warns = [], []
    doc_rows = []

    def load_one(label, path):
        rows, w = parse_registry(path)
        reg = collect(rows)
        c, l = check_conflicts(reg, glos, label)
        conflicts.extend(c)
        lagging.extend(l)
        e, dw = check_registry_self(rows)
        all_self_errors.extend('%s %s' % (label, x) for x in e)
        warns.extend('%s %s' % (label, x) for x in w + dw)
        doc_rows.extend(rows)
        return rows, reg

    glos_rows, glos_warns = parse_glossary(glos_path)
    glos = collect(glos_rows)
    reg1_rows, reg1 = load_one('登记册', reg_path)
    reg2_rows, reg2 = load_one('人名表', reg2_path)

    print('登记册 %s 行 %d（键 %d） | 人名表 %s 行 %d（键 %d） | 词汇表行 %d（键 %d） | 交集键 %d+%d'
          % (os.path.basename(reg_path or '(跳过)'), len(reg1_rows), len(reg1),
             os.path.basename(reg2_path or '(跳过)'), len(reg2_rows), len(reg2),
             len(glos_rows), len(glos),
             len(set(reg1) & set(glos)), len(set(reg2) & set(glos))))
    for w in glos_warns:
        print('告警(解析): %s' % w)
    for label, term, rt, gt, rl, gl in conflicts:
        print('冲突: %s\n  %s(第%s行): %s\n  词汇表(第%s行): %s'
              % (term, label, ','.join(map(str, rl)), '、'.join(rt),
                 ','.join(map(str, gl)), '、'.join(gt)))
    for label, term, rt, gt in lagging:
        print('词汇表滞后（告警）: [%s] %s | 登记侧: %s | 词汇表: %s'
              % (label, term, '、'.join(rt), '、'.join(gt)))
    for e in all_self_errors:
        print('自洽违例: %s' % e)
    for w in warns:
        print(w)

    if docs:
        body_cache = {}
        misses = 0
        for row in doc_rows:
            term, trans, first_seen = row[0], row[1], row[2]
            slugs = [s for s in re.split(r'[（()）/,、]', first_seen or '')
                     if s.strip() and re.fullmatch(r'[a-z0-9\-]+', s.strip())]
            hit_docs = [d for d in docs
                        if any(d.endswith('%s.md' % s) or ('/%s/' % s) in d for s in slugs)]
            for d in hit_docs:
                if d not in body_cache:
                    body_cache[d] = open(os.path.join(ROOT, d), encoding='utf-8').read()
                for t in translations(trans):
                    if t not in body_cache[d]:
                        print('正文缺登记译法（告警）: %s 的「%s」未见于 %s'
                              % (term, t, d))
                        misses += 1
        print('定点核销：%d 个文档，%d 处疑似缺译法（仅告警）' % (len(docs), misses))

    hard = len(conflicts) + len(all_self_errors)
    print('硬错误 %d（冲突 %d + 自洽 %d），词汇表滞后 %d'
          % (hard, len(conflicts), len(all_self_errors), len(lagging)))
    if docs:
        return 0
    return 1 if hard else 0


if __name__ == '__main__':
    sys.exit(main())
