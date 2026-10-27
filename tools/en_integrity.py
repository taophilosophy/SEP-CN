# -*- coding: utf-8 -*-
"""en/ 镜像逐词条完整性深度复核（specs/001 fetch-completeness-analysis 建议 2，2026-10-27）。

fetch_audit.py 只校验「目录内裸文件名」引用；本工具做全量离线深检（零网络）：
  1. 页面真实性：index.html 存在、SEP 页特征、错误页/风控页标记、</html> 截断、
     零字节文件、嵌套目录（上游 /entries/<slug>/ 为平铺命名空间）；
  2. 引用闭包（升级版）：裸文件名与相对路径引用统一按上游 URL 语义解析
     （urljoin 到 /entries/<slug>/）；落在 /entries/ 命名空间内的目标逐一核对
     本地存在（大小写精确比对——Windows 文件系统不区分大小写，会掩盖错名）；
     站点框架（/css /js /symbols /MathJax 等）与外链只计数，不在词条包职责内；
  3. 数学公式形态盘点：MathJax 脚本来源（站点级/CDN/词条内）、内联 MathML/TeX、
     公式图片类引用是否在包内；
  4. 目录结构一致性：在盘文件必须「被引用」（引用即上游路径证据）或
     「已登记 baseline」（抓取时哈希登记为 en/<slug>/<名>），两者都不是 = 游离件；
  5. 未登记文件盘点（fetch_audit 补抓不写 baseline，见 contracts/cli.md）。

用法:
  python tools/en_integrity.py [slug...]        # 审计（纯离线）
  python tools/en_integrity.py --all [--out <path>]
输出: stdout JSON 摘要（含全部问题明细）；--out 落盘完整凭证。
退出码: 0 干净（仅信息级）；1 有硬问题；2 错误。
"""
import argparse
import html
import io
import json
import os
import re
import sys
from collections import Counter
from urllib.parse import urljoin, urlparse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import load_json, repo_path, utcnow_iso, write_json_verified

SITE = "https://plato.stanford.edu"
REF_RE = re.compile(r'(?:src|href)="([^"]+)"')
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
IMG_EXT_RE = re.compile(r"\.(png|jpe?g|gif|svg|webp)$", re.I)
MATH_ASSET_RE = re.compile(r"(eqn|equat|formula|math)", re.I)
INLINE_MATH_RE = re.compile(r"<math[\s>]|\\\(|\\\[")
MARKERS = [
    "attention required", "just a moment", "access denied",
    "request unsuccessful", "incapsula", "error 403", "error 404",
    "page not found", "too many requests", "cf-browser-verification",
    "challenge-platform", "checking your browser", "rate limit",
    "429 too many",
]


def resolve_ref(src, slug):
    """引用 → 上游 URL 语义分类。

    先按浏览器语义做 HTML 实体反解（SEP 混淆邮箱形如 m&#97;ilto:…，
    其含 & 与 #，若先拆 fragment 会误判为资产引用），再拆 fragment/query。
    返回 (kind, slug2/域名/一级路径, 目标)；kind ∈ entry/site/external。
    """
    src = html.unescape(src).split("#")[0].split("?")[0].strip()
    if not src or src.lower().startswith(("mailto:", "javascript:", "tel:", "data:")):
        return None
    url = urljoin(SITE + "/entries/%s/" % slug, src)
    p = urlparse(url)
    if p.scheme and p.netloc and p.netloc != "plato.stanford.edu":
        return ("external", p.netloc, p.path)
    path = re.sub(r"/{2,}", "/", p.path)  # 上游 HTML 存在双斜杠（如 /entries//x/）
    if path.startswith("/entries/"):
        rest = path[len("/entries/"):]
        slug2, _, fname = rest.partition("/")
        return ("entry", slug2, fname)
    seg = path.lstrip("/").split("/")[0]
    return ("site", seg, path)


def audit_dir(root, slug, registered):
    """对单个词条包做全部检查。root 为 en/ 目录绝对路径。

    registered: baseline 登记的包内文件名集合（en/<slug>/<名> 的 <名>）。
    返回 (result, hard_count)。
    """
    d = os.path.join(root, slug)
    res = {"slug": slug}
    hard = 0
    if not os.path.isdir(d):
        return {"slug": slug, "error": "en/%s 不存在" % slug}, 1
    listing = os.listdir(d)
    subdirs = sorted(x for x in listing if os.path.isdir(os.path.join(d, x)))
    files = sorted(x for x in listing if os.path.isfile(os.path.join(d, x)))
    if subdirs:
        res["nested_dirs"] = subdirs
    empty = sorted(f for f in files if os.path.getsize(os.path.join(d, f)) == 0)
    if empty:
        res["empty_files"] = empty
        hard += 1
    if "index.html" not in files:
        res["missing_index"] = True
        hard += 1

    pages = [f for f in files if f.lower().endswith(".html")]
    entry_targets = set()          # (slug2, fname) 需本地存在的 /entries/ 资产
    dir_targets = set()            # 相关词条导航（链接到词条目录根）
    referenced_self = {"index.html"}
    site_seg = Counter()
    external = Counter()
    mathjax, math_inline_pages, math_assets = set(), [], []
    suspects, truncated, no_charset, not_sep = [], [], [], []

    for pf in pages:
        with open(os.path.join(d, pf), encoding="utf-8", errors="replace") as fh:
            txt = fh.read()
        body = COMMENT_RE.sub("", txt)  # 注释掉的引用不构成浏览器加载义务
        low = body.lower()
        if pf == "index.html" and \
                "stanford encyclopedia of philosophy" not in low:
            not_sep.append(pf)  # 非 SEP 签名页：错误页/风控页替换的强信号
        elif pf == "index.html":
            # 错误/风控标记只出现在 title 与 h1（错误页版式）；
            # 全文匹配会把哲学正文误当标记（如 "just a moment ago"）
            head = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
            h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S | re.I)
            head_txt = ((head.group(1) if head else "") + " " +
                        (h1.group(1) if h1 else "")).lower()
            for mk in MARKERS:
                if mk in head_txt:
                    suspects.append({"file": pf, "marker": mk})
        if "</html>" not in low[-300:]:
            truncated.append(pf)
        if "charset" not in low[:3000]:
            no_charset.append(pf)
        if INLINE_MATH_RE.search(body):
            math_inline_pages.append(pf)
        for m in REF_RE.finditer(body):
            r = resolve_ref(m.group(1), slug)
            if r is None:
                continue
            kind, a, b = r
            if kind == "external":
                external[a] += 1
            elif kind == "site":
                site_seg[a] += 1
                if "mathjax" in a.lower():
                    mathjax.add(m.group(1))
            else:  # entry
                if not b:
                    if a != slug:
                        dir_targets.add(a)   # 相关词条导航（链接到词条目录根）
                elif a == slug:
                    entry_targets.add((slug, b))
                    referenced_self.add(b)
                    if IMG_EXT_RE.search(b) and MATH_ASSET_RE.search(b):
                        math_assets.append(b)
                else:
                    entry_targets.add((a, b))

    if not_sep:
        res["not_sep_page"] = not_sep
        hard += 1
    if suspects:
        res["suspect_page"] = suspects
        hard += 1
    if truncated:
        res["truncated"] = truncated
        hard += 1
    if no_charset:
        res["no_charset"] = no_charset

    # /entries/ 命名空间目标逐一核对（大小写精确）
    missing, case_mismatch, cross_missing = [], [], []
    unmirrored = set()
    for slug2, fname in sorted(entry_targets):
        if slug2 == slug:
            if "/" in fname:  # 词条内子目录路径（如 BNfiles/x）
                if os.path.isfile(os.path.join(d, fname)):
                    continue
                missing.append(fname)
                continue
            if fname in files:
                continue
            low_hits = [f for f in files if f.lower() == fname.lower()]
            if low_hits:
                case_mismatch.append({"ref": fname, "on_disk": low_hits[0]})
            else:
                missing.append(fname)
        else:
            d2 = os.path.join(root, slug2)
            if not os.path.isdir(d2):
                unmirrored.add(slug2)   # 上游有而镜像未含（intake 队列），非缺件
                continue
            names2 = os.listdir(d2)
            if "/" in fname:
                if os.path.isfile(os.path.join(d2, fname)):
                    continue
                cross_missing.append({"entry": slug2, "asset": fname})
                continue
            if fname in names2:
                continue
            low_hits = [f for f in names2 if f.lower() == fname.lower()]
            if low_hits:
                case_mismatch.append({"ref": "%s/%s" % (slug2, fname),
                                      "on_disk": "%s/%s" % (slug2, low_hits[0])})
            else:
                cross_missing.append({"entry": slug2, "asset": fname})
    for slug2 in sorted(dir_targets):
        if not os.path.isdir(os.path.join(root, slug2)):
            unmirrored.add(slug2)
    if missing:
        res["missing_assets"] = missing
        hard += 1
    if case_mismatch:
        res["case_mismatch"] = case_mismatch
        hard += 1
    if cross_missing:
        res["cross_entry_missing"] = cross_missing
        hard += 1

    # 目录结构一致性：在盘文件 = 被引用 ∪ 已登记，否则游离
    unreg_orphan, unreg_ref, orphan_reg = [], [], []
    ref_lower = {x.lower() for x in referenced_self}
    for f in files:
        refd = f in referenced_self or f.lower() in ref_lower
        regd = f in registered
        if refd and regd:
            continue
        if refd and not regd:
            unreg_ref.append(f)      # fetch_audit 补抓件（契约：不写 baseline）
        elif not refd and regd:
            orphan_reg.append(f)     # 上游已不再引用（版本更替残件）
        else:
            unreg_orphan.append(f)   # 游离件：既无引用证据也无抓取登记
    if unreg_orphan:
        res["unregistered_orphans"] = unreg_orphan
        hard += 1
    if orphan_reg:
        res["registered_orphans"] = orphan_reg
    if unreg_ref:
        res["fetched_not_registered"] = unreg_ref
    reg_missing = sorted(registered - set(files))
    if reg_missing:
        res["registered_missing"] = reg_missing
        hard += 1

    if mathjax:
        res["mathjax"] = sorted(mathjax)
    if math_inline_pages:
        res["math_inline_pages"] = math_inline_pages
    if math_assets:
        res["math_asset_refs"] = sorted(set(math_assets))

    info = {
        "files": len(files), "pages": len(pages),
        "site_refs": dict(site_seg), "external_refs": dict(external),
        "cross_links_unmirrored": len(unmirrored),
    }
    res["info"] = info
    return res, hard


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true", help="全库（baseline 登记词条）")
    ap.add_argument("--out", default=None, help="凭证 JSON 落盘路径")
    args = ap.parse_args(argv)

    base = load_json(repo_path("baseline", "entries.json"))
    reg = {}
    for r in base["entries"]:
        names = {f["path"].split("/", 2)[2] for f in r.get("files", [])
                 if f["path"].startswith("en/%s/" % r["slug"])}
        reg[r["slug"]] = names
    if args.slugs:
        slugs = args.slugs
    elif args.all:
        slugs = sorted(reg)
    else:
        print(json.dumps({"error": "用法: en_integrity.py <slug>... | --all"}))
        return 2

    root = repo_path("en")
    results, hard_total, errors = [], 0, []
    site_all, ext_all = Counter(), Counter()
    for i, slug in enumerate(slugs):
        if i % 250 == 0:
            sys.stderr.write("[en_integrity] %d/%d ...\n" % (i, len(slugs)))
        try:
            res, hard = audit_dir(root, slug, reg.get(slug, set()))
        except Exception as e:  # noqa: BLE001 — 单词条异常不中断全量
            errors.append({"slug": slug, "error": str(e)})
            continue
        if "error" in res:
            errors.append(res)
            continue
        hard_total += hard
        for k in ("site_refs", "external_refs"):
            counter = site_all if k == "site_refs" else ext_all
            for kk, vv in res["info"][k].items():
                counter[kk] += vv
        if hard:
            results.append(res)
    for r in results:
        r.pop("info", None)

    summary = {
        "audited": len(slugs), "ran_at": utcnow_iso(),
        "clean": len(slugs) - len(results) - len(errors),
        "with_hard_issues": len(results), "hard_findings": hard_total,
        "errors": errors,
        "site_ref_segments": dict(site_all.most_common(20)),
        "external_ref_domains": dict(ext_all.most_common(15)),
        "problems": results,
    }
    out = args.out or repo_path("specs", "001-sep-sync-pipeline", "en-integrity-full.json")
    if args.out or args.all:
        write_json_verified(out, summary)
        summary["evidence"] = out
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if (hard_total or errors) else 0


if __name__ == "__main__":
    sys.exit(main())
