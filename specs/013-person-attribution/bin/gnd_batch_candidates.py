# -*- coding: utf-8 -*-
"""GND（lobid）批量候选池：人名缺籍属/生卒两档收口的第一步（2026-11-26）。

策略（specs/013 两档收口方案，2026-11-26 用户批准）：
  本脚本只**采集**候选，不写登记册——对 `person-missing.txt` 全量过 lobid 精确名检索，每名最多取
  3 条命中，落 `results/gnd-candidates-2026-11-26.tsv`（四列：键｜原文｜译法｜候选；
  候选列形如 q=…; gnd=…; name=…; birth=…; death=…; coa=…; occ=…，制表符已清洗）；
  判定（防误采防线）由 `bin/gnd_triage.py` 完成。

请求间隔 ≥5s（rules/05 礼貌抓取，按“相邻请求”计）；断点 state 落
script/tmp/gnd-batch-state.json，中断重跑自动续。行数以 `person-missing.txt` 现查为准
（2026-11-26 收口后为 19 行），限速 5s。

用法：
  python -I specs/013-person-attribution/bin/gnd_batch_candidates.py [--limit N]
"""
import argparse
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

PM = 'specs/013-person-attribution/results/person-missing.txt'
REN = 'ren-ming-biao.md'
OUT = 'specs/013-person-attribution/results/gnd-candidates-2026-11-26.tsv'
STATE = 'script/tmp/gnd-batch-state.json'
CTX = ssl.create_default_context()  # 默认证书/主机名校验（2026-11-28 安全审计）
OPENER = urllib.request.build_opener(urllib.request.HTTPSHandler(context=CTX))
UA = 'SEP-CN-evidence/1.0 (academic metadata verification; repo maintainer)'
FIELDS = ('gndIdentifier', 'preferredName', 'dateOfBirth', 'dateOfDeath',
          'placeOfBirth', 'placeOfDeath', 'countryOfActivity',
          'professionOrOccupation', 'type')
GAP = 5.0  # 相邻请求最小间隔（秒）
_last_req = [0.0]


def load_registry():
    """键 → (原文列, 译法列)。"""
    reg = {}
    for line in io.open(REN, encoding='utf-8'):
        if not line.startswith('|'):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 9 or c[0] in ('键', ''):
            continue
        if set(c[0]) <= set('-: '):
            continue
        key = c[0].strip('* ').strip()
        reg.setdefault(key.casefold(), (c[1], c[2]))
    return reg


def paced():
    wait = GAP - (time.time() - _last_req[0])
    if wait > 0:
        time.sleep(wait)


def query(name):
    q = urllib.parse.quote('"%s"' % name)
    url = 'https://lobid.org/gnd/search?q=%s&format=json&size=3' % q
    paced()
    _last_req[0] = time.time()
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return json.loads(OPENER.open(req, timeout=40).read().decode('utf-8'))


def lbl(v):
    if v is None:
        return ''
    if isinstance(v, dict):
        return str(v.get('label', ''))
    if isinstance(v, list):
        return '；'.join(lbl(x) for x in v)
    return str(v)


def clean(s):
    return re.sub(r'[\t\r\n]', ' ', str(s or '')).strip()


def cand_str(q, members):
    if not members:
        return 'q=%s; verdict=MISS' % q
    parts = []
    for m in members:
        kv = '; '.join('%s=%s' % (f, clean(lbl(m.get(f)))) for f in FIELDS)
        parts.append('q=%s; verdict=HIT; %s' % (q, kv))
    return ' || '.join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0, help='本次最多查询名数（0=不限）')
    a = ap.parse_args()

    reg = load_registry()
    names = []
    for line in io.open(PM, encoding='utf-8'):
        c = line.rstrip('\n').split('\t')
        if len(c) >= 2 and c[0] != '汇总':
            names.append(c[0])
    print('缺项名单 %d 行' % len(names))

    state = {'done': []}
    if os.path.exists(STATE):
        state = json.load(io.open(STATE, encoding='utf-8'))
    done = set(state.get('done', []))
    header_needed = not os.path.exists(OUT)
    out = io.open(OUT, 'a', encoding='utf-8', newline='\n')
    if header_needed:
        out.write('键\t原文\t译法\t候选\n')

    queried = 0
    for name in names:
        if name in done:
            continue
        if a.limit and queried >= a.limit:
            break
        orig, zh = reg.get(name.casefold(), ('', ''))
        tries = [name]
        orig_first = re.split(r'\s*/\s*', orig.strip('* ').strip())[0].strip()
        if orig_first and orig_first.casefold() != name.casefold():
            tries.append(orig_first)
        got = []
        for q in tries:
            try:
                j = query(q)
                got.append(cand_str(q, j.get('member') or []))
            except Exception as e:
                got.append('q=%s; verdict=ERR; err=%s' % (q, clean(e)))
                break
        out.write('%s\t%s\t%s\t%s\n' % (clean(name), clean(orig), clean(zh),
                                        ' || '.join(got)))
        out.flush()
        done.add(name)
        state['done'] = sorted(done)
        queried += 1
        if queried % 10 == 0:
            json.dump(state, io.open(STATE, 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump(state, io.open(STATE, 'w', encoding='utf-8'), ensure_ascii=False)
    out.close()
    print('本轮查询 %d 名，累计完成 %d/%d → %s' % (queried, len(done), len(names), OUT))


if __name__ == '__main__':
    main()
