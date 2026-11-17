# -*- coding: utf-8 -*-
"""体例机械项修复器 v2（specs/039 P8 红件清障，2026-11-17）。

**修理工与判官分离且不越界**：只改 `check_style` 点名的行与规则，逐行改后
立即复判——该行的目标规则违例须清零且不得引入新违例，否则该行回滚。
照录区（参考文献节、脚注定义行）由检查器自身豁免，故天然不在改动面内。

处理规则：quote-spacing（中文双引号与西文/数字补空格）、bold-spacing（** 邻接
补空格）、italic-cjk（*中文* → **中文**）、no-html（`<https://…>` 剥尖括号）。

用法: python specs/039-md-standardization/bin/style_fix.py <md>... [--execute]
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from tools import check_style  # noqa: E402  判官：行号与规则由它给
from tools.check_style import AFTER_PUNCT, EMPH_RE  # noqa: E402  同一标点集

FIX_RULES = ("quote-spacing", "bold-spacing", "italic-cjk", "no-html")
CJK = "\u4e00-\u9fff"
AUTOLINK = re.compile(r"<(https?://[^>\s]+)>")
ITALIC_CJK = re.compile(r"(?<!\*)\*([^* \n]*[%s][^* \n]*)\*(?!\*)" % CJK)
QS = [(re.compile(r"([A-Za-z0-9])([“‘])"), r"\1 \2"),
      (re.compile(r"([”’])([A-Za-z0-9])"), r"\1 \2")]


def _bold_spacing(line):
    pieces, pos = [], 0
    for m in EMPH_RE.finditer(line):
        s, e = m.start(), m.end()
        if (s > 0 and line[s - 1] == "*") or (e < len(line) and line[e] == "*"):
            continue
        before = line[s - 1] if s > 0 else ""
        after = line[e] if e < len(line) else ""
        nb = bool(before) and before not in " \t" and before not in "（“‘【《—…，。、；：？！）】》”’"
        na = bool(after) and after not in " \t" and after not in AFTER_PUNCT
        pieces.append(line[pos:s])
        pieces.append((" " if nb else "") + m.group(0) + (" " if na else ""))
        pos = e
    pieces.append(line[pos:])
    return "".join(pieces)


def fix_line(line):
    """四类机械变换（幂等：已合规的行返回原样）。"""
    new = AUTOLINK.sub(r"\1", line)
    for rx, rep in QS:
        new = rx.sub(rep, new)
    new = ITALIC_CJK.sub(lambda m: "**%s**" % m.group(1), new)
    new = _bold_spacing(new)
    return new


def issues_by_line(path):
    return _issues_by_text(open(path, encoding="utf-8", newline="").read())


def _issues_by_text(text):
    """把候选内容写临时文件再复判（dry-run 不碰原文件）。"""
    import tempfile
    fd, tmp = tempfile.mkstemp(suffix=".md")
    os.close(fd)
    try:
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        iss, _warn = check_style.check_file(tmp)
    finally:
        os.unlink(tmp)
    out = {}
    for i in iss:
        out.setdefault(i["line"], []).append(i["rule"])
    return out


def process(path, execute):
    text = open(path, encoding="utf-8", newline="").read()
    before = _issues_by_text(text)
    targets = {ln: rules for ln, rules in before.items() if set(rules) & set(FIX_RULES)}
    if not targets:
        return {"path": path, "lines": 0, "kept": 0, "rolled_back": 0, "residual": 0}
    lines = text.split("\n")
    kept = rolled = 0
    for ln in sorted(targets):
        idx = ln - 1
        if not (0 <= idx < len(lines)):
            continue
        orig = lines[idx]
        cand = fix_line(orig)
        if cand == orig:
            continue
        lines[idx] = cand
        after = _issues_by_text("\n".join(lines))
        still = set(after.get(ln, [])) & set(FIX_RULES)
        new_bad = set(after.get(ln, [])) - set(before.get(ln, []))
        if still or new_bad:
            lines[idx] = orig      # 回滚该行
            rolled += 1
        else:
            kept += 1
    final = _issues_by_text("\n".join(lines))
    residual = sum(len(set(r) & set(FIX_RULES)) for r in final.values())
    if execute and kept:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))
    return {"path": path, "lines": len(targets), "kept": kept,
            "rolled_back": rolled, "residual": residual}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args(argv)
    rows = []
    for p in args.paths:
        rows.append(process(p, args.execute))
    tot = {k: sum(r[k] for r in rows) for k in ("lines", "kept", "rolled_back", "residual")}
    for r in rows:
        if r["kept"] or r["rolled_back"]:
            print("%-58s 目标行 %d 改 %d 回滚 %d 余 %d"
                  % (r["path"], r["lines"], r["kept"], r["rolled_back"], r["residual"]))
    print("合计:", tot, "|", "已写回" if args.execute else "dry-run（未写盘）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
