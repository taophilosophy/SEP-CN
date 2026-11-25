# -*- coding: utf-8 -*-
"""批 28 一次性补丁：术语表自动依据行改定（2026-11-25）。幂等：每行断言恰好命中一次。"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

P = 'shu-yu-biao.md'
OLD_B = '学界通行译名（审定库无对口命中，2026-11-23）；凭证 2026-11-23'

# (键, 新译法 or None, 依据追加, 新日期)
PATCH = [
    ('justice as fairness', None,
     '；译形补证 2026-11-25：罗尔斯《作为公平的正义——正义新论》（姚大志译，上海三联书店 2002）书名、'
     '万俊人译《政治自由主义》（译林出版社 2000，增订版 2011）正文均作“作为公平的正义”', '2026-11-25'),
    ('political liberalism', None,
     '；译形补证 2026-11-25：万俊人译《政治自由主义》（译林出版社 2000；增订版 2011，ISBN 9787544720465）书名',
     '2026-11-25'),
    ('legal positivism', '法律实证主义（亦作“法实证主义”）',
     '；译形补证 2026-11-25：哈特《法律的概念》第三版（许家馨、李冠宜译，法律出版社 2018）第九章作“法实证主义”，'
     '大陆法理学文献“法律实证主义”并行为主形，故两形俱收', '2026-11-25'),
    ('narrow content', '窄内容（亦作“狭义内容”）',
     '；译形补证 2026-11-25：黄原〈知觉表征论的难题〉（中国社会科学院哲学研究所，2019）作“窄内容”；'
     '蒉益民〈当前心灵哲学中的核心课题〉作“狭义内容”，与 wide content“广义内容”成对', '2026-11-25'),
    ('large cardinal axioms', None,
     '；译形补证 2026-11-25：杨睿之“集合论进阶（大基数理论）”课程（复旦大学哲学学院，2020 春季）',
     '2026-11-25'),
    ("Skolem's Paradox", None,
     '；译形补证 2026-11-25：Skolem 通行译“斯科伦”，见《数理逻辑与集合论》教学大纲（北京航空航天大学，'
     '“斯科伦函数”）与 Manin《数学家用的数理逻辑教程》第 7 节 Skolem’s Paradox', '2026-11-25'),
]


def main():
    lines = io.open(P, encoding='utf-8', newline='').read().split('\n')
    hit = {k: 0 for k, _, _, _ in PATCH}
    for i, l in enumerate(lines):
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 6:
            continue
        for key, zh, add, date in PATCH:
            if c[0] != key:
                continue
            if OLD_B not in c[4]:
                print('  跳过（依据已改）:', key)
                hit[key] += 1
                continue
            c[4] = c[4].replace(OLD_B, OLD_B + add)
            if zh:
                c[2] = zh
            c[5] = date
            lines[i] = '| ' + ' | '.join(c) + ' |'
            hit[key] += 1
    bad = [k for k, n in hit.items() if n != 1]
    if bad:
        print('断言失败:', bad)
        return 1
    with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print('已写盘', len(PATCH), '行')
    return 0


if __name__ == '__main__':
    sys.exit(main())
