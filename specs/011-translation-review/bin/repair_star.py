# -*- coding: utf-8 -*-
"""specs/011：修复器错配损害回收。

ITALIC_RE 在 `**X**（*Y*）` 相邻结构上跨对错配（`*（*` 被包成粗体），复验门查不到（合法粗体形态）。
本脚本用 style-fix-ledger.jsonl 逐段审计 after 段的星号结构，不健康者回滚为 before 段。

星号结构检查（简化 tokenizer）：
  把段内所有星号串按 \\*\\*（粗体层）与单个 *（斜体层）解析：
  逐字符扫描，`**` 入栈粗体、`*` 入栈斜体，遇闭星匹配栈顶；栈非空或错配 = 不健康。
  完全严格的 CommonMark 解析不必要——破坏形态（`**（**`、`** *（*` 、孤立 `**`）都会在此检查下暴露。

用法：python repair_star.py [--apply]   # 缺省只报告，--apply 执行回滚
"""
import io
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
LEDGER = os.path.join(ROOT, "specs", "011-translation-review", "results", "style-fix-ledger.jsonl")


def star_ok(seg):
    """段内星号标记结构是否健康。"""
    i, stack, n = 0, [], len(seg)
    while i < n:
        if seg[i] == "*":
            if i + 1 < n and seg[i + 1] == "*":
                tok = "**"
            else:
                tok = "*"
            if stack and stack[-1] == tok:
                stack.pop()
            else:
                stack.append(tok)
            i += len(tok)
            continue
        i += 1
    return not stack


def main():
    apply = "--apply" in sys.argv
    rows = [json.loads(l) for l in io.open(LEDGER, encoding="utf-8")]
    files = {}
    for r in rows:
        files.setdefault(r["slug"], []).append(r)
    bad_total = 0
    for slug, items in sorted(files.items()):
        path = slug + ".md"
        t = io.open(path, encoding="utf-8").read()
        changed = 0
        for r in items:
            before, after = r["before"], r["after"]
            if star_ok(after):
                continue
            if after not in t:
                print("SKIP(段已不在): %s L%s %r" % (slug, r["line"], after[:50]))
                continue
            bad_total += 1
            changed += 1
            if apply:
                if not star_ok(before):
                    print("REFUSE(before 也不健康): %s L%s" % (slug, r["line"]))
                    continue
                t = t.replace(after, before, 1)
        if apply and changed:
            io.open(path, "w", encoding="utf-8", newline="").write(t)
        if changed or not apply:
            print("%s: 不健康段 %d / 账本 %d" % (slug, changed, len(items)))
    print("总计不健康段 %d（apply=%s）" % (bad_total, apply))


if __name__ == "__main__":
    main()
