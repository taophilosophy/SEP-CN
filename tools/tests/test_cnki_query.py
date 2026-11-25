# -*- coding: utf-8 -*-
"""cnki_query 单元测试（specs/008 US-2）：provider 解析、节流、重试、注入。"""
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import cnki_query as cq

FIXTURE_PAYLOAD = {
    "success": True, "code": 200,
    "result": {"standardVO": {
        "totalRecords": 2,
        "tmWordList": [
            {"cnName": "溯因推理", "enName": "abductive reasoning",
             "standardCode": "GB/T XXXX", "standardName": "测试标准",
             "subjectName": "计算机科学技术"},
            {"cnName": "溯因", "enName": "abduction", "standardCode": None,
             "standardName": None, "subjectName": None},
        ]}}}


class CnkiQueryTests(unittest.TestCase):

    def test_safe_key(self):
        self.assertEqual(cq.safe_key('Inference to the Best Explanation'),
                         'inference_to_the_best_explanation')
        self.assertEqual(cq.safe_key('贝叶斯 rule'), '贝叶斯_rule')

    def test_standard_parse(self):
        hits, note = cq._tl_standard_parse(FIXTURE_PAYLOAD)
        self.assertEqual(len(hits), 2)
        self.assertEqual(hits[0]['cn'], '溯因推理')
        self.assertEqual(hits[0]['code'], 'GB/T XXXX')
        self.assertIn('totalRecords=2', note)

    def test_empty_parse(self):
        hits, note = cq._tl_standard_parse({"result": {"standardVO": {
            "totalRecords": 0, "tmWordList": []}}})
        self.assertEqual(hits, [])

    def test_retry_records_error(self):
        def boom(term, timeout):
            raise IOError('disconnected')
        prov = {'fetch': boom, 'parse': cq._tl_standard_parse, 'enabled': True}
        status, hits, note, raw, err = cq.query_with_retry(
            prov, 'test', retries=(), timeout=1)
        self.assertEqual(status, 'error')
        self.assertIn('disconnected', err)

    def test_all_parse_normal_db_ids(self):
        hits, note = cq._tl_all_parse({"result": {"searchResult": [
            {"id": "0", "result": {"totalRecords": 1, "tmWordList": [
                {"cn": "信念", "en": "belief", "wordNumber": "03.001",
                 "source": "心理学名词", "subjectFullName": "心理学"}]}}]}})
        self.assertEqual(len(hits), 1)
        self.assertIn('审定公布名词库=1', note)

    def test_all_parse_uuid_buckets_is_denied(self):
        """2026-11-25 实测：token 权限失效时回包 success=true，但分库 id 变 UUID、
        全库零记录。旧解析会记成“审定库确无收录”，产出假凭证。"""
        body = {"success": True, "result": {"searchResult": [
            {"id": "0" * 32, "result": {"totalRecords": 0, "tmWordList": []}},
            {"id": "0" * 31 + "1", "result": {"totalRecords": 0, "tmWordList": []}},
        ]}}
        self.assertRaises(cq.ChannelSuspect, cq._tl_all_parse, body)
        prov = {'fetch': lambda t, to: body, 'parse': cq._tl_all_parse}
        status, hits, note, raw, err = cq.query_with_retry(prov, 'belief', retries=())
        self.assertEqual(status, 'denied')
        self.assertEqual(hits, [])
        self.assertIn('ChannelSuspect', err)

    def test_disabled_provider_rejected(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = cq.main(['--terms', 'x', '--provider', 'cnki-dict'])
        self.assertEqual(code, 2)
        self.assertIn('禁用', buf.getvalue())

    def test_no_source_rejected(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = cq.main([])
        self.assertEqual(code, 2)


if __name__ == '__main__':
    unittest.main()
