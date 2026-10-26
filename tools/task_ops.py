# -*- coding: utf-8 -*-
"""文档任务状态机（FR-011/012/013；状态图见 specs/001-sep-sync-pipeline/data-model.md）。

用法: python tools/task_ops.py <命令> <slug> [参数]
命令: show / create / advance / clear / block
状态机（retranslate）:
  pending → cleared → drafted → s1_checked → s2_checked → s3_checked
          → r1_reviewed → r2_reviewed → r3_reviewed → done
状态机（update）: pending → s1_checked(仅变更段) → s2_checked(变更段所在节)
          → s3_checked(全文档) → r1 → r2 → r3 → done
禁止跳步；blocked 标志独立于状态，解除用 advance --unblock。
退出码: 0 成功；1 任务不存在；2 用法错误；3 前置条件不满足。
"""
import argparse
import json
import os as _os
import sys

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import load_json, repo_path, utcnow_iso, write_json_verified

STEPS = {"draft": "drafted", "s1": "s1_checked", "s2": "s2_checked",
         "s3": "s3_checked", "r1": "r1_reviewed", "r2": "r2_reviewed",
         "r3": "r3_reviewed", "done": "done"}
ORDER = {
    "retranslate": ["pending", "cleared", "drafted", "s1_checked", "s2_checked",
                    "s3_checked", "r1_reviewed", "r2_reviewed", "r3_reviewed", "done"],
    "update": ["pending", "s1_checked", "s2_checked", "s3_checked",
               "r1_reviewed", "r2_reviewed", "r3_reviewed", "done"],
}
STEP_EXPECT_PREV = {
    "draft": "cleared", "s1": ("drafted", "pending"), "s2": "s1_checked",
    "s3": "s2_checked", "r1": "s3_checked", "r2": "r1_reviewed",
    "r3": "r2_reviewed", "done": "r3_reviewed",
}

TASKS_DIR = None  # 可注入（测试用）；默认 <repo>/tasks


def _dir():
    return TASKS_DIR or repo_path("tasks")


def _os_path(slug):
    return _os.path.join(_dir(), slug[0], slug + ".json")


def load_task(slug):
    p = _os_path(slug)
    if not _os.path.exists(p):
        return None
    return load_json(p)


def save_task(task):
    write_json_verified(_os_path(task["slug"]), task)


def _baseline_title(slug):
    base = repo_path("baseline", "entries.json")
    if not _os.path.exists(base):
        return None
    for e in load_json(base)["entries"]:
        if e["slug"] == slug:
            return e.get("title")
    return None


def _version_pin(slug):
    """版本钉从基线取（零信任：翻译依据必须是登记过的英文源）。"""
    base = repo_path("baseline", "entries.json")
    if not _os.path.exists(base):
        raise PreconditionError("baseline/entries.json 不存在，先建立基线")
    recs = [e for e in load_json(base)["entries"] if e["slug"] == slug]
    if not recs:
        raise PreconditionError("词条 %s 不在基线中（先 fetch_entry）" % slug)
    rec = recs[0]
    return {
        "pubinfo_date": rec.get("pubinfo", {}).get("substantive_revision")
        or rec.get("pubinfo", {}).get("first_published"),
        "archive_edition": rec.get("archive_edition"),
        "sha256": next((f["sha256"] for f in rec.get("files", [])
                        if f["kind"] == "main"), None)}


def create(slug, kind, zh_doc=None, change_file=None):
    if kind not in ORDER:
        raise UsageError("kind 必须是 retranslate|update")
    if load_task(slug):
        raise PreconditionError("任务已存在: %s" % slug)
    task = {"slug": slug, "kind": kind, "zh_doc": zh_doc, "state": "pending",
            "steps": [], "blockers": [], "created_at": utcnow_iso()}
    if kind == "retranslate":
        task["version_pin"] = _version_pin(slug)
        if task["zh_doc"] is None:
            task["zh_doc"] = find_zh_doc({"slug": slug, "title": _baseline_title(slug)})
    else:
        if not change_file or not _os.path.exists(change_file):
            raise PreconditionError("update 任务必须给 --from <baseline/changes/…json>")
        task["change_file"] = _os.path.abspath(change_file)
    save_task(task)
    return task


def find_zh_doc(rec):
    from tools.common import find_zh_doc as _f
    return _f(rec["slug"], rec.get("title") or rec.get("title_en"))


def advance(slug, step, actor, evidence, unblock=False):
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    if unblock:
        task["blockers"] = []
        task["steps"].append({"step": "unblock", "status": "ok", "actor": actor,
                              "at": utcnow_iso(), "evidence": evidence})
        save_task(task)
        return task
    if task.get("blockers"):
        raise PreconditionError("任务被阻塞: %s；先 advance --unblock" % task["blockers"])
    if step not in STEPS:
        raise UsageError("step 必须是 %s" % "/".join(STEPS))
    order = ORDER[task["kind"]]
    cur = task["state"]
    if step == "done":
        expect = "r3_reviewed"
    else:
        expect = STEP_EXPECT_PREV[step]
        if isinstance(expect, tuple):
            if cur not in expect:
                raise PreconditionError("step %s 要求状态 %s，当前 %s" % (step, expect, cur))
        elif cur != expect:
            raise PreconditionError("step %s 要求状态 %s，当前 %s（禁止跳步）" % (step, expect, cur))
    if cur not in order:
        raise PreconditionError("非法状态 %s" % cur)
    if step != "done" and task["kind"] == "update" and step in ("s1", "s2") \
            and not evidence.startswith("changes:"):
        raise PreconditionError("update 任务的 %s 证据必须引用变更清单（evidence 以 changes: 开头）" % step)
    task["state"] = STEPS[step]
    task["steps"].append({"step": step, "status": "ok", "actor": actor,
                          "at": utcnow_iso(), "evidence": evidence})
    save_task(task)
    return task


def _clear_gate(slug):
    from tools import baseline_audit
    ok, report = baseline_audit.gate_passes(slug)
    if not ok:
        raise PreconditionError("基线 gate 未通过: %s" % json.dumps(report, ensure_ascii=False))


def clear(slug):
    """清空正文保留 H1（FR-013）；gate：基线哈希复算通过（宪法附加约束）。"""
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    if task["kind"] != "retranslate":
        raise UsageError("clear 仅适用于 retranslate 任务")
    if task["state"] != "pending":
        raise PreconditionError("clear 要求状态 pending，当前 %s" % task["state"])
    if task.get("blockers"):
        raise PreconditionError("任务被阻塞: %s；先 advance --unblock" % task["blockers"])
    _clear_gate(slug)
    if not task.get("zh_doc"):
        raise PreconditionError("中文文档未指定")
    full = task["zh_doc"] if _os.path.isabs(task["zh_doc"]) else repo_path(task["zh_doc"])
    if not _os.path.exists(full):
        raise PreconditionError("中文文档缺失: %r" % task["zh_doc"])
    from tools.common import read_text, write_text
    text = read_text(full)
    lines = text.split("\n")
    if not lines or not lines[0].startswith("# "):
        raise PreconditionError("首行不是 H1，拒绝清空: %s" % full)
    write_text(full, lines[0].rstrip() + "\n")
    task["state"] = "cleared"
    task["steps"].append({"step": "clear", "status": "ok", "actor": "task_ops",
                          "at": utcnow_iso(), "evidence": "baseline gate: hash_ok"})
    save_task(task)
    return task


def block(slug, reason):
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    task["blockers"].append(reason)
    task["steps"].append({"step": "block", "status": "ok", "actor": "task_ops",
                          "at": utcnow_iso(), "evidence": reason})
    save_task(task)
    return task


class UsageError(Exception):
    pass


class PreconditionError(Exception):
    pass


class TaskNotFound(Exception):
    pass


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(__doc__)
        return 2
    cmd, slug = argv[0], argv[1] if len(argv) > 1 else None
    global TASKS_DIR
    try:
        if cmd == "show":
            task = load_task(slug)
            if not task:
                raise TaskNotFound(slug)
            print(json.dumps(task, ensure_ascii=False, indent=2))
            return 0
        if cmd == "create":
            args = _parse(["--kind", "--zh-doc", "--from"], argv[2:])
            task = create(slug, args.get("kind"), args.get("zh_doc"), args.get("from"))
            print(json.dumps(task, ensure_ascii=False, indent=2))
            return 0
        if cmd == "advance":
            args = _parse(["--step", "--actor", "--evidence", "--unblock"], argv[2:])
            task = advance(slug, args.get("step"), args.get("actor") or "?",
                           args.get("evidence") or "", unblock="--unblock" in argv)
            print(json.dumps(task, ensure_ascii=False, indent=2))
            return 0
        if cmd == "clear":
            print(json.dumps(clear(slug), ensure_ascii=False, indent=2))
            return 0
        if cmd == "block":
            args = _parse(["--reason"], argv[2:])
            print(json.dumps(block(slug, args.get("reason") or "unspecified"),
                             ensure_ascii=False, indent=2))
            return 0
        raise UsageError("未知命令: %s" % cmd)
    except TaskNotFound:
        print(json.dumps({"error": "task not found: %s" % slug}, ensure_ascii=False))
        return 1
    except PreconditionError as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        return 3
    except UsageError as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        return 2


def _parse(spec, args):
    out = {}
    i = 0
    positional = [s for s in spec if not s.startswith("--")]
    value_flags = [s for s in spec if s.startswith("--")]
    for p in positional:
        if i < len(args):
            out[p] = args[i]
            i += 1
    while i < len(args):
        a = args[i]
        if a in value_flags:
            if i + 1 < len(args):
                out[a.lstrip("-").replace("-", "_")] = args[i + 1]
                i += 2
                continue
        i += 1
    return out


if __name__ == "__main__":
    sys.exit(main())
