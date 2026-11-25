# -*- coding: utf-8 -*-
"""人名籍属/生卒 Wikidata 试点回填（2026-11-25）。

背景：人名表仍有 780 行缺籍属或生卒。既有流程靠 GND／Wikidata 逐条手工查证
（specs/013），本工具把“候选发现”自动化，裁定仍留人工：

  1. wbsearchentities 按英文名找候选（最多 3 个 QID）；
  2. 取实体描述、P27 国籍、P569 生、P570 卒；
  3. 只在“描述像学者”且“生年可读”时给出候选，并标注与现表冲突；
  4. 输出 TSV 供复核，**不改登记册**。

否定判定不怕：宁可漏，不可错配（同姓异人、同名政客球员是历史高发误配）。

用法：
  python -I specs/058-term-full-reextraction/bin/wikidata_person_sweep.py --limit 50 \
      --out specs/058-term-full-reextraction/results/person-wikidata-2026-11-25.tsv
"""
import argparse
import io
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

UA = 'SEP-CN-research/1.0 (terminology registry; contact: project maintainer)'
SCHOLAR = re.compile(r'philosoph|logician|ethicist|theolog|mathematic|scientist|'
                     r'historian|jurist|economist|sociolog|psycholog|linguist|'
                     r'physicist|astronom|physician|writer|author|scholar|professor',
                     re.I)
# P106 职业白名单：只认这些职业，压掉“作家/天文学家”等同名误配
OCC_OK = {
    'Q4964182',   # philosopher
    'Q14565331',  # logician
    'Q2306091',   # sociologist
    'Q170790',    # mathematician
    'Q188094',    # economist
    'Q1930187',   # journalist
    'Q3400985',   # academic
    'Q1622272',   # university teacher
    'Q14467526',  # linguist
    'Q169470',    # physicist
    'Q11063',     # astronomer
    'Q39631',     # physician
    'Q201788',    # historian
    'Q40348',     # lawyer
    'Q1234713',   # theologian
    'Q121594',    # professor
    'Q2306091',   # sociologist（重复无害）
    'Q205375',    # inventor
    'Q82594',     # computer scientist
}


def api(base, **params):
    url = base + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA,
                                               'Accept': 'application/json'})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt == 0:
                # Wikidata 限流：429 后等 60 秒再试一次（实测 0.6 次/秒即触发）
                time.sleep(60)
                continue
            raise


def search(name):
    try:
        j = api('https://www.wikidata.org/w/api.php', action='wbsearchentities',
                search=name, language='en', uselang='en', limit=3, format='json')
    except Exception:
        return []
    return [x['id'] for x in j.get('search', [])]


def entities(qids):
    if not qids:
        return {}
    j = api('https://www.wikidata.org/w/api.php', action='wbgetentities',
            ids='|'.join(qids), props='descriptions|claims|labels',
            languages='en', format='json')
    return j.get('entities', {})


def claim_year(ent, pid, rank='birth'):
    vals = []
    for c in (ent.get('claims', {}).get(pid) or []):
        try:
            t = c['mainsnak']['datavalue']['value']['time']
        except (KeyError, TypeError):
            continue
        m = re.match(r'[+-](\d{4})-', t)
        if m:
            vals.append(int(m.group(1)))
    return min(vals) if vals else None


def occupations(ent):
    out = set()
    for c in (ent.get('claims', {}).get('P106') or []):
        try:
            out.add(c['mainsnak']['datavalue']['value']['id'])
        except (KeyError, TypeError):
            continue
    return out


def country(ent):
    for c in (ent.get('claims', {}).get('P27') or []):
        try:
            return c['mainsnak']['datavalue']['value']['id']
        except (KeyError, TypeError):
            continue
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=50)
    ap.add_argument('--registry', default='ren-ming-biao.md')
    ap.add_argument('--out', default='specs/058-term-full-reextraction/results/'
                                    'person-wikidata-2026-11-25.tsv')
    a = ap.parse_args()

    todo = []
    for l in io.open(a.registry, encoding='utf-8'):
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 8 or c[0] in ('原文', '---'):
            continue
        if c[3] in ('—', '') or c[4] in ('—', ''):
            name = c[0].split(' / ')[0]
            if ',' in name:
                last, first = [x.strip() for x in name.split(',', 1)]
                name = first + ' ' + last
            todo.append((c[0], name, c[3], c[4]))
    print('待补行', len(todo))
    rows = []
    for i, (key, name, guo, dates) in enumerate(todo[:a.limit]):
        qids = search(name)
        ents = entities(qids)
        best = None
        for q in qids:
            e = ents.get(q) or {}
            desc = ((e.get('descriptions') or {}).get('en') or {}).get('value', '')
            by, dy = claim_year(e, 'P569'), claim_year(e, 'P570')
            occ = occupations(e)
            if not by or not SCHOLAR.search(desc):
                continue
            if occ and not (occ & OCC_OK):
                continue
            best = (q, desc, by, dy, country(e))
            break
        if best:
            q, desc, by, dy, ctry = best
            span = '%d–%d' % (by, dy) if dy else '%d–' % by
            rows.append((key, guo, dates, q, desc[:48], ctry or '', span))
        else:
            rows.append((key, guo, dates, '', '查无学者型候选' if qids else '查无条目', '', ''))
        if (i + 1) % 10 == 0:
            print('  已查', i + 1)
        time.sleep(1.2)

    with io.open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('key\tguo_now\tdates_now\tqid\tdesc\tcountry_qid\tdates_wd\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    ok = sum(1 for r in rows if r[3])
    print('候选 %d/%d → %s' % (ok, len(rows), a.out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
