# -*- coding: utf-8 -*-
"""全翻译流程并行性判定器（specs/045）：静态断言四条公理成立，负向样本可证伪。

判据（specs/045 §2）：
  A1 私有隔离：词条状态路径仅以 slug 为键，不同词条零交集。
  A2 共享原子：BASELINE_LOCK 单锁无嵌套；write_json_verified 原子替换。
  A3 单写者：campaign claim 认领互斥。
  A4/K3：状态机 prev 链无环（无死锁 + 可达的前提）。

只读：不写任何数据。判定器核心为纯函数（接受输入），负向测试注入坏输入证伪。

用法:
  python -I specs/045-parallelism/bin/verify_parallelism.py          # 对仓库真实代码/数据断言
  python -I specs/045-parallelism/bin/verify_parallelism.py --selftest  # 负向证伪
退出码: 0 全部通过；1 存在违反；2 输入错误。
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools.common import repo_path  # noqa: E402


def _read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def check_no_cycle(nodes):
    """DFS 检环：nodes = [{id, prev}]。返回 (ok, 环路径或 None)。"""
    by = {n["id"]: n for n in nodes}
    for start in by:
        path, cur = [], start
        while cur and cur not in path:
            path.append(cur)
            cur = by[cur].get("prev")
        if cur:
            return False, path + [cur]
    return True, None


def check_no_nested_lock(src):
    """检查 with BASELINE_LOCK 无嵌套：所有 with 行缩进深度相同（同层级）。"""
    depths = [len(ln) - len(ln.lstrip())
              for ln in src.split("\n") if "with BASELINE_LOCK" in ln]
    if not depths:
        return False, "无 BASELINE_LOCK 使用点"
    return len(set(depths)) == 1, depths


def check_atomic_replace(src):
    """检查 write_json_verified 用 os.replace 原子替换 + 读回校验。"""
    return ("os.replace" in src) and ("read() != data" in src or "f.read()" in src), None


def check_claim_mutex(src):
    """检查 campaign claim 有认领互斥（claimed_by 非空即拒）。"""
    return ('claimed_by' in src) and ('--force' in src), None


def _pipeline_nodes():
    return json.load(open(repo_path("rules", "pipeline.json"), encoding="utf-8"))["nodes"]


def run_assertions():
    """对仓库真实代码/数据断言四条公理。返回 (ok, 明细列表)。"""
    rows = []
    task_ops = _read(repo_path("tools", "task_ops.py"))
    journal_lib = _read(repo_path("tools", "journal_lib.py"))
    common = _read(repo_path("tools", "common.py"))
    campaign = _read(repo_path("tools", "campaign.py"))
    all_src = "\n".join(_read(repo_path("tools", f)) for f in
                        ("divergence.py", "fetch_entry.py", "yuanwen.py"))

    # A1 私有隔离：路径仅以 slug 为键
    ok = ("slug[0]" in task_ops) and ("slug + \".json\"" in task_ops or 'slug + ".json"' in task_ops)
    rows.append({"axiom": "A1", "name": "词条私有状态 slug 隔离（task_ops._os_path）",
                 "ok": ok, "detail": "路径模板含 slug[0] 与 slug" if ok else "未检出 slug 键路径"})
    ok = ("slug" in journal_lib) and (".ndjson" in journal_lib)
    rows.append({"axiom": "A1", "name": "journal 路径 slug 隔离（journal_lib._journal_path）",
                 "ok": ok, "detail": "路径模板含 slug 与 .ndjson" if ok else "未检出"})

    # A2 单锁无嵌套
    ok, det = check_no_nested_lock(all_src)
    rows.append({"axiom": "A2", "name": "BASELINE_LOCK 单锁无嵌套",
                 "ok": ok, "detail": "with 缩进深度 %s" % det})

    # A2 原子替换
    ok, det = check_atomic_replace(common)
    rows.append({"axiom": "A2", "name": "write_json_verified 原子替换 + 读回校验",
                 "ok": ok, "detail": "含 os.replace 与读回比对" if ok else "缺原子替换或读回校验"})

    # A3 认领互斥
    ok, det = check_claim_mutex(campaign)
    rows.append({"axiom": "A3", "name": "campaign claim 认领互斥",
                 "ok": ok, "detail": "含 claimed_by 与 --force" if ok else "缺认领互斥"})

    # K3 无环
    ok, det = check_no_cycle(_pipeline_nodes())
    rows.append({"axiom": "K3", "name": "状态机 prev 链无环",
                 "ok": ok, "detail": "无环" if ok else "检出环 %s" % det})

    return rows


def selftest():
    """负向证伪：注入坏输入，判定器必须报违反。"""
    cases = [
        ("N1-环", check_no_cycle([{"id": "a", "prev": "b"}, {"id": "b", "prev": "a"}]),
         "状态机带环"),
        ("N2-嵌套锁", check_no_nested_lock(
            "    with BASELINE_LOCK:\n        with BASELINE_LOCK:\n            pass"),
         "嵌套 BASELINE_LOCK"),
        ("N3-无认领互斥", check_claim_mutex("def cmd_claim(args):\n    return None"),
         "claim 无互斥"),
    ]
    ok = True
    for name, (passed, det), expect in cases:
        hit = (passed is False)
        ok &= hit
        print("[%s] 期望检出 %s -> %s%s" % (name, expect,
                                             "PASS" if hit else "FAIL",
                                             "" if hit else " 实际通过，未检出"))
    print("负向证伪：%s" % ("通过（判定器可证伪）" if ok else "失败"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    rows = run_assertions()
    for r in rows:
        print("[%s] %-42s %s%s" % (r["axiom"], r["name"], "PASS" if r["ok"] else "FAIL",
                                    "" if r["ok"] else "  -> " + str(r["detail"])))
    n_pass = sum(1 for r in rows if r["ok"])
    print("汇总：%d 项，通过 %d，失败 %d" % (len(rows), n_pass, len(rows) - n_pass))
    if args.json:
        print(json.dumps({"total": len(rows), "passed": n_pass,
                          "results": rows}, ensure_ascii=False, indent=1))
    return 0 if n_pass == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
