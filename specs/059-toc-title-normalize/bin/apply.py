# -*- coding: utf-8 -*-
"""specs/059 写回器：SUMMARY.md / mu-lu-s.md 条目标题体例规范化（甲类 15＋乙类 11）。

设计约束（rules/05 批量改写纪律）：
- 整行精确匹配，不跑全局正则；每条 old 必须唯一命中，命中 0 或 >1 即中止（残余不为 0 禁写回）；
- 逐行身份追踪：每条记录 file/line_no/tag/old→new；
- 幂等：old 不存在而 new 行已存在，视为已应用，changed 不计；
- 不改行序、不增删行（行数守恒）。
"""
import io
import json
import os
import sys

sys.dont_write_bytecode = True

R = [
    # ---- 甲类 15：符号层归一 ----
    ('SUMMARY.md', 32, 'A1-见前空格',
     '  * \\*逻辑 ——见逻辑学：行动的逻辑 The Logic of Action — see logic: action',
     '  * \\*逻辑——见逻辑学：行动的逻辑 The Logic of Action — see logic: action'),
    ('SUMMARY.md', 36, 'A2-HTML实体',
     '  * \\*行动的理由：正当性、动机、解释——见行动的理由：正当性、动机、解释 reasons for action &ndash; justification, motivation, explanation — see reasons for action: justification, motivation, explanation',
     '  * \\*行动的理由：正当性、动机、解释——见行动的理由：正当性、动机、解释 reasons for action \u2013 justification, motivation, explanation — see reasons for action: justification, motivation, explanation'),
    ('SUMMARY.md', 214, 'A3-间隔号U2027',
     '* \\*弗朗索瓦-马里\u2027阿鲁埃——见伏尔泰 Arouet, François-Marie — see Voltaire',
     '* \\*弗朗索瓦-马里\u00b7阿鲁埃——见伏尔泰 Arouet, François-Marie — see Voltaire'),
    ('SUMMARY.md', 271, 'A4-见后冒号空格',
     '* \\*亚历山大·贝恩——见苏格兰哲学： 19 世纪苏格兰哲学 Bain, Alexander — see Scottish Philosophy in the 19th Century',
     '* \\*亚历山大·贝恩——见苏格兰哲学：19 世纪苏格兰哲学 Bain, Alexander — see Scottish Philosophy in the 19th Century'),
    ('SUMMARY.md', 279, 'A5-见后冒号空格',
     '* \\*詹姆斯·比蒂——见苏格兰哲学： 18 世纪苏格兰哲学 Beattie, James — see Scottish Philosophy in the 18th Century',
     '* \\*詹姆斯·比蒂——见苏格兰哲学：18 世纪苏格兰哲学 Beattie, James — see Scottish Philosophy in the 18th Century'),
    ('SUMMARY.md', 284, 'A6-见前空格',
     '* \\*存在与变化 ——见时间 being and becoming — see time',
     '* \\*存在与变化——见时间 being and becoming — see time'),
    ('SUMMARY.md', 539, 'A7-分组行序',
     '* \\*Confucianism 儒学',
     '* \\*儒学 Confucianism'),
    ('SUMMARY.md', 769, 'A8-冒号见',
     '  * \\*拉姆齐与代际福利经济学：见弗兰克·拉姆齐：拉姆齐与代际福利经济学 Ramsey and intergenerational welfare economics — see Ramsey, Frank: and intergenerational welfare economics',
     '  * \\*拉姆齐与代际福利经济学——见弗兰克·拉姆齐：拉姆齐与代际福利经济学 Ramsey and intergenerational welfare economics — see Ramsey, Frank: and intergenerational welfare economics'),
    ('SUMMARY.md', 1186, 'A9-见前空格',
     '* \\*人体试验 ——见生物医学伦理学：临床研究伦理 human test subjects — see The Ethics of Clinical Research',
     '* \\*人体试验——见生物医学伦理学：临床研究伦理 human test subjects — see The Ethics of Clinical Research'),
    ('SUMMARY.md', 2326, 'A10-冒号见',
     '  * \\*德性伦理学：见伦理学：德性伦理学 virtue ethics — see ethics: virtue',
     '  * \\*德性伦理学——见伦理学：德性伦理学 virtue ethics — see ethics: virtue'),
    ('SUMMARY.md', 2329, 'A11-冒号见',
     '* \\*角色义务：见义务：特殊义务 role obligations — see obligations: special',
     '* \\*角色义务——见义务：特殊义务 role obligations — see obligations: special'),
    ('SUMMARY.md', 2515, 'A12-分组行序',
     '* \\*speech 言语',
     '* \\*言语 speech'),
    ('SUMMARY.md', 2547, 'A13-冒号见',
     '  * \\*数学哲学：见数学哲学：数学哲学中的结构主义 Structuralism in the Philosophy of Mathematics — see mathematics, philosophy of: structuralism',
     '  * \\*数学哲学——见数学哲学：数学哲学中的结构主义 Structuralism in the Philosophy of Mathematics — see mathematics, philosophy of: structuralism'),
    ('mu-lu-s.md', 1618, 'A14-连接号一字线',
     '#### 13\u201314 世纪',
     '#### 13\u201414 世纪'),
    ('mu-lu-s.md', 2136, 'A15-连接号一字线',
     '### 19\u201320世纪',
     '### 19\u201420 世纪'),
    # ---- 乙类 11：别名行补中文连接（目标题为本库既有译名） ----
    ('SUMMARY.md', 680, 'B1-补见字',
     '* \\*设计论证——目的论：上帝存在的目的论论证 design, argument from — see teleology: teleological arguments for God\u2019s existence',
     '* \\*设计论证——见目的论：上帝存在的目的论论证 design, argument from — see teleology: teleological arguments for God\u2019s existence'),
    ('SUMMARY.md', 715, 'B2-道德动机',
     '  * \\*道德动机 moral — see moral motivation',
     '  * \\*道德动机——见道德动机 moral — see moral motivation'),
    ('SUMMARY.md', 985, 'B3-费里尔',
     '* \\*詹姆斯·弗雷德里克·费里尔 Ferrier, James — see Scottish Philosophy: in the 19th century',
     '* \\*詹姆斯·弗雷德里克·费里尔——见苏格兰哲学：19 世纪苏格兰哲学 Ferrier, James — see Scottish Philosophy: in the 19th century'),
    ('SUMMARY.md', 1229, 'B4-人格同一性',
     '  * \\*人格同一性 personal — see personal identity',
     '  * \\*人格同一性——见人格同一性 personal — see personal identity'),
    ('SUMMARY.md', 1808, 'B5-道德实在论',
     '  * \\*道德实在论 moral — see moral realism',
     '  * \\*道德实在论——见道德实在论 moral — see moral realism'),
    ('SUMMARY.md', 1817, 'B6-道德怀疑论',
     '  * \\*道德怀疑论 moral — see moral skepticism',
     '  * \\*道德怀疑论——见道德怀疑论 moral — see moral skepticism'),
    ('SUMMARY.md', 2247, 'B7-结构实在论',
     '  * \\*结构实在论 structural — see structural realism',
     '  * \\*结构实在论——见结构实在论 structural — see structural realism'),
    ('SUMMARY.md', 2378, 'B8-科学模型',
     '  * \\*科学模型 Models in Science — see models in science',
     '  * \\*科学模型——见科学模型 Models in Science — see models in science'),
    ('SUMMARY.md', 2516, 'B9-内部言语',
     '  * \\*内部言语 inner — see inner speech',
     '  * \\*内部言语——见内部言语 inner — see inner speech'),
    ('SUMMARY.md', 2556, 'B10-子结构逻辑',
     '* \\*子结构逻辑 substructural logics — see logic: substructural',
     '* \\*子结构逻辑——见子结构逻辑 substructural logics — see logic: substructural'),
    ('SUMMARY.md', 2562, 'B11-预先指示',
     '* \\*预先指示和替代决策 surrogate decision-making for incompetent individuals — see advance directives',
     '* \\*预先指示和替代决策——见预先指示和替代决策 surrogate decision-making for incompetent individuals — see advance directives'),
]


def read_lines(path):
    with io.open(path, encoding='utf-8', newline='') as f:
        return f.read().split('\n')


def write_lines(path, lines):
    with io.open(path, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(lines))


def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, 'SUMMARY.md')):
        parent = os.path.dirname(d)
        if parent == d:
            raise RuntimeError('仓库根未找到（自 %s 向上）' % __file__)
        d = parent
    return d


def main():
    argv = sys.argv[1:]
    dry = '--dry-run' in argv
    root = find_root()
    cache = {}
    report = {'written': not dry, 'applied': [], 'skipped_applied': [], 'abort': []}

    # 写回前置门：先全量核 old 命中，任一异常即整体中止
    for fname, line_no, tag, old, new in R:
        if fname not in cache:
            cache[fname] = read_lines(os.path.join(root, fname))
        lines = cache[fname]
        olds = [i for i, l in enumerate(lines) if l == old]
        news = [i for i, l in enumerate(lines) if l == new]
        if len(olds) == 1:
            continue
        if len(olds) == 0 and len(news) == 1:
            report['skipped_applied'].append({'tag': tag, 'line': line_no})
            continue
        report['abort'].append({'tag': tag, 'line': line_no, 'old_hits': len(olds),
                                'new_hits': len(news)})

    if report['abort']:
        print(json.dumps(report, ensure_ascii=False, indent=1))
        print('ABORT: 前置门不通过，未写回任何文件（残余不为 0 禁写回）')
        return 2

    # 逐行身份追踪替换
    for fname, line_no, tag, old, new in R:
        lines = cache[fname]
        olds = [i for i, l in enumerate(lines) if l == old]
        if olds:
            i = olds[0]
            lines[i] = new
            report['applied'].append({'file': fname, 'line': i + 1, 'tag': tag,
                                      'old': old, 'new': new})

    if not dry:
        for fname, lines in cache.items():
            write_lines(os.path.join(root, fname), lines)

    report['applied_count'] = len(report['applied'])
    report['skipped_count'] = len(report['skipped_applied'])
    print(json.dumps(report, ensure_ascii=False, indent=1))
    print('applied=%d skipped=%d abort=%d%s' % (
        report['applied_count'], report['skipped_count'], len(report['abort']),
        ' (dry-run)' if dry else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
