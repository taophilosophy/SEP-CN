# -*- coding: utf-8 -*-
"""目录域装配器（specs/054）：contents.html ⇄ 账⊕规则⊕池 的双向验证。

--build 从钉存快照生成两账并冻结（oracle 只读，不写回 en/_catalog/）：
  baseline/catalog-skeleton.json   页面模板账（fixed_rows 锚点行 + tail 行）
  baseline/catalog-residual.json   行级噪声池（kind 准入谓词，A5：池只收形态残差）

重放（默认）：baseline/catalog.json ⊕ 骨架账 ⊕ 池 → 逐字节装配 contents.html；
--check 与指定钉存快照 sha256 对比，全等退出 0（B3.2 装配全等）。
--build-account 从任意快照产临时账（供 A3 跨时点装配，不落 baseline/）。

输出：人读进度 stderr，结果 JSON stdout；退出码 0 全等/成功 / 1 失败 / 2 用法。
"""
import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import parser  # noqa: E402
from tools.common import load_json, repo_path, write_json_verified  # noqa: E402
from html.entities import codepoint2name  # noqa: E402

SKELETON_PATH = ("baseline", "catalog-skeleton.json")
RESIDUAL_PATH = ("baseline", "catalog-residual.json")
ALLOWED_KINDS = ("trailing-space", "inline-markup", "no-close-li", "entity-encoding")


def enc(t):
    """实体编码策略（实测闭合）：HTML4 命名实体优先，无名码点十进制兜底。"""
    out = []
    for ch in t:
        o = ord(ch)
        if ch == "&":
            out.append("&amp;")
        elif ch == "<":
            out.append("&lt;")
        elif ch == ">":
            out.append("&gt;")
        elif o in codepoint2name:
            out.append("&%s;" % codepoint2name[o])
        elif o > 127:
            out.append("&#%d;" % o)
        else:
            out.append(ch)
    return "".join(out)


def render_event(ev):
    """事件 → 规则渲染行（池外的唯一行来源）。"""
    if "slug" not in ev and "label" in ev:                       # 簇母行
        return ("   " if ev.get("level") == 2 else "") + "<li> " + enc(ev["label"])
    if "href_text" in ev:                                        # 别名行
        indent = "   " if ev.get("level") == 2 else ""
        return "%s<li> %s &mdash; see <a href=\"entries/%s/\">%s</a> </li>" % (
            indent, enc(ev["label"]), ev["slug"], enc(ev.get("href_text") or ""))
    it = ev                                                      # 正典条目行
    indent = "   " if it.get("level") == 2 else ""
    core = "<li> <a href=\"entries/%s/\"><strong>%s</strong></a>" % (it["slug"], enc(it["title"]))
    if it.get("authors"):
        core += " (%s)" % enc(it["authors"])
    return indent + core + " </li>"


def strip_variants(got, want):
    """A5 准入谓词（组合枚举）：存在 ALLOWED_KINDS 子集 S，使双方按 S 同构规范化后
    逐字节相等。返回 kind 元组（空=逐字节全等）或 None（谓词外差异，停线）。

    kind：trailing-space（链接/strong 尾随空格）、inline-markup（内联 <em>）、
          no-close-li（行尾闭合标签缺失）、entity-encoding（实体 vs 字面 UTF-8）。
    """
    import itertools
    from html import unescape as _un

    def norm(s, kind):
        if kind == "trailing-space":
            return s.replace(" </strong>", "</strong>").replace(" </a>", "</a>")
        if kind == "inline-markup":
            return s.replace("<em>", "").replace("</em>", "")
        if kind == "no-close-li":
            return re.sub(r"\s*</li>\s*$", "", s)
        if kind == "entity-encoding":
            return _un(s)
        return s

    for r in range(len(ALLOWED_KINDS) + 1):
        for combo in itertools.combinations(ALLOWED_KINDS, r):
            a, b = got, want
            for kind in combo:
                a = norm(a, kind)
                b = norm(b, kind)
            if a == b:
                return combo
    return None


def events_from_account(account):
    evs = (list(account["items"]) + list(account["alias_rows"])
           + list(account["cluster_mothers"]))
    evs.sort(key=lambda x: x["doc_order"])
    return evs


def align_events(lines, events):
    """推进对齐（纯函数）：事件流向后扫谓词匹配行。

    返回 (resid, skeleton, tail, unmatched)——resid=[{doc_order,slug,kind,line}]、
    skeleton=[[anchor_doc_order, text]]、tail=[行]、unmatched=[{doc_order,slug,want}]。
    """
    resid, skeleton, unmatched = [], [], []
    k = 0
    for ev in events:
        want = render_event(ev)
        j = k
        found = None
        while j < len(lines):
            got = lines[j]
            if 'href="entries/' in got or ("slug" not in ev and re.match(r"^\s*<li> ", got)):
                kinds = strip_variants(got, want)
                if kinds is not None:
                    found = (j, kinds)
                    break
            j += 1
        if found is None:
            unmatched.append({"doc_order": ev["doc_order"],
                              "slug": ev.get("slug", ev.get("label")), "want": want})
            k += 1
            continue
        j, kinds = found
        for kk in range(k, j):
            skeleton.append([ev["doc_order"], lines[kk]])
        k = j + 1
        if kinds:
            resid.append({"doc_order": ev["doc_order"], "slug": ev.get("slug"),
                          "kind": sorted(kinds), "line": lines[j]})
        else:
            pass
    tail = lines[k:]
    return resid, skeleton, tail, unmatched


def build(snap_path, skeleton_out=None, residual_out=None):
    """推进对齐：产骨架账＋残差池（冻结）。skeleton_out/residual_out 为相对路径
    （'/' 分段），默认 baseline 固定路径；跨时点装配产独立时点账到 results/。"""
    text = open(snap_path, "rb").read().decode("utf-8")
    lines = text.split("\n")
    full = parser.parse_catalog_full(text)
    events = events_from_account(full)
    resid, skeleton, tail, unmatched = align_events(lines, events)
    if unmatched:
        print(json.dumps({"error": "UNMATCHED/谓词外残差", "items": unmatched[:20],
                          "count": len(unmatched)}, ensure_ascii=False, indent=1))
        return 1
    skel_doc = {"source_snapshot": os.path.basename(snap_path),
                "fixed_rows": skeleton, "tail": tail}
    resid_doc = {"source_snapshot": os.path.basename(snap_path),
                 "count": len(resid), "entries": resid}
    skel_path = tuple(skeleton_out.split("/")) if skeleton_out else SKELETON_PATH
    resid_path = tuple(residual_out.split("/")) if residual_out else RESIDUAL_PATH
    write_json_verified(repo_path(*skel_path), skel_doc)
    write_json_verified(repo_path(*resid_path), resid_doc)
    exact = len(events) - len(resid)
    print(json.dumps({"exact": exact, "residual_count": len(resid),
                      "fixed_rows": len(skeleton), "tail_lines": len(tail),
                      "skeleton": "/".join(skel_path),
                      "residual": "/".join(resid_path)}, ensure_ascii=False))
    return 0


def build_account(snap_path, out_path):
    """从快照产临时账（A3 跨时点装配用；不写 baseline/）。"""
    text = open(snap_path, "rb").read().decode("utf-8")
    full = parser.parse_catalog_full(text)
    doc = {"fetched_at": None, "source": "en/_catalog/" + os.path.basename(snap_path),
           "items": sorted(full["items"], key=lambda x: x["slug"]),
           "alias_rows": sorted(full["alias_rows"], key=lambda x: x["doc_order"]),
           "cluster_mothers": sorted(full["cluster_mothers"], key=lambda x: x["doc_order"])}
    write_json_verified(out_path, doc)
    print(json.dumps({"account": out_path, "items": len(doc["items"]),
                      "alias_rows": len(doc["alias_rows"]),
                      "cluster_mothers": len(doc["cluster_mothers"])}, ensure_ascii=False))
    return 0


def rebuild(account, skel_doc, resid_doc):
    """账⊕规则⊕池 → 装配行流（纯函数；不写任何文件）。"""
    events = events_from_account(account)
    fixed = {}
    for anchor, textline in skel_doc["fixed_rows"]:
        fixed.setdefault(anchor, []).append(textline)
    pool = {e["doc_order"]: e for e in resid_doc["entries"]}
    out = []
    for ev in events:
        do = ev["doc_order"]
        out.extend(fixed.get(do, []))
        if do in pool:
            out.append(pool[do]["line"])
        else:
            out.append(render_event(ev))
    out.extend(skel_doc["tail"])
    return "\n".join(out)


def _basename_any(text):
    """双分隔符 basename（Windows 绝对路径在 Linux CI 上 os.path.basename 不切分）。"""
    return os.path.basename(str(text).replace("\\", "/"))


def compute(snap_path, account_path=None, skeleton_path=None, residual_path=None):
    """纯判定层：返回结果 dict（不打印、不写文件）；供 --check 与四向门 G1 复用。"""
    text = open(snap_path, "rb").read().decode("utf-8")
    account = load_json(repo_path(*account_path)) if account_path else \
        load_json(repo_path("baseline", "catalog.json"))
    if account.get("source") and \
            _basename_any(account["source"]) != os.path.basename(snap_path):
        return {"equal": False, "error": "账与快照不同时点",
                "account_source": _basename_any(account["source"]),
                "snapshot": os.path.basename(snap_path)}
    skel_doc = load_json(repo_path(*skeleton_path)) if skeleton_path else \
        load_json(repo_path(*SKELETON_PATH))
    resid_doc = load_json(repo_path(*residual_path)) if residual_path else \
        load_json(repo_path(*RESIDUAL_PATH))
    rebuilt = rebuild(account, skel_doc, resid_doc)
    h_rb = hashlib.sha256(rebuilt.encode("utf-8")).hexdigest()
    h_snap = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return {"equal": h_rb == h_snap, "sha_rebuilt": h_rb, "sha_snapshot": h_snap,
            "snapshot": os.path.basename(snap_path),
            "residual_used": resid_doc.get("count")}


def check(snap_path, account_path, skeleton_path=None, residual_path=None):
    res = compute(snap_path, account_path, skeleton_path, residual_path)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0 if res.get("equal") else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true",
                    help="从钉存快照生成骨架账＋残差池（冻结）")
    ap.add_argument("--snap", default=None, help="指定快照文件名（en/_catalog 下）")
    ap.add_argument("--build-account", action="store_true",
                    help="从快照产临时账（--out 指定输出，A3 跨时点）")
    ap.add_argument("--out", default=None, help="--build-account 输出路径")
    ap.add_argument("--check", action="store_true", help="重放并 sha256 对比快照")
    ap.add_argument("--account", default=None, help="--check 用账（默认 baseline/catalog.json）")
    ap.add_argument("--skeleton-out", default=None,
                    help="--build 骨架账输出相对路径（默认 baseline/catalog-skeleton.json）")
    ap.add_argument("--residual-out", default=None,
                    help="--build 残差池输出相对路径（默认 baseline/catalog-residual.json）")
    ap.add_argument("--skeleton", default=None, help="--check 骨架账相对路径（跨时点）")
    ap.add_argument("--residual", default=None, help="--check 残差池相对路径（跨时点）")
    args = ap.parse_args(argv)

    snaps = sorted(n for n in os.listdir(repo_path("en", "_catalog"))
                   if n.endswith("-contents.html"))
    if not snaps:
        print(json.dumps({"error": "en/_catalog 无快照"}, ensure_ascii=False))
        return 1
    snap_name = args.snap if args.snap else snaps[-1]
    if args.snap and args.snap not in snaps:
        print(json.dumps({"error": "快照不存在: %s" % args.snap}, ensure_ascii=False))
        return 2
    snap_path = repo_path("en", "_catalog", snap_name)

    if args.build:
        return build(snap_path, args.skeleton_out, args.residual_out)
    if args.build_account:
        if not args.out:
            print(json.dumps({"error": "--build-account 需 --out"}, ensure_ascii=False))
            return 2
        return build_account(snap_path, args.out)
    if args.check:
        acc = tuple(args.account.split("/")) if args.account else None
        skel = tuple(args.skeleton.split("/")) if args.skeleton else None
        res = tuple(args.residual.split("/")) if args.residual else None
        return check(snap_path, acc, skel, res)
    print(json.dumps({"error": "需 --build / --build-account / --check 之一"}, ensure_ascii=False))
    return 2


if __name__ == "__main__":
    sys.exit(main())
