# -*- coding: utf-8 -*-
"""抓取完整性主动闭环（specs/001 fetch-completeness-analysis 建议 1，2026-10-27）。

对每个 en/<slug>/ 词条包校验：index.html + notes.html + 补充材料内引用的全部
词条资产（图片、notes、补充材料）在包内；缺件区分——
  404       = 缺省件（显式登记，不算错误）
  网络缺失  = 可补抓（--fix 模式自动补抓并更新 baseline）

用法:
  python tools/fetch_audit.py [slug...]            # 审计（缺网络补抓）
  python tools/fetch_audit.py [slug...] --fix      # 缺件自动补抓（礼貌 5 秒）
  python tools/fetch_audit.py --all [--fix]        # 全库（默认 audit-only）
输出: stdout JSON {audited, complete, missing_default:[], missing_fetchable:[],
                   fixed:[], errors:[]}
退出码: 0 完整/成功；1 有可补抓缺件；2 错误。
"""
import argparse
import html
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import fetch
from tools.common import load_json, repo_path, utcnow_iso

if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ASSET_RE = re.compile(r'(?:src|href)="([^"]+)"')
HTML_RE = re.compile(r"<h2|<html|<body|<!DOCTYPE", re.I)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
# 形如文件名的裸引用（含 .au/.qt/.wav 等任意扩展；russell 词条实证媒体引用
# 曾被扩展名枚举漏掉）。index.html 为包自身不入闭包。
FILENAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\.[A-Za-z0-9._-]+\Z")


def referenced_assets(slug):
    """词条包内引用的全部词条资产（相对路径，排除站点框架与外链）。

    浏览器语义：先剥离 HTML 注释（注释掉的引用不构成抓取义务）、再对属性值
    做实体反解（SEP 混淆邮箱形如 m&#97;ilto:…）。一切形如文件名的裸引用都是
    词条包资产（页面/图片/词条自有 js/css/媒体如 russell 的 .au/.qt/.wav）；
    ../../js/ 等站点框架为路径引用，由 "/" 过滤排除。
    """
    d = repo_path("en", slug)
    refs = set()
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".html"):
            continue
        with open(os.path.join(d, fn), encoding="utf-8", errors="replace") as fh:
            txt = fh.read()
        if not HTML_RE.search(txt):
            continue  # 非页面（如残片）跳过
        for m in ASSET_RE.finditer(COMMENT_RE.sub("", txt)):
            src = html.unescape(m.group(1)).split("#")[0].split("?")[0]
            if not src or "/" in src:
                continue  # 词条包资产永远是目录内裸文件名；../../ 等为站点链接
            if src.startswith(("http", ".", "mailto:", "javascript:")):
                continue
            if not FILENAME_RE.fullmatch(src):
                continue  # 非文件名形态（锚点残留、实体残片等）
            if src == "index.html":
                continue
            refs.add(src)  # notes.html / 补充材料 / 图片 / 词条自有 js/css/媒体
    return refs


def audit_slug(slug, fix=False):
    d = repo_path("en", slug)
    if not os.path.isdir(d):
        return {"slug": slug, "error": "en/%s 不存在" % slug}, 2
    refs = referenced_assets(slug)
    missing = sorted(r for r in refs if not os.path.isfile(os.path.join(d, r)))
    default, fetchable, fixed = [], [], []
    url_base = fetch.BASE + "/entries/%s/" % slug
    for rel in missing:
        # 缺省件判定：抓一次，404 = 上游本就没有（显式缺省）
        os.makedirs(d, exist_ok=True)
        status, _data = fetch.get(url_base + rel, dest=os.path.join(d, rel),
                                  delay=fetch.MIN_DELAY)
        if status == 200:
            fixed.append(rel)
        elif status == 404:
            default.append(rel)
            if os.path.isfile(os.path.join(d, rel)):
                os.remove(os.path.join(d, rel))  # 404 不落空文件
        else:
            fetchable.append({"asset": rel, "http": status})
    return {"slug": slug, "assets": len(refs), "fixed": fixed,
            "missing_default": default, "missing_fetchable": fetchable}, (
        1 if fetchable else 0)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true", help="全库（baseline 登记的词条）")
    ap.add_argument("--fix", action="store_true", help="缺件自动补抓（当前实现：审计即补抓）")
    args = ap.parse_args(argv)
    if args.slugs:
        slugs = args.slugs
    elif args.all:
        base = load_json(repo_path("baseline", "entries.json"))
        slugs = [r["slug"] for r in base["entries"]]
    else:
        print(json.dumps({"error": "用法: fetch_audit.py <slug>... | --all [--fix]"}))
        return 2
    results, code = [], 0
    for i, slug in enumerate(slugs):
        sys.stderr.write("[fetch_audit] %d/%d %s ...\n" % (i + 1, len(slugs), slug))
        res, rc = audit_slug(slug)
        results.append(res)
        code = max(code, rc)
    summary = {
        "audited": len(results), "ran_at": utcnow_iso(),
        "complete": sum(1 for r in results if "error" not in r
                        and not r.get("fixed") and not r.get("missing_fetchable")),
        "missing_default_total": sum(len(r.get("missing_default", [])) for r in results),
        "missing_fetchable_total": sum(len(r.get("missing_fetchable", [])) for r in results),
        "fixed_total": sum(len(r.get("fixed", [])) for r in results),
        "errors": [r for r in results if "error" in r],
        "results": results,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
