#!/usr/bin/env python3
"""同步上游官方目录基线 .github/sep-baseline/official-snapshot.json（第五方）。

背景：目录四方（zh SUMMARY／en SUMMARY／contents.html 快照／mu-lu-s）由
check_catalog_network --gate 覆盖；但 rebuild_dir check 另用
.github/sep-baseline/official-snapshot.json 作上游 slug 权威。该文件自
2026-11-15 后无刷新机制（旧周检脚本已随 ADR 撤除），会停留在旧快照，
把上游已改名/新增的条目误报成"缺 yuanwen 镜像"。

本工具从本地冻结的 contents.html 快照重新解析出 main/alias，与现行基线
比对；--write 才写回。解析规则沿用旧周检脚本（li → strong 标题 + 作者，
"X — see Y" 为别名），保证与基线同构，差异只反映上游真实变化。

用法：
  python tools/sync_official_snapshot.py --check          # 只比对，输出 JSON
  python tools/sync_official_snapshot.py --write          # 写回基线
  python tools/sync_official_snapshot.py --snap 20261122T021217Z-contents.html --write
"""
import argparse
import html as htmlmod
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / ".github" / "sep-baseline" / "official-snapshot.json"
CATDIR = ROOT / "en" / "_catalog"
MIN_MAIN = 1800
MIN_ALIAS = 600

LI_RE = re.compile(r"\s*<li>\s*(.*?)\s*(?:</li>)?\s*$", re.S)
ALIAS_RE = re.compile(r"^(.*?)\s*[—–]\s*see\s+")


def latest_snap():
    snaps = sorted(CATDIR.glob("*contents.html"))
    if not snaps:
        raise SystemExit("en/_catalog 下没有 contents.html 快照")
    return snaps[-1]


def parse_contents(raw):
    """行级解析官方目录。返回 (main: {slug: {title, authors}}, alias: [{alias, slug}], dup)。"""
    text = htmlmod.unescape(raw.decode("utf-8", errors="replace"))
    main, alias, dup = {}, [], []
    for line in text.splitlines():
        if 'href="entries/' not in line:
            continue
        sm = re.search(r'href="entries/([^"/]+)/"', line)
        if not sm:
            continue
        slug = sm.group(1)
        lm = LI_RE.match(line)
        inner = lm.group(1) if lm else line
        am = ALIAS_RE.match(inner)
        if am and "<strong>" not in inner:
            alias.append({"alias": re.sub(r"<[^>]+>", "", am.group(1)).strip(), "slug": slug})
            continue
        tm = re.search(r"<strong>(.*?)</strong>", inner)
        if not tm:
            continue
        title = re.sub(r"<[^>]+>", "", tm.group(1)).strip()
        authors = re.sub(r"<[^>]+>", "", inner[tm.end():])
        authors = re.sub(r"\s+", " ", authors).strip().strip("()").strip()
        if slug in main:
            dup.append(slug)
        main[slug] = {"title": title, "authors": authors}
    return main, alias, dup


def snap_time(snap):
    m = re.match(r"(\d{8})T(\d{6})Z", snap.name)
    if not m:
        return time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    d, t = m.group(1), m.group(2)
    return f"{d[:4]}-{d[4:6]}-{d[6:]} {t[:2]}:{t[2:4]}:{t[4:]} UTC"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--snap", help="contents.html 快照文件名（默认最新）")
    ap.add_argument("--check", action="store_true", help="只比对不写回")
    ap.add_argument("--write", action="store_true", help="写回基线")
    a = ap.parse_args(argv)

    snap = CATDIR / a.snap if a.snap else latest_snap()
    if not snap.exists():
        raise SystemExit(f"快照不存在：{snap}")
    main_new, alias_new, dup = parse_contents(snap.read_bytes())
    if len(main_new) < MIN_MAIN or len(alias_new) < MIN_ALIAS:
        raise SystemExit(f"解析结果异常（main {len(main_new)} / alias {len(alias_new)}），"
                         f"低于护栏 {MIN_MAIN}/{MIN_ALIAS}，不写回")

    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    bm, ba = base.get("main", {}), base.get("alias", [])
    b_alias = {(x["alias"], x["slug"]) for x in ba}
    n_alias = {(x["alias"], x["slug"]) for x in alias_new}

    report = {
        "snapshot": snap.name,
        "baseline_fetched_at": base.get("fetched_at"),
        "new_fetched_at": snap_time(snap),
        "main": {"old": len(bm), "new": len(main_new), "duplicates": dup,
                 "added": sorted(set(main_new) - set(bm)),
                 "removed": sorted(set(bm) - set(main_new))},
        "alias": {"old": len(ba), "new": len(alias_new),
                  "added": sorted(n_alias - b_alias),
                  "removed": sorted(b_alias - n_alias)},
    }
    report["title_changed"] = [
        {"slug": s, "old": bm[s]["title"], "new": main_new[s]["title"]}
        for s in sorted(set(bm) & set(main_new))
        if bm[s].get("title") != main_new[s].get("title")]
    report["authors_changed"] = [
        {"slug": s, "old": bm[s].get("authors"), "new": main_new[s].get("authors")}
        for s in sorted(set(bm) & set(main_new))
        if bm[s].get("authors") != main_new[s].get("authors")]
    report["changed"] = bool(report["main"]["added"] or report["main"]["removed"]
                             or report["alias"]["added"] or report["alias"]["removed"]
                             or report["title_changed"] or report["authors_changed"]
                             or dup)

    if a.write:
        doc = {"fetched_at": report["new_fetched_at"], "main": main_new, "alias": alias_new}
        BASELINE.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n",
                            encoding="utf-8", newline="\n")
        report["written"] = True
    else:
        report["written"] = False

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
