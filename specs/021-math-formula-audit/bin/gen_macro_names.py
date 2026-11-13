# -*- coding: utf-8 -*-
r"""021 生成 tools/data/sep-macro-names.json：各词条 SEP 自定义宏名清单。

check_math_zh.py 门禁用它判定「译文公式里还有未展开的 SEP 宏」（站点
MathJax 3 无此表，残留即红字）。只存名字，不存展开体——展开体属过程产物，
留在 specs/021 results/macro-table.json。
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SRC = os.path.join(HERE, '..', 'results', 'macro-table.json')
DEST = os.path.join(REPO, 'tools', 'data', 'sep-macro-names.json')


def main():
    table = json.load(open(SRC, encoding='utf-8'))
    names = {slug: sorted(spec) for slug, spec in table.items() if spec}
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    json.dump(names, open(DEST, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1, sort_keys=True)
    print('slugs:', len(names), 'total names:',
          sum(len(v) for v in names.values()), '→', DEST)


if __name__ == '__main__':
    main()
