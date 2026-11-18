# -*- coding: utf-8 -*-
"""生成 GitBook 英文空间（yuanwen/）的目录文件 `yuanwen/SUMMARY-en.md`（ADR-0056）。

为什么需要它：`yuanwen/SUMMARY.md` 是中文侧目录的**逐字符镜像**（标题为中文、条目路径
以 `../` 指回仓库根），既被 VitePress 的中英配对使用（标题相等才配对，不能改），又不能
直接当 GitBook 英文空间的 TOC——GitBook 以 space 根为界，`../` 条目会出界被丢弃。

本工具从 `SUMMARY.md` 派生英文 TOC：
  * 只保留目标文件在 `yuanwen/` 内存在的条目（中文侧导航行如 `qian-yan/*` 自然被剔除）；
  * 标题取「最后一个汉字之后的英文部分」，并保留别名行首的 `*` / `\\*` 标记；
    英文写在前面时（如 `\\*Confucianism 儒学`）取汉字之前的部分；
  * 英文部分内的顿号 `、`（SEP 作者并列）统一为半角逗号；
  * 条目路径改写为相对 `yuanwen/` 根的形态（即去掉 `../`）；
  * 母词条占位行按 ADR-0057 §6 输出为**无链接分组行**（去 `\\*` 标记、留英文标签与缩进）：
    中文侧两形态（`* [\\*美学 aesthetics](README.md)` 与 `* \\*美学 aesthetics`）产出同一结果，
    且绝不指向文件——GitBook 一文件一页，重复引用 `README.md` 会被拒收；
  * 保留 `## A` 字母分节与子条目缩进。

确定性：同一输入必得同一输出，不依赖时间与网络；`--check` 只校验不写回（可入 CI）。

用法:
  python tools/gen_en_summary.py             # 生成/覆盖 yuanwen/SUMMARY-en.md
  python tools/gen_en_summary.py --check     # 校验是否最新（退出码 1 = 需重生成）
  python tools/gen_en_summary.py --verbose   # 附逐条跳过原因
  python tools/gen_en_summary.py --no-groups # 省略分组行（ADR-0057 回退形态）
"""
import argparse
import io
import os
import re
import sys

try:  # 单测批量导入时 stdout 可能已被前序用例的重包 GC 关掉，此时保持原样
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUMMARY = os.path.join(ROOT, "SUMMARY.md")
TARGET = os.path.join(ROOT, "yuanwen", "SUMMARY-en.md")

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
# 汉字与英文标题之间常夹全角标点（书名号、括号、顿号、破折号），切分后须一并剥掉；
# 半角 ( [ ‘ “ 不剥，因为它们可以是英文标题的正常开头（如 ‘Abd al-Latif）。
TRIM = " \t\u3000（）《》〈〉「」『』【】，．。、：；！？…·‧—–－「」"
ENTRY = re.compile(r"^(\s*)\* \[(.*?)\]\((.*?)\)\s*$")
SECTION = re.compile(r"^##\s+(.*)$")
# 条目标题可能以 `\*`（转义星号）或 `*`（裸星号）开头作别名词条标记，两者都保留原样
MARK = re.compile(r"^(\*|\\\*)")


def english_title(title):
    """取英文标题：优先最后一个汉字之后的部分；英文写在前面时（如 `\\*Confucianism 儒学`）取汉字之前的部分。"""
    mark = MARK.match(title)
    prefix = mark.group(1) if mark else ""
    body = title[len(prefix):]
    last = None
    for m in CJK.finditer(body):
        last = m
    if last is not None:
        tail = body[last.end():].strip()
        while tail and tail[0] in TRIM:
            tail = tail[1:].lstrip()
        if tail:
            tail = tail.replace("、", ", ").replace("  ", " ")
            return prefix + tail
    # 回退：英文在前（无「汉字之后」的部分），要求至少两个拉丁字母，避免把孤立的字母编号当标题
    head = CJK.split(body)[0].strip().rstrip("：:—–-，, ")
    while head and head[-1] in TRIM:
        head = head[:-1].rstrip()
    if len(re.findall(r"[A-Za-z]", head)) >= 2:
        return prefix + head.replace("、", ", ")
    return None


def build(summary_path=SUMMARY, groups=True, base=None):
    base = base or os.path.join(ROOT, "yuanwen")
    with open(summary_path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    out = ["# Table of contents", ""]
    emitted, group, skipped = 0, 0, []
    for line in lines:
        sec = SECTION.match(line)
        if sec:
            out.append("## " + sec.group(1).strip())
            out.append("")
            continue
        m = ENTRY.match(line)
        if m:
            indent, title, href = m.group(1), m.group(2), m.group(3)
            # 母词条占位行：中文侧两形态（指向 README.md 的链接式 / 无链接式）统一按
            # ADR-0057 §6 输出为**无链接分组行**（去 `\*` 标记、留英文标签与缩进）。
            # 不得改成指向文件的链接：GitBook 一文件一页，重复引用 README.md 会被拒收。
            if href == "README.md" and MARK.match(title):
                en = english_title(title)
                label = MARK.sub("", en) if en else None
                if label and groups:
                    out.append("%s* %s" % (indent, label))
                    group += 1
                elif not label:
                    skipped.append((href, title, "占位行标题无英文部分"))
                continue
            if href.startswith("../") or href.startswith("/"):
                skipped.append((href, title, "目标不在 yuanwen/ 内"))
                continue
            if not os.path.exists(os.path.join(base, href)):
                skipped.append((href, title, "yuanwen/ 中无此文件"))
                continue
            en = english_title(title)
            if en is None:
                skipped.append((href, title, "标题无英文部分"))
                continue
            if CJK.search(en):
                skipped.append((href, title, "英文部分仍含汉字"))
                continue
            out.append("%s* [%s](%s)" % (indent, en, href))
            emitted += 1
            continue
        bare = re.match(r"^(\s*)\* (.+?)\s*$", line)
        if bare:
            indent, title = bare.group(1), bare.group(2)
            if MARK.match(title):
                en = english_title(title)
                label = MARK.sub("", en) if en else None
                if label and groups:
                    out.append("%s* %s" % (indent, label))
                    group += 1
                elif not label:
                    skipped.append(("-", title, "分组行标题无英文部分"))
            else:
                skipped.append(("-", title, "无法解析的列表行"))
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n", emitted, group, skipped


def main(argv=None):
    ap = argparse.ArgumentParser(description="生成英文空间目录 yuanwen/SUMMARY-en.md")
    ap.add_argument("--check", action="store_true", help="只校验，不写回")
    ap.add_argument("--verbose", action="store_true", help="打印逐条跳过原因")
    ap.add_argument("--summary", default=SUMMARY, help="源目录文件（默认仓库根 SUMMARY.md）")
    ap.add_argument("--out", default=TARGET, help="输出文件（默认 yuanwen/SUMMARY-en.md）")
    ap.add_argument("--no-groups", action="store_true",
                    help="省略母词条分组行（ADR-0057 回退方案：GitBook 若拒收无链接项则用此形态）")
    args = ap.parse_args(argv)

    text, emitted, group, skipped = build(args.summary, groups=not args.no_groups)
    if args.verbose:
        for href, title, why in skipped:
            print("SKIP %-40s %s | %s" % (href, why, title[:60]))
    print("词条 %d；分组行 %d；跳过 %d" % (emitted, group, len(skipped)))
    if not emitted:
        print("错误：没有任何可生成条目，拒绝写回")
        return 1

    old = None
    if os.path.exists(args.out):
        with open(args.out, encoding="utf-8") as fh:
            old = fh.read()
    if args.check:
        if old == text:
            print("english summary: 最新（%s）" % os.path.relpath(args.out, ROOT))
            return 0
        print("english summary: 需要重生成（python tools/gen_en_summary.py）")
        return 1
    if old == text:
        print("无变化，未写回")
        return 0
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("已写入 %s" % os.path.relpath(args.out, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
