# -*- coding: utf-8 -*-
"""补丁池 × B0 判据的交集验证（ADR-0073 交集律的可重跑凭证）。

为何需要（ADR-0073 判例）：B0 的求值视图修正之前，"补丁是否影响 B0"这个问题
**从未被数据提出**——因为补丁池 3 条全是格式层（空格）修正，而 B0 十谓词没有
一条判空格，二者交集为空。空交集意味着：即便判定器求值视图错（在原始字节而
非补丁后求值），也不会有任何一条补丁件"补丁前判红、补丁后转绿"来暴露矛盾。
缺失被完美隐藏。故本脚本把"交集"做成**可机检的量**，每次补丁池变动后重跑。

判据：
  - flipped(False→True) 记录"该补丁修复了一个 B0 缺陷"（交集非空）；
  - regressed(True→False) 必须是 0（补丁不得引入 B0 缺陷）；
  - 若全部补丁 flipped 与 regressed 皆空，则本池与 B0 **交集为空**——此时
    B0 的求值视图正确性无法由补丁数据佐证，只能靠"与 convert_entry 同源"
    的代码对照（ADR-0073 同源对照条）来保证。

用法: python -I specs/044-b0b1-baseline/bin/verify_patch_intersection.py [--json PATH]
退出码: 0 验证完成（无论交集是否为空——空交集是**结论**不是失败）；1 输入缺失。
"""
import argparse
import glob
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools.common import read_text, repo_path  # noqa: E402
from tools.yuanwen import apply_en_patches  # noqa: E402
from verify_b0b1 import b0_predicates  # noqa: E402


def load_index():
    path = repo_path("baseline", "en-patches", "INDEX.json")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return json.load(fh).get("patches", [])


def run():
    patches = load_index()
    rows = []
    for p in patches:
        slug = p["slug"]
        idx = repo_path("en", slug, "index.html")
        if not os.path.exists(idx):
            rows.append({"id": p["id"], "slug": slug, "error": "no en snapshot"})
            continue
        raw = read_text(idx)
        try:
            patched = apply_en_patches(slug, raw)
        except Exception as exc:                # PatchMismatch：上游漂移，如实记
            rows.append({"id": p["id"], "slug": slug,
                         "error": "%s: %s" % (type(exc).__name__, exc)})
            continue
        before = b0_predicates(raw)
        after = b0_predicates(patched)
        flipped = sorted(k for k in before if not before[k] and after.get(k))
        regressed = sorted(k for k in before if before[k] and not after.get(k))
        rows.append({
            "id": p["id"],
            "slug": slug,
            "category": p.get("category"),
            "html_changed": raw != patched,
            "changed_bytes": len(patched) - len(raw),
            "b0_before_ok": all(before.values()),
            "b0_after_ok": all(after.values()),
            "flipped": flipped,
            "regressed": regressed,
        })

    checks = [r for r in rows if "error" not in r]
    summary = {
        "schema": "sep-cn-patch-intersection/1",
        "patches": len(rows),
        "html_changed": sum(1 for r in checks if r["html_changed"]),
        "intersection_nonempty": sum(1 for r in checks if r["flipped"]),
        "regressions": sum(1 for r in checks if r["regressed"]),
        "errors": [r for r in rows if "error" in r],
        "rows": rows,
    }
    if checks and summary["intersection_nonempty"] == 0:
        summary["verdict"] = (
            "空交集：本池补丁无一改动 B0 判据所及之处，故 B0 求值视图的正确性"
            "不能由补丁数据佐证，须由「判定器与 convert_entry 同源」的代码对照保证"
            "（ADR-0073 同源对照条）。")
    elif summary["intersection_nonempty"]:
        summary["verdict"] = "交集非空：%d 条补丁修复了 B0 缺陷（修复前判红、修复后转绿）。" \
                             % summary["intersection_nonempty"]
    else:
        summary["verdict"] = "无有效补丁件可验证。"
    return summary


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None)
    args = ap.parse_args(argv)
    s = run()
    print("补丁池 × B0 交集验证（ADR-0073 交集律）")
    print("  补丁 %d ｜ HTML 实际改动 %d ｜ 交集非空 %d ｜ 回归 %d ｜ 异常 %d"
          % (s["patches"], s["html_changed"], s["intersection_nonempty"],
             s["regressions"], len(s["errors"])))
    for r in s["rows"]:
        if "error" in r:
            print("  [ERR ] %-8s %-24s %s" % (r["id"], r["slug"], r["error"]))
        else:
            print("  [%s] %-8s %-24s html改=%s B0前=%s B0后=%s flipped=%s regressed=%s"
                  % ("FLIP" if r["flipped"] else ("REG!" if r["regressed"] else "NULL"),
                     r["id"], r["slug"], r["html_changed"],
                     r["b0_before_ok"], r["b0_after_ok"],
                     r["flipped"] or "-", r["regressed"] or "-"))
    print("  判读:", s["verdict"])
    path = args.json or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "results", "patch-intersection.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(s, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("落盘:", path)
    return 0 if not s["errors"] else 1


if __name__ == "__main__":
    sys.exit(main())
