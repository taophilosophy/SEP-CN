# -*- coding: utf-8 -*-
"""术语落册统一流水线（specs/008 常态流程优化，2026-11-01）。

取代每批手写登记脚本：rowspec 清单驱动的幂等落册——
  登记册（术语=锚点后插，人名=二分）→ 词汇表（二分）→ 池 publish → 自检计数。
键已存在自动跳过（杜绝重复行事故）；锚点缺失即报错不写盘（杜绝半成品）。

rowspec JSON 格式:
  {"rows": [
     {"en": "expected utility", "zh": "期望效用", "table": "term",
      "anchor": "| Essentialism |", "note": "审定名词库（termonline-all·管理科学，凭证 2026-11-01）",
      "date": "2026-11-01"},
     {"en": "Paul Bernays", "zh": "保罗·贝尔奈斯", "table": "person", "note": "…", "date": "…"} ]}

依据列自动拼装：学界惯例/审定名词库由 note 前缀区分（note 以“审定”开头→审定名词库（…），
否则→学界惯例（note））；date 缺省取 rowspec 顶层 "date"。

用法:
  python tools/term_flow.py --spec <rowspec.json>            # 实写
  python tools/term_flow.py --spec <rowspec.json> --dry-run  # 干跑
退出码: 0 完成（含跳过）；1 锚点缺失（未写盘）；2 参数错误。
"""
import io
import json
import os
import re
import sys
import unicodedata

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
REG = os.path.join(ROOT, 'yi-zhe-shuo-ming.md')
REN = os.path.join(ROOT, 'ren-ming-biao.md')
GLO = os.path.join(ROOT, 'qian-yan', 'ci-hui-biao.md')
POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')


def key_of(line):
    cell = line.strip().strip('|').split('|')[0].strip()
    s = unicodedata.normalize('NFD', cell.replace('*', '').strip())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).casefold()


def norm_key(text):
    sys.path.insert(0, ROOT)
    from tools.cnki_query import norm_key as nk
    return nk(text)


def build_row(spec, date):
    en, zh, table = spec['en'], spec['zh'], spec.get('table', 'term')
    basis = spec.get('basis')
    if not basis:
        note = spec.get('note', '学界惯例')
        if note.startswith('审定'):
            basis = note + '；凭证 ' + date
        else:
            basis = '学界惯例（%s）；凭证 %s' % (note, date)
    if table == 'term':
        reg_row = '| %s | %s | %s | %s | %s |' % (
            en, zh, spec.get('first_seen', '语料回收（标题词）'), basis, date)
    else:
        reg_row = '| %s | %s | %s | %s | %s |' % (
            en, zh, spec.get('first_seen', '语料回收（全目录）'), basis, date)
    glo_row = '|%s|%s|%s|' % (en, zh, spec.get('glo_note', ''))
    return reg_row, glo_row


def bisect_insert(lines, row):
    k = key_of(row)
    for i, l in enumerate(lines):
        if l.startswith('|') and key_of(l) > k and '----' not in l:
            lines.insert(i, row)
            return i
    return None


def anchor_insert(lines, anchor, row):
    hit = next((i for i, l in enumerate(lines) if l.startswith(anchor)), None)
    if hit is None:
        return None
    lines.insert(hit + 1, row)
    return hit


def apply(spec_path, dry):
    spec = json.load(open(spec_path, encoding='utf-8'))
    rows = spec.get('rows', [])
    date = spec.get('date', '')
    reg = io.open(REG, encoding='utf-8', newline='').read().split('\n')
    ren = io.open(REN, encoding='utf-8', newline='').read().split('\n')
    glo = io.open(GLO, encoding='utf-8', newline='').read().split('\n')

    reg_keys = {key_of(l) for l in reg if l.startswith('| ')}
    ren_keys = {key_of(l) for l in ren if l.startswith('| ')}
    miss, dup, ok_r, ok_g = [], 0, 0, 0
    for sp in rows:
        reg_row, glo_row = build_row(sp, sp.get('date', date))
        table = sp.get('table', 'term')
        en_key = key_of(reg_row)
        target, keys = (reg, reg_keys) if table == 'term' else (ren, ren_keys)
        if en_key in keys:
            dup += 1
            print('  跳过（键已存在）: %s' % sp['en'])
            continue
        anchor = sp.get('anchor')
        hit = None
        if table == 'term' and anchor:
            hit = next((i for i, l in enumerate(target)
                        if l.startswith(anchor)), None)
            if hit is None:
                miss.append('%s（锚点 %s）' % (sp['en'], anchor))
                continue
            target.insert(hit + 1, reg_row)
        else:
            if bisect_insert(target, reg_row) is None:
                miss.append('%s（二分失败）' % sp['en'])
                continue
        ok_r += 1
        k = key_of(glo_row)
        for i, l in enumerate(glo):
            if l.startswith('|') and key_of(l) > k and '----' not in l:
                glo.insert(i, glo_row)
                ok_g += 1
                break
    print('登记册: 插入 %d | 词汇表: 插入 %d | 跳过(已存在) %d%s'
          % (ok_r, ok_g, dup, ('；锚点缺失: ' + '; '.join(miss)) if miss else ''))

    import json as _json
    pool_d = _json.load(open(POOL, encoding='utf-8'))
    pk = {norm_key(sp['en']) for sp in rows}
    np_ = 0
    for c in pool_d['candidates']:
        if c.get('status') == 'new' and norm_key(c.get('en', '')) in pk:
            c['status'] = 'published@' + date
            np_ += 1
    print('池: published=%d' % np_)

    if not dry and not miss:
        for path, lines in ((REG, reg), (REN, ren), (GLO, glo)):
            with io.open(path, 'w', encoding='utf-8', newline='') as f:
                f.write('\n'.join(lines))
        _json.dump(pool_d, open(POOL, 'w', encoding='utf-8'), ensure_ascii=False)
        print('已写盘（含池）')
    return 0 if not miss else 1


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if '--spec' not in argv:
        print(__doc__)
        return 2
    spec_path = argv[argv.index('--spec') + 1]
    return apply(spec_path, '--dry-run' in argv)


if __name__ == '__main__':
    sys.exit(main())
