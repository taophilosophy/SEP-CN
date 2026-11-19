# -*- coding: utf-8 -*-
"""上游目录四方漂移巡检（specs/054 运营化）：上游 contents.html ↔ 本地三账。

四面对比（只报告，不改任何内容文件）：
  C 上游快照（--fetched 指定，通常由 fetch_catalog --snapshot-only 落盘）
  ① catalog 账：baseline/catalog.json —— 增/删/改名/作者变/别名变
  ② SUMMARY：slug 行集 —— 上游有而本地无（待接入）、本地有而上游无（待裁撤）
  ③ mu-lu-s：链接行集 —— 同上两向
另可 --assembly：用本次快照产临时骨架/残差池并做 sha256 装配核验（B3.2），
四类准入之外的残差即上游模板/格式层漂移，单独报出（specs/054 A5）。

用法:
  python tools/catalog_drift.py --fetched en/_catalog/<ts>-contents.html --json out.json --md out.md
  python tools/catalog_drift.py --latest --assembly            # 取 en/_catalog 最新快照
退出码: 0 无漂移；1 有漂移（结果仍写盘）；2 用法/输入错误。
"""
import argparse
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import parser  # noqa: E402
from tools.common import load_json, repo_path, utcnow_iso  # noqa: E402

ENTRY_PATH_RE = re.compile(r"^[a-z0-9]/([A-Za-z0-9][A-Za-z0-9.\-]*)\.md$")


def _slugs_from_md(text, skip_see=True):
    """取 mardown 链接行 `<letter>/<slug>.md` 的 slug 集（SUMMARY 与 mu-lu-s 同构）。"""
    out = set()
    for line in text.split("\n"):
        m = re.search(r"\]\(([^)]+)\)", line)
        if not m:
            continue
        p = m.group(1)
        mm = ENTRY_PATH_RE.match(p)
        if not mm:
            continue
        slug = mm.group(1)
        if skip_see and "-see-" in slug.lower():
            continue
        out.add(slug)
    return out


def read_text(path):
    with io.open(path, encoding="utf-8", newline="") as f:
        return f.read()


def suspended_set():
    """specs/001 catalog-verdict 的 remove 挂起集（已知裁撤候选，不计为漂移）。"""
    try:
        vd = load_json(repo_path("specs", "001-sep-sync-pipeline", "catalog-verdict.json"))
    except (OSError, ValueError):
        return set()
    out = set()
    for r in vd.get("remove", []):
        base = str(r.get("path", "")).rsplit("/", 1)[-1]
        out.add(base.rsplit(".", 1)[0])
    return out


def drift_report(upstream_full, baseline, summary_slugs, mulu_slugs, suspended=None):
    """纯函数：四方差异 → 报告 dict。"""
    suspended = suspended or set()
    up_items = sorted(upstream_full["items"], key=lambda x: x["slug"])
    up = {it["slug"]: it for it in up_items}
    base = {it["slug"]: it for it in baseline.get("items", [])}

    added = sorted(set(up) - set(base))
    removed = sorted(set(base) - set(up))
    renamed, authors_changed = [], []
    for slug in sorted(set(up) & set(base)):
        a, b = base[slug], up[slug]
        if (a.get("title") or "") != (b.get("title") or ""):
            renamed.append({"slug": slug, "old": a.get("title"), "new": b.get("title")})
        if (a.get("authors") or "") != (b.get("authors") or ""):
            authors_changed.append({"slug": slug,
                                    "old": a.get("authors"), "new": b.get("authors")})

    up_alias = [r["slug"] for r in upstream_full["alias_rows"]]
    base_alias = [r["slug"] for r in baseline.get("alias_rows", [])]
    alias_added = sorted(set(up_alias) - set(base_alias))
    alias_removed = sorted(set(base_alias) - set(up_alias))

    up_set = set(up)
    up_missing_summary = sorted(up_set - summary_slugs - suspended)
    summary_only = sorted(summary_slugs - up_set - suspended)
    up_missing_mulu = sorted(up_set - mulu_slugs - suspended)
    mulu_only = sorted(mulu_slugs - up_set - suspended)

    rep = {
        "generated_at": utcnow_iso(),
        "upstream": {"items": len(up_items),
                     "alias_rows": len(upstream_full["alias_rows"]),
                     "cluster_mothers": len(upstream_full["cluster_mothers"])},
        "catalog": {
            "added": added,
            "removed": removed,
            "renamed": renamed,
            "authors_changed": authors_changed,
            "alias_added": alias_added,
            "alias_removed": alias_removed,
        },
        "local": {
            "upstream_missing_in_summary": up_missing_summary,
            "summary_only_upstream": summary_only,
            "upstream_missing_in_mulu": up_missing_mulu,
            "mulu_only_upstream": mulu_only,
        },
        "suspended": sorted(suspended),
        "assembly": None,
    }
    rep["changed"] = bool(added or removed or renamed or authors_changed
                          or alias_added or alias_removed
                          or up_missing_summary or summary_only
                          or up_missing_mulu or mulu_only)
    return rep


def assembly_check(snap_path):
    """用本次快照产临时骨架/残差池并做 sha256 装配核验（B3.2）；残差超准入即漂移。"""
    from tools import rebuild_catalog as R
    import tempfile
    tmp = tempfile.mkdtemp(prefix="catalog-assembly-")
    skel = os.path.join(tmp, "skeleton.json")
    resid = os.path.join(tmp, "residual.json")
    acc = os.path.join(tmp, "account.json")
    try:
        rc = R.build(snap_path, skel, resid)
        if rc != 0:
            return {"ok": False, "error": "build 失败（残差超出 A5 准入谓词或对齐失败）"}
        R.build_account(snap_path, acc)
        res = R.compute(snap_path, acc, skel, resid)
        count = None
        try:
            count = load_json(resid).get("count")
        except (OSError, ValueError):
            pass
        return {"ok": bool(res.get("equal")),
                "residual_count": count,
                "sha_rebuilt": res.get("sha_rebuilt"),
                "sha_snapshot": res.get("sha_snapshot"),
                "error": res.get("error")}
    finally:
        for p in (skel, resid, acc):
            if os.path.exists(p):
                os.remove(p)
        try:
            os.rmdir(tmp)
        except OSError:
            pass


def render_md(rep):
    L = []
    L.append("## 上游目录漂移巡检")
    L.append("")
    L.append("- 生成时间：%s" % rep["generated_at"])
    L.append("- 上游快照：%s" % rep.get("snapshot", "—"))
    L.append("- 上游统计：主条目 %(items)d／别名行 %(alias_rows)d／簇母行 %(cluster_mothers)d"
             % rep["upstream"])
    L.append("")
    c = rep["catalog"]
    loc = rep["local"]

    def block(title, rows, cols=None):
        L.append("### %s（%d）" % (title, len(rows)))
        if rows:
            for r in rows[:50]:
                L.append("- %s" % (json.dumps(r, ensure_ascii=False) if isinstance(r, dict) else r))
            if len(rows) > 50:
                L.append("- …… 余 %d 条，见 JSON 报告" % (len(rows) - 50))
        else:
            L.append("- 无")
        L.append("")

    block("上游新增条目（待接入 ADD）", c["added"])
    block("上游删除条目（待裁撤 REMOVE）", c["removed"])
    block("上游改名", c["renamed"])
    block("作者变更", c["authors_changed"])
    block("别名新增", c["alias_added"])
    block("别名消失", c["alias_removed"])
    block("上游有而 SUMMARY 无", loc["upstream_missing_in_summary"])
    block("SUMMARY 有而上游无", loc["summary_only_upstream"])
    block("上游有而 mu-lu-s 无", loc["upstream_missing_in_mulu"])
    block("mu-lu-s 有而上游无", loc["mulu_only_upstream"])
    if rep.get("suspended"):
        L.append("（已挂起不计：%s）" % "、".join(rep["suspended"]))
        L.append("")
    if rep.get("assembly") is not None:
        a = rep["assembly"]
        L.append("### 装配核验（B3.2）")
        L.append("- 结果：%s" % ("全等" if a.get("ok") else "不等/失败"))
        if a.get("residual_count") is not None:
            L.append("- 残差池：%s 条（A5 准入四类之外即格式层漂移）" % a["residual_count"])
        if a.get("error"):
            L.append("- 错误：%s" % a["error"])
        L.append("")
    L.append("### 处置路线（specs/054 §3 单向波纹）")
    L.append("1. `python tools/fetch_catalog.py`（落快照＋重写 baseline/catalog.json＋与上次快照 diff）")
    L.append("2. `python tools/summary_sync.py report`（裁决表 ADD/REMOVE/RENAME）")
    L.append("3. 人工裁定中文标题与归类 → `apply-add`/`apply-rename`/`apply-remove`")
    L.append("4. `python tools/rebuild_catalog.py --build`（池随快照重冻）→ `--check` 全等")
    L.append("5. `python tools/check_catalog_network.py --gate` 四门全绿")
    L.append("")
    return "\n".join(L)


def collect(fetched_path, baseline_path="baseline/catalog.json"):
    text = read_text(fetched_path)
    full = parser.parse_catalog_full(text)
    baseline = load_json(repo_path(*baseline_path.split("/")))
    summary = _slugs_from_md(read_text(repo_path("SUMMARY.md")))
    mulu = _slugs_from_md(read_text(repo_path("mu-lu-s.md")))
    rep = drift_report(full, baseline, summary, mulu, suspended_set())
    rep["snapshot"] = os.path.basename(fetched_path)
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetched", default=None, help="上游 contents.html 路径")
    ap.add_argument("--latest", action="store_true", help="取 en/_catalog 最新快照")
    ap.add_argument("--assembly", action="store_true", help="加做 B3.2 装配核验")
    ap.add_argument("--json", default=None, help="报告 JSON 输出路径")
    ap.add_argument("--md", default=None, help="报告 Markdown 输出路径")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if args.latest and not args.fetched:
        snaps = sorted(n for n in os.listdir(repo_path("en", "_catalog"))
                       if n.endswith("-contents.html"))
        if not snaps:
            print(json.dumps({"error": "en/_catalog 无快照"}, ensure_ascii=False))
            return 2
        fetched = repo_path("en", "_catalog", snaps[-1])
    elif args.fetched:
        fetched = args.fetched if os.path.isabs(args.fetched) else repo_path(args.fetched)
    else:
        print(json.dumps({"error": "需 --fetched <路径> 或 --latest"}, ensure_ascii=False))
        return 2
    if not os.path.exists(fetched):
        print(json.dumps({"error": "快照不存在: %s" % fetched}, ensure_ascii=False))
        return 2

    rep = collect(fetched)
    if args.assembly:
        rep["assembly"] = assembly_check(fetched)
        if not rep["assembly"].get("ok"):
            rep["changed"] = True

    md = render_md(rep)
    if args.json:
        with io.open(args.json, "w", encoding="utf-8", newline="\n") as f:
            json.dump(rep, f, ensure_ascii=False, indent=1)
    if args.md:
        with io.open(args.md, "w", encoding="utf-8", newline="\n") as f:
            f.write(md + "\n")
    if not args.quiet:
        print(json.dumps({k: rep[k] for k in ("changed", "upstream")}, ensure_ascii=False))
        print(md)
    return 1 if rep["changed"] else 0


if __name__ == "__main__":
    sys.exit(main())
