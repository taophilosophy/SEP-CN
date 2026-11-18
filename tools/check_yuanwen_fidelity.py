#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""yuanwen→en 转换保真校验（ADR-0063 不变量 I2/I3；只读判官）

用法:
  python tools/check_yuanwen_fidelity.py [--slug X] [--letter a] [--limit N] [--gate]
  python tools/check_yuanwen_fidelity.py --deep [--slug X] [--limit N]

判官只读：不调用转换器写盘、不改 baseline、不触碰 en/。

默认档（I2-lite，廉价）——基线钉交叉核对：
  baseline/entries.json 每件登记 `yuanwen.sha256`（md 产物）与 `source_sha256`
  （en index.html 转换时的源）。两者任一与盘上不符即说明派生物已与源脱钩：
    md-hand-edited    md sha ≠ 登记（产物被手改，或未重转即改字）
    source-drift      en index.html sha ≠ 登记（源变未重转）
    no-baseline       md 存在而基线无 yuanwen 记录

`--deep`（I3，审计档）——文字流等值：
  两侧各自抽出词元（拉丁/希腊/西里尔/汉字/数字，NFKD 归一），比对**多重集**而非序列：
  书目转脚注定义、Notes 段归位等属合法移位，序列必变；丢字、叠字、重复标题会改变计数，
  正是要抓的缺陷（30 件重复 H1 即此面）。允许差异仅限转换器构造白名单：
    书名号外书目转 `[^key]:` 定义、节题括注（引用注释/原文脚注）、作者行（citation_author）、
    图 alt 与引用地址、上下标记法与 Unicode 上下标（NFKD）、数学内容（归 check_math）、
    补充材料包首说明行、"原文参考文献已转为脚注引用"底稿注记行、TOC（导航非内容）。
  白名单外差异＝转换器缺陷候选，逐条定性后或修转换器、或补白名单——禁止静默放行（P3）。

退出码: 0 通过；1 有不符（--gate 时默认档亦拦）；2 用法/输入错误。
"""
import argparse
import hashlib
import html as html_lib
import json
import os
import re
import sys
import unicodedata
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.common import repo_path, read_text  # noqa: E402
from tools.parser import HEAD_RE, TAIL_RE  # noqa: E402  区域标记与转换器同源

TOKEN_RE = re.compile(r"[0-9A-Za-z\u00C0-\u024F\u0370-\u03FF\u0400-\u04FF\u4e00-\u9fff]+")
FENCE_RE = re.compile(r"^```.*?^```", re.S | re.M)
FENCE_BODY_RE = re.compile(r"^```[^\n]*\n(.*?)^```", re.S | re.M)


def _fence_body_repl(match):
    """围栏体分流（specs/039 I3 三修，linguistics 判例）。

    yuanwen 的围栏主要是显示公式（裸 align/cases 之类，R2 裁定包进围栏），含 TeX
    控制序列或定界符者归数学面、不入字母流；纯文本示例（linguistics 的 XML 句法
    样例）是正文内容，整段保留——旧式一律剔围栏，189 字母凭空算作 html 侧独有。
    """
    body = match.group(1)
    if re.search(r"\\[A-Za-z]+|[${}]", body):
        return " "
    return "\n" + body + "\n"


CODE_RE = re.compile(r"`[^`]*`")
MATH_RE = re.compile(r"\$\$.*?\$\$|\$[^$\n]+\$", re.S)
# I3 标定（specs/039 P9 前置）：数学跨度哨兵与失配上限
SENTINEL = "\uE000"      # 私有区哨兵：字母流判据下与空格等价，为序列比对预留标记
MAX_SPAN = 6000          # 超限视为失配 opener（货币 $、缺 closer），按字面保留计 runaway
BLOCK_RE = re.compile(
    r"</?(?:p|div|br|li|ul|ol|dl|dt|dd|h[1-6]|table|thead|tbody|tr|td|th|"
    r"blockquote|pre|section|figure|figcaption|hr)\b[^>]*>", re.I)
# 侧向对称（specs/039 I3 三修，2026-11-17）：md 产物里逐字搬运的 HTML 片段
# （复杂表格、实体）与 html 侧同法剥离／解码；链接与图目标是机器标识符
# （html 在属性、md 在圆括号），两侧一律不计——簿记面由 check_pairs
# dangling-link 与 en_integrity 管辖。
_MD_TAGS = (
    r"table|thead|tbody|tfoot|tr|td|th|div|span|img|a|p|br|em|i|b|strong|"
    r"ul|ol|li|dl|dt|dd|h[1-6]|sup|sub|math|semantics|annotation|caption|figure|"
    r"blockquote|pre|code|font|center|hr|col|colgroup|small|big|u|s")
# 裸标签与属性标签分两口：带空格却无 `=` 的“尖括号散文”（`<I will go to the
# store…>`，action 判例）不是标签，**不得**整句吃掉——只认裸标签、自闭合、
# 或含属性的形态
MD_TAG_RE = re.compile(r"</?(?:%s)/?>" % _MD_TAGS, re.I)
MD_TAG_ATTR_RE = re.compile(r"</?(?:%s)\b(?=[^<>]*=)[^<>]*?>" % _MD_TAGS, re.I)
# 目标内允许一层成对圆括号（维基类 URL `…/wiki/Foo_(bar)` 判例，philosophy-religion）
MD_TARGET_RE = re.compile(
    r"\((?:https?://(?:[^()]|\([^()]*\))*|mailto:[^()]*|[^()\s]*\.(?:md|html?|png|jpe?g|gif|svg|pdf|js|css)"
    r"(?:#[^()]*)?|#[^()]*|\.\.?/[^()]*)\)", re.I)
ALT_MIN = 40             # 长 alt 说明文入流阈值：html_text 与 md_text 两侧同阈
SUPP_LINE_RE = re.compile(r"^#\s+.*（supplement）\s*$|^>\s*（《.*》词条补充材料.*）\s*$", re.M)
CONV_NOTE_RE = re.compile(r"^>\s*原文参考文献已转为脚注引用.*$", re.M)
TITLE_ANNOT = ("（引用注释）", "（原文脚注，引自主文）", "（原文脚注）")
ALIAS = {"references": "bibliography", "bibliography": "bibliography"}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_baseline():
    data = json.load(open(repo_path("baseline", "entries.json"), encoding="utf-8"))
    return {r["slug"]: r for r in data.get("entries", []) if r.get("slug")}


def iter_entries(only=None, letter=None, limit=None):
    """枚举 yuanwen 主件（带点补充材料子文档另档，不在此面）。"""
    root = repo_path("yuanwen")
    out = []
    for d in sorted(os.listdir(root)):
        # 目录名：单字母（a-z 小写）或单数字（数字开头词条，如 18thGerman-preKant 在 yuanwen/1/）
        if len(d) != 1 or not (d.isdigit() or (d.isalpha() and d.islower())):
            continue
        if letter and d != letter:
            continue
        for f in sorted(os.listdir(os.path.join(root, d))):
            if not f.endswith(".md"):
                continue
            slug = f[:-3]
            if "." in slug or (only and slug != only):
                continue
            out.append((slug, os.path.join("yuanwen", d, f)))
            if limit and len(out) >= limit:
                return out
    return out


def check_pins(slug, relpath, baseline):
    issues = []
    rec = baseline.get(slug)
    if not rec:
        return [{"slug": slug, "rule": "no-baseline", "detail": "基线无该件记录"}]
    yw = rec.get("yuanwen") or {}
    if not yw:
        return [{"slug": slug, "rule": "no-baseline", "detail": "基线无 yuanwen 转换记录"}]
    md_path = repo_path(relpath)
    if os.path.exists(md_path) and yw.get("sha256"):
        got = sha256_file(md_path)
        if got != yw["sha256"]:
            issues.append({"slug": slug, "rule": "md-hand-edited",
                           "detail": "md sha256 %s ≠ 登记 %s（产物被手改或未重转即改字）"
                                     % (got[:12], yw["sha256"][:12])})
    src_path = repo_path("en", slug, "index.html")
    if os.path.exists(src_path) and yw.get("source_sha256"):
        got = sha256_file(src_path)
        if got != yw["source_sha256"]:
            issues.append({"slug": slug, "rule": "source-drift",
                           "detail": "en index.html sha256 %s ≠ 登记 %s（源变未重转）"
                                     % (got[:12], yw["source_sha256"][:12])})
    return issues


def strip_container(html, marker):
    """剥除容器（如 div#toc）：标签深度配对，避免非贪婪正则截断。"""
    i = html.find(marker)
    if i < 0:
        return html
    j = i + len(marker)
    depth = 1
    for m in re.finditer(r"<div\b|</div\s*>", html[j:], re.I):
        depth += -1 if m.group(0).lower().startswith("</") else 1
        if depth == 0:
            return html[:i] + " " + html[j + m.end():]
    return html[:i]


def tokens(text):
    """词元流＋等价折叠（References（引用注释）↔Bibliography，大小写不敏感）。"""
    out = TOKEN_RE.findall(unicodedata.normalize("NFKD", text))
    return [ALIAS.get(w.lower(), w) for w in out]


def _stream_from_text(t):
    m, e = HEAD_RE.search(t), TAIL_RE.search(t)
    if m and e:
        t = t[m.end():e.start()]
    t = strip_container(t, '<div id="toc"')
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", t, flags=re.S | re.I)
    t = BLOCK_RE.sub("\n", t)
    # 注释编号簿记（页内注号锚、回链、<sup>[N]</sup> marker）两侧同剔，注号配对另有检查器
    t = re.sub(r"<sup[^>]*>\s*\[?\s*<a\b[^>]*>\s*[0-9]+[a-z]?[.]?\s*</a>\s*\]?\s*</sup>",
               " ", t, flags=re.I)
    t = re.sub(r"<a\b[^>]*>\s*[0-9]+[a-z]?\.\s*</a>", " ", t, flags=re.I)
    t = re.sub(r"<a\b[^>]*>\s*[0-9]+[a-z]?\s*</a>", " ", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)      # 行内标签不断词（<em>A</em>s → As）
    t = html_lib.unescape(t)
    t, stats = strip_math_ex(t)   # 数学归 check_math 面（转义感知，免 \left( 截断）
    return t, stats


def _html_stream(path):
    if not os.path.exists(path):
        return "", {"spans": 0, "oversize": 0, "unclosed": 0}
    return _stream_from_text(read_text(path))


def html_text(slug, apply_patches=False):
    """主文＝index.html 正文区；Notes 段来自 notes.html，一并入源流（ADR-0062 包内件）。

    图 alt 说明文是 md 侧可见文本（ADR-0037 图注体例），故把 alt 属性并入源流，
    与 md 的 `![说明](…)` 保 alt 处理对称。返回 (text, math_stats)。

    求值视图（specs/044 §1）：apply_patches=True 时先对 index.html 应用格式补丁
    （ADR-0062 apply_en_patches），使词元流源与转换器 yuanwen.convert_entry（先补丁
    后解析）同源；默认 False 保持 fidelity 门禁原行为不变。notes.html 补丁另议
    （当前池仅有 index.html 缺空格补丁）。
    """
    base = repo_path("en", slug)
    idx = os.path.join(base, "index.html")
    if not os.path.exists(idx):
        return None
    raw = read_text(idx)
    if apply_patches:
        from tools.yuanwen import apply_en_patches
        raw = apply_en_patches(slug, raw)
    m, e = HEAD_RE.search(raw), TAIL_RE.search(raw)
    region = raw[m.end():e.start()] if (m and e) else raw
    # 注释区不入流（与 _stream_from_text 同口径）：SEP 图常有旧的 <!-- <img alt…> -->
    # 版本留在注释里，连同 alt 一并收会把图注文本算两遍（large-cardinals 判例）
    region = re.sub(r"<!--.*?-->", " ", region, flags=re.S)
    # 图 alt 说明文（长文本）是 md 侧可见图注；短 alt 属装饰性图标，不入源流
    alts = [html_lib.unescape(a) for a in re.findall(r'alt="([^"]*)"', region)
            if len(a) >= ALT_MIN]
    text, stats = _stream_from_text(raw)
    notes_path = os.path.join(base, "notes.html")
    if os.path.exists(notes_path):
        raw = read_text(notes_path)
        # 注页标题「Notes to <条目>」整元素剔出（md 侧只有「Notes」段题）
        raw = re.sub(r"<h2[^>]*>\s*Notes to[\s\S]{0,300}?</h2>", " Notes ", raw, flags=re.I)
        # 注页里的图 alt 同样入流（time-travel 判例：长 alt 只存在于 notes.html）
        nregion = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
        alts += [html_lib.unescape(a)
                 for a in re.findall(r'alt="([^"]*)"', nregion) if len(a) >= ALT_MIN]
        t2, s2 = _stream_from_text(raw)
        text += "\n" + t2
        stats = {k: stats[k] + s2[k] for k in stats}
    if alts:
        text += "\n" + "\n".join(alts)
    return text, stats


def md_text(path):
    t = read_text(path)
    t = SUPP_LINE_RE.sub(" ", t)
    t = CONV_NOTE_RE.sub(" ", t)
    # 作者行：仅 H1 之后、首个二级标题之前的那一行（citation_author 元数据）
    head, sep, body = t.partition("\n## ")
    head = re.sub(r"^\*[^*\n]+\*\s*$", " ", head, flags=re.M)
    t = head + sep + body
    t = FENCE_BODY_RE.sub(_fence_body_repl, t)
    t = CODE_RE.sub(" ", t)
    t = MD_TAG_RE.sub(" ", t)          # 原样搬运的 HTML 片段：标签名不入流
    t = MD_TAG_ATTR_RE.sub(" ", t)     # 带属性的标签（`<td colspan="2">` 等）
    t = html_lib.unescape(t)           # 实体解码（&nbsp; 等），与 html 侧对称
    t, stats = strip_math_ex(t)
    # 注号 marker 必须先剔：`[^key](括注原文)` 这种“标记紧随括注”的产物会被
    # 链接规则误当成 `[文字](目标)` 把括注原文整段当目标删掉（gadamer/action/
    # secession 判例，2026-11-17 复核）
    t = re.sub(r"\[\^[^\]]+\]:", " ", t)                        # 引用注释定义前缀
    t = re.sub(r"\[\^[^\]]+\]", " ", t)                         # marker（注号与键均属簿记）
    # 图：alt 与 html 侧同阈（短 alt 属装饰性图标不入流，长 alt 是可见图注）；
    # 旧式 `(.*)` 贪婪在同行多图时把路径并进 alt——一并改为逐图匹配
    t = re.sub(r"!\[([^\[\]]*)\]\([^()]*\)",
               lambda m: " %s " % m.group(1) if len(m.group(1)) >= ALT_MIN else " ", t)
    t = MD_TARGET_RE.sub(" ", t)                                # 链接目标（URL/路径/锚）两侧不计
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)              # 链接保留文字
    for a in TITLE_ANNOT:
        t = t.replace(a, " ")
    t = re.sub(r"^#+\s*", " ", t, flags=re.M)
    t = re.sub(r"^>\s*", " ", t, flags=re.M)
    t = re.sub(r"^[*+-]\s+", " ", t, flags=re.M)
    t = re.sub(r"[*_]{1,3}", "", t)
    t = t.replace("{", "").replace("}", "").replace("|", " ")
    return t, stats


def strip_math_ex(text):
    """转义感知剥离数学定界符内容（`\\(…\\)`、`\\[…\\]`、`$…$`、`$$…$$`）——v2。

    返回 (text, stats)，stats = {"spans": 成对剥离数, "oversize": 超限跨度数,
    "unclosed": 缺 closer 数}。
    非贪婪正则会在 `\\left(`、`\\right)` 一类内部括号上提前截断，遗留 TeX 字母，
    使 html 侧凭空多出内容（2026-11-16 全量台账 formal-belief 等 5 万字母级伪差异即此因）。
    v2（specs/039 I3 标定）：
    * 剥离内容统一替换为哨兵 SENTINEL（字母流判据下与空格等价；为序列比对预留标记）；
    * 跨度超 MAX_SPAN 仍剥离但计 oversize——转换器把相邻公式与中间正文并成一个大跨度时
      （formal-belief 判例），字母判据对该件不适用，交 math-asymmetric 分类；
    * 缺 closer 的 opener（货币 `$`、残缺 `\\(`）按字面保留首字符并计 unclosed；
    * 三项计数供两侧对称性判定（判据见深比对主循环）。数学内容归 check_math／
      check_academic 面，本工具两侧一律不计。
    """
    out, i, n = [], 0, len(text)
    pairs = {"\\(": "\\)", "\\[": "\\]", "$$": "$$", "$": "$"}
    spans = oversize = unclosed = 0
    while i < n:
        opener = next((o for o in ("\\(", "\\[", "$$", "$") if text.startswith(o, i)), None)
        if opener is not None and i > 0 and text[i - 1] == "\\":
            opener = None          # 转义 opener（`\$` 字面美元号）：连同前导反斜杠按字面走
        if opener is None:
            out.append(text[i]); i += 1
            continue
        closer, j, found = pairs[opener], i + len(opener), -1
        while j < n:
            if text.startswith(closer, j) and not (j > 0 and text[j - 1] == "\\"):
                found = j
                break
            j += 1
        if found < 0:
            out.append(text[i]); i += 1
            unclosed += 1
            continue
        # 数学跨度一律按哨兵处理。2026-11-17 试过“无命令跨度保留字母”
        # （想做 W5 样式→定界的对称化），全库实测候选 47→47、零收益，已回退。
        out.append(SENTINEL)
        spans += 1
        if found - i > MAX_SPAN:
            oversize += 1
        i = found + len(closer)
    return "".join(out), {"spans": spans, "oversize": oversize, "unclosed": unclosed}


def strip_math(text):
    t, _ = strip_math_ex(text)
    return t


def chars(text):
    """字母流（NFKD 后只留字母，去组合记号）——I3 主判据。

    选字母多重集而非词元序列的理由：书目转脚注定义、Notes 归位、表格与列表重排都是
    合法移位，序列必变而字母计数不变；丢字、叠字、重复标题（如 30 件重复 H1）改变计数，
    正是要抓的面。数字不入主判据：注号、有序列表号、书号在 HTML 与 md 两侧的字面形态
    不对称（`<ol>` 自动编号 vs `1. ` 字面号、`<sup>[1]</sup>` vs `[^note-1]`），且数字
    面已由三校数字对账、`check_math` 与 `check_academic` 管；本工具改为报 `digits` 软信号。
    折叠转换器命名：`References` ↔ `Bibliography`（同义节题，非内容差异）。
    """
    text = re.sub(r"\bReferences\b", "Bibliography", text)
    text = re.sub(r"\breferences\b", "bibliography", text)
    s = unicodedata.normalize("NFKD", text)
    return [c for c in s if c.isalpha() and not unicodedata.combining(c)]


def digit_count(text):
    s = unicodedata.normalize("NFKD", text)
    return sum(1 for c in s if c.isdigit())


def multiset_diff(a, b):
    """主判据：字符多重集差异；返回 None 表示等值。"""
    ca, cb = Counter(chars(a)), Counter(chars(b))
    miss, extra = ca - cb, cb - ca
    if not miss and not extra:
        return None
    render = lambda c: "".join("%s×%d" % (k, v) if v > 1 else k
                               for k, v in sorted(c.items(), key=lambda kv: -kv[1])[:12])
    return {"n_missing": sum(miss.values()), "n_extra": sum(extra.values()),
            "missing": render(miss), "extra": render(extra),
            "words": word_diff(a, b)}


def word_diff(a, b):
    """辅助定位：词元多重集差异（仅用于报告可读性，不作判据）。"""
    ca, cb = Counter(tokens(a)), Counter(tokens(b))
    miss, extra = (ca - cb), (cb - ca)
    if not miss and not extra:
        return ""
    fmt = lambda c: "、".join("%s×%d" % (w, n) if n > 1 else w
                             for w, n in c.most_common(5))
    return "词元 缺[%s] 多[%s]" % (fmt(miss), fmt(extra))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    ap.add_argument("--letter")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--deep", action="store_true")
    ap.add_argument("--gate", action="store_true")
    args = ap.parse_args(argv)

    baseline = load_baseline()
    entries = iter_entries(args.slug, args.letter, args.limit)
    issues, deep_checked = [], 0
    n_asym = 0
    for slug, relpath in entries:
        issues.extend(check_pins(slug, relpath, baseline))
        if args.deep:
            ha = html_text(slug)
            if ha is None:
                continue
            a, st_a = ha
            b, st_b = md_text(repo_path(relpath))
            deep_checked += 1
            # 跨度对称性（specs/039 I3 标定）：两侧 spans 不等或任一侧 oversize/
            # unclosed ＝ 边界解析不对称，字母判据对该件不适用 → math-asymmetric
            # 软信号单列（不混入 text-stream-diff，防工具噪声冒充内容缺陷）。
            asym = (st_a["spans"] != st_b["spans"] or st_a["oversize"] or st_b["oversize"]
                    or st_a["unclosed"] or st_b["unclosed"])
            d = multiset_diff(a, b)
            if d and not asym:
                dd = digit_count(a) - digit_count(b)
                issues.append({"slug": slug, "rule": "text-stream-diff",
                               "detail": "缺 %d 字母「%s」；多 %d「%s」；数字差 %+d（软信号）"
                                         % (d["n_missing"], d["missing"],
                                            d["n_extra"], d["extra"], dd)})
            elif d and asym:
                issues.append({"slug": slug, "rule": "math-asymmetric-diff",
                               "detail": "跨度 html %d(超%d/缺%d) / md %d(超%d/缺%d) 不对称；"
                                         "字母差 缺%d 多%d（判据不适用，审计档）"
                                         % (st_a["spans"], st_a["oversize"], st_a["unclosed"],
                                            st_b["spans"], st_b["oversize"], st_b["unclosed"],
                                            d["n_missing"], d["n_extra"])})
            if asym:
                n_asym += 1
    print(json.dumps({"schema": "sep-cn-yuanwen-fidelity/1",
                      "checked": len(entries), "deep_checked": deep_checked,
                      "math_asymmetric": n_asym,
                      "issues": issues[:400], "issue_total": len(issues)},
                     ensure_ascii=False, indent=1))
    # --gate 拦 md-hand-edited / source-drift（真脱钩）；no-baseline 为覆盖缺口，
    # 告警不拦（2 件历史孤儿待登记，specs/039 P9）
    blocking = [i for i in issues if i.get('rule') != 'no-baseline']
    return 1 if (args.gate and blocking) else 0


if __name__ == "__main__":
    sys.exit(main())
