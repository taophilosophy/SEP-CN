# -*- coding: utf-8 -*-
"""specs/011 style 修复器：italic-cjk（中文斜体→加粗）/ bold-spacing / cjk-spacing 三类自动修复。

rules/05 批量改写纪律落地：
- 前置门：逐行修复后以 check_line 复验，修复类残余 != 0 的行不写回（挂人工清单）；
- 幂等：重跑零改动（不动点循环内建）；
- 逐行身份追踪：账本逐行记录 (file, lineno, rule, before, after)；
- 基线还原：仅在工作区干净时执行（git status --porcelain 对目标文件非空即拒绝）；
- 探针：--probe <slug> 只处理单文件并打印 diff，人工核对后再全量。

不修 curly-quotes / no-html / no-asciiart（语义复杂，逐处人工）。
豁免同 check_file：代码围栏、文献节非中文行、脚注定义行、图片行。
用法：
  python style_fix.py --probe i/impossible-worlds
  python style_fix.py            # 按 results/mechanical-scan.jsonl 全量
  python style_fix.py --slugs a/abduction i/identity
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_style  # noqa: E402

SCAN = os.path.join(ROOT, "specs", "011-translation-review", "results", "mechanical-scan.jsonl")
LEDGER = os.path.join(ROOT, "specs", "011-translation-review", "results", "style-fix-ledger.jsonl")
MANUAL = os.path.join(ROOT, "specs", "011-translation-review", "results", "style-fix-manual.jsonl")
FIX_RULES = ("italic-cjk", "bold-spacing", "cjk-spacing")

HAN = check_style.HAN
AFTER_PUNCT = check_style.AFTER_PUNCT
BEFORE_EXEMPT = " \t（“‘【《—…，。、；：？！）】》”’"
EMPH_RE = re.compile(r"\*\*[^*\n]+\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^* \n\x00]+?)\*(?!\*)")  # 与 check_style 同构：含空格斜体（拉丁短语/版本行）体例豁免不碰
GAP1_RE = re.compile(r"(?<=[%s])([A-Za-z0-9])" % HAN)   # 汉字|拉丁 → 补前空格
GAP2_RE = re.compile(r"([A-Za-z0-9])(?=[%s])" % HAN)    # 拉丁|汉字 → 补后空格
MASK_RE = re.compile(r"\$\$[^$]+?\$\$|\$[^$\n]+?\$|<[^<>\n]{1,60}>|\]\([^)\n]*\)")
BIB_HEADING_RE = check_style.BIB_HEADING_RE
FN_DEF_RE = check_style.FN_DEF_RE
HEADING_RE = check_style.HEADING_RE
CJK_LINE_RE = check_style.CJK_LINE_RE
TEXT_FENCE_RE = check_style.TEXT_FENCE_RE


def _mask(seg):
    """遮蔽数学/HTML/链接url，返回 (masked_seg, holes)。"""
    holes = []

    def _keep(m):
        holes.append(m.group(0))
        return "\x00%d\x00" % (len(holes) - 1)

    return MASK_RE.sub(_keep, seg), holes


def _unmask(seg, holes):
    return re.sub(r"\x00(\d+)\x00", lambda m: holes[int(m.group(1))], seg)


def italic_single_pass(text, seen_manual, manual):
    """线性 tokenizer 斜体转换：纯中文 *X* → **X**。

    re.sub 的回退重试会让「*Latin phrase*」的闭星错当下一对的开星，跨对吞掉
    其间整段中文（al-khunaji L54 复现实锤）。本扫描器保证：
    开星找不到合法闭星（遇 ** 边界/空格/占位/行尾）时原样前进一格；
    ** 粗体块整块跳过不参与配对。
    """
    out = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch != "*":
            out.append(ch)
            i += 1
            continue
        if i + 1 < n and text[i + 1] == "*":
            # ** 粗体块：整块跳过
            j = text.find("**", i + 2)
            if j == -1:
                out.append(text[i:])
                break
            out.append(text[i:j + 2])
            i = j + 2
            continue
        # 单星候选开：内容含空格=合法拉丁斜体对（原样保留整对，闭星不得再当开星）；
        # 仅遇 ** 边界/占位/换行才放弃（放弃时开星原样前进一格）
        j = i + 1
        closed = -1
        has_space = False
        while j < n:
            if text[j] == "*":
                if j + 1 < n and text[j + 1] == "*":
                    break  # 碰到 ** 边界，此开星无合法闭星
                closed = j
                break
            if text[j] == "\x00" or text[j] == "\n":
                break  # 占位/换行边界不可跨
            if text[j] == " ":
                has_space = True
            j += 1
        if closed > i:
            content = text[i + 1:closed]
            if has_space:
                out.append(text[i:closed + 1])  # 拉丁短语/版本行体例豁免，整对保留
            elif re.search(r"[一-鿿]", content) and not re.search(r"[A-Za-z0-9]", content):
                out.append("**%s**" % content)
            else:
                out.append(text[i:closed + 1])
                if re.search(r"[一-鿿]", content):
                    key = ("italic-mixed", content[:60])
                    if key not in seen_manual:
                        seen_manual.add(key)
                        manual.append({"rule": "italic-mixed", "detail": content[:60]})
            i = closed + 1
        else:
            out.append("*")
            i += 1
    return "".join(out)


def fix_seg(seg, seen_manual=None):
    """对单个正文段做三类修复，返回 (new_seg, edits, manual_notes)。

    v4 安全形态（011 复核 v1/v2/v3 事故复盘）：italic 替换只做**单遍**（第 1 轮），
    不进入不动点循环——多轮 italic 会让第 1 轮新产生的 `**` 与行内既有孤立 `*`
    跨对错配，把整段中文包成粗体（al-khunaji L54 复现实锤）。bold/cjk 保留循环。
    """
    edits, manual = [], []
    if seen_manual is None:
        seen_manual = set()
    masked, holes = _mask(seg)
    # ---- italic-cjk：单遍 tokenizer。v4 起**粗体块整块跳过+单星线性配对，
    # 粗斜共存行可安全处理（v1/v2/v3 的事故根因=正则回退跨对，已根治） ----
    masked = italic_single_pass(masked, seen_manual, manual)
    # ---- bold-spacing / cjk-spacing：不动点循环（不产生新星号结构，安全） ----
    for _ in range(4):
        changed = False
        # bold-spacing：两侧补空格（豁免标点/段边界）
        def _bold(m):
            s, e = m.start(), m.end()
            before = masked[s - 1] if s > 0 else ""
            after = masked[e] if e < len(masked) else ""
            core = m.group(0)
            if before and before not in BEFORE_EXEMPT:
                core = " " + core
            if after and after not in AFTER_PUNCT and after not in " \t":
                core = core + " "
            return core
        new_masked = EMPH_RE.sub(_bold, masked)
        if new_masked != masked:
            masked = new_masked
            changed = True
        # cjk-spacing：汉字↔拉丁/数字补空格（捕获组双正则，lookbehind 零宽不占 group）
        new_masked = GAP2_RE.sub(lambda m: m.group(1) + " ", GAP1_RE.sub(lambda m: " " + m.group(1), masked))
        if new_masked != masked:
            masked = new_masked
            changed = True
        if not changed:
            break
    new_seg = _unmask(masked, holes)
    if new_seg != seg:
        edits.append({"rule": "style-fix", "before": seg, "after": new_seg})
    return new_seg, edits, manual


def star_ok(seg):
    """星号标记结构 tokenizer 检查（*/**/*** 依序配对，栈空为健康）。

    行首列表标记 `* `（后随空格）是结构记号不是强调，跳过；
    数学定界 $…$/$$…$$ 内的星号非强调，先剥离；
    `***` 粗斜组作为独立 token 配对（***首次…*** 版本行）。
    """
    seg = re.sub(r"\$\$[^$]*\$\$|\$[^$\n]*?\$", "M", seg)
    seg = re.sub(r"\(\*+\)", "N", seg)  # (*)/(**) 公式编号记号豁免
    i, stack, n = 0, [], len(seg)
    while i < n:
        if seg[i] == "\\" and i + 1 < n and seg[i + 1] == "*":
            i += 2  # 转义星 \* 字面星，跳过
            continue
        m = re.match(r"\*+", seg[i:])
        if not m:
            i += 1
            continue
        tok = m.group(0)
        if len(tok) >= 3:
            if stack and stack[-1] == "***":
                stack.pop()
            elif stack:
                return False
            else:
                stack.append("***")
            i += len(tok)
            continue
        if i == 0 or (seg[i - 1] in " \t" and (i - 2 < 0 or seg[i - 2] in " \t>")):
            # 行首（或引用块内行首）的列表星：后随空格即豁免
            if i + 1 < n and seg[i + 1] == " ":
                i += 1
                continue
        t2 = "**" if len(tok) == 2 else "*"
        if stack and stack[-1] == t2:
            stack.pop()
        elif stack:
            return False  # 交叉：斜体开遇粗体闭（*X **Y** Z* 型，渲染必错乱）
        else:
            stack.append(t2)
        i += len(tok)
    return not stack


def fix_file(slug, dry=False):
    """返回 (ledger_rows, manual_rows, residual)。"""
    path = os.path.join(ROOT, slug + ".md")
    lines = io.open(path, encoding="utf-8").read().splitlines()
    out_lines, ledger, manual = [], [], []
    fence_open = False
    in_bib, bib_lvl = False, 0
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            fence_open = not fence_open
            out_lines.append(line)
            continue
        m_h = HEADING_RE.match(line)
        if m_h:
            lvl = len(m_h.group(1))
            if BIB_HEADING_RE.match(line):
                in_bib, bib_lvl = True, lvl
            elif not (in_bib and lvl > bib_lvl):
                in_bib = False
        if fence_open or line.lstrip().startswith("![") or FN_DEF_RE.match(line):
            out_lines.append(line)
            continue
        if in_bib and not CJK_LINE_RE.search(line):
            out_lines.append(line)
            continue
        # 畸形行（星号结构不平衡）整行跳过：修复器在畸形结构上会跨对错配
        _segs_txt = "".join(p for idx, p in enumerate(line.split("`")) if idx % 2 == 0)
        if not star_ok(_segs_txt):
            manual.append({"slug": slug, "line": i, "rule": "original-broken",
                           "detail": line[:120]})
            out_lines.append(line)
            continue
        # 逐段修复
        parts = line.split("`")
        new_parts, edits, manuals = [], [], []
        for idx, p in enumerate(parts):
            if idx % 2 == 1:
                new_parts.append(p)  # 行内代码不动
                continue
            ns, ed, mn = fix_seg(p)
            new_parts.append(ns)
            edits += ed
            manuals += mn
        new_line = "`".join(new_parts)
        # 复验：修复类残余必须为 0，否则该行回滚挂人工
        _buf = []
        check_style.check_line(path, i, new_line, _buf)
        issues = [x for x in _buf if x["rule"] in FIX_RULES]
        if issues:
            manual.append({"slug": slug, "line": i, "rule": "residual",
                           "detail": "; ".join("%s:%s" % (x["rule"], x["detail"][:50]) for x in issues)})
            out_lines.append(line)
            continue
        for e in edits:
            ledger.append({"slug": slug, "line": i, "rule": e["rule"],
                           "before": e["before"][:200], "after": e["after"][:200]})
        for mn in manuals:
            manual.append({"slug": slug, "line": i, "rule": mn["rule"], "detail": mn["detail"][:120]})
        out_lines.append(new_line)
    residual = sum(1 for m in manual if m["rule"] == "residual")
    if not dry and out_lines != lines:
        io.open(path, "w", encoding="utf-8", newline="").write("\n".join(out_lines) + "\n")
    return ledger, manual, residual


def main():
    args = sys.argv[1:]
    probe = None
    slugs = []
    if "--probe" in args:
        probe = args[args.index("--probe") + 1]
    elif "--slugs" in args:
        slugs = args[args.index("--slugs") + 1].split()
    else:
        slugs = sorted({json.loads(l)["slug"] for l in io.open(SCAN, encoding="utf-8")
                        if any(x["rule"] in FIX_RULES for x in json.loads(l)["style"])})
    if probe:
        slugs = [probe]

    # 基线前置门：有未提交改动的目标文件跳过（并行翻译会话可能在动它），不整体拒绝
    if slugs:
        r = subprocess.run(["git", "status", "--porcelain", "--"] + ["%s.md" % s for s in slugs],
                           capture_output=True, text=True, cwd=ROOT)
        dirty = {l[3:].strip() for l in r.stdout.splitlines() if l.strip()}
        skipped = [s for s in slugs if ("%s.md" % s) in dirty]
        if skipped:
            print("跳过（并行会话改动中）: %s" % " ".join(skipped))
            slugs = [s for s in slugs if s not in skipped]
        if not slugs:
            print("无可处理目标")
            return 0

    all_ledger, all_manual, touched = [], [], 0
    for slug in slugs:
        ledger, manual, residual = fix_file(slug, dry=bool(probe))
        all_ledger += ledger
        all_manual += manual
        if ledger or manual:
            touched += 1
        if probe:
            print("== %s：%d 处修改、%d 条人工" % (slug, len(ledger), len(manual)))
            for e in ledger[:10]:
                print("  L%s: [%s] %s" % (e["line"], e["rule"], e["after"][:80]))
    print("处理 %d 条，修改 %d 条，账本 %d 行，人工 %d 行" % (len(slugs), touched, len(all_ledger), len(all_manual)))
    if not probe:
        with io.open(LEDGER, "a", encoding="utf-8") as f:
            for row in all_ledger:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        with io.open(MANUAL, "a", encoding="utf-8") as f:
            for row in all_manual:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
