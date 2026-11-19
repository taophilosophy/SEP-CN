#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""B3.2 页面级逆向装配判定器。

验收线（三档，逐件给出）：
  chrome_ok  页面骨架（head＋bodyPre＋post）由「骨架模板＋字段账」逐字节再生，
             正文段沿用 H0 原字节（隔离骨架证据）
  article_ok 正文段由 md 经 R（reassemble.reassemble_article）逐字节再生
  page_ok    sha256(render_page(md)) == sha256(en/<slug>/index.html)

同源求值纪律：正文段只经 specs/053 bin/reassemble.py 的 R；本脚本不重实现
转换语义。版式账（page-layout.json）与骨架（skeleton/）是冻结派生件。
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

LAYOUT_PATH = ("baseline", "en-template", "page-layout.json")
SKEL_DIR = ("baseline", "en-template", "skeleton")


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


class Library:
    def __init__(self):
        self.skel = {}
        p = repo_path(*LAYOUT_PATH)
        self.recs = {r["slug"]: r for r in json.load(
            io.open(p, encoding="utf-8"))["entries"]}

    def s(self, kind, eid):
        key = (kind, eid)
        if key not in self.skel:
            fn = repo_path(*SKEL_DIR, "%s-%s.html" % (kind, eid))
            self.skel[key] = io.open(fn, encoding="utf-8", newline="").read()
        return self.skel[key]


def render_page(lib, rec, article_seg):
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
    return head + pre + article_seg + post


def first_diff(a, b):
    pre = 0
    while pre < min(len(a), len(b)) and a[pre] == b[pre]:
        pre += 1
    return {"pos": pre, "h0": a[max(0, pre - 60):pre + 90],
            "asm": b[max(0, pre - 60):pre + 90]}


def judge(slug, lib, base, with_article=True):
    rec = lib.recs.get(slug)
    if not rec:
        return {"slug": slug, "skipped": "no layout"}
    p = repo_path("en", slug, "index.html")
    if not os.path.exists(p):
        return {"slug": slug, "skipped": "no en"}
    h0 = PL.read(p)
    sp = PL.split_page(h0)
    out = {"slug": slug, "page_len": len(h0)}
    page_chrome = render_page(lib, rec, sp["article"])
    out["chrome_ok"] = page_chrome == h0
    if not out["chrome_ok"]:
        out["chrome_diff"] = first_diff(h0, page_chrome)
    out["article_ok"] = False
    out["page_ok"] = False
    out["page_sha"] = sha(page_chrome) == sha(h0)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    args = ap.parse_args(argv)
    lib = Library()
    slugs = sorted(lib.recs) if args.all else (args.slugs or [])
    entries = []
    n_ch = 0
    for i, s in enumerate(slugs, 1):
        r = judge(s, lib, None)
        entries.append(r)
        n_ch += bool(r.get("chrome_ok"))
        if args.all and i % 200 == 0:
            sys.stderr.write("[b32] %d/%d chrome_ok=%d\n" % (i, len(slugs), n_ch))
            sys.stderr.flush()
    payload = {"schema": "sep-cn-b32-page/1",
               "generated_by": "specs/053 bin/page_assemble.py",
               "total": len(entries), "chrome_ok": n_ch,
               "chrome_fail": len(entries) - n_ch, "entries": entries}
    out = args.out or repo_path("specs", "053-en-template-audit", "results",
                                "page-scan.json")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sys.stderr.write("[b32] chrome 逐字节 %d/%d → %s\n"
                     % (n_ch, len(entries), out))
    return 0 if n_ch == len(entries) else 1


if __name__ == "__main__":
    sys.exit(main())
