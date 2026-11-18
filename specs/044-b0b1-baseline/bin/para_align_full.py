# -*- coding: utf-8 -*-
"""全库逐段对齐驱动（specs/007 para_align 算法的全覆盖面版）。

为何另写一个驱动器：`bin/para_align.py` 的条目表是**硬编码 16 件**（specs/007
2026-10-29 战役的一次性清单），因此"逐段比对、禁止抽查"这条要求实际只覆盖了
16 件；其余词条从未做过段落级漏译检测，且这一事实不在任何账上。本驱动器把同
一套 `en_blocks/zh_blocks/align` 用到全库，产出可核对的漏译面。

只读：不写 en/、不写译文、不覆盖 007 的历史凭证（另落 para-align-full.*）。
求值视图：zh 侧为译文 md，en 侧为 yuanwen 镜像（与 para_align 同口径——镜像
对 HTML 的保真由 I2/I3 闭环，本工具判的是"译文对源"的段落覆盖）。

用法: python -I specs/044-b0b1-baseline/bin/para_align_full.py [--limit N] [--slugs s...]
退出码: 0 完成（有漏译也是 0——漏译是发现不是错误）；2 输入缺失。
"""
import argparse
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "specs", "007-review-campaign", "bin"))

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

from tools.common import repo_path  # noqa: E402
from para_align import align, en_blocks, strip_tags, zh_blocks, _post  # noqa: E402


def formal_entries_with_body():
    """SUMMARY 正式词条中有正文者（骨架页不参与——无译文可比）。"""
    out = []
    with open(repo_path("SUMMARY.md"), encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^\s*\* \[(.*)\]\(([^)]*)\)\s*$", line.rstrip("\n"))
            if not m:
                continue
            title, path = m.group(1), m.group(2)
            top = path.split("/")[0]
            if top not in "abcdefghijklmnopqrstuvwxyz0123456789":
                continue
            if "— see" in title or "——见" in title or title.lstrip().startswith("\\*"):
                continue
            fp = repo_path(*path.split("/"))
            if not os.path.exists(fp):
                continue
            text = re.sub(r"(?s)<!--.*?-->", "", open(fp, encoding="utf-8").read())
            rest = re.sub(r"^#\s+.*$", "", text, count=1, flags=re.M)
            if len(re.findall(r"[\u4e00-\u9fff]", rest)) < 50:
                continue
            out.append((os.path.basename(path)[:-3], path))
    return out


def run(limit=None, only=None):
    ents = formal_entries_with_body()
    if only:
        ents = [e for e in ents if e[0] in only]
    if limit:
        ents = ents[:limit]
    rows = []
    for k, (slug, zh_path) in enumerate(ents, 1):
        letter = slug[0]
        ym = repo_path("yuanwen", letter, slug + ".md")
        rec = {"slug": slug}
        if not os.path.exists(ym):
            rec["status"] = "no-yuanwen"
            rows.append(rec)
            continue
        try:
            en = _post(zh_blocks(ym))
            zb = zh_blocks(repo_path(*zh_path.split("/")))
        except Exception as exc:
            rec["status"] = "error"
            rec["detail"] = "%s: %s" % (type(exc).__name__, exc)
            rows.append(rec)
            continue
        pairs, en_left, zh_left = align(en, zb)
        # 脚注键控对账（2026-11-18 加）：`align` 是同序贪心 1:1，脚注定义区在
        # 译文里只要有一处增删（译注、合并、条序变化）就会整体错位，把后续全部
        # 块推成"未配对"——全库首跑 26.7% 未配对率里 300/308 件属此类假阳性。
        # 故对 leftover 中的脚注定义按**键集合**核对，键在译文存在即不算漏。
        zh_text = open(repo_path(*zh_path.split("/")), encoding="utf-8").read()
        zh_defkeys = set(re.findall(r"\[\^([^\]\n]+)\]:", zh_text))
        truly_missing = []
        footnote_realigned = 0
        keymap_realigned = 0
        zh_low = zh_text.lower()
        for b in en_left:
            t = b["text"]
            m = re.match(r"\[\^([^\]]+)\]:", t)
            if m and m.group(1) in zh_defkeys:
                footnote_realigned += 1
                continue
            # 键名规范化容许（2026-11-18 加）：译文脚注键按书目规范可整体改名
            # （davidson 判例：en `davidson-1967a` → zh `an-1967a`，91 键全改），
            # 键集合核对必判缺失。故对**脚注定义类**残留再做内容级核对：
            # 块内特征词（≥6 字母）在译文出现即视为已搬运，不算漏译。
            if m:
                toks = re.findall(r"[A-Za-z]{6,}", re.sub(r"<[^>]+>", " ", t))[:3]
                if toks and any(tok.lower() in zh_low for tok in toks):
                    keymap_realigned += 1
                    continue
            truly_missing.append(t[:60])
        rec.update({
            "status": "ok",
            "en_blocks": len(en), "zh_blocks": len(zb), "pairs": len(pairs),
            "en_leftover_raw": len(en_left),
            "footnote_realigned": footnote_realigned,
            "footnote_keymap_realigned": keymap_realigned,
            "en_leftover": truly_missing,
            "zh_leftover": [b["text"][:60] for b in zh_left],
        })
        rows.append(rec)
        if k % 50 == 0:
            sys.stderr.write("[para_align_full] %d/%d\n" % (k, len(ents)))
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--slugs", nargs="*")
    ap.add_argument("--json", default=None)
    args = ap.parse_args(argv)

    rows = run(limit=args.limit, only=set(args.slugs or []) or None)
    ok = [r for r in rows if r["status"] == "ok"]
    no_yw = [r for r in rows if r["status"] == "no-yuanwen"]
    err = [r for r in rows if r["status"] == "error"]
    with_loss = [r for r in ok if r["en_leftover"]]
    # 漏译规模：EN 侧未配对块数（已剔除"键在译文存在"的脚注错位假阳性）
    total_en = sum(r["en_blocks"] for r in ok)
    total_left = sum(len(r["en_leftover"]) for r in ok)
    raw_left = sum(r.get("en_leftover_raw", 0) for r in ok)
    realigned = sum(r.get("footnote_realigned", 0) for r in ok)
    keymap = sum(r.get("footnote_keymap_realigned", 0) for r in ok)

    summary = {
        "schema": "sep-cn-para-align-full/2",
        "scope": "SUMMARY 正式词条中有正文者（骨架页排除）",
        "entries": len(rows), "aligned": len(ok),
        "no_yuanwen": len(no_yw), "errors": len(err),
        "en_blocks_total": total_en,
        "en_leftover_raw": raw_left,
        "footnote_realigned": realigned,
        "footnote_keymap_realigned": keymap,
        "en_leftover_total": total_left,
        "entries_with_en_leftover": len(with_loss),
        "leftover_rate": round(total_left / total_en, 5) if total_en else 0,
        "top_losses": sorted(
            [{"slug": r["slug"], "en_leftover": len(r["en_leftover"]),
              "en_blocks": r["en_blocks"],
              "samples": r["en_leftover"][:3]} for r in with_loss],
            key=lambda x: -x["en_leftover"])[:25],
        "no_yuanwen_slugs": sorted(r["slug"] for r in no_yw)[:40],
        "error_slugs": [{"slug": r["slug"], "detail": r.get("detail")} for r in err][:20],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))

    path = args.json or repo_path("specs", "044-b0b1-baseline", "results",
                                  "para-align-full-summary.json")
    jl = repo_path("specs", "044-b0b1-baseline", "results", "para-align-full.jsonl")
    # 局部运行不得写主凭证（2026-11-19 修，与 bin/para_align.py 同款事故）：
    # --limit/--slugs 是试跑形态，一次 `--limit 1` 就会把全库账抹成 1 件。
    if (args.limit or args.slugs) and not args.json:
        stem = "para-align-full-partial"
        path = repo_path("specs", "044-b0b1-baseline", "results", stem + "-summary.json")
        jl = repo_path("specs", "044-b0b1-baseline", "results", stem + ".jsonl")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    with io.open(jl, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("落盘: %s + %s" % (path, jl), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
