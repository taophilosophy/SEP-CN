# -*- coding: utf-8 -*-
"""阶段 1.2 辅助：钉账元数据变化（上游修订信号，specs/062 SOP §1.2）。

比较 `results/entries-before.json` 与 `baseline/entries.json`：
  title／authors／pubinfo（first_published、substantive_revision）／archive_edition。

判读：
  substantive_revision 变 → 上游正式发布新修订（建账最硬信号）；
  archive_edition 变      → 新存档版落库（与修订同源，通常同步出现）；
  title／authors 变       → 条目改名或作者变更，优先按目录线处置（specs/054）。

输出：results/entry-meta-delta.md。
用法：python specs/062-phase12-recheck/bin/entry_meta_delta.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RES = os.path.join(ROOT, 'specs', '062-phase12-recheck', 'results')
FIELDS = ('title', 'authors', 'pubinfo', 'archive_edition')


def load(path):
    d = json.load(open(path, encoding='utf-8'))
    return {e['slug']: e for e in d['entries']}


def main():
    before = load(os.path.join(RES, 'entries-before.json'))
    after = load(os.path.join(ROOT, 'baseline', 'entries.json'))
    rows = []
    for slug in sorted(set(before) & set(after)):
        a, b = before[slug], after[slug]
        diff = [f for f in FIELDS if a.get(f) != b.get(f)]
        if diff:
            rows.append({'slug': slug, 'fields': diff,
                         'before': {f: a.get(f) for f in diff},
                         'after': {f: b.get(f) for f in diff}})
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    revs = [r for r in rows
            if 'pubinfo' in r['fields']
            and (r['before'].get('pubinfo') or {}).get('substantive_revision')
            != (r['after'].get('pubinfo') or {}).get('substantive_revision')]
    L = ['# 钉账元数据变化（上游修订信号）', '',
         '词条 %d；元数据变化 %d（其中 substantive_revision 变更 %d）；新增 %d；移除 %d'
         % (len(after), len(rows), len(revs), len(added), len(removed)), '']
    if revs:
        L += ['## substantive_revision 变更（建账硬信号）', '',
              '| 词条 | 旧 | 新 |', '| --- | --- | --- |']
        for r in revs:
            L.append('| %s | %s | %s |'
                     % (r['slug'],
                        (r['before'].get('pubinfo') or {}).get('substantive_revision'),
                        (r['after'].get('pubinfo') or {}).get('substantive_revision')))
        L.append('')
    L += ['## 全部元数据变化', '', '| 词条 | 字段 | 旧 | 新 |', '| --- | --- | --- | --- |']
    for r in rows:
        L.append('| %s | %s | %s | %s |'
                 % (r['slug'], ','.join(r['fields']),
                    json.dumps(r['before'], ensure_ascii=False)[:90],
                    json.dumps(r['after'], ensure_ascii=False)[:90]))
    if added:
        L += ['', '新增：' + '、'.join('`%s`' % s for s in added)]
    if removed:
        L += ['', '移除：' + '、'.join('`%s`' % s for s in removed)]
    with open(os.path.join(RES, 'entry-meta-delta.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L) + '\n')
    print(json.dumps({'meta_changed': len(rows), 'substantive_revision': len(revs),
                      'added': len(added), 'removed': len(removed)}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
