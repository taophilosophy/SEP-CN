#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""B3.2 页面级逆向装配判定器（三档判定＋补集池构建）。

装配链（同源求值）：
  page = 骨架模板(head/pre/post) ＋ 字段账(page-layout) ⊕ 正文段
  正文段 = 结构账(article-ledger) ＋ R(md)（specs/053 bin/reassemble.py）
  验收   sha256(page ⊕ 补集池) == sha256(en/<slug>/index.html)

状态：
  rule   规则装配即逐字节相等（无需补集）
  pool   规则装配＋格式层补集池（可视文字等值谓词准入）后逐字节相等
  gap    仍有正文文字层差异（禁入池；须改规则或改账）
"""
import argparse
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tools.common import repo_path  # noqa: E402
import page_layout as PL  # noqa: E402
import article_build as AB  # noqa: E402
import assembly_pool as POOL  # noqa: E402
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "ra", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "reassemble.py"))
ra = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ra)

LAYOUT_PATH = ("baseline", "en-template", "page-layout.json")
SKEL_DIR = ("baseline", "en-template", "skeleton")
LEDGER_PATH = ("baseline", "en-template", "article-ledger.json")
B1 = "<!-- BEGIN ARTICLE HTML -->"
E1 = "<!-- END ARTICLE HTML -->"


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


class Library:
    def __init__(self):
        self.skel = {}
        self.recs = {r["slug"]: r for r in json.load(
            io.open(repo_path(*LAYOUT_PATH), encoding="utf-8"))["entries"]}
        self.led = json.load(io.open(
            repo_path(*LEDGER_PATH), encoding="utf-8"))["entries"]
        self.base = {r["slug"]: r for r in json.load(
            io.open(repo_path("baseline", "entries.json"),
                    encoding="utf-8"))["entries"] if r.get("slug")}

    def s(self, kind, eid):
        key = (kind, eid)
        if key not in self.skel:
            fn = repo_path(*SKEL_DIR, "%s-%s.html" % (kind, eid))
            self.skel[key] = io.open(fn, encoding="utf-8", newline="").read()
        return self.skel[key]


def render_chrome(lib, rec, article_seg):
    slug = rec["slug"]
    head = (lib.s("headA", rec["headA_id"]) + rec["title_html"]
            + lib.s("headmid", rec["era"]["headmid"])
            + PL.render_meta_block(rec)
            + lib.s("headrest", rec["era"]["headrest"]))
    pre = PL.deslotify(lib.s("pre", rec["era"]["pre"]), slug)
    post = PL.deslotify(lib.s("postrest", rec["era"]["postrest"]), slug)
    if "@CR@" in post:
        post = post.replace("@CR@", PL.render_copyright(
            rec["copyright_year"], rec["copyright_authors"]))
    post = post.replace("@SY@", rec["site_year"] or "")
    return head + pre + B1 + article_seg + E1 + post


def assemble(lib, slug):
    """→ (page, info)。page 为 None 表示装配链断（缺账/缺 md）。"""
    rec = lib.recs.get(slug)
    if not rec:
        return None, {"skipped": "no layout"}
    brec = lib.base.get(slug)
    md_path = repo_path("yuanwen", (brec or {}).get("zh_doc") or "")
    if not os.path.exists(md_path):
        return None, {"skipped": "no yuanwen md"}
    led = lib.led.get(slug) or {}
    md0 = io.open(md_path, encoding="utf-8").read().rstrip("\n")
    authors = [ra.html_unescape(a) for a in (rec.get("meta_authors") or [])]
    _t, flat = ra.reassemble_article(md0, authors, led.get("entities"),
                                     led.get("links"), led.get("greek"),
                                     led.get("italics"), led.get("greek_form"),
                                     led.get("note_forms"),
                                     led.get("math_forms"),
                                     led.get("math_dollars"),
                                     led.get("bq"),
                                     led.get("photo_pre_h1"),
                                     led.get("sup_pos"))
    miss = ra.link_misses()
    art = AB.build(flat, led)
    if art is None:
        return None, {"skipped": "article build failed"}
    info = {"article_len": len(art), "link_total": len(led.get("links") or []),
            "link_miss": len(miss)}
    if miss:
        info["miss_sample"] = [m["text"][:60] for m in miss[:3]]
    return render_chrome(lib, rec, art), info


def judge(lib, slug):
    p = repo_path("en", slug, "index.html")
    if not os.path.exists(p):
        return {"slug": slug, "status": "gap", "skipped": "no en"}
    h0 = PL.read(p)
    page, info = assemble(lib, slug)
    out = {"slug": slug, "page_len": len(h0)}
    if info.get("link_miss"):
        out["link_miss"] = info["link_miss"]
        out["miss_sample"] = info.get("miss_sample")
    if page is None:
        out["status"] = "gap"
        out["why"] = info.get("skipped")
        return out
    if page == h0:
        out["status"] = "rule"
        return out
    patches = POOL.load_pool(slug)
    if patches:
        try:
            pooled = POOL.apply_patches(page, patches)
        except POOL.PatchMiss as ex:
            out["status"] = "stale"
            out["why"] = str(ex)
            return out
        if pooled == h0:
            out["status"] = "pool"
            out["n_patches"] = len(patches)
            out["pool_bytes"] = POOL.pool_bytes(patches)
            return out
        out["why"] = "pool applied but not byte-equal"
    good, gap = POOL.diff_page(page, h0)
    out["status"] = "gap"
    if gap:
        out["why"] = gap.get("why")
        out["sample"] = {"asm": (gap.get("asm") or "")[:240],
                         "tgt": (gap.get("tgt") or "")[:240]}
    else:
        out["rule_patches"] = len(good)
    return out


def build_pool(lib, slug, dry=False):
    p = repo_path("en", slug, "index.html")
    if not os.path.exists(p):
        return None
    h0 = PL.read(p)
    page, info = assemble(lib, slug)
    if page is None:
        return {"slug": slug, "status": "gap", "why": info.get("skipped")}
    if page == h0:
        if not dry:
            POOL.remove_pool(slug)
        return {"slug": slug, "status": "rule", "n_patches": 0,
                "page_len": len(h0)}
    good, gap = POOL.diff_page(page, h0)
    if gap:
        # gap 意味着 A 侧已变（规则/账改动），旧池必失效——留着会让 judge
        # 持续报 stale（anarchism 判例：第三批旧池残留、本轮 28 件 stale）
        if not dry:
            POOL.remove_pool(slug)
        return {"slug": slug, "status": "gap", "why": gap.get("why"),
                "page_len": len(h0),
                "sample": {"asm": (gap.get("asm") or "")[:240],
                           "tgt": (gap.get("tgt") or "")[:240]}}
    pb = POOL.pool_bytes(good)
    # 自洽门：补丁必须能就地再生 H0（写坏池前拦下；judge 侧另有同式校验）
    try:
        if POOL.apply_patches(page, good) != h0:
            return {"slug": slug, "status": "gap", "why": "apply verify failed",
                    "page_len": len(h0),
                    "sample": {"asm": page[:240], "tgt": h0[:240]}}
    except POOL.PatchMiss as ex:
        return {"slug": slug, "status": "gap",
                "why": "patch miss: %s" % ex, "page_len": len(h0)}
    if not dry:
        POOL.write_pool(slug, good, {
            "page_bytes": len(page), "pool_bytes": pb,
            "n_patches": len(good)})
    return {"slug": slug, "status": "pool", "n_patches": len(good),
            "page_len": len(h0), "pool_bytes": pb}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--build", action="store_true", help="抽取/更新补集池")
    ap.add_argument("--dry", action="store_true", help="--build 时不落盘")
    ap.add_argument("--out")
    args = ap.parse_args(argv)
    lib = Library()
    slugs = sorted(lib.recs) if args.all else (args.slugs or [])
    entries = []
    cnt = {"rule": 0, "pool": 0, "gap": 0, "stale": 0}
    tot_page = tot_pool = 0
    for i, s in enumerate(slugs, 1):
        try:
            r = (build_pool(lib, s, args.dry) if args.build
                 else judge(lib, s))
        except Exception as ex:  # noqa: BLE001——单件异常不中断全量
            r = {"slug": s, "status": "gap", "why": "error: %s" % ex}
        entries.append(r)
        cnt[r.get("status", "gap")] = cnt.get(r.get("status", "gap"), 0) + 1
        tot_page += r.get("page_len") or 0
        tot_pool += r.get("pool_bytes") or 0
        if args.all and i % 200 == 0:
            sys.stderr.write("[b32] %d/%d %s\n" % (i, len(slugs), cnt))
            sys.stderr.flush()
    payload = {"schema": "sep-cn-b32-page/2",
               "generated_by": "specs/053 bin/page_assemble.py",
               "mode": "build-pool" if args.build else "judge",
               "total": len(entries), "counts": cnt,
               "page_bytes": tot_page, "pool_bytes": tot_pool,
               "entries": entries}
    out = args.out or repo_path("specs", "053-en-template-audit", "results",
                                "page-scan.json")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sys.stderr.write("[b32] %d 件：%s ｜池 %d B / 页 %d B (%.2f%%) → %s\n"
                     % (len(entries), cnt, tot_pool, tot_page,
                        100.0 * tot_pool / max(tot_page, 1), out))
    return 0 if cnt.get("gap", 0) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
