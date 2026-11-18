# -*- coding: utf-8 -*-
"""全系统融洽性审计计算器（specs/040；第二轮——修复后复算版）。

从权威实现（tools/task_ops.py、tools/check_all.py）与规范文本出发，计算六组
性质并输出机读报告与 stderr 人读摘要。第二轮要点：

  * A 组建模改为「合法前驱由 ORDER 单一事实源推导」后的实现（task_ops
    expected_prev），advance 边＝ORDER 相邻对；clear/reopen/revert 为命令边；
  * 修复落位 tripwire：F-01/02/03 的实现特征（expected_prev 存在、
    STEP_EXPECT_PREV 已删、audit 归一保留）作硬断言；
  * D/E/F/G 组的发现面全部转为 FAIL 旗标——第二轮期望全零。

用法: python specs/040-coherence-audit/bin/audit_coherence.py
输出: stderr 摘要；stdout JSON；报告另写 results/audit-report.json（LF）。
退出码: 恒 0（审计面，不是门禁；红灯面在 stderr 以 [!] 列出）。
"""
import glob
import io
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

if (getattr(sys.stdout, "encoding", "") or "").lower().replace("-", "") != "utf8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

from tools import task_ops as T  # noqa: E402
from tools.check_all import GATES, OPTIONAL  # noqa: E402

report = {"schema": "sep-cn-coherence-audit/2",
          "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
          "root": ROOT}


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


fails = []


def flag(cond, msg):
    if cond:
        fails.append(msg)


# ============ A. 任务状态机 LTS（新实现建模＋tripwire） ============
tosrc = read("tools/task_ops.py")
flag(re.search(r"^STEP_EXPECT_PREV\s*=", tosrc, re.M) is not None,
     "A tripwire：STEP_EXPECT_PREV 定义未删除（F-03 回潮）")
flag("def expected_prev" not in tosrc, "A tripwire：expected_prev 缺失（F-01/02 收口回潮）")
flag("不属于 %s 状态序列" % "%s" if False else "禁止跨 kind 推进" not in tosrc,
     "A tripwire：目标态越界守卫缺失（F-01 回潮）")
flag('if step == "audit":\n        step = "s25"' not in tosrc,
     "A tripwire：audit 别名归一缺失（s25 挂钩派发回潮）")
flag(T.STEPS.get("audit") != "s2.5_checked", "A tripwire：STEPS['audit'] 别名语义漂移")

lts = {"ORDER": {k: v for k, v in T.ORDER.items()},
       "STEPS": dict(T.STEPS)}
edges = []
viol = []
for kind, order in T.ORDER.items():
    # advance 边＝ORDER 相邻对（合法前驱唯一，F-01/F-02 收口后的实现语义）。
    # 目标态越界守卫在运行时由 expected_prev 承担（tripwire 见上）；clear/reopen
    # 等命令边目标（cleared/pending）不经 advance 步，属合法。
    for i in range(1, len(order)):
        step_key = next((s for s, tgt in T.STEPS.items() if tgt == order[i]), None)
        edges.append((kind, order[i - 1], step_key or ("cmd:" + order[i]), order[i]))
# 命令边
edges.append(("retranslate", "pending", "clear", "cleared"))
for s in [x for x in T.ORDER["retranslate"] if x not in ("pending", "cleared", "done")]:
    edges.append(("retranslate", s, "reopen--upstream-sync", "pending"))
edges.append(("retranslate", "done", "reopen", "pending"))
for s in ("s2.5_checked", "s3_checked", "r1_reviewed", "r2_reviewed", "r3_reviewed", "done"):
    edges.append(("retranslate", s, "revert-state", "s2.5_checked"))
    edges.append(("retranslate", s, "revert-state", "s2.4_termchecked"))
for kind, order in T.ORDER.items():
    reach, frontier = {order[0]}, [order[0]]
    while frontier:
        cur = frontier.pop()
        for k2, prev, _step, tgt in edges:
            if k2 == kind and prev == cur and tgt in order and tgt not in reach:
                reach.add(tgt)
                frontier.append(tgt)
    lts.setdefault("reach", {})[kind] = {
        "unreachable": [s for s in order if s not in reach],
        "dead_ends": [s for s in reach if s != order[-1]
                      and s not in {p for k3, p, _s, _t in edges if k3 == kind}]}
readme = read("tasks/README.md")
rules04 = read("rules/04-translation-workflow.md")
doc_missing = []
for kind, order in T.ORDER.items():
    for st in order:
        for label, text in (("tasks/README.md", readme), ("rules/04", rules04)):
            if st not in text:
                doc_missing.append({"kind": kind, "state": st, "doc": label})
lts.update({"viol": viol, "doc_state_missing": doc_missing})
flag(viol, "A LTS 违例 %d 例：%s" % (len(viol), viol[:3]))
for kind, v in lts["reach"].items():
    flag(v["unreachable"], "A %s 不可达态：%s" % (kind, v["unreachable"]))
    flag(v["dead_ends"], "A %s 死端：%s" % (kind, v["dead_ends"]))
flag(doc_missing, "A 文档缺态 %d 处" % len(doc_missing))
report["A_state_machine"] = lts

# ============ B. 门禁映射 Γ ============
gamma = {"gates": []}
rules05 = read("rules/05-ci-and-tools.md")
agents = read("AGENTS.md")
cli = read("specs/001-sep-sync-pipeline/contracts/cli.md")
for name, key, cmd in GATES:
    tool = cmd.split()[0].replace("tools/", "").replace(".py", "")
    row = {"key": key, "tool": tool + ".py",
           "in_rules05_tool_table": ("%s.py" % tool) in rules05,
           "in_cli": tool in cli, "in_agents": tool in agents}
    gamma["gates"].append(row)
    flag(not row["in_rules05_tool_table"], "B 门禁 %s 未登记于 rules/05 工具表" % key)
table_tools = set()
for line in rules05.splitlines():
    if line.lstrip().startswith("|"):
        table_tools.update(re.findall(r"`([a-z_0-9]+)\.py`", line))
actual = sorted(f[:-3] for f in os.listdir(os.path.join(ROOT, "tools"))
                if f.endswith(".py") and f not in ("__init__.py",))
gamma["tools_unregistered_in_rules05"] = [t for t in actual if t not in table_tools]
gamma["rules05_table_ghost"] = sorted(t for t in table_tools if t + ".py" not in
                                      [a + ".py" for a in actual])
gamma["count"] = {"gates": len(GATES), "plus_unittest": len(GATES) + 1,
                  "with_all": len(GATES) + 1 + len(OPTIONAL)}
flag(gamma["tools_unregistered_in_rules05"],
     "B 未登记工具 %d 具：%s" % (len(gamma["tools_unregistered_in_rules05"]),
                                gamma["tools_unregistered_in_rules05"]))
flag(gamma["rules05_table_ghost"], "B rules/05 表幽灵条目：%s" % gamma["rules05_table_ghost"])
# CI 矩阵清单段须含全部门禁工具（F-08）
ci_row = next((l for l in rules05.splitlines() if "`checks.yml`" in l and "矩阵" in l), "")
ci_tools = set(re.findall(r"([a-z_0-9]+)\.py", ci_row))
missing_in_ci = [t for (_n, k, c) in GATES
                 for t in [c.split()[0].replace("tools/", "").replace(".py", "")]
                 if t not in ci_tools]
gamma["rules05_ci_row_missing"] = missing_in_ci
flag(missing_in_ci, "B rules/05 CI 清单缺：%s" % missing_in_ci)
report["B_gamma"] = gamma

# ============ C. ADR 链 ============
adrdir = os.path.join(ROOT, "rules", "adr")
idx = read("rules/adr/README.md")
index_rows = re.findall(r"\|\s*\[(\d{4})\]\(([^)]+\.md)\)\s*\|\s*([^|]+)\|\s*([^|]+)\|", idx)
adr = {"index_count": len(index_rows),
       "index_status": {n: s.strip() for n, _f, _t, s in index_rows},
       "files": sorted(f for f in os.listdir(adrdir) if re.match(r"^\d{4}", f))}
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
        fst = m.group(1).lower()
        idx_st = adr["index_status"][n].split("（")[0].split("；")[0].strip().lower()
        if fst != idx_st:
            status_mismatch.append({"adr": n, "index": adr["index_status"][n],
                                    "file": m.group(0)[:50]})
adr["status_mismatch"] = status_mismatch
flag(status_mismatch, "C 索引/正文状态不一致：%s" % status_mismatch)
flag(adr["numbering_gap"], "C 编号缺口：%s" % adr["numbering_gap"])
flag(adr["dangling_index_file"], "C 索引悬空文件：%s" % adr["dangling_index_file"])
ref_sites = ["AGENTS.md", "tasks/README.md",
             "specs/001-sep-sync-pipeline/contracts/cli.md"]
ref_sites += ["rules/" + f for f in sorted(os.listdir(os.path.join(ROOT, "rules")))
              if f.endswith(".md")]
ref_sites += ["tools/" + f + ".py" for f in actual]
refs = {}
for site in ref_sites:
    try:
        text = read(site)
    except OSError:
        continue
    for m in re.finditer(r"ADR[- ]?(\d{4})", text):
        refs.setdefault(m.group(1), set()).add(site)
existing = {f[:4] for f in adr["files"]}
adr["referenced_n"] = len(refs)
adr["dangling_refs"] = {n: sorted(s) for n, s in refs.items() if n not in existing}
flag(adr["dangling_refs"], "C 悬空 ADR 引用：%s" % adr["dangling_refs"])
sup = []
for f in adr["files"]:
    text = read(os.path.join("rules", "adr", f))
    for m in re.finditer(r"(取代|修订|作废|部分被取代)[^。\n]{0,60}?(\d{4})", text):
        sup.append({"adr": f[:4], "relation": m.group(1), "other": m.group(2)})
adr["supersede_mentions_n"] = len(sup)
report["C_adr_chain"] = adr

# ============ D. 文档声称 vs 数据事实（FAIL 旗标化） ============
claims = {}
stale_counts = []
for site in ("AGENTS.md", "rules/05-ci-and-tools.md", "rules/06-governance.md",
             "rules/09-process-standard.md"):
    text = read(site)
    for pat in ("九项门禁", "十项门禁", "共 10 项", "check_all 10 项", "10 项与单元测试"):
        if pat in text:
            stale_counts.append("%s 含「%s」" % (site, pat))
claims["gate_count_stale"] = stale_counts
claims["gate_count_actual"] = gamma["count"]
flag(stale_counts, "D 门禁计数过时 %d 处：%s" % (len(stale_counts), stale_counts))
r01 = read("rules/01-repository-structure.md")
m = re.search(r"当前最大\s*(rules/\d+[^，。\s]*)\s*(\d+)\s*行", r01)
real = {}
for f in sorted(os.listdir(os.path.join(ROOT, "rules"))):
    if re.match(r"^0\d.*\.md$", f):
        with open(os.path.join(ROOT, "rules", f), encoding="utf-8") as fh:
            real["rules/" + f] = sum(1 for _ in fh)
mx = max(real, key=real.get)
if m:
    claimed_file, claimed_n = m.group(1), int(m.group(2))
    actual_hit = next((k for k in real if k.startswith(claimed_file)), None)
    ok = actual_hit is not None and claimed_n == real[actual_hit]
    claims["rules_line_claim"] = {"claimed": "%s %s 行" % (claimed_file, claimed_n),
                                  "actual_max": "%s %d 行" % (mx, real[mx]), "ok": ok}
    flag(not ok, "D rules/01 行数声称失实：%s %s ≠ 实际 %s %d"
         % (claimed_file, claimed_n, actual_hit or "?", real[actual_hit] if actual_hit else -1))
flag("仅 s3_checked 及其后" in readme, "D tasks/README revert 口径滞后（F-04）")
flag("仅 s3_checked 及其后" in cli, "D cli.md revert 口径滞后（F-04）")
flag("s2.4_termchecked（仅变更段）" in readme, "D tasks/README update s2.4 作用域失真（F-05）")
tosrc2 = tosrc
flag("check_style（specs/028 O1" not in cli, "D cli.md s25 挂钩缺 check_style（F-06）")
flag("check_math_zh --strict＋check_style" not in rules04 and
     "与 `check_style`（specs/028 O1" not in rules04,
     "D rules/04 s25 挂钩缺 check_style（F-06）")


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
    nf = len([f for f in os.listdir(os.path.join(ROOT, "baseline", "en-patches"))
              if f.endswith(".patch")])
    claims["en_patches"] = {"index_count": idxp.get("count"), "files": nf}
    flag(idxp.get("count") != nf, "D 补丁池 INDEX 与正本不一致")
except OSError:
    claims["en_patches"] = "missing"
errata = read("specs/001-sep-sync-pipeline/results/en-errata.md")
body8 = errata[errata.find("## 八、"):]
claims["errata_sec8plus_rows"] = len([
    l for l in body8.splitlines() if l.startswith("|")
    and len(l.strip("|").split("|")) == 7
    and l.strip("|").split("|")[0].strip() not in ("", "slug")
    and not set(l.strip("|").split("|")[0].strip()) <= set("- ")])
done_n, pin_ok_n = 0, 0
for fp in glob.glob(os.path.join(ROOT, "tasks", "*", "*.json")):
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

# ============ E. 陈旧面扫描（FAIL 旗标化） ============
stale = {}
hits = []
for f in actual:
    text = read("tools/" + f + ".py")
    if "en-patches.json" in text:
        hits.append("tools/%s.py 仍写 en-patches.json（F-15）" % f)
    if f == "sync_guard" and "收工时必须" in text:
        hits.append("tools/sync_guard.py 仍载积压线文案（F-16）")
    if f == "check_render_artifacts" and "待登记" in text[:600]:
        hits.append("tools/check_render_artifacts.py 仍写待登记（F-17）")
    if f == "compose_from_ledger" and "已废弃" not in text[:200]:
        hits.append("tools/compose_from_ledger.py 缺废弃标注（F-25）")
    if f == "rebuild_dir" and "词条目录形态：仓库根 <slug>/index.md" in text:
        hits.append("tools/rebuild_dir.py docstring 仍载旧目录形态（F-26）")
    if f == "check_junk" and len(re.findall(r"^\s*'node_modules'", text, re.M)) > 1:
        hits.append("tools/check_junk.py node_modules 重复键（F-29）")
for site, pat, fid in (("rules/01-repository-structure.md", "四类勘误可就地改", "F-20"),
                       ("rules/04-translation-workflow.md", "经派工单 A2 以", "F-21"),
                       ("rules/06-governance.md", "一律 `git commit --no-gpg-sign`", "F-22")):
    if pat in read(site):
        hits.append("%s 仍含「%s」（%s）" % (site, pat, fid))
stale["hits"] = hits
flag(hits, "E 陈旧面 %d 处：%s" % (len(hits), hits[:4]))
report["E_stale_faces"] = stale

# ============ F. ADR 语义错引（FAIL 旗标化） ============
miscites = []
if "ADR-0057" in read("tools/check_academic.py"):
    miscites.append("check_academic.py 引 ADR-0057（应为 0058，F-12）")
if "ADR-0036" in read("tools/check_tables_images.py"):
    miscites.append("check_tables_images.py 引 ADR-0036（应为 0037，F-12）")
flag(miscites, "F ADR 语义错引 %d 处" % len(miscites))
report["F_adr_miscites"] = miscites

# ============ G. 规范层 O/F 冲突（FAIL 旗标化） ============
conf = []
r06 = read("rules/06-governance.md")
r03 = read("rules/03-terminology.md")
if "dict.cnki.net" in r03 and "不再新增查询" not in r03.split("## 译名依据优先级")[1].split("##")[0]:
    conf.append("rules/03 优先级节未标注 CNKI/术语在线冻结（F-19）")
if "四类勘误可就地改" in r01:
    conf.append("rules/01 仍载就地改正线（F-20）")
if "s2.5_checked 在途件不适用" in rules04:
    conf.append("rules/04 仍载已作废 reopen 边界一（F-21）")
if "一律 `git commit --no-gpg-sign`" in r06:
    conf.append("rules/06 GPG 口径未归一（F-22）")
if "含 force push）" in r06 and "授权期" not in r06.split("历史改写与批次护栏")[1].split("\n*")[0]:
    conf.append("rules/06 force push 未标授权期边界（F-23）")
flag(conf, "G 规范层冲突 %d 组：%s" % (len(conf), conf))
report["G_norm_conflicts"] = conf

# 报告落盘（LF）＋stdout 摘要 JSON
out_path = os.path.join(HERE, "..", "results", "audit-report.json")
with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    json.dump(report, f, ensure_ascii=False, indent=1)
    f.write("\n")
report["fails"] = fails
json.dump(report, sys.stdout, ensure_ascii=False, indent=1)
sys.stdout.write("\n")

w = sys.stderr
w.write("== 融洽性审计（第二轮复算）==\n")
w.write("门禁 %d+1 单测（--all %d）；工具 %d 具（rules/05 表登记 %d）；ADR %d 件；引用 %d 个 ADR 号\n"
        % (len(GATES), gamma["count"]["with_all"], len(actual), len(table_tools),
           len(adr["files"]), len(refs)))
if fails:
    for f_ in fails:
        w.write("[!] %s\n" % f_)
else:
    w.write("（无红灯面：A–G 全部性质通过）\n")
sys.exit(0)
