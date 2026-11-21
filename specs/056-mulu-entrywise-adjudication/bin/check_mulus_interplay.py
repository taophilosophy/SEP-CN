#!/usr/bin/env python3
"""mu-lu-s 几方互转专项检查（只读）。

几方：mu-lu-s.md（正文）／baseline/mulu-map.json（归类账＋骨架）／SUMMARY.md（路径与文字源）。
检查项：
  I1 往返恒等：文件 → 抽账 → 重放 → 与文件逐字节比较
  I2 账内一致性：order 连续、indent 合法、path 唯一、kind 统计、骨架锚合法
  I3 文字跟随：账内文字 vs SUMMARY 文字（转义归一）
  I4 负向探针：对账做单点微扰，重放必须产生可测差异（判据非空转）
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MULU = ROOT / "mu-lu-s.md"
MAP = ROOT / "baseline/mulu-map.json"
SUMMARY = ROOT / "SUMMARY.md"

LINK_RE = re.compile(r"^(\s*)\* \[(.+?)\]\(([^()]+)\)\s*$")
GROUP_RE = re.compile(r"^(\s*)\* \\\*(.+?)\s*$")

def read(p):
    return p.read_text(encoding="utf-8")

def build(doc_text):
    """复刻 build_mulu 的抽账逻辑（只读内存，不写盘）。"""
    rows, skeleton, order = [], [], 0
    for l in doc_text.split("\n"):
        m = LINK_RE.match(l)
        g = GROUP_RE.match(l)
        if m:
            rows.append({"kind": "link", "path": m.group(3), "text": m.group(2),
                         "indent": len(m.group(1)), "order": order})
            order += 1
        elif g:
            rows.append({"kind": "group", "text": g.group(2), "indent": len(g.group(1)),
                         "order": order})
            order += 1
        else:
            skeleton.append([order, l])
    fixed, tail = [], []
    for a, t in skeleton:
        (tail if a >= order else fixed).append([a, t] if a < order else t)
    return {"rows": rows, "skeleton": {"fixed_rows": fixed,
                                       "head": [t for a, t in fixed if a == 0], "tail": tail}}

def unesc(s):
    return s.replace("\\[", "[").replace("\\]", "]").replace("\\*", "*")

def replay(doc, spt):
    fixed = {}
    for a, t in doc["skeleton"]["fixed_rows"]:
        fixed.setdefault(a, []).append(t)
    out = []
    for r in doc["rows"]:
        out.extend(fixed.get(r["order"], []))
        ind = " " * r["indent"]
        if r["kind"] == "link":
            out.append("%s* [%s](%s)" % (ind, r["text"], r["path"]))
        else:
            out.append("%s* \\*%s" % (ind, r["text"]))
    out.extend(doc["skeleton"]["tail"])
    return "\n".join(out)

def summary_paths(text):
    out = {}
    for l in text.split("\n"):
        m = LINK_RE.match(l)
        if m:
            out.setdefault(m.group(3), m.group(2))
    return out

def main():
    doc_text = read(MULU)
    on_disk = json.loads(read(MAP))
    spt = summary_paths(read(SUMMARY))
    fails = []

    # ---- I1 往返恒等（磁盘账 vs 现抽账 vs 重放）----
    fresh = build(doc_text)
    r_disk = replay(on_disk, spt)
    r_fresh = replay(fresh, spt)
    i1 = {"replay_disk_eq_file": r_disk == doc_text,
          "replay_fresh_eq_file": r_fresh == doc_text,
          "disk_account_eq_fresh": (on_disk["rows"] == fresh["rows"]
                                    and on_disk["skeleton"] == fresh["skeleton"])}
    if not all(i1.values()):
        fails.append("I1")
    # 差异定位（若不等）
    diff1 = []
    if r_disk != doc_text:
        a, b = r_disk.split("\n"), doc_text.split("\n")
        for k in range(max(len(a), len(b))):
            x = a[k] if k < len(a) else "<EOF>"
            y = b[k] if k < len(b) else "<EOF>"
            if x != y:
                diff1.append({"line": k + 1, "replay": x[:120], "file": y[:120]})
                if len(diff1) >= 5:
                    break

    # ---- I2 账内一致性 ----
    rows = on_disk["rows"]
    orders = [r["order"] for r in rows]
    paths = [r["path"] for r in rows if r["kind"] == "link"]
    anchors = [a for a, _ in on_disk["skeleton"]["fixed_rows"]]
    i2 = {
        "rows": len(rows),
        "links": len(paths),
        "groups": sum(1 for r in rows if r["kind"] == "group"),
        "order_continuous": orders == list(range(len(rows))),
        "indent_values": dict(Counter(r["indent"] for r in rows)),
        "duplicate_paths": [p for p, c in Counter(paths).items() if c > 1],
        "anchor_out_of_range": [a for a in anchors if a < 0 or a >= len(rows)],
        "anchor_monotonic": anchors == sorted(anchors),
    }
    if (not i2["order_continuous"] or i2["duplicate_paths"]
            or i2["anchor_out_of_range"] or not i2["anchor_monotonic"]):
        fails.append("I2")

    # ---- I3 文字跟随 ----
    follow = [r["path"] for r in rows if r["kind"] == "link"
              and (r["path"] not in spt or unesc(r["text"]) != unesc(spt[r["path"]]))]
    missing = [r["path"] for r in rows if r["kind"] == "link" and r["path"] not in spt]
    i3 = {"follow_mismatch": len(follow), "summary_missing": len(missing),
          "samples": follow[:5] + missing[:5]}
    if follow or missing:
        fails.append("I3")

    # ---- I4 负向探针（判据有效性的反证）----
    probes = {}
    base = replay(on_disk, spt)

    def mutate(fn, name):
        d = json.loads(json.dumps(on_disk))
        fn(d)
        probes[name] = replay(d, spt) != base

    def m_text(d):
        for r in d["rows"]:
            if r["kind"] == "link":
                r["text"] = r["text"] + "微扰"
                return

    def m_indent(d):
        for r in d["rows"]:
            if r["kind"] == "link":
                r["indent"] = (r["indent"] + 2) % 4
                return

    def m_swap(d):
        links = [r for r in d["rows"] if r["kind"] == "link"]
        a, b = links[10], links[20]
        a["path"], b["path"] = b["path"], a["path"]
        a["text"], b["text"] = b["text"], a["text"]

    def m_skeleton(d):
        d["skeleton"]["fixed_rows"][5][1] = d["skeleton"]["fixed_rows"][5][1] + "X"

    def m_delete(d):
        d["rows"].pop(100)
        for k, r in enumerate(d["rows"]):
            r["order"] = k

    for fn, name in [(m_text, "text"), (m_indent, "indent"), (m_swap, "swap"),
                     (m_skeleton, "skeleton"), (m_delete, "delete")]:
        mutate(fn, name)
    if not all(probes.values()):
        fails.append("I4")

    print(json.dumps({
        "I1_roundtrip": i1, "I1_diff_sample": diff1,
        "I2_account": i2, "I3_follow": i3, "I4_probes_detected": probes,
        "fails": fails,
    }, ensure_ascii=False, indent=1))
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
