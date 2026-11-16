# -*- coding: utf-8 -*-
"""文档任务状态机（FR-011/012/013；状态图见 specs/001-sep-sync-pipeline/data-model.md）。

用法: python tools/task_ops.py <命令> <slug> [参数]
命令: show / create / advance / clear / reopen / block / revert-state / source-audit
状态机（retranslate）:
  pending → cleared → s0_source_checked(源审计前置) → drafted → s1_checked
          → s2_checked → s2.4_termchecked(术语校) → s2.5_checked(审计已译)
          → s3_checked → r1_reviewed → r2_reviewed → r3_reviewed → done
状态机（update）: pending → s0_source_checked(仅变更段) → s1_checked(仅变更段)
          → s2_checked(变更段所在节) → s2.4_termchecked(仅变更段)
          → s2.5_checked(仅变更段) → s3_checked(全文档)
          → r1(仅变更段) → r2(变更段所在节) → r3(全文档) → done
禁止跳步；blocked 标志独立于状态，解除用 advance --unblock。
r3 终审（ADR-0054，用户 2026-11-15 裁定）：仅用户显式指定的会话执行，未指定不进行
R3、条目停 r2_reviewed；advance --step r3 必须带 --mandate <用户指定记录>。
s0（ADR-0052）：advance --step s0 自动挂 en_integrity＋en_source_audit；
在途/done 存量补课用 source-audit 子命令（追加 s0 记录，状态不迁移）；
进 s3 前任务历史必须有 s0 记录。
s2.4（ADR-0043/0063）：advance --step s24 顺序挂术语轴（check_terms）与体例轴＋勘误轴
（check_pairs --gate 与 check_style，结构硬、空白告警）。
revert-state：受控回退原语，--to {s2.5_checked, s2.4_termchecked}，适用于 s2.5_checked
及其后状态（ADR-0043 全量回退、ADR-0063 扩 s2.4；steps append-only 留史）。
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

STEPS = {"s0": "s0_source_checked", "draft": "drafted", "s1": "s1_checked",
         "s2": "s2_checked",
         "s24": "s2.4_termchecked", "s25": "s2.5_checked",
         "audit": "s2.5_checked",  # s25 兼容别名（ADR-0040 时代步名，ADR-0043 更名）
         "s3": "s3_checked", "r1": "r1_reviewed",
         "r2": "r2_reviewed", "r3": "r3_reviewed", "done": "done"}
ORDER = {
    "retranslate": ["pending", "cleared", "s0_source_checked", "drafted",
                    "s1_checked", "s2_checked",
                    "s2.4_termchecked", "s2.5_checked", "s3_checked", "r1_reviewed",
                    "r2_reviewed", "r3_reviewed", "done"],
    "update": ["pending", "s0_source_checked", "s1_checked", "s2_checked",
               "s2.4_termchecked",
               "s2.5_checked", "s3_checked", "r1_reviewed", "r2_reviewed",
               "r3_reviewed", "done"],
}
STEP_EXPECT_PREV = {
    "s0": ("cleared", "pending"),  # 源审计前置（ADR-0052）：retranslate 在 cleared 后，update 在 pending 后
    "draft": "s0_source_checked", "s1": ("drafted", "s0_source_checked"),
    "s2": "s1_checked",
    "s24": "s2_checked", "s25": "s2.4_termchecked", "audit": "s2_checked",
    "s3": "s2.5_checked", "r1": "s3_checked", "r2": "r1_reviewed",
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


def advance(slug, step, actor, evidence, unblock=False, mandate=""):
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
    if step == "audit":
        step = "s25"  # 兼容别名（ADR-0043 更名；须在状态迁移校验前归一）
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
    if step != "done" and task["kind"] == "update" and step in ("s0", "s1", "s2", "s24", "s25") \
            and not evidence.startswith("changes:"):
        raise PreconditionError("update 任务的 %s 证据必须引用变更清单（evidence 以 changes: 开头）" % step)
    if step == "r3" and task.get("kind") != "glossary-maintenance":
        if not str(mandate or "").strip():
            raise PreconditionError(
                "R3 终审须用户显式指定会话（ADR-0054）：advance --step r3 --mandate "
                "\"<用户指定记录：何时/何范围>\"；未指定时不进行 R3，条目停 r2_reviewed")
        _independence_gate(task, actor, evidence)  # 复核独立性机检（rules/04）
    if step in ("s3", "r3") and task.get("kind") != "glossary-maintenance":
        _academic_gate(task.get("zh_doc"), step)  # 审校挂钩（rules/07）
    if step == "s24" and task.get("kind") != "glossary-maintenance":
        _term_gate(task.get("zh_doc"))  # 术语轴（rules/03/07、ADR-0043）
        _style_gate(task.get("zh_doc"))  # 体例轴＋勘误轴（ADR-0063）
    if step == "s0" and task.get("kind") != "glossary-maintenance":
        _source_gate(slug)  # 源审计前置挂钩（en_integrity＋en_source_audit，ADR-0052）
    if step == "s3" and task.get("kind") != "glossary-maintenance" \
            and not any(s.get("step") == "s0" for s in task.get("steps", [])):
        raise PreconditionError(
            "进三校前必须已有源审计记录（s0，ADR-0052）：在途件先跑 "
            "task_ops.py source-audit 补课（specs/036），新件先 advance --step s0")
    if step == "s25" and task.get("kind") != "glossary-maintenance":
        _audit_gate(task.get("zh_doc"))  # 审计挂钩（rules/04、ADR-0040）
        _audit_independence_gate(task, actor, evidence)  # 同源盲区对冲（specs/027 FR-001）
    task["state"] = STEPS[step]
    step_rec = {"step": step, "status": "ok", "actor": actor,
                "at": utcnow_iso(), "evidence": evidence}
    if step == "r3" and task.get("kind") != "glossary-maintenance":
        step_rec["mandate"] = mandate  # 用户指定终审凭证（ADR-0054）；审计须核对对得上用户当轮发言
    task["steps"].append(step_rec)
    save_task(task)
    return task


def _clear_gate(slug):
    from tools import baseline_audit
    ok, report = baseline_audit.gate_passes(slug)
    if not ok:
        raise PreconditionError("基线 gate 未通过: %s" % json.dumps(report, ensure_ascii=False))


def _term_gate(zh_doc):
    """s2.4_termchecked 校次挂钩：check_terms --docs 定点核销（rules/03/07、ADR-0043）。

    登记册自洽硬错误即拦；告警（滞后/缺裁定日期）留 evidence 不拦。
    词汇表维护任务与无 zh_doc 条目不设门。
    """
    if not zh_doc:
        return
    tools_dir = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                              "tools")
    r = subprocess.run([sys.executable, _os.path.join(tools_dir, "check_terms.py"),
                        "--docs", zh_doc], capture_output=True, text=True)
    if r.returncode == 1:
        raise PreconditionError("术语一致性门禁未通过（s2.4 校次）：%s"
                                % r.stdout.strip()[-800:])


def _style_gate(zh_doc):
    """s2.4 体例轴挂钩（ADR-0063）：结构三则＋勘误落地硬拦，空白类告警不拦。

    `check_pairs --gate` 只对 HARD_RULES（尾序/编号/H1/勘误/出版信息）计退出码；
    `check_style` 为正文体例定点档。桩件与带点补充材料子文档由 check_pairs 内部豁免。
    """
    if not zh_doc:
        return
    tools_dir = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                              "tools")
    for script, args, label in (
            ("check_pairs.py", ["--gate", zh_doc], "体例轴结构/勘误"),
            ("check_style.py", [zh_doc], "正文体例")):
        r = subprocess.run([sys.executable, _os.path.join(tools_dir, script)] + args,
                           capture_output=True, text=True)
        if r.returncode == 1:
            raise PreconditionError("%s门禁未通过（s2.4 体例轴，ADR-0063）：%s"
                                    % (label, (r.stdout or r.stderr).strip()[-800:]))


def _source_gate(slug):
    """s0_source_checked 校次门禁挂钩（ADR-0052）：en_integrity（包完整性）
    ＋en_source_audit（HTML 本体内容审计，离线档）硬错误拦；告警留 evidence
    逐条定性（机检不作裁判，按 ADR-0062 两路：文字层→全局勘误表＋中文译注，
    格式层→baseline/en-patches.json 补丁池）。en/ 包缺失即拦（零信任前置）。"""
    tools_dir = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                              "tools")
    for script, label in (("en_integrity.py", "en 包完整性"),
                          ("en_source_audit.py", "HTML 本体审计")):
        r = subprocess.run([sys.executable, _os.path.join(tools_dir, script), slug],
                           capture_output=True, text=True)
        if r.returncode == 1:
            raise PreconditionError("%s门禁未通过（s0 源审计校次，ADR-0052）：%s"
                                    % (label, (r.stdout or r.stderr).strip()[-800:]))


def source_audit(slug, actor, evidence):
    """在途/done 存量源审计补课（ADR-0052 决策 5、specs/036）。

    向 steps 追加 s0 记录（append-only），状态不迁移；机检门与 advance --step s0
    同源。pending/cleared 不适用（走 advance --step s0 正常推进）。
    """
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    if task.get("kind") == "glossary-maintenance" or task.get("kind") not in ORDER:
        raise PreconditionError("source-audit 不适用于非词条任务")
    if not str(actor or "").strip():
        raise UsageError("actor 必填（写入路径追责字段）")
    if not str(evidence or "").strip():
        raise UsageError("evidence 必填（FR-017）")
    if task.get("blockers"):
        raise PreconditionError("任务被阻塞: %s；先 advance --unblock" % task["blockers"])
    if task["state"] in ("pending", "cleared"):
        raise PreconditionError(
            "状态 %s 用 advance --step s0 正常推进，source-audit 仅补在途/done 存量"
            % task["state"])
    if any(s.get("step") == "s0" for s in task.get("steps", [])):
        raise PreconditionError("任务历史已有 s0 记录，勿重复补课")
    _source_gate(slug)
    task["steps"].append({"step": "s0", "status": "ok", "actor": actor,
                          "at": utcnow_iso(),
                          "evidence": "补课（ADR-0052，状态不迁移）：%s" % evidence})
    save_task(task)
    return task


def revert_state(slug, to_state, reason, actor):
    """受控状态回退原语（026 T0 设计，ADR-0043 目标态；ADR-0063 扩 s2.4）。

    接受 --to {s2.5_checked, s2.4_termchecked}；适用于 state ∈ {s2.5_checked,
    s3_checked, r1_reviewed, r2_reviewed, r3_reviewed, done}；steps 追加 revert
    记录（append-only），不触碰正文与既有 steps/evidence。reason 必填（回退依据）。

    目标态语义同 ADR-0043 既有惯例：置为“该 checkpoint 已完成”，增项须在该状态下补做
    并留 evidence，随后按正常序列推进（回 s2.4 后下一步是 s25，不是重跑 advance s24）。
    """
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    if to_state not in ("s2.5_checked", "s2.4_termchecked"):
        raise UsageError("revert-state 仅支持 --to s2.5_checked 或 s2.4_termchecked"
                         "（ADR-0043 决策 5、ADR-0063）")
    if task.get("kind") == "glossary-maintenance" or task.get("kind") not in ORDER:
        raise PreconditionError("revert-state 不适用于非词条任务")
    if not str(reason or "").strip():
        raise UsageError("revert-state 必须写明回退依据（--reason）")
    if not str(actor or "").strip():
        raise UsageError("actor 必填（写入路径追责字段）")
    if task.get("blockers"):
        raise PreconditionError("任务被阻塞: %s；先 advance --unblock" % task["blockers"])
    if task["state"] not in ("s2.5_checked", "s3_checked", "r1_reviewed",
                             "r2_reviewed", "r3_reviewed", "done"):
        raise PreconditionError(
            "revert-state 要求状态 s2.5/s3/r1/r2/r3/done，当前 %s（更早的任务未经回退点，"
            "按新状态机自然推进）" % task["state"])
    if to_state == "s2.4_termchecked" and not any(
            s.get("step") in ("s2", "s24") for s in task.get("steps", [])):
        raise PreconditionError(
            "该任务历史无 s2/s24 记录，无法定位 s2.4 回退点（先补链，禁跳步）")
    task["steps"].append({"step": "revert-state", "status": "ok", "actor": actor,
                          "at": utcnow_iso(),
                          "evidence": "回退到 %s；依据：%s" % (to_state, reason)})
    task["state"] = to_state
    save_task(task)
    return task


def _audit_independence_gate(task, actor, evidence):
    """audit 校次独立性机检（rules/04“同源盲区对冲”、specs/004 W11、specs/027 FR-001）。

    审计 actor 与初译 actor（retranslate 取 draft、update 取 s1）相同时，属同源盲区
    高危形态，evidence 须记明“冷置”回读或“密度”统计补偿；否则拒绝。旧任务缺首写步
    则跳过（不强溯）。
    """
    first = "draft" if task.get("kind") == "retranslate" else "s1"
    writer = next((s.get("actor") or "" for s in task.get("steps", [])
                   if s.get("step") == first), None)
    if not writer or actor != writer:
        return
    if "冷置" not in (evidence or "") and "密度" not in (evidence or ""):
        raise PreconditionError(
            "审计独立性未满足：audit 与初译 actor（%s）相同，evidence 须记明"
            "“冷置”回读或“密度”统计补偿（rules/04 同源盲区对冲；specs/004 W11）" % writer)


def _audit_gate(zh_doc):
    """s2.5 校次门禁挂钩：check_math_zh 默认档（公式完整性）＋check_style（体例，
    2026-11-15 O1 加挂——回退件历史违例潜伏教训，specs/028 pilot O1）——
    （裸 $、宏残留、中文入公式等 C1–C6/C8）在审计即拦，strict 升档留 s3/r3
    （rules/04 审计已译环节、ADR-0040）。词汇表维护任务与无 zh_doc 条目不设门。"""
    if not zh_doc:
        return
    tools_dir = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                              "tools")
    for script, label in (("check_math_zh.py", "公式体例"), ("check_style.py", "体例预检")):
        r = subprocess.run([sys.executable, _os.path.join(tools_dir, script), zh_doc],
                           capture_output=True, text=True)
        if r.returncode == 1:
            raise PreconditionError("%s门禁未通过（s2.5 校次，specs/028 O1）：%s"
                                    % (label, r.stdout.strip()[-800:]))


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


def reopen(slug, reason, actor, upstream_sync=False):
    """打回 pending（append-only 历史完整；ADR-0033/0050/0051）。

    R1/R2（默认）：仅 done 的 retranslate 任务——质量返工（ADR-0033）或上游实质
    修订（ADR-0050：reopen --clear 置空全量重译）。
    R3 绕过（ADR-0051，--upstream-sync 显式声明）：在途状态（drafted…r3_reviewed）
    遇上游实质修订/换血重发时允许直接打回 pending——绕过「仅 done」限制；
    打回后按 ADR-0050 同构置空重译。约束：reason 必须引用凭证（compare 变更
    文件或分歧账）；blocked 任务仍须先 --unblock；pending/cleared/done 不适用。
    旧 steps 保留为历史（append-only），不删除。
    """
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    if task["kind"] != "retranslate":
        raise UsageError("reopen 仅适用于 retranslate 任务")
    state = task["state"]
    if not str(reason or "").strip():
        raise UsageError("reopen 必须写明返工原因（--reason）")
    if upstream_sync:
        bypassable = set(ORDER["retranslate"]) - {"pending", "cleared", "done"}
        if state not in bypassable:
            raise PreconditionError(
                "reopen --upstream-sync 适用于在途状态（%s）；当前 %s"
                % ("、".join(sorted(bypassable)), state))
    elif state != "done":
        raise PreconditionError(
            "reopen 要求状态 done，当前 %s（在途件遇上游同步用 --upstream-sync，ADR-0051）" % state)
    if task.get("blockers"):
        raise PreconditionError("任务被阻塞: %s；先 advance --unblock" % task["blockers"])
    task["state"] = "pending"
    step = {"step": "reopen", "status": "ok", "actor": actor,
            "at": utcnow_iso(), "evidence": reason}
    if upstream_sync:
        step["bypass"] = "upstream-sync（ADR-0051 R3：在途吸收上游同步）"
    task["steps"].append(step)
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
            args = _parse(["--step", "--actor", "--evidence", "--mandate", "--unblock"],
                          argv[2:])
            task = advance(slug, args.get("step"), args.get("actor") or "?",
                           args.get("evidence") or "", unblock="--unblock" in argv,
                           mandate=args.get("mandate") or "")
            print(json.dumps(task, ensure_ascii=False, indent=2))
            return 0
        if cmd == "clear":
            print(json.dumps(clear(slug), ensure_ascii=False, indent=2))
            return 0
        if cmd == "reopen":
            args = _parse(["--actor", "--reason"], argv[2:])
            task = reopen(slug, args.get("reason") or "",
                          args.get("actor") or "?",
                          upstream_sync="--upstream-sync" in argv)
            if "--clear" in argv:
                # ADR-0050：上游更新引发的 reopen 前置置空（仅留 H1），原子两步防漏
                task = clear(slug)
            print(json.dumps(task, ensure_ascii=False, indent=2))
            return 0
        if cmd == "block":
            args = _parse(["--reason"], argv[2:])
            print(json.dumps(block(slug, args.get("reason") or "unspecified"),
                             ensure_ascii=False, indent=2))
            return 0
        if cmd == "revert-state":
            args = _parse(["--to", "--reason", "--actor"], argv[2:])
            print(json.dumps(revert_state(slug, args.get("to"),
                                          args.get("reason"),
                                          args.get("actor")),
                             ensure_ascii=False, indent=2))
            return 0
        if cmd == "source-audit":
            args = _parse(["--actor", "--evidence"], argv[2:])
            print(json.dumps(source_audit(slug, args.get("actor") or "?",
                                          args.get("evidence") or ""),
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
