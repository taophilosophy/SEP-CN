# -*- coding: utf-8 -*-
"""en/<slug>/index.html 本体格式与内容审计（ADR-0052 s0_source_checked 前置环节）。

零信任前置的 HTML-first 核查：翻译动笔之前先确认源 HTML 本身格式与内容无恙。
与 en_integrity.py（包完整性/引用闭包）互补，本工具查内容与结构正确性：
  1. 页面真实性：错误页/风控页标记、</html> 截断；
  2. typo 候选（启发式，只产候选不裁决——人按 ADR-0062 两路定性：文字层→
     全局勘误表＋中文译注，格式层→baseline/en-patches/ 补丁池）：
     词内混入数字/等号（`Cambridh=ge`、`3s` 型）、重复词、异常标点串；
  3. 死链：页内锚点（href="#X" → id/name=X）、站内词条链接（/entries/<slug>/
     须在 baseline/entries.json 目录中）、外链盘点；--net 活体检查
     （退避重试＋state/link_cache.json URL 级缓存）；
  4. 图片：包内资产存在性（硬）、alt 缺失（告警）；
  5. 公式：\\(…\\)/\\[…\\] 定界符配对（硬）、TeX 花括号平衡（硬）、
     \\unicode/\\char 已知渲染问题族（告警，ADR-0049）；
  6. 表格：<table> 无 <tr>（硬）、table 配平（硬）、嵌套表（信息）；
  7. 注释/交叉引用：note/fn 孤儿定义（定义无引用，告警）；
  8. 段落/标题：空段落（告警）、标题层级跳档（告警）。

机检不作裁判（specs/018 先例）：hard 项是 advance --step s0 的门禁（task_ops
_source_gate）；warn/info 逐条人工定性，处置出口（ADR-0062，en/ 绝对冻结）＝
全局勘误表（baseline/en-errata/en-errata.md，ADR-0076）＋中文译注；
格式层问题入 baseline/en-patches/ 补丁池（一补丁一文件）；其余登记待考/豁免留痕。死链只
登记不改正文（外链失效属上游时效，不属缺陷面）。

用法:
  python tools/en_source_audit.py <slug>...       # 离线审计
  python tools/en_source_audit.py --all [--out <path>] [--net] [--net-refresh]
输出: stdout JSON 摘要（--out 落盘完整凭证）。
退出码: 0 干净（仅信息/告警级）；1 有硬问题；2 错误。
"""
import argparse
import html
import json
import os
import re
import sys
import time
from collections import Counter
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import load_json, repo_path, utcnow_iso  # noqa: E402

SITE = "https://plato.stanford.edu"
MARKERS = ["attention required", "just a moment", "access denied",
           "request unsuccessful", "incapsula", "error 403", "error 404",
           "page not found", "too many requests"]
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
MATH_BLOCK_RE = re.compile(r"<math\b.*?</math>", re.S | re.I)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'src="([^"]+)"', re.I)
HREF_RE = re.compile(r'href="([^"]+)"', re.I)
ID_RE = re.compile(r'\b(?:id|name)="([^"]+)"')
TAG_RE = re.compile(r"<[^>]+>")
HEADING_RE = re.compile(r"<h([1-6])\b", re.I)
TABLE_RE = re.compile(r"<table\b.*?</table>", re.S | re.I)
EMPTY_P_RE = re.compile(r"<p>(?:\s|&nbsp;|&#160;)*</p>", re.I)
CACHE_PATH = None  # 惰性初始化：state/link_cache.json


def _load_html(slug):
    p = repo_path("en", slug, "index.html")
    if not os.path.exists(p):
        raise FileNotFoundError("en/%s/index.html 不存在（先 fetch_entry）" % slug)
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def _text_nodes(raw):
    """剥 script/style/comments/math 与标签后留下文本（typo 检查用）。"""
    t = SCRIPT_STYLE_RE.sub(" ", raw)
    t = COMMENT_RE.sub(" ", t)
    t = MATH_BLOCK_RE.sub(" ", t)
    t = re.sub(r"\\\(.*?\\\)", " ", t, flags=re.S)
    t = re.sub(r"(?<!\\)\\\[.*?(?<!\\)\\\]", " ", t, flags=re.S)
    t = TAG_RE.sub(" ", t)
    t = html.unescape(t)
    t = re.sub(r"doi:\S+", " ", t)  # DOI 后缀（exp043/jzad002 型）不作 typo 候选
    t = re.sub(r"[A-Za-z0-9._+-]+ *@ *[A-Za-z0-9. -]+", " ", t)  # 混淆邮箱
    return t


def _classify(src, slug):
    """引用 → (scope, target, frag)（与 en_integrity 同口径：urljoin 到
    /entries/<slug>/ 的上游 URL 语义）。
    scope: fragment（纯页内锚点）/ entry（站内词条空间，target=词条空间相对路径）/
    site（站点框架）/ external（外链，target=完整 URL）。"""
    s = html.unescape(src).strip()
    frag = None
    if "#" in s:
        s, frag = s.split("#", 1)
    if not s:
        return ("fragment", None, frag)
    url = urljoin(SITE + "/entries/%s/" % slug, s.split("?")[0])
    p = urlparse(url)
    if p.scheme not in ("http", "https"):
        return ("site", None, frag)
    if p.netloc != "plato.stanford.edu":
        return ("external", url, frag)
    if p.path.startswith("/entries/"):
        return ("entry", p.path[len("/entries/"):], frag)
    return ("site", None, frag)


def _check_page(raw, out):
    low = raw.lower()
    if "</html>" not in low:
        out["hard"].append({"class": "truncation", "msg": "缺少 </html>，疑似截断"})
    # 错误/风控页标记只在页头区（title＋导航，前 4000 字符）识别：
    # 词条正文与书目深处出现同词串（zombies 先例：论文题 'Access Denied
    # to Zombies'）不构成抓取失败信号（specs/036 裁定表）
    head = low[:4000]
    for m in MARKERS:
        if m in head:
            out["hard"].append({"class": "error_page", "msg": "命中错误页/风控页标记: %s" % m})
            break


def _check_typo(text, out):
    """启发式候选（warn 级）：只产候选，人按 ADR-0062 两路定性（表＋译注／补丁）。"""
    cands = []
    seen = set()
    # 词内混入数字/等号（Lakatos1978a、Cambridh=ge 型；1999a 年份后缀不以字母起头不命中）
    # 两段式：先以无嵌套量词的线性正则取整词，再用判定式复现原语义——原写法
    # `(?:[0-9=][A-Za-z0-9]*)+` 的 `*` 与后续 `[0-9=]` 争同一批数字，有指数回溯面
    # （CodeQL py/redos）。语义：字母起头（≥2）且词内含数字/等号、以字母数字收尾。
    for m in re.finditer(r"\b[A-Za-z]{2}[A-Za-z0-9=]*", text):
        tok = m.group(0)
        if not any(c.islower() for c in tok):
            continue  # 全大写缩写（MEGA1/ISO3166 型）通常合法
        tok = tok.rstrip("=")  # 原模式末尾须命中 \b，行尾孤等号不计入词
        if not re.search(r"[0-9=]", tok):
            continue  # 纯字母词不属本类
        if tok not in seen:
            seen.add(tok)
            cands.append({"kind": "word_digit_eq", "token": tok,
                          "ctx": text[max(0, m.start() - 40):m.end() + 40].strip()})
    # 重复词（the the / had had 型；英语偶有合法重叠，人工判读）
    for m in re.finditer(r"\b([A-Za-z]{3,})\s+\1\b", text, re.I):
        if m.group(1).lower() not in ("that", "had", "very"):  # 常见合法重叠降噪
            cands.append({"kind": "doubled_word", "token": m.group(0),
                          "ctx": text[max(0, m.start() - 40):m.end() + 40].strip()})
    # 数字替换字母（exists 3s 型）与 pp.缺空格 体例（en-errata #2/#12 先例）
    for m in re.finditer(r"\b\d{1,3}[sz]\b", text):
        cands.append({"kind": "digit_for_letter", "token": m.group(0),
                      "ctx": text[max(0, m.start() - 40):m.end() + 40].strip()})
    for m in re.finditer(r"\bpp\.\d", text):
        cands.append({"kind": "pp_no_space", "token": m.group(0),
                      "ctx": text[max(0, m.start() - 40):m.end() + 40].strip()})
    # 异常标点串
    for pat, label in ((r"[a-z],[a-z]", "comma_no_space"), (r",{2,}|;;|\.\.(?!\.)", "punct_run")):
        for m in re.finditer(pat, text):
            cands.append({"kind": label, "token": m.group(0),
                          "ctx": text[max(0, m.start() - 40):m.end() + 40].strip()})
    for c in cands[:80]:
        c.update(cls="typo_candidate")
        out["warn"].append(c)
    if len(cands) > 80:
        out["warn"].append({"cls": "typo_candidate", "kind": "truncated",
                            "msg": "候选 %d 条仅记 80 条，全量见原文扫描" % len(cands)})


def _check_links(raw, slug, ids, out, catalog):
    # SEP 官方注释停用链接（<!--<a href="..">-->…，188 件存量）不算活链：
    # 与 _text_nodes 同口径先剥注释，注释内锚点不作链接核对（specs/036 裁定表）
    raw = COMMENT_RE.sub(" ", raw)
    # 目录比对大小写不敏感（zombies 先例：源 href ../Russellian-monism/，
    # catalog 键 russellian-monism；slug 本体语义不因 href 大小写漂移）
    catalog_lower = {c.lower() for c in catalog} if catalog else set()
    entry_counts = Counter()
    external = []

    def _entry_target(rest):
        """词条空间相对路径（自 slug 起）→ (slug2, 子路径或 None)。"""
        first = rest.split("/")[0] if rest else ""
        if not first:
            return slug, None
        if first == slug:  # 自包引用：剥离 slug 前缀得包内相对路径
            sub = rest[len(first):].lstrip("/")
            return slug, (sub or None)
        if (catalog and first in catalog) or rest.endswith("/"):
            return first, None  # 目录形链接（../slug/）按词条链接；不在目录者由调用方报
        return slug, rest  # 其余按自包资产核对（多半是缺件/错名）

    for m in HREF_RE.finditer(raw):
        href = html.unescape(m.group(1)).strip()
        if not href or href in ("#",):
            continue
        scope, target, frag = _classify(href, slug)
        if scope == "fragment":
            # 纯页内锚点：目标必须在本文档（他页 fragment 无法离线核对，不查）
            if frag and frag not in ids:
                out["hard"].append({"class": "anchor_missing", "msg": "页内锚点无目标",
                                    "href": href})
            continue
        if scope == "entry":
            slug2, sub = _entry_target(target or "")
            if sub:
                if not os.path.exists(repo_path("en", slug, sub)):
                    out["hard"].append({"class": "asset_missing",
                                        "msg": "包内链接目标缺失: %s" % href})
                continue
            if catalog is not None and slug2 != slug \
                    and slug2.lower() not in catalog_lower:
                out["hard"].append({"class": "entry_link_bad",
                                    "msg": "站内词条链接不在目录: %s（catalog 可能过期，"
                                           "先 fetch_catalog）" % href})
            entry_counts[slug2] += 1
        elif scope == "external":
            external.append(target)
        # site：站点框架（/css /js /symbols /search 等），en_integrity 管职责
    out["counts"]["entry_links"] = sum(entry_counts.values())
    out["counts"]["external_links"] = len(external)
    return external


def _net_check(external, out, refresh=False):
    """外链活体检查：URL 级缓存＋退避。死链 warn（登记不修）。"""
    global CACHE_PATH
    if CACHE_PATH is None:
        CACHE_PATH = repo_path("state", "link_cache.json")
    cache = load_json(CACHE_PATH) if os.path.exists(CACHE_PATH) else {}
    dead = []
    checked = 0
    for url in sorted(set(external)):
        rec = cache.get(url)
        if rec and not refresh:
            status = rec.get("status")
        else:
            status = None
            for attempt in range(3):
                try:
                    req = Request(url, method="HEAD",
                                  headers={"User-Agent": "SEP-CN-audit/1.0"})
                    with urlopen(req, timeout=30) as r:
                        status = r.status
                    break
                except Exception as e:  # HTTPError 带 code；其余网络错误退避重试
                    code = getattr(e, "code", None)
                    if code == 405:  # 不支持 HEAD，降级 GET
                        try:
                            with urlopen(Request(url, headers={
                                    "User-Agent": "SEP-CN-audit/1.0"}), timeout=30) as r:
                                status = r.status
                            break
                        except Exception as e2:
                            code = getattr(e2, "code", None)
                    if code and code < 500:
                        status = code
                        break
                    status = code or "net_error"
                    time.sleep(2 * (attempt + 1))
            cache[url] = {"status": status, "checked_at": utcnow_iso()}
            checked += 1
            with open(CACHE_PATH, "w", encoding="utf-8") as f:
                json.dump(cache, f, ensure_ascii=False, indent=1)
        if status not in (200, 301, 302, 303, 307, 308, 999):
            dead.append({"url": url, "status": status})
    out["counts"]["net_checked"] = checked
    for d in dead:
        d.update(cls="dead_link", note="登记不修（上游时效，不属缺陷面；ADR-0062）")
        out["warn"].append(d)


def _check_images(raw, slug, out):
    for tag in IMG_RE.finditer(raw):
        tag_s = tag.group(0)
        m = SRC_RE.search(tag_s)
        if not m:
            out["hard"].append({"class": "img_no_src", "msg": "img 无 src: %s" % tag_s[:120]})
            continue
        scope, target, _ = _classify(m.group(1), slug)
        if scope == "entry" and target and "/" not in target.rstrip("/"):
            if not os.path.exists(repo_path("en", slug, target)):
                out["hard"].append({"class": "asset_missing",
                                    "msg": "图片不在包内: %s" % m.group(1)})
        if "alt=" not in tag_s:
            out["warn"].append({"cls": "img_no_alt", "msg": "img 缺 alt",
                                "src": m.group(1)})


def _check_math(raw, out):
    n_open_i = len(re.findall(r"\\\(", raw))
    n_close_i = len(re.findall(r"\\\)", raw))
    n_open_d = len(re.findall(r"(?<!\\)\\\[", raw))
    n_close_d = len(re.findall(r"(?<!\\)\\\]", raw))
    out["counts"]["math_inline"] = n_open_i
    out["counts"]["math_display"] = n_open_d
    if n_open_i != n_close_i:
        out["hard"].append({"class": "math_delim", "msg":
                            "\\( %d 处与 \\) %d 处不配对" % (n_open_i, n_close_i)})
    if n_open_d != n_close_d:
        out["hard"].append({"class": "math_delim", "msg":
                            "\\[ %d 处与 \\] %d 处不配对" % (n_open_d, n_close_d)})
    for m in re.finditer(r"\\\(.*?\\\)|(?<!\\)\\\[.*?(?<!\\)\\\]", raw, re.S):
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
            out["hard"].append({"class": "math_brace",
                                "msg": "TeX 花括号不平衡: %s" % tex[:100]})
    n_uni = len(re.findall(r"\\unicode\b|\\char\b", raw))
    if n_uni:
        out["warn"].append({"cls": "math_unicode", "msg":
                            "\\unicode/\\char 共 %d 处（ADR-0049 渲染问题族，逐处核对）" % n_uni})


def _check_tables(raw, out):
    tables = TABLE_RE.findall(raw)
    out["counts"]["tables"] = len(tables)
    for t in tables:
        if not re.search(r"<tr[\s>]", t, re.I):
            out["hard"].append({"class": "table_no_row",
                                "msg": "table 无 <tr>: %s" % t[:100]})
        if TABLE_RE.search(t[7:]):  # 嵌套表（018 已知转换器透传类，信息级）
            out["info"].append({"cls": "nested_table", "msg": "嵌套 table（核对转换透传）"})


def _check_structure(raw, out, ids):
    heads = [int(h) for h in HEADING_RE.findall(raw)]
    out["counts"]["headings"] = len(heads)
    for a, b in zip(heads, heads[1:]):
        if b > a + 1:
            out["warn"].append({"cls": "heading_skip",
                                "msg": "标题层级跳档 h%d→h%d" % (a, b)})
    if EMPTY_P_RE.search(raw):
        out["warn"].append({"cls": "empty_paragraph",
                            "msg": "存在空段落 <p></p>（共 %d 处）" % len(EMPTY_P_RE.findall(raw))})
    # note/fn 孤儿定义：id 存在但从未被 href 引用
    refs = set()
    for m in HREF_RE.finditer(raw):
        h = html.unescape(m.group(1))
        if h.startswith("#"):
            refs.add(h[1:])
    orphans = sorted(i for i in ids if re.match(r"(note|fn)[-_]", i) and i not in refs)
    if orphans:
        out["warn"].append({"cls": "orphan_note", "msg": "无引用的 note/fn 定义",
                            "ids": orphans[:40]})


def audit_slug(slug, net=False, net_refresh=False):
    raw = _load_html(slug)
    out = {"slug": slug, "hard": [], "warn": [], "info": [], "counts": {},
           "checked_at": utcnow_iso()}
    _check_page(raw, out)
    catalog = None
    cat_path = repo_path("baseline", "entries.json")
    if os.path.exists(cat_path):
        catalog = {e["slug"] for e in load_json(cat_path)["entries"]}
    ids = {html.unescape(i) for i in ID_RE.findall(raw)}
    external = _check_links(raw, slug, ids, out, catalog)
    _check_images(raw, slug, out)
    _check_math(raw, out)
    _check_tables(raw, out)
    _check_structure(raw, out, ids)
    _check_typo(_text_nodes(raw), out)
    if net:
        _net_check(external, out, net_refresh)
    return out


def _collect_external(raw, slug):
    external = []
    for m in HREF_RE.finditer(raw):
        href = html.unescape(m.group(1)).strip()
        if href.startswith("#") or not href or href in ("#",):
            continue
        if href.lower().startswith(("mailto:", "javascript:", "tel:", "data:")):
            continue
        path, _, _ = _resolve(href, slug)
        if path and path.startswith("http") and not path.startswith(SITE + "/"):
            external.append(path)
    return sorted(set(external))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--net", action="store_true", help="外链活体检查")
    ap.add_argument("--net-refresh", action="store_true", help="忽略缓存重检")
    args = ap.parse_args(argv if argv is not None else sys.argv[1:])
    if args.all:
        endir = repo_path("en")
        slugs = sorted(d for d in os.listdir(endir)
                       if os.path.exists(os.path.join(endir, d, "index.html")))
    elif args.slugs:
        slugs = args.slugs
    else:
        ap.error("给 <slug> 或 --all")
        return 2
    reports, hard, errors = [], 0, 0
    for slug in slugs:
        try:
            rep = audit_slug(slug, net=args.net, net_refresh=args.net_refresh)
        except FileNotFoundError as e:
            print(json.dumps({"slug": slug, "error": str(e)}, ensure_ascii=False))
            errors += 1
            continue
        hard += len(rep["hard"])
        reports.append(rep)
        slim = {k: (v if k != "info" else len(v)) for k, v in rep.items()}
        print(json.dumps(slim, ensure_ascii=False))
    if args.out:
        from tools.common import write_json_verified
        write_json_verified(args.out, {"checked_at": utcnow_iso(),
                                       "reports": reports})
    print(json.dumps({"slugs": len(reports), "hard_total": hard,
                      "errors": errors}, ensure_ascii=False))
    return 1 if hard else (2 if errors else 0)


if __name__ == "__main__":
    sys.exit(main())
