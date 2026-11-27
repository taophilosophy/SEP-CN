# -*- coding: utf-8 -*-
"""机械替换回溯审计器（自 specs/015 破折号线工具泛化，specs/031 FR-3）。

用途：对指定词条的历次修复 commit 逐行做 diff 分类，揪出「机械替换」候选——即在旧译上
改词面/标点而非整句回源重译（rules/02 破折号条款、rules/03 差异处置、ADR-0048 决策 4）。

分类（删行/增行去标点后比较）：
  pure   去标点后逐字相同            → 仅标点/空白变动（机械替换签名）
  conn   相似度 ≥0.95 且增删 ≤4 字   → 小词块补丁（术语换形常落此类）
  susp   相似度 0.85–0.95            → 疑似（须人工判读：合法重写 or 机械改词）

判读纪律（2026-11-12 用户裁定，ADR-0048 沿用）：本器只产候选，不作定性；每处须回
`html/`／`en/` 源句比对后判定「实修（整句重译）」或「良性保持」，并在任务 evidence
或批次裁定表落凭证。

用法：
  python tools/mech_audit.py <slug> [...]            # 审计指定词条
  python tools/mech_audit.py <slug> --since 2026-11-08
  python tools/mech_audit.py <slug> --marker —       # 只审该标点计数有增减的行（原破折号线口径）
  python tools/mech_audit.py <slug> --out state/audit.json   # 默认 state/mech-audit-latest.json

退出码: 0 完成；2 未给 slug 或路径参数错误。
"""
import json
import re
import subprocess
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "state" / "mech-audit-latest.json"
PUNCT = re.compile(r"[\s—–\-−:：,，、。;；!！?？\u201c\u201d\u2018\u2019'\"()（）\[\]〔〕【】《》<>·….]")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout


def strip_punct(s):
    return PUNCT.sub("", s)


def classify(old, new):
    """→ (cat, why)；cat ∈ {pure, conn, susp, None}。"""
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
    """-U0 diff → [(old, new)]，按 hunk 分组后块内顺序配对。"""
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


def audit(slug, since="", marker=""):
    """单篇审计：返回 spots 列表（字段与 specs/015 原器同构）。"""
    spots = []
    files = git("ls-files", f"**/{slug}.md").strip().splitlines()
    if not files:
        print(f"!! {slug}: 未找到词条文件")
        return spots
    path = files[0]
    cur_lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    log_args = ["log", "--format=%H|%ad|%s", "--date=short"]
    if since:
        log_args.append(f"--since={since}")
    log = git(*log_args, "--", path)
    for logln in [l for l in log.strip().splitlines() if l]:
        sha, date, _subj = logln.split("|", 2)
        diff = git("show", "-U0", sha, "--", path)
        for old, new in pairs_from_diff(diff):
            if not (re.search(r"[\u4e00-\u9fff]", old) and re.search(r"[\u4e00-\u9fff]", new)):
                continue
            # 指定 marker 时只审该标点计数有增减的行（原破折号线口径）：
            # 否则无关的全局标点提交会把 pure 洪流误算进来
            if marker and old.count(marker) == new.count(marker):
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
    return spots


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    since, marker, out = "", "", DEFAULT_OUT
    slugs = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("--since", "--marker", "--out"):
            if i + 1 >= len(argv):
                print(f"{a} 需要参数值")
                return 2
            val = argv[i + 1]
            if a == "--since":
                since = val
            elif a == "--marker":
                marker = val
            else:
                out = Path(val)
            i += 2
            continue
        slugs.append(a)
        i += 1
    if not slugs:
        print(__doc__)
        return 2

    spots = []
    for slug in slugs:
        spots.extend(audit(slug, since=since, marker=marker))

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spots, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    c = Counter((s["slug"], s["cat"]) for s in spots)
    for slug in slugs:
        row = {cat: c.get((slug, cat), 0) for cat in ("pure", "conn", "susp")}
        unlocated = sum(1 for s in spots if s["slug"] == slug and not s["cur_lineno"])
        print(f"{slug:28s} pure={row['pure']:3d} conn={row['conn']:3d} susp={row['susp']:3d} 未定位={unlocated}")
    print(f"\n合计 pure={sum(1 for s in spots if s['cat'] == 'pure')} "
          f"conn={sum(1 for s in spots if s['cat'] == 'conn')} susp={sum(1 for s in spots if s['cat'] == 'susp')}")
    print(f"清单 → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
