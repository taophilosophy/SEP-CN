# -*- coding: utf-8 -*-
"""补丁池可逆性单测（specs/053 §9 公理 A6；Darcs patch theory inverse 律）：
对池内每条补丁，正向应用后逆应用（find↔replace 互换、命中计数与上下文同步互换）
必须逐字节还原原始 en；再正向应用必须还原补丁后形态。unpatch∘patch=id 且
patch∘unpatch=id 于同一 fixture。池为合法空池时整测跳过（A2：空池合法）。"""
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


class PatchReverseTest(unittest.TestCase):

    def setUp(self):
        self.patches = en_patch_lib.load_patches(notice=False)

    def test_pool_present_or_empty(self):
        # 合法空池（INDEX count=0）→ 跳过；非空 → 逐条测
        if not self.patches:
            self.skipTest("合法空池（A2）")

    def test_unpatch_patch_is_id(self):
        for slug, plist in sorted(self.patches.items()):
            with self.subTest(slug=slug):
                path = repo_path("en", slug, "index.html")
                self.assertTrue(os.path.exists(path), "en 原件缺失：%s" % slug)
                html0 = io.open(path, encoding="utf-8").read()
                html1 = _apply(plist, html0)          # patch
                inv = []
                for p in plist:
                    q = dict(p)
                    q["find"], q["replace"] = p["replace"], p["find"]
                    inv.append(q)
                html2 = _apply(inv, html1)            # unpatch
                self.assertEqual(html2, html0, "unpatch∘patch ≠ id（%s）" % slug)
                html3 = _apply(plist, html2)          # 再 patch
                self.assertEqual(html3, html1, "patch∘unpatch ≠ id（%s）" % slug)

    def test_forward_matches_converter_view(self):
        # 判官与生产链同源（ADR-0073）：本测的正向应用必须与
        # yuanwen.apply_en_patches（生产链缓存版）结果逐字节一致
        for slug, plist in sorted(self.patches.items()):
            with self.subTest(slug=slug):
                path = repo_path("en", slug, "index.html")
                html0 = io.open(path, encoding="utf-8").read()
                self.assertEqual(_apply(plist, html0),
                                 yuanwen.apply_en_patches(slug, html0))


if __name__ == "__main__":
    unittest.main()
