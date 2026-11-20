#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""B3.2 装配补集池（v4）：分段对齐 ＋ 文字单元布局账。

分段模型：
  segments(s) → [("m", 标记段) | ("u", 文字段), …]（按串序拼接回原文）
    块级标签/注释/空白为标记段（含标签间空白）；两段之间为文字段。
  A（装配）与 B（H0）按“文字段去空白字符流”序列做 difflib 对齐：
    · 对齐处的标记段差异          → m 补丁（只含标签/空白）
    · 对齐处的文字段差异（键相等）→ u 补丁（布局账：切片引用装配侧文字）
    · 未对齐的区段（插入/删除）   → 仅当涉及文字段去空白后皆为空才可入池，
                                    合并为一个 r 补丁（记 B 侧原文串）

硬谓词：
  P1 文字等值：u 键逐段相等；r 补丁涉及的文字段去空白后为空
  P2 命中即消耗：m/u 补丁的段哈希、r 补丁的段数必须吻合
  P3 全覆盖：应用结果与 H0 逐字节相等
"""
import difflib
import hashlib
import html as htmllib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from tools.common import repo_path  # noqa: E402

POOL_DIR = ("baseline", "en-template", "assembly-patches")
SCHEMA = "sep-cn-assembly-patch/4"
BLOCK_TAGS = ("h1|h2|h3|h4|h5|h6|p|ul|ol|li|div|blockquote|table|tr|td|th|"
              "caption|pre|figure|dl|dt|dd")
BLK_RE = re.compile(r"</?(?:%s)\b[^>]*>" % BLOCK_TAGS)
TOKEN_RE = re.compile(r"<!--.*?-->|<[^>]*>|[^<]+", re.S)
WS_SPLIT_RE = re.compile(r"\s+|[^\s]+")
WS_RE = re.compile(r"\s+")
CMT_RE = re.compile(r"<!--.*?-->", re.S)


def _strip_cmt(s):
    """剥 HTML 注释（注释内文字不是可见文字，不参与等值判定）。

    bodin 判例：H0 用 `<!--<p>Another Bodin Project…</p>-->` 注释掉一段，
    C 正确丢弃；旧 plain/ukey 只剥标签不剥注释内容，注释文字混入 B 侧
    文字流 → 假文字差（ENT FAIL）。"""
    return CMT_RE.sub("", s)


def segments(s):
    """→ [("m", markup) | ("u", text), …]"""
    out, cur, kind = [], "", "m"
    for m in TOKEN_RE.finditer(s):
        tk = m.group(0)
        if tk.startswith("<"):
            if tk.startswith("<!--") or BLK_RE.fullmatch(tk):
                if cur:
                    out.append((kind, cur))
                cur, kind = tk, "m"
                continue
            if kind != "u":
                if cur:
                    out.append((kind, cur))
                cur, kind = "", "u"
            cur += tk
            continue
        if not tk.strip():
            cur += tk
            continue
        if kind != "u":
            if cur:
                out.append((kind, cur))
            cur, kind = "", "u"
        cur += tk
    if cur:
        out.append((kind, cur))
    return out


def plain(text):
    """文字段的无空白字符流（去标签、去空白，实体保留原形）。

    &nbsp; 保留原形（6 字符计入坐标）：layout_items 的 piece 累计与
    ent_spans 的 pos 必须同一坐标系，否则 tx 切片越界（98 件
    "tx out of range" 判例）。&nbsp; 的空白语义由 _ws_decoded（unkey/
    ent 等值判定）承载。"""
    return WS_RE.sub("", re.sub(r"<[^>]*>", "", _strip_cmt(text)))


def ukey(text):
    """对齐键：剥标签＋解实体＋去空白（实体形态差不影响对齐）。"""
    return WS_RE.sub("", htmllib.unescape(re.sub(r"<[^>]*>", "", _strip_cmt(text))))


def _ws_decoded(s):
    """解码实体并折叠空白（排版空白不算文字：&thinsp; 与空格视同等值）。

    aesthetics-of-everyday 判例：H0 `&ldquo;&thinsp;&lsquo;` 对装配侧
    `&ldquo; &lsquo;`——C 把 &thinsp; 折成空格，属格式层差，可入池。"""
    return WS_RE.sub("", htmllib.unescape(_strip_cmt(s)))


ENT_TOK_RE = re.compile(r"&[A-Za-z#0-9]+;|[\s\S]")


def seg_sha(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:16]


def _tok_spans(s):
    """实体为原子 token 的 (起, 止, 文) 序列——字符级 diff 会把 `&thinsp;`
    错切到分号外（`;&thinsp` 对 `` 判不等），实体原子化后不会。"""
    return [(m.start(), m.end(), m.group(0))
            for m in ENT_TOK_RE.finditer(s)]


def ent_spans(raw_a, raw_b):
    """两段原文的实体形态差 → [[pos, 原形, 新形]]（解码后等值才可入账）。

    返回 None 表示差值含真实文字（不可入池）。空白类差（&thinsp; 等）按
    排版空白等值处理，记入补丁由装配侧回写。"""
    if raw_a == raw_b:
        return []
    if _ws_decoded(raw_a) != _ws_decoded(raw_b):
        return None
    ta, tb = _tok_spans(raw_a), _tok_spans(raw_b)
    ka = [x[2] for x in ta]
    kb = [x[2] for x in tb]
    sm = difflib.SequenceMatcher(None, ka, kb, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        pos = ta[i1][0] if i1 < len(ta) else len(raw_a)
        before = raw_a[ta[i1][0]:ta[i2 - 1][1]] if i2 > i1 else ""
        after = raw_b[tb[j1][0]:tb[j2 - 1][1]] if j2 > j1 else ""
        if _ws_decoded(before) != _ws_decoded(after):
            return None
        out.append([pos, before, after])
    return out


def _ent_marks(es):
    """实体差 → b 流区间表 [(b_start, b_end, a_pos, len_before, after)]。"""
    marks, acc = [], 0
    for pos, before, after in sorted(es or [], key=lambda e: e[0]):
        b_start = pos + acc
        marks.append((b_start, b_start + len(after), pos, len(before), after))
        acc += len(after) - len(before)
    return marks


def _b_to_a(y, marks):
    """b 流坐标 → a 流（装配侧 plain）坐标；插入段内部映射到插入点。"""
    x = y
    for b_start, b_end, a_pos, lb, _a in marks:
        if y < b_start:
            break
        if y < b_end:
            return a_pos
        x -= (b_end - b_start) - lb
    return x


def layout_items(text, es=None):
    """文字段布局：mk（标记、空白、实体差异片段）＋ tx（引装配侧 plain 流切片）。

    实体形态差按 b 流区间切开：after 片段直接以 mk 落地，被 before 覆盖的
    a 侧片段自然不被任何 tx 引用。"""
    marks = _ent_marks(es)
    items, pos = [], 0
    for m in TOKEN_RE.finditer(text):
        tk = m.group(0)
        if tk.startswith("<"):
            items.append(["mk", tk])
            continue
        for sm in WS_SPLIT_RE.finditer(tk):
            piece = sm.group(0)
            if piece.isspace():
                # 空白是布局不是文字（H0 的段间空行、缩进、词间空格形态）
                items.append(["mk", piece])
                continue
            y0, y1 = pos, pos + len(piece)
            y = y0
            for b_start, b_end, a_pos, lb, after in marks:
                if b_end <= y:
                    continue
                if b_start >= y1:
                    break
                seg_end = min(b_start, y1)
                if seg_end > y:
                    a0, a1 = _b_to_a(y, marks), _b_to_a(seg_end, marks)
                    if a1 > a0:
                        items.append(["tx", a0, a1 - a0])
                items.append(["mk", after])
                y = max(y, b_end)
            if y < y1:
                a0, a1 = _b_to_a(y, marks), _b_to_a(y1, marks)
                if a1 > a0:
                    items.append(["tx", a0, a1 - a0])
            pos = y1
    return items


def _sub_diff(A, B, offA, a_lo, a_hi, b_lo, b_hi, patches):
    """区间内二级对齐：raw 段键 difflib → 非 equal 块生成 u/r 补丁。

    区间内文字流已对齐（token 级相同），块级键流检查仍按 ukey 硬校验；
    返回 False 即文字层差异（拒录）。"""
    ka = [(k, t) for k, t in A[a_lo:a_hi]]
    kb = [(k, t) for k, t in B[b_lo:b_hi]]
    sm = difflib.SequenceMatcher(None, ka, kb, autojunk=len(ka) > 4000)
    ops = list(sm.get_opcodes())
    i = 0
    while i < len(ops):
        tag, i1, i2, j1, j2 = ops[i]
        if tag == "equal":
            i += 1
            continue
        ai1, ai2 = a_lo + i1, a_lo + i2
        bj1, bj2 = b_lo + j1, b_lo + j2
        # 贪心合并：raw 段键对齐会把“A 一段 = B 多段”切成半截（c14 判例），
        # 块内 ukey 流不等时向后吞并相邻块（含 equal），直到文字流相等
        while True:
            ua = "".join(ukey(t) for k, t in A[ai1:ai2] if k == "u")
            ub = "".join(ukey(t) for k, t in B[bj1:bj2] if k == "u")
            if ua == ub:
                break
            i += 1
            if i >= len(ops):
                return False
            ai2 = a_lo + ops[i][2]
            bj2 = b_lo + ops[i][4]
        a_txt = "".join(t for _, t in A[ai1:ai2])
        b_txt = "".join(t for _, t in B[bj1:bj2])
        i += 1
        if a_txt == b_txt:
            continue
        start = offA[ai1] if ai1 < len(A) else offA[-1] + len(A[-1][1])
        if not ua:
            patches.append({"r": start, "len": len(a_txt),
                            "sha": seg_sha(a_txt), "after": b_txt})
            continue
        es = ent_spans(plain(a_txt), plain(b_txt))
        if es is None:
            return False
        patches.append({"u": start, "len": len(a_txt), "sha": seg_sha(a_txt),
                        "items": layout_items(b_txt, es)})
    return True


def diff_page(assembled, target):
    """→ (patches, gap)；gap 非空＝文字层差异（不可入池）。

    段对齐模型（P1 的区间形态）：
    ① 段数相同时逐段比较（绝大多数件，O(n)）：m 段原文替换、u 段按 ukey
       等值 + 实体差入账；某对文字不等即整页回退到 ②。
    ② 整页 raw 段键 difflib：非 equal 块整段替换，块内 ukey 流不等时贪心
       向后吞并相邻块（段落分合、松散列表 <li><p>、dl、多段合并等边界错位），
       文字流相等才入池；纯布局差走 r 补丁。区间按段索引顺序推进，互不
       重叠（重叠会让先应用的补丁改动后续区间，sha 失配）。"""
    A = segments(assembled)
    B = segments(target)
    offA = []
    acc = 0
    for _, t in A:
        offA.append(acc)
        acc += len(t)
    patches = []
    if len(A) == len(B):
        ok = True
        for i in range(len(A)):
            (ka_, ta), (kb_, tb) = A[i], B[i]
            if ta == tb:
                continue
            if ka_ == "m" and kb_ == "m":
                patches.append({"m": offA[i], "len": len(ta),
                                "sha": seg_sha(ta), "after": tb})
                continue
            if ka_ != "u" or kb_ != "u" or ukey(ta) != ukey(tb):
                ok = False
                break
            es = ent_spans(plain(ta), plain(tb))
            if es is None:
                ok = False
                break
            patches.append({"u": offA[i], "len": len(ta),
                            "sha": seg_sha(ta),
                            "items": layout_items(tb, es)})
        if ok:
            return patches, None
        patches = []
    if _sub_diff(A, B, offA, 0, len(A), 0, len(B), patches):
        return patches, None
    return None, {"why": "unaligned text units", "asm": assembled[:220],
                  "tgt": target[:220]}


def _rebuild(items, base):
    """按布局项重建文字段：mk 原样，tx 引 base（装配侧 plain 流）切片。

    实体形态差已由 layout_items 折进 mk（after 片段）与 tx 的 a 侧区间
    选择，故此层无额外状态；切片越界即补丁与文字流不符，报 PatchMiss。"""
    out = []
    for it in items:
        if it[0] == "mk":
            out.append(it[1])
            continue
        st, ln = it[1], it[2]
        if st < 0 or st + ln > len(base):
            raise PatchMiss("tx out of range")
        out.append(base[st:st + ln])
    return "".join(out)


def apply_patches(text, patches):
    """补丁一律按**字符偏移**降序应用（位移安全，m/u/r 同模型）。

    旧实现混用段索引与字符偏移，且 r 分支取 p["n"]（补丁里根本没有该键）
    ——r 与 m/u 并存时必错位。现统一：每补丁记 [偏移, 长度, 原形哈希]，
    校验哈希后整段替换。u 补丁的覆盖区间可跨标记段（松散列表、多段合并
    等布局族），前提是区间文字键流拼接相等（P1 的区间形态）。"""
    ops = []
    for p in patches:
        key = "u" if "u" in p else ("r" if "r" in p else "m")
        ops.append((p[key], key, p))
    for start, key, p in sorted(ops, key=lambda x: -x[0]):
        ln = p.get("len", 0)
        if start < 0 or start + ln > len(text):
            raise PatchMiss("%s out of range at %d" % (key, start))
        seg = text[start:start + ln]
        if seg_sha(seg) != p["sha"]:
            raise PatchMiss("%s segment hash mismatch at %d" % (key, start))
        new = (_rebuild(p["items"], plain(seg))
               if key == "u" else p["after"])
        text = text[:start] + new + text[start + ln:]
    return text


def pool_path(slug):
    return repo_path(*POOL_DIR, "%s.json" % slug)


def load_pool(slug):
    p = pool_path(slug)
    if not os.path.exists(p):
        return []
    return json.load(io.open(p, encoding="utf-8"))["patches"]


def write_pool(slug, patches, stats):
    os.makedirs(repo_path(*POOL_DIR), exist_ok=True)
    payload = {"schema": SCHEMA, "slug": slug,
               "generated_by": "specs/053 bin/assembly_pool.py",
               "note": "格式层残差补丁：m=标记段、u=单元布局、r=纯布局区段；禁含散文",
               "stats": stats, "patches": patches}
    with io.open(pool_path(slug), "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")


def remove_pool(slug):
    p = pool_path(slug)
    if os.path.exists(p):
        os.remove(p)


class PatchMiss(Exception):
    pass


def pool_bytes(patches):
    n = 0
    for p in patches:
        if "m" in p or "r" in p:
            n += len(p["after"])
        else:
            for it in p.get("items", []):
                n += len(it[1]) if it[0] == "mk" else 6
    return n
