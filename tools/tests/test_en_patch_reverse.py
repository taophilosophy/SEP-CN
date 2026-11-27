# -*- coding: utf-8 -*-
"""补丁池可逆性单测（specs/053 §9 公理 A6；Darcs patch theory inverse 律）：
对池内每条补丁，正向应用后逆应用（find↔replace 互换、命中计数与上下文同步互换）
必须逐字节还原原始 en；再正向应用必须还原补丁后形态。unpatch∘patch=id 且
patch∘unpatch=id 于同一 fixture。池为合法空池时整测跳过（A2：空池合法）。

2026-11-25（specs/062 P-004）：补丁按头部 `file` 限定作用文件，本测亦按文件分组，
并校验“文件不匹配即不应用”（原实现把全部补丁套到 index.html）。
"""
import io
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

from tools import en_patch_lib, yuanwen  # noqa: E402
from tools.common import repo_path  # noqa: E402


def _apply(patch_list, html):
    """按给定补丁列表应用（find→replace，命中计数与上下文硬校验）——
    镜像 yuanwen.apply_en_patches 的语义但不走全局缓存。"""
    for p in patch_list:
        n = html.count(p["find"])
        if n != p["expect"]:
            raise AssertionError("命中 %d != expect %d（%s）"
                                 % (n, p["expect"], p.get("id", "?")))
        for ctx in p.get("context", []):
            if ctx and ctx not in html:
                raise AssertionError("上下文失配（%s）" % p.get("id", "?"))
        html = html.replace(p["find"], p["replace"])
    return html


def _basename(p):
    return (p.get("file") or "").replace("\\", "/").rsplit("/", 1)[-1] or "index.html"


def _group_by_file(patch_list):
    out = {}
    for p in patch_list:
        out.setdefault(_basename(p), []).append(p)
    return out


class PatchReverseTest(unittest.TestCase):

    def setUp(self):
        self.patches = en_patch_lib.load_patches(notice=False)

    def test_pool_present_or_empty(self):
        # 合法空池（INDEX count=0）→ 跳过；非空 → 逐条测
        if not self.patches:
            self.skipTest("合法空池（A2）")

    def test_unpatch_patch_is_id(self):
        for slug, plist in sorted(self.patches.items()):
            for fname, group in sorted(_group_by_file(plist).items()):
                with self.subTest(slug=slug, file=fname):
                    path = repo_path("html", slug, fname)
                    self.assertTrue(os.path.exists(path), "yuanwen 原件缺失：%s/%s"
                                    % (slug, fname))
                    html0 = io.open(path, encoding="utf-8").read()
                    html1 = _apply(group, html0)          # patch
                    inv = []
                    for p in group:
                        q = dict(p)
                        q["find"], q["replace"] = p["replace"], p["find"]
                        inv.append(q)
                    html2 = _apply(inv, html1)            # unpatch
                    self.assertEqual(html2, html0, "unpatch∘patch ≠ id（%s/%s）"
                                     % (slug, fname))
                    html3 = _apply(group, html2)          # 再 patch
                    self.assertEqual(html3, html1, "patch∘unpatch ≠ id（%s/%s）"
                                     % (slug, fname))

    def test_forward_matches_converter_view(self):
        # 判官与生产链同源（ADR-0073）：本测的正向应用必须与
        # yuanwen.apply_en_patches（生产链缓存版）结果逐字节一致
        for slug, plist in sorted(self.patches.items()):
            for fname, group in sorted(_group_by_file(plist).items()):
                with self.subTest(slug=slug, file=fname):
                    path = repo_path("html", slug, fname)
                    html0 = io.open(path, encoding="utf-8").read()
                    self.assertEqual(_apply(group, html0),
                                     yuanwen.apply_en_patches(slug, html0, fname))

    def test_file_scope_isolation(self):
        # 文件不匹配即不应用：notes.html 的补丁不得作用于 index.html，反之亦然
        for slug, plist in sorted(self.patches.items()):
            for fname, group in sorted(_group_by_file(plist).items()):
                others = [p for p in plist if _basename(p) != fname]
                if not others:
                    continue
                with self.subTest(slug=slug, file=fname):
                    path = repo_path("html", slug, fname)
                    if not os.path.exists(path):
                        continue
                    html0 = io.open(path, encoding="utf-8").read()
                    self.assertEqual(yuanwen.apply_en_patches(
                        slug, html0, fname), _apply(group, html0))
                    for other in {_basename(p) for p in others}:
                        self.assertEqual(yuanwen.apply_en_patches(
                            slug, html0, other), html0,
                            "跨文件补丁被误应用（%s/%s）" % (slug, other))


if __name__ == "__main__":
    unittest.main()
