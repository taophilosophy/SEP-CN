# -*- coding: utf-8 -*-
"""ADR-0043 全量回退批量执行（specs/028 §5）。

回退面 = 026 T1 清单（a1-task-states.json at_or_after_audited，A1 波及 185）
        ∪ 清单外现存 s3_checked/r1_reviewed/r2/r3 在途件（ADR-0043 决策 4②）。
非清单 done 不回退（specs/023 并入 028 补课口径）。
快照 → 逐条 revert_state → manifest；失败即停并落日志。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools import task_ops  # noqa: E402

SPEC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS = os.path.join(SPEC, "results")
A1 = os.path.join(os.path.dirname(SPEC), "026-standards-tier3-rollout",
                  "results", "a1-task-states.json")
ACTOR = "pc6-m2.5-revert"
REASON = "ADR-0043 全量回退（specs/028 §5；185 全口径＋非 A1 在途件）"


def main():
    os.makedirs(RESULTS, exist_ok=True)
    a1 = json.load(open(A1, encoding="utf-8"))
    listed = {e["slug"]: e["state"] for e in a1["at_or_after_audited"]}
    # 现存快照（回退面判定）
    snapshot, rollback = {}, []
    import glob
    for f in glob.glob(os.path.join(task_ops.repo_path("tasks"), "*", "*.json")):
        slug = os.path.splitext(os.path.basename(f))[0]
        try:
            t = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            snapshot[slug] = "ERR:%s" % e
            continue
        if not isinstance(t, dict):
            snapshot[slug] = "ERR:top-level %s" % type(t).__name__
            continue
        st = t.get("state")
        if not st or t.get("kind") not in task_ops.ORDER:
            continue
        snapshot[slug] = st
        if st in ("s3_checked", "r1_reviewed", "r2_reviewed", "r3_reviewed"):
            rollback.append(slug)          # 在途超阶段件（含清单内 12+3）
        elif st == "done" and slug in listed:
            rollback.append(slug)          # A1 波及 done（清单 170）
    json.dump(snapshot, open(os.path.join(RESULTS, "rollback-baseline.json"),
                             "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    manifest, ok, fail = [], 0, 0
    for slug in sorted(set(rollback)):
        try:
            t = task_ops.revert_state(slug, "s2.5_checked", REASON, ACTOR)
            manifest.append({"slug": slug, "from": snapshot.get(slug),
                             "to": t["state"], "ok": True})
            ok += 1
        except Exception as e:
            manifest.append({"slug": slug, "from": snapshot.get(slug),
                             "ok": False, "error": str(e)[:200]})
            fail += 1
    with open(os.path.join(RESULTS, "rollback-manifest.jsonl"), "w",
              encoding="utf-8") as f:
        for m in manifest:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(json.dumps({"rollback_target": len(set(rollback)), "ok": ok,
                      "fail": fail, "snapshot": len(snapshot)},
                     ensure_ascii=False))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
