# -*- coding: utf-8 -*-
"""生成 specs/README.md 索引（ADR-0067）。生成物不手改。

用法:
  python tools/spec_index.py            # 重写 specs/README.md
  python tools/spec_index.py --check    # 只校验现有索引是否与目录一致（CI 用，不写）

索引内容：编号、标题（取 spec.md 首行）、状态行、bin/results 有无、执行记录形态。
判定依据只读目录与 spec.md 头部，不解析正文语义。
退出码: 0 成功/一致；1 不一致（--check）；2 用法错误。
"""
import argparse
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "specs")
INDEX = os.path.join(SPECS, "README.md")

HEADER = (
    "# 规格目录索引\n\n"
    "<!-- 本文件由 `tools/spec_index.py` 生成，不手改；门禁 check_layout 的 L3 以此文件为 specs 的索引。 -->\n\n"
    "容器 schema 见 `rules/layout.json` 的 `specs_container`：必需 `spec.md`；"
    "禁止 `tmp/`、`__pycache__/`；规格根不得放 JSON（`results/` 承载）；"
    "`execution-log.md` 与 `execution-log/` 二选一。\n\n"
    "| 编号 | 标题 | 状态 | bin | results | 执行记录 |\n"
    "| --- | --- | --- | --- | --- | --- |\n"
)


def head_lines(path, n=60):
    try:
        with open(path, encoding="utf-8") as f:
            return [next(f, "") for _ in range(n)]
    except OSError:
        return []


def title_of(spec_md):
    for line in head_lines(spec_md):
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            t = m.group(1)
            t = re.sub(r"^specs/\d{3}[^：:]*[：:]\s*", "", t)
            return t.replace("|", "／").strip()
    return "—"


def state_of(spec_md):
    for line in head_lines(spec_md):
        m = re.search(r"\*\*状态\*\*\s*[：:]\s*([^｜|\n]+)", line)
        if m:
            return m.group(1).replace("|", "／").strip()
        m = re.search(r"^\|\s*状态\s*\|\s*([^|]+)\|", line)
        if m:
            return m.group(1).strip()
    return "—"


def build():
    rows = []
    for name in sorted(os.listdir(SPECS)):
        full = os.path.join(SPECS, name)
        if not os.path.isdir(full) or not re.match(r"^\d{3}-", name):
            continue
        children = set(os.listdir(full))
        spec_md = os.path.join(full, "spec.md")
        has_spec = "spec.md" in children
        title = title_of(spec_md) if has_spec else "（缺 spec.md）"
        state = state_of(spec_md) if has_spec else "—"
        bin_mark = "✓" if "bin" in children else "—"
        res_mark = "✓" if "results" in children else "—"
        if "execution-log" in children:
            log_mark = "目录"
        elif "execution-log.md" in children:
            log_mark = "单文件"
        else:
            log_mark = "—"
        rows.append("| [%s](%s/spec.md) | %s | %s | %s | %s | %s |"
                    % (name, name, title, state, bin_mark, res_mark, log_mark))
    total = len(rows)
    body = "\n".join(rows)
    return "%s%s\n\n共 %d 个规格目录。\n" % (HEADER, body, total)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只校验，不写")
    args = ap.parse_args(argv)
    text = build()
    if args.check:
        cur = ""
        if os.path.exists(INDEX):
            with open(INDEX, encoding="utf-8") as f:
                cur = f.read()
        if cur.strip() != text.strip():
            print("specs/README.md 与目录不一致（运行 python tools/spec_index.py 重生成）")
            return 1
        print("specs/README.md 与目录一致")
        return 0
    with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    with open(INDEX, encoding="utf-8") as f:
        if f.read().strip() != text.strip():
            print("写入后读回不一致（A14 可追溯写失败）")
            return 1
    print("已生成 specs/README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
