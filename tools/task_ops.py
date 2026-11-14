# -*- coding: utf-8 -*-
"""文档任务状态机（FR-011/012/013；状态图见 specs/001-sep-sync-pipeline/data-model.md）。

用法: python tools/task_ops.py <命令> <slug> [参数]
命令: show / create / advance / clear / reopen / block
状态机（retranslate）:
  pending → cleared → drafted → s1_checked → s2_checked → audited(审计已译)
          → s3_checked → r1_reviewed → r2_reviewed → r3_reviewed → done
状态机（update）: pending → s1_checked(仅变更段) → s2_checked(变更段所在节)
          → audited(仅变更段) → s3_checked(全文档) → r1(仅变更段) → r2(变更段所在节)
          → r3(全文档) → done
禁止跳步；blocked 标志独立于状态，解除用 advance --unblock。
退出码: 0 成功；1 任务不存在；2 用法错误；3 前置条件不满足。
"""
import argparse
import json
import os as _os
import subprocess
import sys

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import load_json, repo_path, utcnow_iso, write_json_verified

STEPS = {"draft": "drafted", "s1": "s1_checked", "s2": "s2_checked",
         "audit": "audited", "s3": "s3_checked", "r1": "r1_reviewed",
         "r2": "r2_reviewed", "r3": "r3_reviewed", "done": "done"}
ORDER = {
    "retranslate": ["pending", "cleared", "drafted", "s1_checked", "s2_checked",
                    "audited", "s3_checked", "r1_reviewed", "r2_reviewed",
                    "r3_reviewed", "done"],
    "update": ["pending", "s1_checked", "s2_checked", "audited", "s3_checked",
               "r1_reviewed", "r2_reviewed", "r3_reviewed", "done"],
}
STEP_EXPECT_PREV = {
    "draft": "cleared", "s1": ("drafted", "pending"), "s2": "s1_checked",
    "audit": "s2_checked", "s3": "audited", "r1": "s3_checked", "r2": "r1_reviewed",
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
    # 版本钉对两种 kind 一并取：update 的变更同样源于登记过的英文源，
    # check_academic 对词条绑定任务查 pin、缺失即硬错误（2026-11-04 修潜在陷阱）
    task["version_pin"] = _version_pin(slug)
    if kind == "retranslate":
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
    if not str(actor or "").strip():
        raise UsageError("actor 必填（写入路径追责字段）")
    if not str(evidence or "").strip():
        raise UsageError("evidence 必填（FR-017：哈希/diff/对照记录/检查输出）")
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
    expect = STEP_EXPECT_PREV[step]
    if isinstance(expect, tuple):
        if cur not in expect:
            raise PreconditionError("step %s 要求状态 %s，当前 %s" % (step, expect, cur))
    elif cur != expect:
        raise PreconditionError("step %s 要求状态 %s，当前 %s（禁止跳步）" % (step, expect, cur))
    if cur not in order:
        raise PreconditionError("非法状态 %s" % cur)
    if step != "done" and task["kind"] == "update" and step in ("s1", "s2", "audit") \
            and not evidence.startswith("changes:"):
        raise PreconditionError("update 任务的 %s 证据必须引用变更清单（evidence 以 changes: 开头）" % step)
    if step == "r3" and task.get("kind") != "glossary-maintenance":
        _independence_gate(task, actor, evidence)  # 复核独立性机检（rules/04）
    if step in ("s3", "r3") and task.get("kind") != "glossary-maintenance":
        _academic_gate(task.get("zh_doc"), step)  # 审校挂钩（rules/07）
    if step == "audit" and task.get("kind") != "glossary-maintenance":
        _audit_gate(task.get("zh_doc"))  # 审计挂钩（rules/04、ADR-0040）
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


def _audit_gate(zh_doc):
    """audited 校次门禁挂钩：check_math_zh 默认档 0 硬错误——公式完整性硬伤
    （裸 $、宏残留、中文入公式等 C1–C6/C8）在审计即拦，strict 升档留 s3/r3
    （rules/04 审计已译环节、ADR-0040）。词汇表维护任务与无 zh_doc 条目不设门。"""
    if not zh_doc:
        return
    tools_dir = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                              "tools")
    r = subprocess.run([sys.executable, _os.path.join(tools_dir, "check_math_zh.py"), zh_doc],
                       capture_output=True, text=True)
    if r.returncode == 1:
        raise PreconditionError("公式体例门禁未通过（audited 校次）：%s"
                                % r.stdout.strip()[-800:])


def _academic_gate(zh_doc, step):
    """s3/r3 校次门禁挂钩：check_academic --strict 0 硬错误（rules/07、specs/003）
    ＋ check_math_zh --strict 0 硬错误（021 九类公式体例，D26 接线）。

    词汇表维护任务（glossary-maintenance）与无 zh_doc 的 intake 条目不设门。
    """
    if not zh_doc:
        return
    tools_dir = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                              "tools")
    for script, args, label in (
            ("check_academic.py", ["--docs", zh_doc, "--strict"], "学术规范"),
            ("check_math_zh.py", [zh_doc, "--strict"], "公式体例"),
    ):
        r = subprocess.run([sys.executable, _os.path.join(tools_dir, script)] + args,
                           capture_output=True, text=True)
        if r.returncode == 1:
            raise PreconditionError("%s门禁未通过（%s 校次）：%s"
                                    % (label, step, r.stdout.strip()[-800:]))


def _independence_gate(task, actor, evidence):
    """复核独立性机检（rules/04"复核独立性"、ADR-0020 裁定②混合制）。

    r1–r3 的 actor 全部同于初译 actor（retranslate 取 draft、update 取 s1）时，
    属单会话形态，须在 r3 evidence 记明"冷置"（先做其他任务再回读）；
    正常形态由评审线交叉满足（specs/005 §6 评审线接管）。
    旧任务缺首写步则跳过（不强溯）。
    """
    first = "draft" if task.get("kind") == "retranslate" else "s1"
    writer = next((s.get("actor") or "" for s in task.get("steps", [])
                   if s.get("step") == first), None)
    if not writer:
        return
    actors = [s.get("actor") or "" for s in task.get("steps", [])
              if s.get("step") in ("r1", "r2")]
    actors.append(actor or "")
    if all(a == writer for a in actors) and "冷置" not in (evidence or ""):
        raise PreconditionError(
            "复核独立性未满足：r1–r3 与初译 actor（%s）全部相同，单会话形态须在 r3 "
            "evidence 记明冷置（rules/04 复核独立性；或交评审线交叉 r1–r3，specs/005 §6）"
            % writer)


def reopen(slug, reason, actor):
    """把 done 的 retranslate 任务打回 pending（返工入口，ADR-0033 置空处置）。

    只用于已 done 词条被发现语体等硬问题时：reopen → clear → 重新 draft。
    旧 steps 保留为历史（append-only），不删除；reason 必须写明返工原因。
    """
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    if task["kind"] != "retranslate":
        raise UsageError("reopen 仅适用于 retranslate 任务")
    if task["state"] != "done":
        raise PreconditionError("reopen 要求状态 done，当前 %s" % task["state"])
    if not str(reason or "").strip():
        raise UsageError("reopen 必须写明返工原因（--reason）")
    task["state"] = "pending"
    task["steps"].append({"step": "reopen", "status": "ok", "actor": actor,
                          "at": utcnow_iso(), "evidence": reason})
    save_task(task)
    return task


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
        if cmd == "reopen":
            args = _parse(["--actor", "--reason"], argv[2:])
            print(json.dumps(reopen(slug, args.get("reason") or "",
                                    args.get("actor") or "?"),
                             ensure_ascii=False, indent=2))
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
