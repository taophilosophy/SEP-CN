# -*- coding: utf-8 -*-
"""基线完整性审计（宪法门 I 的机器实现，FR-002/017）。

用法: python tools/baseline_audit.py [slug...]
输出: stdout JSON {audited, hash_ok, hash_fail, missing_files}
行为: 对 baseline/entries.json 登记的每件抓取物复算 SHA-256 并核对存在；
      task_ops.py clear 的 gate 直接调用本模块。
"""
import json
import os
import sys

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import load_json, repo_path, utcnow_iso


def audit_slugs(slugs=None):
    path = repo_path("baseline", "entries.json")
    if not os.path.exists(path):
        return {"audited": 0, "hash_ok": 0, "hash_fail": [], "missing_files": [],
                "error": "baseline/entries.json 不存在（先运行 fetch_entry.py）"}
    base = load_json(path)
    recs = base["entries"]
    if slugs:
        want = set(slugs)
        recs = [r for r in recs if r["slug"] in want]
        absent = want - {r["slug"] for r in recs}
    else:
        absent = set()
    ok, fail, missing = 0, [], []
    for r in recs:
        for f in r.get("files", []):
            rel = f["path"]  # 形如 en/<slug>/index.html
            full = repo_path(rel)
            if not os.path.exists(full):
                missing.append({"slug": r["slug"], "path": rel})
                continue
            import hashlib
            h = hashlib.sha256()
            with open(full, "rb") as fh:
                for chunk in iter(lambda: fh.read(1 << 16), b""):
                    h.update(chunk)
            if h.hexdigest() == f["sha256"]:
                ok += 1
            else:
                fail.append({"slug": r["slug"], "path": rel,
                             "recorded": f["sha256"], "actual": h.hexdigest()})
    out = {"audited": len(recs), "hash_ok": ok, "hash_fail": fail,
           "missing_files": missing, "at": utcnow_iso()}
    if absent:
        out["not_in_baseline"] = sorted(absent)
    return out


def gate_passes(slug):
    """clear 的前置 gate：该词条已登记且全部文件哈希复算通过。"""
    out = audit_slugs([slug])
    if out.get("audited", 0) < 1:
        return False, out
    return (not out["hash_fail"] and not out["missing_files"]), out


def main(argv=None):
    slugs = [a for a in (argv or sys.argv[1:]) if not a.startswith("-")]
    print(json.dumps(audit_slugs(slugs or None), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
