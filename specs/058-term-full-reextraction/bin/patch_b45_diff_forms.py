# -*- coding: utf-8 -*-
"""批 45：审定形与本行译形不同的七行，依据列如实写明审定形（2026-11-25）。

这七行的依据原写成“审定名词库（…）”像是本行译形即审定形，实际审定库收的是另一个形
（locality 局域性、superposition 重叠、originality 独特性、POVM 半正定算子测量、
self-adjoint operator 自伴算子、sex discrimination 对应 gender discrimination、
fundamental attribution error 基本归因错误）。只补写明审定形，译法不动。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-25'

PATCH = {
    'locality': (
        '审定名词库（物理学名词 locality）；凭证 2026-11-09',
        '审定名词库作“局域性”（自然辩证法名词·物理学哲学／物理学名词；2026-11-25 界面精确匹配复核）；'
        '本行“定域性”为量子力学文献通行形；凭证 2026-11-09',
    ),
    'superposition': (
        '审定名词库（物理学名词 superposition）；凭证 2026-11-09',
        '审定名词库作“重叠”（物理学名词，superposition；2026-11-25 界面精确匹配复核）；'
        '本行“叠加”为量子力学文献通行形；凭证 2026-11-09',
    ),
    'originality': (
        '审定名词库（termonline-all·心理学，2026-11-18 JWT 直连凭证）',
        '审定名词库作“独特性”（心理学名词；2026-11-25 界面精确匹配复核）；本行“独创性”为美学文献通行形',
    ),
    'POVM': (
        '审定名词库（物理学名词 positive operator-valued measure）；凭证 2026-11-12',
        '审定名词库作“半正定算子测量”（物理学名词·量子信息，positive-operator valued measure；'
        '2026-11-25 界面精确匹配复核）；本行“正算子值测度”为文献通行直译；凭证 2026-11-12',
    ),
    'self-adjoint operator': (
        '审定名词库（物理学名词有“自伴”）；学界通行；凭证 2026-11-11',
        '审定名词库作“自伴算子”（数学名词·泛函分析；2026-11-25 界面精确匹配复核）；'
        '本行“自伴算符”为物理学文献通行形；凭证 2026-11-11',
    ),
    'sex discrimination': (
        '审定名词库（termonline-all·心理学，2026-11-18 JWT 直连凭证）',
        '审定名词库“性别歧视”对应 gender discrimination（计划生育名词，2026-11-25 界面精确匹配复核）；'
        'sex discrimination 英文侧审定无独立条目，本行译形与审定形一致',
    ),
    'fundamental attribution error': (
        '审定名词库（termonline-all·心理学，2026-11-18 JWT 直连凭证）；FLAG 裁定 2026-11-21：'
        '审定名词库“基本归因误差／基本归因错误”两形并存，维持现译（维持现译）',
        '审定名词库作“基本归因错误”（社会学名词 4.1.9.3；2026-11-25 界面精确匹配复核，缓存中未见“误差”形）；'
        'FLAG 裁定 2026-11-21：维持现译“基本归因误差”（社会心理学文献通行形），与审定形并存',
    ),
}


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                if key in PATCH:
                    old, new = PATCH[key]
                    if cells[5].strip() != old:
                        raise SystemExit('旧依据不符，中止：%s\n 实际：%s' % (key, cells[5].strip()))
                    cells[5] = ' ' + new + ' '
                    cells[6] = ' ' + DATE + ' '
                    line = '|'.join(cells)
                    done.add(key)
        out.append(line)
    missing = set(PATCH) - done
    if missing:
        raise SystemExit('未找到行：%s' % missing)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行：%s' % (len(done), '、'.join(sorted(done))))


if __name__ == '__main__':
    main()
