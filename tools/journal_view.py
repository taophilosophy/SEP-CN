# -*- coding: utf-8 -*-
"""journal 派生视图（ADR-0068 W4 的一部分）：只读，不写任何文件（P6/P24）。

从 journal/<letter>/<slug>.ndjson 折叠每个条目的 pass 集合，现算：
  stage_done(e)   已通过节点集
  saturate(e)     pass ⊇ N ∪ M（饱和，相对量，随 pipeline 节点可插而可变假）
  report          曾达饱和 / 强制集完成 / 各节点通过数

stale（钉过期）由 tools/drift_scan.py 派生，本视图不实现（避免重复读 en 全量哈希）。

用法: python tools/journal_view.py [--json]
退出码: 0 正常；2 输入缺失。
"""
import argparse
import io
import json
import os
import sys
from collections import Counter, defaultdict

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNAL = os.path.join(ROOT, "journal")
PIPE = os.path.join(ROOT, "rules", "pipeline.json")


def _load_pipeline():
    if not os.path.exists(PIPE):
        return None
    with open(PIPE, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def _iter_journal():
    for dirpath, _, filenames in os.walk(JOURNAL):
        if os.path.basename(dirpath) == "README.md":
            continue
        for fn in filenames:
            if not fn.endswith(".ndjson"):
                continue
            yield os.path.join(dirpath, fn)


def stage_done(path):
    """折叠一个 journal 文件的 pass 集合（沿主 attempt 累积，pass 只增不减）。

    节点名经 naming.json 归一到 identifier（ADR-0080）。
    """
    from tools import naming_lib
    done = set()
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                ev = json.loads(line)
                if ev.get("type") == "pass" and ev.get("node"):
                    done.add(naming_lib.try_identifier(ev["node"]) or ev["node"])
    except (json.JSONDecodeError, OSError):
        pass
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    pipe = _load_pipeline()
    if pipe is None:
        print("输入缺失: rules/pipeline.json", file=sys.stderr)
        return 2
    if not os.path.isdir(JOURNAL):
        print("输入缺失: journal/", file=sys.stderr)
        return 2

    nodes = {n["id"] for n in pipe.get("nodes", [])}
    mand = set(pipe.get("mandatory_minimum", {}).get("nodes", []))
    # 迁移可达节点：task_ops 状态机覆盖的 15 个；管线/预处理节点（ex-01–03、ex-05、
    # tr-01、tr-05）无迁移事件，须由 journal_ops 未来补齐（ADR-0068 已知局限）
    core = {"tr-02", "tr-03", "tr-04", "rv-09", "sg-01", "sg-02", "sg-03"}
    full = nodes | mand

    core_done, mand_ok, saturate = [], [], []
    node_count = Counter()
    total = 0

    for path in _iter_journal():
        total += 1
        done = stage_done(path)
        node_count.update(done)
        slug = os.path.basename(path)[:-7]
        if done >= core:
            core_done.append(slug)
        if done >= mand:
            mand_ok.append(slug)
        if done >= full:
            saturate.append(slug)

    print("条目 %d｜核心段完成（%d 节点）%d｜强制集完成 %d｜完整饱和（%d 节点）%d"
          % (total, len(core), len(core_done), len(mand_ok), len(full), len(saturate)))

    print("\n各节点通过数：")
    for n in sorted(full):
        print("  %-8s %d" % (n, node_count.get(n, 0)))

    if args.json:
        print(json.dumps({
            "total": total, "core_done": len(core_done), "mandatory_ok": len(mand_ok),
            "saturate": len(saturate),
            "node_count": dict(sorted(node_count.items())),
            "core_done_slugs": core_done,
        }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
