# -*- coding: utf-8 -*-
"""抓取词条完整词条包：正文 + 脚注 + 补充材料 + 图片 + 元数据（FR-001…005）。

用法: python tools/fetch_entry.py <slug>... [--force] [--delay N]
输出: stdout JSON {fetched: [...], failures: [...]}
登记: baseline/entries.json（slug 主键 upsert，写后读回自校验）
落盘: en/<slug>/index.html、notes.html、<补充>.html、<图片>（不可变原始副本）

缺省件政策（spec Edge cases）：正文引用了 notes.html/补充材料/图片才去抓；
404 记入 missing[]（显式缺省，不算失败）；网络错误重试耗尽记 failures[]。
"""
import argparse
import json
import os
import re
import sys

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import fetch, parser
from tools.common import ensure_dirs, load_json, repo_path, sha256_file, utcnow_iso, write_json_verified

BASE = fetch.BASE
ARCHINFO = BASE + "/cgi-bin/encyclopedia/archinfo.cgi?entry=%s"
ENTRY_URL = BASE + "/entries/%s/"


def fetch_one(slug, delay, force):
    rec = {"slug": slug, "fetched_at": utcnow_iso(), "source_url": ENTRY_URL % slug}
    edir = repo_path("en", slug)
    os.makedirs(edir, exist_ok=True)
    files, missing = [], []

    status, data = fetch.get(ENTRY_URL % slug, delay=delay)
    if status != 200:
        return {"slug": slug, "error": "index.html HTTP %s" % status}
    idx_path = os.path.join(edir, "index.html")
    if force or not os.path.exists(idx_path):
        with open(idx_path, "wb") as f:
            f.write(data)
    entry = parser.parse_entry(open(idx_path, "rb").read().decode("utf-8", "replace"))
    pub = next((b for b in entry["blocks"] if b["type"] == "pubinfo"), None)
    rec["title"] = entry["title"]
    rec["authors"] = entry["authors"]
    rec["pubinfo"] = {"first_published": pub["first_published"] if pub else None,
                      "substantive_revision": pub["substantive_revision"] if pub else None}
    rec["in_article_markers"] = entry["in_article_markers"]

    def save(relpath, payload):
        path = os.path.join(edir, relpath.replace("/", os.sep))
        if force or not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(payload)
        return {"path": "en/%s/%s" % (slug, relpath), "sha256": sha256_file(path),
                "bytes": os.path.getsize(path)}

    files.append({"path": "en/%s/index.html" % slug, "sha256": sha256_file(idx_path),
                  "bytes": os.path.getsize(idx_path), "kind": "main"})

    # 脚注：正文有引用才抓（spec：404 为显式缺省件）
    if entry["notes_refs"]:
        st, notes = fetch.get(ENTRY_URL % slug + "notes.html", delay=delay)
        if st == 200:
            files.append(dict(save("notes.html", notes), kind="notes"))
        else:
            missing.append({"expected": "notes.html", "http_status": st})

    # 补充材料：正文相对链接
    for supp in entry["supplements"]:
        st, body = fetch.get(ENTRY_URL % slug + supp, delay=delay)
        if st == 200:
            files.append(dict(save(supp, body), kind="supplement"))
        else:
            missing.append({"expected": supp, "http_status": st})

    # 图片：词条目录相对路径（排除站点框架图与外链）
    for img in entry["images"]:
        src = img["src"]
        rel = src.split("?")[0]
        if rel.startswith(("../", "http:", "https:", "/")):
            continue
        st, body = fetch.get(ENTRY_URL % slug + rel, delay=delay)
        if st == 200:
            files.append(dict(save(rel, body), kind="image"))
        else:
            missing.append({"expected": rel, "http_status": st})

    # archinfo：权威版本核对（FR-003/008）
    st, ai = fetch.get(ARCHINFO % slug, delay=delay)
    rec["archinfo"] = parser.parse_archinfo(ai.decode("utf-8", "replace")) if st == 200 else {
        "error": "HTTP %s" % st}
    rec["archive_edition"] = rec["archinfo"].get("latest_edition")

    rec["files"] = files
    rec["missing"] = missing
    return rec


def upsert_baseline(rec):
    path = repo_path("baseline", "entries.json")
    if os.path.exists(path):
        base = load_json(path)
    else:
        base = {"schema": "sep-cn-baseline/1", "entries": []}
    entries = [e for e in base["entries"] if e["slug"] != rec["slug"]]
    entries.append(rec)
    entries.sort(key=lambda e: e["slug"])
    base["entries"] = entries
    base["updated_at"] = utcnow_iso()
    write_json_verified(path, base)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="+")
    ap.add_argument("--force", action="store_true", help="重抓覆盖本地原始副本")
    ap.add_argument("--delay", type=float, default=fetch.MIN_DELAY)
    args = ap.parse_args(argv)
    ensure_dirs()

    fetched, failures = [], []
    for slug in args.slugs:
        sys.stderr.write("[fetch_entry] %s ...\n" % slug)
        try:
            rec = fetch_one(slug, args.delay, args.force)
        except fetch.FetchError as e:
            failures.append({"slug": slug, "error": str(e)})
            continue
        if "error" in rec:
            failures.append(rec)
            continue
        upsert_baseline(rec)
        fetched.append({"slug": slug, "files": len(rec["files"]),
                        "missing": rec["missing"], "archive_edition": rec["archive_edition"]})
        sys.stderr.write("[fetch_entry] %s OK: %d files, %d missing\n"
                         % (slug, len(rec["files"]), len(rec["missing"])))
    print(json.dumps({"fetched": fetched, "failures": failures},
                     ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
