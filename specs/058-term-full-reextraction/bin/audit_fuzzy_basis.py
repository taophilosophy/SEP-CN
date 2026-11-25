# -*- coding: utf-8 -*-
"""审定依据的配对性审计（2026-11-25，纯本地，不出网）。

背景：termonline-all 通道回的是**模糊匹配**结果（键 "archimedean property" 报
“审定公布名词库=534”即为模糊总数），缓存 hits 只是首屏 20 条邻居。故“缓存里有同形
中文”不足以证明该中文与本案英文键在审定库里成对——批 41 界面复核已实证数行据此误记。

判定只看“审定公布名词库”条目（来源名不含“海峡两岸”“国家标准／标准文件”“百科”）。
四档：
  pair     审定条目：英文（去单复数／属格／多义分号后）＝键，中文＝译法主形或亦作或所引之形
  en-only  有英文配对的审定条目，但中文与本案译法不合 → 依据所引之形须复核
  cn-only  只有中文同形条目，英文并不配对 → “审定作 X”失据，须降档或改记复合词
  tw-only  审定库无配对，仅海峡两岸名词对照库有 → 库名须改（批 41 已改 empiricist、samadhi）
  none     本地缓存查无任何同形（不等于审定库没有，只表示本地不可证）

输出：results/term-basis-pairing-2026-11-25.tsv
"""
import glob
import io
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

QD = 'specs/008-terminology-campaign/results/queries/termonline-all'
TERMS = 'shu-yu-biao.md'
OUT = 'specs/058-term-full-reextraction/results/term-basis-pairing-2026-11-25.tsv'


def strong(s):
    s = re.sub(r"['’][sS]?\b", '', str(s or ''))          # 属格 's 剥去
    s = unicodedata.normalize('NFKD', s.casefold())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s)


def cn_keys(s):
    """中文形归一：GB 方括号是可选字（优先[方]法＝优先法／优先方法），故两种都收。"""
    base = re.sub(r'（[^）]*）|\([^)]*\)', '', str(s or ''))
    out = {strong(re.sub(r'\[[^\]]*\]', '', base)), strong(re.sub(r'\[([^\]]*)\]', r'\1', base))}
    return {x for x in out if x}


def en_stems(s):
    """英文各义项（分号／逗号分隔）的折叠形与去复数形，-ise/-ize、-our/-or 互认。"""
    out = set()
    for part in re.split(r'[;,]', str(s or '')):
        t = strong(part)
        if len(t) < 3:
            continue
        forms = {t}
        for a, b in (('ise', 'ize'), ('isation', 'ization'), ('our', 'or')):
            if a in t:
                forms.add(t.replace(a, b))
            if b in t:
                forms.add(t.replace(b, a))
        for suf, rep in (('ies', 'y'), ('ses', 's'), ('es', ''), ('s', '')):
            if t.endswith(suf) and len(t) > len(suf) + 2:
                forms.add(t[:-len(suf)] + rep)
        out |= {x for x in forms if len(x) >= 3}
    return out


def zh_forms(zh, *extra):
    """译法主形 + 文中所有引号内中文形（亦作、审定作 X、对照说明都算）。

    登记册里“审定”表述花样多（审定作 X／审定名词库 X＝Y／审定收 Y），一律按
    “行内引用过的中文形”处理：只要其中任一式能与审定条目配对，该行的凭证就自洽。
    """
    forms = cn_keys(zh.split('（')[0].strip('《》'))
    for text in (zh,) + extra:
        for x in re.findall(r'[“"]([^”"]{1,14})[”"]', text or ''):
            if re.search(r'[一-鿿]', x):
                forms |= cn_keys(x)
    for x in re.findall(r'审定[^；。，]{0,16}?[＝作]([一-鿿]{2,10})', zh + ' '.join(extra or '')):
        forms.add(strong(x))
    return {y for y in forms if y}


def lib_of(std):
    s = str(std or '')
    if not s:
        return None
    if '海峡两岸' in s:
        return 'tw'
    if '国家标准' in s or '标准文件' in s:
        return 'std'
    if '百科' in s or '维基' in s:
        return 'other'
    return 'audit'


def filename(key):
    return re.sub(r'[^0-9a-zA-Z]+', '_', key.strip().lower()).strip('_')


def main():
    by_key = defaultdict(list)
    en_index = defaultdict(list)
    cn_index = defaultdict(list)
    files = glob.glob(os.path.join(QD, '*.json'))
    for p in files:
        key = os.path.basename(p)[:-5]
        try:
            j = json.load(io.open(p, encoding='utf-8'))
        except Exception:
            continue
        for h in j.get('hits') or []:
            std = h.get('standard') or h.get('source')
            lib = lib_of(std)
            if not lib:
                continue
            rec = (h.get('cn'), h.get('en'), std, h.get('code') or h.get('wordNumber'), lib)
            by_key[key].append(rec)
            for e in en_stems(h.get('en')):
                en_index[e].append(rec)
            for ck in cn_keys(h.get('cn')):
                cn_index[ck].append(rec)
    print('缓存 %d 份；英文形索引 %d、中文形索引 %d' % (len(files), len(en_index), len(cn_index)))

    rows = []
    for line in io.open(TERMS, encoding='utf-8'):
        if not line.startswith('|'):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 6 or c[0] in ('键', '') or set(c[0]) <= set('-: '):
            continue
        if '审定' not in c[4]:
            continue
        rows.append(c)
    print('引用审定的行 %d' % len(rows))

    cnt = defaultdict(int)
    out = []
    for c in rows:
        key, zh, basis = c[0], c[2], c[4]
        forms = zh_forms(zh, basis)
        seg = re.split(r'\s*/\s*', key)
        stems = set()
        for s in [key] + seg:
            stems |= en_stems(s)
        pool = []
        for s in [key] + seg:
            pool.extend(by_key.get(filename(s), []))
        for e in stems:
            pool.extend(en_index.get(e, []))
        for f in forms:
            pool.extend(cn_index.get(f, []))
        pool = {id(r): r for r in pool}.values()
        audit_pool = [r for r in pool if r[4] == 'audit']
        en_hits = [r for r in audit_pool if en_stems(r[1]) & stems]
        cn_hits = [r for r in audit_pool if cn_keys(r[0]) & forms]
        pairs = [r for r in en_hits if cn_keys(r[0]) & forms]
        tw = [r for r in pool if r[4] == 'tw' and (en_stems(r[1]) & stems or cn_keys(r[0]) & forms)]
        if pairs:
            v, ev = 'pair', pairs[0]
        elif en_hits:
            v, ev = 'en-only', en_hits[0]
        elif cn_hits:
            v, ev = 'cn-only', cn_hits[0]
        elif tw:
            v, ev = 'tw-only', tw[0]
        else:
            v, ev = 'none', ('', '', '', '', '')
        cnt[v] += 1
        out.append((key, zh[:40], v, '%s｜%s｜%s｜%s' % (ev[0], ev[1], ev[2], ev[3])))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('key\tzh\tverdict\thit\n')
        for r in out:
            f.write('\t'.join(r) + '\n')
    print('档位分布：', dict(cnt))
    print('→', OUT)


if __name__ == '__main__':
    main()
