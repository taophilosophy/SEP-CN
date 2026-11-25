# -*- coding: utf-8 -*-
"""补丁池有界解析单测（ADR-0063：目录布局＋告知留痕；缺失即硬失败，绝不静默降级）。

跑法: python -m unittest tools.tests.test_en_patch_pool -v
"""
import json
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

from tools import en_patch_lib  # noqa: E402
from check_en_patches import admission  # noqa: E402

PATCH_BODY = """# id: {pid}
# slug: demo
# file: en/demo/index.html
# expect: 1
# category: 格式层（空格）
# origin: upstream-typo
# source: en-errata.md §九 格式层
--- a/en/demo/index.html
+++ b/en/demo/index.html
@@ -1,3 +1,3 @@
 a line
-b Einstein1949b c
+b Einstein 1949b c
 d line
"""


class PoolCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self._record = en_patch_lib.RECORD
        en_patch_lib.RECORD = (self.tmp, "rec.jsonl")
        en_patch_lib._announced = False

    def tearDown(self):
        en_patch_lib.RECORD = self._record
        en_patch_lib._announced = False
        shutil.rmtree(self.tmp, ignore_errors=True)

    def make_pool(self, *pids):
        base = os.path.join(self.tmp, "en-patches")
        os.makedirs(base, exist_ok=True)
        for pid in pids:
            with open(os.path.join(base, pid + ".patch"), "w", encoding="utf-8",
                      newline="\n") as f:
                f.write(PATCH_BODY.format(pid=pid))
        return base

    def read_record(self):
        path = os.path.join(self.tmp, "rec.jsonl")
        if not os.path.exists(path):
            return []
        with open(path, encoding="utf-8") as f:
            return [json.loads(line) for line in f.read().splitlines() if line]


class TestPoolMissingHardFail(PoolCase):
    """B 档：找不到池就抛错（有界解析，不外搜、不静默返回空池）。"""

    def test_missing_dir_raises(self):
        with self.assertRaises(en_patch_lib.PatchPoolMissing):
            en_patch_lib.load_patches(os.path.join(self.tmp, "nope"))

    def test_empty_dir_raises(self):
        base = self.make_pool()  # 无 .patch、无 INDEX
        with self.assertRaises(en_patch_lib.PatchPoolMissing):
            en_patch_lib.load_patches(base)

    def test_index_zero_count_is_legal_empty_pool(self):
        base = self.make_pool()
        with open(os.path.join(base, "INDEX.json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump({"schema": "sep-cn-en-patches-dir/1", "count": 0, "patches": []}, f)
        self.assertEqual(en_patch_lib.load_patches(base), {})

    def test_legacy_single_file_not_searched(self):
        with open(os.path.join(self.tmp, "en-patches.json"), "w", encoding="utf-8") as f:
            json.dump({"patches": []}, f)
        with self.assertRaises(en_patch_lib.PatchPoolMissing):
            en_patch_lib.load_patches(os.path.join(self.tmp, "en-patches"))


class TestPoolDirLayout(PoolCase):
    """A 档：目录正本可读，且必须输出告知信息并落独立记录文件。"""

    def test_loads_find_replace(self):
        base = self.make_pool("P-900")
        out = en_patch_lib.load_patches(base)
        self.assertEqual(out["demo"][0]["find"], "b Einstein1949b c")
        self.assertEqual(out["demo"][0]["replace"], "b Einstein 1949b c")
        self.assertEqual(out["demo"][0]["expect"], 1)

    def test_record_written_once_per_process(self):
        base = self.make_pool("P-900", "P-901")
        en_patch_lib.load_patches(base)
        en_patch_lib.load_patches(base)          # 二次调用不再追加
        recs = self.read_record()
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0]["layout"], "dir")
        self.assertEqual(recs[0]["count"], 2)
        self.assertEqual(recs[0]["ids"], ["P-900", "P-901"])
        self.assertIn("index", recs[0])

    def test_malformed_patch_raises_not_silent(self):
        base = self.make_pool()
        with open(os.path.join(base, "P-902.patch"), "w", encoding="utf-8", newline="\n") as f:
            f.write(PATCH_BODY.format(pid="P-902").replace("-b Einstein1949b c\n", ""))
        with self.assertRaises(ValueError):
            en_patch_lib.load_patches(base)


class TestRepoPoolHealth(unittest.TestCase):
    """现役池：全部条目须过 C2 准入谓词，且转换层可无异常加载。"""

    def test_real_pool_passes_admission(self):
        pool = en_patch_lib.load_patches(notice=False)
        self.assertTrue(pool, "现役补丁池不应为空")
        n = 0
        for items in pool.values():
            for p in items:
                self.assertIsNotNone(admission(p["find"], p["replace"]),
                                     "池内补丁 %s 应过准入谓词（文字层禁入池）" % p["id"])
                n += 1
        self.assertGreaterEqual(n, 3)


if __name__ == "__main__":
    unittest.main()
