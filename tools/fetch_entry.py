# -*- coding: utf-8 -*-
"""抓取词条完整词条包：正文 + 脚注 + 补充材料 + 图片 + 元数据（FR-001…005）。

用法: python tools/fetch_entry.py <slug>... [--force]
输出: stdout JSON {fetched: [...], failures: [...]}
登记: baseline/entries.json（slug 主键 upsert，写后读回自校验）
落盘: en/<slug>/index.html、notes.html、<补充>.html、<图片>（不可变原始副本）

缺省件政策（spec Edge cases）：正文引用了 notes.html/补充材料/图片才去抓；
404 记入 missing[]（显式缺省，不算失败）；网络错误重试耗尽记 failures[]。
"""
import argparse
import json
import os
import re
import sys

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import fetch, parser
from tools.common import (ensure_dirs, find_zh_doc, load_json, repo_path,
                          sha256_bytes, sha256_file, utcnow_iso,
                          write_json_verified)
from tools.divergence import load_divergences

BASE = fetch.BASE
ARCHINFO = BASE + "/cgi-bin/encyclopedia/archinfo.cgi?entry=%s"
ENTRY_URL = BASE + "/entries/%s/"

SOFT404_RE = re.compile(r"<title>\s*(?:Document Not Found|Update Your Link)", re.I)


def is_soft404(head_html):
    """SEP 对不存在/已撤稿 URL 返回 HTTP 200 + 错误页正文（软 404）。"""
    return bool(SOFT404_RE.search(head_html))


def ledger_main_sha(slug):
    """台账原始网页钉（files[] 中 kind=main 的 sha256）；无登记返回 None。"""
    path = repo_path("baseline", "entries.json")
    if not os.path.exists(path):
        return None
    rec = next((r for r in load_json(path)["entries"] if r["slug"] == slug), None)
    if not rec:
        return None
    return next((f["sha256"] for f in rec.get("files", []) if f.get("kind") == "main"),
                None)


def ledger_files(slug):
    """台账该词条 files[] 的 {path: sha256}；无登记返回 {}。"""
    path = repo_path("baseline", "entries.json")
    if not os.path.exists(path):
        return {}
    rec = next((r for r in load_json(path)["entries"] if r["slug"] == slug), None)
    if not rec:
        return {}
    return {f["path"]: f["sha256"] for f in rec.get("files", [])}


def has_active_divergence(slug):
    """该词条在分歧账有登记（ADR-0045）：上游变更时须先搬运再重抓。"""
    return any(d.get("slug") == slug
               for d in load_divergences().get("divergences", []))


def entry_base(slug, archive_edition=None):
    """词条包基 URL；archive_edition 指定时从归档版抓取（撤稿词条）。"""
    if archive_edition:
        return BASE + "/archives/%s/entries/%s/" % (archive_edition, slug)
    return ENTRY_URL % slug


def fetch_one(slug, force, archive_edition=None):
    base = entry_base(slug, archive_edition)
    rec = {"slug": slug, "fetched_at": utcnow_iso(), "source_url": base}
    edir = repo_path("yuanwen", slug)
    os.makedirs(edir, exist_ok=True)
    files, missing = [], []

    status, data = fetch.get(base)
    if status != 200:
        return {"slug": slug, "error": "index.html HTTP %s" % status}
    if is_soft404(data[:4096].decode("utf-8", "replace")):
        # 防垃圾注册（2026-10-28 教训：撤稿词条曾被登记为空 title 基线）；
        # 撤稿词条请用 --archive-edition 从 /archives/<ed>/entries/<slug>/ 抓取
        return {"slug": slug,
                "error": "soft 404（SEP 错误页，词条不在或已撤稿）: %s" % base}
    idx_path = os.path.join(edir, "index.html")
    # 双账语义（ADR-0045）：仅当上游真变才动本地——
    #   上游与原始钉一致 → 不写盘不动台账；有未搬运分歧而上游已变 → 拒抓待搬运。
    old_main_sha = ledger_main_sha(slug)
    new_main_sha = sha256_bytes(data)
    prev_files = ledger_files(slug)
    index_same = bool(old_main_sha and old_main_sha == new_main_sha)
    if old_main_sha and old_main_sha != new_main_sha and not force \
            and has_active_divergence(slug):
        return {"slug": slug,
                "error": "上游已变且该词条存在未搬运分歧（baseline/en-errata/divergences.json）："
                         "先 compare.py 差异裁定，divergence.py carry <path> --new <快照> 随迁，再重抓"}
    if force or not os.path.exists(idx_path) or not index_same:
        with open(idx_path, "wb") as f:
            f.write(data)
    entry = parser.parse_entry(open(idx_path, "rb").read().decode("utf-8", "replace"))
    pub = next((b for b in entry["blocks"] if b["type"] == "pubinfo"), None)
    rec["title"] = entry["title"]
    rec["authors"] = entry["authors"]
    rec["pubinfo"] = {"first_published": pub["first_published"] if pub else None,
                      "substantive_revision": pub["substantive_revision"] if pub else None}
    rec["in_article_markers"] = entry["in_article_markers"]
    zh = find_zh_doc(slug, entry["title"])
    rec["zh_doc"] = ("zh/" + zh) if zh else None

    def save(relpath, payload):
        path = os.path.join(edir, relpath.replace("/", os.sep))
        same = (os.path.exists(path) and sha256_file(path) == sha256_bytes(payload))
        if force or not same:
            with open(path, "wb") as f:
                f.write(payload)
        return {"path": "yuanwen/%s/%s" % (slug, relpath), "sha256": sha256_file(path),
                "bytes": os.path.getsize(path)}

    files.append({"path": "yuanwen/%s/index.html" % slug, "sha256": sha256_file(idx_path),
                  "bytes": os.path.getsize(idx_path), "kind": "main"})

    # 脚注：正文有引用才抓（spec：404 为显式缺省件）
    if entry["notes_refs"]:
        st, notes = fetch.get(base + "notes.html")
        if st == 200:
            files.append(dict(save("notes.html", notes), kind="notes"))
        else:
            missing.append({"expected": "notes.html", "http_status": st})

    # 补充材料：正文相对链接
    for supp in entry["supplements"]:
        st, body = fetch.get(base + supp)
        if st == 200:
            files.append(dict(save(supp, body), kind="supplement"))
        else:
            missing.append({"expected": supp, "http_status": st})

    # 图片：词条目录相对路径（排除站点框架图与外链）
    for img in entry["images"]:
        src = img["src"]
        rel = src.split("?")[0]
        if rel.startswith(("../", "http:", "https:", "/")):
            continue
        st, body = fetch.get(base + rel)
        if st == 200:
            files.append(dict(save(rel, body), kind="image"))
        else:
            missing.append({"expected": rel, "http_status": st})

    # 脚本/样式：正文引用的词条自有 .js/.css（如 local.js——en_integrity 闭包要求，
    # 2026-10-28：每条新基线曾因缺 local.js 被深度复核标记）
    html_text = data[:len(data)].decode("utf-8", "replace")
    for m in re.finditer(r'(?:src|href)="([A-Za-z0-9][A-Za-z0-9._-]*\.(?:js|css))"', html_text):
        rel = m.group(1)
        if rel in {f["path"].split("/")[-1] for f in files}:
            continue
        st, body = fetch.get(base + rel)
        if st == 200:
            files.append(dict(save(rel, body), kind="script"))
        else:
            missing.append({"expected": rel, "http_status": st})

    # archinfo：权威版本核对（FR-003/008）
    st, ai = fetch.get(ARCHINFO % slug)
    rec["archinfo"] = parser.parse_archinfo(ai.decode("utf-8", "replace")) if st == 200 else {
        "error": "HTTP %s" % st}
    rec["archive_edition"] = archive_edition or rec["archinfo"].get("latest_edition")

    rec["files"] = files
    rec["missing"] = missing
    if not force and prev_files:
        changed = [f["path"] for f in files
                   if prev_files.get(f["path"]) != f["sha256"]]
        gone = [p for p in prev_files
                if p not in {f["path"] for f in files} and not p.endswith("index.html")]
        if not changed and not gone:
            return {"slug": slug, "result": "unchanged",
                    "note": "上游与原始网页钉一致（含脚注/附件），未写盘未动台账（ADR-0045）"}
    return rec


def _main_sha_of(files):
    """files[] 中 kind=main 的 sha256；无则 None。"""
    return next((f["sha256"] for f in (files or []) if f.get("kind") == "main"), None)


def _journal_lock(slug, old_main_sha, new_main_sha, rec):
    """主钉字节事实变更时落 journal lock 事件（ADR-0068 W1 事件族）；
    幂等：sha 相同（含重抓同内容）不落。"""
    if old_main_sha == new_main_sha:
        return None
    from tools.journal_lib import append_event
    return append_event(slug, {
        "type": "lock", "at": rec.get("fetched_at"), "actor": "fetch_entry",
        "sha256": new_main_sha,
        "pubinfo_date": (rec.get("pubinfo") or {}).get("substantive_revision"),
        "source_url": rec.get("source_url")})


def merge_files(old_files, new_files):
    """钉账并集保留（2026-11-25，specs/062 R-2）。

    新抓包未含、旧钉已有的文件**保留原记录**：上游新版不再引用的资产（改版后的
    旧图、被撤的补充页）在盘面仍存在（`en/` 绝对冻结，ADR-0062），摘钉即成
    `en_integrity` 的游离件硬发现；保留则落既定的 `registered_orphans`
    （版本更替残件，信息级）。两包同有者以新记录为准（钉前移）；新路径追加。
    顺序：先旧序（原位更新），后新件。
    """
    new_by = {f["path"]: f for f in (new_files or [])}
    merged = [new_by.pop(f["path"], f) for f in (old_files or [])]
    merged.extend(new_by.values())
    return merged


def upsert_baseline(rec):
    from tools.common import BASELINE_LOCK
    if not rec.get("files"):
        # 护栏（2026-11-25）：fetch_one 的 unchanged 结果无 files，若误交本函数
        # 会把整条钉账替换成残记录（files[].sha256 丢失）。只接受带 files 的完整记录。
        raise ValueError('upsert_baseline 拒绝无 files 的记录（slug=%r）：'
                         'unchanged 结果不得覆盖钉账' % rec.get('slug'))
    path = repo_path("baseline", "entries.json")
    old_main_sha = None
    with BASELINE_LOCK:
        if os.path.exists(path):
            base = load_json(path)
        else:
            base = {"schema": "sep-cn-baseline/1", "entries": []}
        prev = next((e for e in base["entries"] if e["slug"] == rec["slug"]), None)
        old_main_sha = _main_sha_of((prev or {}).get("files"))
        if prev and prev.get("files"):
            rec = dict(rec)
            rec["files"] = merge_files(prev["files"], rec["files"])
        entries = [e for e in base["entries"] if e["slug"] != rec["slug"]]
        entries.append(rec)
        entries.sort(key=lambda e: e["slug"])
        base["entries"] = entries
        base["updated_at"] = utcnow_iso()
        write_json_verified(path, base)
    _journal_lock(rec["slug"], old_main_sha, _main_sha_of(rec.get("files")), rec)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="+")
    ap.add_argument("--force", action="store_true", help="重抓覆盖本地原始副本")
    ap.add_argument("--archive-edition", dest="archive_edition",
                    help="撤稿词条归档版抓取：从 /archives/<ed>/entries/<slug>/ 抓取"
                         "（如 spr2017；本批所有 slug 共用同一版本）")
    args = ap.parse_args(argv)
    ensure_dirs()

    fetched, failures = [], []
    for slug in args.slugs:
        sys.stderr.write("[fetch_entry] %s ...\n" % slug)
        try:
            rec = fetch_one(slug, args.force,
                            archive_edition=args.archive_edition)
        except fetch.FetchError as e:
            failures.append({"slug": slug, "error": str(e)})
            continue
        if "error" in rec:
            failures.append(rec)
            continue
        if rec.get("result") == "unchanged":
            fetched.append({"slug": slug, "result": "unchanged"})
            sys.stderr.write("[fetch_entry] %s unchanged（上游未变，跳过）\n" % slug)
            continue
        upsert_baseline(rec)
        fetched.append({"slug": slug, "files": len(rec["files"]),
                        "missing": rec["missing"], "archive_edition": rec["archive_edition"]})
        sys.stderr.write("[fetch_entry] %s OK: %d files, %d missing\n"
                         % (slug, len(rec["files"]), len(rec["missing"])))
    print(json.dumps({"fetched": fetched, "failures": failures},
                     ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
