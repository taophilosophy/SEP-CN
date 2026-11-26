# -*- coding: utf-8 -*-
"""把 44 条“有年份无职业”候选的复核定论写回 gnd-review-decisions 台账（2026-11-26）。

判定四档：采信候选（在册与候选一致）／同名驳回（语境年代或身份不可能）／
改判识别（候选本身同名，但所指人物另有权威档，已在册补录）／存疑／未判（年份相容
但无职业旁证，按两档方案 B 档留空）。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
LEDGER = 'specs/013-person-attribution/results/gnd-review-decisions-2026-11-26.tsv'

ACCEPT = '采信候选（生年与在册一致，无新增）'
VERDICTS = {
    # ---- 改判识别：候选同名，所指另有专档 ----
    'Robertson, G.': ('改判识别',
        '候选 Guy Robertson 1954 年代不合；Mind 1 (1876) 书目行即 George Croom Robertson'
        '（WD Q983704/GND 116576707，1842–1892）已补册'),
    'King, Peter': ('改判识别',
        'lady-masham 指洛克外甥，即第一代金男爵（WD Q7175194/GND 131343440，1669–1734）已补册'),
    'Klein, Peter': ('改判识别',
        'closure-epistemic 指 Peter D. Klein（WD Q7173507/GND 138894388，1940–）已补册；'
        '候选 1959 年德国短跑运动员 Q957312 同名'),
    'Clarke, Edward': ('改判识别',
        'lady-masham 指洛克友人 Edward Clarke of Chipley，GND 1055230068 与 WD Q19039689 同档 '
        '1650–1710，生年 GND 记 1652 属异说，已补册'),
    # ---- 同名驳回 ----
    'Baumgartner, Michael': ('同名驳回',
        '候选 1996 年生；本人 2010 年已发表 Canadian J Phil 论文，年代不可能'),
    'Beurer, Johann Jakob': ('同名驳回',
        '语境为施图尔姆（1507 年生）幼年宫廷牧师，候选 1666–1667 年代不可能'),
    'Callias': ('同名驳回',
        '语境为柏拉图笔下雅典人卡利阿斯；候选 Augustin Callias 1573–1627 为同名异人'),
    'Falk, Richard': ('同名驳回', '语境为国际法学者 Richard Falk（1930 年生），候选 1903 同名'),
    'Fritsche, Franz': ('同名驳回',
        'quine-nf 致谢中当代纠错者，候选 1855 年生年代不可能'),
    'Homer': ('同名驳回', '语境为古希腊诗人荷马；候选 Homér 1964–2011 为匈牙利乐手诗人同名'),
    'Hotho': ('同名驳回', '语境为黑格尔派美术史家 Hotho（19 世纪）；候选 Klaus Hotho 1943 同名'),
    'Howard, William': ('同名驳回',
        '语境为 Curry–Howard 对应的 W. Howard（1980 论文）；候选 Lord William Howard '
        '1563–1640 同名异人'),
    'Huang, Xu': ('同名驳回', '语境为 Fetchenhauer & Huang 2004 作者；候选 1989 年生，年代不可能'),
    'Johann Friedrich': ('同名驳回',
        '语境为主教约翰·弗里德里希宫廷（莱布尼茨 1677）；候选 Grote 1679–1731 同名异人'),
    'Nellie': ('同名驳回',
        'necessary-sufficient 例子中的象名，非人物；候选 Ladd, Nellie E. 1859–1922 驳回'),
    'Noble, C.': ('同名驳回',
        '语境为 Noble (2024) 波爱修斯研究者；候选 Powell, Noble C. 1891–1968 圣公会牧师同名'),
    'Radcliff': ('同名驳回',
        'bradley 语境为“美国工程师 Radcliff”；候选 Radcliff, Nicolaus 1398 修士同名异人'),
    'Regnier, Laurent': ('同名驳回',
        '语境为 Danos & Regnier 1989 线性逻辑；候选 1852 年比利时贵族同名异人'),
    'Straub, Paul': ('同名驳回',
        '语境为 Straub & Murnighan 1995；候选 Straub, Paul-Pierre 1911 年代不合'),
    'Ubaldo': ('同名驳回',
        'descartes-works 语境为 16 世纪意大利自然哲学家 Ubaldo（与塔尔塔利亚并列）；'
        '候选 Stallforth, Ubaldo 1953 同名异人'),
    # ---- 存疑 ----
    'Mehta, Uday': ('存疑',
        '在册 1933 取自候选 GND 1145908829；语境作者为 Uday Singh Mehta'
        '（WD Q28868996/GND 12165687X，无年份）→ 判同名误取，生卒已置回“—”'),
    'Stanhope, Philip': ('存疑',
        'hume-aesthetics 语境为休谟 1776 年前顾问；候选 1755–1815 系第五代切斯特菲尔德伯爵'
        '（WD Q1026379），年代偏晚；另有 Philip Stanhope 1732–1768（Q7184415）年代相容，待专查'),
    'Stegmann, Ulrich': ('存疑',
        '语境为 Stegmann 2009/2015 生物信息语义学；候选 1935 年生者（GND 1220119938，柏林）'
        '年龄偏高，职业无载，未敢采信'),
    'Farley, Belmont': ('存疑',
        '语境为 1954 年林肯实验室神经网络模拟；候选 GND 1020773553（1891 年生，Mercer 名）'
        '年龄虽可能但不十足，职业无载，留待专查'),
    # ---- 未判：年份相容、无职业旁证 ----
    'Michael, John': ('未判', '候选 1953 生年与 2022 专著相容；GND 无职业、WD 为同源导入，留空'),
    'Ross, Stephanie': ('未判', '候选 1970 生年与 2008 论文相容；GND 无职业、WD 同源导入，留空'),
    'Schulz, Stephan': ('未判', '候选 1975 生年与自动定理证明工作相容；GND 无职业，留空'),
    'Simmons, Craig': ('未判', '候选 1959 生年无矛盾；首现 fuller-margaret 语境未定，留空'),
    'Stephens, Chris': ('未判', '候选 1964 生年与 2004 论文相容；GND 无职业，留空'),
    'White, Jonathan': ('未判', '候选 1960 生年与 2014 论文相容；GND 无职业，留空'),
    'Young, Robert': ('未判', '候选 1952 生年与 2007/2017 论文相容；GND 无职业，留空'),
    'Müller, Johannes': ('未判', '首现为语料回收（无词条语境），候选 1902 无法核身份，留空'),
}


def main():
    lines = io.open(LEDGER, encoding='utf-8', newline='').read().split('\n')
    out, seen = [], set()
    for line in lines:
        if line and not line.startswith('键'):
            c = line.split('\t')
            if len(c) >= 8 and c[2].strip() and not c[4].strip():
                key = c[0]
                if key in VERDICTS:
                    c[6], c[7] = VERDICTS[key]
                    seen.add(key)
                elif key not in seen:
                    c[6], c[7] = ACCEPT, '生年与在册一致（GND 无职业，未作新填）'
                    seen.add(key)
                line = '\t'.join(c)
        out.append(line)
    allk = set(VERDICTS) | {k for k in seen}
    io.open(LEDGER, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('台账更新 %d 条（其中专档 %d 条）' % (len(seen), len(VERDICTS)))


if __name__ == '__main__':
    main()
