# -*- coding: utf-8 -*-
"""强制集存量回补（specs/052，ADR-0075）：按现行判据重算，据实记 pass/fail。

对象：journal 已走到 R3 的件（即"曾判定完成"者，specs/051 §2 的 400 件面）。
缺口：强制集（s0/s2.4/global/R1/R2/R3）中 s0/s2.4/global 三节点在这些件上
只有游标或只有 revert 记录，journal 无 pass —— 完成二字无法按现行强制集成立。

语义（rules/journal-schema.json 的 replay_on_change.tighten）：判据收紧后对既存
结果重跑新判据，追加 pass（gate_version 升级）或 fail；state_migration = 0，
**任务状态与 steps 一律不动**（回补是判据重算，不是状态迁移）。

记账规则：
  * 每件按 s0 → s2.4 → global 顺序求值；某节点 fail 即停，下游不记 pass
    （不让 fail 之后出现下游 pass，schema 的 fail 不变量）。
  * pass 事件写 gate（现行判据名，非空）、gate_version、witness（批次账定位）、
    note="backfill:<date>"；fail 事件另写 reason（失败命令与输出尾部）。
  * 已有 pass 的节点跳过；同 note 的 pass 存在即视为已回补（幂等）。

凭证纪律（specs/051 §1.5 教训）：只有全量运行可写主账 backfill-<date>.json；
--limit/--slugs 局部运行只写 backfill-<date>-partial.json，绝不覆盖主账。

用法:
  python tools/mandatory_backfill.py --limit 5            # 试跑（只读，不写 journal）
  python tools/mandatory_backfill.py --limit 5 --apply     # 试跑并记账（写 partial 账）
  python tools/mandatory_backfill.py --all --apply         # 全量（写主账）
退出码: 0 全过；1 有 fail（记账完成后）；2 用法错误。
"""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tools.common import load_json, utcnow_iso, write_text_verified  # noqa: E402
from tools.journal_lib import append_event, read_events  # noqa: E402
from tools.progress import load_journal  # noqa: E402  单一事实源：进度读面与目标面

DATE = datetime.now().strftime("%Y-%m-%d")
ACTOR = "backfill-" + DATE
RESULTS = os.path.join(ROOT, "specs", "052-mandatory-backfill", "results")

# mandatory_minimum 中需要回补的三节点（sg-01–sg-03 在核心段内，本就不缺）
NODES = ("ex-04", "rv-01", "rv-02")

# 目标面：曾走到 sg-03 的件（specs/051 §2 第 1 条的"400 件走完终审"）。
# 不用 CORE ⊆ passed：有 6 件 sg-03 已过但缺 tr-02 记录，用 CORE 会把它们漏在批次外。
TARGET_NODE = "sg-03"

# 节点 → 现行判据名（写入 pass.gate，schema 要求非空）
GATE_NAMES = {
    "ex-04": ["en_integrity", "en_source_audit"],
    "rv-01": ["check_terms", "errata_check", "check_style"],
    "rv-02": ["check_math_zh", "check_quotes", "check_tables_images",
              "check_academic", "check_style"],
}

# 节点 → 实跑命令（与 task_ops 的 _source_gate/_term_gate/_style_gate/_audit_gate 同源）；
# check_quotes 与 check_tables_images 是全库判官，按件归属见 _repo_wide_hits。
NODE_COMMANDS = {
    "ex-04": [("en_integrity.py", "{slug}"), ("en_source_audit.py", "{slug}")],
    "rv-01": [("check_terms.py", "--docs {zh}"), ("check_pairs.py", "--gate {zh}"),
              ("check_style.py", "{zh}")],
    "rv-02": [("check_math_zh.py", "{zh}"), ("check_academic.py", "--docs {zh}"),
               ("check_style.py", "{zh}")],
}


def _pipe_gate_version():
    p = load_json(os.path.join(ROOT, "rules", "pipeline.json"))
    return "%s@%s" % (p.get("schema"), p.get("date"))


def _ledger_name(full):
    """主账仅全量可写；局部运行写 -partial（specs/051 §1.5 凭证覆写教训）。"""
    return "backfill-%s%s.json" % (DATE.replace("-", ""), "" if full else "-partial")


def _run(script, args):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", script)] + args,
                       cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.returncode, ((r.stdout or "") + (r.stderr or "")).strip()


def _repo_wide_hits(zh, node):
    """全库判官按件归属：check_quotes（直角引号）与 check_tables_images（图链硬规则）。

    两者 CLI 无逐件入口，但判据函数本身按文件求值；此处调同一函数、只喂该件，
    保证"同视图、同谓词"，不另写一套规则。
    """
    if node != "rv-02":
        return []
    hits = []
    from tools.check_quotes import scan
    q_hits, _allowed = scan(ROOT, [zh])
    if q_hits:
        hits.append(("check_quotes", "%d 处（首处 %s:%d）" % (len(q_hits), q_hits[0][0], q_hits[0][1])))
    from tools.check_tables_images import HARD_RULES, check_file
    t_hits = [i for i in check_file(os.path.join(ROOT, zh)) if i[1] in HARD_RULES]
    if t_hits:
        hits.append(("check_tables_images", "%d 处（首处 %s:%d %s）"
                     % (len(t_hits), zh, t_hits[0][0], t_hits[0][1])))
    return hits


def eval_node(slug, zh, node):
    """跑一个节点的现行判据。返回 (ok, gate_list, detail)。"""
    gate, detail = list(GATE_NAMES[node]), ""
    for script, tpl in NODE_COMMANDS[node]:
        args = [a.format(slug=slug, zh=zh) for a in tpl.split()] if tpl else []
        rc, out = _run(script, args)
        if rc != 0:
            tail = " ".join(out.splitlines()[-6:])[:600]
            return False, gate, "%s 退出码 %d：%s" % (script, rc, tail)
    for name, msg in _repo_wide_hits(zh, node):
        return False, gate, "%s：%s" % (name, msg)
    return True, gate, ""


def _node_of(ev):
    """事件节点名归一到 identifier（历史事件为旧名，ADR-0080）。"""
    from tools import naming_lib
    return naming_lib.try_identifier(ev.get("node")) or ev.get("node")


def _has_pass(events, node):
    return any(e.get("type") == "pass" and _node_of(e) == node for e in events)


def _has_batch_fail(events, node):
    """本批次已判 fail 的节点不重判（重跑幂等；修判官后重判须显式 --recheck）。"""
    return any(e.get("type") == "fail" and _node_of(e) == node
               and str(e.get("note") or "").startswith("backfill:" + DATE) for e in events)


def process(slug, apply=False, gate_version="", ledger_name="", recheck=False):
    task = _load_task(slug)
    zh = (task or {}).get("zh_doc") or ""
    rec = {"slug": slug, "state": (task or {}).get("state"), "zh_doc": zh, "nodes": {}}
    events = read_events(slug)
    stopped = False
    for node in NODES:
        if _has_pass(events, node):
            rec["nodes"][node] = {"status": "already-pass",
                                  "detail": "journal 已有该节点 pass（含本批次先行记账）"}
            continue
        if _has_batch_fail(events, node) and not recheck:
            rec["nodes"][node] = {"status": "already-fail",
                                  "detail": "本批次已判 fail（修判官后重判须 --recheck）"}
            stopped = True
            continue
        if stopped:
            rec["nodes"][node] = {"status": "skipped-after-fail"}
            continue
        if not zh:
            rec["nodes"][node] = {"status": "fail", "detail": "无 zh_doc（非词条件不适用）"}
            stopped = True
            continue
        ok, gate, detail = eval_node(slug, zh, node)
        rec["nodes"][node] = {"status": "pass" if ok else "fail",
                              "gate": gate, "detail": detail}
        if not ok:
            stopped = True
        if apply:
            ev = {"type": "pass" if ok else "fail", "node": node, "gate": gate,
                  "attempt": "main", "at": utcnow_iso(), "actor": ACTOR,
                  "gate_version": gate_version,
                  "witness": "specs/052-mandatory-backfill/results/%s#%s:%s"
                             % (ledger_name, slug, node),
                  "note": "backfill:%s（现行判据重算，状态不迁移；ADR-0075）" % DATE}
            if not ok:
                ev["reason"] = detail
            append_event(slug, ev)
    return rec


def _load_task(slug):
    for letter in (slug[0], "1"):
        p = os.path.join(ROOT, "tasks", letter, slug + ".json")
        if os.path.exists(p):
            return load_json(p)
    return None


def select(all_flag, slugs, limit):
    passed, _ = load_journal()
    core = sorted(s for s, d in passed.items() if TARGET_NODE in d)
    full = True
    if slugs:
        core, full = [s for s in slugs if s in set(core)], False
    if limit:
        core, full = core[:limit], False
    return core, full


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="全量核心段完成件")
    ap.add_argument("--slugs", nargs="*", default=None)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--apply", action="store_true", help="写 journal（缺省只读试算）")
    ap.add_argument("--recheck", action="store_true",
                    help="重判本批次已 fail 的节点（默认跳过，保证重跑幂等）")
    args = ap.parse_args(argv)

    if not (args.all or args.slugs or args.limit):
        print("须显式指定范围：--all（全量）或 --slugs/--limit（局部，只写 partial 账）")
        return 2
    targets, full = select(args.all, args.slugs, args.limit)
    if not targets:
        print("无目标件（用 --all / --slugs / --limit 指定）")
        return 2
    gv = _pipe_gate_version()
    name = _ledger_name(full)
    print("目标 %d 件｜全量=%s｜apply=%s｜判据版本 %s" % (len(targets), full, args.apply, gv))

    records, done = [], 0
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futs = {pool.submit(process, s, args.apply, gv, name, args.recheck): s for s in targets}
        for fut in futs:
            rec = fut.result()
            records.append(rec)
            done += 1
            bad = [n for n, v in rec["nodes"].items() if v["status"] == "fail"]
            if bad or done % 25 == 0:
                print("  [%d/%d] %s %s" % (done, len(targets), rec["slug"],
                                           ("fail: " + ",".join(bad)) if bad else "ok"))

    # 批次效果按 journal 里的 backfill 标记事件汇总——不按本轮动作汇总。
    # 否则第二遍（全部 already-pass）会把"本批次实际判过多少节点"记成 0，
    # 读账的人据此会低估批次覆盖面（specs/051 §1.5 同族：读数口径要能被复算）。
    def _batch(node, ev_type):
        n = 0
        for s in targets:
            evs = read_events(s)
            hit = any(e.get("type") == ev_type and e.get("node") == node
                      and str(e.get("note") or "").startswith("backfill:" + DATE) for e in evs)
            if not hit:
                continue
            if ev_type == "fail" and any(e.get("type") == "pass" and e.get("node") == node
                                         for e in evs):
                continue          # 判官修复后重判为 pass：fail 留史但不计入存续失败
            n += 1
        return n

    summary = {"date": DATE, "apply": args.apply, "scope": "full" if full else "partial",
               "gate_version": gv, "targets": len(targets),
               "nodes": {n: _batch(n, "pass") for n in NODES},
               "fails": {n: _batch(n, "fail") for n in NODES}}
    out = {"schema": "sep-backfill/v1", "summary": summary, "entries": sorted(records, key=lambda r: r["slug"])}
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, name)
    write_text_verified(path, json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print("凭证：%s" % os.path.relpath(path, ROOT).replace("\\", "/"))
    print("结果：%s｜fail %s" % (summary["nodes"], summary["fails"]))
    return 1 if any(summary["fails"].values()) else 0


if __name__ == "__main__":
    sys.exit(main())
