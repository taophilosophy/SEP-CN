# -*- coding: utf-8 -*-
"""抓取 contents.html 目录快照并与基线 diff（FR-007）。

用法: python tools/fetch_catalog.py [--force]
输出: stdout JSON {fetched_at, entries, aliases, new_vs_baseline:{added,removed,renamed,alias_changed}}
落盘: en/_catalog/<时间戳>-contents.html（不可变）、baseline/catalog.json（最新解析，入库）
"""
import argparse
import json
import re
import sys

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import fetch, parser
from tools.common import ensure_dirs, load_json, repo_path, utcnow_iso, write_json_verified
from tools.fetch_entry import ENTRY_URL

CATALOG_URL = fetch.BASE + "/contents.html"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--reparse", action="store_true",
                    help="离线重建：用 en/_catalog 最新快照重新解析并写 baseline/catalog.json，"
                         "不联网（解析器修复后使快照与解析结果重新一致）")
    ap.add_argument("--reparse-snap", default=None,
                    help="specs/054：--reparse 指定快照文件名（默认取最新），供跨时点账重建")
    ap.add_argument("--snapshot-only", action="store_true",
                    help="只抓快照落 en/_catalog，不写 baseline/catalog.json（CI 巡检用；"
                         "避免在只读检出的工作区写跟踪文件）")
    args = ap.parse_args(argv)
    ensure_dirs()

    if args.reparse:
        snaps = sorted(n for n in __import__("os").listdir(repo_path("yuanwen", "_catalog"))
                       if n.endswith("-contents.html"))
        if not snaps:
            print(json.dumps({"error": "yuanwen/_catalog 无快照"}, ensure_ascii=False))
            return 1
        raw_name = args.reparse_snap if args.reparse_snap else snaps[-1]
        if args.reparse_snap and args.reparse_snap not in snaps:
            print(json.dumps({"error": "快照不存在: %s" % args.reparse_snap}, ensure_ascii=False))
            return 1
        raw_path = repo_path("yuanwen", "_catalog", raw_name)
        m = re.match(r"(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})Z-", snaps[-1])
        fetched_at = ("%s-%s-%sT%s:%s:%sZ" % m.groups()) if m else utcnow_iso()
        data = open(raw_path, "rb").read()
    else:
        ts = utcnow_iso().replace(":", "").replace("-", "")
        raw_path = repo_path("yuanwen", "_catalog", "%s-contents.html" % ts)
        status, data = fetch.get(CATALOG_URL, dest=raw_path)
        if status != 200:
            print(json.dumps({"error": "contents.html HTTP %s" % status}, ensure_ascii=False))
            return 1
        fetched_at = utcnow_iso()

    full = parser.parse_catalog_full(data.decode("utf-8", "replace"))
    # items 保持旧账的 slug 排序（页序由 doc_order 字段承载，specs/054 A1）
    items = sorted(full["items"], key=lambda x: x["slug"])
    if args.snapshot_only:
        print(json.dumps({"fetched_at": fetched_at,
                          "snapshot": "yuanwen/_catalog/" + __import__("os").path.basename(raw_path),
                          "entries": len(items),
                          "alias_rows": len(full["alias_rows"]),
                          "cluster_mothers": len(full["cluster_mothers"]),
                          "snapshot_only": True}, ensure_ascii=False))
        return 0
    catalog = {"fetched_at": fetched_at,
               "source": "yuanwen/_catalog/" + __import__("os").path.basename(raw_path),
               "items": items,
               "alias_rows": sorted(full["alias_rows"], key=lambda x: x["doc_order"]),
               "cluster_mothers": sorted(full["cluster_mothers"], key=lambda x: x["doc_order"])}
    write_json_verified(repo_path("baseline", "catalog.json"), catalog)

    # 与上次目录对比（无上次则全部视为 added 之外保持空 diff）
    prev_path = None
    for name in sorted(__import__("os").listdir(repo_path("yuanwen", "_catalog"))):
        if name.endswith("-contents.html") and name != __import__("os").path.basename(raw_path):
            prev_path = repo_path("yuanwen", "_catalog", name)
    diff = {"added": [], "removed": [], "renamed": [], "alias_changed": []}
    if prev_path:
        prev = parser.parse_catalog(open(prev_path, "rb").read().decode("utf-8", "replace"))
        prev_map = {i["slug"]: i for i in prev}
        cur_map = {i["slug"]: i for i in items}
        diff["added"] = sorted(set(cur_map) - set(prev_map))
        diff["removed"] = sorted(set(prev_map) - set(cur_map))
        for slug in set(prev_map) & set(cur_map):
            if prev_map[slug]["title"] != cur_map[slug]["title"]:
                diff["renamed"].append({"slug": slug, "old": prev_map[slug]["title"],
                                        "new": cur_map[slug]["title"]})
            if bool(prev_map[slug]["alias_of"]) != bool(cur_map[slug]["alias_of"]):
                diff["alias_changed"].append(slug)

    summary = {"fetched_at": catalog["fetched_at"], "entries": len(items),
               "aliases": len(catalog["alias_rows"]),
               "raw": raw_path,
               "reparse": bool(args.reparse),
               "new_vs_baseline": diff}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
