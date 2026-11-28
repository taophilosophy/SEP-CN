# -*- coding: utf-8 -*-
"""抓取层：退避重试、逐请求留痕、显式失败。

2026-11-18 废除礼貌抓取间隔规则（ADR-0069；宪法 V 修订为 v1.4.0，条目改题
「抓取失败显式化」）：相邻请求最小间隔、串行节拍与 Pacer 一并删除——本层
不再设置任何强制间隔，调用方自担并发决策。退避重试、逐请求留痕、禁止静默
跳过三条纪律保留不变。

robots 政策：用户已于 2026-10-26 明确授权绕过 robots.txt 目录禁区
（含 /archives/，见 specs/001-sep-sync-pipeline/spec.md Assumptions）。
"""
import json
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

from tools.common import http_log_path, sha256_bytes
from datetime import datetime, timezone

def _now_ms():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

BASE = "https://plato.stanford.edu"
ALLOWED_SCHEMES = ("http", "https")
ALLOWED_HOSTS = frozenset({"plato.stanford.edu", "www.plato.stanford.edu"})
UA = "SEP-CN-translation-pipeline/0.1 (GitBook community project; contact via github.com/taophilosophy/SEP-CN)"

# 退避基数（秒）：第 n 次重试前睡 BACKOFF_S * 2**n。属重试策略，非请求间隔。
BACKOFF_S = 1.0

_log_lock = threading.Lock()


def _log(record):
    with _log_lock:
        with open(http_log_path(), "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def _log_rejected(url, detail):
    """白名单拒绝也留痕；日志目录缺失时不掩盖策略错误。"""
    try:
        _log({"at": _now_ms(), "url": url, "status": None, "bytes": 0,
              "attempt": 0, "error": "url_rejected: %s" % detail})
    except OSError:
        pass


def get(url, dest=None, retries=3, timeout=60):
    """GET 一个 URL。

    返回 (status, data)。dest 给出时同时落盘该文件（原始字节，不可变副本）。
    429/5xx/URLError 指数退避重试；重试耗尽抛 FetchError（显式失败，禁止
    静默跳过——宪法 V）。成功与失败都写 script/http-log.jsonl。
    """
    last_err = None
    try:
        _validate_url(url)
    except FetchError as exc:
        _log_rejected(url, str(exc))
        raise
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with _OPENER.open(req, timeout=timeout) as resp:
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
                time.sleep(BACKOFF_S * (2 ** attempt))
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
                time.sleep(BACKOFF_S * (2 ** attempt))
                continue
            raise FetchError(url, None, str(last_err))
        except FetchError as e:
            # 重定向目标被白名单拒绝：不重试，留痕后原样抛出
            _log_rejected(e.url, str(e))
            raise
    raise FetchError(url, None, str(last_err))  # pragma: no cover


class FetchError(Exception):
    def __init__(self, url, status, detail):
        super().__init__("fetch failed: %s (status=%s): %s" % (url, status, detail))
        self.url = url
        self.status = status


def _validate_url(url):
    """抓取白名单：只允许 http/https、SEP 主机与标准端口，防目录/词条数据诱导 SSRF。"""
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower()
    if parts.scheme not in ALLOWED_SCHEMES or host not in ALLOWED_HOSTS:
        raise FetchError(url, None,
                         "URL 不在抓取白名单（仅 http/https + plato.stanford.edu）")
    try:
        port = parts.port
    except ValueError:
        port = -1
    expected = 443 if parts.scheme == "https" else 80
    if port not in (None, expected) or parts.username or parts.password:
        raise FetchError(url, None, "URL 端口或用户信息不在抓取白名单")


class _SafeRedirect(urllib.request.HTTPRedirectHandler):
    """重定向目标同样过白名单，避免首跳合法、二跳转向内网。"""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _validate_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_SafeRedirect())
