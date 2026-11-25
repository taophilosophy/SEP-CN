# -*- coding: utf-8 -*-
"""批 34 抽验：从“确无对口”的 733 行里随机抽 30 行，用现网通道重查，核缓存空结论。

缓存建于 11-18/11-24，期间通道有间歇性全零回包；若抽样里有行其实有对口命中，
说明旧缓存存在假空，需整批重查。
"""
import io
import json
import os
import random
import sys
import time

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools import cnki_query as cq  # noqa: E402
from tools.cnki_query import safe_key  # noqa: E402
from tools.register_lib import norm_key_quote  # noqa: E402

AUDIT = 'specs/058-term-full-reextraction/results/auto-basis-reaudit-2026-11-25.tsv'
QD = 'specs/008-terminology-campaign/results/queries/termonline-all'
PHIL = ('哲学', '自然辩证法', '逻辑', '伦理', '美学', '宗教', '心理', '语言',
        '认知', '思维', '方法论', '辩证法', '政治', '法律', '社会', '历史',
        '数学', '物理学', '生物学', '医学', '计算机')


def main():
    # 审计表只写 same/diff/nocache 行；“确无对口”的行不外显，故从登记册反推：
    # 带自动依据标记的行，减去审计表已有的键，余下的就是 733 条候选。
    listed = set()
    for line in io.open(AUDIT, encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) == 9:
            listed.add(p[0])
    rows = []
    for line in io.open('shu-yu-biao.md', encoding='utf-8'):
        if not line.startswith('| '):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) != 6 or '审定库无对口命中' not in c[4] or c[0] in listed:
            continue
        rows.append((c[0], c[2]))
    print('候选', len(rows))
    random.seed(20261125)
    sample = random.sample(rows, 30)
    print('样本', len(sample))
    sus = []
    for i, (key, zh) in enumerate(sample):
        try:
            data = cq._tl_all_fetch(key, 30)
            hits, note = cq._tl_all_parse(data)
            total = cq._tl_all_total(data)
        except Exception as exc:
            print('  异常', key, type(exc).__name__)
            continue
        hit_en = {(h.get('en') or '').strip().lower() for h in hits}
        match = [h for h in hits if (h.get('en') or '').strip().lower() == key.strip().lower()]
        flag = 'HIT' if match else ('fuzzy' if hits else 'zero')
        print('%2d %-42s total=%4d %s' % (i + 1, key[:42], total, flag))
        if match:
            sus.append((key, zh, match[:2]))
        time.sleep(0.8)
    print('抽样内有对口命中', len(sus))
    for k, z, m in sus:
        print('  ', k, '｜现译', z, '｜审定', [(h.get('cn'), h.get('standard'), h.get('subject')) for h in m])
    return 0


if __name__ == '__main__':
    sys.exit(main())
