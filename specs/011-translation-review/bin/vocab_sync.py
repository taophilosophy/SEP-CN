# -*- coding: utf-8 -*-
"""specs/011：词汇表滞后批量仲裁。

对 check_terms 报的每条滞后（登记侧变体集 != 词汇表变体集）：
  统计全部词条译文中各变体的使用次数；
  登记侧独有变体被使用 → 词汇表补；词汇表独有变体被使用 → 报告（登记册补行需人工裁定录入）；
  双向都无使用 → 词汇表对齐登记侧（删多余、不补缺）。
只读报告；--apply 执行词汇表行更新。
"""
import glob
import io
import os
import re
import subprocess
import sys
import collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
GLOSS = "qian-yan/ci-hui-biao.md"

# 译文语料缓存
corpus = None
def get_corpus():
    global corpus
    if corpus is None:
        parts = []
        for f in glob.glob("[a-z]/*.md"):
            if f.startswith(("yi-", "ren-", "mu-")):
                continue
            try:
                parts.append(io.open(f, encoding="utf-8").read())
            except Exception:
                pass
        corpus = "\n".join(parts)
    return corpus


def main():
    r = subprocess.run([sys.executable, "tools/check_terms.py"], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    lags = []
    for l in r.stdout.splitlines():
        m = re.search(r"词汇表滞后（告警）: \[(登记册|人名表)\] (\S+?) \| 登记侧: (.+?) \| 词汇表: (.+?)$", l)
        if m:
            lags.append((m.group(1), m.group(2), m.group(3), m.group(4)))
    print("滞后 %d 条" % len(lags))
    apply = "--apply" in sys.argv
    gtext = io.open(GLOSS, encoding="utf-8").read()
    report = []
    for src, en, reg_side, gl_side in lags:
        reg_vars = [v for v in re.split(r"[、，]", reg_side) if v]
        gl_vars = [v for v in re.split(r"[、，]", gl_side) if v]
        text = get_corpus()
        usage = {v: text.count(v) for v in set(reg_vars + gl_vars)}
        # 词汇表行更新：中文列 = 登记侧全集 ∪ 词汇表中被译文使用的变体
        keep_gl = [v for v in gl_vars if usage.get(v, 0) > 0]
        final = []
        for v in reg_vars + [v for v in keep_gl if v not in reg_vars]:
            if v not in final:
                final.append(v)
        new_zh = "、".join(final)
        # 找词汇表该行
        pat = re.compile(r"^\|%s\|([^|]+)\|" % re.escape(en), re.M)
        m2 = pat.search(gtext)
        reg_only_used = [v for v in reg_vars if v not in gl_vars and usage.get(v, 0) > 0]
        gl_only_used = [v for v in gl_vars if v not in reg_vars and usage.get(v, 0) > 0]
        report.append((en, reg_side, gl_side, new_zh, dict(usage), bool(m2), gl_only_used))
        print("%-26s 登记侧[+%s] 词汇表[+%s] → 词汇表定为「%s」%s" % (
            en, ",".join(v for v in reg_vars if v not in gl_vars) or "-",
            ",".join(v for v in gl_vars if v not in reg_vars) or "-",
            new_zh, "(行存在)" if m2 else "(词汇表无行!)"))
        if gl_only_used:
            print("    ⚠ 词汇表独有变体被译文使用，建议登记册补亦作: %s" % gl_only_used)
        if apply and m2:
            old_line = m2.group(0)
            new_line = "|%s|%s|" % (en, new_zh)
            gtext = gtext.replace(old_line, new_line, 1)
    if apply:
        io.open(GLOSS, "w", encoding="utf-8", newline="").write(gtext)
        print("已写 %s" % GLOSS)


if __name__ == "__main__":
    main()
