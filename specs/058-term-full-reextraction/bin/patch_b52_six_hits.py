# -*- coding: utf-8 -*-
"""批 52：6 行“审定库无查询件”实为审定有条目，按界面复核改正（2026-11-26）。

12 行“termonline-all 目录现查 2026-11-10”的旧措辞逐条界面核验：
  反犹主义、商品拜物教、文化工业、工具理性、否定的辩证法、非同一性 —— 审定库确有条目
  晚期资本主义 —— 仅海峡两岸名词对照库
  权威主义人格、星丛、同一性思维、内在批判、第二自然 —— 确无（前四行已于批 49 补记）
本批改正 6 行（否定辩证法一行已在批 52 之外的清单中，见下）。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'
OLD = '审定库无查询件（termonline-all 目录现查 2026-11-10）'

NEW = {
    'anti-Semitism / Antisemitism':
        '审定作“反犹主义”（Anti-Semitism，世界历史名词；2026-11-26 界面精确匹配复核）',
    'commodity fetishism':
        '审定作“商品拜物教”（commodity fetishism，经济学名词；2026-11-26 界面精确匹配复核）',
    'culture industry':
        '审定作“文化工业”（cultural industry，新闻学与传播学名词；2026-11-26 界面精确匹配复核）',
    'instrumental reason':
        '审定作“工具理性”（instrumental rationality; instrumental reason，自然辩证法名词；'
        '2026-11-26 界面精确匹配复核）',
    'late capitalism':
        '海峡两岸名词对照库作“晚期资本主义”（late capitalism，地理学名词；非审定公布库，'
        '2026-11-26 界面精确匹配复核）',
    'the nonidentical / non-identity':
        '审定作“非同一性”（nonidentity，马克思主义；2026-11-26 界面精确匹配复核）',
}


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                if key in NEW and OLD in cells[5]:
                    cells[5] = cells[5].replace(OLD, NEW[key])
                    cells[6] = ' %s ' % DATE
                    line = '|'.join(cells)
                    done.add(key)
        out.append(line)
    missing = set(NEW) - done
    if missing:
        raise SystemExit('未找到行：%s' % missing)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行：%s' % (len(done), '、'.join(sorted(done))))


if __name__ == '__main__':
    main()
