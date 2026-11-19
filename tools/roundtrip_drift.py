# -*- coding: utf-8 -*-
r"""EN 互转漂移对比（en-roundtrip.yml 调用；specs/053 B3.1 运营化）。

语义（用户 2026-11-19 指令）：HTML 目录（en/）与英文 markdown（yuanwen/）双向互转的
**变动检测**。B3.1 存在已知残差（632/1872，规则闭合率 66.2%），故“变动”一律指
**相对已提交基线的差集**，不是“有失败”：

  ① en 钉漂移   —— divergence.py verify 的 failures 非空（en/ 与原始钉不一致）
  ② I2 漂移     —— check_yuanwen_fidelity --gate 红灯（md ≠ convert(en)）
  ③ 装配转差    —— 基线 ok 而现在 fail（新残差，需人审）
  ④ 装配转好    —— 基线 fail 而现在 ok（规则/内容变化，基线待更新）
  ⑤ 词条增删    —— 扫描面相对基线新增/缺失 slug

只读只报告：不写 baseline/、不改 en/ 与 yuanwen/、不提交任何内容文件。
退出码：0＝脚本正常（无论有无变动，变动状态见 changed 字段）；2＝输入缺失/格式错。

用法:
  roundtrip_drift.py --fresh F --baseline B [--divergence D] [--fidelity 0|1]
                     [--json OUT] [--md OUT] [--quiet]
"""
import argparse
import io
import json
import os
import sys

if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8")

MAX_LIST = 40  # 报告里每族最多列出的 slug 数


def _load(path):
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def scan_map(doc):
    """扫描 JSON → {slug: ok}；兼容 skipped 记录。"""
    out = {}
    for e in doc.get("entries", []):
        slug = e.get("slug")
        if not slug:
            continue
        out[slug] = bool(e.get("ok")) if not e.get("skipped") else None
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--fresh", required=True, help="本轮 assembly 扫描 JSON")
    ap.add_argument("--baseline", required=True, help="已提交基线扫描 JSON")
    ap.add_argument("--divergence", help="divergence.py verify 的 JSON 输出")
    ap.add_argument("--fidelity", default="", help="check_yuanwen_fidelity 退出码")
    ap.add_argument("--json", help="报告 JSON 输出路径")
    ap.add_argument("--md", help="报告 Markdown 输出路径")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    for p in (args.fresh, args.baseline):
        if not os.path.exists(p):
            sys.stderr.write("[roundtrip] 缺输入：%s\n" % p)
            return 2
    fresh = scan_map(_load(args.fresh))
    base = scan_map(_load(args.baseline))

    newly_failing = sorted(s for s, v in fresh.items()
                           if v is False and base.get(s) is True)
    newly_passing = sorted(s for s, v in fresh.items()
                           if v is True and base.get(s) is False)
    added = sorted(set(fresh) - set(base))
    removed = sorted(set(base) - set(fresh))

    div_failures = []
    if args.divergence and os.path.exists(args.divergence):
        try:
            d = _load(args.divergence)
            div_failures = d.get("failures") or []
        except (ValueError, OSError):
            div_failures = [{"reason": "divergence 输出无法解析"}]

    i2_failed = args.fidelity.strip() not in ("", "0")
    changed = bool(div_failures or i2_failed or newly_failing
                   or newly_passing or added or removed)

    n_ok = sum(1 for v in fresh.values() if v is True)
    n_fail = sum(1 for v in fresh.values() if v is False)
    n_skip = sum(1 for v in fresh.values() if v is None)
    report = {
        "schema": "sep-cn-roundtrip-drift/1",
        "generated_by": "tools/roundtrip_drift.py",
        "changed": changed,
        "en_pin_drift": len(div_failures),
        "i2_failed": i2_failed,
        "assembly": {"ok": n_ok, "fail": n_fail, "skipped": n_skip},
        "newly_failing": newly_failing,
        "newly_passing": newly_passing,
        "added_slugs": added,
        "removed_slugs": removed,
        "divergence_failures": div_failures[:MAX_LIST],
    }

    if args.json:
        os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
        with io.open(args.json, "w", encoding="utf-8", newline="\n") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
            f.write("\n")

    def _lst(items, fmt=str):
        if not items:
            return "（无）"
        lines = ["- `%s`" % fmt(x) for x in items[:MAX_LIST]]
        if len(items) > MAX_LIST:
            lines.append("- …另 %d 件（完整清单见报告 JSON）" % (len(items) - MAX_LIST))
        return "\n".join(lines)

    md = []
    md.append("## EN 互转漂移巡检")
    md.append("")
    md.append("| 信号 | 结果 |")
    md.append("| ---- | ---- |")
    md.append("| 变动 | **%s** |" % ("有" if changed else "无"))
    md.append("| ① en 钉漂移 | %d 件 |" % len(div_failures))
    md.append("| ② I2 重放（md≡convert(en)） | %s |"
              % ("红灯" if i2_failed else "全绿"))
    md.append("| ③ 装配转差（基线 ok→今 fail） | %d 件 |" % len(newly_failing))
    md.append("| ④ 装配转好（基线 fail→今 ok） | %d 件 |" % len(newly_passing))
    md.append("| ⑤ 词条增删 | +%d / −%d |" % (len(added), len(removed)))
    md.append("| 装配面 | ok %d／fail %d／skip %d |" % (n_ok, n_fail, n_skip))
    md.append("")
    if div_failures:
        md.append("### ① en 钉漂移")
        md.append("")
        md.append(_lst(div_failures,
                       lambda x: x.get("path") or x.get("reason") or str(x)))
        md.append("")
    if i2_failed:
        md.append("### ② I2 红灯")
        md.append("")
        md.append("`check_yuanwen_fidelity --gate` 非 0——md 与 convert(en) 不一致；"
                  "先跑 `python tools/check_yuanwen_fidelity.py` 看逐件明细。")
        md.append("")
    if newly_failing:
        md.append("### ③ 新残差（装配转差）")
        md.append("")
        md.append(_lst(newly_failing))
        md.append("")
    if newly_passing:
        md.append("### ④ 装配转好（基线可更新）")
        md.append("")
        md.append(_lst(newly_passing))
        md.append("")
    if added or removed:
        md.append("### ⑤ 词条增删")
        md.append("")
        if added:
            md.append("新增：\n\n" + _lst(added))
            md.append("")
        if removed:
            md.append("缺失：\n\n" + _lst(removed))
            md.append("")
    md.append("**落地方向**：③ 新残差 → 人审定四出口（勘误／补丁／转换器／例外登记）；"
              "④ 转好 → 重跑 `python specs/053-en-template-audit/bin/reassemble.py --all "
              "--out specs/053-en-template-audit/results/assembly-scan-all.json` 并提交基线；"
              "① → 走 update 任务（specs/001）；② → 查 yuanwen 是否被手改。")

    md_text = "\n".join(md) + "\n"
    if args.md:
        os.makedirs(os.path.dirname(os.path.abspath(args.md)), exist_ok=True)
        with io.open(args.md, "w", encoding="utf-8", newline="\n") as f:
            f.write(md_text)
    if not args.quiet:
        sys.stdout.write(md_text)
    if os.environ.get("GITHUB_OUTPUT"):
        with io.open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            f.write("changed=%s\n" % ("true" if changed else "false"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
