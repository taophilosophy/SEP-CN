# -*- coding: utf-8 -*-
"""批 29 一次性补丁：按 auto-basis-reaudit-2026-11-25.tsv 的复审结果改写依据（幂等）。

八行审定同形 → 依据改“审定名词库（…）”；三行审定收异义 → 依据加异义注（防重复误判）；
两行台湾异形 → 译法加“亦作”，依据记审定形与出处。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

P = 'shu-yu-biao.md'
OLD = '学界通行译名（审定库无对口命中，2026-11-23）；凭证 2026-11-23'

# key -> (新译法 or None, 新依据全文, 新日期)
PATCH = {
    'active perception': (None,
        '审定名词库（海峡两岸心理学名词·心理学，2016；2026-11-25 缓存重放补正，原记“审定库无对口命中”系初查漏检）',
        '2026-11-25'),
    'common fate': (None,
        '审定名词库（海峡两岸心理学名词·心理学，2016，另收“common fate”＝共同命运、“law of common fate”＝共同命运律；'
        '2026-11-25 缓存重放补正）', '2026-11-25'),
    'conceptual realism': (None,
        '审定名词库（社会学名词·科学知识，2025；2026-11-25 缓存重放补正，原记“无对口命中”系初查漏检）',
        '2026-11-25'),
    'imagined community': (None,
        '审定名词库（社会学名词·历史社会学的核心概念范畴，2025；2026-11-25 缓存重放补正）',
        '2026-11-25'),
    'latent variable': (None,
        '审定名词库（社会学名词·数据分析，2025 作“潜变量”；海峡两岸心理学名词 2016 作“潜［在］变量”；'
        '2026-11-25 缓存重放补正）', '2026-11-25'),
    "Mach's Principle": (None,
        '审定名词库（物理学名词·相对论，2019；2026-11-25 缓存重放补正，原记“无对口命中”系初查漏检）',
        '2026-11-25'),
    'Reality Principle': (None,
        '审定名词库（海峡两岸心理学名词·心理学，2016；2026-11-25 缓存重放补正）', '2026-11-25'),
    'thick description': (None,
        '审定名词库（社会学名词·人类学方法，2025；2026-11-25 缓存重放补正）', '2026-11-25'),
    'active powers': (None,
        OLD + '；2026-11-25 缓存重放复审：审定仅收“active power＝有功功率”（物理学名词·电磁学 2019），'
        '系异义，非对口，依据维持', '2026-11-25'),
    'cultural consciousness': (None,
        OLD + '；2026-11-25 缓存重放复审：审定收“cultural consciousness＝文化自觉”（社会学名词 2025），'
        '“文化自觉”为费孝通义，与本文“文化意识”非同一概念，不采', '2026-11-25'),
    'hard determinism': (None,
        OLD + '；2026-11-25 缓存重放复审：审定仅收“hard determinism＝硬技术决定论”（新闻学与传播学名词 2022），'
        '属技术决定论义，非形而上学决定论，不采', '2026-11-25'),
    'domain specificity': ('领域特殊性（亦作“领域特定性”）',
        OLD + '；2026-11-25 缓存重放：审定“domain specificity＝领域特定性”（海峡两岸心理学名词·心理学 2016），'
        '台湾形，大陆认知科学文献通行“领域特殊性”，主形维持', '2026-11-25'),
    'likelihood principle': ('似然原则（亦作“似然原理”）',
        OLD + '；2026-11-25 缓存重放：审定“likelihood principle＝似然原理”（海峡两岸心理学名词·心理学 2016），'
        '台湾形，两形并存故俱收', '2026-11-25'),
}


def main():
    lines = io.open(P, encoding='utf-8', newline='').read().split('\n')
    hit = {k: 0 for k in PATCH}
    for i, l in enumerate(lines):
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 6:
            continue
        if c[0] not in PATCH:
            continue
        zh, basis, date = PATCH[c[0]]
        if zh:
            c[2] = zh
        c[4] = basis
        c[5] = date
        lines[i] = '| ' + ' | '.join(c) + ' |'
        hit[c[0]] += 1
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
