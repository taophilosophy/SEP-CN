#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""术语表导出／校验／迁移样本（TBX-Core；GB/T 44227-2024 MOD ISO 30042:2019；ADR-0086／ADR-0094）。

源（只读，不推断）：
  zh/shu-yu-biao.md           键｜原文｜译法｜首现｜依据｜裁定日期
  zh/ren-ming-biao.md         原文｜别名｜译法｜籍属｜生卒｜首现｜依据｜裁定日期
  baseline/term-concepts.md   键｜定义｜学科域｜概念关系｜依据｜裁定日期

用法:
  python tools/term_tbx.py [--out PATH]                 # 从三表导出 TBX
  python tools/term_tbx.py --check PATH                 # 校验 TBX（结构／必填／重复／状态）
  python tools/term_tbx.py --sample-out PATH --sample-views DIR [--sample-n 5]
                                                         # 生成迁移样本＋两表视图

退出码: 0 成功；1 校验失败；2 输入缺失；3 数据错误（重复键／空键等）。
"""
import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape, quoteattr

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "zh", "shu-yu-biao.md")
CON = os.path.join(ROOT, "baseline", "term-concepts.md")
NAME = os.path.join(ROOT, "zh", "ren-ming-biao.md")
NS = "urn:iso:std:iso:30042:ed-2"
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"
EMPTY = ("", "—", "-", "－")
STATUSES = ("candidate", "current", "deprecated")
VIEWS = ("shu-yu", "ren-ming")
DESCRIP_KEYS = {
    "definition": "definition",
    "subjectField": "field",
    "relatedConcept": "relation",
    "source": "source_ref",
    "context": "context",
    "grammar": "grammar",
    "crossReference": "crossref",
    "status": "status",
    "date": "date",
    "owner": "owner",
    "view": "view",
    "section": "section",
    "order": "order",
    "firstOccurrence": "first",
    "alias": "alias",
    "nationality": "nationality",
    "life": "life",
}
VIEW_COLUMNS = {
    "shu-yu": ["键", "原文", "译法", "首现", "依据", "裁定日期"],
    "ren-ming": ["原文", "别名", "译法", "籍属", "生卒", "首现", "依据", "裁定日期"],
}
HEADERS = {
    "shu-yu-biao.md": ["键", "原文", "译法", "首现（slug 或书目）", "依据", "裁定日期"],
    "ren-ming-biao.md": ["原文", "别名", "译法", "籍属", "生卒",
                         "首现（slug 或书目）", "依据", "裁定日期"],
    "term-concepts.md": ["键", "定义", "学科域", "概念关系", "依据", "裁定日期"],
}


def _default_header(path):
    return list(HEADERS.get(os.path.basename(path), []))


def rows(path):
    """读 md 表格：返回 [{列名: 值}]（跳过表头与分隔行）。"""
    out, header = [], _default_header(path) or None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if header is None:
                header = cells
                continue
            if cells == header or cells[0] in ("键", "原文"):
                continue  # 分节重复表头
            if set("".join(cells)) <= set("-: "):
                continue
            out.append(dict(zip(header, cells)))
    return out


def layout_rows(path):
    """读 md 表格并保留 `_section`（## 标题）与 `_order`，供迁移样本使用。"""
    out, header, section = [], _default_header(path) or None, ""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("## "):
                section = line[3:].strip()
                continue
            s = line.strip()
            if not s.startswith("|"):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if header is None:
                header = cells
                continue
            if cells == header or cells[0] in ("键", "原文"):
                continue
            if set("".join(cells)) <= set("-: "):
                continue
            rec = dict(zip(header, cells))
            rec["_section"] = section
            rec["_order"] = len(out)
            out.append(rec)
    return out


def _cell(row, name):
    v = str(row.get(name, "")).strip()
    return "" if v in EMPTY else v


def _col(row, name):
    """取列：兼容 `首现（slug 或书目）` 一类带括注的列名。"""
    if name in row:
        return _cell(row, name)
    for key in row:
        if str(key).startswith(name):
            return _cell(row, key)
    return ""


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


def _base(key, source, target, **kw):
    rec = {"key": key, "id": "", "source": source, "target": target,
           "definition": "", "field": "", "relation": "", "source_ref": "",
           "context": "", "grammar": "", "crossref": "", "status": "current",
           "date": "", "owner": "术语员", "view": "shu-yu", "section": "",
           "order": 0, "first": "", "alias": "", "nationality": "", "life": ""}
    rec.update(kw)
    return rec


def concepts(reg_rows, con_rows=None):
    """合并术语表与概念表，返回按 key 排序的概念记录（保持旧 API）。"""
    by_key = {}
    for r in reg_rows:
        key = _cell(r, "键")
        if not key:
            raise ValueError("术语表存在空键行: %r" % r)
        if key in by_key:
            raise ValueError("术语表键重复: %s" % key)
        by_key[key] = _base(key, _cell(r, "原文"), _cell(r, "译法"),
                            source_ref=_cell(r, "依据"), first=_col(r, "首现"),
                            date=_cell(r, "裁定日期"))
    for r in con_rows or []:
        key = _cell(r, "键")
        if not key:
            continue
        rec = by_key.get(key)
        if rec is None:
            rec = by_key[key] = _base(key, "", "")
        rec["definition"] = _cell(r, "定义") or rec["definition"]
        rec["field"] = _cell(r, "学科域") or rec["field"]
        rec["relation"] = _cell(r, "概念关系") or rec["relation"]
        rec["source_ref"] = _cell(r, "依据") or rec["source_ref"]
        rec["date"] = _cell(r, "裁定日期") or rec["date"]
    return [by_key[k] for k in sorted(by_key)]


def migrate_items(reg_layout, con_layout=None, name_layout=None, limit=5):
    """迁移样本：两表各取前 limit 行，转成 TBX 记录（含视图定位）。"""
    con_by_key = {_cell(r, "键"): r for r in (con_layout or []) if _cell(r, "键")}
    items, n_term, n_name = [], 0, 0
    for r in reg_layout:
        if n_term >= limit:
            break
        key = _cell(r, "键")
        if not key:
            continue
        rec = _base(key, _cell(r, "原文"), _cell(r, "译法"),
                    source_ref=_cell(r, "依据"), first=_col(r, "首现"),
                    date=_cell(r, "裁定日期"), view="shu-yu",
                    section=r.get("_section", ""), order=r.get("_order", 0))
        c = con_by_key.get(key)
        if c:
            rec["definition"] = _cell(c, "定义")
            rec["field"] = _cell(c, "学科域")
            rec["relation"] = _cell(c, "概念关系")
        items.append(rec)
        n_term += 1
    for r in name_layout or []:
        if n_name >= limit:
            break
        key = _cell(r, "原文")
        if not key:
            continue
        rec = _base(key, key, _cell(r, "译法"),
                    source_ref=_cell(r, "依据"), first=_col(r, "首现"),
                    date=_cell(r, "裁定日期"), view="ren-ming",
                    section=r.get("_section", ""), order=r.get("_order", 0),
                    alias=_cell(r, "别名"), nationality=_cell(r, "籍属"),
                    life=_cell(r, "生卒"))
        rec["definition"] = "人名条目"
        rec["field"] = "人名"
        items.append(rec)
        n_name += 1
    return items


def render(items):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<tbx xmlns="%s" style="dct" type="TBX-Core" xml:lang="en">' % NS,
           "  <tbxHeader>",
           "    <fileDesc><sourceDesc><p>SEP-CN 术语表（shu-yu-biao.md＋ren-ming-biao.md＋term-concepts.md）</p></sourceDesc></fileDesc>",
           "  </tbxHeader>",
           "  <text>",
           "    <body>"]
    used = set()
    for rec in items:
        ident = rec.get("id") or _ident(rec["key"], used)
        out.append('      <conceptEntry id=%s>' % quoteattr(ident))
        for typ in ("subjectField", "definition", "relatedConcept", "source", "context",
                    "grammar", "crossReference", "status", "date", "owner", "view",
                    "section", "order", "firstOccurrence", "alias", "nationality", "life"):
            key = DESCRIP_KEYS[typ]
            val = str(rec.get(key, "") or "").strip()
            if val and not (typ == "order" and val == "0"):
                out.append('        <descrip type="%s">%s</descrip>' % (typ, escape(val)))
        if rec.get("source"):
            out.append('        <langSec xml:lang="en"><termSec><term>%s</term></termSec></langSec>'
                       % escape(rec["source"]))
        if rec.get("target"):
            out.append('        <langSec xml:lang="zh-Hans"><termSec><term>%s</term></termSec></langSec>'
                       % escape(rec["target"]))
        out.append("      </conceptEntry>")
    out += ["    </body>", "  </text>", "</tbx>"]
    return "\n".join(out) + "\n"


def parse_tbx(path):
    """解析本项目 TBX-Core 子集；返回与 migrate_items 同形的记录。"""
    root = ET.parse(path).getroot()
    ns = {"t": NS}
    items = []
    for ce in root.findall(".//t:conceptEntry", ns):
        rec = _base(ce.get("id") or "", "", "")
        rec["id"] = ce.get("id") or ""
        for d in ce.findall("t:descrip", ns):
            key = DESCRIP_KEYS.get(d.get("type") or "")
            if key:
                rec[key] = (d.text or "").strip()
        rec["order"] = int(rec["order"] or 0)
        for ls in ce.findall("t:langSec", ns):
            term = ls.find("t:termSec/t:term", ns)
            if term is None:
                continue
            lang = ls.get(XML_LANG, "")
            if lang.startswith("en"):
                rec["source"] = (term.text or "").strip()
            elif lang.startswith("zh"):
                rec["target"] = (term.text or "").strip()
        items.append(rec)
    return items


def validate(items):
    """校验结构、必填、重复与状态；返回 {errors, warnings, count}。"""
    errors, warnings, seen = [], [], set()
    for rec in items:
        ident = str(rec.get("id") or "").strip()
        if not ident:
            errors.append("缺 conceptEntry/@id")
        elif ident in seen:
            errors.append("重复 conceptEntry/@id: %s" % ident)
        seen.add(ident)
        if not (str(rec.get("source") or "").strip() or str(rec.get("target") or "").strip()):
            errors.append("%s 缺 term" % (ident or "<无 id>"))
        status = str(rec.get("status") or "").strip()
        if status not in STATUSES:
            errors.append("%s 状态非法: %r" % (ident or "<无 id>", status))
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(rec.get("date") or "").strip()):
            errors.append("%s 日期缺失或非 YYYY-MM-DD" % (ident or "<无 id>"))
        if not str(rec.get("owner") or "").strip():
            errors.append("%s 缺 owner" % (ident or "<无 id>"))
        if str(rec.get("view") or "") not in VIEWS:
            errors.append("%s view 非法: %r" % (ident or "<无 id>", rec.get("view")))
        if status == "current" and not str(rec.get("definition") or "").strip():
            warnings.append("%s 当前术语缺定义（2026-12-01 起新登记须补）" % (ident or "<无 id>"))
    return {"errors": errors, "warnings": warnings, "count": len(items)}


def render_view(items, view):
    """从 TBX 记录生成两表之一的表体（样例视图）。"""
    cols = VIEW_COLUMNS[view]
    picked = sorted([r for r in items if r.get("view") == view],
                    key=lambda r: (r.get("order", 0), r.get("key", "")))
    out = ["| " + " | ".join(cols) + " |",
           "| " + " | ".join(["---"] * len(cols)) + " |"]
    for r in picked:
        vals = {
            "键": r.get("key", ""),
            "原文": r.get("source", ""),
            "别名": r.get("alias", ""),
            "译法": r.get("target", ""),
            "籍属": r.get("nationality", ""),
            "生卒": r.get("life", ""),
            "首现": r.get("first", ""),
            "依据": r.get("source_ref", ""),
            "裁定日期": r.get("date", ""),
        }
        out.append("| " + " | ".join((vals.get(c) or "—").replace("|", "\\|") for c in cols) + " |")
    return "\n".join(out) + "\n"


def write_sample(out_tbx, views_dir, n=5, reg=REG, con=CON, name=NAME):
    items = migrate_items(layout_rows(reg), layout_rows(con), layout_rows(name), limit=n)
    with open(out_tbx, "w", encoding="utf-8", newline="\n") as f:
        f.write(render(items))
    os.makedirs(views_dir, exist_ok=True)
    for view, fn in (("shu-yu", "shu-yu-sample.md"), ("ren-ming", "ren-ming-sample.md")):
        body = render_view(items, view)
        title = "# TBX 迁移样本视图：%s\n\n> 由 `baseline/termbase-sample.tbx` 生成，仅供往返验收；不替代正式两表。\n\n" % view
        with open(os.path.join(views_dir, fn), "w", encoding="utf-8", newline="\n") as f:
            f.write(title + body)
    return items


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", default=REG)
    ap.add_argument("--concepts", default=CON)
    ap.add_argument("--names", default=NAME)
    ap.add_argument("--out", default="")
    ap.add_argument("--check", default="")
    ap.add_argument("--sample-out", default="")
    ap.add_argument("--sample-views", default="")
    ap.add_argument("--sample-n", type=int, default=5)
    args = ap.parse_args(argv)
    if args.check:
        if not os.path.exists(args.check):
            print("输入缺失: %s" % args.check, file=sys.stderr)
            return 2
        result = validate(parse_tbx(args.check))
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return 1 if result["errors"] else 0
    if args.sample_out:
        if not args.sample_views:
            print("--sample-out 须同时给 --sample-views", file=sys.stderr)
            return 2
        for p in (args.registry, args.concepts, args.names):
            if not os.path.exists(p):
                print("输入缺失: %s" % p, file=sys.stderr)
                return 2
        items = write_sample(args.sample_out, args.sample_views, args.sample_n,
                             args.registry, args.concepts, args.names)
        print("已生成迁移样本 %d 条 → %s" % (len(items), args.sample_out))
        return 0
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
