# -*- coding: utf-8 -*-
"""自动依据行全量复审（2026-11-25）：查“审定库无对口命中”是否名副其实。

依据列写「审定库无对口命中」的行共 780 条，其中 746 条在 termonline-all 查询缓存里
有原始返回。本脚本离线重放缓存，按「en 对口＋学科涉哲」重新判命中，并把命中形与
我方译法主形比对，分三档：
  same  审定形与我方主形一致 → 依据可从“无对口命中”改为审定命中（含学科与号）
  diff  审定有对口但汉字不同 → 主形之争，须人工回源判定
  none  缓存里确无对口命中 → 依据照写，属真欠账（工具书通道另议）

只读缓存与登记册，不写登记册，不联网。

用法：
  python -I specs/058-term-full-reextraction/bin/audit_auto_basis.py
产物：
  specs/058-term-full-reextraction/results/auto-basis-reaudit-2026-11-25.tsv
"""
import io
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools.cnki_query import safe_key  # noqa: E402
from tools.register_lib import norm_key_quote  # noqa: E402

QD = 'specs/008-terminology-campaign/results/queries/termonline-all'
OUT = 'specs/058-term-full-reextraction/results/auto-basis-reaudit-2026-11-25.tsv'
PHIL = ('哲学', '自然辩证法', '逻辑', '伦理', '美学', '宗教', '心理', '语言',
        '认知', '思维', '方法论', '辩证法', '政治', '法律', '社会', '历史',
        '数学', '物理学', '生物学', '医学', '计算机')


def strong(s):
    # 保留 CJK：纯中文行若被剥成空串，同形比对会全部空对空误判 same
    s = unicodedata.normalize('NFKD', s.casefold().replace('’', "'"))
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s)


def variants(en):
    out = set()
    for part in re.split(r'\s*/\s*', en):
        part = re.sub(r'（.*?）|\(.*?\)', '', part).strip()
        if not part:
            continue
        b = strong(part)
        if not b:
            continue
        out |= {b, b + 's', b[:-1] if b.endswith('s') else b}
        out |= {strong('the ' + part), strong('law of ' + part),
                strong('principle of ' + part)}
    return out


def zh_main(zh):
    return strong(zh.split('（')[0].strip('《》'))


def main():
    rows = []
    for l in io.open('shu-yu-biao.md', encoding='utf-8'):
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 6 or '审定库无对口命中' not in c[4]:
            continue
        rows.append(c)
    print('自动依据行', len(rows))

    stat = {'same': 0, 'diff': 0, 'none': 0, 'nocache': 0}
    out = ['key\tours\ten_hit\tcn\thit_en\tsource\tsubject\tyear\tgrade']
    for c in rows:
        key, zh = c[0], c[2]
        path = os.path.join(QD, safe_key(norm_key_quote(key)) + '.json')
        if not os.path.exists(path):
            stat['nocache'] += 1
            out.append('%s\t%s\t\t\t\t\t\t\tnocache' % (key, zh))
            continue
        doc = json.load(io.open(path, encoding='utf-8'))
        vs = variants(key)
        cand = []
        for h in doc.get('hits') or []:
            hen = strong(h.get('en') or '')
            subj = (h.get('subjectFullName') or '') + (h.get('subjectName') or '')
            if hen in vs and any(p in subj + (h.get('source') or '') for p in PHIL):
                cand.append(h)
        if not cand:
            stat['none'] += 1
            continue
        mine = zh_main(zh)
        same = [h for h in cand if strong(h.get('cn') or '') == mine]
        grade = 'same' if same else 'diff'
        stat[grade] += 1
        for h in (same or cand)[:2]:
            out.append('\t'.join([
                key, zh, h.get('en') or '', h.get('cn') or '', h.get('en') or '',
                h.get('source') or '', (h.get('subjectName') or '')[:20],
                h.get('publishYear') or '', grade]))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print('审定同形可升档', stat['same'], '｜异形待判', stat['diff'],
          '｜确无对口', stat['none'], '｜无缓存', stat['nocache'])
    print('输出', OUT)


if __name__ == '__main__':
    main()
