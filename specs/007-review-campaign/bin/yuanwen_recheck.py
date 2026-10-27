# -*- coding: utf-8 -*-
"""yuanwen 英语markdown 重转换零写入复核（specs/007-review-campaign）。

以**真实 convert_entry 代码路径**逐词条重算转换产物，但把一切落盘操作改为
窥探比对（write_text_verified→读旧比对、update_baseline→空操作、
os.remove/os.makedirs→记录器），实现零磁盘变更；并行会话在途时避免
baseline/entries.json 写竞态（2026-10-28 会话 1 裁定）。

判定：重转换产物（归一化 CRLF 后）与在盘文件字节一致 = 转换器与镜像无漂移。

另做图片镜像直比：en/<slug>/<img> ↔ yuanwen/assets/<slug>/<img> 逐字节
（转换器复制语义：非图片类历史遗留应已被 D15 清理，多出/缺失/不一致均报）。

输出: stdout JSON {converted, drift[], image_drift[], failures[], at}
退出码: 0 无漂移；1 有漂移/失败。
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from tools.common import load_json, repo_path, sha256_file, utcnow_iso  # noqa: E402
import tools.yuanwen as yw  # noqa: E402

drift = []          # 文本产物漂移 [{slug, kind, path, reason}]
removed_would = []  # 窥探到的 os.remove（历史遗留清理目标，正常应为空）
madesirs = []       # 窥探到的 os.makedirs（信息级）
failures = []


def norm(data_or_text):
    if isinstance(data_or_text, str):
        data_or_text = data_or_text.replace("\r\n", "\n").replace("\r", "\n")
        return data_or_text.encode("utf-8")
    return data_or_text


def spy_write_text_verified(path, text):
    if not os.path.exists(path):
        drift.append({"slug": _slug_of(path), "kind": "new",
                      "path": _rel(path), "reason": "产物在盘缺失"})
        return
    old = open(path, "rb").read()
    if old != norm(text):
        drift.append({"slug": _slug_of(path), "kind": "changed",
                      "path": _rel(path),
                      "reason": "重转换与在盘不一致（%d vs %d 字节）"
                                % (len(old), len(norm(text)))})


def _slug_of(path):
    p = path.replace(os.sep, "/")
    return p.rsplit("/", 1)[-1].rsplit(".", 1)[0].split(".")[0]


def _rel(path):
    return os.path.relpath(path, repo_path(".")).replace(os.sep, "/")


def spy_update_baseline(*a, **k):  # 零写入：并行会话在途，不动 baseline
    pass


def spy_os_remove(path):
    removed_would.append(_rel(path))


def spy_os_makedirs(*a, **k):
    madesirs.append(_rel(a[0]))


yw.write_text_verified = spy_write_text_verified
yw.update_baseline = spy_update_baseline
os.remove = spy_os_remove
os.makedirs = spy_os_makedirs


def main():
    base = load_json(repo_path("baseline", "entries.json"))
    slugs = [r["slug"] for r in base["entries"]]
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1:])
        slugs = [s for s in slugs if s in only]
    converted, n = 0, 0
    for slug in slugs:
        n += 1
        if n % 100 == 0:
            sys.stderr.write("[yuanwen_recheck] %d/%d ...\n" % (n, len(slugs)))
        try:
            yw.convert_entry(slug)
            converted += 1
        except Exception as exc:  # noqa: BLE001 — 单词条失败不中断
            failures.append({"slug": slug, "error": repr(exc)})

    # 图片镜像直比（读侧）：en/<slug>/ 图片 ↔ yuanwen/assets/<slug>/
    image_exts = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf")
    image_drift = []
    for r in base["entries"]:
        slug = r["slug"]
        src_dir = repo_path("en", slug)
        adir = repo_path("yuanwen", "assets", slug)
        if not os.path.isdir(src_dir):
            continue
        imgs = [f for f in os.listdir(src_dir)
                if f.lower().endswith(image_exts)]
        disk = set(os.listdir(adir)) if os.path.isdir(adir) else set()
        for f in imgs:
            if f not in disk:
                image_drift.append({"slug": slug, "kind": "missing",
                                    "path": "yuanwen/assets/%s/%s" % (slug, f)})
                continue
            a = open(os.path.join(src_dir, f), "rb").read()
            b = open(os.path.join(adir, f), "rb").read()
            if a != b:
                image_drift.append({"slug": slug, "kind": "changed",
                                    "path": "yuanwen/assets/%s/%s" % (slug, f)})
        for f in sorted(disk - set(imgs)):
            image_drift.append({"slug": slug, "kind": "extra",
                                "path": "yuanwen/assets/%s/%s" % (slug, f)})

    out = {"converted": converted, "total": len(slugs), "drift": drift,
           "removed_would": removed_would, "image_drift": image_drift,
           "failures": failures, "at": utcnow_iso()}
    out_path = repo_path("specs", "007-review-campaign", "results",
                         "yuanwen-recheck.json")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: out[k] for k in
                      ("converted", "total", "at")}, ensure_ascii=False)
          + " drift=%d image_drift=%d failures=%d removed_would=%d"
          % (len(drift), len(image_drift), len(failures), len(removed_would)))
    return 0 if not (drift or image_drift or failures) else 1


if __name__ == "__main__":
    if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.exit(main())
