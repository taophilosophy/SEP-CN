# -*- coding: utf-8 -*-
"""批 65：44 条“有年份无职业”GND 候选的年代相容性复核（2026-11-26）。

查法：候选只有生年、无职业，无法按三重判据定性 → 改用**条目语境**判年代相容性，
再对可另指者回 Wikidata／GND 专档核实。凭证：WD 实体号＋GND 号（wd_entities.py 与
wd.json 留存 script/tmp，不入库），语境取 en/ 正文首现句（context 档案）。

本轮写册八行（其余判定只入台账，不动册）：

  Robertson, G. —— GND 候选 Guy Robertson 1954 年代不合；书目行“Robertson, G., [1876]
    ‘Mr. Jevons’ Formal Logic’, Mind 1: 206–22”即 Mind 创刊主编 George Croom Robertson
    （WD Q983704／GND 116576707，1842–1892，英格兰）→ 补生卒＋籍属。
  King, Peter —— lady-masham 语境为“洛克外甥 Peter King”，即第一代金男爵
    （WD Q7175194／GND 131343440，1669–1734）→ 补生卒＋籍属；候选 1951 年生者同名驳回。
  Klein, Peter —— closure-epistemic 语境为 Klein 1995 的知识论可传递性讨论，即 Peter D.
    Klein（WD Q7173507／GND 138894388，1940–，美国）→ 补生卒＋籍属；候选 1959 年德国
    短跑运动员（Q957312）同名驳回。
  Clarke, Edward —— lady-masham 语境为洛克友人爱德华·克拉克（Chipley，萨默塞特），
    GND 1055230068 与 WD Q19039689 同档（1650–1710，英格兰）→ 补生卒＋籍属，
    GND 记生年 1652 属异说，从通行 1650 并注。
  Burstall, Rod M. —— 生卒 1934–2025 已由 WD Q7356136 印证；补籍属 英国（同档国籍）。
  Stamos, David —— 生卒 1957– 印证；补籍属 加拿大（WD Q5237896 国籍）。
  Mehta, Uday —— 现记“1933”取自 GND 1145908829（Mehta, Uday 1933）；colonialism 语境
    作者为 Uday Singh Mehta（Liberalism and Empire 1999；WD Q28868996／GND 12165687X，
    政治学家，无年份）→ 判同名误取，生卒置回“—”并注，不再填。
  Nellie —— GND 候选 Ladd, Nellie E. 1859–1922 驳回：necessary-sufficient 正文中的
    Nellie 是“如果 Nellie 是一头大象”假设例子里的象名，非人物，不填生卒。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TABLE = 'ren-ming-biao.md'
DATE = '2026-11-26'

# 键 → (籍属列新值或 None, 生卒列新值或 None, 依据追加串)
FIX = {
    'Robertson, G.': (
        '英国', '1842–1892',
        '2026-11-26 复核：书目“Robertson, G., [1876] “Mr. Jevons’ Formal Logic”, Mind 1: '
        '206–22”为 Mind 创刊主编 George Croom Robertson（Wikidata Q983704／GND 116576707，'
        '1842–1892，英格兰），补生卒籍属；GND 检索候选 Guy Robertson 1954 系同名，驳回'),
    'King, Peter': (
        '英国', '1669–1734',
        '2026-11-26 复核：lady-masham 语境“his nephew Peter King”即第一代金男爵（洛克外甥），'
        'Wikidata Q7175194／GND 131343440，1669–1734，补生卒籍属；GND 候选 1951 年生者同名驳回'),
    'Klein, Peter': (
        '美国', '1940–',
        '2026-11-26 复核：closure-epistemic 所引 Klein 1995 为知识论者 Peter D. Klein'
        '（Wikidata Q7173507／GND 138894388，1940–，美国），补生卒籍属；GND 候选 1959 年'
        '德国短跑运动员（Q957312）同名驳回'),
    'Clarke, Edward': (
        '英国', '1650–1710',
        '2026-11-26 复核：lady-masham 语境洛克友人爱德华·克拉克（Chipley，萨默塞特），'
        'GND 1055230068 与 Wikidata Q19039689 同档，生卒 1650–1710，籍属英格兰→英国；'
        'GND 记生年 1652 属异说，从通行 1650'),
    'Burstall, Rod M.': (
        '英国', None,
        '2026-11-26 复核：Wikidata Q7356136 国籍英国、生卒 1934–2025 与在册一致，补籍属'),
    'Stamos, David': (
        '加拿大', None,
        '2026-11-26 复核：Wikidata Q5237896 国籍加拿大，补籍属；生卒 1957– 与同档一致'),
    'Mehta, Uday': (
        None, '—',
        '2026-11-26 复核：原记“1933”取自 GND 1145908829（Mehta, Uday 1933），而 colonialism '
        '语境作者为 Uday Singh Mehta（Liberalism and Empire 1999；Wikidata Q28868996／'
        'GND 12165687X，政治学家，权威档无年份）→ 判同名误取，生卒置回“—”'),
    'Nellie': (
        None, None,
        '2026-11-26 复核：词条例子“如果 Nellie 是一头大象”中的象名，非人物；'
        'GND 候选 Ladd, Nellie E. 1859–1922 驳回，生卒不填'),
}


def main():
    lines = io.open(TABLE, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 9 and cells[1].strip() in FIX:
                key = cells[1].strip()
                nation, life, note = FIX[key]
                if note not in cells[7]:
                    cells[7] = cells[7].rstrip() + '；' + note + ' '
                if nation is not None:
                    cells[4] = ' %s ' % nation
                if life is not None:
                    cells[5] = ' %s ' % life
                cells[8] = ' %s ' % DATE
                done.add(key)
                line = '|'.join(cells)
        out.append(line)
    missing = set(FIX) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    io.open(TABLE, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('写册 %d 行' % len(done))


if __name__ == '__main__':
    main()
