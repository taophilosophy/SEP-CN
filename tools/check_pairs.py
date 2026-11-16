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

体例轴（ADR-0063，s2.4 硬档，`--gate` 模式只对以下几则拦）:
      tail-order（尾节齐备与顺序：参考文献>学术工具>其他网络资源>相关词条，脚注恒末位；
        译者注释可选末节——ADR-0065）
      heading-number（小节编号点号式 `N.` / `N.N`，与原文一致；跳号同报）
      h1-form（H1 缺作者括号，或与 yuanwen 同件 H1 英文题不符）
      errata-apply（全局勘误表落地：承载=译注 的件，正文禁含上游错字形且须有译注承载；
        承载形态过渡期两可——句内 `（译注：…）`（ADR-0062 决策 4 旧形态，迁移随回炉批）
        或 `## 译者注释` 节（ADR-0065 新形态）；两处引用错字形均豁免）
      note-anchor（译者注释节锚点：节存在时须为末节且非空；正文圈号与节内条目
        一一对应、连续编号 1..N、锚点紧贴句末标点；字符域 U+2460–2473（①–⑳），
        21+ 用 U+3251–（㉑…）；ADR-0065）
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
         "tail-order", "heading-number", "h1-form", "errata-apply", "note-anchor")

# 体例轴硬档（ADR-0063）：`--gate` 模式只对这几则计退出码，供 s2.4 `_style_gate` 使用
HARD_RULES = ("tail-order", "heading-number", "h1-form", "errata-apply", "pubinfo-form",
              "note-anchor")

ZTAIL = ("参考文献", "学术工具", "其他网络资源", "相关词条")
ZNOTES = "脚注"
ZNOTE_SEC = "译者注释"          # ADR-0065：可选末节
# 圈号字符域：①–⑳ = U+2460–2473；㉑–㉟ = U+3251–325F；㊱–㊿ = U+32B1–32BF
_CIRCLED_RANGES = ((0x2460, 0x2473), (0x3251, 0x325F), (0x32B1, 0x32BF))
NUM2CH = {}
_n = 1
for _lo, _hi in _CIRCLED_RANGES:
    for _cp in range(_lo, _hi + 1):
        NUM2CH[_n] = chr(_cp)
        _n += 1
CH2NUM = {ch: num for num, ch in NUM2CH.items()}
CIRCLED_RE = re.compile("[" + re.escape("".join(NUM2CH[ch] for ch in sorted(NUM2CH))) + "]")
ANCHOR_OK_PREV = tuple("。！？；：…”』〉》）")  # 锚点合法的前一字符（句末标点/右引号/右书名号/右括号）
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
    if ZNOTE_SEC in h2:
        # ADR-0065：译者注释为可选末节——必须在全部尾节与脚注之后，且为最后一个二级标题
        anchor = max([h2.index(t) for t in ZTAIL] + ([h2.index(ZNOTES)] if ZNOTES in h2 else []))
        if h2.index(ZNOTE_SEC) < anchor:
            issues.append({"path": path, "line": 0, "rule": "tail-order",
                           "detail": "「译者注释」不在末位（应置于「脚注」之后，ADR-0065）"})
        elif h2[-1] != ZNOTE_SEC:
            issues.append({"path": path, "line": 0, "rule": "tail-order",
                           "detail": "「译者注释」之后仍有其他二级标题：%s" % "、".join(h2[h2.index(ZNOTE_SEC) + 1:][:3])})


def check_heading_number(path, text, issues):
    h2_num = []
    for m in re.finditer(r"^(#{2,4})\s+(.+)$", text, re.M):
        level, title = len(m.group(1)), m.group(2).strip()
        if title in ZTAIL or title in (ZNOTES, ZNOTE_SEC):
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
            pass  # H3 编号形态随原文（N2 离线对齐保证与 yuanwen 一致），运行时不再单查形态
    for prev, cur in zip(h2_num, h2_num[1:]):
        if cur != prev + 1:
            issues.append({"path": path, "line": 0, "rule": "heading-number",
                           "detail": "小节编号跳号：%d → %d" % (prev, cur)})


def split_note_section(text):
    """按 ADR-0065 拆出「译者注释」节：返回 (body, notes_lines)。

    节由 `## 译者注释` 标题起至下一标题或文末；无该节则 notes_lines 为空。
    """
    m = re.search(r"^##\s*%s\s*$" % ZNOTE_SEC, text, re.M)
    if not m:
        return text, []
    body = text[:m.start()]
    rest = text[m.end():]
    nxt = re.search(r"^#{1,6}\s", rest, re.M)
    notes = rest[:nxt.start()] if nxt else rest
    return body, notes.splitlines()


def check_note_anchor(path, text, issues):
    """译者注释节锚点检查（ADR-0065；节非强制，存在即查）。

    断言：①节为最后一个二级标题且非空；②节内条目以圈号开头、连续 1..N；
    ③正文圈号序列与节内条目号完全一致；④正文锚点紧贴句末标点/右引号。
    """
    body, notes = split_note_section(text)
    has_sec = "## %s" % ZNOTE_SEC in text or bool(re.search(r"^##\s*%s\s*$" % ZNOTE_SEC, text, re.M))
    # 节内条目号
    sec_nums = []
    for ln in notes:
        m = CIRCLED_RE.match(ln.lstrip())
        if m:
            sec_nums.append(CH2NUM[m.group(0)])
    if not has_sec:
        # 无节：正文不得出现圈号锚点（出现即缺承载）
        for m in CIRCLED_RE.finditer(_strip_anchors_zone(body)):
            issues.append({"path": path, "line": 0, "rule": "note-anchor",
                           "detail": "正文有锚点 %s 但无「译者注释」节（ADR-0065）" % m.group(0)})
        return
    if not notes or not sec_nums:
        issues.append({"path": path, "line": 0, "rule": "note-anchor",
                       "detail": "「译者注释」节为空（节非强制，存在即须有条目）"})
        return
    for a, b in zip(sec_nums, sec_nums[1:]):
        if b != a + 1:
            issues.append({"path": path, "line": 0, "rule": "note-anchor",
                           "detail": "节内条目编号不连续：%d → %d" % (a, b)})
    # 正文圈号序列（排除引块、书目/脚注定义行、表格行、代码行）
    body_nums = []
    for ln in _strip_anchors_zone(body).splitlines():
        t = ln.strip()
        if not t or t.startswith(">") or t.startswith("|") or re.match(r"^\[\^[^\]]+\]:", t):
            continue
        for m in CIRCLED_RE.finditer(t):
            body_nums.append(CH2NUM[m.group(0)])
            prev = t[:m.start()].rstrip()
            if prev and prev[-1] not in ANCHOR_OK_PREV:
                issues.append({"path": path, "line": 0, "rule": "note-anchor",
                               "detail": "锚点 %s 未紧贴句末标点（前一字符 `%s`）：%s"
                                         % (m.group(0), prev[-1], t[:36])})
    for a, b in zip(body_nums, body_nums[1:]):
        if b != a + 1:
            issues.append({"path": path, "line": 0, "rule": "note-anchor",
                           "detail": "正文锚点编号不连续：%d → %d" % (a, b)})
    if body_nums != sec_nums:
        issues.append({"path": path, "line": 0, "rule": "note-anchor",
                       "detail": "正文锚点与节内条目不对称：正文 %s vs 节内 %s"
                                 % (body_nums[:8], sec_nums[:8])})


def _strip_anchors_zone(text):
    """剥围栏代码块与行内代码（锚点扫描面）。数学跨度不动——公式内不应有圈号，出现即违规。"""
    return re.sub(r"```[\s\S]*?```|`[^`]*`", "", text)


def check_errata(path, slug, text, issues):
    rows = load_errata().get(slug)
    if not rows:
        return
    # 译文正文面：引块（照录英文原文）与书目照录区不计，ADR-0062 决策 4 豁免；
    # 「译者注释」节整节不计（其职责正是引用上游错字形，ADR-0065）；
    # 句内 `（译注：…）` 跨度屏蔽（旧形态过渡豁免，迁移随回炉批，ADR-0065）。
    body, _notes = split_note_section(text)
    lines, in_bib = [], False
    for line in body.splitlines():
        if line.startswith("#"):
            in_bib = line.strip() in ("## 参考文献", "## 参考文献 ")
            continue
        if in_bib or line.lstrip().startswith(">"):
            continue
        lines.append(line)
    prose = mask_notes("\n".join(lines))
    has_carrier = bool(_notes and any(CIRCLED_RE.match(ln.lstrip()) for ln in _notes)) \
        or "译注" in text
    for r in rows:
        carrier = r["carrier"]
        if "译注" not in carrier or "无需译注" in carrier:
            continue
        src = r["src"].strip("`")
        if len(src) >= 6 and src in prose:
            issues.append({"path": path, "line": 0, "rule": "errata-apply",
                           "detail": "正文仍含上游错字形 `%s`（ADR-0062 决策 4：译文不复制错字）"
                                     % src[:40]})
        if not has_carrier:
            issues.append({"path": path, "line": 0, "rule": "errata-apply",
                           "detail": "勘误表命中但无译注承载（句内或「译者注释」节，上游 `%s`）"
                                     % src[:40]})


def norm_title(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def check_h1_form(path, text, issues, yw_text=None):
    first = text.splitlines()[0] if text else ""
    if not first.startswith("# "):
        return
    h1 = first[2:].strip()
    # 作者括号容嵌套（如 Jan van Eijck、Rineke (L.C.) Verbrugge）
    if not re.search(r"[（(].*[)）]\s*$", h1):
        issues.append({"path": path, "line": 1, "rule": "h1-form",
                       "detail": "H1 缺作者括号（应 `# 中文题 英文题 (作者)`）：%s" % h1[:40]})
    if yw_text:
        yw_h1 = next((l[2:].strip() for l in yw_text.splitlines() if l.startswith("# ")), "")
        if yw_h1 and norm_title(yw_h1) not in norm_title(h1):
            issues.append({"path": path, "line": 1, "rule": "h1-form",
                           "detail": "H1 缺原文英文题 `%s`" % yw_h1[:40]})


NOTE_OPEN_RE = re.compile(r"[（(]译注")


def mask_notes(text):
    """把「（译注：…）」跨度替换为等长空格（平衡括号扫描，保留换行与长度）。

    ADR-0062 决策 4 要求译注**引用**上游错字形（`（译注：上游原文作“…”）`），
    故勘误落地检查须先屏蔽译注跨度，否则每条合格译注都会自我触发。
    """
    out = list(text)
    pos = 0
    while True:
        m = NOTE_OPEN_RE.search(text, pos)
        if not m:
            break
        depth, j = 0, m.start()
        while j < len(text):
            ch = text[j]
            if ch in "（(":
                depth += 1
            elif ch in "）)":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        for k in range(m.start(), min(j + 1, len(text))):
            if text[k] != "\n":
                out[k] = " "
        pos = j + 1
    return "".join(out)


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
    zh_h = len([t for t in re.findall(r"^#{2,3}\s+(.+)$", zh_text, re.M)
                if t.strip() != ZNOTE_SEC])  # ADR-0065：译者注释节为中文独有，不入节标题对账
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
    seen_heading = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("#"):
            seen_heading = True
            in_biblio = bool(BIB_HEAD.match(line))
            continue
        if line.startswith("|"):
            continue
        check_brackets(path, lineno, line, issues)
        if not seen_heading:
            # pubinfo 只查首节前的题头区（书目 def 与正文叙述里的“首次发表于”不算）
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
        check_note_anchor(path, text, issues)
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
