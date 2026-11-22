# -*- coding: utf-8 -*-
"""specs/058 第二批：术语在线优先的落册清单生成。

规则（用户裁定 2026-11-22 优先术语在线）：
  ① 审定库命中（英文形一致或单复数变体）且学科对口 → 采审定译名，依据列审定名词库；
  ② 无对口命中 → 学界通行 A 档直裁，依据列注明查无／命中他义。
输出 rowspec-batch2.json + rowspec-batch2.review.tsv（人审比对）。
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
from tools.register_lib import norm_key_quote, parse_registry_full, term_path  # noqa: E402

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
QD = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                  'queries', 'termonline-all')
PHIL = ('哲学', '自然辩证法', '逻辑', '伦理', '美学', '宗教', '心理', '语言',
        '科学哲学', '技术哲学', '认知科学', '马克思主义', '外国哲学', '思维',
        '方法论', '辩证法', '数学')
# 审定译名与人工译名不同时，只有强哲学学科命中才改采（防“moral duties→士气”类别义）
STRONG = ('哲学', '自然辩证法', '逻辑', '伦理', '美学', '宗教', '马克思主义')
# 审定命中义与源词不合（同形别义）时强制保留人工译名
KEEP_MINE = {'physical theories', 'moral concepts'}


def variants(en):
    b = en.casefold().strip()
    out = {b}
    if b.endswith('ies'):
        out.add(b[:-3] + 'y')
    if b.endswith('es'):
        out.add(b[:-2])
    if b.endswith('s'):
        out.add(b[:-1])
    out.add(b + 's')
    return out


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--tsv', default='curated2-translations.tsv')
    ap.add_argument('--out', default='rowspec-batch2.json')
    ap.add_argument('--batch', default='058-batch2')
    args = ap.parse_args()
    alias = set()
    for r in parse_registry_full(term_path())[0]:
        for part in r[0].split('/'):
            alias.add(norm_key_quote(part.strip()))
    rows, review = [], ['en\tmine\thit\tcn\tsource\tsubject\tmode']
    for line in open(os.path.join(RES, args.tsv), encoding='utf-8'):
        if not line.strip():
            continue
        en, zh = line.rstrip('\n').split('\t')
        if any(norm_key_quote(v) in alias for v in variants(en)):
            review.append('%s\t%s\t-\t-\t-\t-\tskip_alias' % (en, zh))
            continue
        path = os.path.join(QD, safe_key(norm_key_quote(en)) + '.json')
        doc = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
        hits = doc.get('hits') or []
        vs = variants(en)
        exact_phil = [h for h in hits
                      if (h.get('en') or '').strip().casefold() == en.casefold()
                      and any(p in ((h.get('subjectFullName') or '')
                                    + (h.get('subjectName') or '')
                                    + (h.get('source') or '')) for p in PHIL)]
        var_phil = [h for h in hits
                    if (h.get('en') or '').strip().casefold() in vs
                    and any(p in ((h.get('subjectFullName') or '')
                                  + (h.get('subjectName') or '')
                                  + (h.get('source') or '')) for p in PHIL)]
        cand = exact_phil or var_phil
        aligned = [h for h in cand if h.get('cn') == zh]
        strong = [h for h in cand if any(
            s in ((h.get('subjectFullName') or '') + (h.get('subjectName') or '')
                  + (h.get('source') or '')) for s in STRONG)]
        if aligned:
            h = aligned[0]
            mode, cn = 'same', zh
            basis = '审定名词库（%s%s%s%s；凭证 2026-11-22）' % (
                h.get('source') or '',
                '·' + (h.get('subjectFullName') or '') if h.get('subjectFullName') else '',
                '，' + (h.get('publishYear') or '') if h.get('publishYear') else '',
                '，' + (h.get('wordNumber') or '') if h.get('wordNumber') else '')
        elif strong and strong[0].get('cn') and en not in KEEP_MINE:
            h = strong[0]
            mode, cn = 'diff', h['cn']
            basis = '审定名词库（%s%s%s；命中形 %s；凭证 2026-11-22）' % (
                h.get('source') or '',
                '·' + (h.get('subjectFullName') or '') if h.get('subjectFullName') else '',
                '，' + (h.get('publishYear') or '') if h.get('publishYear') else '',
                h.get('en') or '')
        elif not hits:
            mode, cn = 'mine_empty', zh
            basis = ('学界通行（教科书级标准术语，specs/058 A 档直裁；'
                     '审定库查无对应条目；凭证 2026-11-22）')
        else:
            mode, cn = 'mine_other', zh
            basis = ('学界通行（教科书级标准术语，specs/058 A 档直裁；'
                     '审定库命中他义或形不完全一致，未采；凭证 2026-11-22）')
        rows.append({'en': en, 'zh': cn, 'table': 'term',
                     'first_seen': '语料回收（specs/058 全库提取）',
                     'basis': basis, 'date': '2026-11-22'})
        review.append('%s\t%s\t%s\t%s\t%s\t%s\t%s' % (
            en, zh, mode, cn,
            (exact_phil or var_phil or [{}])[0].get('source') or '',
            ((exact_phil or var_phil or [{}])[0].get('subjectName') or ''),
            'DIFF' if cn != zh else 'same'))
    out = {'batch': args.batch, 'date': '2026-11-22',
           'scope': '全库提取批次（术语在线优先：审定命中即采，无命中 A 档直裁）',
           'evidence': 'specs/008-terminology-campaign/results/queries/termonline-all/',
           'rows': rows}
    json.dump(out, open(os.path.join(RES, args.out), 'w',
                        encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    open(os.path.join(RES, args.out + '.review.tsv'), 'w', encoding='utf-8',
         newline='\n').write('\n'.join(review) + '\n')
    import collections
    print('rows=%d modes=%s diff=%d'
          % (len(rows), collections.Counter(
              r['basis'][:4] for r in rows).most_common(),
             sum(1 for l in review[1:] if l.endswith('DIFF'))))


if __name__ == '__main__':
    main()
