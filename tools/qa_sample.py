#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISO 5060 人工抽样计划（T173／CP-S14-21；ADR-0095）。

规则（rules/qa-scorecard.json sampling.manual）：
  H2 分层，每层至少 1 段；总量 >= max(20, 10%)；按 sha256(slug+段序号) 升序取；
  任一样本出现 Critical 即转全量复核（本工具只产计划，不判定）。
用法：python tools/qa_sample.py <zh-doc> [--json]
"""
import argparse
import hashlib
import json
import math
import os
import re
import sys


def _slug(path):
    return os.path.splitext(os.path.basename(path))[0]


def segments(text):
    """按 H2 分节，段=连续非空行块；返回 [{section, index, text}]。"""
    out, section, buf = [], "全文", []

    def flush():
        if buf:
            out.append({"section": section, "index": len(out),
                        "text": " ".join(buf).strip()})
            buf.clear()

    for line in text.split("\n"):
        if line.startswith("## "):
            flush()
            section = line[3:].strip()
            continue
        if line.startswith("# "):
            continue
        if line.strip():
            buf.append(line.strip())
        else:
            flush()
    flush()
    return out


def plan(path, text=None, min_ratio=0.1, min_segments=20):
    if text is None:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    slug = _slug(path)
    segs = segments(text)
    if not segs:
        return {"slug": slug, "total": 0, "target": 0, "selected": []}
    target = max(min_segments, int(math.ceil(len(segs) * min_ratio)))
    sections = {}
    for seg in segs:
        seg["hash"] = hashlib.sha256(
            ("%s:%d" % (slug, seg["index"])).encode("utf-8")).hexdigest()
        sections.setdefault(seg["section"], []).append(seg)
    selected = []
    for name in sections:
        selected.append(sorted(sections[name], key=lambda s: s["hash"])[0])
    picked = {s["index"] for s in selected}
    for seg in sorted(segs, key=lambda s: s["hash"]):
        if len(selected) >= target:
            break
        if seg["index"] not in picked:
            selected.append(seg)
            picked.add(seg["index"])
    selected.sort(key=lambda s: s["index"])
    return {
        "slug": slug,
        "total": len(segs),
        "target": target,
        "sections": len(sections),
        "selected": [{"section": s["section"], "index": s["index"],
                      "hash": s["hash"], "preview": s["text"][:40]} for s in selected],
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("doc")
    ap.add_argument("--min-ratio", type=float, default=0.1)
    ap.add_argument("--min-segments", type=int, default=20)
    args = ap.parse_args(argv)
    if not os.path.exists(args.doc):
        print(json.dumps({"error": "missing: %s" % args.doc}, ensure_ascii=False))
        return 2
    result = plan(args.doc, min_ratio=args.min_ratio, min_segments=args.min_segments)
    print(json.dumps(result, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
