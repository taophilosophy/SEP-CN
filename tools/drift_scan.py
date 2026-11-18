# -*- coding: utf-8 -*-
"""全量回源 sha 核对（ADR-0045 跟进项，用户 2026-11-15 批准）。

对 baseline/entries.json 全部词条抓取 live index.html，sha256 与原始网页钉
（files[].sha256）比对——只读审计：不写 en/、不动台账、不登记分歧；
真漂移清单供 compare.py/update 任务消费。撤稿/归档版词条（source_url 含
/archives/）单列跳过；retired 词条照抓，软 404 如实分类。

用法:
  python tools/drift_scan.py [--limit N] [--only slug...] [--channels 64] [--report]
输出: stdout JSON 汇总（scanned/unchanged/changed/soft404/http_404/failures/…）；
      --report 另落盘 specs/001-sep-sync-pipeline/results/drift-scan-<ts>.json
      （write_json_verified）。
退出码: 0 完成（有漂移也是 0——漂移是发现不是错误）；1 全部失败；2 用法。
留痕: 全部请求经 tools/fetch.py 写 script/http-log.jsonl；429/5xx 退避重试不变。
"""
import argparse
import io
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import fetch
from tools.common import load_json, repo_path, sha256_bytes, utcnow_iso, write_json_verified
from tools.fetch_entry import ENTRY_URL, is_soft404

# stdout 重包守卫：CI/unittest 下可能已是被别的模块重包过的流，重复包会关闭底层 buffer
if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8")


def scan_one(slug, pin):
    """抓 live 主文件并与钉比对 → (slug, 分类, 详情)。"""
    url = ENTRY_URL % slug
    try:
        status, data = fetch.get(url)
    except fetch.FetchError as e:
        return slug, "failure", {"slug": slug, "error": str(e)}
    if status == 200:
        if is_soft404(data[:4096].decode("utf-8", "replace")):
            return slug, "soft404", {"slug": slug, "note": "软 404（SEP 错误页）"}
        live = sha256_bytes(data)
        if live == pin:
            return slug, "unchanged", None
        return slug, "changed", {"slug": slug, "pin_sha256": pin, "live_sha256": live}
    if status == 404:
        return slug, "http_404", {"slug": slug, "http_status": 404}
    return slug, "http_error", {"slug": slug, "http_status": status}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="只扫前 N 条（试金石）")
    ap.add_argument("--only", nargs="+", help="只扫指定 slug")
    ap.add_argument("--channels", type=int, default=64,
                    help="并发通道数（默认 64）")
    ap.add_argument("--report", action="store_true", help="报告落盘 results/drift-scan-<ts>.json")
    args = ap.parse_args(argv)

    base = load_json(repo_path("baseline", "entries.json"))
    want = set(args.only) if args.only else None
    items = []
    for r in base["entries"]:
        if want and r["slug"] not in want:
            continue
        main_f = next((f for f in r.get("files", []) if f.get("kind") == "main"), None)
        if main_f is None:
            continue
        if "/archives/" in r.get("source_url", ""):
            continue  # 撤稿/归档版词条：上游冻结，单列跳过
        items.append((r["slug"], main_f["sha256"]))
    if args.limit:
        items = items[:args.limit]

    total = len(items)
    sys.stderr.write("[drift_scan] %d 词条，%d 路并发\n"
                     % (total, args.channels))
    counts = {"unchanged": 0, "changed": 0, "soft404": 0, "http_404": 0,
              "http_error": 0, "failure": 0}
    changed, soft404, http_404, http_error, failures = [], [], [], [], []
    done = 0
    with ThreadPoolExecutor(max_workers=args.channels) as pool:
        futs = [pool.submit(scan_one, slug, pin)
                for i, (slug, pin) in enumerate(items)]
        for fut in futs:
            slug, kind, detail = fut.result()
            counts[kind] += 1
            if kind == "changed":
                changed.append(detail)
            elif kind == "soft404":
                soft404.append(detail)
            elif kind == "http_404":
                http_404.append(detail)
            elif kind == "http_error":
                http_error.append(detail)
            elif kind == "failure":
                failures.append(detail)
            done += 1
            if done % 100 == 0:
                sys.stderr.write("[drift_scan] %d/%d（changed=%d failure=%d）\n"
                                 % (done, total, counts["changed"], counts["failure"]))

    out = {"at": utcnow_iso(), "scope": "main index.html vs files[].sha256 原始钉",
           "channels": args.channels, "total": total,
           **counts,
           "changed": sorted(changed, key=lambda x: x["slug"]),
           "soft404": sorted(soft404, key=lambda x: x["slug"]),
           "http_404": sorted(http_404, key=lambda x: x["slug"]),
           "http_error": sorted(http_error, key=lambda x: x["slug"]),
           "failures": sorted(failures, key=lambda x: x["slug"])}
    if args.report:
        ts = out["at"].replace(":", "").replace("-", "")
        rp = repo_path("specs", "001-sep-sync-pipeline", "results",
                       "drift-scan-%s.json" % ts)
        write_json_verified(rp, out)
        out["report"] = os.path.relpath(rp, repo_path(".")).replace(os.sep, "/")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0 if total == 0 or counts["unchanged"] + counts["changed"] + \
        counts["soft404"] + counts["http_404"] + counts["http_error"] > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
