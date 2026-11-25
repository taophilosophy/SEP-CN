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
# 核心翻译段（task_ops 状态机覆盖的 15 个节点中，存量真实走通的 7 个）：
# 不含 ex-04/rv-01/rv-02（后加环节，存量由 revert 到达而非 advance 通过，ADR-0068 发现 2）
CORE = {"tr-02", "tr-03", "tr-04", "rv-09", "sg-01", "sg-02", "sg-03"}


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
                    # 无状态机的登记册/数据池（如 term-pool 术语候选池、
                    # ci-hui-biao 词汇表）不是任务，不计入
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
    节点名经 naming.json 归一到 identifier（ADR-0080；历史事件不改写）。
    journal_dir 可注入供单元测试隔离。
    """
    try:
        from tools import naming_lib
    except ImportError:  # 直连脚本运行（无包路径）
        import naming_lib
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
                            done.add(naming_lib.try_identifier(ev["node"]) or ev["node"])
            except (json.JSONDecodeError, OSError):
                continue
            passed[slug] = done
            node_count.update(done)
    return passed, node_count


def load_backfill_slugs(journal_dir=JOURNAL):
    """有回补 pass 事件的词条集合（specs/052，ADR-0075）。

    回补＝判据收紧后对既存结果按现行判据重算（journal-schema 的 tighten 档），
    pass.note 以 `backfill:` 开头。单独计数，避免把"回补所得"混读为原批次已完成：
    回补不迁移状态，任务游标可能仍停在回补节点之前。
    """
    out = set()
    if not os.path.isdir(journal_dir):
        return out
    for dirpath, _, filenames in os.walk(journal_dir):
        for fn in filenames:
            if not fn.endswith(".ndjson"):
                continue
            path = os.path.join(dirpath, fn)
            try:
                with open(path, encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        ev = json.loads(line)
                        if ev.get("type") == "pass" and str(ev.get("note") or "").startswith("backfill:"):
                            out.add(fn[:-7])
                            break
            except (json.JSONDecodeError, OSError):
                continue
    return out


def count_skeletons(journal_slugs=None, summary_paths=None, root=ROOT):
    """按 SUMMARY 正式词条面统计「内容状态 × 是否有 journal」二维账。

    返回 dict：
      formal              SUMMARY 正式词条（重译对象）数
      skeleton            仅标题骨架（H1 之外汉字 <50）件数
      body                有正文件数
      skeleton_offledger  骨架且无 journal（账外）
      skeleton_onledger   骨架但有 journal（已建任务、尚未开工为主）

    为何需要（2026-11-18 补）：进度读数五项的分母是 journal 词条（有任务者），
    而 SUMMARY 声明的重译对象是全库正式词条，两者不等。差额是 `rules/01` 允许的
    "未翻译条目为仅含 H1 的骨架"（不建任务、无 journal）。不显式列出，读者会把
    完成度误读为占全库的比例；只列"账外"不列"账内骨架"，又会漏掉同一现象的另一面
    （骨架页同样已上站、同样对读者不可读）。

    口径：SUMMARY 中带链接、标题非别名（— see / ——见）、非占位母行（* 前缀）者，
    与 load_summary 计入 formal 的是同一集合。root 与 journal_slugs 可注入供单测。
    """
    if summary_paths is None:
        summary_paths = []
        with open(os.path.join(root, 'SUMMARY.md'), encoding='utf-8') as f:
            for line in f:
                m = re.match(r'^\s*\* \[(.*)\]\(([^)]*)\)\s*$', line.rstrip('\n'))
                if not m:
                    continue
                title, path = unescape(m.group(1)), m.group(2)
                top = path.split('/')[0]
                if top not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                    continue
                if '— see' in title or '——见' in title or title.lstrip().startswith('*'):
                    continue
                summary_paths.append(path)
    if journal_slugs is None:
        journal_slugs = set()
        jdir = os.path.join(root, 'journal')
        for dirpath, _, filenames in os.walk(jdir):
            for fn in filenames:
                if fn.endswith('.ndjson'):
                    journal_slugs.add(fn[:-7])
    skel = body = skel_off = skel_on = 0
    for path in summary_paths:
        fp = os.path.join(root, path.replace('/', os.sep))
        try:
            with open(fp, encoding='utf-8') as fh:
                text = fh.read()
        except OSError:
            continue
        text = re.sub(r'(?s)<!--.*?-->', '', text)
        rest = re.sub(r'^#\s+.*$', '', text, count=1, flags=re.M)
        is_skel = len(re.findall(r'[\u4e00-\u9fff]', rest)) < 50
        slug = os.path.basename(path)[:-3]
        if is_skel:
            skel += 1
            if slug in journal_slugs:
                skel_on += 1
            else:
                skel_off += 1
        else:
            body += 1
    return {"formal": len(summary_paths), "skeleton": skel, "body": body,
            "skeleton_offledger": skel_off, "skeleton_onledger": skel_on}


def main():
    per_letter, total_alias = load_summary()
    baseline = load_baseline()
    tasks = load_tasks()
    nodes, mand = load_pipeline()
    passed, node_count = load_journal()
    backfilled = load_backfill_slugs()

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
    mand_backfill = sum(1 for s, d in passed.items() if mand <= d and s in backfilled)
    saturate = sum(1 for d in passed.values() if (nodes | mand) <= d)
    blocked = [t for t in tasks if t.get('blockers')]
    total_formal = sum(v[0] for v in per_letter.values())
    full = nodes | mand
    skel_stat = count_skeletons(journal_slugs=set(passed))
    # 账实一致性（specs/051）：清账不变量与过程记录不变量的违例数。只读引用
    # check_taskfile_invariant.check，不重复实现判据；异常时降级为 None，
    # 不让进度生成本身因判官故障而失败。
    try:
        if ROOT not in sys.path:
            sys.path.insert(0, ROOT)
        from tools.check_taskfile_invariant import check as _chk_invariant
        inv = _chk_invariant(ROOT)
        inv_by = Counter(x["rule"] for x in inv)
    except Exception:            # noqa: BLE001 —— 视图层不承担判据失败
        inv, inv_by = None, None
    untracked = total_formal - len(passed)   # 全库正式词条中无 journal 记录者

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
        '|**账外词条（无 journal，未建任务）**|**%d**|' % untracked,
        '|全库仅标题骨架（H1 之外无正文）|%d|' % skel_stat['skeleton'],
        '|其中：骨架且在账内（有任务未开工）|%d|' % skel_stat['skeleton_onledger'],
        '|其中：骨架且在账外（无任务）|%d|' % skel_stat['skeleton_offledger'],
        '|全库有正文（已译出内容）|%d|' % skel_stat['body'],
        '|**账实不符（cleared 有正文／有正文零过程记录）**|**%s**|'
        % (len(inv) if inv is not None else '判据未跑'),
        '|核心段完成（tr-02..sg-03 七节点）|%d|' % len(core_done),
        '|强制集完成（ex-04/rv-01/rv-02/rv-03–08/sg-01–03）|%d|' % mand_ok,
        '|其中：依赖回补重算（specs/052）|%d|' % mand_backfill,
        '|完整饱和（16 节点全过）|%d|' % saturate,
        '|在途（已开工未走完核心段）|%d|' % len(wip_slugs),
        '|未开工（journal 内无 pass 事件）|%d|' % not_started,
        '|阻塞（调度侧，journal 未迁移）|%d|' % len(blocked),
        '',
        '> **分母口径**：完成／强制集／饱和／在途／未开工五项的分母是 **journal 词条 %d 件**，'
        '不是全库正式词条 %d 件。差额 %d 件无 journal 记录（全部为仅标题骨架，'
        '`rules/01` 约定未翻译条目为仅含 H1 的骨架）；骨架合计 %d 件（账内 %d ＋ 账外 %d），'
        '这些页已随 SUMMARY 上站但对读者为空。要把账外件计入进度，须先建任务'
        '（`task_ops.py create`）。'
        % (len(passed), total_formal, untracked, skel_stat['skeleton'],
           skel_stat['skeleton_onledger'], skel_stat['skeleton_offledger']),
        '',
        '> **强制集口径**：强制集完成 %d 件中，%d 件的 s0/s2.4/global 是 2026-11-19 按现行判据'
        '重算所得（`specs/052` 回补批次，journal 事件 note 以 `backfill:` 标记，状态不迁移）。'
        '回补证明"内容过现行判据"，不证明"该件已完成 s2.5 人审"——读强制集完成数时须连同'
        '此行一起读。' % (mand_ok, mand_backfill),
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
