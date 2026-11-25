# -*- coding: utf-8 -*-
"""管线判据登记表核对（ADR-0068：rules/pipeline.json 为判据唯一事实源）。

七谓词（全部只读，A11 判官只读）：
  S1 链闭合   prev 链首/链尾唯一、无环、无悬挂、覆盖全部节点
  S2 判据唯一 每个判据至多一个硬拦节点（gate_owner），且与 criteria_owner 双向一致
  S3 强制集   mandatory_minimum 是节点子集，且含 sg-01/sg-02/sg-03（原 R1–R3）
  S4 类型值域  type ∈ {pipe,stage,review,format}；review 必须属强制集
  S5 承载体   判据承载体可解析；硬拦判据不由告警级承载
  S6 对象域   判据对象域登记；节点 object_class 覆盖其判据域
  S7 命名词表 rules/naming.json 自洽、与 pipeline 一一对应、号段与 seg 一致、
              历史 journal 节点值与任务状态名均可经别名归一（ADR-0080）

用法: python tools/check_stages.py [--json]
退出码: 0 全绿；1 有违例；2 输入缺失（A12 禁静默兜底）。
"""
import argparse
import io
import json
import os
import sys

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPE = os.path.join(ROOT, "rules", "pipeline.json")
TYPES = {"pipe", "stage", "review", "format"}
SIGNOFF = frozenset(("sg-01", "sg-02", "sg-03"))
SEG_PREFIX = {"seg1": ("ex",), "seg2": ("tr",), "seg3": ("rv", "sg")}


def load_pipeline(path=PIPE):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def _journal_node_values():
    """journal 中出现过的全部 node 值（只读；S7 用于验证别名可解析）。"""
    vals = set()
    jdir = os.path.join(ROOT, "journal")
    for dirpath, _, files in os.walk(jdir):
        for fn in files:
            if not fn.endswith(".ndjson"):
                continue
            try:
                with open(os.path.join(dirpath, fn), encoding="utf-8") as fh:
                    for line in fh:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            ev = json.loads(line)
                        except ValueError:
                            continue
                        if ev.get("node"):
                            vals.add(ev["node"])
            except OSError:
                continue
    return vals


def _task_state_values():
    """tasks/ 中词条任务（kind=retranslate）出现过的 state 值（S7 用）。

    词汇表维护与每日例行检查等非词条任务有自己的状态词（如 checked），不属管线
    状态机（ADR-0068 只覆盖 retranslate），故不纳入。
    """
    vals = set()
    tdir = os.path.join(ROOT, "tasks")
    for dirpath, _, files in os.walk(tdir):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            try:
                with open(os.path.join(dirpath, fn), encoding="utf-8") as fh:
                    t = json.load(fh)
            except (OSError, ValueError):
                continue
            if isinstance(t, dict) and t.get("state") \
                    and str(t.get("kind") or "") == "retranslate":
                vals.add(t["state"])
    return vals


def check(pipe, naming_path=None, journal_nodes=None, task_states=None):
    """纯函数：对 pipeline dict 求值，返回 hits 列表。

    S7 默认读 rules/naming.json 与磁盘 journal/tasks；单测可注入 naming_path／
    journal_nodes／task_states 以免依赖工作区现状。
    """
    nodes = pipe.get("nodes", [])
    by = {n["id"]: n for n in nodes}
    ids = set(by)
    mand = set(pipe.get("mandatory_minimum", {}).get("nodes", []))
    owner = {k: v for k, v in pipe.get("criteria_owner", {}).items() if k != "note"}

    hits = []

    def rec(code, name, ok, detail=""):
        hits.append({"code": code, "name": name, "ok": bool(ok), "detail": detail})

    # ---- S1 链闭合 ----
    heads = [i for i in by if not by[i].get("prev")]
    tails = [i for i in by if i not in {n.get("prev") for n in nodes}]
    rec("S1", "链首唯一", len(heads) == 1, "链首=%s" % heads)
    rec("S1", "链尾唯一", len(tails) == 1, "链尾=%s" % tails)

    cyc = []
    for start in by:
        path, cur = [], start
        while cur and cur not in path:
            path.append(cur)
            cur = by.get(cur, {}).get("prev")
        if cur:
            cyc.append(path)
    rec("S1", "无环", not cyc, "环=%s" % (cyc[:2] if cyc else "无"))

    dangling = [n["id"] for n in nodes if n.get("prev") and n["prev"] not in ids]
    rec("S1", "prev 无悬挂", not dangling, "悬挂=%s" % (dangling or "无"))

    # ---- S2 判据唯一 ----
    hard = {}
    for n in nodes:
        if n.get("gate_owner"):
            for g in n.get("criteria", []):
                hard.setdefault(g, []).append(n["id"])
    multi = {g: v for g, v in hard.items() if len(v) > 1}
    rec("S2", "判据硬拦唯一", not multi, "多挂=%s" % (multi or "无"))

    unreg, back = [], []
    for n in nodes:
        if not n.get("gate_owner"):
            continue
        for g in n.get("criteria", []):
            if g not in owner or n["id"] not in owner[g]:
                unreg.append("%s:%s" % (n["id"], g))
    for g, ns in owner.items():
        for nid in ns:
            if nid not in by or g not in by[nid].get("criteria", []):
                back.append("%s->%s" % (g, nid))
    rec("S2", "硬拦判据已登记", not unreg, "未登记=%s" % (unreg or "无"))
    rec("S2", "登记表反向完备", not back, "悬挂=%s" % (back or "无"))

    # ---- S3 强制集 ----
    rec("S3", "强制集是节点子集", mand <= ids, "越界=%s" % sorted(mand - ids))
    rec("S3", "终审三节点在强制集内", SIGNOFF <= mand,
        "差集=%s" % sorted(SIGNOFF - mand))

    # ---- S4 类型值域 ----
    badtype = [n["id"] for n in nodes if n.get("type") not in TYPES]
    rec("S4", "type 值域合法", not badtype, "非法=%s" % (badtype or "无"))
    lax = [n["id"] for n in nodes if n.get("type") == "review" and n["id"] not in mand]
    rec("S4", "review 必属强制", not lax, "非强制=%s" % (lax or "无"))

    # ---- S5 判据承载体（2026-11-18 补：判据名 ≠ 工具名的情形须显式登记）----
    # 动机：`errata_check` 曾是 check_pairs 的一个轴、`markdownlint` 是 CI 外部工具、
    # `ci_all` 是聚合门禁——三者都不存在同名 tools/*.py，S2 却只查"登记双向一致"，
    # 于是"登记完备"与"有真实承载体"被混为一谈，判据可悬空登记而全绿通过。
    carriers = {k: v for k, v in pipe.get("criteria_carrier", {}).items() if k != "note"}

    def _carrier_ok(name):
        """返回 (resolved, detail)：承载体能否落到真实文件/规则。"""
        c = carriers.get(name)
        if c is None:
            # 缺省承载体＝同名本地工具
            path = os.path.join(ROOT, "tools", "%s.py" % name)
            return (os.path.exists(path),
                    "tools/%s.py%s" % (name, "" if os.path.exists(path) else "（不存在）"))
        kind = c.get("kind")
        if kind == "axis":
            host = c.get("of")
            path = os.path.join(ROOT, "tools", "%s.py" % host)
            if not os.path.exists(path):
                return (False, "轴宿主 tools/%s.py 不存在" % host)
            # 规则名须真出现在宿主源码里（防"登记了一个不存在的轴"）
            try:
                with open(path, encoding="utf-8") as fh:
                    src = fh.read()
            except OSError:
                return (False, "轴宿主不可读")
            rule = c.get("rule") or ""
            return (bool(rule) and rule in src,
                    "%s#%s%s" % (host, rule, "" if rule in src else "（宿主内无此规则）"))
        if kind == "external":
            cfg = c.get("config")
            wf = c.get("workflow")
            miss = [x for x in (cfg, wf) if x and not os.path.exists(os.path.join(ROOT, x))]
            return (not miss, "external:%s%s" % (cfg or wf,
                                                 "" if not miss else "（缺 %s）" % ",".join(miss)))
        if kind == "manual":
            # 人工审核判据：无工具承载体，凭据为签字（ADR-0079 S6 补登记）
            return True, "manual:%s" % (c.get("note") or "")
        if kind == "aggregate":
            host = c.get("of")
            path = os.path.join(ROOT, "tools", "%s.py" % host)
            return (os.path.exists(path), "aggregate:%s" % host)
        return (False, "未知 carrier kind=%s" % kind)

    dangling_carrier = []
    for g in sorted(owner):
        ok, detail = _carrier_ok(g)
        if not ok:
            dangling_carrier.append("%s->%s" % (g, detail))
    rec("S5", "判据承载体可解析", not dangling_carrier,
        "悬挂=%s" % (dangling_carrier or "无"))

    # 硬拦级判据不得由告警级承载体承担（"声明硬拦、实际不拦"）
    level_bad = []
    hard_gates = {g for n in nodes if n.get("gate_owner") for g in n.get("criteria", [])}
    for g in sorted(hard_gates):
        c = carriers.get(g)
        lvl = (c or {}).get("level", "hard")
        if lvl != "hard":
            level_bad.append("%s（硬拦位，承载体 level=%s）" % (g, lvl))
    rec("S5", "硬拦判据不由告警级承载", not level_bad, "不符=%s" % (level_bad or "无"))

    # ---- S6 对象域双登记（ADR-0079 补记，2026-11-25 用户批准）----
    domains = {k: v for k, v in pipe.get("criteria_domain", {}).items()
               if k != "note"}
    undeclared = [g for g in sorted(owner) if g not in domains]
    rec("S6", "判据对象域已登记", not undeclared,
        "未登记=%s" % (undeclared or "无"))

    class_bad, overload = [], []
    for n in nodes:
        crit = [g for g in n.get("criteria", []) if g]
        if not crit:
            continue
        oc = n.get("object_class")
        if len(crit) > 1 and not oc:
            class_bad.append("%s：多判据未声明 object_class" % n["id"])
            continue
        ocs = set(oc if isinstance(oc, list) else [oc]) if oc else set()
        miss = [g for g in crit if domains.get(g) not in ocs]
        if miss:
            class_bad.append("%s：%s 的 domain 不在 object_class %s"
                             % (n["id"], ",".join(miss), sorted(ocs)))
        if len(ocs) > 3:
            overload.append("%s=%d" % (n["id"], len(ocs)))
    rec("S6", "节点对象类覆盖判据域", not class_bad,
        "不符=%s" % (class_bad or "无"))
    rec("S6", "节点对象类未过载（提示，≤3）", True,
        "过载=%s" % (overload or "无"))

    # ---- S7 命名词表（ADR-0080：identifier／name／state 三层分离）----
    # 动机：旧命名把标识与名称压成一个字符串（s2.4、global、S3），于是“改语义名”等于
    # “改标识”，历史 journal（只追加，P5）就成了改名的锁死项。三层分离后改名只动
    # name／label。本谓词是分离不被悄悄放弃的哨兵：登记表缺项、号段越界、
    # 历史节点名解析不了、状态名游离在别名表外，一律红。
    try:
        from tools import naming_lib
    except ImportError:  # 直连脚本运行（无包路径）
        sys.path.insert(0, ROOT)
        from tools import naming_lib
    npath = naming_path or naming_lib.REGISTRY_PATH
    try:
        reg = naming_lib.load(npath)
        v_errs = naming_lib.validate(npath)
    except (RuntimeError, ValueError, OSError) as exc:
        rec("S7", "登记表自洽", False, "rules/naming.json 不可读：%s" % exc)
        return hits
    rec("S7", "登记表自洽", not v_errs, "违例=%s" % (v_errs[:4] or "无"))

    reg_ids = [n["identifier"] for n in reg.get("nodes", [])]
    missing = sorted(set(ids) - set(reg_ids))
    extra = sorted(set(reg_ids) - set(ids))
    rec("S7", "登记表与管线一一对应", not missing and not extra,
        "未登记=%s；无对应节点=%s" % (missing or "无", extra or "无"))

    seg_bad = []
    for n in nodes:
        nid = n["id"]
        if "-" not in nid:
            seg_bad.append("%s：非 identifier 形态" % nid)
            continue
        prefix = nid.split("-")[0]
        allow = SEG_PREFIX.get(n.get("seg") or "", ())
        if allow and prefix not in allow:
            seg_bad.append("%s：号段 %s 与 seg %s 不符" % (nid, prefix, n.get("seg")))
    rec("S7", "号段与管线段一致", not seg_bad, "不符=%s" % (seg_bad or "无"))

    dup = [n["id"] for n in nodes if "label" in n or "name" in n]
    rec("S7", "命名属性不在管线重复", not dup,
        "重复=%s（label／name 归 rules/naming.json，管线只放判据）" % (dup or "无"))

    unresolved = sorted({v for v in (journal_nodes if journal_nodes is not None
                                     else _journal_node_values())
                         if naming_lib.try_identifier(v) is None})
    rec("S7", "历史节点名可归一", not unresolved,
        "解析失败=%s" % (unresolved or "无"))

    known = set(reg.get("non_node_states", [])) | set(naming_lib.all_states()) \
        | set(reg.get("state_aliases", {}))
    stray = sorted({s for s in (task_states if task_states is not None
                                else _task_state_values()) if s not in known})
    rec("S7", "任务状态名在词表内", not stray, "游离=%s" % (stray or "无"))

    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--pipe", default=PIPE, help="被验的 pipeline JSON（负向测试用）")
    args = ap.parse_args()

    pipe_path = args.pipe if os.path.isabs(args.pipe) else os.path.join(ROOT, args.pipe)
    if not os.path.exists(pipe_path):
        print("输入缺失: %s（判据唯一事实源，A12 禁静默兜底）" % pipe_path, file=sys.stderr)
        return 2

    with open(pipe_path, "rb") as f:
        pipe = json.loads(f.read().decode("utf-8"))

    hits = check(pipe)
    fails = [h for h in hits if not h["ok"]]
    for h in hits:
        print("[%s] %-18s %s%s" % (h["code"], h["name"], "PASS" if h["ok"] else "FAIL",
                                    "" if h["ok"] else "  -> " + h["detail"]))
    print("汇总：%d 项，通过 %d，失败 %d" % (len(hits), len(hits) - len(fails), len(fails)))

    if args.json:
        print(json.dumps({"nodes": len(pipe.get("nodes", [])), "total": len(hits),
                          "passed": len(hits) - len(fails), "failed": len(fails),
                          "results": hits}, ensure_ascii=False, indent=1))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
