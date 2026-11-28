# -*- coding: utf-8 -*-
"""2026-11-28 安全审计回归：抓取白名单、包内路径包含、凭证脱敏。"""
import os
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.common import contained_path  # noqa: E402
from tools.cnki_query import redact_secrets  # noqa: E402
from tools.fetch import FetchError, _validate_url  # noqa: E402
from tools.net_guard import validate_public_url  # noqa: E402

# 完全合成的测试 JWT：用户名与到期时间均与任何真实凭证无关。
JWT = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
       "eyJzdWIiOiJmaXh0dXJlLXVzZXIiLCJleHAiOjE2MDAwMDAwMDB9."
       "Zml4dHVyZS1zaWduYXR1cmUtbm90LXNlY3JldA")


class TestContainedPath(unittest.TestCase):
    def test_accepts_relative_inside(self):
        with tempfile.TemporaryDirectory() as d:
            p = contained_path(d, "images", "figure1.jpg")
            self.assertEqual(os.path.realpath(p),
                             os.path.realpath(os.path.join(d, "images", "figure1.jpg")))

    def test_rejects_parent_escape(self):
        with tempfile.TemporaryDirectory() as d:
            for rel in ("../x", "a/../../x", os.path.join(d, "..", "x")):
                with self.assertRaises(ValueError):
                    contained_path(d, rel)

    def test_rejects_base_outside_root(self):
        with tempfile.TemporaryDirectory() as root, tempfile.TemporaryDirectory() as outside:
            with self.assertRaises(ValueError):
                contained_path(outside, "x", root=root)
            self.assertTrue(contained_path(os.path.join(root, "sub"), "x", root=root))


class TestFetchAllowlist(unittest.TestCase):
    def test_allows_sep_hosts(self):
        _validate_url("https://plato.stanford.edu/entries/abduction/")
        _validate_url("http://www.plato.stanford.edu/contents.html")
        _validate_url("https://plato.stanford.edu:443/contents.html")
        _validate_url("http://plato.stanford.edu:80/contents.html")

    def test_rejects_other_schemes_and_hosts(self):
        for url in ("file:///etc/passwd", "http://127.0.0.1/x",
                    "https://evil.example/x", "ftp://plato.stanford.edu/x"):
            with self.assertRaises(FetchError):
                _validate_url(url)

    def test_rejects_nonstandard_port_and_userinfo(self):
        for url in ("https://plato.stanford.edu:8443/x",
                    "http://plato.stanford.edu:443/x",
                    "https://user:pass@plato.stanford.edu/x"):
            with self.assertRaises(FetchError):
                _validate_url(url)


class TestRedactSecrets(unittest.TestCase):
    def test_redacts_bare_jwt(self):
        out = redact_secrets("操作失败：%s 非法" % JWT)
        self.assertNotIn(JWT, out)
        self.assertIn("[REDACTED-JWT]", out)

    def test_redacts_token_query(self):
        out = redact_secrets("...?token=opaque-not-a-jwt-123&x=1")
        self.assertNotIn("opaque-not-a-jwt-123", out)
        self.assertIn("[REDACTED]", out)

    def test_keeps_plain_text(self):
        text = "belief 在术语在线审定库有 3 条命中"
        self.assertEqual(redact_secrets(text), text)


class TestPublicUrlGuard(unittest.TestCase):
    PUBLIC = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 443))]
    PRIVATE = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("127.0.0.1", 443))]

    def test_allows_public_address(self):
        with patch("tools.net_guard.socket.getaddrinfo", return_value=self.PUBLIC):
            validate_public_url("https://example.com/x")

    def test_rejects_loopback(self):
        with patch("tools.net_guard.socket.getaddrinfo", return_value=self.PRIVATE):
            with self.assertRaises(ValueError):
                validate_public_url("https://example.com/x")

    def test_rejects_non_http(self):
        with self.assertRaises(ValueError):
            validate_public_url("file:///etc/passwd")


if __name__ == "__main__":
    unittest.main()
