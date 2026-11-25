# -*- coding: utf-8 -*-
"""命名登记表读取与别名解析（ADR-0080）。

单一事实源：rules/naming.json。本模块只读，不做判据裁决（裁决在 check_stages S7）。
三层：identifier（永不变）／name（可演进）／state（identifier 派生）；历史 journal
与 tasks.steps 里的旧节点名经 aliases 归一，记录本身不改写（ISO 15489-1、P5）。

不导入 pipeline.json：避免与 task_ops／check_stages 形成循环依赖；两者的一致性由 S7 交叉核对。
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY_PATH = os.path.join(ROOT, "rules", "naming.json")

_REG = None


def load(path=None):
    """读登记表（模块级缓存；测试可传 path 覆盖）。缺失即硬失败（A12）。"""
    global _REG
    p = path or REGISTRY_PATH
    if _REG is not None and p == REGISTRY_PATH:
        return _REG
    if not os.path.exists(p):
        raise RuntimeError("rules/naming.json 不存在（节点标识唯一事实源，A12）")
    with open(p, "rb") as f:
        reg = json.loads(f.read().decode("utf-8"))
    reg["_by_id"] = {n["identifier"]: n for n in reg.get("nodes", [])}
    reg["_by_name"] = {n["name"]: n for n in reg.get("nodes", [])}
    reg["_by_alias"] = {}
    for n in reg.get("nodes", []):
        for a in n.get("aliases", []):
            reg["_by_alias"][a] = n["identifier"]
        reg["_by_alias"][n["identifier"]] = n["identifier"]
        reg["_by_alias"][n["name"]] = n["identifier"]
    if p == REGISTRY_PATH:
        _REG = reg
    return reg


class UnknownNode(KeyError):
    pass


def identifier(value):
    """把 identifier／name／历史别名／CLI 短名解析为 identifier；不可解析即抛。"""
    reg = load()
    v = str(value)
    if v in reg["_by_alias"]:
        return reg["_by_alias"][v]
    raise UnknownNode("未知节点名 %r（见 rules/naming.json）" % (value,))


def try_identifier(value):
    try:
        return identifier(value)
    except UnknownNode:
        return None


def identifiers():
    return [n["identifier"] for n in load().get("nodes", [])]


def record(identifier_value):
    return load()["_by_id"][identifier(identifier_value)]


def name_of(value):
    return record(value)["name"]


def label_of(value):
    return record(value)["label"]


def state_of(value):
    """节点对应的新状态名；无迁移状态的节点返回 None。"""
    return record(value).get("state")


def all_states():
    return [n["state"] for n in load().get("nodes", []) if n.get("state")]


def normalize_state(state):
    """旧状态名 → 新状态名；新状态与 pending／cleared／done 原样返回。"""
    reg = load()
    if state is None:
        return None
    return reg.get("state_aliases", {}).get(state, state)


def node_of_state(state):
    """状态 → 节点 identifier（非节点状态返回 None）。"""
    s = normalize_state(state)
    for n in load().get("nodes", []):
        if n.get("state") == s:
            return n["identifier"]
    return None


def step_matches(value, *identifiers_expected):
    """历史或新写的 step 名是否属于给定 identifier 集合（读取侧归一用）。"""
    nid = try_identifier(value)
    return nid is not None and nid in identifiers_expected


def steps_table():
    """全部合法 step 拼写 → 新状态（identifier／name／别名＋done）。"""
    reg = load()
    out = {alias: reg["_by_id"][nid]["state"]
           for alias, nid in reg["_by_alias"].items()
           if reg["_by_id"][nid].get("state")}
    out["done"] = "done"
    return out


def validate(path=None):
    """登记表自洽校验（S7 的纯函数部分）。返回错误串列表，空即通过。"""
    import re
    reg = load(path)
    errs = []
    pat_id = re.compile(reg.get("patterns", {}).get("identifier", r"^$"))
    pat_name = re.compile(reg.get("patterns", {}).get("name", r"^$"))
    pat_state = re.compile(reg.get("patterns", {}).get("state", r"^$"))
    ids, names, states, aliases = [], [], [], {}
    reserved = set()
    for seg in reg.get("segments", []):
        m = re.match(r"^(ex|tr|rv|sg)-(\d{2}) 至 (ex|tr|rv|sg)-(\d{2})$", seg.get("reserved", ""))
        if not m:
            errs.append("预留号段格式不可解析: %s" % seg.get("reserved"))
            continue
        for i in range(int(m.group(2)), int(m.group(4)) + 1):
            reserved.add("%s-%02d" % (m.group(1), i))
    for n in reg.get("nodes", []):
        i = n.get("identifier", "")
        if not pat_id.match(i):
            errs.append("identifier 不合规: %r" % i)
        if i in ids:
            errs.append("identifier 重复: %s" % i)
        ids.append(i)
        nm = n.get("name", "")
        if not pat_name.match(nm):
            errs.append("name 不合规: %r" % nm)
        if nm in names:
            errs.append("name 重复: %s" % nm)
        names.append(nm)
        if not str(n.get("name_version") or "").strip():
            errs.append("name_version 为空: %s" % i)
        if not str(n.get("label") or "").strip():
            errs.append("label 为空: %s" % i)
        st = n.get("state")
        if st is not None:
            if not pat_state.match(st):
                errs.append("state 不合规: %r" % st)
            if st != i + "_checked":
                errs.append("state 与 identifier 不对应: %s → %s" % (i, st))
            if st in states:
                errs.append("state 重复: %s" % st)
            states.append(st)
        for a in n.get("aliases", []):
            if a in aliases and aliases[a] != i:
                errs.append("alias 冲突: %s → %s / %s" % (a, aliases[a], i))
            aliases[a] = i
    # 预留号不得与在用号重叠
    used = set(ids)
    clash = sorted(used & reserved)
    if clash:
        errs.append("在用号占用预留号段: %s" % clash)
    # 非节点状态不得与节点状态重名
    for s in reg.get("non_node_states", []):
        if s in states:
            errs.append("非节点状态与节点状态重名: %s" % s)
    # 状态别名目标必须是现行节点状态
    for old, new in reg.get("state_aliases", {}).items():
        if new not in states:
            errs.append("state_aliases 目标不存在: %s → %s" % (old, new))
        if old in states:
            errs.append("state_aliases 旧名与现行状态重名: %s" % old)
    # 回退点必须是 identifier
    for c in reg.get("revert_checkpoints", []):
        if c not in used:
            errs.append("revert_checkpoints 含未知节点: %s" % c)
    return errs
