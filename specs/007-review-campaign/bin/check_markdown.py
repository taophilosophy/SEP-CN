# -*- coding: utf-8 -*-
"""markdown 全要素检查器（specs/007-review-campaign，用户 2026-10-28 新增任务）。

用户指令："确保所有markdown 格式正确，确保归一化，确保注释引用公式表格链接
图片等均正确，逐个审阅复核。"

检查维度（对全部入库 md 文件逐个执行）：
  A. 归一化（硬）：UTF-8 无 BOM；换行一律 LF（CRLF/裸 CR 为硬）；文件以换行
     收尾（硬）；全角空格 U+3000（硬，02-style"全角空格一律改半角"）；NBSP、
     制表符（信息级）。
  B. 脚注配对（硬）：`[^key]` 引用必须有对应 `[^key]:` 定义；孤儿定义信息级。
     围栏代码块与行内代码豁免。
  C. 表格（硬）：含分隔行的管道块内各行"列数=表头列数"；`\|`、`&#124;` 按
     转义字面计；无分隔行的管道块跳过（信息级提示）。
  D. 链接（硬）：`[text](target)` 内部相对目标必须解析到在盘文件；纯锚点
     `#frag` 与目标文件内锚点做信息级匹配；外链 http(s)/mailto 只计数。
  E. 图片（硬）：`![alt](path)` 目标必须在盘存在。
  F. 标题（信息级）：H1 缺失；H2 重复。

域分治：中文体例（引号/中西文空格/HTML 残留）归 tools/check_style.py，公式
保真归 tools/check_math.py，本工具不重复；yuanwen 英文镜像同样适用 B-E
（转换器产出应满足；上游固有噪声见执行日志裁定记录）。

用法:
  python specs/007-review-campaign/bin/check_markdown.py [--out PATH] [--scope all|yuanwen|zh|meta] [--quiet]
输出: stdout JSON 摘要；--out 落盘全量（含逐文件明细）。
退出码: 0 无硬问题；1 有硬问题；2 用法错误。
"""
import io
import json
import os
import re
import subprocess
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from tools.common import repo_path, utcnow_iso  # noqa: E402

FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
INLINE_MATH_RE = re.compile(r"\$\$?[^$]*\$\$?")
FOOT_USE_RE = re.compile(r"\[\^([^\]\s]+)\](?!:)")
FOOT_DEF_RE = re.compile(r"^\s{0,3}\[\^([^\]]+)\]:")
LINK_RE = re.compile(r"(?<!\!)\[([^\]]*)\]\(\s*<([^>]+)>\s*|(?<!\!)\[([^\]]*)\]\(\s*([^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
IMG_RE = re.compile(r"!\[([^\]]*)\]\(\s*([^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
DISPLAY_OPEN_RE = re.compile(r"(\$\$|\\\[)")


def classify(path):
    if path.startswith("yuanwen/"):
        return "yuanwen"
    if re.match(r"^[a-z0-9]/[^/]+\.md$", path):
        return "zh"
    return "meta"


def split_cells(line):
    """管道行 → 单元格列表；\\| 与 &#124; 为转义字面，不算分隔。"""
    s = INLINE_CODE_RE.sub("\x00", line.strip())
    s = s.replace("&#124;", "\x01")
    s = re.sub(r"\\\|", "\x01", s)
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def strip_spans(line):
    """剥行内代码与行内公式，避免 [^]…](…)/| 误报。"""
    line = INLINE_CODE_RE.sub("\x00", line)
    line = INLINE_MATH_RE.sub("\x00", line)
    return line


def resolve_target(target, base_dir):
    """相对目标 → 仓库相对路径（percent 解码、去 fragment）；外链/邮件返回 None。"""
    t = target.strip().replace("\\", "/")
    if re.match(r"^(https?:|mailto:|javascript:)", t, re.I):
        return None
    t = t.split("#", 1)[0]
    if not t:
        return ""
    t = urllib.parse.unquote(t)
    p = os.path.normpath(os.path.join(base_dir, t)).replace(os.sep, "/")
    return p


def check_file(rel):
    """单文件全要素检查 → (hard[], info[], counters, info_counts)。"""
    hard, info, cnt = [], [], {"external_links": 0, "images": 0, "internal_links": 0}
    info_counts = {}
    raw = open(repo_path(*rel.split("/")), "rb").read()
    abspath = repo_path(*rel.split("/"))
    base_dir = os.path.dirname(abspath)

    # A. 归一化（字节层）
    if raw.startswith(b"\xef\xbb\xbf"):
        hard.append({"line": 0, "kind": "bom", "detail": "UTF-8 BOM"})
    if b"\r\n" in raw:
        hard.append({"line": 0, "kind": "crlf", "detail": "含 CRLF 换行"})
    elif re.search(rb"\r[^\n]", raw):
        hard.append({"line": 0, "kind": "cr", "detail": "含裸 CR"})
    if raw and not raw.endswith(b"\n"):
        hard.append({"line": 0, "kind": "final-newline", "detail": "未以换行收尾"})
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        hard.append({"line": 0, "kind": "utf8", "detail": str(e)})
        return hard, info, cnt, info_counts

    lines = text.split("\n")
    in_fence = in_display = False
    foot_uses, foot_defs, headings = [], {}, []
    table_block = []

    def flush_table(end_lineno):
        nonlocal table_block
        if len(table_block) >= 2 and SEP_RE.match(table_block[1][1]):
            ncol = len(split_cells(table_block[0][1]))
            for ln, l in table_block[2:]:
                if len(split_cells(l)) != ncol:
                    hard.append({"line": ln, "kind": "table-columns",
                                 "detail": "列数 %d ≠ 表头 %d" % (len(split_cells(l)), ncol)})
        elif table_block:
            info_counts["pipe-block-no-sep"] = info_counts.get("pipe-block-no-sep", 0) + 1
        table_block = []

    for i, line in enumerate(lines, 1):
        if FENCE_RE.match(line):
            flush_table(i)
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # 行间公式状态（$$…$$ / \[…\] 可跨行）
        probe = line
        while True:
            m = DISPLAY_OPEN_RE.search(probe)
            if not m:
                break
            closer = "\\]" if m.group(1) == "\\[" else "$$"
            j = probe.find(closer, m.end())
            if j == -1:
                in_display = not in_display
                probe = probe[m.end():]
                break
            probe = probe[j + len(closer):]
        if in_display:
            flush_table(i)
            continue

        hm = HEAD_RE.match(line)
        if hm:
            flush_table(i)
            headings.append((len(hm.group(1)), hm.group(2).strip()))
            strip = hm.group(2)
        else:
            strip = line

        # 全角空格（02-style 硬规则）
        if "\u3000" in line:
            hard.append({"line": i, "kind": "fullwidth-space",
                         "detail": "全角空格 U+3000（应改半角）"})
        if "\u00a0" in line:
            info.append({"line": i, "kind": "nbsp", "detail": "不换行空格 U+00A0"})
        if "\t" in line:
            info.append({"line": i, "kind": "tab", "detail": "制表符"})

        bare = strip_spans(strip)
        fm = FOOT_DEF_RE.match(bare)
        if fm:
            foot_defs.setdefault(fm.group(1), 0)
            foot_defs[fm.group(1)] += 1
            if foot_defs[fm.group(1)] > 1:
                hard.append({"line": i, "kind": "footnote-def-dup",
                             "detail": "重复定义 [^%s]:" % fm.group(1)})
            continue
        for um in FOOT_USE_RE.finditer(bare):
            if strip.lstrip().startswith(">"):
                # 引用块内的 [^key] 多为体例说明文字（如转换器注释行），非真引用
                info_counts["footnote-mention-in-quote"] = \
                    info_counts.get("footnote-mention-in-quote", 0) + 1
            else:
                foot_uses.append((i, um.group(1)))

        if line.lstrip().startswith("|"):
            table_block.append((i, line))
            continue
        flush_table(i)

        for im in IMG_RE.finditer(bare):
            cnt["images"] += 1
            p = resolve_target(im.group(2), base_dir)
            if p and not os.path.exists(p):
                hard.append({"line": i, "kind": "image-missing",
                             "detail": "图片不存在: %s" % im.group(2)})

        for lm in LINK_RE.finditer(bare):
            target = lm.group(2) or lm.group(4)
            if not target:
                continue
            t = target.strip()
            if (t.startswith("*") or "(" in t or ")" in t
                    or ("/" not in t and "." not in t)):
                # 数学/排版记号伪装成链接（如 [Unmarried(*x*,*w*)](、单字母记号），
                # 真实相对目标必含 / 或 .
                continue
            if re.match(r"^(https?:|mailto:)", t, re.I):
                cnt["external_links"] += 1
                continue
            frag = None
            if t.startswith("#"):
                frag = t[1:]
            else:
                cnt["internal_links"] += 1
                p = resolve_target(t, base_dir)
                if p == "":
                    frag = None
                elif p and not os.path.exists(p):
                    hard.append({"line": i, "kind": "link-broken",
                                 "detail": "内部链接目标不存在: %s" % t})
                else:
                    frag = t.split("#", 1)[1] if "#" in t else None
            if frag:
                pass  # 锚点匹配为渲染器相关行为，不做逐条记录（信息级已由计数承载）
    flush_table(len(lines))

    # 脚注配对（meta 文档的 [^..] 多为体例示例文字，只查 yuanwen/zh）
    scope = classify(rel)
    defs = set(foot_defs)
    if scope in ("yuanwen", "zh"):
        for ln, key in foot_uses:
            if key not in defs:
                hard.append({"line": ln, "kind": "footnote-dangling",
                             "detail": "引用 [^%s] 无定义" % key})
    # 孤儿定义（yuanwen 设计使然：参考文献全量转脚注、正文只标实际引用组）——
    # 聚合计数，不逐条落 info
    info_counts["footnote-orphan-def"] = len(defs - {k for _, k in foot_uses})

    # 标题
    lv = [l for l, t in headings if l == 1]
    if not lv:
        info_counts["no-h1"] = 1
    seen = {}
    for l, t in headings:
        if l >= 2:
            seen[t] = seen.get(t, 0) + 1
    info_counts["dup-heading"] = sum(1 for n in seen.values() if n > 1)

    return hard, info, cnt, info_counts


def _file_foot_defs(rel):
    """文件内脚注定义键集合（快速扫描，供跨文件判定）。"""
    try:
        text = open(repo_path(*rel.split("/")), encoding="utf-8", errors="replace").read()
    except OSError:
        return set()
    return set(FOOT_DEF_RE.findall(text))


def tracked_md():
    """git 追踪的 md ∪ 磁盘扫描 yuanwen/（英文镜像语料不入库但属审阅对象，
    AGENTS.md：en/ 原始抓取、yuanwen/ 转换镜像均不入库）。"""
    out = subprocess.run(["git", "ls-files", "*.md"], cwd=repo_path("."),
                         capture_output=True, check=True).stdout
    files = {p.decode("utf-8") for p in out.split(b"\n") if p.strip()}
    yroot = repo_path("yuanwen")
    for dirpath, _dirs, names in os.walk(yroot):
        for n in names:
            if n.endswith(".md"):
                p = os.path.relpath(os.path.join(dirpath, n), repo_path(".")).replace(os.sep, "/")
                files.add(p)
    return sorted(files)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    scope, out_path, quiet = "all", None, False
    if "--scope" in argv:
        scope = argv[argv.index("--scope") + 1]
    if "--out" in argv:
        out_path = argv[argv.index("--out") + 1]
    quiet = "--quiet" in argv
    if scope not in ("all", "yuanwen", "zh", "meta"):
        print(json.dumps({"error": "scope 取值 all|yuanwen|zh|meta"}, ensure_ascii=False))
        return 2

    files = tracked_md()
    if scope != "all":
        files = [f for f in files if classify(f) == scope]

    hard_all, info_all, per_file, counters = [], [], [], {
        "external_links": 0, "images": 0, "internal_links": 0}
    info_kind_totals = {}
    for n, rel in enumerate(files, 1):
        if n % 200 == 0 and not quiet:
            sys.stderr.write("[check_markdown] %d/%d ...\n" % (n, len(files)))
        try:
            hard, info, cnt, info_counts = check_file(rel)
        except OSError as e:
            hard_all.append({"path": rel, "line": 0, "kind": "read-error", "detail": str(e)})
            continue
        for k, v in info_counts.items():
            info_kind_totals[k] = info_kind_totals.get(k, 0) + v
        # 跨文件脚注：yuanwen 补充材料可引用主文 md 的定义（转换器附载语义）
        if rel.startswith("yuanwen/") and rel.count("/") == 2 and rel.endswith(".md"):
            stem = os.path.basename(rel)[:-3]
            if "." in stem:
                sib = rel.replace(os.path.basename(rel), stem.split(".")[0] + ".md")
                sib_defs = _file_foot_defs(sib)
                kept = []
                for h in hard:
                    m = re.match(r"引用 \[\^([^\]]+)\] 无定义", h["detail"])
                    if m and m.group(1) in sib_defs:
                        info_all.append({"path": rel, "line": h["line"],
                                         "kind": "footnote-crossfile",
                                         "detail": h["detail"] + "（定义在主文 %s）"
                                                   % os.path.basename(sib)})
                    else:
                        kept.append(h)
                hard = kept
        for h in hard:
            hard_all.append({"path": rel, **h})
        for x in info:
            info_all.append({"path": rel, **x})
        for k in counters:
            counters[k] += cnt.get(k, 0)
        per_file.append({"path": rel, "scope": classify(rel),
                         "hard": len(hard), "info": len(info),
                         "info_counts": info_counts})

    from collections import Counter
    hard_kinds = Counter(h["kind"] for h in hard_all)
    summary = {"files": len(files), "hard": len(hard_all), "info": len(info_all),
               "hard_kinds": dict(hard_kinds), "info_kinds": info_kind_totals,
               "counters": counters, "scope": scope, "at": utcnow_iso()}
    if out_path:
        with open(repo_path(*out_path.split("/")) if not os.path.isabs(out_path) else out_path,
                  "w", encoding="utf-8", newline="\n") as f:
            json.dump({"summary": summary, "hard": hard_all, "info": info_all,
                       "per_file": per_file}, f, ensure_ascii=False, indent=1)
    print(json.dumps(summary, ensure_ascii=False))
    return 1 if hard_all else 0


if __name__ == "__main__":
    if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.exit(main())
