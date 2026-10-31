# -*- coding: utf-8 -*-
"""三表术语关系审计（specs/008 常态流程，2026-10-31）。

四类关系，只报告不修改：
  ①重名    不同登记键撞同一中文主形（跨行/跨表），附各自原文供消歧裁决；
  ②别名    归并行（主形 / 他形）与 亦作/译作 链计数——按设计存在，列清单备查；
  ③一词多义 译法主形含 ≥2 个分号义（多义行），列出供语境核销；
  ④匿名    已译词条英文源中出现（freq≥2）而登记册未收录的候选术语
            （harvest-cache 单篇缓存为源，先登记后使用合规审计）。

用法:
  python tools/term_relations.py                       # 全部非存根词条
  python tools/term_relations.py a/abelard.md ...      # 指定词条
  python tools/term_relations.py --out <file>          # 报告落盘
退出码: 0 完成。
"""
import io
import glob
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
from tools import check_terms  # noqa: E402

REG = os.path.join(ROOT, 'yi-zhe-shuo-ming.md')
REN = os.path.join(ROOT, 'ren-ming-biao.md')
GLO = os.path.join(ROOT, 'qian-yan', 'ci-hui-biao.md')
CACHE = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                     'harvest-cache')


def fold(text):
    s = unicodedata.normalize('NFD', text.replace('*', '').strip())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).casefold()


def main_forms(trans):
    """译法主形（注记前），按 / ／ ； 、 拆多义。"""
    head = trans.split('（')[0].strip()
    return [v.strip() for v in re.split(r'[/／；、;，]', head) if v.strip()]


def load_tables():
    """两登记册 + 词汇表 → 行列表。"""
    out = []
    for path, label in ((REG, '术语'), (REN, '人名')):
        lines = io.open(path, encoding='utf-8', newline='').read().split('\n')
        for i, l in enumerate(lines):
            if not l.startswith('| ') or '----' in l:
                continue
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if len(cells) < 2 or not cells[0] \
                    or cells[0].casefold() in ('原文', 'term') \
                    or set(cells[0]) <= set(':-— '):
                continue
            out.append({'table': label, 'line': i + 1, 'term': cells[0],
                        'trans': cells[1], 'forms': main_forms(cells[1]),
                        'row': cells})
    return out


def nonstub_docs():
    docs = []
    for p in sorted(glob.glob(os.path.join(ROOT, '[a-z1]', '*.md'))):
        body = [l for l in open(p, encoding='utf-8') if l.strip()]
        if len(body) > 10:
            docs.append(os.path.relpath(p, ROOT).replace(os.sep, '/'))
    return docs


def load_en(doc):
    slug = os.path.basename(doc)[:-3]
    en_path = os.path.join(ROOT, 'yuanwen', doc.split('/')[0], slug + '.md')
    if not os.path.exists(en_path):
        return ''
    text = open(en_path, encoding='utf-8', errors='replace').read()
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)
    text = '\n'.join(l for l in text.split('\n')
                     if 'plato.stanford.edu' not in l)
    return re.split(r'\n## (?:References|Bibliography|Academic Tools|'
                    r'Other Internet Resources|Related Entries)[^\n]*\n',
                    text)[0]


def en_pattern(en_key):
    body = re.escape(en_key).replace(r'\ ', r'\s+')
    return re.compile(r'(?<![A-Za-z\u00C0-\u024F])' + body + r's?(?![A-Za-z])')


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    out_path = None
    if '--out' in argv:
        out_path = argv[argv.index('--out') + 1]
        argv = [a for a in argv if a != '--out' and a != out_path]
    docs = argv or nonstub_docs()

    tables = load_tables()
    rep = ['=== 术语关系审计 %s | 词条 %d | 登记行 %d ==='
           % (__import__('datetime').date.today().isoformat(), len(docs),
              len(tables))]

    # ① 重名：中文主形 → 多登记键
    zh_index = {}
    for e in tables:
        for f in e['forms']:
            zh_index.setdefault(f, []).append(e)
    collisions = {f: es for f, es in zh_index.items() if len(es) > 1}
    rep.append('')
    rep.append('## ① 重名（同一中文主形 ↔ 多登记键）：%d 组' % len(collisions))
    for f in sorted(collisions):
        es = collisions[f]
        keys = '；'.join('%s[%s L%d]' % (e['term'], e['table'], e['line'])
                         for e in es)
        rep.append('  「%s」← %s' % (f, keys))

    # ② 别名：归并行与亦作链（按设计存在，计数备查）
    slash_rows = [e for e in tables if '/' in e['term']]
    ye_zuo = [e for e in tables if re.search(r'亦作[“"]', e['trans'])]
    rep.append('')
    rep.append('## ② 别名：归并行 %d 行 | 含亦作链 %d 行（设计内，不构成缺口）'
               % (len(slash_rows), len(ye_zuo)))
    for e in slash_rows[:12]:
        rep.append('  归并: %s → %s' % (e['term'], e['forms'][0] if e['forms'] else ''))

    # ③ 一词多义：主形 ≥2 义的行
    poly = [e for e in tables if len(e['forms']) >= 2]
    rep.append('')
    rep.append('## ③ 一词多义（主形 ≥2 义，按语境分行使用）：%d 行' % len(poly))
    for e in poly[:25]:
        rep.append('  %s[%s] = %s' % (e['term'], e['table'], '；'.join(e['forms'])))

    # ④ 匿名：已译词条英文源出现（freq≥2）而登记册未收录
    rep.append('')
    rep.append('## ④ 匿名（译文使用而登记册未收录，freq≥2）')
    anon_total = 0
    for doc in sorted(docs):
        slug = os.path.basename(doc)[:-3]
        letter = doc.split('/')[0]
        cache_p = os.path.join(CACHE, '%s.%s.json' % (letter, slug))
        if not os.path.exists(cache_p):
            continue
        cache = json.load(open(cache_p, encoding='utf-8'))
        reg_keys = set()
        for e in tables:
            reg_keys.add(fold(e['term']))
            for part in re.split(r'\s*/\s*', e['term']):
                if part.strip():
                    reg_keys.add(fold(part))
        cands = []
        for k, cnt in cache.get('counts', {}).items():
            if cnt < 2:
                continue
            typ = cache.get('types', {}).get(k, 'phrase')
            if typ in ('phrase', 'italic', 'ism', 'topic') and k not in reg_keys:
                cands.append((cnt, cache.get('forms', {}).get(k, k), typ))
        cands.sort(reverse=True)
        if cands:
            anon_total += len(cands)
            rep.append('  %s：%d 个' % (doc, len(cands)))
            for cnt, form, typ in cands[:10]:
                rep.append('    %d× [%s] %s' % (cnt, typ, form))
    rep.append('  匿名合计：%d 个（低频尾部随词条翻译核定）' % anon_total)

    report = '\n'.join(rep)
    print(report)
    if out_path:
        with io.open(out_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(report + '\n')
        print('报告落盘：%s' % out_path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
