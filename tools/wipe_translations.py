#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全库置空：既有中文译文只留 H1，任务游标归零（用户 2026-11-25 裁定）。

执行口径（rules/04、ADR-0050/0068）：
  * 正文：SUMMARY 列出的正式词条 `<letter>/<slug>.md` 一律截为 H1 一行；
    无 H1 的文件不动并报告（不代造标题）。
  * 状态：`kind=retranslate` 任务按状态机走正规原语——
      pending           → `clear`
      cleared（有正文） → 直接截 H1（I1 账实修正），状态不变
      done              → `reopen` → `clear`
      其它在途          → `reopen --upstream-sync` → `clear`
    有 blockers 先 `advance --unblock`（留 evidence）。
    `clear` 的基线 gate 未过时，按用户裁定强制置空：截 H1＋状态置 cleared＋steps 记
    `clear` 并写明 gate 未过（不静默）。逐条入报告。
  * 事实层（journal 的 4276 个事件、`tasks.steps` 历史）不删不改；归零的是游标与
    正文，PROGRESS 等视图由 journal 重算。

用法:
  python tools/wipe_translations.py                # 干跑：统计目标与阻断
  python tools/wipe_translations.py --apply        # 执行
  python tools/wipe_translations.py --limit 3 --apply   # 小样本试金石
退出码: 0 完成；1 有不可置空项（无 H1 等），见报告。
"""
import argparse
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools import task_ops  # noqa: E402
from tools.common import read_text, write_text  # noqa: E402

ACTOR = "wipe-2026-11-25"
REASON = ("全库置空重译（用户 2026-11-25 裁定）：既有中文译文全部置空仅留 H1、"
          "全部进度归零；逐字依据见本会话指令与 qian-yan 日志同日条目")
REPORT = os.path.join(ROOT, "specs", "060-six-axis-quality-gates", "results", "wipe-2026-11-25.json")

ENTRY_RE = re.compile(r"\]\((?:\./)?([a-z0-9]+/[a-z0-9-]+)\.md\)")


def summary_docs():
    """SUMMARY 中的正式词条 md 相对路径（去重、保序）。"""
    s = read_text(os.path.join(ROOT, "SUMMARY.md"))
    out = []
    for m in ENTRY_RE.finditer(s):
        p = m.group(1) + ".md"
        if p not in out:
            out.append(p)
    return out


def iter_tasks():
    tdir = os.path.join(ROOT, "tasks")
    for dirpath, _, files in os.walk(tdir):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
                    t = json.load(f)
            except (OSError, ValueError):
                continue
            if isinstance(t, dict) and t.get("slug") \
                    and str(t.get("kind") or "") == "retranslate":
                yield t["slug"]


def truncate_h1(rel):
    """截为 H1 一行。返回 (status, detail)。"""
    full = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
    if not os.path.exists(full):
        return "missing", rel
    text = read_text(full)
    first = text.split("\n", 1)[0]
    if not first.startswith("# "):
        return "no-h1", rel
    if text != first.rstrip() + "\n":
        write_text(full, first.rstrip() + "\n")
        return "wiped", rel
    return "already", rel


def reset_task(slug, dry=False):
    """把一条任务归零：unblock → reopen（按需）→ clear。返回状态串。"""
    t = task_ops.load_task(slug)
    if not t:
        return "no-task"
    if t.get("blockers"):
        if not dry:
            task_ops.advance(slug, None, actor=ACTOR, evidence=REASON, unblock=True)
        note = "unblocked"
    else:
        note = ""
    state = t.get("state")
    if state == "pending":
        pass
    elif state == "cleared":
        return "already-cleared" + ("+" + note if note else "")
    elif state == "done":
        if not dry:
            task_ops.reopen(slug, REASON, ACTOR)
    else:
        if not dry:
            task_ops.reopen(slug, REASON, ACTOR, upstream_sync=True)
    if dry:
        return "would-clear" + ("+" + note if note else "")
    try:
        task_ops.clear(slug)
        return "cleared" + ("+" + note if note else "")
    except task_ops.PreconditionError as exc:
        # 用户裁定：不计成本全部置空。gate 未过也置空，但逐条留痕（不静默）。
        t = task_ops.load_task(slug)
        zh = t.get("zh_doc")
        st = truncate_h1(zh)[0] if zh else "missing"
        t["state"] = "cleared"
        t["steps"].append({"step": "clear", "status": "ok", "actor": ACTOR,
                           "at": task_ops.utcnow_iso(),
                           "evidence": "全库置空（强制）：clear gate 未过——%s；%s"
                                       % (str(exc)[:300], REASON)})
        task_ops.save_task(t)
        return "forced-clear（gate 未过，%s）%s" % (st, "+" + note if note else "")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args(argv)

    docs = summary_docs()
    slugs = sorted(iter_tasks())
    if args.limit:
        docs, slugs = docs[:args.limit], slugs[:args.limit]

    doc_stats, task_stats = {}, {}
    detail = []
    for rel in docs:
        st, d = ("would-wipe", rel) if not args.apply else truncate_h1(rel)
        doc_stats[st] = doc_stats.get(st, 0) + 1
        if st not in ("wiped", "would-wipe", "already"):
            detail.append({"doc": d, "status": st})

    for slug in slugs:
        st = reset_task(slug, dry=not args.apply)
        key = st.split("（")[0].split("+")[0]
        task_stats[key] = task_stats.get(key, 0) + 1
        if key in ("no-task", "forced-clear") or st.startswith("forced"):
            detail.append({"slug": slug, "status": st})

    print("正文：%d 件｜%s" % (len(docs), json.dumps(doc_stats, ensure_ascii=False)))
    print("任务：%d 条｜%s" % (len(slugs), json.dumps(task_stats, ensure_ascii=False)))
    if detail:
        print("需关注 %d 条（前 10）：" % len(detail))
        for x in detail[:10]:
            print("  %s" % json.dumps(x, ensure_ascii=False))

    if args.apply:
        os.makedirs(os.path.dirname(REPORT), exist_ok=True)
        with open(REPORT, "w", encoding="utf-8", newline="\n") as f:
            json.dump({"schema": "wipe/v1", "actor": ACTOR, "reason": REASON,
                       "docs": doc_stats, "tasks": task_stats, "detail": detail},
                      f, ensure_ascii=False, indent=1)
        print("报告：%s" % os.path.relpath(REPORT, ROOT))
    else:
        print("干跑：未写任何文件（--apply 执行）")
    bad = any(v for k, v in doc_stats.items() if k not in ("wiped", "would-wipe", "already"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
