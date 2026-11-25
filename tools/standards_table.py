# -*- coding: utf-8 -*-
"""从 rules/standards.json 的 cited 层生成 rules/README.md 标准表（ADR-0083）。

只改写 <!-- standards:begin --> 与 <!-- standards:end --> 之间的内容；标记缺失即报错，
不猜位置（防止误改正文）。用法：
  python tools/standards_table.py           # 写入
  python tools/standards_table.py --check   # 只校验是否同步（不同步退出 1）
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "rules", "standards.json")
README = os.path.join(ROOT, "rules", "README.md")
BEGIN = "<!-- standards:begin -->"
END = "<!-- standards:end -->"


def render():
    with open(REG, "rb") as f:
        d = json.loads(f.read().decode("utf-8"))
    rows = ["| 域 | 标准 | 版本/状态 | 落点 |", "| ---- | ---- | ---- | ---- |"]
    for c in d.get("cited", []):
        rows.append("| %s | %s | %s | %s |" % (c.get("domain", ""), c.get("std", ""),
                                               c.get("status", ""), c.get("owner", "")))
    return "\n".join(rows)


def rewrite(text):
    if BEGIN not in text or END not in text:
        raise SystemExit("README 缺 standards 标记（%s / %s）" % (BEGIN, END))
    head, rest = text.split(BEGIN, 1)
    _old, tail = rest.split(END, 1)
    return head + BEGIN + "\n" + render() + "\n" + END + tail


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    with open(README, encoding="utf-8") as f:
        text = f.read()
    new = rewrite(text)
    if args.check:
        if new != text:
            print("README 标准表与 cited 不同步；运行 python tools/standards_table.py")
            return 1
        print("README 标准表与 cited 同步")
        return 0
    with open(README, "w", encoding="utf-8", newline="\n") as f:
        f.write(new)
    print("已生成标准表（%d 行）" % (len(render().splitlines()) - 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
