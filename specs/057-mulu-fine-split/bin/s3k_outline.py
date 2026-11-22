#!/usr/bin/env python3
"""specs/057 s3k：全库结构清单（供身份错位复核）。

每节点一行：H 级｜路径｜直属条目数｜子节名｜条目简称。
按 H1 区分档输出到 results/s3k-review/（避免 ADR-0004 单体超限）。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "specs/057-mulu-fine-split/bin"))
from inventory_all import scan  # noqa: E402


def zh(t, n=12):
    head = re.split(r"\s+(?=[A-Z])", t)[0].strip()
    return head[:n]


def main():
    nodes = scan((ROOT / "mu-lu-s.md").read_text(encoding="utf-8"))
    outdir = ROOT / "specs/057-mulu-fine-split/results/s3k-review"
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("*.md"):
        old.unlink()
    zones = {}
    for n in nodes:
        zones.setdefault(n["path"][0], []).append(n)
    index = ["# s3k 全库结构清单（身份错位复核用）", ""]
    for z, ns in zones.items():
        if z in ("前言", "关于"):
            continue
        lines = [f"# {z}", ""]
        for n in ns:
            if n["level"] > 4:
                continue
            kids = f"{n['sub']} 个"
            items = "、".join(zh(t) for _, t, _ in n["direct"]) or "—"
            lines.append(f"H{n['level']}｜{'／'.join(n['path'][1:])}｜{len(n['direct'])} 条｜"
                         f"子节：{kids}｜条目：{items}")
        fn = "s3k-" + re.sub(r"[、，\s]", "", z) + ".md"
        (outdir / fn).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        index.append(f"- `s3k-review/{fn}`｜{z}：H≤4 节点 {sum(1 for n in ns if n['level'] <= 4)}")
    (ROOT / "specs/057-mulu-fine-split/results/s3k-review-INDEX.md").write_text(
        "\n".join(index) + "\n", encoding="utf-8", newline="\n")
    print("写出", outdir)


if __name__ == "__main__":
    sys.exit(main())
