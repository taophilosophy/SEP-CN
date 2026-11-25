# -*- coding: utf-8 -*-
"""批 49：11 行“审定已查无对口”依据补日期化界面复核记录（2026-11-26）。

这些行的依据是模糊时代的措辞（“审定库无查询件（目录现查 2026-11-10）”等），语义正确但
没有界面复核的日期与结论；批 48 的界面逐条核已覆盖全部 11 行，现将结论写回依据列，
使 ADR-0088 机检（审定引用配对）对它们放行有据。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'

# 键 → (旧片段, 新片段)
PATCH = {
    'constellation': (
        '审定库无查询件（termonline-all 目录现查 2026-11-10）',
        '审定库无查询件（termonline-all 目录现查 2026-11-10）；2026-11-26 界面精确匹配复核：无“星丛”对口',
    ),
    'explanatory store': (
        '随 explanation＝说明（审定）与 explanatory power＝说明能力统一族形；Kitcher E(K) 语境',
        '随 explanation＝说明（审定）与 explanatory power＝说明能力统一族形；Kitcher E(K) 语境；'
        '2026-11-26 界面精确匹配复核：审定库无“说明库”对口（explanation＝说明 在案）',
    ),
    'global governance': (
        '审定库无精确命中，2026-11-25）；凭证 2026-11-25',
        '审定库无精确命中，2026-11-25；2026-11-26 界面精确匹配复核：无“全球治理”对口）；凭证 2026-11-25',
    ),
    'homunculus': (
        '与审定 homunculus fallacy＝微型人谬误 分域，维持（维持现译）',
        '与审定 homunculus fallacy＝微型人谬误 分域，维持（维持现译）；'
        '2026-11-26 界面精确匹配复核：审定库无“侏儒图”对口（侏儒＝dwarf，兽医学）',
    ),
    'hypersequent': (
        '随 sequent＝矢列式（审定）统一族形',
        '随 sequent＝矢列式（审定，2026-11-26 界面精确匹配复核在案）统一族形；'
        '2026-11-26 界面精确匹配复核：审定库无“超矢列式”对口',
    ),
    'identity thinking': (
        '审定库无查询件（termonline-all 目录现查 2026-11-10）',
        '审定库无查询件（termonline-all 目录现查 2026-11-10）；2026-11-26 界面精确匹配复核：无“同一性思维”对口',
    ),
    'immanent critique': (
        '审定库无查询件（termonline-all 目录现查 2026-11-10）',
        '审定库无查询件（termonline-all 目录现查 2026-11-10）；2026-11-26 界面精确匹配复核：无“内在批判”对口',
    ),
    'prajñapti': (
        '撞形改定 2026-11-21：审定 Prajñapti＝假名；假立归 upādhi',
        '撞形改定 2026-11-21；2026-11-26 界面精确匹配复核：审定“假名”对应 pseudonymity／Kana'
        '（新闻学与传播学／世界历史名词），非佛典义，审定库无 prajñapti 对口；假立归 upādhi',
    ),
    'probabilism': (
        '审定库仅模糊噪声命中（凭证 2026-10-31）',
        '审定库仅模糊噪声命中（凭证 2026-10-31）；2026-11-26 界面精确匹配复核：无“或然论”对口',
    ),
    'second nature': (
        '审定库无查询件（termonline-all 目录现查 2026-11-10）',
        '审定库无查询件（termonline-all 目录现查 2026-11-10）；2026-11-26 界面精确匹配复核：'
        '无“第二自然”对口（审定收“人工自然”为另词）',
    ),
    'taṣdīq': (
        '审定库仅模糊噪声命中（凭证 2026-10-31）',
        '审定库仅模糊噪声命中（凭证 2026-10-31）；2026-11-26 界面精确匹配复核：无“断定”对口',
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
                    if old not in cells[5]:
                        raise SystemExit('旧依据不符，中止：%s\n 实际：%s' % (key, cells[5].strip()))
                    cells[5] = cells[5].replace(old, new)
                    cells[6] = ' %s ' % DATE
                    line = '|'.join(cells)
                    done.add(key)
        out.append(line)
    missing = set(PATCH) - done
    if missing:
        raise SystemExit('未找到行：%s' % missing)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('补记 %d 行：%s' % (len(done), '、'.join(sorted(done))))


if __name__ == '__main__':
    main()
