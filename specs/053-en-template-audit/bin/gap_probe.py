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
        print("[%s] %s %s segs=%s first=%s %s"
              % (r.get("status"), r["slug"], "", r.get("segs"),
                 (first[0] or {}).get("reason"), ""), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
