# -*- coding: utf-8 -*-
"""右逆装配器（specs/053 bin/reassemble.py）单测：书目区再生标题与固定注。

判例取自 2026-11-26 第四十八批（B3.1 不动点）。
"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "specs", "053-en-template-audit", "bin"))

import reassemble as R  # noqa: E402

NOTE = "> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。"


class TestBibRegionShape(unittest.TestCase):
    def test_nested_references_heading_and_def_ul(self):
        # aesthetic-judgment 判例：`<h2>Bibliography</h2>` 内又有 `<h3>References</h3>`；
        # 嵌套标题按原文标题发出（C 才能再生标题＋固定注），定义 ul 紧随该标题
        # （其后同级 Further Reading 会终止书目区，留在区末条目即蒸发）
        md = "\n".join([
            "# Aesthetic Judgment",
            "",
            "*First published Fri Feb 28, 2003*",
            "",
            "## References（引用注释）",
            "",
            NOTE,
            "",
            "### References（引用注释）",
            "",
            NOTE,
            "",
            "### Further Reading",
            "",
            "- Bender, John W., 1995, “General but Defeasible Reasons”, *JAAC*.",
            "",
            "[^bender-1995]: Bender, John W., 1995, “General but Defeasible Reasons”, *JAAC*.",
            "",
        ])
        _t, art = R.reassemble_article(md, [])
        self.assertIn("<h3>References</h3>", art)
        boss = "Bender, John W., 1995, “General but Defeasible Reasons”, <em>JAAC</em>.</li>"
        self.assertLess(art.index("<h3>References</h3>"), art.index(boss))
        self.assertLess(art.index(boss), art.index("<h3>Further Reading</h3>"))

    def test_fixed_note_not_carried(self):
        # C 注入的固定注含 `[^key]` 字面，经行内渲染会被当脚注标记吃掉——
        # R 一律不搬运，由 C 按标题再生
        md = "\n".join([
            "# Price",
            "",
            "*First published Mon Jan 1, 2001*",
            "",
            "## References（引用注释）",
            "",
            NOTE,
            "",
            "### Works",
            "",
            NOTE,
            "",
            "[^price-1940]: Price, H. H., 1940, *Hume’s Theory*, Oxford: OUP.",
            "",
        ])
        _t, art = R.reassemble_article(md, [])
        self.assertNotIn("原文参考文献已转为脚注引用", art)
        self.assertIn("<h2>Bibliography</h2>", art)


if __name__ == "__main__":
    unittest.main()
