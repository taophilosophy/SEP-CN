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
WS_RE = re.compile(r"\s+")


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
    """文字段的无空白字符流（去标签、去空白与 &nbsp;，其余实体保留原形）。"""
    t = re.sub(r"<[^>]*>", "", text)
    t = t.replace("&nbsp;", "")
    return WS_RE.sub("", t)


def ukey(text):
    return plain(text)


def seg_sha(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:16]


def layout_items(text):
    """文字段布局：拆成 mk/tx 项，tx 以装配侧字符流的 [起,长] 引用。"""
    items, pos = [], 0
    for m in TOKEN_RE.finditer(text):
        tk = m.group(0)
        if tk.startswith("<"):
            items.append(["mk", tk])
            continue
        n = len(WS_RE.sub("", tk))
        items.append(["tx", pos, n])
        pos += n
    return items


def diff_page(assembled, target):
    """→ (patches, gap)；gap 非空＝文字层差异（不可入池）。"""
    A = segments(assembled)
    B = segments(target)
    offA = []
    acc = 0
    for _, t in A:
        offA.append(acc)
        acc += len(t)
    ia = [i for i, (k, _) in enumerate(A) if k == "u"]
    ib = [i for i, (k, _) in enumerate(B) if k == "u"]
    ka = [ukey(A[i][1]) for i in ia]
    kb = [ukey(B[i][1]) for i in ib]
    patches = []
    if ka == kb:
        # 快路：文字键序列完全相同（绝大多数件）——无需序列对齐
        for d in range(len(ia)):
            a_at, b_at = ia[d], ib[d]
            ta, tb = A[a_at][1], B[b_at][1]
            if ta == tb:
                continue
            patches.append({"u": offA[a_at], "len": len(ta),
                            "sha": seg_sha(ta), "items": layout_items(tb)})
        if len(A) == len(B):
            for i in range(len(A)):
                if A[i][0] == "m" and B[i][0] == "m" and A[i][1] != B[i][1]:
                    patches.append({"m": offA[i], "len": len(A[i][1]),
                                    "sha": seg_sha(A[i][1]), "after": B[i][1]})
        return patches, None
    sm = difflib.SequenceMatcher(None, ka, kb, autojunk=len(ka) > 2000)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for d in range(i2 - i1):
                a_at, b_at = ia[i1 + d], ib[j1 + d]
                ta, tb = A[a_at][1], B[b_at][1]
                if ta == tb:
                    continue
                if plain(ta) != plain(tb):
                    return None, {"why": "unit text mismatch",
                                  "asm": ta[:220], "tgt": tb[:220]}
                patches.append({"u": offA[a_at], "len": len(ta),
                                "sha": seg_sha(ta),
                                "items": layout_items(tb)})
            continue
        a_lo = ia[i1 - 1] + 1 if i1 > 0 else 0
        a_hi = ia[i2] if i2 < len(ia) else len(A)
        b_lo = ib[j1 - 1] + 1 if j1 > 0 else 0
        b_hi = ib[j2] if j2 < len(ib) else len(B)
        if any(ka[i1:i2]) or any(kb[j1:j2]):
            return None, {"why": "unaligned text units (%d/%d)" % (
                i2 - i1, j2 - j1),
                "asm": "".join(x for _, x in A[a_lo:a_hi])[:220],
                "tgt": "".join(x for _, x in B[b_lo:b_hi])[:220]}
        a_txt = "".join(x for _, x in A[a_lo:a_hi])
        b_txt = "".join(x for _, x in B[b_lo:b_hi])
        patches.append({"r": offA[a_lo] if a_lo < len(A) else len(assembled),
                        "len": len(a_txt), "sha": seg_sha(a_txt),
                        "after": b_txt})
    if len(A) == len(B):
        for i in range(len(A)):
            if A[i][0] == "m" and B[i][0] == "m" and A[i][1] != B[i][1]:
                patches.append({"m": offA[i], "len": len(A[i][1]),
                                "sha": seg_sha(A[i][1]), "after": B[i][1]})
    return patches, None


def apply_patches(text, patches):
    segs = segments(text)
    for p in sorted([x for x in patches if "r" in x], key=lambda x: -x["r"]):
        i, n = p["r"], p["n"]
        if i > len(segs) or i + n > len(segs):
            raise PatchMiss("r out of range")
        if seg_sha("".join(x for _, x in segs[i:i + n])) != p["sha"]:
            raise PatchMiss("r segment hash mismatch at %d" % i)
        segs[i:i + n] = [("m", p["after"])]
    for p in patches:
        if "m" in p:
            i = p["m"]
            if i >= len(segs) or segs[i][0] != "m" or \
                    seg_sha(segs[i][1]) != p["sha"]:
                raise PatchMiss("m slot %d mismatch" % i)
            segs[i] = ("m", p["after"])
        elif "u" in p:
            i = p["u"]
            if i >= len(segs) or segs[i][0] != "u" or \
                    seg_sha(segs[i][1]) != p["sha"]:
                raise PatchMiss("u slot %d mismatch" % i)
            base = plain(segs[i][1])
            out = []
            for it in p["items"]:
                if it[0] == "mk":
                    out.append(it[1])
                else:
                    out.append(base[it[1]:it[1] + it[2]])
            segs[i] = ("u", "".join(out))
    return "".join(x for _, x in segs)


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
