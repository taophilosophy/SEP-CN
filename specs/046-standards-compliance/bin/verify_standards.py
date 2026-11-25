# -*- coding: utf-8 -*-
"""规范对齐公理化判定器（specs/046）：对 rules/standards.json 求值三性质。

判据（specs/046 §2）：
  充分性 = 每条采纳项 owner（承接规则）与 tool（承接工具/凭证）均非空。
  一致性 = id 唯一（登记单射），无重复登记、无冲突承接。
  完备性 = 五类规范（翻译质量/校对/参考文献/工具链安全/合规）均非空且覆盖流程环节。

只读。核心为纯函数（接受输入），负向测试注入坏输入证伪。

用法:
  python -I specs/046-standards-compliance/bin/verify_standards.py          # 对真实登记册断言
  python -I specs/046-standards-compliance/bin/verify_standards.py --selftest  # 负向证伪
退出码: 0 全部通过；1 存在违反；2 输入错误。
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools.common import repo_path  # noqa: E402

FLOW_STAGES = {"翻译质量": "s1/s2/s2.4/r 链", "校对": "s3", "参考文献": "文献节",
               "工具链安全": "工具层", "合规": "治理层"}


def check_sufficiency(adopted):
    """充分性：每条采纳项 owner 与 tool 均非空。"""
    bad = [a.get("id") for a in adopted if not (a.get("owner") and a.get("tool"))]
    return not bad, bad


def check_consistency(adopted):
    """一致性：id 唯一（登记单射）。"""
    ids = [a.get("id") for a in adopted]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    return not dup, dup


def check_completeness(categories):
    """完备性：五类规范均非空且覆盖流程环节。"""
    empty = [k for k, v in (categories or {}).items() if not v]
    missing = [k for k in FLOW_STAGES if k not in (categories or {})]
    return not empty and not missing, {"empty": empty, "missing_stage": missing}


STD_RE = re.compile(
    r"(?<![A-Za-z0-9])"
    r"((?:GB/T|GB|CY/T|DA/T|ISO/IEC/IEEE|ISO/IEC|ISO|ASTM|SAE)\s*\d+(?:\.\d+)?(?:[.\-]\d+)?)")


def _variants(tok):
    """标准号的可能登记写法：全文、去年份、去分册、去分册与序号。"""
    t = tok.strip()
    out = {t}
    m = re.match(r"^(.*?)[-:](\d{4})$", t)
    if m:
        out.add(m.group(1))
        t = m.group(1)
    m = re.match(r"^(.*?)\.\d+(-\d+)?$", t)
    if m:
        out.add(m.group(1))
    m = re.match(r"^(.*?)-\d+$", t)
    if m:
        out.add(m.group(1))
    return {x.replace(" ", "") for x in out}


def check_citation_resolution(cited, not_adopted, texts):
    """V5 引用可解析：正文出现的标准号必须能落到 cited／not_adopted 的 std_key。"""
    keys = set()
    for c in cited:
        keys.update(k.replace(" ", "") for k in c.get("std_key", []))
    for n in not_adopted:
        keys.update(_variants(str(n.get("std", "")).split("（")[0]))
    unresolved = []
    for name, text in texts.items():
        for m in STD_RE.finditer(text or ""):
            if not (_variants(m.group(1)) & keys):
                unresolved.append("%s:%s" % (name, m.group(1)))
    return not unresolved, sorted(set(unresolved))


def _rules_texts():
    """rules 下非 ADR／非 reference 的 md 正文（ADR 保留年代名，不纳入扫描）。"""
    base = repo_path("rules")
    out = {}
    for dirpath, dirnames, files in os.walk(base):
        rel = os.path.relpath(dirpath, base).replace(os.sep, "/")
        if rel.startswith("adr") or rel.startswith("reference"):
            dirnames[:] = []
            continue
        for fn in files:
            if fn.endswith(".md"):
                p = os.path.join(dirpath, fn)
                with open(p, encoding="utf-8") as f:
                    out[os.path.relpath(p, base).replace(os.sep, "/")] = f.read()
    return out


def run():
    d = json.load(open(repo_path("rules", "standards.json"), encoding="utf-8"))
    adopted = d.get("adopted", [])
    cats = d.get("categories", {})
    rows = []
    ok, det = check_sufficiency(adopted)
    rows.append({"prop": "充分性", "name": "每条采纳项有 owner+tool 承接", "ok": ok,
                 "detail": "缺承接=%s" % (det or "无")})
    ok, det = check_consistency(adopted)
    rows.append({"prop": "一致性", "name": "登记 id 唯一（单射）", "ok": ok,
                 "detail": "重复=%s" % (det or "无")})
    ok, det = check_completeness(cats)
    rows.append({"prop": "完备性", "name": "五类规范覆盖流程环节", "ok": ok,
                 "detail": json.dumps(det, ensure_ascii=False)})
    ok, det = check_citation_resolution(d.get("cited", []), d.get("not_adopted", []),
                                        _rules_texts())
    rows.append({"prop": "V5", "name": "规则正文标准号可解析到登记册", "ok": ok,
                 "detail": "未解析=%s" % (det[:8] or "无")})
    return rows, len(adopted)


def selftest():
    good = [{"id": "S1", "std": "X", "clause": "c", "owner": "o", "tool": "t"}]
    cases = [
        ("N1-充分性", check_sufficiency([{"id": "S1", "owner": "", "tool": ""}]), "缺承接"),
        ("N2-一致性", check_consistency(good + [{"id": "S1", "owner": "o2", "tool": "t2"}]),
         "重复 id"),
        ("N3-完备性", check_completeness({}), "空类别"),
        ("N4-V5", check_citation_resolution(
            [{"std_key": ["ISO 17100"]}], [],
            {"a.md": "依 ISO 17100 与 GB/T 9999-2025"}), "未解析标准号"),
    ]
    ok = True
    for name, (passed, det), expect in cases:
        hit = (passed is False)
        ok &= hit
        print("[%s] 期望检出 %s -> %s%s" % (name, expect, "PASS" if hit else "FAIL",
                                            "" if hit else " 实际=%s" % det))
    print("负向证伪：%s" % ("通过" if ok else "失败"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    rows, n = run()
    for r in rows:
        print("[%s] %-40s %s%s" % (r["prop"], r["name"], "PASS" if r["ok"] else "FAIL",
                                    "" if r["ok"] else "  -> " + str(r["detail"])))
    n_pass = sum(1 for r in rows if r["ok"])
    print("汇总：%d 项，通过 %d，失败 %d；采纳项 %d" % (len(rows), n_pass, len(rows) - n_pass, n))
    if args.json:
        print(json.dumps({"total": len(rows), "passed": n_pass, "adopted": n,
                          "results": rows}, ensure_ascii=False, indent=1))
    return 0 if n_pass == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
