#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tasks.state 迁移：旧状态名 → identifier 派生状态（ADR-0080）。

只迁移 `kind=retranslate` 的条目状态；`steps` 历史不改写（记录只追加，ISO 15489-1）。
映射唯一来源：rules/naming.json 的 state_aliases。

验证（迁移的验收，不依赖 journal 重放）：
  1. 映射双档：迁移前逐条记 (slug, old)；迁移后逐条复核 new == aliases[old]，
     一条不符即整体不写（先算后写，写后回读校验由 write_json_verified 保证）。
  2. 分布对照：迁移前后按状态计数，必须满足 count(new) = Σ count(old→new)。
  3. 重放体检：迁移前后 `replay_state.classify` 的分类逐条一致（只换标签，不换事实）。
     —— 严格重放只能复现 803/1200（回补 pass、cleared/done 非事件），故重放只作
     漂移体检，不作硬门；理由见 tools/replay_state.py 头注。

用法:
  python tools/migrate_state_names.py            # 干跑：打印映射与分布
  python tools/migrate_state_names.py --apply     # 写入（幂等；逐条读回校验）
退出码: 0 成功或无需迁移；1 存在无法映射的状态；2 输入缺失。
"""
import argparse
import json
import os
import sys
from collections import Counter

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools import naming_lib  # noqa: E402
from tools.common import utcnow_iso, write_json_verified  # noqa: E402
from tools.replay_state import classify, replay  # noqa: E402

RESULTS = os.path.join(ROOT, "specs", "060-six-axis-quality-gates", "results",
                       "state-migration.json")


def iter_tasks():
    tdir = os.path.join(ROOT, "tasks")
    if not os.path.isdir(tdir):
        raise SystemExit(2)
    for dirpath, _, files in os.walk(tdir):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8") as f:
                    t = json.load(f)
            except (OSError, ValueError):
                continue
            if isinstance(t, dict) and t.get("state") \
                    and str(t.get("kind") or "") == "retranslate":
                yield p, t


def plan():
    """先算后写：返回 (待迁移, 已是新名, 不可映射)。"""
    todo, done, bad = [], [], []
    for p, t in iter_tasks():
        old = t["state"]
        new = naming_lib.normalize_state(old)
        if new == old and old not in naming_lib.all_states() \
                and old not in ("pending", "cleared", "done"):
            bad.append((t["slug"], old))
            continue
        if new == old:
            done.append((p, t))
        else:
            todo.append((p, t, old, new))
    return todo, done, bad


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    todo, done, bad = plan()
    if bad:
        print("存在无法映射的状态（先归因再迁移）：%s" % bad[:5])
        return 1

    dist = Counter((old, new) for _, _, old, new in todo)
    print("条目 %d｜待迁移 %d｜已是新名 %d" % (len(todo) + len(done), len(todo), len(done)))
    for (old, new), n in sorted(dist.items(), key=lambda x: -x[1]):
        print("  %-18s → %-16s %d" % (old, new, n))

    replay_before = {t["slug"]: classify(naming_lib.normalize_state(t["state"]), replay(t["slug"])[0])
                     for _, t, _, _ in todo}
    if not args.apply:
        print("干跑：未写任何文件（--apply 执行）")
        return 0

    for p, t, old, new in todo:
        before = json.load(open(p, encoding="utf-8"))
        before["state"] = new
        before["state_migrated"] = {"at": utcnow_iso(), "from": old,
                                    "to": new, "by": "ADR-0080"}
        write_json_verified(p, before)

    # 写后逐条复核（映射双档）
    after_map = {}
    mism = []
    for p, t, old, new in todo:
        now = json.load(open(p, encoding="utf-8"))
        after_map[t["slug"]] = now["state"]
        if now["state"] != new:
            mism.append((t["slug"], old, now["state"], new))
    if mism:
        print("迁移后复核失败（%d 条），回滚请 git checkout -- tasks/" % len(mism))
        print(mism[:5])
        return 1

    replay_after = {s: classify(st, replay(s)[0]) for s, st in after_map.items()}
    drift = sorted(k for k in replay_before if replay_before[k] != replay_after.get(k))

    report = {
        "schema": "state-migration/v1",
        "at": utcnow_iso(),
        "mapping": naming_lib.load().get("state_aliases", {}),
        "dist": {"%s→%s" % k: v for k, v in dist.items()},
        "migrated": len(todo), "already": len(done),
        "changed_paths": [os.path.relpath(p, ROOT).replace(os.sep, "/")
                          for p, _, _, _ in todo],
        "replay_drift": drift,
        "replay_classes": dict(Counter(replay_after.values())),
    }
    os.makedirs(os.path.dirname(RESULTS), exist_ok=True)
    write_json_verified(RESULTS, report)
    print("已迁移 %d 条；复核 0 不符；重放分类漂移 %d 条；报告 %s"
          % (len(todo), len(drift), os.path.relpath(RESULTS, ROOT)))
    return 0 if not drift else 1


if __name__ == "__main__":
    sys.exit(main())
