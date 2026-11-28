# -*- coding: utf-8 -*-
"""ex-05 格式闭合检查（rules/11 §6 八项；T166／T281）。

用法: python tools/check_format_closure.py <路径>...
输出: JSON {files, issues:[{path,line,rule,detail}], pass}
规则: heading-skip｜table-sep｜code-fence｜math-delim｜html-entity｜
      trailing-space｜consecutive-blank｜final-newline
退出码: 0 无问题；1 有 issue。零差异写 pass=true。
"""
import json
import re
import sys

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(
    __import__("os").path.abspath(__file__))))

HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
ENTITY_RE = re.compile(r"&(?:amp|lt|gt|quot|apos|#\d+|#x[0-9A-Fa-f]+);")


def check_text(text, path="<text>"):
    issues = []
    lines = text.split("\n")
    in_fence = False
    fence_count = 0
    prev_blank = False
    last_heading = 0
    math_open = False

    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            fence_count += 1
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.strip() == "":
            if prev_blank and i < len(lines):
                issues.append({"path": path, "line": i, "rule": "consecutive-blank",
                               "detail": "连续空行"})
            prev_blank = True
            continue
        prev_blank = False
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            if last_heading and level - last_heading > 1:
                issues.append({"path": path, "line": i, "rule": "heading-skip",
                               "detail": "标题跳级 H%d → H%d" % (last_heading, level)})
            last_heading = level
        if line.rstrip() != line:
            issues.append({"path": path, "line": i, "rule": "trailing-space",
                           "detail": "行尾空白"})
        prev_line = lines[i - 2] if i >= 2 else ""
        if line.lstrip().startswith("|") and not prev_line.lstrip().startswith("|"):
            nxt = lines[i] if i < len(lines) else ""
            sep = [c.strip() for c in nxt.strip().strip("|").split("|")] if "|" in nxt else []
            if not (sep and all(re.match(r"^:?-+:?$", c) for c in sep if c)):
                issues.append({"path": path, "line": i, "rule": "table-sep",
                               "detail": "表块缺对齐行"})
        if line.count("$") % 2:
            math_open = not math_open
        for m in re.finditer(r"&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9A-Fa-f]+);)", line):
            issues.append({"path": path, "line": i, "rule": "html-entity",
                           "detail": "未转义 &"})
            break
    if fence_count % 2:
        issues.append({"path": path, "line": len(lines), "rule": "code-fence",
                       "detail": "代码围栏未闭合"})
    if math_open:
        issues.append({"path": path, "line": len(lines), "rule": "math-delim",
                       "detail": "行内 $ 定界符未闭合"})
    if text and not text.endswith("\n"):
        issues.append({"path": path, "line": len(lines), "rule": "final-newline",
                       "detail": "文件末缺换行"})
    return issues


def main(argv):
    paths = [a for a in argv if not a.startswith("-")]
    if not paths:
        print(__doc__)
        return 2
    files, issues = [], []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            text = f.read()
        files.append(p)
        issues.extend(check_text(text, p))
    print(json.dumps({"files": files, "issues": issues, "pass": not issues},
                     ensure_ascii=False, indent=1))
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
