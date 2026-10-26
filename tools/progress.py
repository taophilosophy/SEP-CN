# -*- coding: utf-8 -*-
"""进度汇总：从 SUMMARY/baseline/tasks 生成 PROGRESS.md（自动生成，不手改）。

用法: python tools/progress.py [--out PROGRESS.md]
数据源: SUMMARY.md（条目结构与分类）、baseline/entries.json（已建基线）、
       tasks/**/*.json（文档任务状态）。输出 rollup 报告，不改任何数据。
"""
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATES = ["pending", "cleared", "drafted", "s1_checked", "s2_checked", "s3_checked",
          "r1_reviewed", "r2_reviewed", "r3_reviewed", "done"]


def unescape(t):
    out, i = [], 0
    while i < len(t):
        if t[i] == '\\' and i + 1 < len(t) and t[i + 1] in '*[]':
            out.append(t[i + 1])
            i += 2
        else:
            out.append(t[i])
            i += 1
    return ''.join(out)


def load_summary():
    formal, alias, placeholder = defaultdict(int), 0, defaultdict(int)
    total_alias = 0
    per_letter = defaultdict(lambda: [0, 0, 0])  # formal, alias, placeholder
    with open(os.path.join(ROOT, 'SUMMARY.md'), encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*\* \[(.*)\]\(([^)]*)\)\s*$', line.rstrip('\n'))
            if not m:
                continue
            title, path = unescape(m.group(1)), m.group(2)
            top = path.split('/')[0]
            if top not in 'abcdefghijklmnopqrstuvwxyz':
                continue
            if '— see' in title:
                total_alias += 1
                per_letter[top][1] += 1
            elif title.lstrip().startswith('*'):
                per_letter[top][2] += 1
            else:
                per_letter[top][0] += 1
    return per_letter, total_alias


def load_baseline():
    p = os.path.join(ROOT, 'baseline', 'entries.json')
    if not os.path.exists(p):
        return {}
    data = json.load(open(p, encoding='utf-8'))
    return {e['slug']: e for e in data.get('entries', [])}


def load_tasks():
    tasks, bad = [], 0
    tdir = os.path.join(ROOT, 'tasks')
    for dirpath, _, filenames in os.walk(tdir):
        for fn in filenames:
            if fn.endswith('.json'):
                try:
                    data = json.load(open(os.path.join(dirpath, fn), encoding='utf-8'))
                except (json.JSONDecodeError, OSError) as exc:
                    print('警告：任务文件解析失败 %s: %s' % (fn, exc))
                    bad += 1
                    continue
                if isinstance(data, dict) and data.get('slug'):
                    tasks.append(data)
                else:
                    bad += 1
    if bad:
        print('警告：%d 个任务记录缺少 slug 或解析失败，未计入统计' % bad)
    return tasks


def main():
    per_letter, total_alias = load_summary()
    baseline = load_baseline()
    tasks = load_tasks()

    states = Counter(t.get('state', '?') for t in tasks)
    done = [t for t in tasks if t.get('state') == 'done']
    wip = [t for t in tasks if t.get('state') not in ('pending', 'done')]
    blocked = [t for t in tasks if t.get('blockers')]
    total_formal = sum(v[0] for v in per_letter.values())

    lines = [
        '# 项目进度',
        '',
        '<!-- 本文件由 `python tools/progress.py` 自动生成，不手改。数据源：SUMMARY.md、baseline/entries.json、tasks/。 -->',
        '',
        '生成时间：%s（UTC）' % datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M'),
        '',
        '## 总览',
        '',
        '|指标|数值|',
        '|---|---|',
        '| SUMMARY 正式词条（重译对象）|%d|' % total_formal,
        '| 别名词条（— see，不建任务）|%d|' % total_alias,
        '| 占位母词条（* 前缀，不建任务）|%d|' % sum(v[2] for v in per_letter.values()),
        '| 已建英文基线|%d|' % len(baseline),
        '| 已建任务|%d|' % len(tasks),
        '| 已完成（done）|%d|' % len(done),
        '| 在途（drafted 起、done 前）|%d|' % len(wip),
        '| 阻塞|%d|' % len(blocked),
        '',
        '## 任务状态分布',
        '',
        '|状态|数量|',
        '|---|---|',
    ]
    for s in STATES:
        if states.get(s):
            lines.append('|%s|%d|' % (s, states[s]))
    for s, n in sorted(states.items()):
        if s not in STATES:
            lines.append('|%s（非标准状态）|%d|' % (s, n))

    lines += ['', '## 按首字母（正式词条 / 基线 / 任务 / 完成）', '',
              '|字母|正式词条|已建基线|已建任务|done|', '|---|---|---|---|---|']
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        formal = per_letter.get(ch, [0, 0, 0])[0]
        if not formal:
            continue
        base_n = sum(1 for s in baseline if s.startswith(ch))
        task_n = sum(1 for t in tasks if t.get('slug', '').startswith(ch))
        done_n = sum(1 for t in done if t.get('slug', '').startswith(ch))
        lines.append('|%s|%d|%d|%d|%d|' % (ch.upper(), formal, base_n, task_n, done_n))

    if wip:
        lines += ['', '## 在途任务', '', '|slug|类型|状态|最后执行|', '|---|---|---|---|']
        for t in sorted(wip, key=lambda x: x.get('slug', '')):
            last = t['steps'][-1] if t.get('steps') else {}
            lines.append('|%s|%s|%s|%s %s|' % (t.get('slug'), t.get('kind'),
                                               t.get('state'), last.get('actor', ''),
                                               last.get('at', '')[:10]))
    if blocked:
        lines += ['', '## 阻塞任务', '', '|slug|阻塞原因|', '|---|---|']
        for t in blocked:
            lines.append('|%s|%s|' % (t.get('slug'), '；'.join(t.get('blockers'))))

    lines.append('')
    out = os.path.join(ROOT, sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv \
        else os.path.join(ROOT, 'PROGRESS.md')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print('生成 %s（正式词条 %d，done %d，在途 %d，阻塞 %d）'
          % (os.path.relpath(out, ROOT), total_formal, len(done), len(wip), len(blocked)))


if __name__ == '__main__':
    main()
