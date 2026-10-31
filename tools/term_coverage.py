# -*- coding: utf-8 -*-
"""术语落地全覆盖核验（specs/008 常态流程，2026-10-31）。

对每个非存根词条：扫描英文源（yuanwen 镜像，References 尾部裁剪）中出现的
登记册术语（词边界、变音符折叠、允许尾 s 复数），再查中文译文是否含任一
登记变体（check_terms.translations 口径：主形+亦作+译作+书名号）。
EN 出现而中文零变体 → 「未落实」缺口（只报告不修改）。

用法:
  python tools/term_coverage.py                    # 全部非存根词条
  python tools/term_coverage.py a/abduction.md ... # 指定词条
退出码: 0 无缺口或仅报告；2 参数错误。
"""
import io
import glob
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
from tools import check_terms  # noqa: E402


def fold(text):
    """登记/匹配统一折叠键：NFD 剥组合记号 + casefold + 空白归一。"""
    s = unicodedata.normalize('NFD', text.replace('*', '').strip())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).casefold()


def en_pattern(en_key):
    """英文源匹配模式：词边界 + 多词内空白弹性 + 可选尾 s 复数。"""
    body = re.escape(en_key).replace(r'\ ', r'\s+')
    return re.compile(r'(?<![A-Za-z\u00C0-\u024F])' + body + r's?(?![A-Za-z])')


def nonstub_docs():
    docs = []
    for p in sorted(glob.glob(os.path.join(ROOT, '[a-z1]', '*.md'))):
        body = [l for l in open(p, encoding='utf-8') if l.strip()]
        if len(body) > 10:
            docs.append(os.path.relpath(p, ROOT).replace(os.sep, '/'))
    return docs


def load_en(doc):
    """英文源：中文词条路径 → yuanwen 镜像；References 尾部裁剪。"""
    slug = os.path.basename(doc)[:-3]
    letter = doc.split('/')[0]
    en_path = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    if not os.path.exists(en_path):
        return ''
    text = open(en_path, encoding='utf-8', errors='replace').read()
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)
    # 补充材料源头行（plato.stanford.edu URL）与站点框架行剔除
    text = '\n'.join(l for l in text.split('\n')
                     if 'plato.stanford.edu' not in l)
    return re.split(r'\n## (?:References|Bibliography|Academic Tools|'
                    r'Other Internet Resources|Related Entries)[^\n]*\n',
                    text)[0]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    docs = argv or nonstub_docs()
    # 登记册两表 → [(fold(原文), 变体集, 原文, 表)]
    entries = []
    for path, label in ((os.path.join(ROOT, 'yi-zhe-shuo-ming.md'), '术语'),
                        (os.path.join(ROOT, 'ren-ming-biao.md'), '人名')):
        rows, _ = check_terms.parse_registry(path)
        for term, trans, first_seen, basis, row_date, lineno in rows:
            variants = check_terms.translations(trans)
            en_key = check_terms.norm_key(term)
            if not en_key or len(en_key) < 2:
                continue
            entries.append((en_key, variants, term, label, first_seen))
    entries.sort(key=lambda e: -len(e[0]))  # 长词优先，短词不遮蔽长词命中

    flags = {}
    checked = 0
    for doc in docs:
        zh_path = os.path.join(ROOT, doc)
        if not os.path.exists(zh_path):
            continue
        zh_text = open(zh_path, encoding='utf-8').read()
        en_text = fold(load_en(doc))
        if not en_text:
            continue
        checked += 1
        seen_in_doc = set()
        for en_key, variants, term, label, first_seen in entries:
            if en_key in seen_in_doc:
                continue
            m = en_pattern(en_key).search(en_text)
            if m:
                seen_in_doc.add(en_key)
                found = [v for v in variants if v and v in zh_text]
                if not found:
                    s = max(0, m.start() - 50)
                    ctx = re.sub(r'\s+', ' ', en_text[s:m.end() + 50]).strip()
                    flags.setdefault(doc, []).append(
                        (label, term, '／'.join(sorted(variants))[:60], first_seen, ctx))
    total = sum(len(v) for v in flags.values())
    print('词条 %d 个 | 登记行 %d | 未落实缺口 %d 处' % (checked, len(entries), total))
    for doc in sorted(flags):
        for label, term, vs, first_seen, ctx in flags[doc]:
            print('  [%s] %s 「%s」未见于 %s' % (label, term, vs, doc))
            print('      EN: …%s…' % ctx)
    return 0


if __name__ == '__main__':
    sys.exit(main())
