# -*- coding: utf-8 -*-
"""B3.2 缺口探针：定位首处不可入池的文字层差异（四出口裁定用）。

`diff_page` 只回“unaligned text units”并把页面开头 220 字当样本，无法定位。
本脚本按同一分段模型逐段比对，给出首个（或前 N 个）失配段的种类、ukey 差与
两侧原文片段，供判断出口（勘误／补丁／转换器／例外）。

用法：
  python specs/053-en-template-audit/bin/gap_probe.py <slug> [...]
  python specs/053-en-template-audit/bin/gap_probe.py --from-scan [--limit N]
  python specs/053-en-template-audit/bin/gap_probe.py --from-scan --status gap --only-new

只读判官：不改 en/、不改池、不写 baseline；凭证落 results/。
"""
import argparse
import difflib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "specs", "053-en-template-audit", "bin"))

import page_assemble as PA  # noqa: E402
import page_layout as PL  # noqa: E402
import assembly_pool as POOL  # noqa: E402
from tools.common import repo_path  # noqa: E402


def _char_diff(a, b, width=120):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    ops = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        ops.append({"op": tag,
                    "a": a[max(0, i1 - width):i2 + width],
                    "b": b[max(0, j1 - width):j2 + width]})
        if len(ops) >= 3:
            break
    return ops


def _ukey_diverge(ua, ub, width=120):
    """两个 ukey 流首次分叉处（含两侧窗口），供判断“谁少/多了什么”。"""
    j = 0
    while j < min(len(ua), len(ub)) and ua[j] == ub[j]:
        j += 1
    return {"at": j,
            "a": ua[max(0, j - width):j + width],
            "b": ub[max(0, j - width):j + width]}


def fail_block(A, B):
    """复演 POOL._sub_diff 的吞并逻辑，给出**首个救不回的块**（拒录真因）。

    逐段下标比对的 “first mismatch” 多是可吞并的标记漂移；池的判据是区间内
    ukey 流相等，故缺口定位必须按同一算法走一遍：ran-out＝吞并到页尾仍不等
    （文字差或顺序差）；ent-spans＝文字流相等但实体边界对不上。
    """
    sm = difflib.SequenceMatcher(None, list(A), list(B),
                                 autojunk=len(A) > 4000)
    ops = list(sm.get_opcodes())
    i = 0
    while i < len(ops):
        tag, i1, i2, j1, j2 = ops[i]
        if tag == "equal":
            i += 1
            continue
        ai1, ai2, bi1, bi2 = i1, i2, j1, j2
        start = {"op": tag, "range": [i1, i2, j1, j2]}
        while True:
            ua = "".join(POOL.ukey(t) for k, t in A[ai1:ai2] if k == "u")
            ub = "".join(POOL.ukey(t) for k, t in B[bi1:bi2] if k == "u")
            if ua == ub:
                break
            i += 1
            if i >= len(ops):
                return {"why": "ran-out", "start": start,
                        "a_i": [ai1, ai2], "b_i": [bi1, bi2],
                        "diverge": _ukey_diverge(ua, ub),
                        "a_head": [t[:200] for k, t in A[ai1:ai1 + 3]],
                        "b_head": [t[:200] for k, t in B[bi1:bi1 + 3]]}
            ai2, bi2 = ops[i][2], ops[i][4]
        at = "".join(t for _, t in A[ai1:ai2])
        bt = "".join(t for _, t in B[bi1:bi2])
        i += 1
        if at == bt or not ua:
            continue
        if POOL.ent_spans(POOL.plain(at), POOL.plain(bt)) is None:
            return {"why": "ent-spans", "start": start,
                    "a_i": [ai1, ai2], "b_i": [bi1, bi2],
                    "a": at[:300], "b": bt[:300],
                    "diff": _char_diff(at, bt)}
    return None


def probe(lib, slug, limit=3):
    p = repo_path("en", slug, "index.html")
    if not os.path.exists(p):
        return {"slug": slug, "status": "no-en"}
    h0 = PL.read(p)
    page, info = PA.assemble(lib, slug)
    out = {"slug": slug, "page_len": len(h0),
           "asm_len": len(page) if page else None,
           "skipped": info.get("skipped")}
    if page is None:
        out["status"] = "assemble-skip"
        return out
    A, B = POOL.segments(page), POOL.segments(h0)
    out["segs"] = [len(A), len(B)]
    mism = []
    for i in range(min(len(A), len(B))):
        (ka, ta), (kb, tb) = A[i], B[i]
        if ta == tb:
            continue
        if ka == "m" and kb == "m":
            continue
        reason = None
        if ka != "u" or kb != "u":
            reason = "kind-mismatch"
        else:
            ua, ub = POOL.ukey(ta), POOL.ukey(tb)
            if ua != ub:
                reason = "ukey-diff"
            else:
                es = POOL.ent_spans(POOL.plain(ta), POOL.plain(tb))
                if es is None:
                    reason = "ent-spans-fail"
        if not reason:
            continue
        mism.append({"i": i, "kinds": [ka, kb], "reason": reason,
                     "a": ta[:400], "b": tb[:400],
                     "diff": _char_diff(ta, tb)})
        if len(mism) >= limit:
            break
    out["status"] = "gap" if mism else "no-text-mismatch"
    out["mismatch"] = mism
    out["first_index"] = mism[0]["i"] if mism else None
    out["flow"] = flow_diff(A, B)
    # 拒录真因：按池自己的吞并算法走一遍（first mismatch 多为可吞并的漂移）
    out["fail"] = fail_block(A, B) if mism else None
    return out


def flow_diff(A, B, limit=3):
    """按文字单元 ukey 流对齐（忽略标记漂移），给出真正的文字层差异。

    逐段下标比对会把标记插入造成的位次漂移误报成文字差；池的 P1 谓词判的是
    ukey 流，所以定位也要按流做。
    """
    ua = [POOL.ukey(t) for k, t in A if k == "u"]
    ub = [POOL.ukey(t) for k, t in B if k == "u"]
    ta = [t for k, t in A if k == "u"]
    tb = [t for k, t in B if k == "u"]
    out = {"units": [len(ua), len(ub)], "equal": ua == ub, "ops": []}
    sm = difflib.SequenceMatcher(None, ua, ub, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        out["ops"].append({
            "op": tag, "range": [i1, i2, j1, j2],
            "a": [t[:220] for t in ta[i1:i2][:3]],
            "b": [t[:220] for t in tb[j1:j2][:3]]})
        if len(out["ops"]) >= limit:
            break
    return out


def _scan_slugs(status, only_new):
    scan = json.load(io.open(repo_path(
        "specs", "053-en-template-audit", "results", "page-scan-all.json"),
        encoding="utf-8"))
    slugs = [e["slug"] for e in scan["entries"] if e.get("status") == status]
    if only_new:
        import subprocess
        r = subprocess.run(
            ["git", "show", "802db20da:specs/053-en-template-audit/results/page-scan-all.json"],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        old = json.loads(r.stdout)
        old_status = {e["slug"]: e.get("status") for e in old["entries"]}
        slugs = [s for s in slugs if old_status.get(s) != status]
    return slugs


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--from-scan", action="store_true")
    ap.add_argument("--status", default="gap")
    ap.add_argument("--only-new", action="store_true",
                    help="只取相对 802db20da 新增的该状态件")
    ap.add_argument("--limit", type=int, default=3, help="每件最多报几处失配")
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    slugs = args.slugs or (_scan_slugs(args.status, args.only_new)
                           if args.from_scan else [])
    if not slugs:
        ap.error("给 slug 或用 --from-scan")
    lib = PA.Library()
    rows = [probe(lib, s, args.limit) for s in slugs]
    payload = {"schema": "sep-cn-gap-probe/1", "count": len(rows),
               "results": rows}
    text = json.dumps(payload, ensure_ascii=False, indent=1)
    if args.out:
        with io.open(args.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    else:
        print(text)
    for r in rows:
        first = r.get("mismatch") or [{}]
        fail = r.get("fail") or {}
        print("[%s] %s segs=%s first=%s fail=%s@%s"
              % (r.get("status"), r["slug"], r.get("segs"),
                 (first[0] or {}).get("reason"), fail.get("why"),
                 (fail.get("start") or {}).get("range")), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
