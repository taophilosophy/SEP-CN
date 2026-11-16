# -*- coding: utf-8 -*-
"""格式配对与一致性预检（告警级，不进 CI；ADR-0045 流程增补）。

用法: python tools/check_pairs.py <路径>... [--strict]
输出: stdout JSON {files, issues:[{path,line,rule,detail}]}

规则（启发式清单，GB/T 15834/15289/26514 与业界引用一致性检查器启发）:
      bracket-pair（全角括号/方括号/书名号/六角括号 配对与方向：右先于左、负深度）
      cite-authoryear（文内作者-年份引注与书目条目启发式匹配：姓氏+年份未见于书目）
      bib-duplicate（书目条目重复：同键多 def 或同键规范化重复）
      count-vs-source（数量对照：节标题数/书目条数/公式数 zh vs en/yuanwen，容差告警；
        公式数两侧对称剔除孤立希腊字母片段——ADR-0049 文字化回改后 zh 侧归零而
        yuanwen 源形态仍在，不剔则回改必触告警）
      dangling-link（相对链接目标缺失：站内 md/目录两解均不存在）
      pubinfo-form（出版信息行非正典形态 > *…*）
      ellipsis-form（中文语境省略号非六连点）

体例轴（ADR-0063，s2.4 硬档，`--gate` 模式只对以下四则拦）:
      tail-order（尾节齐备与顺序：参考文献>学术工具>其他网络资源>相关词条，脚注恒末位）
      heading-number（小节编号点号式 `N.` / `N.N`，与原文一致；跳号同报）
      h1-form（H1 缺作者括号，或与 yuanwen 同件 H1 英文题不符）
      errata-apply（全局勘误表落地：承载=译注 的件，正文禁含上游错字形且须有译注）
      参考文献承载（marker↔定义配对）由 check_academic 管辖，本工具不重复实现。

豁免: 围栏代码块、行内代码、数学定界符、表格行（结构项除外）；桩件（无二级标题或
      <2KB）、带点补充材料子文档（`<slug>.<part>.md`）不适用体例轴。
对照文件推导: <letter>/<slug>.md → en/<slug>/index.html、yuanwen/<letter>/<slug>.md。
退出码: 0 无问题（告警级）；1 有 issue（仅 --strict）；1 且仅体例轴四则命中（--gate）。
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import read_text  # noqa: E402

RULES = ("bracket-pair", "cite-authoryear", "bib-duplicate", "count-vs-source",
         "dangling-link", "pubinfo-form", "ellipsis-form",
         "tail-order", "heading-number", "h1-form", "errata-apply")

# 体例轴硬档（ADR-0063）：`--gate` 模式只对这几则计退出码，供 s2.4 `_style_gate` 使用
HARD_RULES = ("tail-order", "heading-number", "h1-form", "errata-apply", "pubinfo-form")

ZTAIL = ("参考文献", "学术工具", "其他网络资源", "相关词条")
ZNOTES = "脚注"
ERRATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "specs", "001-sep-sync-pipeline", "results", "en-errata.md")
_ERRATA_CACHE = {}


def load_errata():
    """解析全局勘误表 §八/§九 的七列表行：slug → [{上游原文, 参考读法, 中文承载}]。

    只取七列表（§8.3 为五列待考行，不在此面）；表内 `slug` 列即键。
    """
    if _ERRATA_CACHE:
        return _ERRATA_CACHE
    rows = []
    if os.path.exists(ERRATA_PATH):
        text = read_text(ERRATA_PATH)
        start = text.find("## 八、")
        body = text[start:] if start >= 0 else ""
        for line in body.splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) != 7 or cells[0] in ("slug", "") or set(cells[0]) <= set("- "):
                continue
            rows.append({"slug": cells[0], "pos": cells[1], "src": cells[2],
                         "reading": cells[4], "carrier": cells[5]})
    for r in rows:
        _ERRATA_CACHE.setdefault(r["slug"], []).append(r)
    return _ERRATA_CACHE


def check_tail_order(path, text, issues):
    h2 = [m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", text, re.M)]
    if not h2:
        return  # 桩件
    present = [t for t in h2 if t in ZTAIL]
    missing = [t for t in ZTAIL if t not in h2]
    if missing:
        issues.append({"path": path, "line": 0, "rule": "tail-order",
                       "detail": "尾节缺失：%s" % "、".join(missing)})
        return
    idx = [ZTAIL.index(t) for t in present]
    if idx != sorted(idx):
        issues.append({"path": path, "line": 0, "rule": "tail-order",
                       "detail": "尾节顺序非正典（应 %s）：%s" % (" > ".join(ZTAIL), " > ".join(present))})
    if ZNOTES in h2:
        last_tail = max(h2.index(t) for t in ZTAIL)
        if h2.index(ZNOTES) < last_tail:
            issues.append({"path": path, "line": 0, "rule": "tail-order",
                           "detail": "「脚注」不在末位（应置于「相关词条」之后，ADR-0063）"})


def check_heading_number(path, text, issues):
    h2_num = []
    for m in re.finditer(r"^(#{2,4})\s+(.+)$", text, re.M):
        level, title = len(m.group(1)), m.group(2).strip()
        if title in ZTAIL or title == ZNOTES:
            continue
        if not title[:1].isdigit():
            continue
        if level == 2:
            mm = re.match(r"^(\d+)\.\s+\S", title)
            if not mm:
                issues.append({"path": path, "line": 0, "rule": "heading-number",
                               "detail": "二级标题须点号式 `N. 标题`：%s" % title[:36]})
            else:
                h2_num.append(int(mm.group(1)))
        elif level == 3:
            if not re.match(r"^\d+\.\d+\s+\S", title):
                issues.append({"path": path, "line": 0, "rule": "heading-number",
                               "detail": "三级标题须 `N.N 标题`（父号.子号）：%s" % title[:36]})
    for prev, cur in zip(h2_num, h2_num[1:]):
        if cur != prev + 1:
            issues.append({"path": path, "line": 0, "rule": "heading-number",
                           "detail": "小节编号跳号：%d → %d" % (prev, cur)})


def norm_title(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def check_h1_form(path, text, issues, yw_text=None):
    first = text.splitlines()[0] if text else ""
    if not first.startswith("# "):
        return
    h1 = first[2:].strip()
    if not re.search(r"[（(][^（()）]+[)）]\s*$", h1):
        issues.append({"path": path, "line": 1, "rule": "h1-form",
                       "detail": "H1 缺作者括号（应 `# 中文题 英文题 (作者)`）：%s" % h1[:40]})
    if yw_text:
        yw_h1 = next((l[2:].strip() for l in yw_text.splitlines() if l.startswith("# ")), "")
        if yw_h1 and norm_title(yw_h1) not in norm_title(h1):
            issues.append({"path": path, "line": 1, "rule": "h1-form",
                           "detail": "H1 缺原文英文题 `%s`" % yw_h1[:40]})


def check_errata(path, slug, text, issues):
    rows = load_errata().get(slug)
    if not rows:
        return
    # 译文正文面：引块（照录英文原文）与书目照录区不计，ADR-0062 决策 4 豁免
    lines, in_bib = [], False
    for line in text.splitlines():
        if line.startswith("#"):
            in_bib = line.strip() in ("## 参考文献", "## 参考文献 ")
            continue
        if in_bib or line.lstrip().startswith(">"):
            continue
        lines.append(line)
    prose = "\n".join(lines)
    for r in rows:
        carrier = r["carrier"]
        if "译注" not in carrier or "无需译注" in carrier:
            continue
        src = r["src"].strip("`")
        if len(src) >= 6 and src in prose:
            issues.append({"path": path, "line": 0, "rule": "errata-apply",
                           "detail": "正文仍含上游错字形 `%s`（ADR-0062 决策 4：译文不复制错字）"
                                     % src[:40]})
        if "译注" not in text:
            issues.append({"path": path, "line": 0, "rule": "errata-apply",
                           "detail": "勘误表命中但全文无译注（上游 `%s`）" % src[:40]})

HAN = r"\u4e00-\u9fff"
MATH_RE = re.compile(r"\$\$.+?\$\$|\$[^$\n]+\$")
CODE_RE = re.compile(r"`[^`]*`")
PAIRS = (("（", "）"), ("《", "》"), ("〔", "〕"), ("【", "】"))
BIB_HEAD = re.compile(r"^#{1,6}\s*(?:参考文献|Bibliography|References（引用注释）)\s*$", re.M)
AY_RE = re.compile(r"（([A-Z][A-Za-zāáǎàééěèīíǐìóóǒòūúǔùü\u2019\-]{1,20})\s+(\d{4})[a-z]?(?:,\s*\d{1,4})?）")

# ADR-0049：纯孤立希腊字母行内片段（无撇号/下标/运算符），公式数对账时两侧对称剔除。
GREEK_LONE_RE = re.compile(
    r"\$\\(?:alpha|beta|gamma|delta|epsilon|varepsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|"
    r"pi|rho|sigma|tau|upsilon|phi|varphi|chi|psi|omega|varpi|varrho|varsigma|vartheta|"
    r"Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega)\$")


def _mask(line):
    t = MATH_RE.sub("\x00", line)
    return CODE_RE.sub("\x00", t)


def check_brackets(path, lineno, line, issues):
    t = _mask(line)
    if not re.search(r"[%s（）〔〕【】《》]" % HAN, t):
        return
    for lo, hi in PAIRS:
        depth = 0
        for i, ch in enumerate(t):
            if ch == lo:
                depth += 1
            elif ch == hi:
                if depth == 0:
                    prev = t[i - 1] if i else ""
                    if re.match(r"[\d一二三四五六七八九十]", prev):
                        continue  # 序次语 N）——零深度右括号前邻数字，GB/T 15834 序次语形态，放行
                    issues.append({"path": path, "line": lineno, "rule": "bracket-pair",
                                   "detail": "%s%s 右先于左：%s" % (lo, hi, t.strip()[:44])})
                    continue
                depth -= 1
        if depth != 0:
            issues.append({"path": path, "line": lineno, "rule": "bracket-pair",
                           "detail": "%s%s 不配对（深度 %d）：%s" % (lo, hi, depth, t.strip()[:44])})


def check_pubinfo(path, lineno, line, issues):
    s = line.strip()
    if "首次发表于" in s or "First published" in s:
        if not re.match(r"^>?\s*\*[^*]+\*\s*$", s):
            issues.append({"path": path, "line": lineno, "rule": "pubinfo-form",
                           "detail": "出版信息行非斜体正典形（应 `*…*` 或 `> *…*`）：%s" % s[:44]})


def check_ellipsis(path, lineno, line, issues):
    t = _mask(line)
    if not re.search(r"[%s]" % HAN, t):
        return
    for m in re.finditer(r"(?<!\.)\.{3}(?!\.)", t):
        issues.append({"path": path, "line": lineno, "rule": "ellipsis-form",
                       "detail": "中文语境三点省略号（应六连点 ……）：%s" % t.strip()[:44]})
        break


def check_links(path, lineno, line, issues, base_dir):
    t = _mask(line)
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", t):
        target = m.group(2).strip()
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        cand1 = os.path.normpath(os.path.join(base_dir, target))
        cand2 = os.path.normpath(os.path.join(os.path.dirname(base_dir), target))
        if os.path.exists(cand1) or os.path.exists(cand2):
            continue
        issues.append({"path": path, "line": lineno, "rule": "dangling-link",
                       "detail": "相对链接目标缺失 [%s](%s)" % (m.group(1)[:20], target[:40])})


def extract_bib_defs(text):
    """返回 (有序 (键, 行文本) 列表, 重复键列表)。引用注释形态：书目 def 无需文内 marker。"""
    ordered, dups = [], []
    for m in re.finditer(r"^\[\^([^\]\n]+)\]:\s*(.+)$", text, re.M):
        k, v = m.group(1), m.group(2)
        if any(k == kk for kk, _ in ordered):
            dups.append(k)
        ordered.append((k, v))
    return ordered, dups


def check_authoryear(path, lineno, line, issues, defs, en_text=None):
    t = _mask(line)
    for m in AY_RE.finditer(t):
        surname, year = m.group(1), m.group(2)
        # 破折号承接链（–––, 2002, …＝同上作者）：dash 行继承上一条的作者命中
        prev = False
        hit = False
        for _k, v in defs:
            dash = bool(re.match(r"^[—–]{2,}", v.strip()))
            cur = surname in v
            if (cur or (dash and prev)) and year in v:
                hit = True
                break
            prev = cur or (dash and prev)
        if hit:
            continue
        if en_text:
            mb = re.search(r"<h2[^>]*>\s*(?:Bibliography|References[^<]*)</h2>([\s\S]*?)(?:<h2|$)", en_text)
            en_bib = mb.group(1) if mb else ""
            if en_bib and re.search(re.escape(surname) + r"[\s\S]{0,120}" + year, en_bib):
                issues.append({"path": path, "line": lineno, "rule": "cite-authoryear",
                               "detail": "文内引注（%s %s）在 en 书目有对应条目而 zh 书目缺失：%s"
                                         % (surname, year, t.strip()[:40])})
            # en 书目亦无＝源风格提及（SEP 正文可提及书目未列之作），不计


def check_counts(path, slug, zh_text, issues, tol_head=2, tol_bib=2):
    en_p = os.path.join(os.path.dirname(path).rsplit(os.sep, 1)[0], "en", slug, "index.html")
    yw_p = os.path.join(os.path.dirname(path), "..", "yuanwen",
                        os.path.basename(os.path.dirname(path)), slug + ".md")
    en = read_text(en_p) if os.path.exists(en_p) else None
    yw = read_text(yw_p) if os.path.exists(yw_p) else None
    zh_h = len(re.findall(r"^#{2,3}\s", zh_text, re.M))
    if en:
        en_h = len(re.findall(r"<h[23][\s>]", en))
        if abs(zh_h - en_h) > tol_head:
            issues.append({"path": path, "line": 0, "rule": "count-vs-source",
                           "detail": "节标题数 zh %d vs en %d（容差 %d）" % (zh_h, en_h, tol_head)})
        mb = re.search(r"<h2[^>]*>\s*(?:Bibliography|References[^<]*)</h2>([\s\S]*?)(?:<h2|$)", en)
        zh_bib = len(re.findall(r"^\[\^[^\]\n]+\]:", zh_text, re.M))
        if mb:
            en_bib = len(re.findall(r"<li", mb.group(1)))
            if en_bib and abs(en_bib - zh_bib) > tol_bib:
                issues.append({"path": path, "line": 0, "rule": "count-vs-source",
                               "detail": "书目条数 zh %d vs en %d（容差 %d）" % (zh_bib, en_bib, tol_bib)})
    if yw:
        clean = lambda s: re.sub(r"```[\s\S]*?```|`[^`]*`", "", s)
        strip = lambda s: (len(re.findall(r"\$\$[^$]+\$\$|\$[^$\n]+\$", s))
                           - len(GREEK_LONE_RE.findall(s)))
        a, b = strip(clean(zh_text)), strip(clean(yw))
        if max(a, b) > 20 and abs(a - b) > max(3, int(0.1 * max(a, b))):
            issues.append({"path": path, "line": 0, "rule": "count-vs-source",
                           "detail": "公式数 zh %d vs yuanwen %d（偏差超 10%%）" % (a, b)})


def check_file(path):
    issues = []
    base_dir = os.path.dirname(os.path.abspath(path))
    text = read_text(path)
    slug = os.path.splitext(os.path.basename(path))[0]
    defs, dup = extract_bib_defs(text)
    en_p = os.path.join(os.path.dirname(base_dir), "en", slug, "index.html")
    en_text = read_text(en_p) if os.path.exists(en_p) else None
    yw_p = os.path.join(os.path.dirname(base_dir), "yuanwen",
                        os.path.basename(base_dir), slug + ".md")
    yw_text = read_text(yw_p) if os.path.exists(yw_p) else None
    for k in set(dup):
        issues.append({"path": path, "line": 0, "rule": "bib-duplicate",
                       "detail": "书目键重复定义 [^%s]（%d 次）" % (k, dup.count(k) + 1)})
    in_fence, in_biblio = False, False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("#"):
            in_biblio = bool(BIB_HEAD.match(line))
            continue
        if line.startswith("|"):
            continue
        check_brackets(path, lineno, line, issues)
        check_pubinfo(path, lineno, line, issues)
        check_ellipsis(path, lineno, line, issues)
        check_links(path, lineno, line, issues, base_dir)
        if not in_biblio:
            check_authoryear(path, lineno, line, issues, defs, en_text)
    check_counts(path, slug, text, issues)
    # 体例轴（ADR-0063）：桩件与带点补充材料子文档不适用
    if "." not in slug and "## " in text:
        check_tail_order(path, text, issues)
        check_heading_number(path, text, issues)
        check_h1_form(path, text, issues, yw_text)
        check_errata(path, slug, text, issues)
    return issues


def main(argv):
    args = [a for a in argv if a not in ("--strict", "--gate")]
    strict = "--strict" in argv
    gate = "--gate" in argv
    if not args:
        print(__doc__)
        return 2
    issues = []
    for p in args:
        issues.extend(check_file(p))
    print(json.dumps({"files": len(args), "issues": issues}, ensure_ascii=False, indent=1))
    if gate:
        return 1 if any(i["rule"] in HARD_RULES for i in issues) else 0
    return 1 if strict and issues else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
