# -*- coding: utf-8 -*-
"""SEP 上游同步检查脚本。

抓取 https://plato.stanford.edu/contents.html，与已提交的基线快照
（.github/sep-baseline/official-snapshot.json）比对，报告上游变化；
并对 SUMMARY.md 做尽力匹配，提示受影响的本地词条文件。

用法：
    python .github/scripts/sep_sync_check.py                    # 检查（CI / 本地）
    python .github/scripts/sep_sync_check.py --write-baseline   # 人工核对变化并落地后，更新基线

退出码：0 = 运行成功（无论有无变化，结果见 status.json）；2 = 严重错误。
设计原则：本脚本只报告、不修改任何内容文件；SUMMARY.md 与 mu-lu-s.md
的更新必须由人工核对后进行。
"""
import argparse, html as htmlmod, io, json, os, re, sys, time, unicodedata
import urllib.request, urllib.error

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEP_URL = "https://plato.stanford.edu/contents.html"
MIN_MAIN_ENTRIES = 1500      # 解析护栏：官方主条目数低于此值视为页面改版/解析失败
MIN_BYTES = 100000           # 内容护栏：响应过小视为异常
RETRIES = 3

def norm(s):
    """归一化：去 HTML 实体后已在解析层完成；此处去变音符、去非字母数字。"""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("ø", "o").replace("ł", "l").replace("æ", "ae").replace("ß", "ss")
    return re.sub(r"[^a-z0-9]+", "", s.lower())

def fetch(url):
    last_err = None
    for attempt in range(1, RETRIES + 1):
        try:
            req = urllib.request.Request(
                url + ("?sync=%d" % int(time.time())),
                headers={"User-Agent": "SEP-CN-sync-check/1.0 (GitHub Actions; repo taophilosophy/SEP-CN)"},
            )
            with urllib.request.urlopen(req, timeout=90) as resp:
                return resp.read()
        except Exception as e:  # 网络/限流等，退避重试
            last_err = e
            if attempt < RETRIES:
                time.sleep(15 * attempt)
    raise RuntimeError("抓取失败（重试 %d 次）：%s" % (RETRIES, last_err))

def parse_contents(raw):
    """行级解析官方目录。返回 (main: {slug: {title, authors}}, alias: [{alias, slug}], dup_slugs)。"""
    text = htmlmod.unescape(raw.decode("utf-8", errors="replace"))
    main, alias, dup = {}, [], []
    li_re = re.compile(r"\s*<li>\s*(.*?)\s*(?:</li>)?\s*$", re.S)
    alias_re = re.compile(r"^(.*?)\s*[—–]\s*see\s+")
    for line in text.splitlines():
        if 'href="entries/' not in line:
            continue
        sm = re.search(r'href="entries/([^"/]+)/"', line)
        if not sm:
            continue
        slug = sm.group(1)
        lm = li_re.match(line)
        inner = lm.group(1) if lm else line
        am = alias_re.match(inner)
        if am and "<strong>" not in inner:
            alias.append({"alias": re.sub(r"<[^>]+>", "", am.group(1)).strip(), "slug": slug})
            continue
        tm = re.search(r"<strong>(.*?)</strong>", inner)
        if not tm:
            continue
        title = re.sub(r"<[^>]+>", "", tm.group(1)).strip()
        authors = re.sub(r"<[^>]+>", "", inner[tm.end():])
        authors = re.sub(r"\s+", " ", authors).strip().strip("()").strip()
        if slug in main:
            dup.append(slug)
        main[slug] = {"title": title, "authors": authors}
    return main, alias, dup

def auth_norm(a):
    return frozenset(x for x in (norm(t) for t in re.sub(r"\s+and\s+", ",", a or "").split(",")) if x)

def parse_summary_paths():
    """从 SUMMARY.md 提取 (title, path) 列表，用于尽力提示受影响的本地文件。"""
    out = []
    path_re = re.compile(r"^\s*\*\s+\[([^\]]*)\]\(([^)]*)\)\s*$")
    try:
        with open(os.path.join(ROOT, "SUMMARY.md"), encoding="utf-8") as f:
            for line in f:
                m = path_re.match(line.rstrip("\n"))
                if m:
                    out.append((m.group(1).replace("\\*", "*").strip(), m.group(2).strip()))
    except OSError:
        pass
    return out

def local_hints(slugs, summary_entries):
    """对给定 slug，尽力在 SUMMARY 中找路径包含它的条目（仅为提示，可能漏报/误报）。"""
    res = {}
    for slug in slugs:
        ns = norm(slug)
        if len(ns) < 6:
            continue
        hits = [t for t, p in summary_entries if ns in norm(os.path.basename(p))]
        if hits:
            res[slug] = hits[:5]
    return res

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", default=os.path.join(ROOT, ".github", "sep-baseline", "official-snapshot.json"))
    ap.add_argument("--out-dir", default=os.path.join(ROOT, ".github", "sep-sync-report"))
    ap.add_argument("--write-baseline", action="store_true",
                    help="把本次抓取写为新基线（仅在人工核对变化并落地 SUMMARY/mu-lu-s 之后使用）")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    report = {"status": "clean", "fetched_at": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()), "url": SEP_URL}

    try:
        raw = fetch(SEP_URL)
    except Exception as e:
        report.update(status="fetch-error", error=str(e))
        finish(report, args, code=0)
        return
    if len(raw) < MIN_BYTES:
        report.update(status="fetch-error", error="响应过小（%d 字节），疑似异常页面" % len(raw))
        finish(report, args, code=0)
        return

    main, alias, dup = parse_contents(raw)
    if len(main) < MIN_MAIN_ENTRIES:
        report.update(status="parse-error",
                      error="解析得到 %d 条主条目（低于护栏 %d），官方页面结构可能已改版，解析器需人工更新" % (len(main), MIN_MAIN_ENTRIES))
        finish(report, args, code=0)
        return
    report["official_counts"] = {"main": len(main), "alias": len(alias), "duplicate_slugs": dup}

    if args.write_baseline:
        os.makedirs(os.path.dirname(args.baseline), exist_ok=True)
        json.dump({"fetched_at": report["fetched_at"], "main": main, "alias": alias},
                  open(args.baseline, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        report.update(status="baseline-written",
                      note="基线已更新：%s（请将该文件随人工核对的改动一并提交）" % os.path.relpath(args.baseline, ROOT))
        finish(report, args, code=0)
        return

    if not os.path.isfile(args.baseline):
        report.update(status="no-baseline", error="基线不存在：%s；请先运行 --write-baseline 建立基线" % args.baseline)
        finish(report, args, code=0)
        return

    base = json.load(open(args.baseline, encoding="utf-8"))
    b_main, b_alias = base.get("main", {}), base.get("alias", [])
    b_alias_n = {norm(a["alias"]): a for a in b_alias}
    n_alias_n = {norm(a["alias"]): a for a in alias}

    added = [s for s in main if s not in b_main]
    removed = [s for s in b_main if s not in main]
    title_chg = [{"slug": s, "old": b_main[s]["title"], "new": main[s]["title"]}
                 for s in main if s in b_main and norm(main[s]["title"]) != norm(b_main[s]["title"])]
    auth_chg = [{"slug": s, "old": b_main[s]["authors"], "new": main[s]["authors"]}
                for s in main if s in b_main and auth_norm(main[s]["authors"]) != auth_norm(b_main[s]["authors"])]
    alias_added = [a["alias"] for k, a in n_alias_n.items() if k not in b_alias_n]
    alias_removed = [a["alias"] for k, a in b_alias_n.items() if k not in n_alias_n]

    drift = bool(added or removed or title_chg or auth_chg or alias_added or alias_removed or dup)
    summary_entries = parse_summary_paths()
    touched = local_hints(added + [c["slug"] for c in title_chg], summary_entries)

    report.update(status="drift" if drift else "clean", baseline_fetched_at=base.get("fetched_at", "未知"),
                  added_main=added, removed_main=removed, title_changed=title_chg,
                  authors_changed=auth_chg, aliases_added=alias_added, aliases_removed=alias_removed,
                  duplicate_slugs=dup, affected_local_hints=touched)
    finish(report, args, code=0)

def finish(report, args, code):
    json.dump(report, open(os.path.join(args.out_dir, "status.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    open(os.path.join(args.out_dir, "report.md"), "w", encoding="utf-8").write(render_md(report))
    print("STATUS: %s" % report["status"])
    print(json.dumps({k: report[k] for k in report if k not in ("status",)}, ensure_ascii=False)[:2000])
    sys.exit(code)

def render_md(r):
    L = ["## SEP 上游同步报告", "", "- 抓取时间：%s" % r.get("fetched_at", "?"),
         "- 官方条目数：主 %s / 别名 %s" % (r.get("official_counts", {}).get("main", "?"), r.get("official_counts", {}).get("alias", "?")),
         "- 基线时间：%s" % r.get("baseline_fetched_at", "—"), ""]
    st = r.get("status")
    if st in ("fetch-error", "parse-error", "no-baseline"):
        L += ["**⚠️ 本次检查未完成（%s）**：%s" % (st, r.get("error", "")), "",
              "请人工排查后重跑；不要据此改动任何内容文件。"]
        return "\n".join(L)
    if st == "baseline-written":
        L += ["✅ %s" % r.get("note", "基线已更新")]
        return "\n".join(L)
    if st == "clean":
        L += ["✅ 上游无变化。"]
        return "\n".join(L)
    L += ["**🔔 检测到上游变化**，请人工核对后更新 `SUMMARY.md` / `mu-lu-s.md`；", "",
          "### 新增条目（%d）" % len(r.get("added_main", []))]
    L += ["- `%s`" % s for s in r.get("added_main", [])] or ["（无）"]
    L += ["", "### 撤下条目（%d，切勿自动删除，先人工核实是否真被撤下）" % len(r.get("removed_main", []))]
    L += ["- `%s`" % s for s in r.get("removed_main", [])] or ["（无）"]
    tc = r.get("title_changed", [])
    L += ["", "### 标题变更（%d）" % len(tc)]
    L += ["- `%s`：%s → %s" % (c["slug"], c["old"], c["new"]) for c in tc] or ["（无）"]
    ac = r.get("authors_changed", [])
    L += ["", "### 作者变更（%d）" % len(ac)]
    L += ["- `%s`：%s → %s" % (c["slug"], c["old"], c["new"]) for c in ac] or ["（无）"]
    L += ["", "### 别名增删", "- 新增别名：%s" % ("、".join(r.get("aliases_added", [])) or "（无）"),
          "- 移除别名：%s" % ("、".join(r.get("aliases_removed", [])) or "（无）")]
    if r.get("duplicate_slugs"):
        L += ["", "### ⚠️ 官方目录中出现重复 slug"]
        L += ["- `%s`" % s for s in r["duplicate_slugs"]]
    hints = r.get("affected_local_hints", {})
    if hints:
        L += ["", "### 受影响本地文件提示（尽力匹配，须人工确认）"]
        for s, hs in hints.items():
            L += ["- `%s` → %s" % (s, "；".join(hs))]
    L += ["", "---", "处理流程见《分类目录核查建议书》第十节：核对变化 → 更新 SUMMARY/mu-lu-s → ",
          "`python .github/scripts/sep_sync_check.py --write-baseline` 更新基线 → 基线随改动一并提交。"]
    return "\n".join(L)

if __name__ == "__main__":
    main()
