# -*- coding: utf-8 -*-
"""2026-11-28 安全审计回归：抓取白名单、包内路径包含、凭证脱敏。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.common import contained_path  # noqa: E402
from tools.cnki_query import redact_secrets  # noqa: E402
from tools.fetch import FetchError, _validate_url  # noqa: E402

JWT = ("eyJhbGciOiJIUzI1NiJ9."
       "eyJleHAiOjE3OTgxNzE2OTcsInVzZXJuYW1lIjoiMTc3NjQwMzE1MTcifQ."
       "CXjcnv6q1uQKeibgnbTpWJ66-7hDHefbCsi_AKGEM_E")


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


class TestFetchAllowlist(unittest.TestCase):
    def test_allows_sep_hosts(self):
        _validate_url("https://plato.stanford.edu/entries/abduction/")
        _validate_url("http://www.plato.stanford.edu/contents.html")

    def test_rejects_other_schemes_and_hosts(self):
        for url in ("file:///etc/passwd", "http://127.0.0.1/x",
                    "https://evil.example/x", "ftp://plato.stanford.edu/x"):
            with self.assertRaises(FetchError):
                _validate_url(url)


class TestRedactSecrets(unittest.TestCase):
    def test_redacts_bare_jwt(self):
        out = redact_secrets("操作失败：%s 非法" % JWT)
        self.assertNotIn(JWT, out)
        self.assertIn("[REDACTED-JWT]", out)

    def test_redacts_token_query(self):
        out = redact_secrets("...?token=%s&x=1" % JWT)
        self.assertNotIn(JWT, out)

    def test_keeps_plain_text(self):
        text = "belief 在术语在线审定库有 3 条命中"
        self.assertEqual(redact_secrets(text), text)


if __name__ == "__main__":
    unittest.main()
