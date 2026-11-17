# -*- coding: utf-8 -*-
"""目录布局一致性门禁（ADR-0067）：rules/layout.json 为唯一事实源，本脚本只读比对四个面。

用法:
  python tools/check_layout.py [--json] [--quiet]

四谓词（rules/08 §14 四件套登记）:
  L1 根目录实际集合 ⊆ layout.json 声明（含 <letter> 展开）；未登记即红。
  L2 rules/01 目录职责表 ≡ layout.json 路径集合（双向）；缺一或多一即红。
  L3 每个已入库容器目录有 index（README/索引）或 index_exempt 登记；两者皆无即红。
  L4 specs/<NNN>-<slug>/ 子项 ⊆ required∪optional，forbidden 不出现，
     execution-log 两形态不并存；legacy_exceptions 登记项按登记范围放行。

判官只读（A11）：本脚本不写任何文件；判定权与规则所有权表见 rules/05。
预期命中数（首次全量）：L1=0、L2=0（表已补录）、L3=0（README 已补）、L4=0。
幂等：纯只读，重复运行结果一致。
一行回退：git revert 引入本门禁的提交（GATES 删行即撤，CI 矩阵自动跟随）。
退出码: 0 全绿；1 有硬错误；2 用法错误。
"""
import argparse
import json
import os
import re
import sys

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYOUT = os.path.join(ROOT, "rules", "layout.json")
RULES01 = os.path.join(ROOT, "rules", "01-repository-structure.md")


def load_layout(path=LAYOUT):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def declared_paths(layout):
    """声明集合：entries 的 path ＋ letter_dirs 的展开字符。"""
    declared = {e["path"] for e in layout["entries"]}
    ld = layout.get("letter_dirs") or {}
    declared |= set(ld.get("match", ""))
    return declared


def normalize_table_cell(cell):
    """把 rules/01 表第一列归一为根级路径集合。

    规则：取反引号内容；去删除线；去尾斜杠；取首段；`<letter>/<slug>.md` → `<letter>`。
    """
    out = set()
    for m in re.finditer(r"`([^`]+)`", cell):
        token = m.group(1).replace("~~", "").strip()
        token = token.rstrip("/")
        if not token:
            continue
        head = token.split("/")[0]
        if head.startswith("<"):
            out.add(head.split(">")[0] + ">")
        out.add(head)
    return out


def table_paths():
    """解析 rules/01「目录职责」表：只取第一列含反引号的表格行。"""
    with open(RULES01, encoding="utf-8") as f:
        lines = f.read().splitlines()
    paths = set()
    in_section = False
    for line in lines:
        if line.startswith("## "):
            in_section = "目录职责" in line
            continue
        if not in_section or not line.startswith("|"):
            continue
        cell = line.split("|")[1]
        if "`" not in cell:
            continue
        paths |= normalize_table_cell(cell)
    # 表内用 <letter>/ 表示字母目录
    if "<letter>" in paths:
        paths.discard("<letter>")
        paths |= set("abcdefghijklmnopqrstuvwxyz1")
    return paths


def check_l1(layout, declared):
    actual = {n for n in os.listdir(ROOT)}
    return sorted(actual - declared)


def check_l2(declared, table):
    missing_in_table = sorted(declared - table)
    extra_in_table = sorted(table - declared)
    return missing_in_table, extra_in_table


def check_l3(layout):
    bad = []
    for e in layout["entries"]:
        full = os.path.join(ROOT, e["path"])
        if not (e.get("tracked") and os.path.isdir(full)):
            continue
        if e.get("index_exempt"):
            continue
        idx = e.get("index")
        if not idx or not os.path.exists(os.path.join(ROOT, idx)):
            bad.append((e["path"], idx or "（未登记 index）"))
    return bad


def check_l4(layout, base=None):
    """返回 (硬错误, 告警)。判据：必需文件、黑名单子目录、目录命名、根级 JSON、互斥对。

    白名单式子项判定已于 2026-11-17 否决（误判 67 项合法规格文档），见 layout.json 的 schema_note。
    base 可注入（单测用），默认仓库 specs/。
    """
    spec = layout["specs_container"]
    base = base or os.path.join(ROOT, "specs")
    known = set(spec.get("known_subdirs", []))
    forbidden = set(spec.get("forbidden_subdirs", []))
    legacy = {x["path"]: x for x in spec.get("legacy_exceptions", [])}
    deny_root_json = spec.get("root_json_policy") == "deny"
    hard, warn = [], []
    if not os.path.isdir(base):
        return hard, warn

    for name in sorted(os.listdir(base)):
        full = os.path.join(base, name)
        if not os.path.isdir(full):
            continue
        rel = "specs/" + name
        if not re.match(r"^\d{3}-", name):
            hard.append((rel, "目录名不符 <NNN>-<slug>"))
            continue
        children = os.listdir(full)
        dirs = {c for c in children if os.path.isdir(os.path.join(full, c))}
        files = set(children) - dirs
        exc = legacy.get(rel, {})

        for c in sorted(dirs & forbidden):
            hard.append((rel + "/" + c, "禁止子目录"))
        for c in sorted(dirs - known - forbidden):
            warn.append((rel + "/" + c, "未知子目录（未登记 known_subdirs）"))

        if spec["required"][0] not in files and not exc.get("allow_missing_spec"):
            hard.append((rel, "缺 " + spec["required"][0]))

        if deny_root_json and not exc.get("allow_root_json"):
            allow_files = set(exc.get("allow_root_json_files", []))
            for f in sorted(files):
                if f.endswith((".json", ".jsonl")) and f not in allow_files:
                    hard.append((rel + "/" + f, "规格根不得放 JSON（归 results/）"))

        for a, b in spec.get("exclusive_pairs", []):
            if a in children and b in children:
                hard.append((rel, "并存：%s 与 %s" % (a, b)))

    return hard, warn


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="输出机读 JSON")
    ap.add_argument("--quiet", action="store_true", help="只报失败项")
    args = ap.parse_args(argv)

    layout = load_layout()
    declared = declared_paths(layout)
    table = table_paths()

    l1 = check_l1(layout, declared)
    l2_missing, l2_extra = check_l2(declared, table)
    l3 = check_l3(layout)
    l4, l4_warn = check_l4(layout)

    hard = bool(l1 or l2_missing or l2_extra or l3 or l4)
    if args.json:
        print(json.dumps({
            "declared": len(declared),
            "L1_undeclared": l1,
            "L2_missing_in_table": l2_missing,
            "L2_extra_in_table": l2_extra,
            "L3_no_index": l3,
            "L4_specs_violation": l4,
            "L4_specs_warning": l4_warn,
            "ok": not hard,
        }, ensure_ascii=False, indent=2))
        return 0 if not hard else 1

    if hard or not args.quiet:
        print("目录布局一致性（layout.json 为唯一事实源）")
        print("  L1 根目录未声明：%d" % len(l1))
        for x in l1:
            print("     - " + x)
        print("  L2 职责表缺 %d / 多 %d" % (len(l2_missing), len(l2_extra)))
        for x in l2_missing:
            print("     表缺: " + x)
        for x in l2_extra:
            print("     表多: " + x)
        print("  L3 容器无自述：%d" % len(l3))
        for p, why in l3:
            print("     - %s（%s）" % (p, why))
        print("  L4 specs 违规：%d（告警 %d）" % (len(l4), len(l4_warn)))
        for p, why in l4:
            print("     - %s（%s）" % (p, why))
        for p, why in l4_warn:
            print("     ~ %s（%s）" % (p, why))
    if hard:
        print("结果：不合规（退出码 1）")
        return 1
    print("结果：L1–L4 全绿（声明 %d 条）" % len(declared))
    return 0


if __name__ == "__main__":
    sys.exit(main())
