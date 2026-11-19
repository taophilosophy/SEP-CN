# -*- coding: utf-8 -*-
r"""B3.1 逆向装配器 R（specs/053 §7/§9；收缩对 C∘R=id_md）。

定理 T6/T7 语境：md 是转换器 C 的像，R 只需为每个 md 找到一个原像使
C(R(md)) == md（字节级）。歧义处（希腊字母、被丢链接、拆分标题）按收缩对
性质任意选定原像，不追求 R∘C=id。

设计（同源对照，ADR-0073）：R 不重实现转换语义——装配出的 HTML 交给
yuanwen 的同一套生产函数（extract_blocks_raw→render_blocks→build_cite_keys→
link_citations）求值。引注标记 [^bib-key] 从正文剥除（link_citations 确定性
重生成）；[^note-N] 还原为 <a href="notes.html#N">；Notes（原文脚注）节与
[^note-N]: 定义剥除（convert_notes 从 notes.html 再生）；References（引用注释）
改名 Bibliography 并剥固定注（render_blocks 再生）。

加强复核（ADR-0067 四件套内建）：
  ①守恒——R(md) 经 parse_entry 解析零错误＋marker/pubinfo B0 抽检；
  ②同源——求值用生产函数原体（本文件只做 md→HTML 的右逆）；
  ③负向——--selftest 篡改 md 一段必须破坏不动点；
  ④交集——试金石含补丁件（P-001 incommensurability，求值视图 en⊕patches）。

用法:
  reassemble.py [slugs...] [--out PATH]      # 缺省试金石：leucippus＋11 校准件
  reassemble.py --selftest                   # 负向证伪
退出码: 0 全部不动点成立；1 有失败；2 用法/selftest 失败。
只读判官：不写 en/、yuanwen/、baseline（R 的输出只在内存）。
"""
import argparse
import html as _html_mod
import io
import json
import os
import re
import sys
import time

html_unescape = _html_mod.unescape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

from tools import parser, yuanwen  # noqa: E402
from tools.common import repo_path, read_text  # noqa: E402

if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8")

TRIAL = ["leucippus", "david", "elias", "peirce-benjamin", "evolution",
         "reism", "holes", "lady-masham", "richard-sophister", "cockburn",
         "penbygull", "crathorn", "incommensurability", "abelard",
         "bayes-theorem"]

MD_HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
MD_DEF_RE = re.compile(r"^\[\^([^\]\s]+)\]:(.*)$", re.S)
NOTEDEF_KEY_RE = re.compile(r"^note-\d+$")
MD_LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.])\s+(.*)$")
SUB_MAP = getattr(yuanwen, "SUB_MAP", {})
SUP_MAP = getattr(yuanwen, "SUP_MAP", {})
GREEK_UNI = getattr(yuanwen, "GREEK_UNI", {})
GREEK_C_DEFER = getattr(yuanwen, "GREEK_C_DEFER", set())
GREEK_REV = {v: k for k, v in GREEK_UNI.items()}

FIXED_NOTE = ("原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，"
              "完整条目见本文末脚注定义。")


# ------------------------------------------------------------ inline 逆写 --

def _inline_md_to_html(text):
    """md 行内 → 行内 HTML（inline_to_md 的右逆；只覆盖 C 像内出现的形）。"""
    s = text
    # 文本层转义：C 在输出端 unescape，R 必须先把字面 & < > 编码回实体——
    # 否则 md 里的 <URL> 尖括号在装配 HTML 中被当标签吃掉（bayes-theorem 判例）
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # 字面转义星（\*）占位保护——必须在强调解析前隔离，否则 *H\** 会被
    # 拆成 *H** 破配对（bayes-theorem 判例）；解析后还原为裸 *
    s = s.replace("\\*", "\x01")
    # 引注标记剥除——link_citations 确定性重生成（keys 同源）
    s = re.sub(r"\[\^(?!note-)[^\]\s]+\]", "", s)
    # 注释引用 → 锚链接（NOTE_REF_RE 可匹配的两种 href 形任选其一）
    s = re.sub(r"\[\^note-([^\]\s]+)\]", r'<a href="notes.html#note-\1">\1</a>', s)
    # 数学先占位——TeX 内的 _{x}/^{x} 不得被下面的 sub/sup 规则改写
    # （dutch-book 判例：$\pr_{t}$ 曾变 $\pr<sub>t</sub>$ → C 出 ₜ）
    math_store = []

    def _stash_math(m):
        math_store.append(m.group(0))
        return "\x02%d\x02" % (len(math_store) - 1)

    s = re.sub(r"\$\$[^$]+\$\$|\$[^$]+\$", _stash_math, s)
    # 链接（分类还原；页内锚/index.html 链接 C 本就丢弃 → 纯文本）
    def _link(m):
        t, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://")):
            return '<a href="%s">%s</a>' % (url, t)
        m2 = re.fullmatch(r"\.\./assets/[a-z0-9-]+/([A-Za-z0-9._%+-]+)", url)
        if m2:
            return '<a href="%s">%s</a>' % (m2.group(1), t)
        m3 = re.fullmatch(r"([a-z0-9-]+)\.([a-z0-9-]+)\.md", url)
        if m3:
            return '<a href="%s.%s">%s</a>' % (m3.group(2), "html", t)
        return t  # 页内锚／index.html 链接——C 原样丢链接保文本
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, s)
    # 行内代码
    s = re.sub(r"`([^`]*)`", r"<code>\1</code>", s)
    # sub/sup 记号（_{x}/^{x}）→ 标签；原生 Unicode 字形已由 C 直接产出，
    # R 不识别（原样文本，C 亦原样）。数学占位符内的记号不受影响。
    s = re.sub(r"_\{([^}]*)\}", r"<sub>\1</sub>", s)
    s = re.sub(r"\^\{([^}]*)\}", r"<sup>\1</sup>", s)
    # 强调／粗体（单层；C 的 em 先于 strong，嵌套粗斜体在像内为 ***x***——
    # 简形词条未出现，残差清单登记）
    # 强调／粗体：小型星解析器——C 输出的强调定界符恒「紧」（内侧无空格，
    # _md_emphasis strip 保证），据此把裸星三分类：开／闭／字面（W10：
    # happens* 与 10 * Prob 的乘号/记号星不再被误配对）
    s = _star_parse(s)
    # 数学占位还原（$x$ → \(x\)；$$x$$ → \[x\]）
    for idx, val in enumerate(math_store):
        if val.startswith("$$"):
            rep = r"\[" + val[2:-2] + r"\]"
        else:
            rep = r"\(" + val[1:-1] + r"\)"
        s = s.replace("\x02%d\x02" % idx, rep)
    # 字面星还原（占位符 \x01 → 裸 *，在 HTML 文本层即普通字符）
    s = s.replace("\x01", "*")
    return s


def _em(inner):
    """孤立希腊斜体回写 \\(\\alpha\\)（ADR-0049 逆映射，反斜杠必须有——C 侧
    fullmatch r'\\\\([A-Za-z]+)' 识别的是带杠命令名）；其余内容包 <em>。"""
    m = re.fullmatch(r"([A-Za-zα-ωΑ-Ω]+)", inner)
    if m and m.group(0) in GREEK_REV and m.group(0) not in GREEK_C_DEFER:
        return r"\(\%s\)" % GREEK_REV[m.group(0)]
    return "<em>%s</em>" % inner


def _star_parse(s):
    """md 星号 → HTML 强调（C 输出定界符恒紧：内侧无空格）。

    逐 run 决策：开＝下一字符非空白且同级未开；闭＝上一字符非空白且同级已开；
    其余＝字面星（HTML 文本层原样）。***x*** 为 strong+em 双级（W10：
    happens* / 10 * Prob 的记号星与乘号星按紧性判为字面，不再被误配对）。
    """
    parts = re.split(r"(\*+)", s)
    out = []
    marks = {}  # 'strong'/'em' -> out 中内容起始下标
    for i, p in enumerate(parts):
        if i % 2 == 0:
            out.append(p)
            continue
        run = parts[i]
        before = parts[i - 1]
        after = parts[i + 1] if i + 1 < len(parts) else ""
        prev_tight = bool(before) and not before[-1:].isspace()
        next_tight = bool(after) and not after[:1].isspace()
        # 开星要求左邻非字母数字（(G*1) 类记号星、A* 类字面星不误开）；
        # 存疑一律按字面——字面星经 C 原样回写，不动点不受损
        prev_alnum = bool(before) and before[-1:].isalnum()
        L = len(run)
        want = ["strong", "em"] if L >= 3 else (["strong"] if L == 2 else ["em"])
        if all(k in marks for k in want) and prev_tight:
            start = min(marks.pop(k) for k in want)
            content = "".join(out[start:])
            del out[start:]
            if len(want) == 2:
                out.append("<strong>%s</strong>"
                           % ("<em>%s</em>" % content.strip()))
            elif want[0] == "em":
                out.append(_em(content.strip()))
            else:
                out.append("<strong>%s</strong>" % content)
        elif not any(k in marks for k in want) and next_tight and not prev_alnum:
            slot = len(out)
            for k in want:
                marks[k] = slot
            out.append("")
            marks.setdefault("__runs", {})[slot] = run
        else:
            out.append(run)
    # 未闭合星恢复为字面（(3*) 这类括号内记号星——无配对即字面）
    runs = marks.pop("__runs", {})
    for slot, run in runs.items():
        if slot < len(out) and out[slot] == "":
            out[slot] = run
    return "".join(out)


def _td(cell):
    return "<td>%s</td>" % _inline_md_to_html(cell.strip())


# ------------------------------------------------------------ 块级逆写 ----

def reassemble_article(md, authors):
    """md（主档全文）→ (title, article_html)。不动点验证在调用方闭环。"""
    lines = md.split("\n")
    out = []          # HTML 片段
    title = None
    i = 0
    n = len(lines)
    bib_defs = []     # 文献定义（非 note-*），两遍扫描：先收集
    for ln in lines:
        dm = MD_DEF_RE.match(ln)
        if dm and not (NOTEDEF_KEY_RE.match(dm.group(1))
                       or dm.group(1).startswith("note-")):
            bib_defs.append(dm.group(2).strip())
    bib_ul_emitted = False
    while i < n:
        ln = lines[i]
        stripped = ln.strip()
        if not stripped:
            i += 1
            continue
        # 前三行的合成层（C 再生，R 不装配）：pubinfo 行与作者行
        if i <= 3 and PUBINFO_LINE_RE.fullmatch(stripped):
            out.append(_pubinfo_html([stripped]) or "")
            i += 1
            continue
        if i <= 3 and re.fullmatch(r"\*[^*]+\*", stripped):
            i += 1
            continue
        m = MD_HEAD_RE.match(ln)
        if m:
            lv = len(m.group(1))
            text = m.group(2).strip()
            if lv == 1:
                # h1 直接装配（像内词条的 H1 多来自 article h1 块；meta 前缀
                # 仅在 md 不以 '# ' 开头时触发——装配后恒以 '# ' 开头）
                out.append("<h1>%s</h1>" % _inline_md_to_html(text))
                i += 1
                continue
            if text == "References（引用注释）":
                out.append("<h2>Bibliography</h2>")
                i += 1
                # 剥固定注（render_blocks 再生）；区散文段按序先发（bib_entries
                # 次序＝HTML 文档序——abhidharma 判例：prose 先于 ul，
                # 次序颠倒即全键错位）；文献 li 随后原位发射
                while i < n and (not lines[i].strip()
                                 or lines[i].startswith("> ")
                                 or lines[i].strip() == ">"):
                    i += 1
                region_ps = []
                while i < n:
                    s2 = lines[i].strip()
                    if (not s2 or s2.startswith("#") or MD_DEF_RE.match(lines[i])
                            or s2.startswith("|") or MD_LIST_RE.match(lines[i])):
                        break
                    region_ps.append(s2)
                    i += 1
                for s2 in region_ps:
                    out.append("<p>%s</p>" % _inline_md_to_html(s2))
                if bib_defs and not bib_ul_emitted:
                    lis = "".join("<li>%s</li>" % _inline_md_to_html(d)
                                  for d in bib_defs)
                    out.append("<ul>%s</ul>" % lis)
                    bib_ul_emitted = True
                continue
            if text.startswith("Notes（原文脚注"):
                # 注释节是 C 在文末追加的末节（其后仅 cite defs），脚注内容可含
                # 引块/列表/公式块——一律跳到文件尾（affirmative-action 判例：
                # 只跳空行+def 行会把脚注里的列表漏成正文）
                i = n
                continue
            out.append("<h%d>%s</h%d>" % (lv, _inline_md_to_html(text), lv))
            i += 1
            continue
        if stripped.startswith(">"):
            # 引块：整块收集（含引块表）；剥 '> ' 前缀。
            # 空 `>` 行＝段落分隔；连续非空行＝同段内 <br>（richard-sophister 判例：
            # C 侧块内 BR_MARK 恢复为 \n 后每行加 '> '，无空行分隔）
            q = []
            while i < n and lines[i].startswith(">"):
                q.append(lines[i][1:].lstrip(" "))
                i += 1
            paras = []
            cur = []
            for line in q:
                if line.strip():
                    cur.append(line)
                elif cur:
                    paras.append(cur)
                    cur = []
            if cur:
                paras.append(cur)
            if not paras:
                continue
            if len(paras) == 1 and paras[0][0].strip().startswith("|"):
                rows = _pipe_rows("\n".join(paras[0]))
                cells = [[_td(c) for c in r] for r in rows]
                trs = "".join("<tr>%s</tr>" % "".join(cs) for cs in cells)
                out.append("<blockquote><table>%s</table></blockquote>" % trs)
            else:
                inner = ""
                for p in paras:
                    if p[0].strip().startswith("|"):
                        rows = _pipe_rows("\n".join(p))
                        cells = [[_td(c) for c in r] for r in rows]
                        trs = "".join("<tr>%s</tr>" % "".join(cs) for cs in cells)
                        inner += "<table>%s</table>" % trs
                    else:
                        inner += "<p>%s</p>" % "<br>".join(
                            _inline_md_to_html(x) for x in p)
                out.append("<blockquote>%s</blockquote>" % inner)
            continue
        if MD_DEF_RE.match(ln):
            # 定义行已两遍扫描收集（note-* 由 convert_notes 再生，文献由
            # Bibliography 区 ul 再生）——主循环一律跳过
            i += 1
            while i < n and lines[i].strip():
                i += 1
            continue
        if stripped.startswith("|"):
            rows, i = _pipe_rows_collect(lines, i)
            out.append(_table_html(rows))
            continue
        if MD_LIST_RE.match(ln):
            items, i = _collect_list(lines, i)
            out.append(_list_html(items))
            continue
        # 段落：连续非空、非结构行
        para = [stripped]
        i += 1
        while i < n and lines[i].strip() and not _is_block_start(lines[i]):
            para.append(lines[i].strip())
            i += 1
        text = " ".join(para)
        # 表题：table_to_md 输出 '*cap*' 紧贴表格（cap 自身可为 **bold**，
        # 故 md 形为 ***X***）——逆装配为 <caption>（bayes-theorem 判例）
        cm = re.fullmatch(r"\*(.+)\*", text)
        j = i
        while j < n and not lines[j].strip():
            j += 1
        if cm and j < n and lines[j].strip().startswith("|"):
            rows, i = _pipe_rows_collect(lines, j)
            out.append(_table_html(rows, cap_md=cm.group(1)))
            continue
        out.append("<p>%s</p>" % _inline_md_to_html(text))
    # 文献 ul 已在 References（引用注释）分支原位发射（bib_ul_emitted 守卫）；
    # 文末不再发射——尾部 ul 落在 in_bib 区间外会被渲染成 md 列表（leucippus 判例）
    return title, "\n".join(out)


def _strip_md(text):
    return text.strip()


PUBINFO_LINE_RE = re.compile(r"\*\*First published[^*]*\*\*")


def _is_block_start(ln):
    s = ln.strip()
    return (not s or s.startswith(">") or s.startswith("|")
            or MD_HEAD_RE.match(ln) or MD_DEF_RE.match(ln)
            or MD_LIST_RE.match(ln) or PUBINFO_LINE_RE.fullmatch(s))


def _pubinfo_html(lines):
    for idx, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("**First published") and s.endswith("**") and idx <= 3:
            inner = s[2:-2]
            return '<div id="pubinfo"><em>%s</em></div>' % inner
        if idx > 3:
            break
    return None


def _pipe_rows(body):
    rows = []
    for ln in body.split("\n"):
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c for c in s.strip("|").split("|")]
        if re.fullmatch(r"[\s:|-]+", s.strip("|")):
            continue  # 分隔行
        rows.append(cells)
    return rows


def _pipe_rows_collect(lines, i):
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        s = lines[i].strip()
        cells = [c for c in s.strip("|").split("|")]
        if not re.fullmatch(r"[\s:|-]+", s.strip("|")):
            rows.append(cells)
        i += 1
    return rows, i


def _table_html(rows, cap_md=None):
    cells = [[_td(c) for c in r] for r in rows]
    trs = "".join("<tr>%s</tr>" % "".join(cs) for cs in cells)
    cap = ""
    if cap_md is not None:
        cap = "<caption>%s</caption>" % _inline_md_to_html(cap_md)
    return "<table>%s%s</table>" % (cap, trs)


def _collect_list(lines, i):
    items = []  # (indent, ordered, text)
    base_indent = len(lines[i]) - len(lines[i].lstrip())
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            break  # 松散列表：项间空行即列表边界（C 每 <ul> 紧排输出；
            # 桥接会把两个列表并成一个——atheism-agnosticism 判例）
        m = MD_LIST_RE.match(ln)
        if not m or (len(ln) - len(ln.lstrip())) < base_indent:
            break
        ind = len(ln) - len(ln.lstrip())
        ordered = m.group(2)[0].isdigit()
        items.append((ind, ordered, m.group(3)))
        i += 1
    return items, i


def _list_html(items):
    """一层列表 → <ul>/<ol><li>（嵌套缩进扁平化＝C list_to_md 的可逆形）。"""
    ordered = items[0][1]
    tag = "ol" if ordered else "ul"
    lis = "".join("<li>%s</li>" % _inline_md_to_html(tx) for _, _, tx in items)
    return "<%s>%s</%s>" % (tag, lis, tag)


# ------------------------------------------------------------ 求值闭环 ----

def convert_from_parts(slug, title, authors, article_html, notes_html=None):
    """同源求值：replicate convert_entry 主链（读映射原体），不落盘。"""
    article = yuanwen.strip_closed_comments(article_html)
    article, stash = yuanwen.protect_cross_block_math(article)
    ctx = yuanwen.Ctx(slug)
    yuanwen.render_blocks(yuanwen.extract_blocks_raw(article), ctx)
    md = "\n".join(ctx.out).strip()
    if not md.startswith("# "):
        md = "# %s\n\n%s" % (title, md)
    md = yuanwen._drop_duplicate_h1(md)
    if authors:
        md = md.replace("\n\n", "\n\n*%s*\n\n" % ", ".join(authors), 1)
    if notes_html:
        note_defs = yuanwen.convert_notes(notes_html, slug)
        if note_defs:
            md += "\n\n## Notes（原文脚注）\n\n" + "\n\n".join(note_defs)
    keys = yuanwen.build_cite_keys(ctx.bib_entries, fallback_author=slug)
    if keys:
        md, _, _used = yuanwen.link_citations(md, keys)
        md += "\n\n" + "\n\n".join("[^%s]: %s" % (k["key"], k["text"])
                                   for k in keys)
    md = yuanwen.restore_cross_block_math(md, stash)
    return md


def judge_slug(slug, baseline):
    rec = baseline.get(slug)
    if not rec:
        return {"slug": slug, "ok": False, "skipped": "not in baseline"}
    en_idx = repo_path("en", slug, "index.html")
    md_path = repo_path("yuanwen", rec.get("zh_doc") or "")
    if not os.path.exists(en_idx):
        return {"slug": slug, "ok": False, "skipped": "no en package"}
    if not os.path.exists(md_path):
        return {"slug": slug, "ok": False, "skipped": "no yuanwen md"}
    html0 = read_text(en_idx)
    md0 = io.open(md_path, encoding="utf-8").read().rstrip("\n")
    try:
        html1 = yuanwen.apply_en_patches(slug, html0)
    except Exception as ex:  # noqa: BLE001——判官报告，不中断全量
        return {"slug": slug, "ok": False, "skipped": "patch: %s" % ex}
    m = re.search(r'<meta name="citation_title" content="([^"]*)"', html1)
    authors = [html_unescape(a) for a in
               re.findall(r'<meta name="citation_author" content="([^"]*)"', html1)]
    notes_path = repo_path("en", slug, "notes.html")
    notes_html = read_text(notes_path) if os.path.exists(notes_path) else None
    title, article_r = reassemble_article(md0, authors)
    if not title:
        title = m.group(1) if m else slug
    # ①守恒抽检：装配体可解析＋marker/pubinfo 命中（mini-B0）
    pr = parser.parse_entry(article_r)
    b0_mini = {"sections": len([b for b in pr["blocks"]
                                if b["type"].startswith("h")]) > 0,
               "parses": True}
    # ②同源求值闭环
    md2 = convert_from_parts(slug, title, authors, article_r, notes_html)
    ok = md2 == md0
    res = {"slug": slug, "ok": ok, "md_len": len(md0),
           "b0_mini": b0_mini}
    if not ok:
        # O(n) 首差定位（difflib.SequenceMatcher autojunk=False 在大文件近等串
        # 上二次方，abelard 150KB 实证卡死——改前后缀修剪）
        pre = 0
        while pre < min(len(md0), len(md2)) and md0[pre] == md2[pre]:
            pre += 1
        suf = 0
        while (suf < min(len(md0), len(md2)) - pre
               and md0[len(md0) - 1 - suf] == md2[len(md2) - 1 - suf]):
            suf += 1
        res["first_diff"] = {"op": "replace",
                             "md": md0[max(0, pre - 60):len(md0) - suf + 60][-140:],
                             "asm": md2[max(0, pre - 60):len(md2) - suf + 60][-140:]}
    return res


def selftest(baseline):
    """负向证伪：篡改 md 任一段 → 不动点必须破坏。"""
    slug = "leucippus"
    rec = baseline[slug]
    md0 = io.open(repo_path("yuanwen", rec["zh_doc"]), encoding="utf-8").read()
    md0 = md0.rstrip("\n")
    lines = md0.split("\n")
    # 删一个正文段（首个非空、非结构、非定义行）
    idx = next(i for i, ln in enumerate(lines)
               if ln.strip() and not _is_block_start(ln) and i > 3)
    bad = "\n".join(lines[:idx] + lines[idx + 1:])
    html0 = read_text(repo_path("en", slug, "index.html"))
    authors = [html_unescape(a) for a in
               re.findall(r'<meta name="citation_author" content="([^"]*)"',
                          html0)]
    m = re.search(r'<meta name="citation_title" content="([^"]*)"', html0)
    title, article_r = reassemble_article(bad, authors)
    md2 = convert_from_parts(slug, m.group(1) if m else slug, authors,
                             article_r, None)
    return {"ok": md2 != bad, "slug": slug}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    baseline = {r["slug"]: r for r in json.load(io.open(
        repo_path("baseline", "entries.json"), encoding="utf-8"))["entries"]
        if isinstance(r, dict) and r.get("slug")}
    if args.selftest:
        res = selftest(baseline)
        print(json.dumps({"schema": "sep-cn-b31-selftest/1", "selftest": res},
                         ensure_ascii=False, indent=1))
        return 0 if res["ok"] else 2
    slugs = sorted(baseline) if args.all else (args.slugs or TRIAL)
    entries, n_ok, n_fail, n_skip = [], 0, 0, 0
    t0 = time.time()
    for idx, slug in enumerate(slugs, 1):
        ts = time.time()
        try:
            r = judge_slug(slug, baseline)
        except Exception as ex:  # noqa: BLE001——单件异常不中断全量
            r = {"slug": slug, "ok": False, "skipped": "error: %s" % ex}
        r["sec"] = round(time.time() - ts, 3)
        if r["sec"] > 5:
            sys.stderr.write("[b31] 慢件 %.1fs %s\n" % (r["sec"], slug))
            sys.stderr.flush()
        if args.all and idx % 50 == 0:
            sys.stderr.write("[b31] %d/%d 已过 %.0fs\n"
                             % (idx, len(slugs), time.time() - t0))
            sys.stderr.flush()
        entries.append(r)
        if r.get("skipped"):
            n_skip += 1
        elif r["ok"]:
            n_ok += 1
        else:
            n_fail += 1
    payload = {"schema": "sep-cn-b31-assembly/1",
               "generated_by": "specs/053 bin/reassemble.py",
               "total": len(entries), "ok": n_ok, "fail": n_fail,
               "skipped": n_skip, "entries": entries}
    out = args.out or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "results", "assembly-trial.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sys.stderr.write("[b31] 总 %d：不动点 %d／失败 %d／跳过 %d → %s\n"
                     % (len(entries), n_ok, n_fail, n_skip, out))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
