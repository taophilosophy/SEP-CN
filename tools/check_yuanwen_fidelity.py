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
CODE_RE = re.compile(r"`[^`]*`")
MATH_RE = re.compile(r"\$\$.*?\$\$|\$[^$\n]+\$", re.S)
BLOCK_RE = re.compile(
    r"</?(?:p|div|br|li|ul|ol|dl|dt|dd|h[1-6]|table|thead|tbody|tr|td|th|"
    r"blockquote|pre|section|figure|figcaption|hr)\b[^>]*>", re.I)
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
        if len(d) != 1 or not d.isalpha() or not d.islower():
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
    t = strip_math(t)   # 数学归 check_math 面（转义感知，免 \left( 截断）
    return t


def _html_stream(path):
    return _stream_from_text(read_text(path)) if os.path.exists(path) else ""


def html_text(slug):
    """主文＝index.html 正文区；Notes 段来自 notes.html，一并入源流（ADR-0062 包内件）。

    图 alt 说明文是 md 侧可见文本（ADR-0037 图注体例），故把 alt 属性并入源流，
    与 md 的 `![说明](…)` 保 alt 处理对称。
    """
    base = repo_path("en", slug)
    idx = os.path.join(base, "index.html")
    if not os.path.exists(idx):
        return None
    raw = read_text(idx)
    m, e = HEAD_RE.search(raw), TAIL_RE.search(raw)
    region = raw[m.end():e.start()] if (m and e) else raw
    # 图 alt 说明文（长文本）是 md 侧可见图注；短 alt 属装饰性图标，不入源流
    alts = [html_lib.unescape(a) for a in re.findall(r'alt="([^"]*)"', region)
            if len(a) >= 40]
    text = _stream_from_text(raw)
    if alts:
        text += "\n" + "\n".join(alts)
    notes_path = os.path.join(base, "notes.html")
    if os.path.exists(notes_path):
        raw = read_text(notes_path)
        # 注页标题「Notes to <条目>」整元素剔出（md 侧只有「Notes」段题）
        raw = re.sub(r"<h2[^>]*>\s*Notes to[\s\S]{0,300}?</h2>", " Notes ", raw, flags=re.I)
        text += "\n" + _stream_from_text(raw)
    return text


def md_text(path):
    t = read_text(path)
    t = SUPP_LINE_RE.sub(" ", t)
    t = CONV_NOTE_RE.sub(" ", t)
    # 作者行：仅 H1 之后、首个二级标题之前的那一行（citation_author 元数据）
    head, sep, body = t.partition("\n## ")
    head = re.sub(r"^\*[^*\n]+\*\s*$", " ", head, flags=re.M)
    t = head + sep + body
    t = FENCE_RE.sub(" ", t)
    t = CODE_RE.sub(" ", t)
    t = strip_math(t)
    t = re.sub(r"!\[(.*)\]\([^)]*\)", r"\1", t)                 # 图：保 alt 说明（与 html alt 对称）
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)              # 链接保留文字
    t = re.sub(r"\[\^[^\]]+\]:", " ", t)                        # 引用注释定义前缀
    t = re.sub(r"\[\^[^\]]+\]", " ", t)                         # marker（注号与键均属簿记）
    for a in TITLE_ANNOT:
        t = t.replace(a, " ")
    t = re.sub(r"^#+\s*", " ", t, flags=re.M)
    t = re.sub(r"^>\s*", " ", t, flags=re.M)
    t = re.sub(r"^[*+-]\s+", " ", t, flags=re.M)
    t = re.sub(r"[*_]{1,3}", "", t)
    t = t.replace("{", "").replace("}", "").replace("|", " ")
    return t


def strip_math(text):
    """转义感知剥离数学定界符内容（`\\(…\\)`、`\\[…\\]`、`$…$`、`$$…$$`）。

    非贪婪正则会在 `\\left(`、`\\right)` 一类内部括号上提前截断，遗留 TeX 字母，
    使 html 侧凭空多出内容（2026-11-16 全量台账 formal-belief 等 5 万字母级伪差异即此因）。
    数学内容归 check_math／check_academic 面，本工具两侧一律不计。
    """
    out, i, n = [], 0, len(text)
    pairs = {"\\(": "\\)", "\\[": "\\]", "$$": "$$", "$": "$"}
    while i < n:
        opener = next((o for o in ("\\(", "\\[", "$$", "$") if text.startswith(o, i)), None)
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
            continue
        out.append(" ")
        i = found + len(closer)
    return "".join(out)


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
    for slug, relpath in entries:
        issues.extend(check_pins(slug, relpath, baseline))
        if args.deep:
            a = html_text(slug)
            if a is None:
                continue
            b = md_text(repo_path(relpath))
            deep_checked += 1
            d = multiset_diff(a, b)
            if d:
                dd = digit_count(a) - digit_count(b)
                issues.append({"slug": slug, "rule": "text-stream-diff",
                               "detail": "缺 %d 字母「%s」；多 %d「%s」；数字差 %+d（软信号）"
                                         % (d["n_missing"], d["missing"],
                                            d["n_extra"], d["extra"], dd)})
    print(json.dumps({"schema": "sep-cn-yuanwen-fidelity/1",
                      "checked": len(entries), "deep_checked": deep_checked,
                      "issues": issues[:400], "issue_total": len(issues)},
                     ensure_ascii=False, indent=1))
    # --gate 拦 md-hand-edited / source-drift（真脱钩）；no-baseline 为覆盖缺口，
    # 告警不拦（2 件历史孤儿待登记，specs/039 P9）
    blocking = [i for i in issues if i.get('rule') != 'no-baseline']
    return 1 if (args.gate and blocking) else 0


if __name__ == "__main__":
    sys.exit(main())
