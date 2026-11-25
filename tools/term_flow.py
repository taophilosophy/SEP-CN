# -*- coding: utf-8 -*-
"""术语落册统一流水线（specs/008 常态流程优化，2026-11-01）。

取代每批手写登记脚本：rowspec 清单驱动的幂等落册——
  登记册（术语=锚点后插，人名=二分）→ 池 publish → 自检计数（ADR-0036：词汇表已并网删除）。
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

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.register_lib import norm_key, person_path, term_path  # noqa: E402

REG = term_path()
REN = person_path()
POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')


def key_of(line):
    cell = line.strip().strip('|').split('|')[0].strip()
    return norm_key(cell)


def _quote_norm(text):
    """写册前引号归一（rules/02 第 11 条）：直角引号一律改弯引号。

    rowspec 是人写的判定文本，历史上多次把「」写进依据列致全库引号门禁红
    （2026-11-19 实测 190 行 306 处）。归一放在写路径，杜绝回流。
    """
    if not isinstance(text, str):
        return text
    return (text.replace('\u300c', '\u201c').replace('\u300d', '\u201d')
            .replace('\u300e', '\u2018').replace('\u300f', '\u2019'))


def build_row(spec, date):
    en, zh, table = spec['en'], spec['zh'], spec.get('table', 'term')
    basis = spec.get('basis')
    if not basis:
        note = spec.get('note', '学界惯例')
        if note.startswith('审定'):
            basis = note + '；凭证 ' + date
        else:
            basis = '学界惯例（%s）；凭证 %s' % (note, date)
    basis = _quote_norm(basis)
    if table == 'term':
        # 6 列：键｜原文｜译法｜首现｜依据｜裁定日期（原文缺省 —，键即英文原形）
        reg_row = '| %s | %s | %s | %s | %s | %s |' % (
            _quote_norm(en), spec.get('orig', '—'), _quote_norm(zh),
            spec.get('first_seen', '语料回收'), basis, date)
    else:
        # 8 列：原文｜别名｜译法｜籍属｜生卒｜首现｜依据｜裁定日期
        reg_row = '| %s | %s | %s | %s | %s | %s | %s | %s |' % (
            _quote_norm(en), spec.get('alias', '—'), _quote_norm(zh),
            _quote_norm(spec.get('affiliation', '—')), spec.get('dates', '—'),
            spec.get('first_seen', '语料回收（全目录）'), basis, date)
    return reg_row


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

    reg_keys = {key_of(l) for l in reg if l.startswith('| ')}
    ren_keys = {key_of(l) for l in ren if l.startswith('| ')}
    # 中文主形查重（2026-11-23 加）：同主形不同英文＝疑似同概念异拼写重复登记，
    # 只告警不拦截（同形不同义按 rules/03 分行时需人工判定）。
    # 2026-11-25：告警带出既有行键与译法，并给处置提示——只报“已有”时告警曾被忽略，
    # 同概念二次登记因此造出 air pump（抽气机／空气泵）、《谈谈方法》／《方法谈》等分裂。
    zh_main = {}
    for l in reg:
        if not l.startswith('| '):
            continue
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) != 6 or cells[2] in ('—', ''):
            continue
        m = cells[2].split('（')[0].strip('《》')
        if m:
            zh_main.setdefault(m, []).append((cells[0], cells[2]))
    zh_warn = []
    for sp in rows:
        if sp.get('table', 'term') != 'term':
            continue
        m = sp.get('zh', '').split('（')[0].strip('《》')
        if not m or m not in zh_main:
            continue
        en_n = norm_key(sp['en'])
        olds = [(k, z) for k, z in zh_main[m]
                if en_n not in {norm_key(x) for x in k.split('/')}]
        if olds:
            k, z = olds[0]
            zh_warn.append('%s（%s 已有：%s＝%s）' % (sp['en'], m, k, z[:40]))
    if zh_warn:
        print('  告警 中文主形已存在（同概念异拼写？）：' + '；'.join(zh_warn))
        print('  提示 同形不同义请在译法加域括注后重跑；同概念请并键（键写 A / B，'
              '依据栏记旧键与旧首现），勿两行照登')
    miss, dup, ok_r = [], 0, 0
    for sp in rows:
        reg_row = build_row(sp, sp.get('date', date))
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
    print('登记册: 插入 %d | 跳过(已存在) %d%s'
          % (ok_r, dup, ('；锚点缺失: ' + '; '.join(miss)) if miss else ''))

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
        for path, lines in ((REG, reg), (REN, ren)):
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
