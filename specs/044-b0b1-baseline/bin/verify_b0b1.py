# -*- coding: utf-8 -*-
"""B0/B1 前置基线判定器（specs/044）：HTML 模板一致性与 markdown 保真的可执行判官。

判据（specs/044 §1）：
  B0 = 10 谓词合取（结构契约 4 + 可解析性 6）——判"该 HTML 符不符合模板、可不可解析"。
  B1 = I2 重放等值（check_pins）+ I3 词元流等值（multiset_diff）。

只读：不写 en/、不改 yuanwen、不动 baseline。可注入 HTML 字符串供负向测试。

用法:
  python -I specs/044-b0b1-baseline/bin/verify_b0b1.py --slug <s> [--json]
  python -I specs/044-b0b1-baseline/bin/verify_b0b1.py --slugs <s1> <s2> ... [--json]
  python -I specs/044-b0b1-baseline/bin/verify_b0b1.py --selftest        # 负向证伪
退出码: 0 全部通过；1 存在违反；2 输入/用法错误。
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools import parser  # noqa: E402
from tools import en_source_audit as esa  # noqa: E402
from tools.check_yuanwen_fidelity import (  # noqa: E402
    check_pins, html_text, iter_entries, load_baseline, md_text, multiset_diff)
from tools.common import read_text, repo_path  # noqa: E402

TABLE_RE = re.compile(r"<table\b.*?</table>", re.S | re.I)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'\bsrc="([^"]*)"', re.I)


def _math_brace_ok(raw):
    """公式内 TeX 花括号平衡（复用 en_source_audit._check_math 语义）。"""
    for m in re.finditer(r"\\\(.*?\\\)|\\\[.*?\\\]", raw, re.S):
        tex = m.group(0)
        depth, i, bad = 0, 0, False
        while i < len(tex):
            c = tex[i]
            if c == "\\":
                i += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth < 0:
                    bad = True
                    break
            i += 1
        if bad or depth != 0:
            return False
    return True


def b0_predicates(html):
    """B0 十谓词：对 HTML 字符串求值，返回 dict[谓词 -> bool]。"""
    p = {}
    m = parser.HEAD_RE.search(html)
    e = parser.TAIL_RE.search(html)
    p["marker"] = bool(m and e)
    p["pubinfo"] = bool(parser.PUBINFO_RE.search(html))
    p["title"] = bool(parser.META_RE.search(html))
    blocks = parser.parse_entry(html).get("blocks", [])
    p["section"] = any(b.get("type") == "h2" and b.get("section") for b in blocks)
    low = html.lower()
    p["no_truncation"] = "</html>" in low
    p["no_error_page"] = not any(mk in low[:4000] for mk in esa.MARKERS)
    p["math_delim"] = (len(re.findall(r"\\\(", html)) == len(re.findall(r"\\\)", html))
                       and len(re.findall(r"\\\[", html)) == len(re.findall(r"\\\]", html)))
    p["math_brace"] = _math_brace_ok(html)
    p["table_row"] = all(re.search(r"<tr[\s>]", t, re.I) for t in TABLE_RE.findall(html))
    p["img_src"] = all(SRC_RE.search(t) for t in IMG_RE.findall(html))
    return p


def b0_ok(slug):
    """读 en/<slug>/index.html 求 B0。"""
    idx = repo_path("en", slug, "index.html")
    if not os.path.exists(idx):
        return {"slug": slug, "b0": False, "error": "no en snapshot"}
    preds = b0_predicates(read_text(idx))
    return {"slug": slug, "b0": all(preds.values()), "predicates": preds,
            "failed": [k for k, v in preds.items() if not v]}


def b1_ok(slug):
    """I2 重放等值 + I3 词元流等值。"""
    entries = iter_entries(only=slug)
    if not entries:
        return {"slug": slug, "b1": False, "error": "no yuanwen md"}
    relpath = entries[0][1]
    baseline = load_baseline()
    pins = check_pins(slug, relpath, baseline)
    pin_bad = [i for i in pins if i.get("rule") in ("md-hand-edited", "source-drift")]
    a = html_text(slug)
    if a is None:
        return {"slug": slug, "b1": False, "error": "no en snapshot for token stream"}
    toks_a, st_a = a
    toks_b, st_b = md_text(repo_path(relpath))
    d = multiset_diff(toks_a, toks_b)
    asym = (st_a["spans"] != st_b["spans"] or st_a["oversize"] or st_b["oversize"]
            or st_a["unclosed"] or st_b["unclosed"])
    token_ok = (d is None) or asym  # asym 时判据不适用（软信号单列），不判失败
    return {"slug": slug, "b1": (not pin_bad) and token_ok,
            "pin_bad": pin_bad, "token_diff": d, "token_asym": asym}


def check_slug(slug):
    b0 = b0_ok(slug)
    b1 = b1_ok(slug)
    return {"slug": slug, "b0": b0.get("b0"), "b1": b1.get("b1"),
            "b0_failed": b0.get("failed", []), "b0_error": b0.get("error"),
            "b1_error": b1.get("error"), "b1_pin_bad": b1.get("pin_bad"),
            "b1_token_asym": b1.get("token_asym"),
            "b1_token_diff": b1.get("token_diff")}


def _selftest():
    """负向证伪：3 个坏样本必须分别触发 marker / no_truncation / math_delim 假。"""
    base = ('<!-- BEGIN ARTICLE HTML --><html><body>'
            '<div id="pubinfo"><em>First published Mar 10, 2002; substantive revision '
            'Jul 1, 2026</em></div>'
            '<meta name="citation_title" content="T">'
            '<h2><a id="x">1. Intro</a></h2>'
            '<p>body \\(x=y\\) text</p>'
            '<table><tr><td>a</td></tr></table>'
            '<img src="f.jpg" alt="a">'
            '</body></html><!-- END ARTICLE HTML -->')
    cases = {
        "N1-no-marker": base.replace("<!-- BEGIN ARTICLE HTML -->", "", 1),
        "N2-truncated": base.replace("</html>", "", 1),
        "N3-unbalanced-math": base.replace(r"\)", "("),
    }
    expect = {"N1-no-marker": "marker", "N2-truncated": "no_truncation",
              "N3-unbalanced-math": "math_delim"}
    ok = True
    for name, html in cases.items():
        preds = b0_predicates(html)
        bad = [k for k, v in preds.items() if not v]
        hit = expect[name] in bad
        ok &= hit
        print("[%s] 期望 %s 为假 -> %s%s" % (name, expect[name],
                                              "PASS" if hit else "FAIL", "" if hit else " 实际=%s" % bad))
    print("负向证伪：%s" % ("通过（判定器可证伪）" if ok else "失败"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    ap.add_argument("--slugs", nargs="*")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    slugs = [args.slug] if args.slug else (args.slugs or [])
    if not slugs:
        print("用法：--slug <s> 或 --slugs <s1> ... 或 --selftest", file=sys.stderr)
        return 2

    rows = [check_slug(s) for s in slugs]
    for r in rows:
        flag = "PASS" if (r["b0"] and r["b1"]) else "FAIL"
        print("[%s] %-28s b0=%s b1=%s" % (flag, r["slug"], r["b0"], r["b1"]))
        if not r["b0"]:
            print("       b0 失败谓词:", r.get("b0_failed") or r.get("b0_error"))
        if not r["b1"]:
            print("       b1 失败:", r.get("b1_error") or r.get("b1_pin_bad")
                  or ("token diff: %s" % json.dumps(r.get("b1_token_diff"), ensure_ascii=False)))
        elif r.get("b1_token_asym"):
            print("       b1 token 判据不适用（数学跨度不对称，软信号）")
    if args.json:
        print(json.dumps({"results": rows, "total": len(rows),
                          "passed": sum(1 for r in rows if r["b0"] and r["b1"])},
                         ensure_ascii=False, indent=1))
    return 0 if all(r["b0"] and r["b1"] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
