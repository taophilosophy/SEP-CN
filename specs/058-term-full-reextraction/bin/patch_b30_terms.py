# -*- coding: utf-8 -*-
"""批 30 一次性补丁：中文主形撞车组的并键与括注消歧（2026-11-25）。

九组同概念异形并键（keeper 取排序靠前行，键写 A / B，依据记旧键旧首现）；
十四行同形不同义加括注消歧。逐行断言恰好命中一次，幂等。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

P = 'shu-yu-biao.md'
DATE_NOTE = '；2026-11-25 异形并键（旧键 %s；旧首现 %s）'

MERGES = [  # (keeper 键, absorbed 键, 合并后键)
    ('cognitive ability', 'cognitive capacities',
     'cognitive ability / cognitive capacities'),
    ("maker's knowledge (tradition)", 'maker\u2019s knowledge',
     "maker's knowledge (tradition) / maker's knowledge"),
    ('mental states', 'psychological states',
     'mental states / psychological states'),
    ('Ny\u0101ya-s\u016btra', 'Ny\u0101yas\u016btra (Gautama)',
     'Ny\u0101ya-s\u016btra / Ny\u0101yas\u016btra (Gautama)'),
    ('Occam\u2019s razor', 'Ockham\u2019s razor',
     'Occam\u2019s razor / Ockham\u2019s razor'),
    ('Peripatetic', 'Peripatetics', 'Peripatetic / Peripatetics'),
    ('significatio', 'signification', 'significatio / signification'),
    ('sublunar world', 'sublunary world', 'sublunar world / sublunary world'),
    ('Lutheran', 'Lutheranism', 'Lutheran / Lutheranism'),
]

NOTES = [  # (键, 新译法全文)
    ('sentimentalism', '情感主义（道德情感主义传统；与 emotivism 元伦理学情感主义分列）'),
    ('interpretability', '可解释性（模型内部）'),
    ('renunciation', '出离（印度宗教）'),
    ('ka\u1e63\u0101ya', '烦恼（耆那）'),
    ('kle\u015ba', '烦恼（佛教）'),
    ('omniscience', '全知（神学）'),
    ('Principles of Mathematics', '《数学原理》（罗素 1903 单卷；与 Principia Mathematica《数学原理》（怀特海、罗素合著）分立）'),
    ('philosophy of right', '法哲学（黑格尔 Rechtsphilosophie）'),
    ('choice theory', '选择理论（决策论）'),
    ('selection theory', '选择理论（进化论）'),
    ('sy\u0101dv\u0101da', '或然论（耆那）'),
    ('mithy\u0101tva', '邪见（虚妄性）'),
    ('Book of Optics', '《光学》（伊本·海赛姆）'),
    ('La Dioptrique', '《光学》（笛卡尔）'),
]


def main():
    lines = io.open(P, encoding='utf-8', newline='').read().split('\n')
    rows = {}
    for i, l in enumerate(lines):
        if not l.startswith('| ') or l.startswith('| ---'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and c[0] != '键':
            rows.setdefault(c[0], (i, c))
    miss = [k for k, _a, _b in MERGES if k not in rows] + \
           [b for _a, b, _c in MERGES if b not in rows] + \
           [k for k, _ in NOTES if k not in rows]
    if miss:
        print('键未命中:', miss)
        return 1

    for keeper, absorbed, newkey in MERGES:
        ki, kc = rows[keeper]
        ai, ac = rows[absorbed]
        kc[0] = newkey
        kc[4] = kc[4].rstrip() + DATE_NOTE % (absorbed, ac[3])
        lines[ki] = '| ' + ' | '.join(kc) + ' |'
        lines[ai] = None
    for key, zh in NOTES:
        i, c = rows[key]
        c[2] = zh
        c[5] = '2026-11-25'
        lines[i] = '| ' + ' | '.join(c) + ' |'
    out = [l for l in lines if l is not None]
    if len(out) != len(lines) - len(MERGES):
        print('行数守恒失败')
        return 1
    with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out))
    print('并键 %d 组，括注 %d 行，删行 %d' % (len(MERGES), len(NOTES), len(MERGES)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
