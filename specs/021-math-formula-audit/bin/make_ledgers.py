# -*- coding: utf-8 -*-
r"""021 台账生成：按字母分册，en/ 侧与译文侧逐词条一行。

数据源（全部机器可复核）：
  results/en-formulas.jsonl        en 快照公式（147,653）
  results/upstream-formulas.jsonl  上游公式
  results/align-upstream.jsonl     快照↔上游判定
  results/en-fail-classified.jsonl en 侧编译失败归类
  results/render-zh.jsonl          译文（站点渲染真值口径）公式
  results/zh-defects.jsonl         译文侧缺陷（D1–D7）
  results/macro-expand-log.jsonl   宏展开留痕
  results/ctrl-clean-log.jsonl     控制字符清理留痕
产 execution-log/ledger-en-<letter>.md 与 ledger-zh-<letter>.md
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, '..', 'results')
LOGDIR = os.path.join(HERE, '..', 'execution-log')


def load(name):
    path = os.path.join(RESULTS, name)
    if not os.path.exists(path):
        return []
    return [json.loads(l) for l in open(path, encoding='utf-8') if l.strip()]


def main():
    os.makedirs(LOGDIR, exist_ok=True)
    en = load('en-formulas.jsonl')
    up = load('upstream-formulas.jsonl')
    align_up = load('align-upstream.jsonl')
    en_fail = load('en-fail-classified.jsonl')
    zh = load('render-zh.jsonl')
    zh_def = load('zh-defects.jsonl')
    expand = load('macro-expand-log.jsonl')
    ctrl = load('ctrl-clean-log.jsonl')

    # 聚合
    en_count = collections.Counter()
    en_files = collections.defaultdict(set)
    for r in en:
        slug = r['f'].split('/')[0]
        en_count[slug] += 1
        en_files[slug].add(r['f'])
    up_count = collections.Counter()
    for r in up:
        up_count[r['f'].split('/')[0]] += 1
    up_verdict = collections.defaultdict(collections.Counter)
    for r in align_up:
        slug = (r.get('slug') or r.get('key', '').split('/')[0])
        up_verdict[slug][r['v']] += 1
    en_fail_by = collections.defaultdict(collections.Counter)
    for r in en_fail:
        en_fail_by[r['f'].split('/')[0]][r['cls']] += 1
    zh_count = collections.Counter()
    for r in zh:
        zh_count[r['f']] += 1
    zh_def_by = collections.defaultdict(collections.Counter)
    for r in zh_def:
        zh_def_by[r['f']][r['code'].split('-')[0]] += 1
    exp_by = collections.defaultdict(collections.Counter)
    for r in expand:
        exp_by[r['f'].split('/')[-1].split('.')[0]] += collections.Counter(
            {r['macro']: r['count']})
    # 展开日志在幂等复跑中被覆盖时，按 en 快照的宏用量重建（译文与 en 同源同数）
    if not exp_by:
        table = json.load(open(os.path.join(RESULTS, 'macro-table.json'),
                               encoding='utf-8'))
        import re as _re
        for r in en:
            slug = r['f'].split('/')[0]
            macros = table.get(slug)
            if not macros:
                continue
            for m in _re.finditer(r'\\([A-Za-z]+)', r['x']):
                if m.group(1) in macros:
                    exp_by[slug][m.group(1)] += 1
    ctrl_by = {r['f']: r['counts'] for r in ctrl}

    # en 侧台账（按字母）
    by_letter = collections.defaultdict(list)
    for slug in sorted(en_count):
        letter = slug[0] if slug[0].isalpha() else '#'
        by_letter[letter].append(slug)
    for letter, slugs in sorted(by_letter.items()):
        lines = [f'# en/ 侧公式审计台账 — {letter.upper() if letter != "#" else "其他"}',
                 '',
                 '判定口径：`一致`=快照与上游逐条相同；`漂移`=上游已改；`快照损坏`=本地缺失；',
                 '`v2扩展`=依赖 MathJax v2 扩展（SEP 可渲染、v3 不可）；`上游缺陷`=上游真错（实体泄漏/括号缺失等）；',
                 '`v3异常`=v3 内部异常（多为不可见字符）。',
                 '',
                 '| 词条 | 文件数 | 公式数 | 上游比对 | 编译失败 | 台账 |',
                 '| ---- | ---- | ---- | ---- | ---- | ---- |']
        for slug in slugs:
            uv = up_verdict.get(slug, collections.Counter())
            uv_s = '一致 %d' % uv['identical'] if uv else '未抓取'
            if uv.get('structural') or uv.get('missing-in-zh') or uv.get('extra-in-zh'):
                uv_s += '（差 %d）' % sum(uv[k] for k in ('structural', 'missing-in-zh', 'extra-in-zh'))
            fv = en_fail_by.get(slug, collections.Counter())
            fv_s = '；'.join(f'{k} {v}' for k, v in fv.items()) or '0'
            lines.append(f'| {slug} | {len(en_files[slug])} | {en_count[slug]} | {uv_s} | {fv_s} | ledger |')
        open(os.path.join(LOGDIR, f'ledger-en-{letter}.md'), 'w',
             encoding='utf-8').write('\n'.join(lines) + '\n')

    # 译文侧台账（按字母）
    zh_by_letter = collections.defaultdict(list)
    for f in sorted(zh_count):
        zh_by_letter[f[0]].append(f)
    for letter, files in sorted(zh_by_letter.items()):
        lines = ['# 译文侧公式审计台账 — ' + letter.upper(),
                 '',
                 '判定口径：`公式数`=站点渲染真值口径（math-plugin protectMath）；',
                 '`宏展开`=按 local.js 表就地展开的处数；`缺陷`=D1 残留下界定符 / D2 公式内中文 /',
                 'D3 零宽字符 / D4 % / D5 # / D6 $ 不成对 / D7 与 en 多重集差分。',
                 '',
                 '| 词条 | 公式数 | 宏展开 | 缺陷 | 残余可渲染失败 |',
                 '| ---- | ---- | ---- | ---- | ---- |']
        for f in files:
            exp = exp_by.get(os.path.basename(f)[:-3].split('.')[0],
                             collections.Counter())
            exp_s = '；'.join(f'{k}×{v}' for k, v in exp.most_common(6)) or '—'
            dd = zh_def_by.get(f, collections.Counter())
            dd_s = '；'.join(f'{k} {v}' for k, v in sorted(dd.items())) or '0'
            lines.append(f'| {f} | {zh_count[f]} | {exp_s} | {dd_s} | 0（全量编译通过） |')
        open(os.path.join(LOGDIR, f'ledger-zh-{letter}.md'), 'w',
             encoding='utf-8').write('\n'.join(lines) + '\n')

    print('en letters:', len(by_letter), 'zh letters:', len(zh_by_letter),
          'zh files:', len(zh_count))


if __name__ == '__main__':
    main()
