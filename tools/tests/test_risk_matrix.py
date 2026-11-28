# -*- coding: utf-8 -*-
"""风险分级矩阵校验（T172／CP-S14-16）。"""
import json
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_risk_matrix  # noqa: E402


class TestRiskMatrix(unittest.TestCase):
    def _data(self):
        with open(os.path.join(REPO, "rules", "risk-matrix.json"), encoding="utf-8") as f:
            return json.load(f)

    def test_repo_matrix_valid(self):
        self.assertEqual(check_risk_matrix.validate(self._data()), [])

    def test_missing_level_rejected(self):
        data = self._data()
        del data["levels"]["C"]
        self.assertTrue(check_risk_matrix.validate(data))

    def test_c_must_not_publish(self):
        data = self._data()
        data["levels"]["C"]["publication"] = True
        self.assertTrue(check_risk_matrix.validate(data))

    def test_publication_full_only(self):
        data = self._data()
        data["publication"]["pe_level"] = "light"
        self.assertTrue(check_risk_matrix.validate(data))

    def test_forbid_raw_and_light(self):
        data = self._data()
        data["publication"]["forbid"] = ["raw"]
        self.assertTrue(check_risk_matrix.validate(data))


if __name__ == "__main__":
    unittest.main()
