# -*- coding: utf-8 -*-
"""specs/058 首批落册：人工译法＋审定库凭证 → term_flow rowspec。

用法:
  python specs/058-term-full-reextraction/bin/make_rowspec_curated.py
输出:
  specs/058-term-full-reextraction/results/rowspec-batch1.json
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.cnki_query import safe_key  # noqa: E402
from tools.register_lib import (norm_key_quote, parse_registry_full,  # noqa: E402
                                term_path)

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
QD = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                  'queries', 'termonline-all')
PHIL = ('哲学', '自然辩证法', '逻辑', '伦理', '美学', '宗教', '心理', '语言',
        '科学哲学', '技术哲学', '认知科学', '马克思主义', '外国哲学', '思维',
        '方法论', '辩证法')


def main():
    rows = []
    stats = {'hit': 0, 'empty': 0, 'other': 0, 'nocred': 0, 'skip_alias': 0}
    # 登记册键允许 "A / B" 合写；按斜杠拆成别名，防同一著作/术语重复登记
    alias = set()
    for r in parse_registry_full(term_path())[0]:
        for part in r[0].split('/'):
            alias.add(norm_key_quote(part.strip()))
    for line in open(os.path.join(RES, 'curated-translations.tsv'),
                     encoding='utf-8'):
        if not line.strip():
            continue
        en, zh = line.rstrip('\n').split('\t')
        if norm_key_quote(en) in alias:
            stats['skip_alias'] += 1
            continue
        path = os.path.join(QD, safe_key(norm_key_quote(en)) + '.json')
        doc = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
        hits = doc.get('hits') or []
        exact = [h for h in hits if (h.get('en') or '').strip().casefold()
                 == en.casefold()]
        aligned = [h for h in exact if h.get('cn') == zh]
        if aligned:
            h = aligned[0]
            basis = '审定名词库（%s%s%s%s；凭证 2026-11-22）' % (
                h.get('source') or '',
                '·' + (h.get('subjectFullName') or '') if h.get('subjectFullName') else '',
                '，' + (h.get('publishYear') or '') if h.get('publishYear') else '',
                '，' + (h.get('wordNumber') or '') if h.get('wordNumber') else '')
            stats['hit'] += 1
        else:
            if not doc:
                why = '无凭证'
                stats['nocred'] += 1
            elif not hits:
                why = '审定库查无对应条目'
                stats['empty'] += 1
            else:
                why = '审定库命中他义或形不完全一致，未采'
                stats['other'] += 1
            basis = ('学界通行（教科书级标准术语，specs/058 A 档直裁；%s；'
                     '凭证 2026-11-22）' % why)
        rows.append({'en': en, 'zh': zh, 'table': 'term',
                     'first_seen': '语料回收（specs/058 全库提取）',
                     'basis': basis, 'date': '2026-11-22'})
    out = {'batch': '058-batch1', 'date': '2026-11-22',
           'scope': '全库提取高置信术语首批（人工逐条定译，审定库凭证对齐）',
           'evidence': 'specs/008-terminology-campaign/results/queries/termonline-all/',
           'rows': rows}
    path = os.path.join(RES, 'rowspec-batch1.json')
    json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('rows=%d %s' % (len(rows), stats))


if __name__ == '__main__':
    main()
