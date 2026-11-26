# -*- coding: utf-8 -*-
"""生成 GND review 候选判定台账（2026-11-26，覆盖全部 383 条）。

输入
  specs/013-person-attribution/results/gnd-review-short-2026-11-26.tsv（383 条）
  script/tmp/review-signals.tsv（281 条“缺年份或缺职业”者的条目内引证旁证）
输出
  specs/013-person-attribution/results/gnd-review-decisions-2026-11-26.tsv

判定口径（两档方案）：GND 只产 dossier，采信＝姓名、职业、年代、条目语境四者相容；
非学界职业驳回；学界职业但语境不符记同名异人；无生卒或缺职业且无法从条目旁证定身份者
记“未判”，随译核。采信者仍留人工终审。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
SRC = 'specs/013-person-attribution/results/gnd-review-short-2026-11-26.tsv'
SIG = 'script/tmp/review-signals.tsv'
OUT = 'specs/013-person-attribution/results/gnd-review-decisions-2026-11-26.tsv'

ACCEPT = {
    'Thijssen, Hans': 'buridan 注释引 Hans Thijssen，中古哲学史家（Nijmegen）',
    'Tuna, Emine Hande': 'imaginative-resistance 词条作者（citation_author）',
    'Planer, Ronald': 'gene 词条引 Planer 2014（Ronald J. Planer，生物学哲学家）',
    'Hawkins, Jennifer': 'informed-consent 引 Hawkins 2008（Jennifer S. Hawkins，生命伦理）',
    'Wülfer, Daniel': 'johann-sturm 正文：圣洛伦茨牧师兼教长',
    'Rötenbeck, Georg Paul': 'johann-sturm 正文：阿尔特多夫教授、悼文作者',
}
SUSPECT = {
    'Páez, Andrés': 'GND 记法学家（Ibarra 1966）；SEP 记其哲学学士，职业不符，待人工',
}
REJECT = {
    'Hippo': '非人名（地名／残句），GND 命中经济学者属同名',
    'Nicanor': '同名哲学家，Bayle 词条无此引证',
    'Lin, J.': '同名心理学家；belief-merging 引者为 Jinxin Lin（逻辑学者）',
    'Martin, Christopher J.': '同名史家；binarium 语境为逻辑史学者，职业不符',
    'Magee, John': '同名经济学者；boethius 引者为多伦多古典学者',
    'Jenkins': '同名艺术史家，disability 语境不符',
    'Moran, Thomas': '同名汉学家；environmental-aesthetics 引者为画家 Thomas Moran',
    'Webb, Peter': '同名阿拉伯学家，erotic-art 引者不符',
    'Thompson, Paul': '同名史家；fitness 引者为生物学哲学家',
    'Wilson, James': '同名史家，fitness 语境不符',
    'Griffiths, Paul': '同名史家；genetics 引者为生物学哲学家 Paul E. Griffiths',
    'MacLeod, Colin': '同名古典学家；genetics 引者为遗传学家（1909–1972）',
    'Elihu': '圣经人名；GND 命中社会学家属同名',
    'Weinrich, Martin': '同名医师，gianfrancesco-pico 语境未证',
    'Valentini, Laura': '同名史家；应为政治哲学家 Laura Valentini',
    'Smith, Holly': '同名史家；justice-moral-psych 引者为伦理学家',
    'Martini, Simone': '同名史家，logic-linear 语境不符',
    'Nicolas, David': '同名法学家；logic-massexpress 引者为哲学家 David Nicolas',
    'Sutton, Peter': '同名人类学家，logic-massexpress 语境未证',
    'Perry, John': '同名神学家；logic-relevance 引者为哲学家 John Perry',
    'Crupi, Vincenzo': '同名文学研究者；necessary-sufficient 引者为科学哲学家',
    'Jonah': '圣经人名；GND 命中法学家属同名',
    'Grant, Robert': '同名统计学家，oakeshott 引者不符',
    'Pöll, Wilhelm': '同名神学家，reinach 语境未证',
    'Thaumas': '同名法学家，xenophanes 语境不符',
    'Campbell': '同名男爵法学家，zombies 语境不符',
    'Charles Mills': '同名经济学家（Tiebout, Charles Mills 1924–1968）；应为 Charles W. Mills（1951–2021）',
    'John Norton': '同名史家；语料回收无首现条目可核',
    'Le Seur': '同名神学家；语料回收无首现条目可核',
    'Hippo, Yasuyuki': '非人名（地名／残句）',
}


def main():
    signals = {}
    try:
        for l in io.open(SIG, encoding='utf-8'):
            c = l.rstrip('\n').split('\t')
            if len(c) >= 8 and c[0] != '键':
                signals[c[0]] = c[7]
    except IOError:
        pass
    rows = []
    for l in io.open(SRC, encoding='utf-8'):
        x = l.rstrip('\n').split('\t')
        if len(x) < 7 or x[0] == '键' or x[1] != 'review':
            continue
        key, cand, years, pob, occ, gnd = x[0], x[2], x[3], x[4], x[5], x[6]
        if key in ACCEPT:
            verdict, why = '采信候选', ACCEPT[key]
        elif key in SUSPECT:
            verdict, why = '存疑', SUSPECT[key]
        elif key in REJECT:
            verdict, why = '驳回', REJECT[key]
        elif years and occ:
            verdict, why = '驳回', '职业非学界（%s）' % occ
        else:
            verdict = '未判'
            why = '无生卒或缺职业，随译核；条目内引证 %s' % (
                '有' if signals.get(key) == 'Y' else '无／未搜到')
        rows.append((key, cand, years, pob, occ, gnd, verdict, why))
    order = {'采信候选': 0, '存疑': 1, '未判': 2, '驳回': 3}
    rows.sort(key=lambda r: (order[r[6]], r[0]))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('键\t候选名\t生卒\t出生地\t职业\tGND\t判定\t理由\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    from collections import Counter
    print('台账 %d 行：%s' % (len(rows), dict(Counter(r[6] for r in rows))))


if __name__ == '__main__':
    main()
