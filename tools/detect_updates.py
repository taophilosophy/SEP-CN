# -*- coding: utf-8 -*-
"""上游变更检测（specs/001 T020-21 契约实现）：What's New ＋ 版次核对 → 待办队列。

两源：
  from_web        new.html 的 [NEW]/[REVISED] 条目（默认近三个月窗）；sep.xml 若仍为
                  有效 feed 则并采，否则记 feed=unavailable（2026-11-19 实测 /sep.xml
                  返回 Document Not Found，只剩 new.html 一个源）。
  from_archinfo   对上述条目（或 --only 列表）抓 archinfo.cgi，与 baseline/entries.json
                  的 edition 对比，报出版次前移（不超过 --archinfo-max 条）。

queue 合并两源：NEW → retranslate；REVISED → update。只报告，不改内容文件。

用法:
  python tools/detect_updates.py                      # 联网抓 new.html（近 90 天）
  python tools/detect_updates.py --new-html <路径>     # 离线：用本地已存页面
  python tools/detect_updates.py --archinfo --archinfo-max 40
  python tools/detect_updates.py --no-write --out state/queue.json
退出码: 0 成功（无论有无变更）；1 抓取/解析失败。
"""
import argparse
import io
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import fetch, parser  # noqa: E402
from tools.common import load_json, repo_path, utcnow_iso  # noqa: E402

NEW_URL = fetch.BASE + "/new.html"
FEED_URL = fetch.BASE + "/sep.xml"
ARCHINFO_URL = fetch.BASE + "/cgi-bin/encyclopedia/archinfo.cgi?entry=%s"

ITEM_RE = re.compile(
    r'<li>\s*<a href="entries/([^"/]+)/"><strong>(.*?)</strong></a>'
    r'\s*(?:\(([^()]*(?:\([^()]*\)[^()]*)*)\))?\s*'
    r'\[(NEW|REVISED):\s*<em>(.*?)</em>\]'
    r'(?:\s*<div class="small">(.*?)</div>)?', re.S)
TAG_RE = re.compile(r"<[^>]+>")


def _strip(html_text):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", html_text or "")).strip()


def parse_new_html(text):
    """new.html → [{slug,title,authors,event,date,changes}]（文档序）。"""
    out = []
    for m in ITEM_RE.finditer(text):
        out.append({
            "slug": m.group(1),
            "title": _strip(m.group(2)),
            "authors": _strip(m.group(3)),
            "event": m.group(4).lower(),
            "date": _strip(m.group(5)),
            "changes": _strip(m.group(6)),
        })
    return out


def _parse_date(text):
    try:
        return datetime.strptime(text.strip(), "%B %d, %Y").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def filter_window(items, days):
    cut = datetime.now(timezone.utc) - timedelta(days=days)
    out, undated = [], []
    for it in items:
        d = _parse_date(it["date"])
        if d is None:
            undated.append(it)
        elif d >= cut:
            out.append(dict(it, when=d.strftime("%Y-%m-%d")))
    return out, undated


def parse_feed(text):
    """sep.xml → 条目列表；不是 feed 返回 None。"""
    if "<item" not in text and "<entry" not in text:
        return None
    try:
        root = ET.fromstring(text.encode("utf-8", "replace"))
    except ET.ParseError:
        return None
    out = []
    for node in root.iter():
        tag = node.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue
        rec = {}
        for child in node:
            name = child.tag.split("}")[-1]
            if name in ("title", "link", "pubDate", "updated", "published", "description"):
                rec[name] = _strip("".join(child.itertext()))
        if rec:
            out.append(rec)
    return out


def filter_synced(web_items, baseline):
    """剔除已同步条目：baseline 的 fetched_at 日期 ≥ 事件日期 → 该变更已入钉存。

    否则 90 天窗内每天都把已落地条目重报一遍（2026-11-19 issue #47 结案时暴露）。
    """
    idx = {e.get("slug"): e for e in baseline.get("entries", [])}
    out, done = [], 0
    for it in web_items:
        b = idx.get(it["slug"])
        when = it.get("when") or ""
        fetched = str((b or {}).get("fetched_at") or "")[:10]
        if b and when and fetched and fetched >= when:
            done += 1
            continue
        out.append(it)
    return out, done


def verify_web_items(web_items, baseline, limit=120):
    """逐条核内容钉：抓 index.html 与 baseline 的 main sha 比对，剔除「列表说改了、
    实际与本地钉逐字节一致」的假阳性（2026-11-19 emotion-Christian-tradition 实证）。"""
    import hashlib
    idx = {e.get("slug"): e for e in baseline.get("entries", [])}
    out, same = [], []
    for it in web_items[:limit]:
        b = idx.get(it["slug"])
        pin = None
        if b:
            pin = next((f["sha256"] for f in b.get("files", []) if f.get("kind") == "main"), None)
        if not pin:
            out.append(it)
            continue
        st, data = fetch.get(fetch.BASE + "/entries/%s/" % it["slug"])
        if st != 200:
            out.append(it)
            continue
        cur = hashlib.sha256(data).hexdigest()
        if cur == pin:
            same.append(it["slug"])
        else:
            out.append(it)
    out.extend(web_items[limit:])
    return out, same


def archinfo_drift(slugs, baseline, limit):
    """抓 archinfo.cgi 与 baseline 版次比对（slugs 去重、截断 limit）。"""
    base = {e["slug"]: e for e in baseline.get("entries", [])}
    out = []
    seen = set()
    for slug in slugs:
        if slug in seen or len(out) >= limit:
            continue
        seen.add(slug)
        status, data = fetch.get(ARCHINFO_URL % slug)
        if status != 200:
            out.append({"slug": slug, "error": "archinfo HTTP %s" % status})
            continue
        ai = parser.parse_archinfo(data.decode("utf-8", "replace"))
        b = base.get(slug)
        pending = ai.get("pending_change_type")
        if not b:
            out.append({"slug": slug, "baseline_edition": None,
                        "latest_edition": ai.get("latest_edition"),
                        "change_type": ai.get("latest_change_type") or pending,
                        "pending": bool(pending),
                        "note": "不在 baseline"})
            continue
        b_ed = (b.get("archinfo") or {}).get("latest_edition")
        cur = ai.get("latest_edition")
        if cur and b_ed != cur:
            out.append({"slug": slug, "baseline_edition": b_ed, "latest_edition": cur,
                        "change_type": ai.get("latest_change_type"), "pending": False})
        elif b_ed and pending:
            # 基线有存档版、线上是冻结后修订（尚未归档）：版次前移的「进行中」信号
            out.append({"slug": slug, "baseline_edition": b_ed,
                        "latest_edition": "pending-archive",
                        "change_type": pending, "pending": True})
        elif b_ed is None and cur is None:
            # 基线也是「未归档」态：无可比的版次，交由 new.html 时点覆盖（不重复报）
            continue
    return out


def build_queue(web_items, arch_items):
    """两源合并为待办队列：NEW → retranslate；REVISED → update。"""
    q, seen = [], {}

    def push(slug, action, reason, **extra):
        key = (slug, action)
        if key in seen:
            seen[key]["sources"].append(reason)
            return
        rec = {"slug": slug, "action": action, "reason": reason,
               "sources": [reason]}
        rec.update(extra)
        seen[key] = rec
        q.append(rec)

    for it in web_items:
        if it["event"] == "new":
            push(it["slug"], "retranslate", "web:new:%s" % it.get("when", it["date"]),
                 title=it["title"], changes=it.get("changes", ""))
        else:
            push(it["slug"], "update", "web:revised:%s" % it.get("when", it["date"]),
                 title=it["title"], changes=it.get("changes", ""))
    for a in arch_items:
        if a.get("error"):
            continue
        push(a["slug"], "update",
             "archinfo:%s->%s" % (a.get("baseline_edition") or "—",
                                  a.get("latest_edition") or "未归档"))
    return q


def _human_source(key, val):
    """单条数据源状态 → 人话（替代裸 JSON/dict repr）。"""
    if val.startswith("live:"):
        return "%s 正常（HTTP %s）" % (key, val[5:])
    if val.startswith("local:"):
        return "%s 本地文件" % key
    if val.startswith("unavailable:"):
        return "%s 不可用（%s）" % (key, val[12:])
    if val == "ok":
        return "%s 正常" % key
    return "%s %s" % (key, val)


def render_queue_md(doc):
    """队列 → Markdown 摘要（CI issue 正文用）。"""
    L = ["## 上游变更待办（new.html ＋ 版次核对）", ""]
    L.append("- 数据源：%s" % "；".join(_human_source(k, v)
                                      for k, v in doc.get("sources", {}).items()))
    q = doc.get("queue", [])
    L.append("- 窗口：近 %s 个月；队列 %d 条" % (doc.get("window_months"), len(q)))
    L.append("")
    for it in q[:60]:
        src = ", ".join(it.get("sources", []))
        tail = ("：" + it["changes"]) if it.get("changes") else ""
        L.append("- `%s` → %s（%s）%s" % (it["slug"], it["action"], src, tail))
    if len(q) > 60:
        L.append("- …… 余 %d 条，见运行工件 queue.json" % (len(q) - 60))
    L.append("")
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--new-html", default=None, help="离线：本地 new.html 路径")
    ap.add_argument("--feed", default=None, help="离线：本地 sep.xml 路径")
    ap.add_argument("--months", type=int, default=3, help="时间窗（月，默认 3）")
    ap.add_argument("--archinfo", action="store_true", help="加抓 archinfo.cgi 版次核对")
    ap.add_argument("--archinfo-max", type=int, default=60)
    ap.add_argument("--only", nargs="*", default=None, help="限定 slug（archinfo 用）")
    ap.add_argument("--out", default="baseline/queue.json")
    ap.add_argument("--md", default=None, help="另写 Markdown 摘要（CI issue 正文用）")
    ap.add_argument("--verify-web", action="store_true",
                    help="抓 index.html 核内容钉，剔除 new.html 假阳性（列表标改、实际未变）")
    ap.add_argument("--no-write", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    sources = {}
    if args.new_html:
        text = io.open(args.new_html, encoding="utf-8", newline="").read()
        sources["new_html"] = "local:%s" % os.path.basename(args.new_html)
    else:
        st, data = fetch.get(NEW_URL)
        if st != 200:
            print(json.dumps({"error": "new.html HTTP %s" % st}, ensure_ascii=False))
            return 1
        text = data.decode("utf-8", "replace")
        sources["new_html"] = "live:200"
    web_all = parse_new_html(text)
    if not web_all:
        print(json.dumps({"error": "new.html 解析为空（页面改版？）"}, ensure_ascii=False))
        return 1
    web_items, undated = filter_window(web_all, args.months * 30)

    feed_items = None
    if args.feed:
        feed_items = parse_feed(io.open(args.feed, encoding="utf-8", newline="").read())
        sources["feed"] = "local:%s" % ("ok" if feed_items else "unavailable")
    else:
        st, data = fetch.get(FEED_URL)
        feed_items = parse_feed(data.decode("utf-8", "replace")) if st == 200 else None
        sources["feed"] = ("ok" if feed_items else
                           "unavailable:%s" % (st if st != 200 else "not-a-feed"))

    baseline = load_json(repo_path("baseline", "entries.json"))
    web_items, synced_skipped = filter_synced(web_items, baseline)
    verified_same = []
    if args.verify_web and web_items:
        web_items, verified_same = verify_web_items(web_items, baseline)

    arch_items = []
    if args.archinfo:
        slugs = args.only or [it["slug"] for it in web_items]
        arch_items = archinfo_drift(slugs, baseline, args.archinfo_max)

    queue = build_queue(web_items, arch_items)
    doc = {"generated_at": utcnow_iso(), "window_months": args.months,
           "sources": sources,
           "from_web": web_items, "from_web_undated": len(undated),
           "synced_skipped": synced_skipped, "verified_same": verified_same,
           "from_rss": feed_items or [],
           "from_archinfo": arch_items,
           "queue": queue}
    # --no-write 只抑制默认落盘（baseline/queue.json）；显式 --out 一律写（CI 写 runner 临时区）
    explicit_out = any(a == "--out" or a.startswith("--out=") for a in (argv or sys.argv[1:]))
    if not args.no_write or explicit_out:
        out = args.out if os.path.isabs(args.out) else repo_path(*args.out.split("/"))
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        with io.open(out, "w", encoding="utf-8", newline="\n") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
        doc["written"] = out
    if args.md:
        md = args.md if os.path.isabs(args.md) else repo_path(*args.md.split("/"))
        with io.open(md, "w", encoding="utf-8", newline="\n") as f:
            f.write(render_queue_md(doc) + "\n")
    if not args.quiet:
        print(json.dumps(doc, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
