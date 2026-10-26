# -*- coding: utf-8 -*-
"""全量抓取+原文镜像驱动器（用户 2026-10-27 指令：把所有原文按目录抓取到 yuanwen/）。

对 baseline/catalog.json 中全部非别名词条（alias_of 为空）执行：
  fetch_entry.fetch_one（并发节拍）→ upsert_baseline → yuanwen.convert_entry
并逐 slug 留痕 script/fetch-all-log.jsonl，每 25 条写检查点
script/fetch-all-status.json（可中断续跑：--resume 跳过已登记且文件齐全者）。

并发配置（用户 2026-10-27 指定，script/probe_concurrency.py 实测均无限流）：
  A = 16 路 × 每 5 秒一请求（≈3.2 req/s）
  B = 64 路 × 每 10 秒一请求（≈6.4 req/s，默认）

用法: python tools/fetch_all.py [--config A|B] [--limit N] [--only slug...]
                                [--resume] [--no-convert] [--status-every N]
输出: stderr 进度；stdout JSON {total, fetched, converted, failures, elapsed_s}
"""
import argparse
import json
import os
import sys
import threading
import time
from queue import Empty, Queue

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import fetch, yuanwen  # noqa: E402
from tools.common import (  # noqa: E402
    ensure_dirs, load_json, repo_path, utcnow_iso, write_json_verified)
from tools.fetch_entry import fetch_one, upsert_baseline  # noqa: E402

CONFIGS = {"A": (16, 5.0), "B": (64, 10.0)}

_log_lock = threading.Lock()
_stop = threading.Event()


def _flog(rec):
    with _log_lock:
        with open(repo_path("script", "fetch-all-log.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _checkpoint(done, failed, total, cfg):
    write_json_verified(repo_path("script", "fetch-all-status.json"), {
        "at": utcnow_iso(), "config": {"channels": cfg[0], "period_s": cfg[1]},
        "done": done, "failed": failed, "total": total,
        "remaining": total - done - failed,
    })


def load_slugs(args):
    if args.only:
        return list(args.only)
    cat = load_json(repo_path("baseline", "catalog.json"))
    slugs = sorted(it["slug"] for it in cat["items"] if not it["alias_of"])
    if args.resume:
        base = load_json(repo_path("baseline", "entries.json"))
        have = {r["slug"]: r for r in base["entries"]}
        keep = []
        for s in slugs:
            rec = have.get(s)
            files = rec.get("files") if rec else None
            if rec and files and all(os.path.exists(repo_path(f["path"])) for f in files):
                continue  # 原始物齐全：跳过抓取（转换仍按 --no-convert/登记判断）
            keep.append(s)
        skipped = len(slugs) - len(keep)
        sys.stderr.write("[fetch_all] --resume：跳过已齐全 %d，待抓 %d\n" % (skipped, len(keep)))
        slugs = keep
    if args.limit:
        slugs = slugs[:args.limit]
    return slugs


def worker(q, cfg, flags, stats):
    channels, period = cfg
    pacer = fetch.Pacer(period)
    while not _stop.is_set():
        try:
            slug = q.get_nowait()
        except Empty:
            return
        rec = {"at": utcnow_iso(), "slug": slug}
        try:
            r = fetch_one(slug, fetch.MIN_DELAY, False, pacer=pacer)
            if "error" in r:
                rec.update(ok=False, stage="fetch", error=r["error"])
                stats["fail"].append(rec)
                _flog(rec)
                sys.stderr.write("[fetch_all] FAIL %s: %s\n" % (slug, r["error"]))
                q.task_done()
                continue
            upsert_baseline(r)
            rec["files"] = len(r["files"])
            rec["missing"] = len(r["missing"])
            rec["archive_edition"] = r.get("archive_edition")
            rec["ok"] = True
            stats["fetched"] += 1
            if flags["convert"]:
                try:
                    yuanwen.convert_entry(slug)
                    rec["converted"] = True
                    stats["converted"] += 1
                except Exception as exc:  # 转换失败不阻塞抓取，登记后继续
                    rec["converted"] = False
                    rec["conv_error"] = repr(exc)[:200]
                    stats["conv_fail"].append(rec)
            stats["done"] += 1
            _flog(rec)
            n = stats["done"] + stats["failed"]
            if n % 25 == 0 or n == stats["total"]:
                _checkpoint(stats["done"], stats["failed"], stats["total"], cfg)
            if n % 10 == 0:
                sys.stderr.write("[fetch_all] %d/%d fetched=%d conv_fail=%d fail=%d\n"
                                 % (n, stats["total"], stats["fetched"],
                                    len(stats["conv_fail"]), stats["failed"]))
        except fetch.FetchError as e:
            rec.update(ok=False, stage="fetch", error=str(e))
            stats["fail"].append(rec)
            stats["failed"] += 1
            _flog(rec)
            sys.stderr.write("[fetch_all] FETCH-ERR %s: %s\n" % (slug, e))
        except Exception as exc:
            rec.update(ok=False, stage="worker", error=repr(exc)[:200])
            stats["fail"].append(rec)
            stats["failed"] += 1
            _flog(rec)
            sys.stderr.write("[fetch_all] ERR %s: %r\n" % (slug, exc))
        finally:
            q.task_done()


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="B", choices=sorted(CONFIGS),
                    help="A=16路×5s；B=64路×10s（默认，实测无限流）")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--resume", action="store_true",
                    help="跳过原始物已齐全的词条（断点续跑）")
    ap.add_argument("--no-convert", action="store_true", help="只抓取不转换")
    args = ap.parse_args(argv)
    ensure_dirs()

    cfg = CONFIGS[args.config]
    slugs = load_slugs(args)
    total = len(slugs)
    if not total:
        print(json.dumps({"error": "无待处理词条"}, ensure_ascii=False))
        return 0
    sys.stderr.write("[fetch_all] 配置 %s：%d 路 × 每 %g 秒，共 %d 词条\n"
                     % (args.config, cfg[0], cfg[1], total))

    stats = {"done": 0, "failed": 0, "fetched": 0, "converted": 0,
             "fail": [], "conv_fail": [], "total": total}
    flags = {"convert": not args.no_convert}
    q = Queue()
    for s in slugs:
        q.put(s)
    t0 = time.time()
    threads = [threading.Thread(target=worker, args=(q, cfg, flags, stats), daemon=True)
               for _ in range(cfg[0])]
    for t in threads:
        t.start()
    q.join()
    _stop.set()
    _checkpoint(stats["done"], stats["failed"], total, cfg)

    out = {"total": total, "fetched": stats["fetched"], "converted": stats["converted"],
           "fetch_failures": stats["fail"], "convert_failures": stats["conv_fail"],
           "elapsed_s": round(time.time() - t0, 1)}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 1 if (stats["fail"] or stats["conv_fail"]) else 0


if __name__ == "__main__":
    sys.exit(main())
