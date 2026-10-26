# -*- coding: utf-8 -*-
"""原始 HTML → 带节号块序列文本（零信任 II：同输入必得同输出，可复算复核）。

用法: python tools/extract_text.py <slug>... [--to <输出路径>]
输出: stdout JSON {slug, source, sha256_in, sha256_out, blocks}
产物: en/<slug>.txt
"""
import argparse
import json
import sys

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import parser
from tools.common import load_json, read_text, repo_path, utcnow_iso, write_json_verified, write_text, sha256_file


def render_blocks(entry):
    lines = []
    for b in entry["blocks"]:
        t = b["type"]
        if t == "pubinfo":
            line = "[PUBINFO] First published %s; substantive revision %s" % (
                b["first_published"], b["substantive_revision"] or "(same)")
        elif t in ("h2", "h3", "h4"):
            text = b["text"]
            sec = b.get("section")
            if sec and text.startswith(sec + "."):
                text = text[len(sec) + 1:].strip()
            line = "[%s] %s%s" % (t.upper(), (sec + " ") if sec else "", text)
            if b.get("anchor"):
                line += " <#%s>" % b["anchor"]
        elif t == "img":
            line = "[FIGURE] %s | src=%s | alt=%s" % (
                b.get("figlabel", "(unlabelled)"), b.get("src", ""), b.get("alt", ""))
        elif t in ("li", "dt", "dd"):
            line = "[%s] %s" % (t.upper(), b["text"])
        else:
            line = "[%s] %s" % (t.upper(), b.get("text", ""))
        lines.append(line)
    return "\n\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="+")
    ap.add_argument("--to", default=None, help="单词条时指定输出路径")
    args = ap.parse_args(argv)

    results = []
    for slug in args.slugs:
        src = repo_path("en", slug, "index.html")
        try:
            html = read_text(src)
        except FileNotFoundError:
            results.append({"slug": slug, "error": "source not found: %s（先运行 fetch_entry.py）" % src})
            continue
        sha_in = sha256_file(src)
        entry = parser.parse_entry(html)
        text = render_blocks(entry)
        out = args.to or repo_path("en", "%s.txt" % slug)
        write_text(out, text)
        sha_out = sha256_file(out)
        results.append({"slug": slug, "source": "en/%s/index.html" % slug,
                        "sha256_in": sha_in, "sha256_out": sha_out,
                        "blocks": len(entry["blocks"]), "out": out, "at": utcnow_iso()})
    print(json.dumps({"results": results}, ensure_ascii=False, indent=2))
    return 1 if any("error" in r for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
