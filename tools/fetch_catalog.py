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
    args = ap.parse_args(argv)
    ensure_dirs()

    if args.reparse:
        snaps = sorted(n for n in __import__("os").listdir(repo_path("en", "_catalog"))
                       if n.endswith("-contents.html"))
        if not snaps:
            print(json.dumps({"error": "en/_catalog 无快照"}, ensure_ascii=False))
            return 1
        raw_path = repo_path("en", "_catalog", snaps[-1])
        m = re.match(r"(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})Z-", snaps[-1])
        fetched_at = ("%s-%s-%sT%s:%s:%sZ" % m.groups()) if m else utcnow_iso()
        data = open(raw_path, "rb").read()
    else:
        ts = utcnow_iso().replace(":", "").replace("-", "")
        raw_path = repo_path("en", "_catalog", "%s-contents.html" % ts)
        status, data = fetch.get(CATALOG_URL, dest=raw_path, delay=fetch.MIN_DELAY)
        if status != 200:
            print(json.dumps({"error": "contents.html HTTP %s" % status}, ensure_ascii=False))
            return 1
        fetched_at = utcnow_iso()

    items = parser.parse_catalog(data.decode("utf-8", "replace"))
    catalog = {"fetched_at": fetched_at, "source": raw_path, "items": items}
    write_json_verified(repo_path("baseline", "catalog.json"), catalog)

    # 与上次目录对比（无上次则全部视为 added 之外保持空 diff）
    prev_path = None
    for name in sorted(__import__("os").listdir(repo_path("en", "_catalog"))):
        if name.endswith("-contents.html") and name != __import__("os").path.basename(raw_path):
            prev_path = repo_path("en", "_catalog", name)
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
               "aliases": sum(len(i.get("aliases", [])) for i in items)
                          + len([i for i in items if i["alias_of"]]),
               "raw": raw_path,
               "reparse": bool(args.reparse),
               "new_vs_baseline": diff}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
