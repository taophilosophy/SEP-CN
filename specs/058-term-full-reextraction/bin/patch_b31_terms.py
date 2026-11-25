# -*- coding: utf-8 -*-
"""批 31 一次性补丁：撞形组余下 21 组逐行加括注消歧（2026-11-25）。

只加“（…）”括注，不动主形（“（”之前一字不改），故不是译法改定，是撞形登记。
逐行断言恰好命中一次，幂等。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

P = 'shu-yu-biao.md'
NEW = {
    'De prima philosophia / On First Philosophy': '《论第一哲学》（“第一哲学”通名，非专书）',
    'On First Philosophy (al-Kindi)': '《论第一哲学》（肯迪著作）',
    'reliable cognition': '可靠认知（一般认识论）',
    'causal relation': '因果关系（关系义）',
    'Causation': '因果关系（主题义；亦作“因果”）',
    'hairesis': '宗派（古代学派组织）',
    'shi (actuality)': '实（名实论）',
    'demon (daemon)': '恶魔（daemon 义）',
    'affectus sive affectiones': '情感（维韦斯 affectiones）',
    'number theory': '数论（数学）',
    'expectation value': '期望值（物理）',
    'expected value': '期望值（决策论；亦作“期望价值”）',
    'rightness': '正当性（行为正当）',
    'Truth': '真理（truth 通义）',
    'divine nature': '神性（基督教通用语）',
    'correspondence theory': '符合论（真理理论）',
    'statistical relevance': '统计相关性（Salmon 相关性模型）',
    'highest good': '至善（英语通名）',
    'tea ceremony': '茶道（日本文化通名；亦作“茶道仪式”）',
    'naya': '视角（耆那 naya）',
    'perspective (RQM)': '视角（罗韦利关系量子力学）',
    'dialectical question': '论辩问题（问答式论辩）',
    'claim (promissory)': '请求权（允诺 claim；亦作“要求权”）',
    'point-mass': '质点（物理）',
    'moral values': '道德价值（价值观义）',
}


def main():
    lines = io.open(P, encoding='utf-8', newline='').read().split('\n')
    hit = {k: 0 for k in NEW}
    for i, l in enumerate(lines):
        if not l.startswith('| ') or l.startswith('| ---'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 6 or c[0] not in NEW:
            continue
        c[2] = NEW[c[0]]
        c[5] = '2026-11-25'
        lines[i] = '| ' + ' | '.join(c) + ' |'
        hit[c[0]] += 1
    bad = [k for k, n in hit.items() if n != 1]
    if bad:
        print('断言失败:', bad)
        return 1
    with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print('已改', len(NEW), '行')
    return 0


if __name__ == '__main__':
    sys.exit(main())
