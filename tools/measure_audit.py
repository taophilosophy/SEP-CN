# -*- coding: utf-8 -*-
"""q5 计量扫描器（ADR-0079；机检做形态与白名单，人审判换算与语境）。

用法:
  python tools/measure_audit.py [路径...] [--all] [--init] [--gate] [--json] [--out PATH]

判据（checklists/q5-measure.md）:
  M-1 单位符号合规（大小写、正体、不加复数/句点；kg 不加倍词头）
  M-2 数值与单位符号间一个空格（% ‰ ° ′ ″ 例外）
  M-3 单位中文名称合规（人审）
  M-4 单位符号非规范形（m2、km. 等）
  M-5 同量全文单位一致
  M-6 数值范围连接号（～／— 全文同形；省略单位不歧义）
  M-7 数字形态一致（人审；本器只列候选）
  M-9 换算可复核（人审）
--gate：M-1/M-2/M-4 命中未处置、M-5 同量多单位未说明。
退出码: 0 通过/仅报告；1 --gate 未通过；2 用法错误。
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import axis_lib as ax  # noqa: E402

STATE_DIR = os.path.join(ax.ROOT, "state", "axis")

# 规范符号 → 量（M-1/M-5 用）
UNITS = {
    "km": "length", "m": "length", "cm": "length", "mm": "length",
    "µm": "length", "nm": "length", "mile": "length", "mi": "length",
    "ft": "length", "in": "length", "yd": "length",
    "kg": "mass", "g": "mass", "mg": "mass", "t": "mass", "lb": "mass", "oz": "mass",
    "s": "time", "min": "time", "h": "time", "d": "time",
    "°C": "temperature", "°F": "temperature", "K": "temperature",
    "m²": "area", "m³": "volume", "L": "volume", "mL": "volume",
    "ha": "area", "acre": "area",
    "m/s": "speed", "km/h": "speed", "mph": "speed",
    "J": "energy", "kJ": "energy", "W": "power", "kW": "power",
    "kWh": "energy", "cal": "energy", "kcal": "energy",
    "Pa": "pressure", "kPa": "pressure", "bar": "pressure", "atm": "pressure",
    "Hz": "frequency", "kHz": "frequency", "MHz": "frequency", "GHz": "frequency",
    "V": "voltage", "A": "current", "Ω": "resistance", "mol": "amount",
    "N": "force", "%": "ratio", "‰": "ratio",
    "°": "angle", "′": "angle", "″": "angle",
}
BAD_FORM = {
    "KM": "km", "KG": "kg", "ML": "mL", "CM": "cm", "MM": "mm",
    "HZ": "Hz", "KHZ": "kHz", "MHZ": "MHz", "GHZ": "GHz",
    "KW": "kW", "KWH": "kWh", "PA": "Pa", "KPA": "kPa",
}
NUM_UNIT = re.compile(
    r"(?<![\w.])(\d+(?:[.,]\d+)?)\s*([A-Za-zµμ°Ω%‰′″][A-Za-z0-9µμ°Ω/·^²³⁻¹′″]*)")
RANGE = re.compile(r"(\d+(?:[.,]\d+)?)\s*([-–—~～])\s*(\d+(?:[.,]\d+)?)\s*([A-Za-zµμ°Ω%‰/²³]*)")
BAD_M2 = re.compile(r"\b([A-Za-z]+)\s*\^\s*([23])\b|\b([A-Za-z]+)([23])\b(?!\d)")
NO_SPACE_OK = set("%‰°′″")
DATA = os.path.join(ax.ROOT, "tools", "data")


def _load_units():
    p = os.path.join(DATA, "units.json")
    if not os.path.exists(p):
        return
    with open(p, "rb") as f:
        d = json.loads(f.read().decode("utf-8"))
    UNITS.update(d.get("units", {}))
    BAD_FORM.update(d.get("bad_form", {}))
    NO_SPACE_OK.update(d.get("no_space_ok", []))


_load_units()


def classify(sym):
    """返回 (规范符号, 问题类型或 None)。"""
    if sym in UNITS:
        return sym, None
    if sym in BAD_FORM:
        return BAD_FORM[sym], "M-1"
    if sym.endswith("."):
        return sym.rstrip("."), "M-4"
    return sym, None


def scan(path):
    text = ax.read_doc(path)
    slug = ax.slug_of(path)
    items, issues = [], []
    masked = ax.protect(text)
    for m in NUM_UNIT.finditer(masked):
        val, sym = m.group(1), m.group(2)
        line_no = text.count("\n", 0, m.start()) + 1
        norm, prob = classify(sym)
        if prob:
            issues.append({"rule": prob, "line": line_no,
                           "detail": "%s%s → %s" % (val, sym, norm),
                           "verdict": "pending"})
        if sym not in NO_SPACE_OK:
            gap = masked[m.start(1) + len(val):m.start(2)]
            if gap != " ":
                issues.append({"rule": "M-2", "line": line_no,
                               "detail": "%s%s 数值与单位间应恰一个空格" % (val, sym),
                               "verdict": "pending"})
        q = UNITS.get(norm)
        items.append({"id": "m-%s-%03d" % (slug, len(items) + 1), "loc": "L%d" % line_no,
                      "value": val, "unit": norm, "quantity": q or "",
                      "verdict": "pending", "note": ""})
    for m in BAD_M2.finditer(masked):
        line_no = text.count("\n", 0, m.start()) + 1
        issues.append({"rule": "M-4", "line": line_no, "detail": m.group(0) + "（应上标）",
                       "verdict": "pending"})
    ranges = []
    for m in RANGE.finditer(masked):
        line_no = text.count("\n", 0, m.start()) + 1
        ranges.append({"line": line_no, "dash": m.group(2), "text": m.group(0)})
    dash_set = {r["dash"] for r in ranges}
    if len(dash_set) > 1:
        issues.append({"rule": "M-6", "line": ranges[0]["line"],
                       "detail": "数值范围连接号混用：%s" % "／".join(sorted(dash_set)),
                       "verdict": "pending"})
    by_q = {}
    for it in items:
        if it["quantity"]:
            by_q.setdefault(it["quantity"], set()).add(it["unit"])
    for q, us in by_q.items():
        if len(us) > 1:
            issues.append({"rule": "M-5", "line": 0,
                           "detail": "同量多单位 %s：%s" % (q, "／".join(sorted(us))),
                           "verdict": "pending"})
    return slug, {"schema": "measure-manifest/v1", "slug": slug,
                  "items": items, "ranges": ranges, "issues": issues}


def report_path(slug):
    return os.path.join(STATE_DIR, slug + ".measure.json")


def merge(slug, fresh):
    oldmap = {}
    if os.path.exists(report_path(slug)):
        with open(report_path(slug), "rb") as f:
            data = json.loads(f.read().decode("utf-8"))
        oldmap = {(x.get("rule"), x.get("line"), x.get("detail")): x
                  for x in data.get("issues", [])}
    for it in fresh["issues"]:
        k = (it["rule"], it["line"], it["detail"])
        if k in oldmap and oldmap[k].get("verdict") not in (None, "", "pending"):
            it["verdict"] = oldmap[k]["verdict"]
    return fresh


def gate(slug):
    p = report_path(slug)
    if not os.path.exists(p):
        return ["报告缺失：先跑 --init"]
    with open(p, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    probs = []
    for it in data.get("issues", []):
        if it.get("rule") in ("M-1", "M-2", "M-4", "M-5") \
                and it.get("verdict") in (None, "", "pending"):
            probs.append("%s@%s 未处置" % (it["rule"], it["line"]))
    return probs[:80]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    args = ap.parse_args()
    if args.all:
        args.paths = ax.target_paths(None)
    if not args.paths:
        ap.error("需要路径或 --all")

    report = {"schema": "measure-audit/v1", "files": [], "problems": []}
    for p in ax.target_paths(args.paths):
        slug, data = scan(p)
        if args.init:
            data = merge(slug, data)
            os.makedirs(STATE_DIR, exist_ok=True)
            with open(report_path(slug), "w", encoding="utf-8", newline="\n") as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
        probs = gate(slug) if args.gate else []
        for x in probs:
            report["problems"].append("%s: %s" % (slug, x))
        report["files"].append({
            "path": os.path.relpath(p, ax.ROOT).replace("\\", "/"),
            "slug": slug, "measures": len(data["items"]), "issues": len(data["issues"]),
            "samples": data["issues"][:6]})

    if args.out:
        ax.emit(report, args.out)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print("文件 %d；量值 %d；问题 %d"
              % (len(report["files"]),
                 sum(f["measures"] for f in report["files"]), len(report["problems"])))
        for x in report["problems"][:30]:
            print("  -", x)
    return 1 if (args.gate and report["problems"]) else 0


if __name__ == "__main__":
    sys.exit(main())
