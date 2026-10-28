# -*- coding: utf-8 -*-
"""学术规范门禁（specs/003-academic-norms，rules/07 哲学学术规范）。

用法:
  python tools/check_academic.py                      # 全库词条文档 + 任务版本钉（门禁）
  python tools/check_academic.py --docs <路径>...     # 定点检查指定文档（不查任务）
  python tools/check_academic.py --strict             # 告警升硬错误（s3/r3 验收）
  python tools/check_academic.py --root <目录> --baseline <json> --tasks-dir <目录>  # 测试注入

检查项（rules/07）:
  硬错误:
    pubinfo-missing        非存根词条缺“首次发表于”版本事实行（baseline 有 pubinfo 时）
    pubinfo-mismatch       版本事实行日期与 baseline pubinfo 不一致
    orphan-ref / orphan-def  正文 [^key] 引用与文末 [^key]: 定义不配对
    task-pin-missing       任务 JSON 缺 version_pin（pubinfo_date/archive_edition/sha256）
    task-evidence-missing  done 任务步骤缺 evidence（或步数不足 6）
  告警（--strict 升硬）:
    biblio-missing          非存根词条无“参考文献”节
    scholar-tools-missing   非存根词条无“学术工具/如何引用本词条”
    biblio-note-missing     “参考文献”节缺“照录”说明
    biblio-note-outdated    节首说明为 ADR-0011 前旧措辞（缺“中国文献译为中文”）
    biblio-chinese-untranslated  文献节疑似中国文献条目仍全罗马化（ADR-0011）
    trans-note              译注未闭合或出现在参考文献节
    baseline-lookup-miss    文档未能在 baseline 定位（pubinfo 不可核）
退出码: 0 无硬错误；1 有硬错误（--strict 时告警也算）；2 用法错误。
"""
import argparse
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools.biblio_audit import probe_text  # noqa: E402  文献探针（疑似中国文献定位）

EXCLUDE_DIRS = {
    '.git', '.github', '.vitepress', '.specify', '.zcode', 'node_modules',
    'en', 'yuanwen', 'pending', 'public', 'script', 'tools', 'rules', 'specs',
    'tasks', 'baseline', 'state', 'assets',
    'qian-yan', 'fang-fa-lun', 'jian-yi-shu', 'guan-yu',
}
EXCLUDE_FILES = {
    'README.md', 'SUMMARY.md', 'mu-lu-s.md', 'yi-zhe-shuo-ming.md',
    'ren-ming-biao.md',  # ADR-0012 人名登记册，与 yi-zhe-shuo-ming 同性质
    'PROGRESS.md', 'AGENTS.md', 'CODE_OF_CONDUCT.md', 'CONTRIBUTING.md',
}

STUB_BODY_LINES = 10      # 非空行 ≤ 此数（含 H1）视为存根
PUBINFO_WINDOW = 30       # 版本事实行须落在前 N 个非空行内
DONE_MIN_STEPS = 6        # done 任务最少步数（update 无 clear/draft）

MONTHS = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
          'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

RE_PUBINFO = re.compile(r'首次发表于')
RE_ZH_DATE = re.compile(r'(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日')
RE_EN_DATE = re.compile(r'([A-Za-z]+)\s+(\d{1,2})\s*,\s*(\d{4})')
RE_FOOTREF = re.compile(r'\[\^([^\]\s]+)\](?!:)')
RE_FOOTDEF = re.compile(r'^\[\^([^\]\s]+)\]:')
RE_HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$')
BIBLIO_HEADINGS = {'参考文献', 'bibliography', 'secondary literature', '延伸阅读', '文献目录', 'references（引用注释）'}
PIN_FIELDS = ('pubinfo_date', 'archive_edition', 'sha256')


def norm_rel(path, root):
    return os.path.relpath(path, root).replace(os.sep, '/').replace('\\', '/')


def parse_en_date(text):
    m = RE_EN_DATE.search(text or '')
    if not m:
        return None
    month = MONTHS.get(m.group(1)[:3].casefold())
    if not month:
        return None
    return (int(m.group(3)), month, int(m.group(2)))


def fmt_zh(d):
    return '%d 年 %d 月 %d 日' % d


def load_baseline(path):
    """返回 (by_zh_doc, records)；zh_doc 键 casefold、正斜杠归一。"""
    with open(path, encoding='utf-8') as fh:
        data = json.load(fh)
    records = [r for r in (data.get('entries') or []) if isinstance(r, dict)]
    by_zh_doc = {}
    for rec in records:
        zh = str(rec.get('zh_doc') or '').replace('\\', '/').strip().casefold()
        if zh:
            by_zh_doc.setdefault(zh, rec)
    return by_zh_doc, records


def resolve_record(rel, by_zh_doc, records, warns):
    """zh_doc 精确匹配 → slug 词元回退（长 slug 优先，pubinfo 同则取首个）。"""
    rec = by_zh_doc.get(rel.casefold())
    if rec:
        return rec
    stem = os.path.basename(rel)[:-3].casefold()
    wrap = '-%s-' % stem
    cands = [r for r in records
             if r.get('slug') and ('-%s-' % str(r['slug']).casefold()) in wrap]
    if not cands:
        return None
    if len(cands) > 1:
        longest = max(len(str(r['slug'])) for r in cands)
        cands = [r for r in cands if len(str(r['slug'])) == longest]
        if len(cands) > 1:
            pins = {str((r.get('pubinfo') or {}).get('first_published') or '')
                    for r in cands}
            if len(pins) > 1:
                warns.append('[baseline-lookup-miss] %s slug 词元歧义（%s），pubinfo 不核'
                             % (rel, '、'.join(str(r.get('slug')) for r in cands)))
                return None
            cands = cands[:1]
    return cands[0]


def find_biblio_span(headings):
    """返回参考文献节内容的 (start_lineno, stop_lineno|None)，未找到返回 None。"""
    for pos, (lineno, level, text) in enumerate(headings):
        if text.casefold() in BIBLIO_HEADINGS:
            for j in range(pos + 1, len(headings)):
                if headings[j][1] <= level:
                    return lineno, headings[j][0]
            return lineno, None
    return None


def check_doc(rel, ne, warns, is_supp=False):
    """文档级结构检查；返回 (pubinfo_lineno, pubinfo_line)。"""
    headings = []
    for lineno, line in ne:
        m = RE_HEADING.match(line.strip())
        if m:
            headings.append((lineno, len(m.group(1)), m.group(2)))
    biblio = find_biblio_span(headings)
    if biblio is None:
        if not is_supp:
            warns.append('[biblio-missing] %s 非存根词条无“参考文献”节' % rel)
    else:
        start, stop = biblio
        in_sec = [line for ln, line in ne
                  if start <= ln and (stop is None or ln < stop)]
        note_lines = [line for line in in_sec if '照录' in line]
        if not note_lines:
            warns.append('[biblio-note-missing] %s:%d “参考文献”节缺“照录”说明' % (rel, start))
        elif not any('中国文献' in line for line in note_lines):
            warns.append('[biblio-note-outdated] %s:%d 节首说明为 ADR-0011 前旧措辞，应含“中国文献译为中文”' % (rel, start))
        # ADR-0011：疑似中国文献条目仍全罗马化 → 告警（行级定位用 biblio_audit.py）
        zh_rows = 0
        for line in in_sec:
            p = probe_text(line)
            if p['cjk'] or p['kana']:
                continue
            if p['classic_hits'] or p['authorpos_hits'] >= 2:
                zh_rows += 1
        if zh_rows:
            warns.append('[biblio-chinese-untranslated] %s:%d 文献节约 %d 行疑似中国文献仍全罗马化，按 ADR-0011 还原中文'
                         % (rel, start, zh_rows))

    fence = False
    for lineno, line in ne:
        s = line.strip()
        if s.startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        start_at = 0
        while True:
            i = line.find('（译注：', start_at)
            if i < 0:
                break
            if '）' not in line[i:]:
                warns.append('[trans-note] %s:%d 译注未闭合' % (rel, lineno))
            if biblio and biblio[0] <= lineno and (biblio[1] is None or lineno < biblio[1]):
                warns.append('[trans-note] %s:%d 译注出现在参考文献节' % (rel, lineno))
            start_at = i + 1

    has_scholar = (any(t.casefold() in {'学术工具', 'scholarly tools'} or '如何引用' in t
                       for _, _, t in headings)
                   or any('如何引用本词条' in line for _, line in ne))
    if not has_scholar and not is_supp:
        warns.append('[scholar-tools-missing] %s 非存根词条无“学术工具/如何引用本词条”' % rel)

    pubinfo = next(((ln, l) for ln, l in ne[:PUBINFO_WINDOW] if RE_PUBINFO.search(l)), None)
    return pubinfo or (None, None)


def check_pubinfo(rel, pubinfo, rec, hard, warns):
    pub = rec.get('pubinfo') if rec else None
    if not pub:
        return
    b_first = parse_en_date(str(pub.get('first_published') or ''))
    b_rev = parse_en_date(str(pub.get('substantive_revision') or ''))
    if b_first is None:
        warns.append('[baseline-lookup-miss] %s baseline pubinfo 无法解析，pubinfo 不核' % rel)
        return
    lineno, line = pubinfo
    if lineno is None:
        hard.append('[pubinfo-missing] %s:1 缺“首次发表于”版本事实行（baseline 首发: %s）'
                    % (rel, pub.get('first_published')))
        return
    dates = RE_ZH_DATE.findall(line)
    if not dates:
        hard.append('[pubinfo-mismatch] %s:%d 版本事实行无中文日期（baseline 首发: %s）'
                    % (rel, lineno, pub.get('first_published')))
        return
    d_first = tuple(int(x) for x in dates[0])
    if d_first != b_first:
        hard.append('[pubinfo-mismatch] %s 首发日期 文内 %s ≠ baseline %s'
                    % (rel, fmt_zh(d_first), fmt_zh(b_first)))
        return
    d_rev = tuple(int(x) for x in dates[1]) if len(dates) > 1 else None
    if (b_rev is None) != (d_rev is None) or (b_rev and d_rev and b_rev != d_rev):
        hard.append('[pubinfo-mismatch] %s 修订日期 文内 %s ≠ baseline %s'
                    % (rel, fmt_zh(d_rev) if d_rev else '（无）',
                       fmt_zh(b_rev) if b_rev else '（无）'))


def check_footnotes(ne, rel, hard, cross_refs=None, biblio_span=None):
    refs, defs = {}, {}
    fence = False
    for lineno, line in ne:
        s = line.strip()
        if s.startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        dm = RE_FOOTDEF.match(s)
        if dm:
            defs.setdefault(dm.group(1), lineno)
            continue
        for m in RE_FOOTREF.finditer(line):
            refs.setdefault(m.group(1), lineno)
    for key, lineno in sorted(refs.items()):
        if key not in defs:
            hard.append('[orphan-ref] %s:%d 脚注引注 [^%s] 无文末定义' % (rel, lineno, key))
    for key, lineno in sorted(defs.items()):
        if key not in refs:
            # 跨文件引用豁免：SEP 的脚注定义可被同词条补充材料引用
            # （notes.html#note-N 出现在 en/<slug>/*.html 中），主文定义非孤儿
            if cross_refs and key in cross_refs:
                continue
            # 引用注释方案豁免："参考文献"节内的定义即文献表条目本身
            # （转换器把整份文献表转为 [^key]: 定义，文内标记只挂已链接的引用组），
            # 未被文内引用的条目是文献表的自然组成部分，非孤儿
            if biblio_span and biblio_span[0] <= lineno and (biblio_span[1] is None or lineno < biblio_span[1]):
                continue
            hard.append('[orphan-def] %s:%d 文末定义 [^%s]: 无正文引用' % (rel, lineno, key))


def check_tasks(tasks_dir, hard, warns, records=None):
    n = 0
    if not os.path.isdir(tasks_dir):
        warns.append('[task-dir-missing] 任务目录不存在：%s' % tasks_dir)
        return 0
    base = os.path.dirname(tasks_dir)
    for dirpath, _dirnames, filenames in os.walk(tasks_dir):
        for fn in sorted(filenames):
            if not fn.endswith('.json'):
                continue
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, encoding='utf-8') as fh:
                    rec = json.load(fh)
            except (OSError, ValueError) as exc:
                warns.append('[task-parse-failed] %s（%s）' % (norm_rel(fp, base), exc))
                continue
            if not isinstance(rec, dict) or 'slug' not in rec or 'state' not in rec:
                continue
            n += 1
            rel = norm_rel(fp, base)
            if str(rec.get('kind') or '') == 'glossary-maintenance':
                # 非词条翻译任务（词汇表维护等）无 SEP 版本可钉，不要求 version_pin
                continue
            missing = [k for k in PIN_FIELDS
                       if not str((rec.get('version_pin') or {}).get(k) or '').strip()]
            # 上游无存档史的词条（新首发，baseline archinfo 为空）合法缺失
            # archive_edition——pubinfo_date + sha256 已足够钉版本
            if 'archive_edition' in missing:
                slug = str(rec.get('slug') or '')
                recs = [e for e in records if str(e.get('slug') or '') == slug]
                if recs and not (recs[0].get('archive_edition')
                                 or (recs[0].get('archinfo') or {}).get('latest_edition')):
                    missing.remove('archive_edition')
            if missing:
                hard.append('[task-pin-missing] %s version_pin 缺 %s' % (rel, '/'.join(missing)))
            if str(rec.get('state')) == 'done':
                steps = rec.get('steps') or []
                if len(steps) < DONE_MIN_STEPS:
                    hard.append('[task-evidence-missing] %s done 任务仅 %d 步（应 ≥%d）'
                                % (rel, len(steps), DONE_MIN_STEPS))
                for st in steps:
                    if not str((st or {}).get('evidence') or '').strip():
                        hard.append('[task-evidence-missing] %s 步骤 %s 缺 evidence'
                                    % (rel, (st or {}).get('step', '?')))
    return n


def collect_docs(root):
    docs = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        parts = [] if rel_dir == '.' else rel_dir.split(os.sep)
        if parts and (parts[0] in EXCLUDE_DIRS or rel_dir.startswith('.')):
            dirnames[:] = []
            continue
        for fn in sorted(filenames):
            if not fn.endswith('.md') or fn in EXCLUDE_FILES:
                continue
            docs.append(os.path.join(dirpath, fn))
    return sorted(docs)


def check_one_doc(fp, root, by_zh_doc, records, hard, warns, stats):
    rel = norm_rel(fp, root)
    try:
        with open(fp, encoding='utf-8') as fh:
            lines = fh.read().splitlines()
    except OSError as exc:
        warns.append('[read-failed] %s（%s）' % (rel, exc))
        return
    ne = [(i, l) for i, l in enumerate(lines, 1) if l.strip()]
    if not ne or not ne[0][1].startswith('# '):
        stats['nonentry'] += 1
        return
    if len(ne) <= STUB_BODY_LINES:
        stats['stub'] += 1
        return
    stats['entry'] += 1
    # 补充材料豁免（specs/007 审阅实证）：`<slug>.<x>.md` 形态的补充文件按模板
    # 不设独立参考文献/学术工具节（主词条承载），亦无独立 baseline 记录
    stem = os.path.basename(rel)[:-3] if rel.endswith('.md') else ''
    is_supp = '.' in stem and not rel.startswith(('en/', 'yuanwen/'))
    rec = resolve_record(rel, by_zh_doc, records, warns)
    pubinfo = check_doc(rel, ne, warns, is_supp=is_supp)
    if is_supp:
        pass  # 参考文献节/学术工具节/版本钉均由主词条承载
    elif rec:
        check_pubinfo(rel, pubinfo, rec, hard, warns)
    else:
        warns.append('[baseline-lookup-miss] %s 未能在 baseline 定位，pubinfo 不核' % rel)
    # 跨文件脚注引用：词条包内（含补充材料）对 notes.html#note-N 的引用
    cross_refs = set()
    slug = os.path.basename(rel)[:-3] if rel.endswith('.md') else ''
    en_dir = os.path.join(root, 'en', slug)
    if slug and os.path.isdir(en_dir):
        for fn in os.listdir(en_dir):
            if not fn.endswith('.html'):
                continue
            try:
                t = open(os.path.join(en_dir, fn), encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            cross_refs.update(re.findall(r'notes\.html#([A-Za-z0-9_-]+)', t))
    heads2 = []
    for lineno, line in ne:
        m2 = RE_HEADING.match(line.strip())
        if m2:
            heads2.append((lineno, len(m2.group(1)), m2.group(2)))
    biblio_span = find_biblio_span(heads2)
    check_footnotes(ne, rel, hard, cross_refs, biblio_span)


def main(argv=None):
    ap = argparse.ArgumentParser(description='学术规范门禁（specs/003）')
    ap.add_argument('--docs', nargs='*', help='定点检查指定文档（不查任务）')
    ap.add_argument('--strict', action='store_true', help='告警升硬错误')
    ap.add_argument('--root', default=ROOT, help='仓库根（测试注入）')
    ap.add_argument('--baseline', default=os.path.join(ROOT, 'baseline', 'entries.json'))
    ap.add_argument('--tasks-dir', default=os.path.join(ROOT, 'tasks'))
    args = ap.parse_args(argv)

    hard, warns = [], []
    stats = {'entry': 0, 'stub': 0, 'nonentry': 0}
    by_zh_doc, records = load_baseline(args.baseline)

    if args.docs is not None:
        paths = []
        for p in args.docs:
            fp = os.path.abspath(p)
            if not os.path.isfile(fp):
                print('用法错误：文档不存在 %s' % p)
                return 2
            paths.append(fp)
        for fp in paths:
            check_one_doc(fp, args.root, by_zh_doc, records, hard, warns, stats)
        n_tasks = None
    else:
        for fp in collect_docs(args.root):
            check_one_doc(fp, args.root, by_zh_doc, records, hard, warns, stats)
        n_tasks = check_tasks(args.tasks_dir, hard, warns, records)

    if args.strict and warns:
        hard.extend(warns)
        warns = []

    tag = '（--strict）' if args.strict else ''
    print('学术规范门禁（specs/003，rules/07）%s：非存根词条 %d | 存根跳过 %d | 非词条跳过 %d%s'
          % (tag, stats['entry'], stats['stub'], stats['nonentry'],
             '' if n_tasks is None else ' | 任务 JSON %d' % n_tasks))
    if hard:
        kinds = {}
        for line in hard:
            kind = line[1:line.index(']')]
            kinds[kind] = kinds.get(kind, 0) + 1
        print('硬错误 %d（%s）' % (len(hard),
                                  ' + '.join('%s %d' % kv for kv in sorted(kinds.items()))))
        for line in hard:
            print('  ' + line)
    if warns:
        print('告警 %d（--strict 时升为硬错误）' % len(warns))
        for line in warns:
            print('  ' + line)
    if hard:
        print('学术规范硬错误 %d 处，退出码 1' % len(hard))
        return 1
    print('OK：学术规范无硬错误%s' % ('（含 %d 处告警）' % len(warns) if warns else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
