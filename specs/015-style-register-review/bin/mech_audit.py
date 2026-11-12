# -*- coding: utf-8 -*-
"""015 破折号线·机械替换审计器。

用途：对已收口（action=fix 后转 ok）词条的历次修复 commit 逐行做 diff 分类，
揪出「符号层机械替换」——即 rules/02 明令禁止的在旧译上改标点，而非整句回源重译。

分类（对删行/增行做去标点后的 SequenceMatcher）：
  pure   去标点后逐字相同            → 纯符号替换（必属违规，须回源重译）
  conn   相似度 ≥0.95 且增删 ≤4 字   → 连接词级补丁（如补「即」「因为」）
  susp   相似度 0.85–0.95            → 疑似（须人工判读：合法重写 or 机械删符号）

输出：results/mech-spots.json（含 cur_lineno 定位到当前文件行）。

用法：
  python specs/015-style-register-review/bin/mech_audit.py                # 审计内置 CLOSED 清单
  python specs/015-style-register-review/bin/mech_audit.py <slug> [...]   # 只审计指定词条

判读纪律（2026-11-12 用户裁定）：本器只产候选，不作定性；每处须回 yuanwen/ 源句比对后
判定「实修（整句重译）」或「良性保持」，并在 dash-verdicts.jsonl 落证据。
"""
import json
import re
import subprocess
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "specs/015-style-register-review/results/mech-spots.json"
PUNCT = re.compile(r"[\s—–\-−:：,，、。;；!！?？\u201c\u201d\u2018\u2019'\"()（）\[\]〔〕【】《》<>·….]")

# 截至 2026-11-12 已收口且审计完毕的 17 条（后续新增收口条目请追加）
CLOSED = [
    "mathematics-inconsistent", "lambert-auxerre", "scholz", "peirce-benjamin",
    "lady-masham", "kaspi-joseph", "lawphil-theory", "telesio", "olympiodorus",
    "leibniz-logic-influence", "dai-zhen", "kepler", "al-farabi", "leibniz-ethics",
    "reid-memory-identity", "kilvington", "kant-leibniz",
]


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout


def strip_punct(s):
    return PUNCT.sub("", s)


def classify(old, new):
    a, b = strip_punct(old), strip_punct(new)
    if not a or not b:
        return None, ""
    sm = SequenceMatcher(None, a, b)
    if sm.ratio() == 1.0:
        return "pure", "去标点逐字同"
    ops = sm.get_opcodes()
    ins = "".join(a[i1:i2] for tag, i1, i2, _, _ in ops if tag == "insert")
    dele = "".join(b[i1:i2] for tag, _, _, i1, i2 in ops if tag == "delete")
    if sm.ratio() >= 0.95 and len(ins) <= 4 and len(dele) <= 4:
        return "conn", f"ins={ins!r} del={dele!r}"
    if sm.ratio() >= 0.85:
        return "susp", f"r={sm.ratio():.2f} ins={ins[:12]!r} del={dele[:12]!r}"
    return None, ""


def pairs_from_diff(diff):
    """-U0 diff → [(old,new)]，按 hunk 分组后块内顺序配对。"""
    hunks, cur_o, cur_n = [], [], []
    for ln in diff.splitlines():
        if ln.startswith("@@"):
            if cur_o or cur_n:
                hunks.append((cur_o, cur_n))
            cur_o, cur_n = [], []
        elif ln.startswith(("---", "+++")):
            continue
        elif ln.startswith("-"):
            cur_o.append(ln[1:])
        elif ln.startswith("+"):
            cur_n.append(ln[1:])
    if cur_o or cur_n:
        hunks.append((cur_o, cur_n))
    out = []
    for o, n in hunks:
        out.extend(zip(o, n))
    return out


def main():
    slugs = sys.argv[1:] or CLOSED
    spots = []
    for slug in slugs:
        files = git("ls-files", f"**/{slug}.md").strip().splitlines()
        if not files:
            print(f"!! {slug}: 未找到词条文件")
            continue
        path = files[0]
        cur_lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
        log = git("log", "--since=2026-11-08", "--format=%H|%ad|%s", "--date=short", "--", path)
        for logln in [l for l in log.strip().splitlines() if l]:
            sha, date, _subj = logln.split("|", 2)
            diff = git("show", "-U0", sha, "--", path)
            for old, new in pairs_from_diff(diff):
                if not (re.search(r"[\u4e00-\u9fff]", old) and re.search(r"[\u4e00-\u9fff]", new)):
                    continue
                cat, why = classify(old, new)
                if not cat:
                    continue
                hits = [i + 1 for i, ln in enumerate(cur_lines) if new.strip() and new in ln]
                spots.append({
                    "slug": slug, "commit": sha[:9], "date": date, "cat": cat, "why": why,
                    "old": old, "new": new, "path": path,
                    "cur_lineno": hits, "cur_line": cur_lines[hits[0] - 1] if hits else None,
                })
    OUT.write_text(json.dumps(spots, ensure_ascii=False, indent=1), encoding="utf-8")

    c = Counter((s["slug"], s["cat"]) for s in spots)
    for slug in slugs:
        row = {cat: c.get((slug, cat), 0) for cat in ("pure", "conn", "susp")}
        unlocated = sum(1 for s in spots if s["slug"] == slug and not s["cur_lineno"])
        print(f"{slug:28s} pure={row['pure']:3d} conn={row['conn']:3d} susp={row['susp']:3d} 未定位={unlocated}")
    print(f"\n合计 pure={sum(1 for s in spots if s['cat']=='pure')} "
          f"conn={sum(1 for s in spots if s['cat']=='conn')} susp={sum(1 for s in spots if s['cat']=='susp')}")
    print(f"清单 → {OUT}")


if __name__ == "__main__":
    main()
