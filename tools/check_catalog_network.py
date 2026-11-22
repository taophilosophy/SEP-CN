# -*- coding: utf-8 -*-
"""目录四方重放网络门禁＋官方基线快照（specs/054）：zh SUMMARY ／ en SUMMARY ／ contents.html ／ mu-lu-s。

五子门（--gate，判官只读）：
  G1 装配等值：rebuild_catalog --check 对最新＋旧钉存快照 sha256 全等（B3.2 目录域）
  G2 en-SUMMARY 重放：gen_en_summary --check 直通（zh SUMMARY → SUMMARY-en.md 纯函数）
  G3 mu-lu 重放：mulu-map ⊕ SUMMARY → 重建 mu-lu-s.md 逐行全等
  G4 目录↔SUMMARY 对账：catalog slug 集 ↔ SUMMARY slug 行集双向差=0
     （反向豁免：别名 stub 行 −see- ＋ specs/001 catalog-verdict.json remove 挂起集）
  G5 官方基线快照：official-snapshot ≡ 最新 contents.html 解析 ≡ catalog 账

--build-mulu 从 mu-lu-s.md 现状抽账写 baseline/mulu-map.json（建账动作，非判定）。
退出码 0 全绿 / 1 红 / 2 用法。结果 JSON 走 stdout。
"""
import argparse
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import load_json, repo_path, write_json_verified  # noqa: E402

MULU = "mu-lu-s.md"
SUMMARY = "SUMMARY.md"
MAP_PATH = ("baseline", "mulu-map.json")
OLD_SNAP = "20261027T171130Z-contents.html"
OLD_ACCOUNT = "specs/054-catalog-network-replay/results/catalog-20261027.json"
OLD_SKEL = "specs/054-catalog-network-replay/results/catalog-skeleton-20261027.json"
OLD_RESID = "specs/054-catalog-network-replay/results/catalog-residual-20261027.json"
VERDICT = ("specs", "001-sep-sync-pipeline", "catalog-verdict.json")

LINK_RE = re.compile(r"^(\s*)\*\s\[(.+)\]\(([^)]+)\)\s*$")
GROUP_RE = re.compile(r"^(\s*)\*\s\\\\\*(.+)$")


def _split_slashes(p):
    return tuple(p.split("/"))


# --------------------------------------------------------------- G3 build --

def build_mulu():
    """从 mu-lu-s.md 抽归类账＋骨架（数据行=链接行⊕组行；序/缩进/组行文字=编辑判断入账）。"""
    lines = repo_text(MULU).split("\n")
    rows, skeleton = [], []
    order = 0
    for l in lines:
        m = LINK_RE.match(l)
        g = GROUP_RE.match(l)
        if m:
            rows.append({"kind": "link", "path": m.group(3), "text": m.group(2),
                         "indent": len(m.group(1)), "order": order})
            order += 1
        elif g:
            rows.append({"kind": "group", "text": g.group(2), "indent": len(g.group(1)),
                         "order": order})
            order += 1
        else:
            skeleton.append([order, l])    # 锚=下一数据行 order；≥order 的属尾段
    # 头段=锚 0 的骨架（首数据行前，frontmatter 等）；尾段=锚 ≥ order；其余按锚插入。
    # head 仅作冗余视图，重放只走 fixed_rows（锚 0 的行天然在首数据行前），避免双插。
    fixed, tail = [], []
    for a, t in skeleton:
        if a >= order:
            tail.append(t)
        else:
            fixed.append([a, t])
    head = [t for a, t in fixed if a == 0]
    doc = {"source": MULU, "rows": rows,
           "skeleton": {"fixed_rows": fixed, "head": head, "tail": tail}}
    write_json_verified(repo_path(*MAP_PATH), doc)
    print(json.dumps({"rows": len(rows), "links": sum(1 for r in rows if r["kind"] == "link"),
                      "groups": sum(1 for r in rows if r["kind"] == "group"),
                      "fixed": len(fixed), "head": len(head), "tail": len(tail),
                      "map": "/".join(MAP_PATH)}, ensure_ascii=False))
    return 0


def repo_text(rel):
    with open(repo_path(*rel.split("/")), encoding="utf-8") as f:
        return f.read()


def summary_path_text():
    """SUMMARY.md → {path: 链接文字}（无链接分组行不收；重复 path 报错语义由调用方处理）。"""
    out = {}
    for l in repo_text(SUMMARY).split("\n"):
        m = LINK_RE.match(l)
        if m:
            p = m.group(3)
            if p in out and out[p] != m.group(2):
                raise SystemExit(json.dumps({"error": "SUMMARY path 重复且文字不一致",
                                             "path": p}, ensure_ascii=False))
            out.setdefault(p, m.group(2))
    return out


def _unesc_md(s):
    """markdown 转义归一（文字跟随校验用；转义形态本身属形态残差，由账承载）。"""
    return s.replace("\\[", "[").replace("\\]", "]").replace("\\*", "*")


def replay_mulu():
    """G3：mulu-map ⊕ SUMMARY → 重建 mu-lu-s.md，逐行全等。

    link 行文字取账内原样（转义形态属形态残差）；另做「文字跟随」子断言：
    账文字与 SUMMARY 链接文字转义归一后必须一致——SUMMARY 改名即红（跟随语义）。
    """
    doc = load_json(repo_path(*MAP_PATH))
    spt = summary_path_text()
    fixed = {}
    for a, t in doc["skeleton"]["fixed_rows"]:
        fixed.setdefault(a, []).append(t)
    out = []
    follow_err = None
    for r in doc["rows"]:
        out.extend(fixed.get(r["order"], []))
        ind = " " * r["indent"]
        if r["kind"] == "link":
            if r["path"] not in spt:
                return None, {"error": "SUMMARY 缺 mu-lu-s 链接路径", "path": r["path"]}
            if follow_err is None and \
                    _unesc_md(r["text"]) != _unesc_md(spt[r["path"]]):
                follow_err = {"error": "mu-lu-s 文字未跟随 SUMMARY",
                              "path": r["path"],
                              "map_text": r["text"][:100],
                              "summary_text": spt[r["path"]][:100]}
            out.append("%s* [%s](%s)" % (ind, r["text"], r["path"]))
        else:
            out.append("%s* \\*%s" % (ind, r["text"]))
    out.extend(doc["skeleton"]["tail"])
    return "\n".join(out), follow_err


def g3():
    rebuilt, err = replay_mulu()
    if err:
        return {"gate": "G3", "ok": False, **err}
    orig = repo_text(MULU)
    ok = rebuilt == orig
    detail = {}
    if not ok:
        a, b = rebuilt.split("\n"), orig.split("\n")
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                detail = {"first_diff_line": i + 1, "rebuilt": x[:120], "orig": y[:120]}
                break
        detail.setdefault("line_counts", [len(a), len(b)])
    return {"gate": "G3", "ok": ok, **detail}


# ------------------------------------------------------------------- G4 ----

def g4():
    from tools.common import find_zh_doc
    account = load_json(repo_path("baseline", "catalog.json"))
    up = {it["slug"]: it["title"] for it in account["items"]}
    unmapped = [s for s, t in up.items() if not find_zh_doc(s, t)]
    # 反向：SUMMARY slug 行集 − 账 − 别名 stub − 挂起集
    slugs_in_summary = set()
    for l in repo_text(SUMMARY).split("\n"):
        m = LINK_RE.match(l)
        if not m:
            continue
        p = m.group(3)
        if not re.fullmatch(r"[a-z0-9]/[A-Za-z0-9][A-Za-z0-9.\-]*\.md", p):
            continue
        slug = p.rsplit("/", 1)[-1][:-3]
        if "-see-" in slug.lower():
            continue
        slugs_in_summary.add(slug)
    suspended = set()
    try:
        vd = load_json(repo_path(*VERDICT))
        for r in vd.get("remove", []):
            path = r.get("path", "")
            suspended.add(path.rsplit("/", 1)[-1].rsplit(".", 1)[0])
    except FileNotFoundError:
        pass
    extra = slugs_in_summary - set(up) - suspended
    ok = not unmapped and not extra
    return {"gate": "G4", "ok": ok, "upstream": len(up),
            "unmapped": unmapped[:10], "unmapped_count": len(unmapped),
            "extra": sorted(extra)[:10], "extra_count": len(extra),
            "suspended": sorted(suspended)}


def g5():
    """G5 官方基线快照：official-snapshot ≡ 最新 contents.html 解析 ≡ catalog 账。

    该文件是 rebuild_dir 的 slug 权威，长期无生成器/门禁（2026-11-15 后过期，
    曾把上游改名误报成缺镜像）。三处一致才算绿；修正走
    tools/sync_official_snapshot.py --write。
    """
    from tools import sync_official_snapshot as S
    snap = S.latest_snap()
    main_new, alias_new, dup = S.parse_contents(snap.read_bytes())
    base = json.loads(S.BASELINE.read_text(encoding="utf-8"))
    bm, ba = base.get("main", {}), base.get("alias", [])
    account = load_json(repo_path("baseline", "catalog.json"))
    am = {it["slug"]: it for it in account["items"] if not it.get("alias_of")}
    b_alias = {(x["alias"], x["slug"]) for x in ba}
    n_alias = {(x["alias"], x["slug"]) for x in alias_new}
    title_chg = [s for s in sorted(set(bm) & set(main_new))
                 if bm[s].get("title") != main_new[s].get("title")]
    auth_chg = [s for s in sorted(set(bm) & set(main_new))
                if bm[s].get("authors") != main_new[s].get("authors")]
    acct_chg = [s for s in sorted(set(am) & set(bm))
                if am[s].get("title") != bm[s].get("title")
                or am[s].get("authors") != bm[s].get("authors")]
    ok = (set(bm) == set(main_new) and set(am) == set(bm)
          and b_alias == n_alias and not title_chg and not auth_chg
          and not acct_chg and not dup)
    return {"gate": "G5", "ok": ok, "snapshot": snap.name,
            "baseline_fetched_at": base.get("fetched_at"),
            "main_old": len(bm), "main_new": len(main_new),
            "account": len(am),
            "main_added": sorted(set(main_new) - set(bm))[:10],
            "main_removed": sorted(set(bm) - set(main_new))[:10],
            "alias_added": sorted(n_alias - b_alias)[:10],
            "alias_removed": sorted(b_alias - n_alias)[:10],
            "title_changed": title_chg[:10],
            "authors_changed": auth_chg[:10],
            "account_mismatch": acct_chg[:10],
            "duplicates": dup[:10]}


# ------------------------------------------------------------------- G1 ----

def g1():
    from tools import rebuild_catalog as R
    res = []
    ok = True
    for snap, acc, skel, resid, tag in (
            (None, None, None, None, "latest"),
            (OLD_SNAP, _split_slashes(OLD_ACCOUNT), _split_slashes(OLD_SKEL),
             _split_slashes(OLD_RESID), "20261027")):
        snaps = sorted(n for n in os.listdir(repo_path("en", "_catalog"))
                       if n.endswith("-contents.html"))
        snap_name = snap or snaps[-1]
        if snap and snap not in snaps:
            res.append({"tag": tag, "ok": False, "error": "快照不存在: %s" % snap})
            ok = False
            continue
        entry = R.compute(repo_path("en", "_catalog", snap_name), acc, skel, resid)
        entry["tag"] = tag
        entry["ok"] = bool(entry.get("equal"))
        res.append(entry)
        ok = ok and entry["ok"]
    return {"gate": "G1", "ok": ok, "checks": res}


# ------------------------------------------------------------------- G2 ----

def g2():
    r = subprocess.run([sys.executable, "tools/gen_en_summary.py", "--check"],
                       cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       capture_output=True, text=True)
    return {"gate": "G2", "ok": r.returncode == 0,
            "detail": (r.stdout + r.stderr).strip()[-300:]}


def gate():
    results = [g1(), g2(), g3(), g4(), g5()]
    ok = all(r.get("ok") for r in results)
    print(json.dumps({"ok": ok, "gates": results}, ensure_ascii=False, indent=1))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--build-mulu", action="store_true",
                    help="从 mu-lu-s.md 现状抽账写 baseline/mulu-map.json")
    ap.add_argument("--gate", action="store_true", help="五子门判定（判官只读）")
    args = ap.parse_args(argv)
    if args.build_mulu:
        return build_mulu()
    if args.gate:
        return gate()
    print(json.dumps({"error": "需 --build-mulu / --gate 之一"}, ensure_ascii=False))
    return 2


if __name__ == "__main__":
    sys.exit(main())
