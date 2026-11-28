# -*- coding: utf-8 -*-
"""文档任务状态机（FR-011/012/013；状态图见 specs/001-sep-sync-pipeline/data-model.md）。

用法: python tools/task_ops.py <命令> <slug> [参数]
命令: show / create / advance / clear / reopen / block / revert-state / source-audit / competence
状态机（retranslate，identifier 口径，ADR-0080）:
  pending → cleared → ex-04_checked(源审计前置) → tr-02_checked(初译) → tr-03_checked(一校)
          → tr-04_checked(二校) → rv-01_checked(术语校) → rv-02_checked(审计已译)
          → rv-03_checked → rv-04_checked → rv-05_checked
          → rv-06_checked → rv-07_checked → rv-08_checked
          → rv-09_checked(体例终校) → sg-01_checked → sg-02_checked → sg-03_checked → done
  旧状态名（drafted／s1_checked／s2.5_checked／r3_reviewed…）作为输入别名接受，
  经 rules/naming.json 的 state_aliases 归一（ADR-0080）。
  rv-03–rv-08（ADR-0079 六轴，原 q1–q6）：advance 时按步挂对应扫描器 --gate。
  旧命令行短名（s0／s24／s25／audit／s3／r1–r3）保留为输入别名，内部写 identifier。
状态机（update）已删除（ADR-0068 W5）：零任务使用，上游修订走 reopen --upstream-sync。
禁止跳步；blocked 标志独立于状态，解除用 advance --unblock。
合法前驱由 ORDER 单一事实源推导（expected_prev）：目标态不属于该任务 kind 的
序列即拒，且前驱唯一直接前驱——specs/040 F-01/F-02 收口（旧 STEP_EXPECT_PREV 元组并集语义废止）。
ORDER 与 STEPS 由 rules/pipeline.json 推导（ADR-0068 W5），不再硬编码序列。
r3 终审（ADR-0054，用户 2026-11-15 裁定）：仅用户显式指定的会话执行，未指定不进行
终审、条目停 sg-02_checked；advance --step sg-03 必须带 --mandate <用户指定记录>。
源审计（ADR-0052）：advance --step ex-04 自动挂 en_integrity＋en_source_audit；
在途/done 存量补课用 source-audit 子命令（追加 ex-04 记录，状态不迁移）；
进体例终校（rv-09）前任务历史必须有源审计记录。
术语与勘误（ADR-0043/0063）：advance --step rv-01 顺序挂术语轴（check_terms）与
体例轴＋勘误轴（check_pairs --gate 与 check_style，结构硬、空白告警）。
revert-state：受控回退原语，--to {rv-02_checked, rv-01_checked}（旧名 s2.5_checked／
s2.4_termchecked 作输入别名），适用于 rv-02_checked 及其后状态（ADR-0043 全量回退、
ADR-0063 扩 rv-01；steps append-only 留史）。
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
from tools.journal_lib import (NODE_MAP, NODE_TO_STATE, REVERT_CHECKPOINTS,
                               append_event, step_to_event)


def _derive_order_steps():
    """W5：ORDER 与 STEPS 从 rules/pipeline.json 单一源推导，删除硬编码序列。

    ORDER[kind] 的状态序列 = 边界（pending/cleared/done）＋ pipeline 节点链中
    有 NODE_TO_STATE 映射的节点（按 prev 拓扑序）。STEPS = NODE_MAP 短名 → 状态名。
    pipeline 缺失即硬失败（A12 禁静默兜底）。
    """
    pipe_path = repo_path("rules", "pipeline.json")
    if not os.path.exists(pipe_path):
        raise RuntimeError("rules/pipeline.json 不存在（判据唯一事实源，A12）")
    pipe = load_json(pipe_path)
    nodes = {n["id"]: n for n in pipe.get("nodes", [])}
    heads = [i for i in nodes if not nodes[i].get("prev")]
    chain, cur = [], heads[0] if heads else None
    while cur:
        chain.append(cur)
        nxt = [i for i in nodes if nodes[i].get("prev") == cur]
        cur = nxt[0] if len(nxt) == 1 else None
    states = [NODE_TO_STATE[n] for n in chain if n in NODE_TO_STATE]
    order = {
        "retranslate": ["pending", "cleared"] + states + ["done"],
        # update 死序列删除（ADR-0068 W5）：零任务使用，上游修订走 reopen --upstream-sync
    }
    steps = {alias: NODE_TO_STATE[node] for alias, node in NODE_MAP.items()
             if node in NODE_TO_STATE}
    steps["done"] = "done"
    return order, steps


ORDER, STEPS = _derive_order_steps()
# revert-state 可回退目标态：由 pipeline 的 checkpoint 节点推导（ADR-0043/0063）
REVERT_TARGETS = tuple(NODE_TO_STATE[c] for c in REVERT_CHECKPOINTS)


def _history_steps(task):
    """任务历史里出现过的节点 identifier 集合（历史 step 名经别名归一，ADR-0080）。"""
    out = set()
    for s in task.get("steps", []):
        v = s.get("step")
        out.add(NODE_MAP.get(v, v))
    return out


def expected_prev(kind, step):
    """步 s 的合法前驱＝ORDER[kind] 中目标态的唯一直接前驱（specs/040 F-01/F-02 收口）。

    取代旧 STEP_EXPECT_PREV 元组表：旧表是「cur ∈ 允许集」的并集语义，跨 kind
    互通（retranslate 可 pending→s0 跳过 clear、可 s0→s1 跳过 draft），且
    `audit` 表项在归一化后永不读取（死条目）。现由 ORDER 单一事实源推导：
    目标态不属于该 kind 序列即拒，前驱唯一。
    """
    tgt = STEPS[step]
    order = ORDER[kind]
    if tgt not in order:
        raise PreconditionError(
            "step %s 的目标态 %s 不属于 %s 状态序列（禁止跨 kind 推进，specs/040 F-01）"
            % (step, tgt, kind))
    i = order.index(tgt)
    return None if i == 0 else order[i - 1]

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


def _journal_append(task, step_name, evidence, actor):
    """W3 双写：状态推进成功后，向 journal 追加对应事件（P5 只追加）。

    非节点动作（done/clear/block 等）经 step_to_event 返回 None，跳过。
    """
    ev = step_to_event(step_name, evidence or "", utcnow_iso(), actor or "task_ops")
    if ev is None:
        return
    append_event(task["slug"], ev)


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


def create(slug, kind, zh_doc=None, change_file=None, translation_mode="human",
           pe_level="full", pe_system="", pe_disclosure="", project_spec=None):
    if kind != "retranslate":
        raise UsageError("kind 仅支持 retranslate（update 死序列已删，ADR-0068 W5；"
                         "上游修订走 reopen --upstream-sync，ADR-0051）")
    if translation_mode not in ("human", "llm-pe"):
        raise UsageError("translation_mode 仅支持 human／llm-pe（ADR-0084 D2=B）")
    if translation_mode == "llm-pe" and not str(pe_system or "").strip():
        raise UsageError("llm-pe 任务须给 --pe-system（引擎与版本，ADR-0084 D2=B）")
    if load_task(slug):
        raise PreconditionError("任务已存在: %s" % slug)
    spec = _build_project_spec(project_spec)
    want_pe = pe_level if translation_mode == "llm-pe" else "n/a（人工翻译）"
    if project_spec and "pe_level" in project_spec and project_spec["pe_level"] != want_pe:
        raise UsageError("project_spec.pe_level 须与 --pe-level／translation_mode 一致（ADR-0093）")
    spec["pe_level"] = want_pe
    task = {"slug": slug, "kind": kind, "zh_doc": zh_doc, "state": "pending",
            "translation_mode": translation_mode,
            "project_spec": spec,
            "steps": [], "blockers": [], "created_at": utcnow_iso()}
    if translation_mode == "llm-pe":
        task["pe"] = {"level": pe_level, "system": pe_system,
                      "disclosure": pe_disclosure or "tr-02 evidence"}
    # 版本钉一并取：check_academic 对词条绑定任务查 pin、缺失即硬错误（2026-11-04 修潜在陷阱）
    task["version_pin"] = _version_pin(slug)
    if task["zh_doc"] is None:
        zh = find_zh_doc({"slug": slug, "title": _baseline_title(slug)})
        task["zh_doc"] = ("zh/" + zh) if zh else None
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
    step = NODE_MAP.get(step, step)  # 标识归一（ADR-0080）：历史短名／name／identifier
    # 统一为 identifier；非节点动作（done 等）原样透传
    order = ORDER.get(task["kind"])
    if order is None:
        raise PreconditionError("非法任务类型 %s（状态机仅 retranslate）" % task["kind"])
    cur = task["state"]
    prev_needed = expected_prev(task["kind"], step)
    if prev_needed is not None and cur != prev_needed:
        raise PreconditionError(
            "step %s 要求状态 %s，当前 %s（禁止跳步）" % (step, prev_needed, cur))
    if cur not in order:
        raise PreconditionError("非法状态 %s" % cur)
    if step in ("sg-01", "sg-02", "sg-03") and task.get("kind") != "glossary-maintenance":
        if step == "sg-03" and not str(mandate or "").strip():
            raise PreconditionError(
                "终审须用户显式指定会话（ADR-0054）：advance --step sg-03 --mandate "
                "\"<用户指定记录：何时/何范围>\"（旧短名 r3 仍可用）；未指定时不进行终审，"
                "条目停 sg-02_checked")
        _review_independence_gate(task, step, actor)  # 四审分离（ADR-0093）
        _review_competence_gate(task, actor)  # 能力记录（ISO 17100 3.1.3–3.1.7）
    if step in ("rv-09", "sg-03") and task.get("kind") != "glossary-maintenance":
        _academic_gate(task.get("zh_doc"), step)  # 审校挂钩（rules/07）
    if step == "rv-01" and task.get("kind") != "glossary-maintenance":
        _term_gate(task.get("zh_doc"))  # 术语轴（rules/03/07、ADR-0043）
        _style_gate(task.get("zh_doc"))  # 体例轴＋勘误轴（ADR-0063）
    if step == "ex-04" and task.get("kind") != "glossary-maintenance":
        _source_gate(slug)  # 源审计前置挂钩（en_integrity＋en_source_audit，ADR-0052）
    if step == "rv-09" and task.get("kind") != "glossary-maintenance" \
            and "ex-04" not in _history_steps(task):
        raise PreconditionError(
            "进三校前必须已有源审计记录（ex-04，原 s0，ADR-0052）：在途件先跑 "
            "task_ops.py source-audit 补课（specs/036），新件先 advance --step ex-04")
    if step in AXIS_TOOL and task.get("kind") != "glossary-maintenance":
        _axis_gate(step, task.get("zh_doc"))
    if step == "tr-02" and task.get("kind") != "glossary-maintenance":
        _project_spec_gate(task)  # 项目规格机检（ISO 11669:2024；ADR-0093）
        _pe_gate(task, evidence)  # 译后编辑定位机检（ADR-0084 D2=B）
    if step == "rv-02" and task.get("kind") != "glossary-maintenance":
        # 三轴并挂（ADR-0063 2026-11-17 补记）：受控回退的目标态是
        # rv-01_checked（原 s2.4_termchecked，视为该 checkpoint 已完成），随后 normal
        # 推进即 rv-02，advance rv-01 对回退件不可达 → 术语/体例/勘误三轴须在
        # rv-02 复检，否则 P8 回退件整体绕过体例硬门。同一先例见 ADR-0043「s2.4
        # 增项并入 s25 凭证」。三项均只读幂等，正常件在 rv-01 刚过、此处复检零成本。
        _term_gate(task.get("zh_doc"))  # 术语轴（rules/03、ADR-0043）
        _style_gate(task.get("zh_doc"))  # 体例轴＋勘误轴（ADR-0063）
        _audit_gate(task.get("zh_doc"))  # 审计挂钩（rules/04、ADR-0040）
        _audit_independence_gate(task, actor, evidence)  # 同源盲区对冲（specs/027 FR-001）
    task["state"] = STEPS[step]
    step_rec = {"step": step, "status": "ok", "actor": actor,
                "at": utcnow_iso(), "evidence": evidence}
    if step == "sg-03" and task.get("kind") != "glossary-maintenance":
        step_rec["mandate"] = mandate  # 用户指定终审凭证（ADR-0054）；审计须核对对得上用户当轮发言
    task["steps"].append(step_rec)
    save_task(task)
    _journal_append(task, step, evidence, actor)  # W3 双写（done/block 经 step_to_event 跳过）
    return task


def _clear_gate(slug):
    from tools import baseline_audit
    ok, report = baseline_audit.gate_passes(slug)
    if not ok:
        raise PreconditionError("基线 gate 未通过: %s" % json.dumps(report, ensure_ascii=False))


PROJECT_SPEC_SCHEMA = {
    "content": ("language_pair", "content_type", "audience", "purpose",
                "subject_field", "terminology_basis", "register"),
    "process": ("workflow", "pe_level", "qa_level", "pre_edit"),
    "other": ("risk_level", "confidentiality", "delivery", "communication",
              "qualifications"),
}
PROJECT_SPEC_FIELDS = tuple(k for keys in PROJECT_SPEC_SCHEMA.values() for k in keys)
PROJECT_SPEC_REQUIRED = ("audience", "purpose", "qa_level", "pe_level", "risk_level")
PROJECT_SPEC_DEFAULT = {
    "language_pair": "en → zh-Hans",
    "content_type": "学术百科词条（SEP）",
    "audience": "中文哲学读者（研究者与研究生为主）",
    "purpose": "学术阅读与引用（SEP 词条简体中文译本）",
    "subject_field": "哲学（按词条分支）",
    "terminology_basis": "shu-yu-biao.md／ren-ming-biao.md／baseline/term-concepts.md",
    "register": "现代汉语学术书面语",
    "workflow": "retranslate 22 节点（rules/04）",
    "pe_level": "n/a（人工翻译）",
    "qa_level": "CY/T 266＋ISO 5060（六轴机检＋人工复核）",
    "pre_edit": "源审计后按 tr-01 术语摘录与提示词准备",
    "risk_level": "B 中",
    "confidentiality": "公开源；未公开草稿与审稿意见不入模型",
    "delivery": "GitBook Markdown＋VitePress 双语站",
    "communication": "任务 evidence＋journal",
    "qualifications": "见 task.competences（ISO 17100 3.1.3–3.1.7）",
}
RISK_LEVELS = ("A 高", "B 中", "C 低／内部")
PE_LEVELS = ("full", "light", "n/a（人工翻译）")
COMPETENCE_FIELDS = ("qualification", "experience", "domain", "training")


def _project_spec_gate(task):
    """项目规格机检（ISO 11669:2024；ADR-0086／ADR-0093）：16 字段非空且枚举合法才可进 tr-02。"""
    spec = task.get("project_spec") or {}
    miss = [k for k in PROJECT_SPEC_FIELDS if not str(spec.get(k) or "").strip()]
    if miss:
        raise PreconditionError(
            "project_spec 缺项 %s（ISO 11669:2024 项目规格，ADR-0093）：补齐后再进 tr-02"
            % "/".join(miss))
    if spec.get("risk_level") not in RISK_LEVELS:
        raise PreconditionError(
            "project_spec.risk_level 须为 %s（ADR-0093）" % "／".join(RISK_LEVELS))
    pe_level = spec.get("pe_level")
    if pe_level not in PE_LEVELS:
        raise PreconditionError(
            "project_spec.pe_level 须为 %s（ADR-0093）" % "／".join(PE_LEVELS))
    if task.get("translation_mode") == "llm-pe":
        if pe_level != (task.get("pe") or {}).get("level"):
            raise PreconditionError(
                "project_spec.pe_level 与 task.pe.level 不一致（ADR-0093）")
    elif pe_level != "n/a（人工翻译）":
        raise PreconditionError(
            "human 任务的 project_spec.pe_level 须为 n/a（人工翻译）（ADR-0093）")


def _build_project_spec(overrides):
    spec = dict(PROJECT_SPEC_DEFAULT)
    for k, v in (overrides or {}).items():
        if k not in PROJECT_SPEC_FIELDS:
            raise UsageError("project_spec 未知字段: %s（可选 %s）"
                             % (k, "/".join(PROJECT_SPEC_FIELDS)))
        if not str(v or "").strip():
            raise UsageError("project_spec.%s 不得为空（ISO 11669:2024）" % k)
        spec[k] = str(v).strip()
    return spec


def _pe_gate(task, evidence):
    """译后编辑定位机检（ADR-0084 D2=B；标准 ISO 18587:2017／GB/T 40036-2021）。

    llm-pe 任务：PE 级别须为 full（light 须有用户逐件裁定的 light_basis）、引擎与版本、
    披露位置均非空；tr-02 evidence 须写明“译后编辑”或“PE”。human 任务不设门。
    """
    if task.get("translation_mode") != "llm-pe":
        return
    pe = task.get("pe") or {}
    level = str(pe.get("level") or "")
    if level not in ("full", "light"):
        raise PreconditionError("llm-pe 任务须有 pe.level=full／light（ADR-0084 D2=B）")
    if level == "light" and not str(pe.get("light_basis") or "").strip():
        raise PreconditionError("轻译后编辑须有用户逐件裁定记录（pe.light_basis）")
    for key, label in (("system", "引擎与版本"), ("disclosure", "披露位置")):
        if not str(pe.get(key) or "").strip():
            raise PreconditionError("llm-pe 任务缺 pe.%s（%s）" % (key, label))
    if "译后编辑" not in (evidence or "") and "PE" not in (evidence or ""):
        raise PreconditionError(
            "llm-pe 任务 tr-02 evidence 须写明译后编辑（含“译后编辑”或“PE”），"
            "以对应 ISO 18587／GB/T 40036 的过程留痕（ADR-0084 D2=B）")


AXIS_TOOL = {"rv-03": "cite_audit.py", "rv-04": "logic_audit.py",
             "rv-05": "grammar_audit.py", "rv-06": "register_audit.py",
             "rv-07": "measure_audit.py", "rv-08": "punct_audit.py"}


def _axis_gate(step, zh_doc):
    """六轴校次挂钩（ADR-0079）：对应扫描器 --gate，未裁定/未登记即拦。

    机检只筛，人审为判：--gate 通过只证明清单与裁决字段齐备，不证明内容合格。
    无 zh_doc（词汇表维护等）不设门。
    """
    if not zh_doc:
        return
    tools_dir = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                              "tools")
    script = AXIS_TOOL[step]
    r = subprocess.run([sys.executable, _os.path.join(tools_dir, script),
                        zh_doc, "--gate"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode == 1:
        raise PreconditionError("%s 门禁未通过（ADR-0079 六轴工序）：%s"
                                % (step, (r.stdout or r.stderr).strip()[-800:]))


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
    格式层→baseline/en-patches/ 补丁池，一补丁一文件）。en/ 包缺失即拦（零信任前置）。"""
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

    向 steps 追加 ex-04 记录（append-only），状态不迁移；机检门与 advance --step ex-04
    （旧名 s0）同源。pending/cleared 不适用（走 advance --step ex-04 正常推进）。
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
            "状态 %s 用 advance --step ex-04（旧名 s0）正常推进，"
            "source-audit 仅补在途/done 存量" % task["state"])
    if "ex-04" in _history_steps(task):
        raise PreconditionError("任务历史已有源审计记录（ex-04，原 s0），勿重复补课")
    _source_gate(slug)
    task["steps"].append({"step": "ex-04", "status": "ok", "actor": actor,
                          "at": utcnow_iso(),
                          "evidence": "补课（ADR-0052，状态不迁移）：%s" % evidence})
    save_task(task)
    _journal_append(task, "ex-04", "补课（ADR-0052）：%s" % evidence, actor)
    return task


def revert_state(slug, to_state, reason, actor):
    """受控状态回退原语（026 T0 设计，ADR-0043 目标态；ADR-0063 扩 rv-01）。

    接受 --to {rv-02_checked, rv-01_checked}（旧名 s2.5_checked／s2.4_termchecked
    仍可作输入别名）；适用于 state ∈ {rv-02_checked, rv-09_checked, sg-01_checked,
    sg-02_checked, sg-03_checked, done}；steps 追加 revert 记录（append-only），
    不触碰正文与既有 steps/evidence。reason 必填（回退依据）。

    目标态语义同 ADR-0043 既有惯例：置为“该 checkpoint 已完成”，增项须在该状态下补做
    并留 evidence，随后按正常序列推进（回 rv-01 后下一步是 rv-02，不是重跑 advance rv-01）。
    """
    from tools import naming_lib
    to_state = naming_lib.normalize_state(to_state)
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    if to_state not in REVERT_TARGETS:
        raise UsageError("revert-state 仅支持 --to %s（由 pipeline checkpoint 推导，ADR-0068 W5；"
                         "旧状态名亦作别名接受）" % " 或 ".join(REVERT_TARGETS))
    if task.get("kind") == "glossary-maintenance" or task.get("kind") not in ORDER:
        raise PreconditionError("revert-state 不适用于非词条任务")
    if not str(reason or "").strip():
        raise UsageError("revert-state 必须写明回退依据（--reason）")
    if not str(actor or "").strip():
        raise UsageError("actor 必填（写入路径追责字段）")
    if task.get("blockers"):
        raise PreconditionError("任务被阻塞: %s；先 advance --unblock" % task["blockers"])
    if task["state"] not in ("rv-02_checked", "rv-09_checked", "sg-01_checked",
                             "sg-02_checked", "sg-03_checked", "done"):
        raise PreconditionError(
            "revert-state 要求状态 rv-02/rv-09/sg-01/sg-02/sg-03/done，当前 %s"
            "（更早的任务未经回退点，按新状态机自然推进）" % task["state"])
    if to_state == "rv-01_checked" and not (_history_steps(task) & {"tr-04", "rv-01"}):
        raise PreconditionError(
            "该任务历史无 tr-04/rv-01 记录（原 s2/s24），无法定位 rv-01 回退点（先补链，禁跳步）")
    task["steps"].append({"step": "revert-state", "status": "ok", "actor": actor,
                          "at": utcnow_iso(),
                          "evidence": "回退到 %s；依据：%s" % (to_state, reason)})
    task["state"] = to_state
    save_task(task)
    _journal_append(task, "revert-state",
                    "回退到 %s；依据：%s" % (to_state, reason), actor)
    return task


def _audit_independence_gate(task, actor, evidence):
    """audit 校次独立性机检（rules/04“同源盲区对冲”、specs/004 W11、specs/027 FR-001）。

    审计 actor 与初译 actor（retranslate 取 draft、update 取 s1）相同时，属同源盲区
    高危形态，evidence 须记明“冷置”回读或“密度”统计补偿；否则拒绝。旧任务缺首写步
    则跳过（不强溯）。
    """
    first = "tr-02" if task.get("kind") == "retranslate" else "tr-03"
    writer = next((s.get("actor") or "" for s in task.get("steps", [])
                   if NODE_MAP.get(s.get("step"), s.get("step")) == first), None)
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


def _review_independence_gate(task, step, actor):
    """四审分离硬门（ADR-0093 取代 ADR-0084 D1=C）：译者≠初审≠复审≠终审。

    sg-01 须异于初译；sg-02 须异于初译与 sg-01；sg-03 须异于初译、sg-01、sg-02。
    冷置／密度补偿一律不适用。旧任务缺相应步骤时，仅在可判定范围内检查。
    """
    steps = task.get("steps", [])

    def actor_of(node):
        return next((s.get("actor") or "" for s in steps
                     if NODE_MAP.get(s.get("step"), s.get("step")) == node), None)

    translator = actor_of("tr-02")
    prior = []
    if translator:
        prior.append(("初译", translator))
    if step in ("sg-02", "sg-03"):
        a = actor_of("sg-01")
        if a:
            prior.append(("初审", a))
    if step == "sg-03":
        a = actor_of("sg-02")
        if a:
            prior.append(("复审", a))
    conflicts = [label for label, a in prior if a == actor]
    if conflicts:
        raise PreconditionError(
            "审校独立性未满足（ADR-0093）：actor %r 已参与 %s；"
            "译者≠初审≠复审≠终审，冷置／密度补偿一律不适用"
            % (actor, "、".join(conflicts)))


def _review_competence_gate(task, actor):
    """审校能力记录（ISO 17100 3.1.3–3.1.7；ADR-0093）。"""
    rec = (task.get("competences") or {}).get(actor) or {}
    miss = [k for k in COMPETENCE_FIELDS if not str(rec.get(k) or "").strip()]
    if miss:
        raise PreconditionError(
            "审校 actor %r 缺 competence 记录 %s（ISO 17100 3.1.3–3.1.7）：先 "
            "task_ops.py competence %s --actor %r --qualification ... --experience ... "
            "--domain ... --training ..." % (actor, "/".join(miss), task.get("slug"), actor))


def set_competence(slug, actor, qualification, experience, domain, training):
    """登记审校能力记录（ADR-0093；ISO 17100 3.1.3–3.1.7）。"""
    task = load_task(slug)
    if not task:
        raise TaskNotFound(slug)
    actor = str(actor or "").strip()
    if not actor:
        raise UsageError("competence 须给 --actor")
    rec = {"qualification": str(qualification or "").strip(),
           "experience": str(experience or "").strip(),
           "domain": str(domain or "").strip(),
           "training": str(training or "").strip()}
    miss = [k for k in COMPETENCE_FIELDS if not rec[k]]
    if miss:
        raise UsageError("competence 缺项 %s（ISO 17100 3.1.3–3.1.7）" % "/".join(miss))
    task.setdefault("competences", {})[actor] = rec
    save_task(task)
    return task


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
    _journal_append(task, "reopen", reason, actor)
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
            args = _parse(["--kind", "--zh-doc", "--from", "--translation-mode",
                           "--pe-level", "--pe-system", "--pe-disclosure",
                           "--spec-audience", "--spec-purpose", "--spec-register",
                           "--spec-basis", "--spec-delivery", "--spec-qa",
                           "--spec-content-type", "--spec-subject-field",
                           "--spec-pe-level", "--spec-risk-level",
                           "--spec-confidentiality", "--spec-qualifications"], argv[2:])
            spec = {}
            for flag, key in (("spec_audience", "audience"), ("spec_purpose", "purpose"),
                              ("spec_register", "register"), ("spec_basis", "terminology_basis"),
                              ("spec_delivery", "delivery"), ("spec_qa", "qa_level"),
                              ("spec_content_type", "content_type"),
                              ("spec_subject_field", "subject_field"),
                              ("spec_pe_level", "pe_level"),
                              ("spec_risk_level", "risk_level"),
                              ("spec_confidentiality", "confidentiality"),
                              ("spec_qualifications", "qualifications")):
                if args.get(flag):
                    spec[key] = args[flag]
            task = create(slug, args.get("kind"), args.get("zh_doc"), args.get("from"),
                          translation_mode=args.get("translation_mode") or "human",
                          pe_level=args.get("pe_level") or "full",
                          pe_system=args.get("pe_system") or "",
                          pe_disclosure=args.get("pe_disclosure") or "",
                          project_spec=spec or None)
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
        if cmd == "competence":
            args = _parse(["--actor", "--qualification", "--experience",
                           "--domain", "--training"], argv[2:])
            print(json.dumps(set_competence(
                slug, args.get("actor") or "", args.get("qualification") or "",
                args.get("experience") or "", args.get("domain") or "",
                args.get("training") or ""), ensure_ascii=False, indent=2))
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
