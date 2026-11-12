#!/usr/bin/env python3
"""specs/015 破折号专项：枚举 done 词条正文的破折号用量，生成候选优先队列。

职责边界（spec.md「不做关键词扫描判定」）：本脚本只统计用量、排出复核优先级，
不产生任何滥用/合规结论；滥用与否由复核人按 rules/02「破折号节制」语义判定，
结论记 results/dash-verdicts.jsonl。

统计口径：
* 只数中文破折号「——」（成对 em dash）与孤立 em dash「—」（前后不成对，
  多为误用单破折号）；en dash「–」（页码/年份范围）不计。
* 排除：围栏代码块、`>` 引块（直接引文/典籍原文）、`## References（引用注释）`
  与 `## 参考文献` 节标题及其后所有照录区（学术工具/网络资源/相关词条一并切断）。
* 脚注定义行（`[^...]:`）属译文正文，计入。
* 密度 = 破折号总次数 / 千汉字（全/半角汉字字数），供排序；不设阈值判定。

用法：python dash_scan.py（读同目录 results/queue.jsonl，写 results/dash-scan.jsonl）
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
QUEUE = RESULTS / "queue.jsonl"
OUT = RESULTS / "dash-scan.jsonl"

CUT_RE = re.compile(r"^## (?:References（引用注释）|参考文献)\s*$")
PAIR = "——"


def iter_body_lines(text: str):
    """产出计入统计的行；跳过围栏代码块与 `>` 引块，遇到文献照录区标题即止。"""
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith(">"):
            continue
        if CUT_RE.match(line):
            break
        yield line


def scan_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    dash2 = dash1 = 0
    han = 0
    for line in iter_body_lines(text):
        dash2 += line.count(PAIR)
        residue = line.replace(PAIR, "")
        dash1 += residue.count("—")
        han += sum(1 for ch in residue if "\u4e00" <= ch <= "\u9fff" or ch in "，。；：？！“”‘’（）《》")
    total = dash2 + dash1
    per_1k = round(total * 1000 / han, 2) if han else 0.0
    return {
        "path": str(path).replace("\\", "/"),
        "dash2": dash2,
        "dash1": dash1,
        "han": han,
        "per_1k": per_1k,
    }


def main() -> None:
    rows = []
    missing = []
    for raw in QUEUE.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        rec = json.loads(raw)
        fpath = HERE.parents[2] / rec["path"]
        if not fpath.exists():
            # queue.jsonl 是历史快照；官方退休/迁移后的词条可能已不在，跳过并提示
            missing.append(rec["path"])
            continue
        stat = scan_file(fpath)
        rows.append({"slug": rec["slug"], **stat})
    rows.sort(key=lambda r: (-r["per_1k"], -r["dash2"], r["slug"]))
    with OUT.open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"scanned {len(rows)} entries -> {OUT}")
    if missing:
        print(f"  跳过队列中已不存在的词条 {len(missing)}: {', '.join(missing)}")
    top = rows[:10]
    for r in top:
        print(f"  {r['per_1k']:>7.2f}/千字  dash2={r['dash2']:<3} dash1={r['dash1']:<2} {r['slug']}")


if __name__ == "__main__":
    main()
