# -*- coding: utf-8 -*-
"""外部链接的公网可达性护栏（链接检查器用，2026-11-28 安全审计）。

链接检查器按设计要访问条目引用的任意外部 URL；这些 URL 来自上游 HTML，属外部
输入。只允许 http/https 且解析结果必须是公网地址，避免被一条 `http://127.0.0.1`
或云元数据地址诱导本机发起内网请求。重定向逐跳复验。

DNS 解析与实际连接之间仍存在理论上的重绑定窗口；本模块面向本机审计工具，
不承诺对抗拥有 DNS 控制权的攻击者。
"""
from __future__ import annotations

import ipaddress
import socket
import urllib.parse
import urllib.request


def validate_public_url(url):
    """http/https + 解析结果全为公网地址，否则抛 ValueError。"""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ("http", "https"):
        raise ValueError("只允许 http/https：%s" % url)
    host = parts.hostname
    if not host:
        raise ValueError("URL 缺少主机：%s" % url)
    port = parts.port or (443 if parts.scheme == "https" else 80)
    try:
        infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    except socket.gaierror as exc:
        raise ValueError("主机无法解析：%s" % host) from exc
    if not infos:
        raise ValueError("主机无地址：%s" % host)
    for info in infos:
        addr = info[4][0].split("%", 1)[0]
        try:
            ip = ipaddress.ip_address(addr)
        except ValueError as exc:
            raise ValueError("无法识别的地址：%s" % addr) from exc
        if not ip.is_global:
            raise ValueError("非公网地址：%s（%s）" % (addr, host))


class _PublicRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_PublicRedirect())


def open_public(req, timeout=30):
    """按公网护栏打开请求；重定向目标逐跳校验。"""
    return _OPENER.open(req, timeout=timeout)
