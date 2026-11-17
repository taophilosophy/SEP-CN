# -*- coding: utf-8 -*-
"""进度汇总：从 SUMMARY/baseline/journal/tasks 生成 PROGRESS.md（自动生成，不手改）。

用法: python tools/progress.py [--out PROGRESS.md]
数据源（ADR-0068 W4 切读面后）:
  SUMMARY.md（条目结构与分类，清单）＋ baseline/entries.json（已建基线，清单）
  journal/<letter>/<slug>.ndjson（进度事实：pass 事件集合，唯一进度读面）
  tasks/**/*.json（仅调度侧：例行任务判定、blockers——journal 未迁移，见 ADR-0068）
输出 rollup 报告，不改任何数据。
"""
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNAL = os.path.join(ROOT, "journal")
PIPE = os.path.join(ROOT, "rules", "pipeline.json")
# 核心翻译段（task_ops 状态机覆盖的 10 节点中，存量真实走通的 7 个）：
# 不含 s0/s2.4/global（后加环节，存量由 revert 到达而非 advance 通过，ADR-0068 发现 2）
CORE = {"draft", "s1", "s2", "S3", "R1", "R2", "R3"}


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
    """解析 SUMMARY.md 分类统计。

    ADR-0057/0060（2026-11-16）：集群占位母行与别名词条行都改为**无链接行**
    （GitBook 一文件一页），故它们不再有路径：按所在 `## X` 字母分节归位，
    别名按「— see / ——见」判定，其余无链接行计为占位母行。
    """
    total_alias = 0
    per_letter = defaultdict(lambda: [0, 0, 0])  # formal, alias, placeholder（按字母分节，ADR-0009）
    section = None
    with open(os.path.join(ROOT, 'SUMMARY.md'), encoding='utf-8') as f:
        for line in f:
            s = line.rstrip('\n')
            h = re.match(r'^##\s+([A-Za-z0-9])\s*$', s)
            if h:
                section = h.group(1).lower()
                continue
            m = re.match(r'^\s*\* \[(.*)\]\(([^)]*)\)\s*$', s)
            if m:
                title, path = unescape(m.group(1)), m.group(2)
                top = path.split('/')[0]
                if top not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                    continue
                if '— see' in title or '——见' in title:
                    total_alias += 1
                    per_letter[top][1] += 1
                elif title.lstrip().startswith('*'):
                    per_letter[top][2] += 1
                else:
                    per_letter[top][0] += 1
                continue
            n = re.match(r'^\s*\* (.*)$', s)
            if n and section is not None:
                title = unescape(n.group(1))
                if '— see' in title or '——见' in title:
                    total_alias += 1
                    per_letter[section][1] += 1
                else:
                    per_letter[section][2] += 1
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
        if os.path.basename(dirpath) == 'manifests':
            # 战役清单目录（008 术语战役 manifest 等批量 JSON）不是逐词条任务记录，不扫
            continue
        for fn in filenames:
            if fn.endswith('.json'):
                try:
                    data = json.load(open(os.path.join(dirpath, fn), encoding='utf-8'))
                except (json.JSONDecodeError, OSError) as exc:
                    print('警告：任务文件解析失败 %s: %s' % (fn, exc))
                    bad += 1
                    continue
                if isinstance(data, dict) and data.get('state') is None \
                        and not data.get('steps'):
                    # 无状态机的登记册/数据池（如 term-candidates 术语候选册、
                    # term-pool 术语候选池）不是任务，不计入
                    continue
                if isinstance(data, dict) and data.get('slug'):
                    tasks.append(data)
                else:
                    bad += 1
    if bad:
        print('警告：%d 个任务记录缺少 slug 或解析失败，未计入统计' % bad)
    return tasks


def load_pipeline():
    """读 rules/pipeline.json（判据唯一事实源），返回 (节点集, 强制集)。"""
    with open(PIPE, "rb") as f:
        d = json.loads(f.read().decode("utf-8"))
    nodes = {n["id"] for n in d.get("nodes", [])}
    mand = set(d.get("mandatory_minimum", {}).get("nodes", []))
    return nodes, mand


def load_journal(journal_dir=JOURNAL):
    """读 journal/<letter>/<slug>.ndjson，折叠 pass 集合（只增不减，P5）。

    返回 (passed: dict[slug -> set(node)], node_count: Counter)。
    不读 tasks 的 state——进度事实只认 journal（ADR-0068 W4）。
    journal_dir 可注入供单元测试隔离。
    """
    passed, node_count = {}, Counter()
    if not os.path.isdir(journal_dir):
        return passed, node_count
    for dirpath, _, filenames in os.walk(journal_dir):
        for fn in filenames:
            if not fn.endswith(".ndjson"):
                continue
            slug = fn[:-7]
            done = set()
            path = os.path.join(dirpath, fn)
            try:
                with open(path, encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        ev = json.loads(line)
                        if ev.get("type") == "pass" and ev.get("node"):
                            done.add(ev["node"])
            except (json.JSONDecodeError, OSError):
                continue
            passed[slug] = done
            node_count.update(done)
    return passed, node_count


def main():
    per_letter, total_alias = load_summary()
    baseline = load_baseline()
    tasks = load_tasks()
    nodes, mand = load_pipeline()
    passed, node_count = load_journal()

    # 例行/维护任务（非词条绑定：zh_doc 为空、glossary-maintenance 等）不跟词条
    # 状态机，单独计数，不计入在途/阻塞（2026-11-04，D9；与 check_academic 豁免同族）
    entry_tasks, routine = [], []
    for t in tasks:
        if (not str(t.get('zh_doc') or '').strip()
                or str(t.get('kind') or '') == 'glossary-maintenance'):
            routine.append(t)
        else:
            entry_tasks.append(t)
    tasks = entry_tasks

    # 进度读数（journal 口径，ADR-0068 W4）：完成 = CORE ⊆ passed；
    # 在途 = 有 pass 但未走完 CORE；未开工 = 无 pass。
    core_done = sorted(s for s, d in passed.items() if CORE <= d)
    wip_slugs = sorted(s for s, d in passed.items() if d and not (CORE <= d))
    not_started = sum(1 for d in passed.values() if not d)
    mand_ok = sum(1 for d in passed.values() if mand <= d)
    saturate = sum(1 for d in passed.values() if (nodes | mand) <= d)
    blocked = [t for t in tasks if t.get('blockers')]
    total_formal = sum(v[0] for v in per_letter.values())
    full = nodes | mand

    lines = [
        '# 项目进度',
        '',
        '<!-- 本文件由 `python tools/progress.py` 自动生成，不手改。数据源：SUMMARY.md（结构）、baseline/entries.json（基线）、journal/（进度事实）、tasks/（仅调度侧阻塞）。 -->',
        '',
        '生成时间：%s（UTC）' % datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M'),
        '',
        '## 总览',
        '',
        '|指标|数值|',
        '|---|---|',
        '|SUMMARY 正式词条（重译对象）|%d|' % total_formal,
        '|别名词条（— see，不建任务）|%d|' % total_alias,
        '|占位母词条（* 前缀，不建任务）|%d|' % sum(v[2] for v in per_letter.values()),
        '|已建英文基线|%d|' % len(baseline),
        '|已建任务（journal 词条）|%d|' % len(passed),
        '|例行/维护任务（不计状态机）|%d|' % len(routine),
        '|核心段完成（draft..R3 七节点）|%d|' % len(core_done),
        '|强制集完成（s0/s2.4/global/R1/R2/R3）|%d|' % mand_ok,
        '|完整饱和（16 节点全过）|%d|' % saturate,
        '|在途（已开工未走完核心段）|%d|' % len(wip_slugs),
        '|未开工（无 pass 事件）|%d|' % not_started,
        '|阻塞（调度侧，journal 未迁移）|%d|' % len(blocked),
        '',
        '## 节点通过数（journal 口径，共 %d 节点）' % len(full),
        '',
        '|节点|通过数|',
        '|---|---|',
    ]
    for n in sorted(full):
        lines.append('|%s|%d|' % (n, node_count.get(n, 0)))

    lines += ['', '## 按首字母（正式词条 / 基线 / 任务 / 核心段完成）', '',
              '|字母|正式词条|已建基线|已建任务|核心段完成|', '|---|---|---|---|---|']
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        formal = per_letter.get(ch, [0, 0, 0])[0]
        if not formal:
            continue
        base_n = sum(1 for s in baseline if s.startswith(ch))
        task_n = sum(1 for s in passed if s.startswith(ch))
        done_n = sum(1 for s in core_done if s.startswith(ch))
        lines.append('|%s|%d|%d|%d|%d|' % (ch.upper(), formal, base_n, task_n, done_n))

    if wip_slugs:
        lines += ['', '## 在途词条（已开工未走完核心段）', '',
                  '|slug|已过节点数|已过节点|', '|---|---|---|']
        for s in wip_slugs:
            d = passed[s]
            lines.append('|%s|%d|%s|' % (s, len(d), ' '.join(sorted(d))))

    if blocked:
        lines += ['', '## 阻塞任务（调度侧，journal 未迁移 blockers）', '',
                  '|slug|阻塞原因|', '|---|---|']
        for t in blocked:
            lines.append('|%s|%s|' % (t.get('slug'), '；'.join(t.get('blockers'))))

    lines.append('')
    out = os.path.join(ROOT, sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv \
        else os.path.join(ROOT, 'PROGRESS.md')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print('生成 %s（正式词条 %d，核心段完成 %d，在途 %d，强制集完成 %d，完整饱和 %d，阻塞 %d）'
          % (os.path.relpath(out, ROOT), total_formal, len(core_done), len(wip_slugs),
             mand_ok, saturate, len(blocked)))


if __name__ == '__main__':
    main()
