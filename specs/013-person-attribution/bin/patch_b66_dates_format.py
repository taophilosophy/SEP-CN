# -*- coding: utf-8 -*-
"""批 66：生卒列异形与同名误填（2026-11-26）。

由“生卒格式异形”量测牵出四类：

1. 单年无破折号（6 行）——在册值本义为“生年，卒年不详”，按全表 1112 行既有口径补破折号；
   其中 Walter Kinder 的卒年由 en/scholz 正文括注补出（1909–1998）。
2. GND 占位串（Koslicki）——GND 1058425617 的 dateOfBirth 是字面 “[19XX]”，被原样抄进册，
   属机械抄录缺陷，清为“—”。
3. 同名误填（Yin Xian）——尹咸为汉代太史（《数术略》辑者），在册 1943 取自 GND
   1048302512（Yin, Xian，现代人），年代不可能，清为“—”。
4. 其余保留原值，仅补破折号（格式归一，不动证据）。

前置门：每条旧值必须逐字命中；改后生卒列不得出现单年或方括号；幂等。
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
TABLE = 'ren-ming-biao.md'
DATE = '2026-11-26'

# 键 → (旧生卒原值, 新生卒, 追加依据或 '')
FIX = {
    'Alvarado, José Tomás': ('1969', '1969–', ''),
    'Gollwitzer, Manfred': ('1947', '1947–', ''),
    'Lévy, Jean-Jacques': ('1947', '1947–', ''),
    'Taylor, C.C.W.': ('1936', '1936–', ''),
    'Walter Kinder': (
        '1909', '1909–1998',
        '2026-11-26 补卒年：en/scholz 正文括注 Walter Kinder (1909–1998)（与 GND 生年 1909 一致）'),
    'Koslicki, Kathrin': (
        '[19X–', '—',
        '2026-11-26 核：GND 1058425617 的 dateOfBirth 为字面占位“[19XX]”，非年份，'
        '原样抄录入册系抄录缺陷，清为“—”；权威档无确年'),
    'Yin Xian': (
        '1943', '—',
        '2026-11-26 核：尹咸为汉代太史（《数术略》辑者），在册 1943 取自 GND 1048302512'
        '（Yin, Xian，现代同名者），年代不可能，清为“—”'),
}


def main():
    lines = io.open(TABLE, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 9 and cells[1].strip() in FIX:
                key = cells[1].strip()
                old, new, note = FIX[key]
                if cells[5].strip() == new:      # 幂等：已改过则跳过
                    done.add(key)
                    out.append(line)
                    continue
                if cells[5].strip() != old:
                    raise SystemExit('%s 旧值不符：%r ≠ %r' % (key, cells[5].strip(), old))
                cells[5] = ' %s ' % new
                if note and note not in cells[7]:
                    cells[7] = cells[7].rstrip() + '；' + note + ' '
                cells[8] = ' %s ' % DATE
                done.add(key)
                line = '|'.join(cells)
        out.append(line)
    missing = set(FIX) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    text = '\n'.join(out)
    io.open(TABLE, 'w', encoding='utf-8', newline='\n').write(text)
    bad = []
    for line in out:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 9 and cells[1].strip() and cells[1].strip() != '键':
                d = cells[5].strip()
                if re.fullmatch(r'\d{3,4}', d) or re.search(r'[\[\]]', d):
                    bad.append((cells[1].strip(), d))
    print('改正 %d 行；残余异形 %d' % (len(done), len(bad)))
    if bad:
        raise SystemExit('残余：%r' % bad[:5])


if __name__ == '__main__':
    main()
