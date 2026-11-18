# -*- coding: utf-8 -*-
"""候选池全量 A/B/C 分档提议（specs/050 §6；rules/03 分档裁定的机器提议半）。

机检为筛、人审为判（ADR-0070）：本工具只给每条的**建议档位与理由**，不登记、不译名。
裁定与译名仍由人逐条给出（A 档凭通行译法直裁 / B 档联网查证后裁 / C 档挂起或驳回）。

档位提议口径：
  A（教科书级标准术语候选，建议优先直裁）
    · -ism 词族（学说名）；或
    · foreign 纯原文（无非拉丁混排，如 Wirklichkeit/dasein）；或
    · 任一词元含术语后缀（-ism/-ology/-tion/-ity/-ness/-ship/-ment/-ence/-ance… 且 freq≥3）
  P（人名，建议转人名表 workflow，不属术语档）
    · type=person
  C（挂起/驳回候选）
    · type=topic（标题/节名，非原子术语）；或
    · 单 token、首字母大写、无术语后缀（书名/刊名候选，ADR-0011）；或
    · phrase/quoted freq≥100 且全词元为普通词（漏网泛搭配）
  B（需核，默认）
    · 其余（多词无后缀短语、多词引语、斜体多词、ascii 外语、希腊/汉/阿等）

用法:
  python tools/term_grade.py            # 产出 results/grade-<日期>.json + .md
  python tools/term_grade.py --pool <p> --out <dir>
退出码: 0 完成；2 路径错误。
"""
import io
import json
import os
import sys
from collections import Counter, defaultdict

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools import term_harvest as th  # noqa: E402

POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')
OUT = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results')


def grade(c):
    en = c.get('en', '')
    typ = c.get('type', '')
    freq = c.get('freq', 0)
    toks = th.WORD_RE.findall(en)
    low = [t.casefold() for t in toks]
    if typ == 'person':
        return 'P', '人名（type=person）'
    # A
    if typ == 'ism':
        return 'A', '-ism 学说名'
    if typ == 'foreign':
        has_ascii_lower = any(__import__('re').fullmatch(r"[a-z][a-z'\-]*", t) for t in toks)
        has_nonascii = any(ord(ch) > 127 for ch in en)
        # 纯原文术语：非拉丁扩展 / 德语名词后缀 / 经典词小词典（Wirklichkeit 类 ASCII 德语名词
        # 靠 GERMAN_SUFFIX_RE 与 FOREIGN_LEXICON 兜住）
        if (has_nonascii and not has_ascii_lower) \
                or th.GERMAN_SUFFIX_RE.search(en) \
                or en.casefold() in th.FOREIGN_LEXICON:
            return 'A', 'foreign 纯原文术语'
    if typ != 'topic' and toks:
        for t in toks:
            m = th.RE_TERM_SUFFIX.search(t)
            # 词干须 ≥3 字符：防 unity→un+ity、importance 类短干误判
            if m and len(t[:m.start()]) >= 3 and freq >= 3:
                return 'A', '术语后缀（%s）' % t
    # C
    if typ == 'topic':
        return 'C', '标题/节名（topic）'
    if len(toks) == 1 and en[:1].isupper() and not th.RE_TERM_SUFFIX.search(low[0]) \
            and not th.NONASCII_LATIN.search(en):
        return 'C', '单 Token 大写（书名/刊名候选，ADR-0011）'
    if typ in ('phrase', 'quoted') and freq >= 100 and low \
            and all(w in th.COMMON_SINGLE for w in low):
        return 'C', '高频全普通词（泛搭配）'
    # B
    return 'B', '需核'


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    pool_path, out_dir = POOL, OUT
    i = 0
    while i < len(argv):
        if argv[i] == '--pool':
            pool_path, i = argv[i + 1], i + 1
        elif argv[i] == '--out':
            out_dir, i = argv[i + 1], i + 1
        i += 1
    if not os.path.exists(pool_path):
        print('候选池缺失: %s' % pool_path)
        return 2
    pool = json.load(open(pool_path, encoding='utf-8'))
    buckets = defaultdict(list)
    counts = Counter()
    bytype = defaultdict(Counter)
    for c in pool.get('candidates', []):
        if not str(c.get('status', '')).startswith('new'):
            continue
        b, reason = grade(c)
        counts[b] += 1
        bytype[b][c.get('type', '')] += 1
        buckets[b].append({'en': c.get('en', ''), 'type': c.get('type', ''),
                           'freq': c.get('freq', 0), 'reason': reason})
    for b in buckets:
        buckets[b].sort(key=lambda x: -x['freq'])
    total = sum(counts.values())
    print('=== A/B/C 分档提议（共 %d 条 new）===' % total)
    for b in ('A', 'B', 'C', 'P'):
        print('  %s: %d（%s）' % (b, counts.get(b, 0),
                                ' '.join('%s=%d' % (k, v) for k, v in bytype[b].most_common())))
    today = __import__('datetime').date.today().isoformat()
    manifest = {'date': today, 'script': 'tools/term_grade.py',
                'pool': os.path.relpath(pool_path, ROOT), 'total_new': total,
                'counts': dict(counts),
                'bytype': {b: dict(t) for b, t in bytype.items()},
                'buckets': {b: buckets[b] for b in ('A', 'B', 'C', 'P')}}
    os.makedirs(out_dir, exist_ok=True)
    jp = os.path.join(out_dir, 'grade-%s.json' % today)
    tmp = jp + '.tmp'
    json.dump(manifest, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    os.replace(tmp, jp)
    # 人读摘要
    lines = ['# 候选池 A/B/C 分档提议 %s' % today, '',
             '机检为筛、人审为判：下列为**建议档位**，登记与译名仍由人逐条裁定'
             '（A 直裁 / B 查证 / C 挂起或驳）。合计 new %d 条。' % total, '',
             '| 档 | 条数 | 按 type |', '| ---- | ---- | ---- |']
    for b in ('A', 'B', 'C', 'P'):
        lines.append('| %s | %d | %s |' % (b, counts.get(b, 0),
                     '，'.join('%s %d' % (k, v) for k, v in bytype[b].most_common())))
    for b in ('A', 'B', 'C', 'P'):
        lines += ['', '## %s 档样例（前 40，按 freq 降序）' % b, '']
        for r in buckets[b][:40]:
            lines.append('* [%s|%s] %s' % (r['type'], r['freq'], r['en']))
    md = '\n'.join(lines) + '\n'
    mp = os.path.join(out_dir, 'grade-%s.md' % today)
    tmp2 = mp + '.tmp'
    with open(tmp2, 'w', encoding='utf-8', newline='\n') as f:
        f.write(md)
    os.replace(tmp2, mp)
    print('  → %s' % jp)
    print('  → %s' % mp)
    return 0


if __name__ == '__main__':
    sys.exit(main())
