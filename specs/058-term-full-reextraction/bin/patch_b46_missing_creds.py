# -*- coding: utf-8 -*-
"""批 46：三行“缺凭证”用界面精确匹配补齐（2026-11-25）。

halting problem、right inverse、selector 自批 37 起标“本地无缓存凭证，待通道恢复补证”。
界面复核结果：
  halting problem → 停机问题（自然辩证法名词／计算机科学技术名词／数学名词）
  right inverse   → 右逆元（数学名词，right inverse element）
  selector        → 选择子（海峡两岸遗传学名词，selector）
只把这句待办换成复核记录，其余不动。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
OLD = '；2026-11-25 凭证对账：本地无缓存凭证（键名或已变），待通道恢复补证'
NEW = {
    'halting problem': '；2026-11-25 界面精确匹配复核：自然辩证法名词／计算机科学技术名词／数学名词均作“停机问题”，凭证在案',
    'right inverse': '；2026-11-25 界面精确匹配复核：数学名词作“右逆元”（right inverse element），凭证在案',
    'selector': '；2026-11-25 界面精确匹配复核：海峡两岸遗传学名词作“选择子”（selector），凭证在案',
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
                    line = '|'.join(cells)
                    done.add(key)
        out.append(line)
    missing = set(NEW) - done
    if missing:
        raise SystemExit('未找到：%s' % missing)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('补齐 %d 行：%s' % (len(done), '、'.join(sorted(done))))


if __name__ == '__main__':
    main()
