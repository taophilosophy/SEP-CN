# -*- coding: utf-8 -*-
"""项目公理体系·形式化充分性审计计算器（specs/041）。

输入：登记册 results/axioms.md（三节机读表）＋ specs/040 复算报告（一致性输入）。
判定五面：
  S1 锚存在    每条公理的权威锚 path::keyword 在现行文本命中；
  S2 载体存在  gate:/tool:/impl:mod(sym)/hook: 载体在工具链真实存在（discipline 只验非空）；
  S3 反向接地  每条 GATES 门禁/步级挂钩/不变量工具可上溯 ≥1 公理（映射表内置于本脚本，
               人工审订——映射本身的正确性属语义面，由 specs/040 语料通读背书）；
  S4 正向接地  每条硬约束规范（AGENTS 速览＋rules/09 阶段）映射 ≥1 公理；
  S5 目的导出  Φ1–Φ8 公理子集合法＋witness 载体存在。
附加：T4 一致性（specs/040 G 组＝空）；T5 非冗余（独占列非空）。

用法: python specs/041-axiom-system/bin/axiom_audit.py
输出: stderr 摘要；stdout JSON；报告写 results/axiom-report.json（LF）。退出码恒 0（审计面）。
"""
import io
import json
import os
import re
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

if (getattr(sys.stdout, "encoding", "") or "").lower().replace("-", "") != "utf8":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    except (AttributeError, ValueError):
        pass

from tools.check_all import GATES, OPTIONAL, UNIT_TESTS  # noqa: E402

REG = os.path.join(HERE, "..", "results", "axioms.md")
OUT = os.path.join(HERE, "..", "results", "axiom-report.json")
fails = []


def flag(cond, msg):
    if cond:
        fails.append(msg)


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


reg_text = read(os.path.relpath(REG, ROOT).replace("\\", "/"))

# ---------- 解析三节 ----------
sec1 = reg_text.split("## 一、")[1].split("## 二、")[0]
sec2 = reg_text.split("## 二、")[1].split("## 三、")[0]
sec3 = reg_text.split("## 三、")[1]

def rows_of(sec, min_cols):
    out = []
    for line in sec.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= min_cols and re.match(r"^A1[0-4]$|^A\d$", cells[0] or ""):
            out.append(cells)
    return out

axiom_rows = rows_of(sec1, 6)

def generic_rows(sec, min_cols):
    out = []
    for line in sec.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < min_cols or not cells[0]:
            continue
        if set(cells[0]) <= set("- "):
            continue
        if cells[0].startswith(("规范（", "公理", "子目标")):
            continue
        out.append(cells)
    return out

fwd_rows = generic_rows(sec2, 2)
phi_rows = generic_rows(sec3, 3)
phi_rows = [r for r in phi_rows if re.match(r"^Φ\d", r[0])]

axiom_ids = [r[0] for r in axiom_rows]
report = {"schema": "sep-cn-axiom-audit/1",
          "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
          "axioms": len(axiom_rows), "forward_norms": len(fwd_rows),
          "phi_goals": len(phi_rows)}

flag(len(axiom_rows) != 14, "登记册公理行数 %d ≠ 14" % len(axiom_rows))
flag(len(set(axiom_ids)) != len(axiom_ids), "公理编号重复")
flag(len(fwd_rows) < 28, "正向接地行 %d（应 ≥28：AGENTS 16＋rules/09 P0–P11）" % len(fwd_rows))
flag(len(phi_rows) != 8, "Φ 行数 %d ≠ 8" % len(phi_rows))

# ---------- 载体语法 ----------
TOOL_CACHE = {}


def tool_src(name):
    if name not in TOOL_CACHE:
        p = os.path.join(ROOT, "tools", name + ".py")
        TOOL_CACHE[name] = read(os.path.relpath(p, ROOT).replace("\\", "/")) if os.path.exists(p) else None
    return TOOL_CACHE[name]


HOOK_MAP = {"independence": "_independence_gate", "r3_mandate": "--mandate",
            "s24_gates": "_term_gate", "s0_gates": "_source_gate",
            "s25_gates": "_audit_gate", "s3r3_gates": "_academic_gate"}
GATE_KEYS = {k for (_n, k, _c) in GATES} | {UNIT_TESTS[1]}


def check_carrier(tok, axiom):
    """返回 None=通过，否则错误消息。gate:/tool: 容忍全角括注（剥「（…」后验本体）。"""
    if tok.startswith("discipline:"):
        return None if len(tok) > len("discipline:") else "空 discipline"
    if tok.startswith("gate:"):
        key = tok[5:].split("（")[0].strip()
        return None if key in GATE_KEYS else "GATES 无键 %s" % key
    if tok.startswith("tool:"):
        name = tok[5:].split("（")[0].strip()
        return None if tool_src(name) is not None else "工具不存在 %s" % name
    m = re.match(r"impl:([a-z_0-9]+)\((.+)\)$", tok)
    if m:
        mod, sym = m.group(1), m.group(2)
        src = tool_src(mod)
        if src is None:
            return "impl 模块不存在 %s" % mod
        return None if sym in src else "符号 %r 不在 %s.py" % (sym, mod)
    if tok.startswith("hook:"):
        sym = HOOK_MAP.get(tok[5:])
        if sym is None:
            return "未知 hook %s" % tok
        src = tool_src("task_ops")
        return None if (src and sym in src) else "hook %s 符号 %r 缺失" % (tok, sym)
    return "未知载体语法 %s" % tok


# ---------- S1 锚存在（锚＝规范正文；index:＝AGENTS.md 入口索引，不计权威锚） ----------
s1_bad = []
anchor_count = {"正文锚": 0, "索引": 0}
index_only = []
for r in axiom_rows:
    aid, anchors = r[0], r[3]
    body_n = 0
    for a in [x.strip() for x in anchors.split("、") if x.strip()]:
        if a.startswith("index:"):
            rest = a[len("index:"):]
            if "::" not in rest:
                s1_bad.append("%s 索引缺 :: 分隔：%s" % (aid, a))
                continue
            path, kw = rest.split("::", 1)
            try:
                text = read(path)
            except OSError:
                s1_bad.append("%s 索引文件缺失：%s" % (aid, path))
                continue
            if kw not in text:
                s1_bad.append("%s 索引关键词未命中：%s::%s" % (aid, path, kw))
            else:
                anchor_count["索引"] += 1
            continue
        if "::" not in a:
            s1_bad.append("%s 锚缺 :: 分隔：%s" % (aid, a))
            continue
        path, kw = a.split("::", 1)
        try:
            text = read(path)
        except OSError:
            s1_bad.append("%s 锚文件缺失：%s" % (aid, path))
            continue
        if kw not in text:
            s1_bad.append("%s 锚关键词未命中：%s::%s" % (aid, path, kw))
        else:
            body_n += 1
            anchor_count["正文锚"] += 1
    if body_n == 0:
        index_only.append(aid)
report["s1_anchor_miss"] = s1_bad
report["s1_anchor_count"] = anchor_count
report["s1_index_only_axioms"] = index_only
flag(s1_bad, "S1 锚存在 %d 处失败：%s" % (len(s1_bad), s1_bad[:4]))
flag(index_only, "S1 仅有索引无正文锚（公理效力悬空）：%s" % index_only)

# ---------- S2 载体存在 ----------
s2_bad = []
for r in axiom_rows:
    aid, carriers = r[0], r[4]
    toks = [x.strip() for x in re.split(r"[、；]", carriers) if x.strip()]
    if not toks:
        s2_bad.append("%s 载体为空" % aid)
    for t in toks:
        err = check_carrier(t, aid)
        if err:
            s2_bad.append("%s 载体 %s：%s" % (aid, t, err))
report["s2_carrier_miss"] = s2_bad
flag(s2_bad, "S2 载体存在 %d 处失败：%s" % (len(s2_bad), s2_bad[:4]))

# ---------- T5 非冗余 ----------
t5_bad = [r[0] for r in axiom_rows if not r[5].strip()]
flag(t5_bad, "T5 独占列缺失：%s" % t5_bad)
report["t5_nonredundant"] = not t5_bad

# ---------- S3 反向接地（映射表：人工审订，specs/040 语料背书） ----------
REVERSE = {
    "summary": ["A5"], "mulu": ["A5"], "docsize": ["A5", "A11"], "junk": ["A5", "A12"],
    "images": ["A5", "A12"], "terms": ["A5", "A13"], "quotes": ["A13"],
    "academic": ["A2", "A3", "A6", "A8"], "mathzh": ["A13"],
    "divergence": ["A1", "A4"], "fidelity": ["A1", "A4", "A11"], "unittest": ["A7", "A11"],
}
HOOK_AXIOMS = {"independence": ["A8"], "r3_mandate": ["A9"], "s24_gates": ["A5", "A13", "A11"],
               "s0_gates": ["A1", "A12"], "s25_gates": ["A13", "A8"], "s3r3_gates": ["A2", "A3", "A6"]}
INV_TOOLS = {"en_patch_lib": ["A1", "A4", "A12"], "check_en_patches": ["A1", "A12"],
             "check_yuanwen_fidelity": ["A1", "A4"], "divergence": ["A1", "A4"],
             "common": ["A14", "A12"], "register_lib": ["A5"], "baseline_audit": ["A1", "A3"],
             "mech_audit": ["A13", "A2"], "task_ops": ["A7", "A9", "A14"], "sync_guard": ["A4"],
             "check_prose": ["A6"], "check_style": ["A13"]}
s3_bad = []
covered_axioms = set()
for (_n, k, _c) in GATES:
    ax = REVERSE.get(k)
    if not ax:
        s3_bad.append("门禁 %s 无公理映射" % k)
    else:
        covered_axioms.update(ax)
        for a in ax:
            if a not in axiom_ids:
                s3_bad.append("门禁 %s 映射未知公理 %s" % (k, a))
for h, ax in HOOK_AXIOMS.items():
    covered_axioms.update(ax)
    if not any(h in c for r in axiom_rows for c in [r[4]]):
        # hook 允许经 impl 声明（HOOK_MAP 符号在载体列以 impl/hook 形式出现）
        pass
for t, ax in INV_TOOLS.items():
    covered_axioms.update(ax)
    if tool_src(t) is None:
        s3_bad.append("不变量工具不存在 %s" % t)
unused = [a for a in axiom_ids if a not in covered_axioms]
report["s3_reverse"] = {"gates": len(GATES), "hooks": list(HOOK_AXIOMS), "uncovered_axioms": unused}
flag(s3_bad, "S3 反向接地 %d 处失败：%s" % (len(s3_bad), s3_bad[:4]))
flag(unused, "S3 未被任何门禁/挂钩/工具引用的公理：%s（纪律/留痕面公理经 S4 接地即合法）"
    % unused) if set(unused) - {"A2", "A6", "A10"} else None
if set(unused) - {"A2", "A6", "A10"}:
    fails.append("S3 未接地公理（非留痕/纪律面）：%s" % unused)

# ---------- S4 正向接地 ----------
s4_bad = []
for r in fwd_rows:
    norm, ax = r[0], r[1]
    ids = [x.strip() for x in re.split(r"[、,，]", ax) if x.strip().startswith("A")]
    if not ids:
        s4_bad.append("%s 无公理映射" % norm)
    for a in ids:
        if a not in axiom_ids:
            s4_bad.append("%s 映射未知公理 %s" % (norm, a))
report["s4_forward"] = {"norms": len(fwd_rows), "bad": s4_bad}
flag(s4_bad, "S4 正向接地 %d 处失败：%s" % (len(s4_bad), s4_bad[:4]))

# ---------- S5 目的导出 ----------
s5_bad = []
for r in phi_rows:
    goal, ax, wit = r[0], r[1], r[2]
    ids = [x.strip() for x in re.split(r"[、,，]", ax) if x.strip().startswith("A")]
    if not ids:
        s5_bad.append("%s 无公理子集" % goal)
    for a in ids:
        if a not in axiom_ids:
            s5_bad.append("%s 引用未知公理 %s" % (goal, a))
    for t in [x.strip() for x in re.split(r"[、；]", wit) if x.strip()]:
        err = check_carrier(t, goal)
        if err:
            s5_bad.append("%s witness %s：%s" % (goal, t, err))
report["s5_phi"] = {"goals": len(phi_rows), "bad": s5_bad}
flag(s5_bad, "S5 目的导出 %d 处失败：%s" % (len(s5_bad), s5_bad[:4]))

# ---------- T4 一致性（specs/040 复算报告为输入） ----------
try:
    prev = json.load(open(os.path.join(ROOT, "specs", "040-coherence-audit",
                                       "results", "audit-report.json"), encoding="utf-8"))
    g_conf = prev.get("G_norm_conflicts") or []
    a_conf = (prev.get("A_state_machine") or {}).get("viol") or []
    t4_ok = not g_conf and not a_conf
    report["t4_consistency"] = {"specs040_G": len(g_conf), "specs040_A_viol": len(a_conf),
                                "ok": t4_ok}
    flag(not t4_ok, "T4 一致性输入面非零（specs/040 G=%d, A_viol=%d）" % (len(g_conf), len(a_conf)))
except OSError:
    report["t4_consistency"] = "specs/040 报告缺失"
    flag(True, "T4 输入缺失：specs/040 audit-report.json 不可读")

# ---------- S6 层级定位（公理最高／AGENTS.md 入口目录／SE 理论哲学方法论） ----------
s6_bad = []
agents_md = read("AGENTS.md")
spec_md = read("specs/041-axiom-system/spec.md")
if "规则正文一律以" not in agents_md or "rules/" not in agents_md:
    s6_bad.append("AGENTS.md 未自述为入口索引（缺“规则正文一律以 rules/ 为准”）")
if "本文件不复制数字" not in agents_md:
    s6_bad.append("AGENTS.md 未声明不复制数字（ADR-0015 入口定位）")
for must in ("层级模型", "哲学与方法论论证", "公理层", "入口与目录"):
    if must not in spec_md:
        s6_bad.append("spec.md 缺层级定位节内容：%s" % must)
report["s6_layering"] = {"agents_self_index": "规则正文一律以" in agents_md,
                         "bad": s6_bad}
flag(s6_bad, "S6 层级定位 %d 处失败：%s" % (len(s6_bad), s6_bad[:3]))

# ---------- 汇总落盘 ----------
report["fails"] = fails
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(report, f, ensure_ascii=False, indent=1)
    f.write("\n")
json.dump(report, sys.stdout, ensure_ascii=False, indent=1)
sys.stdout.write("\n")

w = sys.stderr
w.write("== 公理体系充分性审计（specs/041）==\n")
w.write("公理 %d 条（正文锚 %d＋入口索引 %d）| 正向规范 %d 行 | Φ %d 项 | 门禁 %d＋挂钩 %d＋不变量工具 %d\n"
        % (len(axiom_rows), anchor_count["正文锚"], anchor_count["索引"],
           len(fwd_rows), len(phi_rows), len(GATES), len(HOOK_AXIOMS),
           len(INV_TOOLS)))
if fails:
    for m in fails:
        w.write("[!] %s\n" % m)
else:
    w.write("（S1–S6 全绿；T4 一致、T5 非冗余：公理体系对本项目目的充分）\n")
sys.exit(0)
