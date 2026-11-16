# -*- coding: utf-8 -*-
"""全系统融洽性审计计算器（specs/040）。

从权威实现（tools/task_ops.py、tools/check_all.py）与规范文本（rules/、
tasks/README.md、contracts/cli.md、rules/adr/）出发，计算六组性质并输出
机读报告（stdout JSON）与人读摘要（stderr）：

  A. 任务状态机 LTS：可达性、死端、目标态越界（kind 纯度）、别名死条目、
     文档（tasks/README）与实现（ORDER）逐态对账。
  B. 门禁映射 Γ：GATES 逐项在 rules/05 CI 清单与工具表中的登记情况；
     rules/05 工具表 vs tools/*.py 全集差集（未登记工具）。
  C. ADR 链：索引状态 vs 正文状态、编号连续性、悬空引用
     （AGENTS/rules/tasks/cli/tools 内引用的 ADR-NNNN 是否有文件）。
  D. 文档声称 vs 数据事实：门禁计数四处口径、rules/01:80 行数声称、
     分歧账/补丁池/基线计数、revert 口径三处文本（ADR-0043 vs ADR-0063）。
  E. 陈旧面扫描：en-patches.json 旧路径、积压线文案、就地改正残留、
     旧目录布局 docstring（rebuild_dir/compose_from_ledger）。
  F. ADR 语义错引启发：check_academic 引 0057（SUMMARY 题）作语体留痕据、
     check_tables_images 引 0036（词汇表题）作表格图片据。

用法: python specs/040-coherence-audit/bin/audit_coherence.py [--quiet]
输出: stdout JSON（schema sep-cn-coherence-audit/1）；退出码 0（恒 0，
      只报告不拦门——本工具是审计面，不是门禁）。
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

if (getattr(sys.stdout, "encoding", "") or "").lower().replace("-", "") != "utf8":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    except (AttributeError, ValueError):
        pass

from tools import task_ops as T  # noqa: E402
from tools.check_all import GATES, OPTIONAL, UNIT_TESTS  # noqa: E402

report = {"schema": "sep-cn-coherence-audit/1", "at": __import__("datetime").datetime.now(
    __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "root": ROOT}


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


# ============ A. 任务状态机 LTS ============
lts = {"ORDER": {k: v for k, v in T.ORDER.items()},
       "STEPS": dict(T.STEPS), "STEP_EXPECT_PREV": {k: list(v) if isinstance(v, tuple)
                                                    else [v] for k, v in T.STEP_EXPECT_PREV.items()}}
# 边集：expect 元组的实现语义是「cur ∈ 允许集」（并集，任意 kind 皆可取任一元素），
# 并非按 kind 绑定——此弱化本身是 LTS 发现（retranslate 可跳过 clear/draft）。
# 边按 (kind, prev∈exp) 全展开；clear/reopen/revert 为独立命令边，一并入图。
edges = []
viol_target = []   # 目标态越界（update 漂入 retranslate 专用态）
viol_pred = []     # 允许集 ≠ 该 kind 内目标态唯一前驱（禁跳步弱化）
kinds = list(T.ORDER)
for step, exp in T.STEP_EXPECT_PREV.items():
    tgt = T.STEPS[step]
    exps = exp if isinstance(exp, tuple) else (exp,)
    for kind in kinds:
        order = T.ORDER[kind]
        for prev in exps:
            if prev in order:
                edges.append((kind, prev, step, tgt))
                if tgt not in order:
                    viol_target.append({"kind": kind, "from": prev, "step": step, "to": tgt})
# 独立命令边：clear（pending→cleared，仅 retranslate）、reopen（done→pending 默认；
# --upstream-sync：在途→pending）、revert-state（源集→目标两态）
edges.append(("retranslate", "pending", "clear", "cleared"))
reopen_src = ["done"] + [s for s in T.ORDER["retranslate"]
                         if s not in ("pending", "cleared", "done")]
for s in reopen_src:
    edges.append(("retranslate", s, "reopen" + ("--upstream-sync" if s != "done" else ""),
                  "pending"))
for s in ("s2.5_checked", "s3_checked", "r1_reviewed", "r2_reviewed", "r3_reviewed", "done"):
    edges.append(("retranslate", s, "revert-state", "s2.5_checked"))
    edges.append(("retranslate", s, "revert-state", "s2.4_termchecked"))
# 可达性（advance 边）与前驱对账
for kind, order in T.ORDER.items():
    preds_of = {order[0]: []}
    for i, st in enumerate(order[1:], 1):
        preds_of[st] = [order[i - 1]]
    for k2, prev, step, tgt in edges:
        if k2 != kind:
            continue
        if step.startswith(("clear", "reopen", "revert")):
            continue
        if tgt not in order:
            continue
        if tgt != prev and prev not in preds_of.get(tgt, []) + [tgt]:
            viol_pred.append({"kind": kind, "from": prev, "step": step,
                              "to": tgt, "preds_of_tgt": preds_of.get(tgt, [])})
    reach, frontier = {order[0]}, [order[0]]
    while frontier:
        cur = frontier.pop()
        for k2, prev, step, tgt in edges:
            if k2 == kind and prev == cur and tgt in order and tgt not in reach:
                reach.add(tgt)
                frontier.append(tgt)
    lts.setdefault("reach", {})[kind] = {"unreachable": [s for s in order if s not in reach],
                                         "dead_ends": [s for s in reach
                                                       if s != order[-1] and s not in
                                                       {p for _k, p, _s, _t in edges if _k == kind}]}
# 别名死条目：advance 在 expect 查表前把 audit 归一为 s25，故 audit 的表项不可达
alias_dead = []
if "audit" in T.STEP_EXPECT_PREV:
    alias_dead.append({"step": "audit", "table_entry": list(
        T.STEP_EXPECT_PREV["audit"] if isinstance(T.STEP_EXPECT_PREV["audit"], tuple)
        else (T.STEP_EXPECT_PREV["audit"],)),
        "actual_after_remap": list(T.STEP_EXPECT_PREV["s25"] if isinstance(
            T.STEP_EXPECT_PREV["s25"], tuple) else (T.STEP_EXPECT_PREV["s25"],))})
# 文档对账：tasks/README 状态机块与 rules/04 状态序列表逐态出现
readme = read("tasks/README.md")
rules04 = read("rules/04-translation-workflow.md")
doc_missing = []
for kind, order in T.ORDER.items():
    for st in order:
        for label, text in (("tasks/README.md", readme), ("rules/04", rules04)):
            if st not in text:
                doc_missing.append({"kind": kind, "state": st, "doc": label})
lts.update({"edges": len(edges), "viol_target_outside_order": viol_target,
            "viol_pred_jump": viol_pred, "alias_dead_entry": alias_dead,
            "doc_state_missing": doc_missing})
report["A_state_machine"] = lts

# ============ B. 门禁映射 Γ ============
gamma = {"gates": []}
rules05 = read("rules/05-ci-and-tools.md")
agents = read("AGENTS.md")
cli = read("specs/001-sep-sync-pipeline/contracts/cli.md")
tasks_readme = readme
for name, key, cmd in GATES:
    tool = cmd.split()[0].replace("tools/", "").replace(".py", "")
    row = {"key": key, "tool": tool + ".py", "in_rules05_workflow_table": False,
           "in_rules05_tool_table": False, "in_cli": False, "in_agents": False}
    if tool + ".py" in rules05:
        row["in_rules05_tool_table"] = True
    if tool in rules05:
        row["in_rules05_workflow_table"] = True
    if tool in cli:
        row["in_cli"] = True
    if tool in agents:
        row["in_agents"] = True
    gamma["gates"].append(row)
# CI 矩阵清单段（rules/05:11）含的工具名
wf_names = ["check_summary", "check_mulu_s", "check_doc_size", "check_junk",
            "check_images", "check_terms", "check_quotes", "check_academic",
            "check_math_zh", "divergence"]
gamma["rules05_ci_list_missing_vs_GATES"] = [k for (_n, k, c) in GATES
                                             if c.split()[0].replace("tools/", "")
                                             .replace(".py", "") not in wf_names]
# rules/05 工具表登记 vs 全集（表行内可含多具 `name.py`，逐行全取）
table_tools = set()
for line in rules05.splitlines():
    if line.lstrip().startswith("|"):
        table_tools.update(re.findall(r"`([a-z_0-9]+)\.py`", line))
actual = sorted(f[:-3] for f in os.listdir(os.path.join(ROOT, "tools"))
                if f.endswith(".py") and f not in ("__init__.py",))
gamma["tools_unregistered_in_rules05"] = [t for t in actual if t not in table_tools]
gamma["rules05_table_ghost"] = sorted(t for t in table_tools if t + ".py" not in
                                      [a + ".py" for a in actual])
gamma["optional_all_items"] = [o[0] for o in OPTIONAL]
gamma["count"] = {"gates": len(GATES), "plus_unittest": len(GATES) + 1,
                  "with_all": len(GATES) + 1 + len(OPTIONAL)}
report["B_gamma"] = gamma

# ============ C. ADR 链 ============
adr = {}
adrdir = os.path.join(ROOT, "rules", "adr")
idx = read("rules/adr/README.md")
index_rows = re.findall(r"\|\s*\[(\d{4})\]\(([^)]+\.md)\)\s*\|\s*([^|]+)\|\s*(\S+)\s*\|", idx)
adr["index_count"] = len(index_rows)
adr["index_status"] = {n: s for n, _f, _t, s in index_rows}
adr["files"] = sorted(f for f in os.listdir(adrdir) if re.match(r"^\d{4}", f))
adr["numbering_gap"] = [n for n in range(1, len(adr["files"]) + 1)
                        if "%04d" % n not in {f[:4] for f in adr["files"]}]
adr["dangling_index_file"] = [n for n, f, _t, _s in index_rows
                              if not os.path.exists(os.path.join(adrdir, f))]
status_mismatch = []
for f in adr["files"]:
    n = f[:4]
    head = read(os.path.join("rules", "adr", f))[:1200]
    m = re.search(r"状态[：:]\s*\*{0,2}([A-Za-z]+)", head)
    if m and n in adr["index_status"]:
        file_st = m.group(1).lower()
        if file_st != adr["index_status"][n].lower() and not (
                file_st == "accepted" and adr["index_status"][n] == "accepted"):
            status_mismatch.append({"adr": n, "index": adr["index_status"][n],
                                    "file": m.group(0)[:60]})
adr["status_mismatch"] = status_mismatch
# 悬空引用：AGENTS/rules/tasks/cli/tools 内 ADR-NNNN 引用
ref_sites = ["AGENTS.md", "tasks/README.md",
             "specs/001-sep-sync-pipeline/contracts/cli.md",
             "specs/001-sep-sync-pipeline/results/en-errata.md"]
ref_sites += ["rules/" + f for f in sorted(os.listdir(os.path.join(ROOT, "rules")))
              if f.endswith(".md")]
ref_sites += ["rules/adr/README.md"]
ref_sites += ["tools/" + f for f in actual]
refs = {}
for site in ref_sites:
    try:
        text = read(site)
    except OSError:
        continue
    for m in re.finditer(r"ADR[- ]?(\d{4})", text):
        refs.setdefault(m.group(1), set()).add(site)
existing = {f[:4] for f in adr["files"]}
adr["referenced"] = sorted(refs)
adr["dangling_refs"] = {n: sorted(s) for n, s in refs.items() if n not in existing}
# 取代链（索引标题与正文中的显式取代/修订表述）
sup = []
for f in adr["files"]:
    text = read(os.path.join("rules", "adr", f))
    n = f[:4]
    for m in re.finditer(r"(取代|修订|作废|部分被取代)[^。\n]{0,60}?(\d{4})", text):
        sup.append({"adr": n, "relation": m.group(1), "other": m.group(2)})
adr["supersede_mentions"] = sup
report["C_adr_chain"] = adr

# ============ D. 文档声称 vs 数据事实 ============
claims = {}
# 门禁计数四处口径
counts_scan = {}
for site in ("AGENTS.md", "rules/05-ci-and-tools.md", "rules/06-governance.md",
             "rules/09-process-standard.md"):
    text = read(site)
    hits = re.findall(r"[^。\n]*?(?:九项门禁|十项门禁|十一项门禁|共 10 项|共 12 项|10 项)[^。\n]*",
                      text)
    counts_scan[site] = [h.strip()[:80] for h in hits][:6]
claims["gate_count_statements"] = counts_scan
claims["gate_count_actual"] = gamma["count"]
# rules/01:80 行数声称
r01 = read("rules/01-repository-structure.md")
m = re.search(r"当前最大\s*(rules/\d+[^，。\s]*)\s*(\d+)\s*行", r01)
if m:
    claimed_file, claimed_n = m.group(1), int(m.group(2))
    real = {}
    for f in os.listdir(os.path.join(ROOT, "rules")):
        if re.match(r"^0\d.*\.md$", f):
            with open(os.path.join(ROOT, "rules", f), encoding="utf-8") as fh:
                real["rules/" + f] = sum(1 for _ in fh)
    mx = max(real, key=real.get)
    claims["rules_line_claim"] = {"claimed": "%s %s 行" % (claimed_file, claimed_n),
                                  "actual_max": "%s %d 行" % (mx, real[mx]),
                                  "all": real}
# revert 口径三处（ADR-0063 扩 s2.4 后仍写旧口径的面）
claims["revert_scope"] = {
    "rules04_has_expansion": "源态集扩" in rules04,
    "tasks_README_line": [l.strip()[:90] for l in readme.splitlines()
                          if "revert-state" in l],
    "cli_line": [l.strip()[:90] for l in cli.splitlines() if "revert-state" in l],
}
# update s2.4 作用域口径（rules/04 全文档 vs tasks/README 仅变更段）
claims["update_s24_scope"] = {
    "rules04": [l.strip()[:90] for l in rules04.splitlines() if "体例轴与勘误轴跑全文档" in l],
    "tasks_README": [l.strip()[:90] for l in readme.splitlines()
                     if "s2.4_termchecked（仅变更段）" in l],
}
# s25/s3 挂钩清单口径（code 实况 vs cli.md 摘要）
claims["step_hooks"] = {
    "code_s25_extra_style": "check_style.py" in read("tools/task_ops.py"),
    "code_s3_extra_mathzh_strict": True,
    "cli_s25_mentions_style": "s25 挂 check_style" in cli or (
        "check_style" in [seg for seg in re.findall(r"s25 挂 [^；\n]*", cli)[0]]
        if re.findall(r"s25 挂 [^；\n]*", cli) else False),
    "cli_s3_lines": [l.strip()[:110] for l in cli.splitlines() if "s3/r3 挂" in l],
}
# 数据事实
def jload(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return json.load(f)

try:
    dv = jload("baseline/divergences.json")
    claims["divergences"] = {"active": len(dv.get("divergences", [])),
                             "tombstones": len(dv.get("tombstones", []))}
except OSError:
    claims["divergences"] = "missing"
try:
    ent = jload("baseline/entries.json")
    es = ent["entries"]
    claims["baseline"] = {"entries": len(es),
                          "pin_files": sum(len(e.get("files", [])) for e in es),
                          "yuanwen_recs": sum(1 for e in es if e.get("yuanwen"))}
except OSError:
    claims["baseline"] = "missing"
try:
    idxp = jload("baseline/en-patches/INDEX.json")
    claims["en_patches"] = {"index_count": idxp.get("count"),
                            "files": len([f for f in os.listdir(
                                os.path.join(ROOT, "baseline", "en-patches"))
                                if f.endswith(".patch")])}
except OSError:
    claims["en_patches"] = "missing"
errata = read("specs/001-sep-sync-pipeline/results/en-errata.md")
body8 = errata[errata.find("## 八、"):]
rows8 = [l for l in body8.splitlines()
         if l.startswith("|") and len(l.strip("|").split("|")) == 7
         and l.strip("|").split("|")[0].strip() not in ("", "slug")
         and not set(l.strip("|").split("|")[0].strip()) <= set("- ")]
claims["errata_sec8plus_rows"] = len(rows8)
# Φ 可满足性 witness：done 任务计数与版本钉完备率
import glob as _glob
done_n, pin_ok_n = 0, 0
for fp in _glob.glob(os.path.join(ROOT, "tasks", "*", "*.json")):
    try:
        with open(fp, encoding="utf-8") as fh:
            rec = json.load(fh)
    except (OSError, ValueError):
        continue
    if not isinstance(rec, dict) or rec.get("state") != "done":
        continue
    if rec.get("kind") == "glossary-maintenance" or not str(rec.get("zh_doc") or "").strip():
        continue
    done_n += 1
    pin = rec.get("version_pin") or {}
    if all(str(pin.get(k) or "").strip() for k in ("pubinfo_date", "sha256")):
        pin_ok_n += 1
claims["phi_witness"] = {"done_tasks": done_n, "done_with_pin": pin_ok_n}
report["D_claims_vs_facts"] = claims

# ============ E. 陈旧面扫描 ============
stale = {"en_patches_json_path": [], "backlog_line": [], "inplace_fix": [],
         "old_layout_docstring": [], "render_todo_note": []}
for f in actual:
    text = read("tools/" + f + ".py")
    if "en-patches.json" in text:
        for i, l in enumerate(text.splitlines(), 1):
            if "en-patches.json" in l:
                stale["en_patches_json_path"].append("%s:%d" % (f, i))
    if "积压" in text and f == "sync_guard":
        stale["backlog_line"].append("sync_guard.py (docstring+cmd_status)")
    if f == "rebuild_dir" and "index.md" in text[:2000]:
        stale["old_layout_docstring"].append("rebuild_dir.py docstring 仍写 <slug>/index.md")
    if f == "compose_from_ledger" and re.search(r"tasks/h/|h/<slug>", text[:1500]):
        stale["old_layout_docstring"].append("compose_from_ledger.py docstring 仍写 tasks/h/ 与 h/<slug>")
    if f == "check_render_artifacts" and "待登记" in text[:1200]:
        stale["render_todo_note"].append("check_render_artifacts.py docstring 仍写“待登记 rules/05”")
for site, pat in (("rules/01-repository-structure.md", "就地改"),
                  ("rules/03-terminology.md", "CNKI 翻译助手"),
                  ("rules/04-translation-workflow.md", "派工单 A2")):
    text = read(site)
    for i, l in enumerate(text.splitlines(), 1):
        if pat in l:
            stale.setdefault(site, []).append("第 %d 行含「%s」：%s" % (i, pat, l.strip()[:70]))
report["E_stale_faces"] = stale

# ============ F. ADR 语义错引启发 ============
miscites = []
ca = read("tools/check_academic.py")
if "ADR-0057" in ca:
    t57 = read(os.path.join("rules", "adr",
               [f for f in adr["files"] if f.startswith("0057")][0]))[:200]
    miscites.append({"tool": "check_academic.py", "cited": "ADR-0057",
                     "adr0057_title_head": t57.splitlines()[0][:70],
                     "expected": "ADR-0058（语体留痕步级时点）"})
cti = read("tools/check_tables_images.py")
if "ADR-0036" in cti:
    t36 = read(os.path.join("rules", "adr",
               [f for f in adr["files"] if f.startswith("0036")][0]))[:200]
    miscites.append({"tool": "check_tables_images.py", "cited": "ADR-0036",
                     "adr0036_title_head": t36.splitlines()[0][:70],
                     "expected": "ADR-0037（表格与图片体例）"})
report["F_adr_miscites"] = miscites

# ============ G. 规范层 O/F 冲突机检子集 ============
conf = []
r05 = rules05
r06 = read("rules/06-governance.md")
if "--no-gpg-sign" in r06 and "无需 --no-gpg-sign" in r05:
    conf.append({"id": "gpg", "a": "rules/06 §并发会话纪律 2：一律 git commit --no-gpg-sign",
                 "b": "rules/05 §提交策略：提交默认免签、无需 --no-gpg-sign"})
if "dict.cnki.net" in read("rules/03-terminology.md") and "不再新增查询" in read("rules/03-terminology.md"):
    conf.append({"id": "cnki", "a": "rules/03 §译名依据优先级 1：知网系权威源（CNKI 翻译助手、术语在线）",
                 "b": "rules/03 §术语落地：术语在线与 CNKI 翻译助手不再新增查询（2026-11-14 裁定）"})
r01_70 = [l for l in r01.splitlines() if "四类勘误可就地改" in l]
if r01_70:
    conf.append({"id": "en_freeze", "a": "rules/01 图片节：%s" % r01_70[0].strip()[:70],
                 "b": "ADR-0062 决策 1：en/ 绝对冻结，任何变动禁止（rules/README 判例已改）"})
r04_126 = [l for l in rules04.splitlines() if "s2.5_checked 在途件不适用" in l]
if r04_126:
    conf.append({"id": "reopen_boundary",
                 "a": "rules/04 §上游更新引发的置空返工 边界：%s" % r04_126[0].strip()[:60],
                 "b": "ADR-0051 决策：R3 在途绕过含 s2.5_checked，边界一作废"})
if "force push" in r06 and "已裁定允许重写 git 记录" in r06 and "仍禁" in r06:
    conf.append({"id": "force_push",
                 "a": "rules/06 §历史改写与批次护栏：已裁定允许重写 git 记录（含 force push）",
                 "b": "rules/06 §多机并行 + rules/05 §提交策略：--force 仍禁（ADR-0059）"})
report["G_norm_conflicts"] = conf

json.dump(report, sys.stdout, ensure_ascii=False, indent=1)
sys.stdout.write("\n")

# 人读摘要（stderr）
w = sys.stderr
fails = []
if viol_target:
    fails.append("A 目标态越界 %d 例：%s" % (len(viol_target), viol_target[:3]))
if viol_pred:
    fails.append("A expect≠前驱 %d 例：%s" % (len(viol_pred), viol_pred[:3]))
for kind, v in lts.get("reach", {}).items():
    if v["unreachable"]:
        fails.append("A %s 不可达态：%s" % (kind, v["unreachable"]))
    if v["dead_ends"]:
        fails.append("A %s 死端：%s" % (kind, v["dead_ends"]))
if doc_missing:
    fails.append("A 文档缺态 %d 处" % len(doc_missing))
if gamma["rules05_ci_list_missing_vs_GATES"]:
    fails.append("B rules/05 CI 清单缺门禁：%s" % gamma["rules05_ci_list_missing_vs_GATES"])
if gamma["tools_unregistered_in_rules05"]:
    fails.append("B 未登记工具 %d 具：%s" % (len(gamma["tools_unregistered_in_rules05"]),
                  "、".join(gamma["tools_unregistered_in_rules05"])))
if adr["status_mismatch"]:
    fails.append("C 索引/正文状态不一致：%s" % adr["status_mismatch"])
if adr["dangling_refs"]:
    fails.append("C 悬空 ADR 引用：%s" % adr["dangling_refs"])
if miscites:
    fails.append("F ADR 语义错引 %d 处" % len(miscites))
if conf:
    fails.append("G 规范层冲突 %d 组：%s" % (len(conf), [c["id"] for c in conf]))
w.write("== 融洽性审计摘要 ==\n")
w.write("门禁 %d+1 单测（--all %d）；工具 %d 具（rules/05 表登记 %d）；ADR %d 件；引用 %d 个 ADR 号\n"
        % (len(GATES), gamma["count"]["with_all"], len(actual), len(table_tools),
           len(adr["files"]), len(refs)))
for f_ in fails:
    w.write("[!] %s\n" % f_)
if not fails:
    w.write("（无红灯面）\n")
return_code = 0
sys.exit(return_code)
