# -*- coding: utf-8 -*-
"""任务账本与译文文件的一致性检查（specs/051，2026-11-18）。

检查两条不变量（违例都是实测存在的，非假想风险）：

  I1 **清账不变量**：`state == cleared` 的词条，其译文文件应仅剩 H1。
     `task_ops.clear()` 的实现是「写入 H1 行」并把状态置 cleared，且 clear 要求
     pending 前置——所以 cleared 的**唯一**合法含义是「正文已置空、等待重译」。
     若文件有正文而状态仍是 cleared，则任何按状态调度的批次都会跳过它
     （`task_ops.advance` 拒绝从 cleared 直接跳 s1 之外的步骤，而批次通常按
     state 挑选目标），这批内容就成了「账外译文」。

  I2 **过程记录不变量**：译文文件有正文，但 journal 无任何 `pass` 事件。
     有正文意味着至少做过 draft；无 pass 意味着这件事没有被任何节点记录。
     此类件逃过了全部校审门禁（`check_pairs --gate` 按状态决定是否硬拦，
     cleared 在 `GATE_STATES` 之外 → 完全不拦）。

两判据同向，故合并计数、同一工具。

严格度：默认**告警档**（exit 0，打印违例数与清单），`--strict` 时违例非空即 exit 1。
理由：存量 18 件是**跨机 WIP 快照收编**带入的既成事实（2026-11-13 提交
「在途账本 WIP 快照（接手 S 批前收编）」把 1,127 文件的工作区内容入库，其中
505 行新内容进入一个已 cleared 的文件，而该批次的任务进度在另一台机器上、
journal 无对应记录）。判据若直接升严格档，等于用一条新门禁去惩罚已经发生且
尚无处置方案的历史，只会让门禁长期红。正确路径是：先清零或显式豁免，再升档
（`rules/08 §14` 升门须附清零计划与豁免清单）。故本工具先入 CI 每日告警。
2026-11-19 违例清零（`specs/052`：18 件按跨机收编回炉、`ci-hui-biao` 指针随并网修正），
已按收口判据升入 `tools/check_all.py` 的 `GATES` 严格档（ADR-0075）。

用法: python tools/check_taskfile_invariant.py [--strict] [--json]
退出码: 0 完成（告警档恒 0）；1 严格档且存在违例；2 输入缺失。
"""
import argparse
import io
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

CJK_RE = re.compile(r"[\u4e00-\u9fff]")
BODY_MIN = 50          # H1 之外汉字数低于此视为无正文（骨架/清空白）


def _strip_comments(text):
    return re.sub(r"(?s)<!--.*?-->", "", text)


def body_cjk(text):
    """H1 之外的汉字数——与 progress.count_skeletons 同口径。"""
    rest = re.sub(r"^#\s+.*$", "", _strip_comments(text), count=1, flags=re.M)
    return len(CJK_RE.findall(rest))


def iter_tasks(root=ROOT):
    for dirpath, _, filenames in os.walk(os.path.join(root, "tasks")):
        for fn in filenames:
            if not fn.endswith(".json"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8") as fh:
                    t = json.load(fh)
            except (OSError, ValueError):
                continue
            if isinstance(t, dict) and t.get("slug") and t.get("state"):
                yield t


def journal_passed(slug, root=ROOT):
    """该词条 journal 里的 pass 节点集合；无文件返回 None（账外）。"""
    letter = slug[0] if slug and slug[0].isalnum() else "0"
    p = os.path.join(root, "journal", letter, slug + ".ndjson")
    if not os.path.exists(p):
        return None
    done = set()
    with open(p, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except ValueError:
                continue
            if e.get("type") == "pass" and e.get("node"):
                done.add(e["node"])
    return done


def check(root=ROOT):
    """纯函数：返回违例列表（无副作用，可单测）。"""
    violations = []
    for t in iter_tasks(root):
        slug = t["slug"]
        state = t["state"]
        zh_doc = str(t.get("zh_doc") or "").strip()
        if not zh_doc:
            continue                       # 未绑定文档的任务
        if str(t.get("kind") or "") == "glossary-maintenance":
            # 维护任务的 zh_doc 指登记册/报告，不是词条正文：不适用清账与过程记录
            # 两条不变量（其 step 名也是自由形态，不与管线节点同名）。文件缺失单列，
            # 因为那仍是账本指向空处，只是不属于「译文账外」这一类。
            fp = zh_doc if os.path.isabs(zh_doc) else os.path.join(root, zh_doc)
            if not os.path.exists(fp):
                violations.append({"slug": slug, "rule": "maintenance-doc-missing",
                                   "state": state, "file": zh_doc, "cjk": None,
                                   "journal": None})
            continue
        fp = zh_doc if os.path.isabs(zh_doc) else os.path.join(root, zh_doc)
        if not os.path.exists(fp):
            violations.append({"slug": slug, "rule": "zh-doc-missing", "state": state,
                               "file": zh_doc, "cjk": None, "journal": None})
            continue
        try:
            with open(fp, encoding="utf-8") as fh:
                n = body_cjk(fh.read())
        except OSError as exc:
            violations.append({"slug": slug, "rule": "unreadable", "state": state,
                               "file": zh_doc, "cjk": None, "detail": str(exc),
                               "journal": None})
            continue
        passed = journal_passed(slug, root)
        if state == "cleared" and n >= BODY_MIN:
            violations.append({"slug": slug, "rule": "I1-cleared-but-bodied",
                               "state": state, "file": zh_doc, "cjk": n,
                               "journal": sorted(passed) if passed is not None else None})
        elif n >= BODY_MIN and not passed:
            # passed 为空集合或 None：有正文却无任何过程记录
            violations.append({"slug": slug, "rule": "I2-body-without-pass",
                               "state": state, "file": zh_doc, "cjk": n,
                               "journal": passed})
    return violations


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="违例即 exit 1（清零后方可升此档入 check_all GATES）")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    tdir = os.path.join(ROOT, "tasks")
    if not os.path.isdir(tdir):
        print("输入缺失: tasks/", file=sys.stderr)
        return 2

    v = check(ROOT)
    from collections import Counter
    by_rule = Counter(x["rule"] for x in v)
    if args.json:
        print(json.dumps({"total": len(v), "by_rule": dict(by_rule),
                          "violations": v}, ensure_ascii=False, indent=1))
    else:
        print("任务账本↔译文一致性（I1 清账／I2 过程记录）")
        print("  违例 %d ｜ 分布 %s" % (len(v), json.dumps(dict(by_rule), ensure_ascii=False)))
        for x in sorted(v, key=lambda y: -(y["cjk"] or 0)):
            print("  [%-22s] %-26s state=%-14s 汉字=%-6s journal=%s"
                  % (x["rule"], x["slug"], x["state"], x["cjk"], x["journal"]))
        if v:
            print("  处置：逐件回炉（从 s1 起补记录）或按跨机 WIP 补 journal 凭证"
                  "（specs/052 先例：import 补溯源 + s0→draft 回炉，截断件停 s0 并 block）。")
    return 1 if (args.strict and v) else 0


if __name__ == "__main__":
    sys.exit(main())
