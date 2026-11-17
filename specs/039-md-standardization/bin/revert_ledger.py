# -*- coding: utf-8 -*-
"""P8 回退面前置台账（specs/039，2026-11-17）。

对回退面（s2.5_checked / r2 / r3 / done 且带 zh_doc 的词条任务）逐件预跑
s2.4/s2.5 三轴机检（术语＋体例/勘误＋正文体例），产出：
  * results/revert-ledger-20261117.json   逐件结果（供批量回退驱动消费）
  * results/revert-ledger-20261117.md     汇总（族/红灯分布/阻断件清单）

只读：不改任务状态、不改正文。判据与 task_ops 门禁同源：
  check_terms --docs（硬错误计失败）、check_pairs.check_file 的 HARD_RULES、
  check_style.check_file 的全部 issue。

用法: python specs/039-md-standardization/bin/revert_ledger.py [--limit N]
"""
import argparse
import json
import os
import subprocess
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

import check_pairs  # noqa: E402
import check_style  # noqa: E402

FACE_STATES = ("s2.5_checked", "r2_reviewed", "r3_reviewed", "done")
SKIP_KINDS = ("glossary-maintenance",)


def face():
    out = []
    tdir = os.path.join(ROOT, "tasks")
    for dirpath, _dirnames, filenames in os.walk(tdir):
        for fn in filenames:
            if not fn.endswith(".json"):
                continue
            try:
                d = json.load(open(os.path.join(dirpath, fn), encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(d, dict):
                continue
            if d.get("state") in FACE_STATES and d.get("zh_doc") \
                    and d.get("kind") not in SKIP_KINDS:
                out.append({"slug": d["slug"], "state": d["state"],
                            "kind": d.get("kind"), "zh_doc": d["zh_doc"]})
    return out


def term_ok(zh_doc):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_terms.py"),
                        "--docs", zh_doc], capture_output=True, text=True,
                       encoding="utf-8", cwd=ROOT)
    return r.returncode == 0, (r.stdout or r.stderr).strip()[-400:]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    args = ap.parse_args(argv)

    items = face()
    if args.limit:
        items = items[:args.limit]
    rows, by_state, rule_hist = [], Counter(), Counter()
    for n, it in enumerate(items, 1):
        path = os.path.join(ROOT, it["zh_doc"])
        hard, warn = [], []
        if not os.path.exists(path):
            rows.append(dict(it, status="missing-doc", hard=["zh_doc 不存在"], warn=[]))
            by_state[it["state"]] += 1
            continue
        try:
            pair_issues = check_pairs.check_file(path)
        except Exception as exc:  # 检查器自身异常也须显式
            rows.append(dict(it, status="checker-error", hard=[repr(exc)], warn=[]))
            continue
        for i in pair_issues:
            if i.get("rule") in check_pairs.HARD_RULES:
                hard.append("%s: %s" % (i["rule"], i.get("detail", "")[:110]))
                rule_hist[i["rule"]] += 1
            else:
                warn.append("%s: %s" % (i.get("rule"), i.get("detail", "")[:80]))
        try:
            style_issues, _style_warn = check_style.check_file(path)
        except Exception as exc:
            hard.append("style-checker-error: %r" % exc)
            style_issues = []
        for i in style_issues:
            hard.append("%s: %s" % (i.get("rule"), i.get("detail", "")[:110]))
            rule_hist[i["rule"]] += 1
        tok, tout = term_ok(it["zh_doc"])
        if not tok:
            hard.append("check_terms: " + tout.replace("\n", " ")[-160:])
            rule_hist["check_terms"] += 1
        rows.append(dict(it, status="red" if hard else "green",
                         hard=hard, warn=warn))
        by_state[it["state"]] += 1
        if n % 50 == 0:
            sys.stderr.write("[ledger] %d/%d\n" % (n, len(items)))

    green = sum(1 for r in rows if r["status"] == "green")
    red = [r for r in rows if r["status"] == "red"]
    outdir = os.path.join(ROOT, "specs", "039-md-standardization", "results")
    os.makedirs(outdir, exist_ok=True)
    jpath = os.path.join(outdir, "revert-ledger-20261117.json")
    with open(jpath, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"at": "2026-11-17", "total": len(rows), "green": green,
                   "red": len(red), "by_state": dict(by_state),
                   "rule_hist": dict(rule_hist.most_common()),
                   "rows": rows}, f, ensure_ascii=False, indent=1)

    lines = ["# P8 回退面前置台账（2026-11-17）", "",
             "- 回退面：**%d 件**（%s）" % (len(rows), "、".join(
                 "%s %d" % (k, v) for k, v in by_state.items())),
             "- 三轴机检：**绿 %d / 红 %d**（绿＝可携机检凭证进入重走，红＝须先修）" % (green, len(red)),
             "", "## 红灯规则分布", "",
             "| 规则 | 件次 |", "| ---- | ---- |"]
    for k, v in rule_hist.most_common():
        lines.append("| `%s` | %d |" % (k, v))
    lines += ["", "## 阻断件清单（前 60）", "",
              "| slug | 状态 | 硬错误 |", "| ---- | ---- | ---- |"]
    for r in red[:60]:
        lines.append("| `%s` | %s | %s |" % (
            r["slug"], r["state"], "<br>".join(r["hard"][:3]).replace("|", "/")))
    if len(red) > 60:
        lines.append("| … | | 余 %d 件见 JSON |" % (len(red) - 60))
    mpath = os.path.join(outdir, "revert-ledger-20261117.md")
    with open(mpath, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(json.dumps({"total": len(rows), "green": green, "red": len(red),
                      "by_state": dict(by_state),
                      "rule_hist": dict(rule_hist.most_common())},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
