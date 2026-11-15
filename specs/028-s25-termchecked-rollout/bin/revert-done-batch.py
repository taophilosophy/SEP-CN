# -*- coding: utf-8 -*-
"""ADR-0053 全量 done 回炉批量执行（specs/028 §0-bis）。

清单驱动：读 results/rollback-done-<batch>-list.json（slug 数组），
逐条校验当前 state=done → revert_state 至 s2.5_checked。
快照 → 逐条回退 → manifest（jsonl）；失败记录并落日志，退出码非零。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools import task_ops  # noqa: E402

SPEC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS = os.path.join(SPEC, "results")
ACTOR = "pc6-m2.5-revert"
REASON = "ADR-0053 全量 done 回炉（specs/028 §0-bis；先行批字头 a＋1）"


def main():
    batch = sys.argv[1] if len(sys.argv) > 1 else "a1"
    list_path = os.path.join(RESULTS, "rollback-done-%s-list.json" % batch)
    slugs = json.load(open(list_path, encoding="utf-8"))
    if not isinstance(slugs, list) or not slugs:
        raise SystemExit("清单为空或格式错误: %s" % list_path)
    snapshot = {}
    for slug in slugs:
        t = task_ops.load_task(slug)
        snapshot[slug] = t["state"] if t else "ERR:not-found"
    json.dump(snapshot, open(os.path.join(
        RESULTS, "rollback-done-%s-baseline.json" % batch), "w",
        encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    manifest, ok, fail = [], 0, 0
    for slug in slugs:
        try:
            t = task_ops.revert_state(slug, "s2.5_checked", REASON, ACTOR)
            manifest.append({"slug": slug, "from": snapshot.get(slug),
                             "to": t["state"], "ok": True})
            ok += 1
        except Exception as e:
            manifest.append({"slug": slug, "from": snapshot.get(slug),
                             "ok": False, "error": str(e)[:200]})
            fail += 1
    with open(os.path.join(RESULTS, "rollback-done-%s-manifest.jsonl" % batch),
              "w", encoding="utf-8", newline="\n") as f:
        for m in manifest:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(json.dumps({"batch": batch, "listed": len(slugs), "ok": ok,
                      "fail": fail}, ensure_ascii=False))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
