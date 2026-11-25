#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""术语表导出 TBX Core（DCT 风格）：GB/T 44227-2024（MOD ISO 30042:2019）；ADR-0086。

源（只读，不推断）：
  shu-yu-biao.md              键｜原文｜译法｜首现｜依据｜裁定日期
  baseline/term-concepts.md   键｜定义｜学科域｜概念关系｜依据｜裁定日期
字段映射（rules/10 §10.6）：键→conceptEntry/@id；原文→en term；译法→zh-Hans term；
定义→descrip type="definition"；学科域→descrip type="subjectField"；
概念关系→descrip type="relatedConcept"。

用法:
  python tools/term_tbx.py [--out PATH] [--registry PATH] [--concepts PATH]
退出码: 0 成功；2 输入缺失；3 数据错误（重复键／空键等）。
"""
import argparse
import os
import re
import sys
from xml.sax.saxutils import escape, quoteattr

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "shu-yu-biao.md")
CON = os.path.join(ROOT, "baseline", "term-concepts.md")
NS = "urn:iso:std:iso:30042:ed-2"
EMPTY = ("", "—", "-", "－")


def rows(path):
    """读 md 表格：返回 [{列名: 值}]（跳过表头与分隔行）。"""
    out, header = [], None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if header is None:
                header = cells
                continue
            if cells == header or cells[0] == "键":
                continue  # 分节重复表头
            if set("".join(cells)) <= set("-: "):
                continue
            out.append(dict(zip(header, cells)))
    return out


def _cell(row, name):
    v = str(row.get(name, "")).strip()
    return "" if v in EMPTY else v


def _ident(key, used):
    base = re.sub(r"[^\w.-]+", "-", key).strip("-") or "entry"
    if base[0].isdigit():
        base = "k" + base
    ident, n = base, 2
    while ident in used:
        ident = "%s-%d" % (base, n)
        n += 1
    used.add(ident)
    return ident


def concepts(reg_rows, con_rows=None):
    """合并两表，返回按键排序的概念记录列表。"""
    by_key = {}
    for r in reg_rows:
        key = _cell(r, "键")
        if not key:
            raise ValueError("术语表存在空键行: %r" % r)
        if key in by_key:
            raise ValueError("术语表键重复: %s" % key)
        by_key[key] = {"key": key, "source": _cell(r, "原文"), "target": _cell(r, "译法"),
                       "definition": "", "field": "", "relation": ""}
    for r in con_rows or []:
        key = _cell(r, "键")
        if not key:
            continue
        rec = by_key.setdefault(key, {"key": key, "source": "", "target": "",
                                      "definition": "", "field": "", "relation": ""})
        rec["definition"] = _cell(r, "定义") or rec["definition"]
        rec["field"] = _cell(r, "学科域") or rec["field"]
        rec["relation"] = _cell(r, "概念关系") or rec["relation"]
    return [by_key[k] for k in sorted(by_key)]


def render(items):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<tbx xmlns="%s" style="dct" type="TBX-Core" xml:lang="en">' % NS,
           "  <tbxHeader>",
           "    <fileDesc><sourceDesc><p>SEP-CN 术语表（shu-yu-biao.md＋baseline/term-concepts.md）</p></sourceDesc></fileDesc>",
           "  </tbxHeader>",
           "  <text>",
           "    <body>"]
    used = set()
    for rec in items:
        out.append('      <conceptEntry id=%s>' % quoteattr(_ident(rec["key"], used)))
        if rec["field"]:
            out.append('        <descrip type="subjectField">%s</descrip>' % escape(rec["field"]))
        if rec["definition"]:
            out.append('        <descrip type="definition">%s</descrip>' % escape(rec["definition"]))
        if rec["relation"]:
            out.append('        <descrip type="relatedConcept">%s</descrip>' % escape(rec["relation"]))
        if rec["source"]:
            out.append('        <langSec xml:lang="en"><termSec><term>%s</term></termSec></langSec>'
                       % escape(rec["source"]))
        if rec["target"]:
            out.append('        <langSec xml:lang="zh-Hans"><termSec><term>%s</term></termSec></langSec>'
                       % escape(rec["target"]))
        out.append("      </conceptEntry>")
    out += ["    </body>", "  </text>", "</tbx>"]
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", default=REG)
    ap.add_argument("--concepts", default=CON)
    ap.add_argument("--out", default="")
    args = ap.parse_args(argv)
    for p in (args.registry, args.concepts):
        if not os.path.exists(p):
            print("输入缺失: %s" % p, file=sys.stderr)
            return 2
    try:
        items = concepts(rows(args.registry), rows(args.concepts))
    except ValueError as e:
        print("数据错误: %s" % e, file=sys.stderr)
        return 3
    text = render(items)
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("已导出 %d 个概念 → %s" % (len(items), args.out))
    else:
        sys.stdout.write(text)
        print("已导出 %d 个概念" % len(items), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
