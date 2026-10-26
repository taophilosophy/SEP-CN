# -*- coding: utf-8 -*-
"""礼貌抓取层：相邻请求 ≥5 秒（宪法 V）、退避重试、逐请求留痕。

robots 政策：用户已于 2026-10-26 明确授权绕过 robots.txt 目录禁区
（含 /archives/，见 specs/001-sep-sync-pipeline/spec.md Assumptions）；
但 crawl-delay: 5 保留为默认礼貌下限——本模块把间隔做成硬约束，
调用方只能调大（--delay），不能调小。
"""
import json
import time
import urllib.error
import urllib.request

from tools.common import http_log_path, sha256_bytes
from datetime import datetime, timezone

def _now_ms():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

BASE = "https://plato.stanford.edu"
UA = "SEP-CN-translation-pipeline/0.1 (GitBook community project; contact via github.com/taophilosophy/SEP-CN)"
MIN_DELAY = 5.0

_last_ts = [0.0]


def _wait(delay):
    gap = time.time() - _last_ts[0]
    if _last_ts[0] > 0 and gap < delay:
        time.sleep(delay - gap)
    _last_ts[0] = time.time()


def _log(record):
    with open(http_log_path(), "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def get(url, dest=None, delay=None, retries=3, timeout=60):
    """GET 一个 URL。

    返回 (status, data)。dest 给出时同时落盘该文件（原始字节，不可变副本）。
    429/5xx/URLError 指数退避重试；重试耗尽抛 FetchError（显式失败，
    禁止静默跳过——宪法 V）。成功与失败都写 script/http-log.jsonl。
    """
    if delay is None:
        delay = MIN_DELAY
    delay = max(delay, MIN_DELAY)
    last_err = None
    for attempt in range(retries + 1):
        _wait(delay)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
                status = resp.status
            if dest:
                with open(dest, "wb") as f:
                    f.write(data)
                    f.flush()
            _log({"at": _now_ms(), "url": url, "status": status,
                  "bytes": len(data), "sha256": sha256_bytes(data), "attempt": attempt})
            return status, data
        except urllib.error.HTTPError as e:
            last_err = e
            _log({"at": _now_ms(), "url": url, "status": e.code,
                  "bytes": 0, "attempt": attempt, "error": "HTTPError"})
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(MIN_DELAY * (2 ** attempt))
                continue
            if 400 <= e.code < 500:
                # 4xx（含 404 缺省件）不重试，直接返回让调用方登记
                return e.code, b""
            raise FetchError(url, e.code, str(e))
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = e
            _log({"at": _now_ms(), "url": url, "status": None,
                  "attempt": attempt, "error": str(e)})
            if attempt < retries:
                time.sleep(MIN_DELAY * (2 ** attempt))
                continue
            raise FetchError(url, None, str(last_err))
    raise FetchError(url, None, str(last_err))  # pragma: no cover


class FetchError(Exception):
    def __init__(self, url, status, detail):
        super().__init__("fetch failed: %s (status=%s): %s" % (url, status, detail))
        self.url = url
        self.status = status
