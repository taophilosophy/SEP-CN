#!/usr/bin/env python3
"""渲染残留物扫描（2026-10-30，会话裁定待登记 rules/05）

对构建产物 HTML 做文本级残留物检查：裸 **、字面 [^脚注引用、markdown 链接
残留 ]( 、数学哨兵 @@M。代码块/预排块内的字面量为合法内容，自动排除。

用法:
    python tools/check_render_artifacts.py [dist目录]   # 默认 .vitepress/dist

输出按残留类别汇总；退出码: 有残留 1（作门禁需先裁定阈值与豁免清单）。
"""
import glob
import html
import json
import os
import re
import sys

PATS = {
    "literal**": lambda s: s.count("**"),
    "raw[^": lambda s: s.count("[^"),
    "md-link](": lambda s: s.count("]("),
    "sentinel@@M": lambda s: s.count("@@M"),
}


def text_of(path):
    t = open(path, encoding="utf8", errors="ignore").read()
    t = re.sub(r"<(code|pre)[\s\S]*?</\1>", " ", t)
    t = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    return html.unescape(t)


def main():
    dist = sys.argv[1] if len(sys.argv) > 1 else os.path.join(".vitepress", "dist")
    pages, by_kind = 0, {}
    for p in glob.glob(os.path.join(dist, "**", "*.html"), recursive=True):
        pages += 1
        s = text_of(p)
        for k, f in PATS.items():
            v = f(s)
            if v:
                by_kind.setdefault(k, []).append({"file": os.path.relpath(p, dist), "count": v})
    summary = {
        "pages": pages,
        "pages_with_artifacts": len({p for lst in by_kind.values() for p in lst}),
        "kinds": {
            k: {"pages": len(v), "total": sum(x["count"] for x in v), "top": sorted(v, key=lambda x: -x["count"])[:8]}
            for k, v in by_kind.items()
        },
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    return 1 if by_kind else 0


if __name__ == "__main__":
    sys.exit(main())
