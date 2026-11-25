# -*- coding: utf-8 -*-
"""批 42：把 94 行“审定库复核一致”按界面精确匹配结果改写（2026-11-25）。

背景：该措辞是 2026-10-29 浏览器通道留下的整批套语，批 41 抽验发现真假混杂
（学术自由、不可知论等确在审定库；绝对唯心主义、古代哲学、中国哲学、演绎系统
查无）。故逐条过界面“精确匹配”，结果分四型改写：

  在案   审定公布名词库有同形条目 → 补 2026-11-25 复核日期
  无对口 界面明示“未审定” → 原“复核一致”作废，改记无对口
  两岸   仅海峡两岸名词对照库有 → 改记库名
  形异   审定库同概念作他形（犹太教→以色列教等）→ 如实记审定形

只动这一处套语，其余依据文字、译法、首现一概不动。
"""
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
TMP = os.path.join(os.environ.get('LOCALAPPDATA', '.'), 'Temp')
OUT = 'specs/058-term-full-reextraction/results/ui-check-recheck-94-2026-11-25.tsv'
OLD = '审定库复核一致（termonline-all 浏览器通道凭证 2026-10-29）'
NEW_OK = '审定库复核一致（termonline-all 浏览器通道凭证 2026-10-29；2026-11-25 界面精确匹配复核在案）'
NEW_MISS = '审定库无对口条目（2026-11-25 界面精确匹配复核：未审定；原“审定库复核一致”表述作废）'
NEW_TW = '海峡两岸名词对照库有同形条目（2026-11-25 界面精确匹配复核；原“审定库复核一致”表述作废，该库非审定公布库）'
NEW_DIFF = '审定库作“%s”（2026-11-25 界面精确匹配复核；与本行主形不同，原“复核一致”表述作废）'
NON_AUDIT = ('海峡两岸', '国家标准', '标准文件', '百科', '辞典')


def load_ui():
    got = {}
    for p in sorted(glob.glob(os.path.join(TMP, 'tl_ui4_b*.json'))):
        for r in json.load(io.open(p, encoding='utf-8')):
            got[r['zh']] = r
    return got


def verdict(zh, rec):
    forms = {zh} | {x.strip() for x in re.split(r'[；;／/]', zh) if x.strip()}
    cards = rec.get('cards') or []
    audit = [c for c in cards if not any(k in (c.get('src') or '') for k in NON_AUDIT)]
    if audit:
        same = [c for c in audit if (c.get('cn') or '').strip() in forms]
        if same:
            return 'ok', same[0].get('src', '')
        return 'diff', audit[0].get('cn', '')
    if cards:
        return 'tw', cards[0].get('src', '')
    return 'miss', ''


def main():
    ui = load_ui()
    rows, seen, out = [], {}, []
    for line in io.open(TERMS, encoding='utf-8', newline='').read().split('\n'):
        if line.startswith('|'):
            c = line.split('|')
            if len(c) >= 8 and OLD in c[5]:
                zh = c[3].strip().split('（')[0].strip('《》').strip()
                rec = ui.get(zh)
                if not rec:
                    for part in re.split(r'[；;／/]', zh):
                        rec = ui.get(part.strip())
                        if rec:
                            break
                if not rec:
                    rows.append((zh, 'norec', ''))
                    line2 = line
                else:
                    v, info = verdict(zh, rec)
                    if v == 'ok':
                        new = c[5].replace(OLD, NEW_OK)
                    elif v == 'miss':
                        new = c[5].replace(OLD, NEW_MISS)
                    elif v == 'tw':
                        new = c[5].replace(OLD, NEW_TW)
                    else:
                        new = c[5].replace(OLD, NEW_DIFF % info)
                    c[5] = new
                    c[6] = ' 2026-11-25 '
                    line2 = '|'.join(c)
                    rows.append((zh, v, info))
                    seen[zh] = seen.get(zh, 0) + 1
                out.append(line2)
                continue
        out.append(line)
    if not rows:
        raise SystemExit('没有命中待改行，中止')
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('zh\tverdict\thit\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    from collections import Counter
    print('改写 %d 处：' % len(rows), dict(Counter(r[1] for r in rows)))
    print('→', OUT)


if __name__ == '__main__':
    main()
