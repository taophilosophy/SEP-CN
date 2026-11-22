# -*- coding: utf-8 -*-
"""specs/058 补登选料：从全量总表挑出高置信未登记候选，产出查证队列与评审表。

用法:
  python specs/058-term-full-reextraction/bin/select_register.py [--top 300]

输出:
  specs/058-term-full-reextraction/results/register-queue.json    查证队列（[{en}]）
  specs/058-term-full-reextraction/results/register-review.tsv    评审表（人读）
"""
import argparse
import collections
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.register_lib import (norm_key, norm_key_quote, parse_registry2_full,  # noqa: E402
                                parse_registry_full, person_path, term_path)

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
CAND = os.path.join(RES, 'candidates.json.gz')
POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')

# 泛搭配黑名单（池内已见高频噪声；语义判定前的机械拦截）
GENERIC = set(
    'important role|central role|physical world|physical objects|moral principles|'
    'philosophical work|true belief|human beings|natural sciences|causal relations|'
    'morally responsible|twentieth century|public opinion|social sciences|mental states|'
    'possible worlds|rational agent|moral truths|human nature|moral judgment|'
    'logical truths|conceptual scheme|mental properties|first principles|'
    'scientific theories|normative claims|rational agents|value judgments|'
    'empirical claims|human action|moral facts|philosophical problems|'
    'conceptual analysis|philosophical tradition|philosophical views|moral reasoning|'
    'human conduct|moral theory|western philosophy|contemporary philosophy|'
    'early modern|moral knowledge|rational belief|empirical knowledge|'
    'conceptual truths|philosophical inquiry|philosophical reflection|human experience|'
    'philosophical position|philosophical issue|common sense|ordinary language|'
    'logical form|natural property|mental representation|linguistic expression|'
    'scientific explanation|causal process|causal efficacy|external world|'
    'sensory experience|logical consequence|semantic value|truth value|'
    'propositional attitude|intentional object|physical event|mental event|'
    'social construct|political institution|legal system|moral obligation|'
    'practical reason|theoretical reason|human mind|cognitive process|language use|'
    'belief system|concept system|ancient philosophy|medieval philosophy|'
    'modern philosophy'.split('|'))
# 泛短语首/尾词（仅作用于 phrase 型；宁可漏报，不把泛搭配写进登记册）
PH_HEAD = set('''certain various another other some any both each every most many
few several different similar particular specific same new old good bad best
better well more less very quite rather such this that these those its their
our his her one two three first second third last next recent large small
infinite finite'''.split())
PH_TAIL = set('''case cases way ways form forms kind kinds sort sorts type types
number numbers variety else upon known understood related speaking point points
thing things part parts fact facts view views issue issues question questions
answer answers literature work works year years century centuries time times
people person persons something anything nothing example examples'''.split())


def variants(k):
    """折叠键的单复数近形（只用于查重跳过，不用于登记）。"""
    yield k
    if k.endswith('ies'):
        yield k[:-3] + 'y'
    if k.endswith('es'):
        yield k[:-2]
    if k.endswith('s'):
        yield k[:-1]
    yield k + 's'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--top', type=int, default=300)
    ap.add_argument('--group', default='all',
                    choices=['all', 'terms', 'persons', 'works'])
    args = ap.parse_args()

    import gzip
    with gzip.open(CAND, 'rb') as f:
        d = json.loads(f.read().decode('utf-8'))
    pool = {}
    for c in json.load(open(POOL, encoding='utf-8'))['candidates']:
        st = c.get('status', 'new')
        pool[norm_key(c['en'])] = st
        pool.setdefault(norm_key_quote(c['en']), st)
    terms = {norm_key_quote(r[0]) for r in parse_registry_full(term_path())[0]}
    # 登记册允许 "A / B" 合写；拆成别名，防同一概念换形重复入队
    alias = set()
    for k in terms:
        for part in k.split('/'):
            alias.add(part.strip())
    terms |= alias
    persons = {norm_key_quote(r[0]) for r in parse_registry2_full(person_path())[0]}

    picked = []
    allow = {'terms': {'term', 'phrase'}, 'persons': {'person'},
             'works': {'work'}}.get(args.group)
    skipped_decided = 0
    for c in d['candidates']:
        if c['status'].startswith('已登记'):
            continue
        ps = pool.get(c['key'], '')
        if ps.startswith(('rejected', 'held', 'published')):
            skipped_decided += 1
            continue
        if c['type'] not in ('term', 'phrase', 'work', 'person'):
            continue
        if allow and c['type'] not in allow:
            continue
        if c['tier'] not in ('T1', 'T2'):
            continue
        en = c['en']
        key = ' '.join(en.split())
        if key.casefold() in GENERIC:
            continue
        if c['type'] == 'phrase':
            low = [w.casefold().strip('.,;:') for w in key.split()]
            if low[0] in PH_HEAD or low[-1] in PH_TAIL:
                continue
            if re.search(r'(?i)\b(?:published|updated)\b', key):
                continue
        if not re.search(r'[A-Za-z\u0370-\u03FF\u0600-\u06FF]', en):
            continue
        if len(en) > 60:
            continue
        if c['type'] == 'person':
            if c['key'] in persons:
                continue
        else:
            if any(v in terms or v in persons for v in variants(c['key'])):
                continue
        score = c['freq'] * (1 + min(c['spread'], 40))
        if c['type'] == 'phrase':
            score *= 1.5
        picked.append((score, c))
    picked.sort(key=lambda x: -x[0])
    picked = picked[:args.top]

    queue = [{'en': c['en']} for _, c in picked]
    suffix = '' if args.group == 'all' else '-' + args.group
    json.dump(queue, open(os.path.join(RES, 'register-queue%s.json' % suffix), 'w',
                          encoding='utf-8'), ensure_ascii=False, indent=1)
    lines = ['score\ttype\tfreq\tspread\ttier\tpool_status\ten\tsources']
    for s, c in picked:
        lines.append('%d\t%s\t%d\t%d\t%s\t%s\t%s\t%s' % (
            s, c['type'], c['freq'], c['spread'], c['tier'],
            pool.get(norm_key(c['en']), '-'), c['en'],
            '；'.join(c['sources'][:3])))
    io.open(os.path.join(RES, 'register-review%s.tsv' % suffix), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('候选 %d → 队列 %d；已裁定跳过 %d；类型分布 %s'
          % (len(d['candidates']), len(picked), skipped_decided,
             collections.Counter(c['type'] for _, c in picked).most_common()))


if __name__ == '__main__':
    main()
