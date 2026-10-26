#!/usr/bin/env python3
"""目录重建工具（ADR-0005）。

解析 SUMMARY.md，把非别名条目映射到规范路径 <letter>/<slug>.md，
生成英文侧（yuanwen/）重建工作包，供子代理补建骨架文件。

用法:
  python tools/rebuild_dir.py packages   # 生成工作包 + manifest + all-items.json
  python tools/rebuild_dir.py verify     # 核验镜像缺口/多余文件/跟踪文件状态
仅标准库；不访问网络。
"""
import difflib
import io
import json
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUMMARY = os.path.join(ROOT, "SUMMARY.md")
BASELINE = os.path.join(ROOT, "baseline", "entries.json")
SNAPSHOT = os.path.join(ROOT, ".github", "sep-baseline", "official-snapshot.json")
YUANWEN = os.path.join(ROOT, "yuanwen")
OUT = os.path.join(ROOT, "specs", "001-sep-sync-pipeline", "dir-rebuild")

PROJECT_PREFIXES = ("pending/", "rules/", ".zcode/", ".specify/")
PROJECT_FILES = {"SUMMARY.md", "mu-lu-s.md", "yi-zhe-shuo-ming.md", "PROGRESS.md"}
CJK = re.compile(r"[\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
AUTHORS_TAIL = re.compile(r"\(([^()]*)\)\s*$")
PATH_SLUG = re.compile(r"^([A-Za-z0-9])/([A-Za-z0-9][A-Za-z0-9.\-]*)\.md$")
LINE = re.compile(r"^(\s*)\* \[(.+)\]\((.+)\)\s*$")


def norm(s):
    """规范化标题为 slug 候选：小写、去撇号、其余非字母数字切分为连字符。"""
    s = s.lower().replace("\u2019", "").replace("'", "")
    return "-".join(re.findall(r"[a-z0-9]+", s))


def parse_summary():
    entries = []
    with open(SUMMARY, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            m = LINE.match(line.rstrip("\n"))
            if not m:
                continue
            title, path = m.group(2), m.group(3)
            title = title.replace("\\*", "*").replace("\\[", "[").replace("\\]", "]")
            entries.append({"line_no": i, "indent": len(m.group(1)), "title": title, "path": path})
    return entries


def split_title(title):
    """剥掉占位星号与末尾作者括号，切出英文标题部分。"""
    t = title.lstrip("* ").strip()
    authors = ""
    m = AUTHORS_TAIL.search(t)
    if m:
        authors = m.group(1).strip()
        t = t[: m.start()].strip()
    idx = None
    for mm in CJK.finditer(t):
        idx = mm.end()
    english = t[idx:].strip(" -–—·") if idx is not None else t.strip()
    if not re.search(r"[A-Za-z]", english):
        english = ""
    return english, authors


def build_inventory():
    """yuanwen 单字符目录内文件名 stem 规范化索引（assets 等不参与）。"""
    inv = {}
    if not os.path.isdir(YUANWEN):
        return inv
    for d in sorted(os.listdir(YUANWEN)):
        if not re.fullmatch(r"[a-z0-9]", d):
            continue
        for fn in os.listdir(os.path.join(YUANWEN, d)):
            stem, ext = os.path.splitext(fn)
            if ext == ".md":
                inv.setdefault(norm(stem), []).append(d + "/" + fn)
    return inv


def load_snapshot():
    """官方快照 norm(title) -> [(slug, authors), ...]；slug 为 SEP 权威命名。"""
    idx = {}
    try:
        with open(SNAPSHOT, encoding="utf-8") as f:
            data = json.load(f)
        for slug, meta in (data.get("main") or {}).items():
            t = (meta or {}).get("title") or ""
            if t:
                idx.setdefault(norm(t), []).append((slug, (meta or {}).get("authors") or ""))
    except (OSError, ValueError):
        pass
    return idx


def load_baseline():
    """baseline/entries.json 的 norm(title)->slug 索引。"""
    idx = {}
    try:
        with open(BASELINE, encoding="utf-8") as f:
            data = json.load(f)
        for e in data.get("entries", []):
            t = e.get("title") or ""
            if t and e.get("slug"):
                idx.setdefault(norm(t), e["slug"])
    except (OSError, ValueError):
        pass
    return idx


def author_overlap(a, b):
    """作者串的词级重合率，用于同名标题消歧。"""
    wa = set(re.findall(r"[a-z]+", a.lower()))
    wb = set(re.findall(r"[a-z]+", b.lower()))
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / max(len(wa), len(wb))


def derive_slug(path, eng, authors, inv, bl, snap):
    """取证优先级：官方快照 > SUMMARY 单段路径 > yuanwen 文件名 > baseline 标题
    > 快照模糊匹配 > 标题推导。同名候选以作者重合消歧。"""
    if eng:
        n = norm(eng)
        cands = snap.get(n) or []
        if len(cands) == 1:
            return cands[0][0], "snapshot"
        if len(cands) > 1:
            best = max(cands, key=lambda c: author_overlap(authors, c[1]))
            if author_overlap(authors, best[1]) >= 0.4:
                return best[0], "snapshot"
            return "", "needs_review:" + ",".join(c[0] for c in cands)
    m = PATH_SLUG.match(path)
    if m:
        return m.group(2), "path"
    if eng:
        n = norm(eng)
        if n in inv:
            return inv[n][0].split("/")[1][:-3], "yuanwen"
        if n in bl:
            return bl[n], "baseline"
        close = difflib.get_close_matches(n, list(snap), n=2, cutoff=0.9)
        if len(close) == 1 or (len(close) == 2 and close[0] != close[1]
                               and difflib.SequenceMatcher(None, n, close[0]).ratio()
                               > difflib.SequenceMatcher(None, n, close[1]).ratio() + 0.05):
            cands = snap[close[0]]
            if author_overlap(authors, cands[0][1]) >= 0.4 or not authors:
                return cands[0][0], "snapshot-fuzzy"
        if n:
            return n, "derived"
    return "", "needs_review"


def classify():
    entries = parse_summary()
    inv = build_inventory()
    bl = load_baseline()
    snap = load_snapshot()

    stats = {"total": len(entries), "alias": 0, "project": 0,
             "entry": 0, "exists": 0, "create": 0, "review": 0}
    conf_count = {}
    items, seen = [], {}
    sep_stack = []  # (indent, item) 栈：为子词条提供母词条上下文

    for e in entries:
        title, path = e["title"], e["path"]
        if "— see" in title or "——见" in title:
            stats["alias"] += 1
            continue
        if path.startswith(PROJECT_PREFIXES) or path in PROJECT_FILES:
            stats["project"] += 1
            continue
        eng, authors = split_title(title)
        slug, conf = derive_slug(path, eng, authors, inv, bl, snap)
        note = ""
        if conf.startswith("needs_review:") and not slug:
            note = "同名候选: " + conf.split(":", 1)[1]
            conf = "needs_review"
        letter = slug[0].lower() if slug and re.fullmatch(r"[a-z0-9]", slug[0].lower()) else ""
        action = "create"
        if not slug or not letter:
            slug = letter = ""
            action = "review"
        else:
            target = letter + "/" + slug + ".md"
            if target in seen:
                prev = seen[target]
                if norm(prev["english"]) == norm(eng):
                    continue  # 同一条目重复出现，合并
                note = "slug 与 line %d 冲突" % prev["line_no"]
                conf, action = "conflict", "review"
            else:
                seen[target] = {"english": eng, "line_no": e["line_no"]}
                if os.path.isfile(os.path.join(YUANWEN, letter, slug + ".md")):
                    action = "skip"
                elif conf == "derived" and not authors:
                    # 无作者且官方快照无此条目：疑为纯导航节点（ADR-0005 决策 5）
                    note = "无作者且快照无此条目，疑为纯导航节点"
                    conf, action = "derived-nav", "review"
        while sep_stack and sep_stack[-1][0] >= e["indent"]:
            sep_stack.pop()
        parent = sep_stack[-1][1] if sep_stack and sep_stack[-1][0] < e["indent"] else None
        if action != "review":
            stats["entry"] += 1
            conf_count[conf] = conf_count.get(conf, 0) + 1
            stats["exists" if action == "skip" else "create"] += 1
        else:
            stats["review"] += 1
        item = {"line_no": e["line_no"], "title": title, "path": path,
                "english": eng, "authors": authors, "slug": slug, "letter": letter,
                "conf": conf, "action": action}
        if note:
            item["note"] = note
        if parent:
            item["parent_title"] = parent.get("title", "")
            if parent.get("slug"):
                item["parent_slug"] = parent["slug"]
        item["_indent"] = e["indent"]
        if slug:
            item_for_stack = dict(item)
            sep_stack.append((e["indent"], item_for_stack))
        items.append(item)

    return items, stats, conf_count


def main_packages():
    items, stats, conf_count = classify()
    os.makedirs(os.path.join(OUT, "packages"), exist_ok=True)

    by_letter = {}
    for it in items:
        if it["action"] == "skip":
            continue  # 工作包只装需动手的条目；全量清单在 all-items.json
        by_letter.setdefault(it["letter"] or "zz", []).append(it)

    # 小目录归并成组，目标每组 <=120 条可动条目
    groups, cur, cur_n = [], [], 0
    for key in sorted(by_letter):
        n = len(by_letter[key])
        if cur and cur_n + n > 120:
            groups.append(cur)
            cur, cur_n = [], 0
        cur.append(key)
        cur_n += n
    if cur:
        groups.append(cur)

    group_files = []
    for gi, keys in enumerate(groups, 1):
        name = "group-%02d" % gi
        merged = [it for k in keys for it in by_letter[k]]
        with open(os.path.join(OUT, "packages", name + ".json"), "w", encoding="utf-8") as f:
            json.dump({"group": name, "letters": keys, "items": merged}, f, ensure_ascii=False, indent=1)
        creates = sum(1 for x in merged if x["action"] == "create")
        reviews = sum(1 for x in merged if x["action"] == "review")
        group_files.append(name)
        print("%s: letters=%s items=%d create=%d review=%d" % (name, "".join(keys), len(merged), creates, reviews))

    with open(os.path.join(OUT, "all-items.json"), "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
    manifest = {"stats": stats, "conf": conf_count, "groups": group_files,
                "letters": {k: len(v) for k, v in sorted(by_letter.items())}}
    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("manifest:", json.dumps({**stats, "conf": conf_count}, ensure_ascii=False))


def main_verify():
    with open(os.path.join(OUT, "all-items.json"), encoding="utf-8") as f:
        items = json.load(f)
    inv = build_inventory()
    canonical = {it["letter"] + "/" + it["slug"] + ".md" for it in items
                 if it.get("slug") and it.get("action") != "review"}
    have = {p for paths in inv.values() for p in paths}
    missing = sorted(canonical - have)
    extras = sorted(have - canonical)
    print("canonical=%d have=%d missing=%d extras=%d" % (len(canonical), len(have), len(missing), len(extras)))
    with open(os.path.join(OUT, "missing.json"), "w", encoding="utf-8") as f:
        json.dump(missing, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "extras.json"), "w", encoding="utf-8") as f:
        json.dump(extras, f, ensure_ascii=False, indent=1)
    st = subprocess.run(["git", "status", "--porcelain", "yuanwen/"], cwd=ROOT,
                        capture_output=True, text=True)
    changed = [l for l in st.stdout.splitlines() if l.startswith(" M") or l.startswith("M ")]
    print("git modified tracked files in yuanwen/: %d" % len(changed))
    for l in changed:
        print(" ", l)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "packages"
    if cmd == "packages":
        main_packages()
    elif cmd == "verify":
        main_verify()
    else:
        print(__doc__)
        sys.exit(2)
