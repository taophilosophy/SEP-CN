#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""B3.2 正文段装配补集：结构账抽取器。

只抽结构，不抽散文：
  hids        每个 h2/h3 的 id 形态（`X` 为 id 属性 / `name:X` / `aid:X` / 空串）
  bib_groups  文献分节各自的条目数（切分文献 ul）
  rel_links   相关条目链接（href＋显示文本＋死链注释标记）
  acad_icons  学术工具四行的图标与 alt
  wrap/entities 视觉层（空白位图与实体策略）由后续批次补入

产出 baseline/en-template/article-ledger.json（冻结派生件，重跑须复核）。
"""
import argparse
import hashlib
import html as htmllib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), "tools"))
from tools.common import repo_path  # noqa: E402

B1 = "<!-- BEGIN ARTICLE HTML -->"
E1 = "<!-- END ARTICLE HTML -->"
LEDGER_PATH = ("baseline", "en-template", "article-ledger.json")
HEAD_RE = re.compile(r"<h([2-6])((?:\s[^>]*)?)>(.*?)</h\1>", re.S)
# 脚注键判定：`note-<id>`（数字/字母/混合，来自 notes.html）。例外——后缀是四位
# 年份者（`note-2005`、`note-1831`）不是脚注：那是书目区散文段被 C 当条目建键
# （首词 Note + 年份，hutcheson／schlick 判例）。按书目定义处理，pd 才能定位
# 并原位发 <p>；误当脚注则整段丢（R 侧同判据，账与 R 必须同语料）。
_NOTE_KEY_RE = re.compile(r"^note-(?!1[5-9]\d\d\b|20\d\d\b)\S+$")


def _is_note_key(key):
    return bool(_NOTE_KEY_RE.match(key))


def read(p):
    return io.open(p, encoding="utf-8", newline="").read()


def inner_article(t):
    i1 = t.index(B1) + len(B1)
    i2 = t.index(E1)
    return t[i1:i2]


def hid_form(attrs, inner):
    m = re.search(r'\bid="([^"]*)"', attrs)
    if m:
        return m.group(1)
    m = re.search(r'<a\s+name="([^"]*)"', inner)
    if m:
        return "name:" + m.group(1)
    m = re.search(r'<a\s+id="([^"]*)"', inner)
    if m:
        return "aid:" + m.group(1)
    return ""


ENT_RE = re.compile(r"&(#[0-9]+|#[xX][0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]*);")


def extract_entities(art_inner):
    """实体策略：件内以实体形态出现的非 ASCII 字符 → 该实体串。

    同一字符若在本文中既以实体出现又以字面出现，视为非一致策略（不入账，
    交装配补集吸收）；`&amp;`/`&lt;`/`&gt;` 等 ASCII 实体不入账（R 自带转义）。
    """
    forms = {}
    ambig = set()
    for m in ENT_RE.finditer(art_inner):
        dec = htmllib.unescape(m.group(0))
        if len(dec) != 1 or ord(dec) < 128:
            continue
        forms.setdefault(dec, set()).add(m.group(0))
    # 字面出现统计：剥掉全部实体后计字面次数
    stripped = ENT_RE.sub("", art_inner)
    out = {}
    for ch, fs in forms.items():
        if len(fs) > 1 or ch in stripped:
            ambig.add(ch)
            continue
        out[ch] = next(iter(fs))
    return out


def wrap_width(art_inner):
    """折行宽度：源字符宽度（标签计入）贪心折行，取使 <p>/<li> 命中最多的一档。"""
    def wrap_src(flat, width):
        toks = flat.split(" ")
        lines, cur = [], toks[0]
        for tk in toks[1:]:
            if len(cur) + 1 + len(tk) > width:
                lines.append(cur)
                cur = tk
            else:
                cur += " " + tk
        lines.append(cur)
        return "\n".join(lines)

    samples = []
    for m in re.finditer(r"<p>\n(.*?)</p>", art_inner, re.S):
        if "<p>" in m.group(1):
            continue
        samples.append(m.group(1))
    for m in re.finditer(r"<li>(.*?)</li>", art_inner, re.S):
        if "<li>" in m.group(1):
            continue
        samples.append(m.group(1))
    if not samples:
        return None
    flows = [re.sub(r"\n", " ", s) for s in samples]
    best = (0, None)
    for w in range(60, 85):
        n = sum(1 for s, fl in zip(samples, flows) if wrap_src(fl, w) == s)
        if n > best[0]:
            best = (n, w)
    return best[1]


def _cut_region(s, start_pat, end_pat):
    m1 = re.search(start_pat, s)
    if not m1:
        return s
    m2 = re.search(end_pat, s[m1.end():])
    return s[:m1.start()] + s[m1.end() + (m2.end() if m2 else 0):]


def _count_word(text, needle):
    """同 R 侧一致的出现计数（词界判定），用于定义“第 n 次出现”。"""
    if not needle:
        return 0
    pat = "(?<![A-Za-z0-9])" + re.escape(needle) + "(?![A-Za-z0-9])"
    return len(re.findall(pat, text))


def extract_math_forms(art_inner):
    """显示公式形态账（文档序）：`br`＝`\\[…\\]` 包裹，`naked`＝裸排环境。

    C 侧 wrap_naked_envs（ADR-0049 决策 6）把裸 `\\begin{align}` 也包成
    `$$…$$` 送渲染，md 里两种形态都成了 `$$`；右逆若一律发 `\\[…\\]`，裸排件
    的文字层就多出定界符（belief-merging 判例：H0 `\\begin{align}` 对装配
    `\\[\\begin{align}…`）。账记原位形态，R 按游标还原。"""
    env = (r"align\*?|aligned|gather\*?|gathered|multline\*?|equation\*?|"
           r"eqnarray\*?|displaymath")
    # 行内段先原子吞掉：H0 有 `\(\begin{align*}…\)` 行内环境（negation
    # (21)(22) 判例），裸排分支会把行内当显示记账，R 的显示式游标随即错位，
    # 整页后续形态全错（负号真值表被发成裸排）。行内归 $…$，不入本账。
    pat = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]|\\begin\{(?P<e>" + env +
                     r")\}.*?\\end\{(?P=e)\}", re.S)
    out = []
    for m in pat.finditer(art_inner):
        head = m.group(0)[:2]
        if head == "\\(":
            continue
        out.append("br" if head == "\\[" else "naked")
    return out


def extract_math_dollars(art_inner):
    """行内公式的美元源形账：`\\(…\\)` 体内每个 `$` 是否为原文转义（`\\$`）。

    C 侧 `_esc_math_dollar` 把裸 `$` 一律写成 `\\$`（`\\($S\\)` 判例），原文
    已带转义的 `\\$` 形态不变——md 同形双源，右逆无法判别（dutch-book 18 裸
    对 decision-causal 17 转义）。账按**体内文字指纹**锚定（`\\$`/`$` 统一换
    哨兵后取 sha），避免 C 丢弃空式/单希腊降级造成的 span 序号漂移。
    """
    pat = re.compile(r"\\\((.*?)\\\)", re.S)
    out = []
    for m in pat.finditer(art_inner):
        body = m.group(1)
        if "$" not in body:
            continue
        forms = []
        i = 0
        while i < len(body):
            if body.startswith("\\$", i):
                forms.append("b")
                i += 2
                continue
            if body[i] == "$":
                forms.append("d")
            i += 1
        out.append([_dollar_blank(body), "".join(forms)])
    return out


def _dollar_blank(body):
    """`\\$` 与 `$` 统一替换为哨兵、且**折叠空白**后的指纹（两侧同式）。

    H0 与 md 的换行位置不同（C 重排段落），不折叠空白则同式指纹不等
    （formal-epistemology `u(-$10)\n\approx…` 对 `u(-\\$10) \approx…` 判例）。"""
    body = re.sub(r"\s+", "", body)
    for ch in ("\\$", "$"):
        body = body.replace(ch, "\x00")
    return hashlib.sha1(body.encode("utf-8")).hexdigest()[:16]


def extract_links(art_inner, skip=()):
    """C 丢弃的内部链接（跨词条 ../slug/、页内 #anchor），文档序＋出现序。

    扫描域＝正文区（剔 TOC／学术工具／相关条目三块——它们各有专用账）。
    nth＝该锚文在本文可见文字流中的第几次出现（0 基），R 按此定位，
    避免同文多处时把链接挂错位置（advance-directives 判例）。
    skip：题后散字等**不入 md** 的 H0 片段——其中的链接由散字原文整段发出，
    不再入链接账（否则 R 侧无对应锚文可消费，成假 link_miss）。"""
    s = art_inner
    s = _cut_region(s, '<div id="toc"', '</div>' + chr(92) + 's*(?=<div id="main-text">)')
    s = _cut_region(s, '<div id="academic-tools"', '</div>')
    s = _cut_region(s, '<div id="related-entries"', '</div>')
    # HTML 注释整体抹白（保偏移）：注释里被停用的 `<a>` 在 md 无锚文可消费，
    # 入账即成幽灵链接，永久卡在游标头部连锁饿死整页（findlay 两条
    # `#bib-H`/`#bib-K` 是 `<!-- <tr>… -->` 里的停用行）。全库 262 条。
    s = re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), s, flags=re.S)
    out = []
    for m in re.finditer('<a href="([^"]*)">(.*?)</a>', s, re.S):
        if any(m.group(0) in t for t in skip):
            continue
        href, inner = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "notes.html#")):
            continue
        # 三族入账：跨词条 `../slug/`、页内 `#anchor`、带片段的裸兄弟链
        # `other.html#frag`。第三族 C 在 md 侧把片段整个丢掉（`slug.target.md`
        # 无 `#frag`，全库 0 条），不记则只能靠补丁池兜；无片段的 `other.html`
        # md 已保形（R `_link` 按 `slug.target.md` 还原），**不入账**免双发。
        _bare_frag = re.fullmatch(r"[A-Za-z0-9._-]+\.html#.+", href)
        if not (href.startswith("../") or href.startswith("#") or _bare_frag):
            continue
        text = htmllib.unescape(re.sub("<[^>]*>", "", inner)).strip()
        if not text:
            continue
        prefix = htmllib.unescape(re.sub("<[^>]*>", "", s[:m.start()]))
        # 左邻上下文＝锚文前**最后两个词**（空白归一、小写）：按字符取上下文
        # 会被 H0／md 折行位置不同打乱（R 逐行匹配），词边界才是折行不变量；
        # 单字符太弱（`Section 2` 与 `See section 2` 同以 n 收尾，infinity 判例）。
        # 数学段整体抹掉：H0 是 `\(c\)`、md 是 `$C$`，两侧词形必然不同
        # （logic-nonmonotonic 判例：一条卡死会连锁饿死同页后续全部链接）。
        prefix = re.sub(r"\\\(.*?\\\)|\\\[.*?\\\]", "", prefix, flags=re.S)
        # HTML 注释残片不入可见文：H0 常有 `<!-- … 1958 -->` 夹在词间，md 无，
        # 账尾词写成 `1958 -->` 后短锚文恒不符（findlay `#bib-H`/`#bib-K` 判例）。
        prefix = re.sub(r"<!--.*?-->", " ", prefix, flags=re.S)
        # 可见脚注号 `[19]`（H0 是 `<sup>…[19]…</sup>`，md 侧成 `[^note-19]`）：
        # 两侧都剥，否则账尾词写成 `be.[19]` 而 md 侧只剩 `be.`，短锚文恒不符
        # 并连锁饿死（implicature `(1)` 判例）。
        prefix = re.sub(r"\[\d+\]", "", prefix)
        _words = re.sub(r"\s+", " ", prefix).strip().lower().split(" ")
        lead = " ".join(_words[-2:])
        out.append({"text": text, "href": href,
                    "nth": _count_word(prefix, text), "lead": lead})
    return out


def extract_bq(art_inner):
    """引块形态账：按**文档序**记每个 `<blockquote>` 是否裸装文字（首子非 `<p>`）。

    R 的 `_render_bq` 一贯发 `<blockquote><p>…</p></blockquote>`；H0 另有 6,120
    处裸装（798 页），套 `<p>` 后每处多 4 个段、整页 `_sub_diff` 对不齐
    （descriptions Δ109、desert Δ44 判例）。只记有裸装的页：0＝首子
    `<p>`/`<table>`（现行形态，含管道表路径），1＝裸装。切区与
    `extract_links` 同式（TOC／学术工具／相关条目各自的 `<blockquote>` 不算）。
    """
    s = art_inner
    s = _cut_region(s, '<div id="toc"', '</div>' + chr(92) + 's*(?=<div id="main-text">)')
    s = _cut_region(s, '<div id="academic-tools"', '</div>')
    s = _cut_region(s, '<div id="related-entries"', '</div>')
    s = re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), s, flags=re.S)
    out = []
    for m in re.finditer(r"<blockquote\b[^>]*>", s):
        after = s[m.end():m.end() + 60].lstrip()
        out.append(0 if after.startswith(("<p", "<table")) else 1)
    return out if any(out) else None


def extract_photo_pre_h1(art_inner):
    """头部图账：H0 首个 `<h1>` 之前有 `<img>` 记 1（照片题注段在标题前）。

    C 把 h1 提到 md 首行、题注段留在其后，R 按 md 序发则题注段错到标题后，
    整页段序错位（whitehead 判例；全库 26 页）。注释抹白后取首个 `<h1` 前缀。"""
    s = re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), art_inner, flags=re.S)
    m = re.search(r"<h1[\s>]", s)
    if m and "<img" in s[:m.start()]:
        return 1
    return None


def extract_italics(art_inner):
    """按件斜体标签形：H0 全用 <i> 时记 "i"（C 把 <em>/<i> 同归一为 *…*）。"""
    BS = chr(92)
    n_i = len(re.findall("<i[" + BS + "s>]", art_inner))
    n_em = len(re.findall("<em[" + BS + "s>]", art_inner))
    return "i" if n_i and not n_em else None


def extract_greek_form(art_inner):
    """按件希腊字形态：H0 用 <em>&alpha;</em> 而非宏时记 "em"。"""
    BS = chr(92)
    rng = "[" + chr(0x370) + "-" + chr(0x3ff) + "]"
    n_ent = len(re.findall("<em>" + BS + "s*&[A-Za-z]+;" + BS + "s*</em>", art_inner))
    n_uni = len(re.findall("<em>" + BS + "s*" + rng + BS + "s*</em>", art_inner))
    n_macro = len(re.findall("[(]" + BS + BS + "[A-Za-z]+[)]", art_inner))
    return "em" if (n_ent or n_uni) and not n_macro else None


def extract_note_forms(art_inner):
    """脚注引用形账：H0 全部 `notes.html#…` 引用按**文档序**记列表。

    同一 note 键可既有规范脚注又有散文原形（agent-modeling 判例），且 md
    的 `[^note-N]` 出现序＝H0 引用序（C 保序），故全量记账、R 侧游标逐个
    消费：规范形记 form=None（R 出默认 sup 形），非规范形记**完整替代片段**。

    片段可为锚自身（散文形：`note <a href="notes.html#supplement-4">4</a>`）
    或含外层 `<sup>[ … ]</sup>`（首尾方括号形）；`form` 里存哪一种，R 就原样
    发哪一种，不再二次包裹。

    片段名不必然等于显示号：`href="notes.html#complex" name="note-complex"`
    显示 `1`（binarium）、`#supplement-4` 显示 `4`（chance-randomness）——
    显示号不可从 md 推出，故整段记账。规范形判据：被 `<sup>[` … `]</sup>`
    包住、且锚文＝片段名去掉 `note-` 前缀后的文本。
    """
    out = []
    # 属性序不固定：`<a name="note-1" href="notes.html#1">`（logical-constants
    # 判例）——href 前可有任意属性
    for m in re.finditer(
            r'<a\b[^>]*href="notes\.html#([^"]+)"[^>]*>(.*?)</a>', art_inner,
            re.S):
        frag, inner = m.group(1), m.group(2)
        key = frag[len("note-"):] if frag.startswith("note-") else frag
        pre = art_inner[max(0, m.start() - 40):m.start()]
        post = art_inner[m.end():m.end() + 24]
        # 方括号与 sup 之间可有空白（bell-theorem 判例：`]\n </sup>`）
        sup_m = re.search(r"<sup>\s*(\[)?$", pre)
        close_m = re.match(r"(\])?\s*</sup>", post)
        if sup_m and close_m:
            # 规范形：`<sup>[` … `]</sup>` 且显示号＝键 → form=None（R 出默认形）
            if (sup_m.group(1) == "[" and close_m.group(1) == "]"
                    and inner.strip() == key):
                out.append({"n": key, "form": None})
            else:
                # 非规范包裹整段原样记账——含上游畸形（pain `<sup>[<a…>10</a></sup>`
                # 缺右括号、jaspers `<sup><a…>1</a>]</sup>` 缺左括号），R 逐字节复刻
                f0 = max(0, m.start() - 40) + sup_m.start()
                f1 = m.end() + close_m.end()
                out.append({"n": key, "form": art_inner[f0:f1]})
        else:
            out.append({"n": key, "form": m.group(0)})
    return out


def extract_sup_pos(art_inner):
    """上下标「同页双源」按位账：cp → ["ent"|"tag", …]（文档序，仅双源字符）。

    kant-science／proclus 判例：同一页 `&sup2;` 与 `<sup>2</sup>` 并存，C 两者
    都转成 `²`，md 同形双源；`entities` 账只能给统一形态（第三十三批让 R 一律
    留实体），于是原位是标签形的那些也被发成 `&sup2;`。此账按文档序记每次
    出现的原位形态，R 按出现序消费。只记同时具备两形的字符（纯单源页不受
    影响，走原统一策略）。"""
    sup_rev = {v: k for k, v in SUP_MAP.items()}
    sub_rev = {v: k for k, v in SUB_MAP.items()}
    seq = []
    for m in re.finditer(r"&sup([A-Za-z0-9]+);|&sub([A-Za-z0-9]+);",
                         art_inner):
        base = m.group(1) or m.group(2)
        cp = (SUP_MAP if m.group(1) else SUB_MAP).get(base)
        if cp:
            seq.append((cp, "ent", m.start()))
    # 标签形内文恒单字符（C 的 _subsup_md 只在整段可映射时产字形）
    for m in re.finditer(r"<sup>\s*([^<>]{1,3}?)\s*</sup>|<sub>\s*([^<>]{1,3}?)\s*</sub>",
                         art_inner):
        base = (m.group(1) or m.group(2)).strip()
        cp = (SUP_MAP if m.group(1) else SUB_MAP).get(base)
        if cp:
            seq.append((cp, "tag", m.start()))
    seq.sort(key=lambda x: x[2])
    out = {}
    for cp, form, _pos in seq:
        out.setdefault(cp, []).append(form)
    return {cp: f for cp, f in out.items() if "ent" in f and "tag" in f}


def extract_toc(art_inner):
    """TOC 块逐字（导航区：题与锚皆由正文派生，另设一致性核对）。"""
    m = re.search(r'<div id="toc".*?(?=<div id="main-text">)', art_inner, re.S)
    return m.group(0) if m else None


MD_DEF_RE = re.compile(r"^\[\^([^\]\s]+)\]:(.*)$", re.M)
SUP_MAP = getattr(__import__("yuanwen"), "SUP_MAP", {})
SUB_MAP = getattr(__import__("yuanwen"), "SUB_MAP", {})


def norm_md(s):
    """md 定义行 → 可见文（去链接包裹/星号/上下标字形/反斜杠转义）。

    URL 可含一级圆括号（`ERInt.2013(1(2)).pdf` 实证，al-farabi-logic 文献
    条目匹配失败判例），故 URL 组允许括号对。

    转义还原（2026-11-22，heidegger 判例）：C 自第六/九批起对字面 `*`／`$`／
    `\\`／行首 `N.`／`#` 逐字转义，md 侧 `1\\.` 与 H0 `1.`、`(\\*)` 与 `(*)`
    本应等值；旧实现只去星不去反斜杠，含转义的条目在可见文等值上全部失配
    （书目 dl 配对失败回落散文 → 整块结构差）。`\\*` 须先占位再移除强调星，
    否则字面星被当强调星删掉（dilthey `(*)` 判例）。"""
    t = s.replace("\\*", "\x01")
    t = re.sub(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]"
               r"\(((?:[^()\s]|\([^()]*\))*)\)", r"\1", t)
    t = re.sub(r"\[\^note-([^\]\s]+)\]", r"[\1]", t)  # 注引用是可见文字：
    #   H0 `<sup>[<a…>4</a>]</sup>` 可见为 `[4]`，md `[^note-4]` 须同形
    #   （meinong 判例：书目散文含注引用，两侧失配致 pd 定位全错）
    t = re.sub(r"\[\^[^\]\s]+\]", "", t)   # 其余脚注引用标记不是可见文字（clauberg 判例：
    #   书目散文带 `[^verbeek-1999a]` 标记，与 H0 段可见文失配致 pd 定位失败）
    t = t.replace("*", "")
    t = t.replace("\x01", "*")
    t = re.sub(r"\\(.)", r"\1", t)
    rev = {v: k for k, v in list(SUP_MAP.items()) + list(SUB_MAP.items())}
    if rev:
        cls = "".join(__import__("re").escape(c) for c in rev)

        def rep(m):
            return "".join(rev[c] for c in m.group(0))

        t = re.sub("[%s]+" % cls, rep, t)
    return re.sub(r"\s+", " ", htmllib.unescape(t)).strip()


def norm_html(s):
    """H0 li → 可见文（剥标签）。"""
    return re.sub(r"\s+", " ", htmllib.unescape(
        re.sub(r"<[^>]*>", "", s))).strip()


BI_START = re.compile(r"<h([2-6])[^>]*>|<ul[^>]*>|<ol[^>]*>|<table[^>]*>"
                      r"|<dl[^>]*>|<blockquote[^>]*>|<p>", re.S)


def _match_close(region, start, open_pat, close_pat):
    """从 start 起按深度扫描，返回 [(内容起, 内容止, 标签止)] 的顶层块。"""
    depth = 1
    j = None
    for t in re.finditer(open_pat + "|" + close_pat, region):
        if t.start() < start:
            continue
        depth += 1 if re.match(open_pat, t.group(0)) else -1
        if depth == 0:
            j = t
            break
    return j


def split_items(inner):
    """顶层 <li> 内容表（支持条目内嵌套列表与 H0 缺闭合 li）。

    只返回顶层项：嵌套子 li 留在父项 inner 里，由 _tree_nodes 递归拆解。
    旧实现用裸 finditer 会把嵌套 li 当兄弟一并发射，父项重建后子项双计
    （abelard subhang：账 37 节点 vs 真 25＋4，h3 与条目错位）。

    H0 允许省 `</li>`（anarchism 判例：`<li>Goldman…Penguin.\n\n<li>Graeber…`
    ——配平会把 Graeber 起后 57 条吞进 Goldman 一项）：配平闭合落到下一
    兄弟之后、且两者之间无未闭合 `<ul>` 时，按兄弟边界截断。"""
    out = []
    opens = [(m.start(), m.end(), m.group(1))
             for m in re.finditer(r"<li([^>]*)>", inner)]
    pos = 0
    for idx, (s, e, attrs) in enumerate(opens):
        if s < pos:
            continue
        nxt = opens[idx + 1][0] if idx + 1 < len(opens) else len(inner)
        t = _match_close(inner, e, r"<li[^>]*>", r"</li>")
        end = t.start() if t else nxt
        if end > nxt:
            gap = inner[e:nxt]
            if gap.count("<ul") <= gap.count("</ul>"):
                end = nxt
        out.append((attrs, inner[e:end]))
        pos = (t.end() if (t and end == t.start()) else end)
    return out


def scan_bib(region):
    """文献区按文档序解析 → [("h", level, inner) | ("ul", [(attrs, inner)])
    | ("dl", attrs, [(dt_attrs, dt_inner, dd_attrs, dd_inner)]) | ("p", inner)
    | ("bq", inner)]"""
    out = []
    i = 0
    while i < len(region):
        m = BI_START.search(region, i)
        if not m:
            # 区尾裸排文字（philosophy-religion 判例：末条 ul 后悬一段
            # `Zagzebski, Linda, 2022, …` 散文，无后续标签可寻）——同样
            # 自成 p 块，文字仍只从 md 取
            if region[i:].strip():
                out.append(("p", region[i:]))
            break
        if m.start() > i and region[i:m.start()].strip():
            # 块间裸排文字自成 p 块（locke 判例：`</p> The Clarendon Edition
            # … Press:` 悬在 `</p>` 与 `<ul>` 之间，BI_START 不收裸文字——
            # 旧实现整段丢、md 对应散文段永不匹配）。文字仍只从 md 取：
            # 裸文 norm 后与 md 散文段精确等值，seq 走常规 'p' 步。
            out.append(("p", region[i:m.start()]))
        if m.group(1) is not None:
            close = "</h%s>" % m.group(1)
            e = region.find(close, m.end())
            out.append(("h", int(m.group(1)), region[m.end():e]))
            i = e + len(close)
        elif m.group(0).startswith("<ul") or m.group(0).startswith("<ol"):
            tag = "ol" if m.group(0).startswith("<ol") else "ul"
            t = _match_close(region, m.end(), r"<" + tag + r"[^>]*>",
                             r"</" + tag + ">")
            if not t:
                break
            out.append((tag, split_items(region[m.end():t.start()])))
            i = t.end()
        elif m.group(0).startswith("<table"):
            # 文献区表格（两列缩写＋条目，abu-bakr-al-razi 判例：H0 用
            # `<td id="bib-RF">[RF]</td>` 表格而非 li）
            t = _match_close(region, m.end(), r"<table[^>]*>", r"</table>")
            if not t:
                break
            out.append(("table", region[m.start():t.end()]))
            i = t.end()
        elif m.group(0).startswith("<dl"):
            # 文献区定义表（缩写键块 `<dt>[AOP]</dt><dd>&ldquo;…&rdquo;</dd>`、
            # 著作表 `<dt>[GA 2]</dt><dd>…</dd>`）：C 侧折成散文段，文字在 md，
            # 结构（dl/dt/dd 属性）只此一侧有（alain-locke 判例：23 件）
            t = _match_close(region, m.end(), r"<dl[^>]*>", r"</dl>")
            if not t:
                break
            inner = region[m.end():t.start()]
            pairs = [(pm.group(1), pm.group(2), pm.group(3), pm.group(4))
                     for pm in re.finditer(
                         r"<dt([^>]*)>(.*?)</dt>\s*<dd([^>]*)>(.*?)</dd>",
                         inner, re.S)]
            out.append(("dl", m.group(0)[len("<dl"):-len(">")], pairs))
            i = t.end()
        elif m.group(0).startswith("<blockquote"):
            # 文献区引块（berkeley 的 `[W]` 版本条目以 <blockquote> 排）：旧
            # BI_START 不含 blockquote，整块漏扫→装配时被丢（22 件有此类块）
            t = _match_close(region, m.end(), r"<blockquote[^>]*>",
                             r"</blockquote>")
            if not t:
                break
            out.append(("bq", region[m.start():t.end()]))
            i = t.end()
        else:
            e = region.find("</p>", m.end())
            out.append(("p", region[m.end():e]))
            i = e + 4
    return out


def _match_def(vis, defs_plain, used):
    """可见文 → md 定义序索引：先精确等值，再前缀回退（末尾格式差异，
    如省略号/&nbsp;/标点；abelard 8 条文献因此定位失败致渲染重复）。"""
    idx = next((i for i, t in enumerate(defs_plain)
                if i not in used and t == vis), None)
    if idx is not None:
        return idx
    k = 40
    if len(vis) >= k:
        idx = next((i for i, t in enumerate(defs_plain)
                    if i not in used and len(t) >= k and t[:k] == vis[:k]),
                   None)
    return idx


def _tree_nodes(inner, md_plain, used):
    """ul 内层 → [{i, u, c}] 节点表（i＝md 定义序，u＝子 ul 属性，c＝子节点）。

    父项匹配用“剥净嵌套 ul 后的本层文字”——否则子项文字混入父项可见文。"""
    nodes = []
    for attrs, sub in split_items(inner):
        kids = []
        rest = ""
        pos = 0
        for m in re.finditer("<ul([^>]*)>", sub):
            if m.start() < pos:
                # 已被上一层 ul 的平衡跨度吞掉的内层 ul 不再计一次：三层嵌套
                # （li→ul→ul）时旧实现把同一子表登记两遍、子节点双计，多出
                # 的节点匹配不到 md 定义，渲染按「下一个未用索引」兜底→整条
                # ul 的条目级联错位一位（habermas 判例：Works 节尾部混进
                # Aboulafia、Secondary 节首条变 Adorno）
                continue
            t = _match_close(sub, m.end(), "<ul[^>]*>", "</ul>")
            if not t:
                continue
            kids.append((m.group(1), sub[m.end():t.start()]))
            rest += sub[pos:m.start()]
            pos = t.end()
        rest += sub[pos:]
        vis = norm_html(rest)
        idx = _match_def(vis, md_plain, used)
        if idx is None and not kids:
            # 全文前缀回退只给无子表的条目：H0 双层 ul 的空壳包装 li 自身
            # 无文字、sub 全文以首条目开头，前缀回退会让包装冒领首条定义
            # （confucian-gender 判例：包装领走 def 0，真条目全部错位一位）
            idx = _match_def(norm_html(sub), md_plain, used)
        if idx is not None:
            used.add(idx)
        node = {"i": idx}
        if vis:
            # 本层自带文字（父条目的引子行）：渲染侧 i 缺失时须兜底占位，
            # 否则文字整条丢失（pomponazzi 判例：`Aristotle,` 父条 + 子表）
            node["t"] = 1
        for attrs2, inner2 in kids:
            node.setdefault("u", (attrs2 or "").strip())
            node.setdefault("c", []).extend(_tree_nodes(inner2, md_plain, used))
        nodes.append(node)
    return nodes


def extract_bib_tree(art_inner, md_defs):
    """文献区嵌套结构账：每 ul 的节点树（纯整数＋ul 属性）。"""
    bib = _bib_region(art_inner)
    if bib is None:
        return None
    md_plain = [norm_md(t) for t in md_defs]
    used = set()
    uls = []
    for blk in scan_bib(bib):
        if blk[0] != "ul":
            continue
        inner = "<li>".join("")  # 占位，不会用到
        # 从扫描块重建原始 inner：把 (attrs, inner) 拼回
        raw = "".join("<li%s>%s</li>" % (a or "", b) for a, b in blk[1])
        uls.append({"nodes": _tree_nodes(raw, md_plain, used)})
    return uls or None


def extract_bib_indices(art_inner, md_defs):
    """文献条目在 md 定义序中的位置账（分节序，纯整数）＋ li id 属性表。

    条目匹配用可见文等值（norm_md ↔ norm_html）；li 的 id 只记属性、不记散文。"""
    bib = _bib_region(art_inner)
    if bib is None:
        return None
    plain = [norm_md(t) for t in md_defs]
    used, ids = set(), {}
    sections, cur = [], None
    for blk in scan_bib(bib):
        if blk[0] == "h":
            if cur is not None:
                sections.append(cur)
            cur = []
            continue
        if blk[0] not in ("ul", "ol"):
            continue
        if cur is None:
            cur = []
        for attrs, inner in blk[1]:
            vis = norm_html(inner)
            idx = _match_def(vis, plain, used)
            cur.append(idx)
            if idx is not None:
                used.add(idx)
                m = re.search('id="([^"]*)"', attrs or "")
                if m:
                    ids[idx] = m.group(1)
    if cur is not None:
        sections.append(cur)
    return sections, ids



def _bib_region(art_inner):
    """bibliography div 的内容区间（收口形态不齐：adorno 等件结尾无
    `</div> ` 尾随空格——用括号配平定位，支持嵌套 div）。

    div 闭后到下一个 `<div ` 之间的条目块一并收入（rights-group 判例：
    H0 的书目 div 在 h2 后即闭、全部条目 ul 悬在 div 外；BI_START 扫描
    不看 div 边界，不收则整单条目层丢失）。"""
    m0 = re.search(r'<div id="bibliography">', art_inner)
    if not m0:
        return None
    t0 = _match_close(art_inner, m0.end(), r"<div[^>]*>", r"</div>")
    if not t0:
        return None
    inner = art_inner[m0.end():t0.start()]
    pos = t0.end()
    while True:
        # div 闭后到下一个 `<div ` 之间的条目块一并收入（rights-group 判例：
        # H0 的书目 div 在 h2 后即闭、全部条目 ul 悬在 div 外）；兄弟书目
        # div（id 以 biblio 起）也并入（spacetime-singularities 判例：作者把
        # 书目拆成 biblio-phil/phys/-ref 四个兄弟 div）
        nxt = re.search(r"<div[\s>]", art_inner[pos:])
        seg_end = pos + (nxt.start() if nxt else len(art_inner) - pos)
        tail = art_inner[pos:seg_end]
        if BI_START.search(tail):
            inner += tail
        ndiv = (re.match(r'<div id="biblio[^"]*">', art_inner[seg_end:])
                if nxt else None)
        if ndiv:
            t1 = _match_close(art_inner, seg_end + ndiv.end(),
                              r"<div[^>]*>", r"</div>")
            if t1:
                inner += art_inner[seg_end:t1.end()]
                pos = t1.end()
                continue
        break
    # H0 书目区常见整条注释掉的条目（`<!--<li>Humane Society…n.d.…</li>-->`）：
    # C 侧注释被丢弃，账侧必须同等丢弃，否则账里多出一个 md 无对应的条目，
    # 分组条目数与 H0 不等（chimeras 判例：组 2 少 1 件、首条错位）
    return re.sub(r"<!--.*?-->", "", inner, flags=re.S)


def extract_bib_seq(art_inner, md, tails=None):
    """文献区块序账：[[kind, idx], …]，kind ∈ h/p/pd/ul/table/dl。

    dl 另出配对账（纯整数 + 标签属性；文字仍只从 md 取）：dls[k] 记
    {"attrs": <dl 开标签属性>, "pairs": [[dt_pidx, dd_pidx, dt_attrs,
    dd_attrs], …]}，pidx 为 md 散文段序（与 R 侧 ps 同序）。"""
    if not md:
        return None
    # bibliography 的收口形态不齐（adorno 等件结尾无 `</div> ` 尾随空格），
    # 用括号配平定位（_match_close 支持嵌套 div）
    bib_region = _bib_region(art_inner)
    if bib_region is None:
        return None
    NL = chr(10)
    reg = re.search("^## References[^" + NL + "]*" + NL + "(.*?)(?=^## |\\Z)",
                    md, re.S | re.M)
    if not reg:
        return None
    # 题后散字里可能夹链接（boethius-dacia：`Editions</h3> See <a>section 2</a>, above.`），
    # 与 md 散文段比对须剥标签解实体（norm_html 与下方 vis 同式），否则跳不掉
    # p 步、题后散字发两遍
    tail_set = {norm_html(t) for t in (tails or []) if t}
    md_heads, md_prose = [], []
    for ln in reg.group(1).split(NL):
        s2 = ln.strip()
        if not s2 or s2.startswith(">") or MD_DEF_RE.match(ln):
            continue
        if s2.startswith("|"):
            # 表格行归 table 块（R 侧发 <table>，不是 <p>）——散文序必须与
            # R 侧 ps 块序一致，含表格行的文件旧索引会错位（anselm 判例：
            # `["p", 6]` 越界被静默跳过，整段散文在装配页消失）
            continue
        if re.match(r"[-*+]\s+", s2) or re.match(r"\d+[.]\s+", s2):
            # md 列表行同理不入散文（logic-propositional 判例：C 的 md 在
            # References 区保留可见列表形，`- Schechter…` 混进 md_prose 使
            # p 步索引整体错位、段落在装配页互换）
            continue
        m = re.match(r"^(#{3,6})\s+(.*)$", s2)
        if m:
            md_heads.append(norm_md(m.group(2)))
            continue
        md_prose.append(norm_md(s2))
    defs = [m.group(2).strip() for m in MD_DEF_RE.finditer(md)
            if not _is_note_key(m.group(1))]
    defs_plain = [norm_md(t) for t in defs]
    used, seq = set(), []
    dls = []
    n_bq = 0
    hi = pi = 0
    for blk in scan_bib(bib_region):
        if blk[0] == "h":
            vis = norm_html(blk[2])
            idx = next((i for i in range(hi, len(md_heads))
                        if md_heads[i] == vis), None)
            if idx is not None:
                hi = idx + 1
            seq.append(["h", idx])
        elif blk[0] in ("ul", "ol"):
            ids = []
            for attrs, inner in blk[1]:
                vis = norm_html(inner)
                idx = _match_def(vis, defs_plain, used)
                ids.append(idx)
                if idx is not None:
                    used.add(idx)
            seq.append([blk[0], ids])
        elif blk[0] == "table":
            # 表格块按原样发（R 侧 md 表格已渲染 HTML；位形差由标记层补丁吸收）
            seq.append(["table", None])
        elif blk[0] == "bq":
            # 引块记文档序位次（文本取自 md 的 `>` 块，R 侧按位次取 body 内
            # 的 blockquote 块原样发；位次不匹配时 R 侧跳过不硬发）
            seq.append(["bq", n_bq])
            n_bq += 1
        elif blk[0] == "dl":
            # dt/dd 逐对定位 md 散文段（文字只从 md 取；属性只记结构）
            rec = {"attrs": blk[1], "pairs": []}
            pi0, ok = pi, True
            for dt_attrs, dt_in, dd_attrs, dd_in in blk[2]:
                # 空 dt/dd（`<dt> </dt>` 无 md 段，contract-law 判例）不入配对
                dti = None
                if norm_html(dt_in):
                    dti = next((i for i in range(pi, len(md_prose))
                                if md_prose[i] == norm_html(dt_in)), None)
                    if dti is None:
                        ok = False
                        break
                    pi = dti + 1
                ddi = None
                if norm_html(dd_in):
                    ddi = next((i for i in range(pi, len(md_prose))
                                if md_prose[i] == norm_html(dd_in)), None)
                    if ddi is None:
                        ok = False
                        break
                    pi = ddi + 1
                rec["pairs"].append([dti, ddi, dt_attrs, dd_attrs])
            if ok and rec["pairs"]:
                dls.append(rec)
                seq.append(["dl", len(dls) - 1])
            else:
                # 配对失败回落散文序：文字不丢，dl 位形交补集池（A5）
                pi = pi0
                for dt_in, dd_in in [(p[1], p[3]) for p in blk[2]]:
                    for txt in (dt_in, dd_in):
                        vis = norm_html(txt)
                        k = next((i for i in range(pi, len(md_prose))
                                  if md_prose[i] == vis), None)
                        if k is None:
                            continue
                        pi = k + 1
                        seq.append(["p", k])
        else:
            vis = norm_html(blk[1])
            if vis in tail_set:
                # 题后散字（bib_heads 第 4 位已记、由标题步原样发出）：
                # 不再单独发 p，否则重复（boethius-dacia 判例）
                continue
            idx = next((i for i in range(pi, len(md_prose))
                        if md_prose[i] == vis), None)
            if idx is not None:
                pi = idx + 1
                seq.append(["p", idx])
                continue
            di = next((i for i, t in enumerate(defs_plain)
                       if i not in used and t == vis), None)
            if di is not None:
                used.add(di)
            seq.append(["pd", di])
    return seq, dls


TABLE_TAG_RE = re.compile(r"<table\b[^>]*>|</table\s*>", re.I)


def table_spans(s):
    """顶层 `<table>` 块区间 [(起, 止)]（深度配平，含嵌套表只算顶层）。

    扫前先把 HTML 注释**抹白**（等长空格，偏移不变）：SEP 的
    `<!--pdf include <table …> pdf include-->` 注释里含 `<table` 而无
    `</table>`，会把配平栈永久压高、把后续同级表误判成嵌套
    （paradox-simpson：7 表被读成顶层 2）。
    """
    view = re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), s, flags=re.S)
    spans, stack = [], []
    for m in TABLE_TAG_RE.finditer(view):
        if m.group(0).startswith("</"):
            if stack:
                st = stack.pop()
                if not stack:
                    spans.append((st, m.end()))
        else:
            stack.append(m.start())
    for st in stack:  # 未闭合：保守延到串尾
        spans.append((st, len(s)))
    return sorted(spans)


def stash_nested(inner):
    """本层内的嵌套表 → 占位（返回 (文本, [内层原文…])，序为文档序）。"""
    spans = table_spans(inner)
    store = [inner[st:en] for st, en in spans]
    out = inner
    for k in range(len(spans) - 1, -1, -1):
        st, en = spans[k]
        out = out[:st] + "\x06T%d\x06" % k + out[en:]
    return out, store


def extract_tables(art_inner):
    """表格结构账：**顶层**表（深度配平，文档序）的开标签属性、thead/tbody、逐行逐格位形。

    格位记 [kind, colspan]（kind ∈ h/d/x）——H0 常用 `<td colspan="2">`
    跨列（aristotle-logic 判例），md pipe 表格按**逻辑列**展开，不记
    colspan 会让整表错位一格。文字不入账。

    嵌套表（`<td>` 内含 `<table>`，altruism-empirical／benjamin 等 17 件）：
    本层解析先把内层整表换占位，否则非贪婪 `</t[dh]>` 在首个内层收口处截断
    （旧式把外层记成乱序 `[d1,d2]` 残形）。账**只记顶层表**：内层表在 md 里
    就是 C 存下的 H0 原文，渲染侧原样发出、布局差由补丁池吸收；若账也记内层，
    渲染侧序号会与账错位。代价：C 把嵌套**压平**成同级管道表的件
    （paradox-simpson：H0 顶层 2、装配侧 5）账表数不齐，登记为 C 侧结构缺陷。

    仅 `&nbsp;` 的格记**空位** 'x'：C 落 md 后是空白，而 R 的 `pool` 只收
    非空单元格——两口径必须一致，否则整表回退、页面留缺口。
    """
    out = []
    for st, en in table_spans(art_inner):
        block = art_inner[st:en]
        m = re.match(r"<table([^>]*)>", block, re.I)
        if not m:
            continue
        open_tag = m.group(1)
        inner, _ = stash_nested(block[m.end():])
        inner = re.sub(r"</table\s*>\s*$", "", inner, flags=re.I)
        thead = "<thead>" in inner
        tbody = "<tbody>" in inner
        rows = []
        for r in re.finditer(r"<tr[^>]*>(.*?)</tr>", inner, re.S):
            cells = []
            for c in re.finditer("<t([hd])([^>]*)>(.*?)</t[hd]>",
                                 r.group(1), re.S):
                sm = re.search(r'colspan="(\d+)"', c.group(2))
                span = int(sm.group(1)) if sm else 1
                body = re.sub(r"&nbsp;|&#160;|&#xa0;", "", c.group(3))
                kind = "x" if not body.strip() else c.group(1)
                cells.append([kind, span])
            rows.append(cells)
        th_rows = 0
        tm = re.search("<thead>(.*?)</thead>", inner, re.S)
        if tm:
            th_rows = len(re.findall("<tr", tm.group(1)))
        out.append({"attrs": open_tag, "thead": thead, "tbody": tbody,
                    "thead_rows": th_rows, "rows": rows})
    return out


def extract_greek(art_inner, md=None):
    """按件希腊字序账：H0 文档序的**逐次出现形态**（宏名或 "em"）。

    同形不同名（phi/varphi 等）按出现序记宏名；H0 以 `<em>&phi;</em>`／
    `<em>φ</em>` 排的斜体字形记 "em"（C 落 md 成 `*φ*`，R 侧须还原为
    em 形而非宏）。单一名且从未出 em 形的字形不入账（默认规则已覆盖）。"""
    GREEK_UNI = getattr(__import__("yuanwen"), "GREEK_UNI", {})
    rev = {}
    for k, v in GREEK_UNI.items():
        rev.setdefault(v, []).append(k)
    name2cp = {}
    for cp, names in rev.items():
        for nm in names:
            name2cp[nm] = cp
    rng = "[" + chr(0x370) + "-" + chr(0x3ff) + "]"
    # 宏名按“反斜杠＋字母”取（与 C 侧命令识别一致）：不能要求紧跟 `\)`——
    # 数学体里 `\varepsilon` 可出现在 `\stackrel{,}{…}` 等复合写法中间，
    # 卡定界符会漏位、序列整体错位（logic-temporal/chance-randomness 判例：
    # ε 取了 epsilon 而 H0 是 varepsilon）
    pat = re.compile(r"\\([A-Za-z]+)"
                     r"|<(em|i)>\s*(?:&([A-Za-z]+);|(" + rng + r"))\s*</\2>")
    seq = {}
    for m in pat.finditer(art_inner):
        if m.group(1):
            cp = name2cp.get(m.group(1))
            if cp:
                seq.setdefault(cp, []).append(m.group(1))
            continue
        cp = name2cp.get(m.group(3)) if m.group(3) else m.group(4)
        if cp is None:
            continue
        seq.setdefault(cp, []).append("em")
    out = {}
    for cp, names in seq.items():
        canon = (rev.get(cp) or [None])[0]
        if len(rev.get(cp, [])) > 1 or names[0] != canon or "em" in names:
            out[cp] = names
    return out


# 锚提取：抹掉数学段/行内代码/标签/实体后取可见词——两侧（H0 与 md）同式调用，
# 键可逐字比较。数学段两侧写法不同（H0 `\(…\)`、md `$…$`），整段抹掉后
# 剩下的都只是散文词，故能对上。
ANCHOR_DROP = re.compile(
    r"\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$"
    r"|\$[^$\n]*\$|`[^`\n]*`|\[\^[^\]]*\]"
    r"|<[^>]*>|&[A-Za-z#0-9]+;")


def ital_anchor(text, pos, words=5):
    """`pos` 之前最近 5 个词（去数学/代码/标签/实体）——斜体字形的定位锚。

    斜体希腊位次不能靠“全文档第 k 次出现”定位：md 侧有正文层多出的段
    （H0 无对应、装配层会丢），出现数一多就整体错位（recursive-functions
    判例：md 339 对 H0 336，4 处 φ/varphi 互换）。锚词是散文，两侧一致。"""
    pre = ANCHOR_DROP.sub(" ", text[max(0, pos - 220):pos])
    return " ".join(re.findall(r"[A-Za-z]{2,}", pre)[-words:])


ITAL_STAR_RE = re.compile(r"(?<![*\w])\*\s*([A-Za-z\u0370-\u03ff])\s*\*(?!\*)")


def _mask_md(md):
    """围栏/行内代码/数学段抹成等长空白（位置不变），只用于找斜体字形。"""
    out = list(md)
    n = len(md)

    def blank(a, b):
        for k in range(a, min(b, n)):
            if out[k] != "\n":
                out[k] = " "

    i = 0
    while i < n:
        if md.startswith("```", i):
            j = md.find("```", i + 3)
            j = n if j < 0 else j + 3
            blank(i, j)
            i = j
            continue
        c = md[i]
        if c == "`":
            j = md.find("`", i + 1)
            if j > 0 and "\n" not in md[i:j]:
                blank(i, j + 1)
                i = j + 1
                continue
        if c == "$":
            if md.startswith("$$", i):
                j = md.find("$$", i + 2)
                if j > 0:
                    blank(i, j + 2)
                    i = j + 2
                    continue
            else:
                j = md.find("$", i + 1)
                if j > 0 and "\n" not in md[i:j]:
                    blank(i, j + 1)
                    i = j + 1
                    continue
        i += 1
    return "".join(out)


def extract_greek_ital(art_inner, md, greek):
    """md 侧 `*φ*` 斜体字形的逐次宏名账：{码位: [宏名或 None, …]}（md 序）。

    名字取自 H0 中**锚词相同**的那次出现（H0 侧同名同锚），与数学段出现数
    脱钩——正文层多余段（md_extra）不再让后续位次整体漂移。None 表示该次
    没有可靠锚，R 侧退回旧口径（分字形序）。"""
    if not md or not greek:
        return None
    uni = getattr(__import__("yuanwen"), "GREEK_UNI", {})
    # 先定 md 侧需要定名的斜体（只有账内字形才要），再按需扫 H0——全扫会为
    # 每件数千次希腊出现算锚，账重生成明显变慢
    stars = []
    for m in ITAL_STAR_RE.finditer(_mask_md(md)):
        glyph = m.group(1)
        cp = uni.get(glyph) or glyph
        if cp in greek:
            stars.append((m.start(), cp))
    if not stars:
        return None
    need = {cp for _, cp in stars}
    name2cp = dict(uni)
    rng = "[" + chr(0x370) + "-" + chr(0x3ff) + "]"
    pat = re.compile(r"\\([A-Za-z]+)"
                     r"|<(em|i)>\s*(?:&([A-Za-z]+);|(" + rng + r"))\s*</\2>")
    occ = {}
    for m in pat.finditer(art_inner):
        if m.group(1):
            cp = name2cp.get(m.group(1))
            if not cp:
                continue
            nm = m.group(1)
        else:
            cp = name2cp.get(m.group(3)) if m.group(3) else m.group(4)
            if cp is None:
                continue
            nm = "em"
        if cp not in need:
            continue
        occ.setdefault(cp, []).append(
            [nm, ital_anchor(art_inner, m.start())])
    out = {}
    used = {}
    for pos, cp in stars:
        lst = out.setdefault(cp, [])
        cands = occ.get(cp) or []
        taken = used.setdefault(cp, set())
        key = ital_anchor(md, pos)
        picked = None
        if key:
            # 同名锚可能重复（同段两次 `*φ*`）：取**最小未用**位次，天然保序；
            # 不能用“游标只进不退”——md 侧正文层段序与 H0 有出入时游标会
            # 越过尚未对上的位次（recursive-functions 判例：后两处漏配）
            for idx, o in enumerate(cands):
                if idx not in taken and o[1] == key:
                    picked = o[0]
                    taken.add(idx)
                    break
        lst.append(picked)
    out = {k: v for k, v in out.items() if v}
    return out or None


def extract(art_inner, md=None):
    led = {}
    heads = []
    for m in HEAD_RE.finditer(art_inner):
        txt = re.sub(r"<[^>]*>", "", m.group(3)).strip()
        heads.append({"level": int(m.group(1)), "text": htmllib.unescape(txt),
                      "id": hid_form(m.group(2), m.group(3))})
    led["hids"] = heads
    # 文献分节账：标题级别＋该节条目数（文献区题可为 h3/h4，条目与题交错）
    # 文献区一律用括号配平取全区间（旧式 `(.*?)\n</div> ` 正则遇嵌套 div
    # 会在第一个内层收口处早断——aristotle-ethics 的 bib_heads 只剩 3 项，
    # 区标题因而不认“Bibliography”；adorno 等件又无 `\n</div> ` 尾随空格）
    region = _bib_region(art_inner)
    if region is not None:
        # H0 文献区标题文字（md 侧标题带中文加工后缀，如
        # `## References（引用注释）`；全库 1,878 件统一形态）。渲染按账取
        # H0 规范形，否则装配标题与 H0 文字不等（aesthetic-judgment 判例）
        # 第 4 位＝题后散字（`</h3> Works by Hobbes`、`</h3> Note: …`、
        # `See section 2, above.` 判例）：H0 在标题与首个块之间夹一行散文，
        # md 侧被丢（h0_extra 族）。按原文片段逐字入账，渲染侧原样接在题后；
        # 若该文字已紧随 md 同名标题出现（C 已转出）则不记，防重复。
        def _flat(s):
            return re.sub(r"\s+", "", htmllib.unescape(re.sub(r"<[^>]*>", "", s)))

        _bib_heads = []
        _block = re.compile(r"</?(?:ul|ol|li|p|table|div|h[2-6]|dl|blockquote)\b|<!--",
                            re.I)
        for m in re.finditer(r'<h([2-6])([^>]*)>(.*?)</h\1>', region, re.S):
            _nx = _block.search(region, m.end())
            tail = region[m.end():_nx.start() if _nx else len(region)]
            rec = [int(m.group(1)), norm_html(m.group(3)),
                   (re.search(r'id="([^"]*)"', m.group(2) or "") or [None, None])[1]]
            flat = _flat(tail)
            if flat:
                # 无 md 侧去重守卫：文献区的**裸文字**（不包 <p>）C 一律丢，
                # 而 R 的 `seq` 只为 `<p>` 块发散文——即便 md 里有这段文字
                # 也没有发射点（boethius-dacia `See section 2, above.` 判例，
                # md 第 235 行有、装配页缺席）。故只要题后有裸文字即入账。
                rec.append(tail)
            _bib_heads.append(rec)
        led["bib_heads"] = _bib_heads
        secs, pend, n = [], None, 0
        for m in re.finditer(r'<h([2-6])[^>]*>(.*?)</h\1>|<ul[^>]*>(.*?)</ul>',
                             region, re.S):
            if m.group(1) is not None:
                if pend is not None:
                    secs.append([pend, n])
                pend, n = int(m.group(1)), 0
            else:
                n += len(re.findall(r"<li>", m.group(3)))
        if pend is not None:
            secs.append([pend, n])
        led["bib_sections"] = secs
        led["bib_groups"] = [x[1] for x in secs]
        if md:
            _tails_bib = [h[3] for h in (led.get("bib_heads") or [])
                          if len(h) > 3]
            defs = [m.group(2).strip() for m in MD_DEF_RE.finditer(md)
                    if not _is_note_key(m.group(1))]
            got = extract_bib_indices(art_inner, defs)
            if got:
                idx, ids = got
                if idx is not None:
                    led["bib_indices"] = idx
                if ids:
                    led["bib_ids"] = {str(k): v for k, v in ids.items()}
            seq, dls = extract_bib_seq(art_inner, md, _tails_bib)
            if seq is not None:
                led["bib_seq"] = seq
            if dls:
                led["bib_dl"] = dls
            tree = extract_bib_tree(art_inner, defs)
            if tree:
                led["bib_tree"] = tree
    # 相关条目
    rel = re.search(r'<div id="related-entries">.*?<p>(.*?)</p>', art_inner, re.S)
    if rel:
        items = []
        # 每项前是否有 `|`：按竖线切段后，段首项带 sep（首段除外）；
        # 同段挤多项（H0 末两项之间无 `|`，aesthetic-experience 判例）时
        # 后者不带 sep——渲染须按账逐项发分隔符，不能靠 enumerate 推断
        st = {"first_of_part": True}

        def _push(item):
            if st["cur_sep"] and st["first_of_part"] and items:
                item["sep"] = True
            if st["first_of_part"]:
                st["first_of_part"] = False
            items.append(item)

        def _push_text(seg):
            seg = seg.strip()
            if seg:
                _push({"kind": "text",
                       "text": htmllib.unescape(
                           re.sub(r"<[^>]*>", "", seg))})

        for part in re.split(r"\s*\|\s*", rel.group(1)):
            part = part.strip()
            if not part:
                continue
            # 一段里可能挤多项（H0 末两项之间无 `|` 分隔，aesthetic-experience
            # 判例：Wittgenstein 项与死链 Yoruba 项同段），逐子项扫描
            st["first_of_part"] = True
            st["cur_sep"] = bool(items)  # 段与段之间必有 `|`
            pos = 0
            for m in re.finditer(
                    r'<!--<a href="([^"]*)">-->(.*?)<!--</a>-->'
                    r'|<a href="([^"]*)"[^>]*>(.*?)</a>', part, re.S):
                _push_text(part[pos:m.start()])
                if m.group(1) is not None:
                    _push({"kind": "dead", "href": m.group(1),
                           "text": htmllib.unescape(
                               re.sub(r"<[^>]*>", "", m.group(2)))})
                else:
                    _push({"kind": "a", "href": m.group(3),
                           "text": htmllib.unescape(
                               re.sub(r"<[^>]*>", "", m.group(4)))})
                pos = m.end()
            _push_text(part[pos:])
        led["rel_items"] = items
        # 尾随竖线（aesthetics-race 判例：H0 末项后仍有 ` |`）
        led["rel_trailing"] = bool(re.search(r"\|\s*$", rel.group(1)))
        # 首项前的竖线（realism／feminist-science／friedrich-lange 判例：H0 的
        # `<p>` 以 ` |` 起，C 落 md 时保留同名前导竖线，渲染侧须照发）
        if re.match(r"\s*\|", rel.group(1)):
            led["rel_lead"] = 1
    # 致谢区形态：独立 `<div id="acknowledgments">`（h3 常例）或 related-entries
    # 之后的裸 <h2>/<h3>（scientific-revolutions／fallacies 等 6 件）。只记有无包层；
    # 标题级别与锚形由 hids 按位取，区序由 md 的标题次序定。
    if re.search(r'<div id="acknowledgments">', art_inner):
        led["ack_div"] = 1
    elif re.search(r"<h[2-4][^>]*>(?:\s*<a[^>]*>)?\s*Acknowl", art_inner):
        led["ack_div"] = 0
    # 学术工具图标
    acad = re.search(r'<table class="vert-top">(.*?)</table>', art_inner, re.S)
    if acad:
        icons = []
        for m in re.finditer(r'<tr>\s*<td>(.*?)</td>\s*<td>', acad.group(1), re.S):
            cell = m.group(1)
            im = re.search(r'src="\.\./\.\./symbols/([^"]*)"\s+alt="([^"]*)"', cell)
            icons.append([im.group(1), im.group(2)] if im else ["", ""])
        led["acad_icons"] = icons
    tb = extract_tables(art_inner)
    if tb:
        led["tables"] = tb
    gk = extract_greek(art_inner, md)
    if gk:
        led["greek"] = gk
    gi = extract_greek_ital(art_inner, md, gk)
    if gi:
        led["greek_ital"] = gi
    led["entities"] = extract_entities(art_inner)
    _tails = [h[3] for h in led.get("bib_heads") or [] if len(h) > 3]
    led["links"] = extract_links(art_inner, _tails)
    it = extract_italics(art_inner)
    if it:
        led["italics"] = it
    gf = extract_greek_form(art_inner)
    if gf:
        led["greek_form"] = gf
    nf = extract_note_forms(art_inner)
    if nf:
        led["note_forms"] = nf
    sp = extract_sup_pos(art_inner)
    if sp:
        led["sup_pos"] = sp
    bq = extract_bq(art_inner)
    if bq:
        led["bq"] = bq
    pp = extract_photo_pre_h1(art_inner)
    if pp:
        led["photo_pre_h1"] = pp
    mf = extract_math_forms(art_inner)
    if mf:
        led["math_forms"] = mf
    mdol = extract_math_dollars(art_inner)
    if mdol:
        led["math_dollars"] = mdol
    toc = extract_toc(art_inner)
    if toc:
        led["toc_block"] = toc
    w = wrap_width(art_inner)
    if w:
        led["wrap_width"] = w
    return led


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    entries = {}
    n_no = 0
    base = {}
    bpath = repo_path("baseline", "entries.json")
    if os.path.exists(bpath):
        base = {r["slug"]: r for r in json.load(
            io.open(bpath, encoding="utf-8"))["entries"] if r.get("slug")}
    for d in sorted(os.listdir(repo_path("en"))):
        p = repo_path("en", d, "index.html")
        if not os.path.exists(p):
            continue
        t = read(p)
        if B1 not in t or E1 not in t:
            continue
        md = None
        zhip = (base.get(d) or {}).get("zh_doc")
        if zhip:
            mp = repo_path("yuanwen", zhip)
            if os.path.exists(mp):
                md = io.open(mp, encoding="utf-8").read()
        led = extract(inner_article(t), md)
        if not led.get("bib_groups") and not led.get("rel_items"):
            n_no += 1
        entries[d] = led
    sys.stderr.write("[ledger] %d 件；缺区段 %d\n" % (len(entries), n_no))
    if args.check:
        return 0
    payload = {"schema": "sep-cn-article-ledger/1",
               "generated_by": "specs/053 bin/article_ledger.py",
               "note": "正文段结构补集：只承载结构（标题 id 形态/文献切分/链接目标/图标），禁含散文",
               "entries": entries}
    with io.open(repo_path(*LEDGER_PATH), "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sys.stderr.write("[ledger] 写出 %s\n" % repo_path(*LEDGER_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
