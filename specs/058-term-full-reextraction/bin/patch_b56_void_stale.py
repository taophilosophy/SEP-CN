# -*- coding: utf-8 -*-
"""批 56：清理同行的作废旧记（2026-11-26，批 55 的收尾）。

批 55 把 arché、Bedeutung、Sittlichkeit、Vorstellung 等行的“审定库无相关命中”改判为
审定确有条目，但行内更早还留着一句“审定库精确查无（凭证 2026-10-31）”，与改判并列
自相矛盾。本批只给这三行的旧记加作废标注，不删原文（不删历史口径）。

hypersequent、Novum Organum 两行出现两处“2026-11-26 界面”，系两族负证各盖一戳，
措辞各自成立，不动。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'
OLD = '；审定库精确查无（凭证 2026-10-31）'
NEW = '；旧记“审定库精确查无”（凭证 2026-10-31）经 2026-11-26 界面复核作废'
KEYS = ('Bedeutung', 'Sittlichkeit', 'Vorstellung')


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8 and cells[1].strip() in KEYS and OLD in cells[5]:
                cells[5] = cells[5].replace(OLD, NEW, 1)
                cells[6] = ' %s ' % DATE
                done.add(cells[1].strip())
                line = '|'.join(cells)
        out.append(line)
    missing = set(KEYS) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('作废标注 %d 行' % len(done))


if __name__ == '__main__':
    main()
