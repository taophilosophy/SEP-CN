# -*- coding: utf-8 -*-
"""模型／提示登记校验（T172／CP-S14-17）。"""
import json
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_model_registry  # noqa: E402


class TestModelRegistry(unittest.TestCase):
    def _data(self):
        with open(os.path.join(REPO, "baseline", "model-registry.json"), encoding="utf-8") as f:
            return json.load(f)

    def test_repo_registry_valid(self):
        self.assertEqual(check_model_registry.validate(self._data()), [])

    def test_missing_field_rejected(self):
        data = self._data()
        del data["models"][0]["data_terms"]
        self.assertTrue(check_model_registry.validate(data))

    def test_duplicate_id_rejected(self):
        data = self._data()
        data["models"].append(dict(data["models"][0]))
        self.assertTrue(check_model_registry.validate(data))

    def test_bad_date_rejected(self):
        data = self._data()
        data["models"][0]["date"] = "2026/11/28"
        self.assertTrue(check_model_registry.validate(data))

    def test_params_must_be_object(self):
        data = self._data()
        data["models"][0]["params"] = "temperature=0"
        self.assertTrue(check_model_registry.validate(data))


if __name__ == "__main__":
    unittest.main()
