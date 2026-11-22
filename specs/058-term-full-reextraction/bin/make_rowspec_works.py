# -*- coding: utf-8 -*-
"""生成著作名批次 rowspec（审定库无对口，依据=权威译本）。"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.register_lib import norm_key_quote, parse_registry_full, term_path  # noqa: E402

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
BASIS = {
    'Philosophical Investigations':
        '权威译本（陈嘉映译《哲学研究》通行汉译；审定库无对口条目，2026-11-22）；凭证 2026-11-22',
    'Theory of Justice':
        '权威译本（何怀宏等译《正义论》，中国社会科学出版社；审定库无对口条目，2026-11-22）；凭证 2026-11-22',
    'Treatise of Human Nature':
        '权威译本（关文运译《人性论》，商务印书馆；审定库无对口条目，2026-11-22）；凭证 2026-11-22',
    'Principles of Philosophy':
        '权威译本（商务印书馆汉译名著《哲学原理》；审定库无对口条目，2026-11-22）；凭证 2026-11-22',
    'Politics':
        '权威译本（吴寿彭译《政治学》，商务印书馆；审定库无对口条目，2026-11-22）；凭证 2026-11-22',
    'Laws':
        '权威译本（柏拉图《法律篇》通行汉译；审定库无对口条目，2026-11-22）；凭证 2026-11-22',
    'Summa theologiae':
        '权威译本（《神学大全》通行汉译；审定库无对口条目，2026-11-22）；凭证 2026-11-22',
}
alias = set()
for r in parse_registry_full(term_path())[0]:
    for part in r[0].split('/'):
        alias.add(norm_key_quote(part.strip()))
rows = []
for line in open(os.path.join(RES, 'curated-works.tsv'), encoding='utf-8'):
    if not line.strip():
        continue
    en, zh = line.rstrip('\n').split('\t')
    if norm_key_quote(en) in alias:
        print('skip alias:', en)
        continue
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': BASIS.get(en, '权威译本（通行汉译）；凭证 2026-11-22'),
                 'date': '2026-11-22'})
json.dump({'batch': '058-batch3-works', 'date': '2026-11-22',
           'scope': '著作名批次（术语在线无对口命中，依据权威译本）',
           'rows': rows},
          open(os.path.join(RES, 'rowspec-batch3-works.json'), 'w',
               encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('works rows', len(rows))
