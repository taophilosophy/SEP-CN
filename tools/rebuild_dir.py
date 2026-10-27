#!/usr/bin/env python3
"""上游同构重建工具（ADR-0007）。

词条目录形态：仓库根 <slug>/index.md（中文）与 yuanwen/<slug>/index.md（英文），
与上游 entries/<slug>/ 同构（省 entries/ 层）。SUMMARY 条目链接 <slug>/index.md，
别名行保留并链到目标词条。

用法:
  python tools/rebuild_dir.py rebuild    # 重写 SUMMARY.md 与 mu-lu-s.md 链接
  python tools/rebuild_dir.py stubs      # 中文侧骨架 <slug>/index.md（仅 H1）
  python tools/rebuild_dir.py yuanwen    # yuanwen 扁平迁移 + 英文侧补缺
  python tools/rebuild_dir.py check      # 核验链接解析与镜像覆盖
仅标准库；不访问网络。
"""
import difflib
import io
import json
import os
import re
import shutil
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPSHOT = os.path.join(ROOT, ".github", "sep-baseline", "official-snapshot.json")
OUT = os.path.join(ROOT, "specs", "001-sep-sync-pipeline", "dir-rebuild")
CJK = re.compile(r"[\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
AUTHORS_TAIL = re.compile(r"\(([^()]*)\)\s*$")
LINE = re.compile(r"^(\s*)\* \[(.+)\]\((.+)\)\s*$")

# 前置项目页：标题 -> 规范路径（12 页，全部已存在于 qian-yan/ 与 guan-yu/）
FRONT = {
    "斯坦福哲学百科全书简体中文版": "README.md",
    "分类目录": "mu-lu-s.md",
    "版权说明": "qian-yan/ban-quan-shuo-ming.md",
    "日志与编辑规划": "qian-yan/ri-zhi-yu-bian-ji-gui-hua.md",
    "词汇表": "qian-yan/ci-hui-biao.md",
    "编辑信息": "guan-yu/bian-ji-xin-xi.md",
    "关于 SEP": "guan-yu/guan-yu-sep.md",
    "编委会": "guan-yu/bian-wei-hui.md",
    "如何引用 SEP": "guan-yu/ru-he-yin-yong-sep.md",
    "特殊字符": "guan-yu/te-shu-zi-fu.md",
    "高级工具": "guan-yu/gao-ji-gong-ju.md",
    "联系信息": "guan-yu/lian-xi-xin-xi.md",
}
JUNK_PREFIXES = (".zcode/", ".specify/", "tools/", "rules/", "fang-fa-lun/", "jian-yi-shu/", "specs/")
JUNK_FILES = {"AGENTS.md", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "PROGRESS.md",
              "SUMMARY.md", "yi-zhe-shuo-ming.md"}


def norm(s):
    s = s.lower().replace("\u2019", "").replace("'", "")
    return "-".join(re.findall(r"[a-z0-9]+", s))


def unescape(t):
    return t.replace("\\*", "*").replace("\\[", "[").replace("\\]", "]")


def split_title(title):
    """剥占位星号与末尾作者括号，切出英文标题部分。"""
    t = unescape(title).lstrip("* ").strip()
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


def author_overlap(a, b):
    wa = set(re.findall(r"[a-z]+", a.lower()))
    wb = set(re.findall(r"[a-z]+", b.lower()))
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / max(len(wa), len(wb))


def load_snapshot():
    with open(SNAPSHOT, encoding="utf-8") as f:
        data = json.load(f)
    main = data.get("main") or {}
    by_title = {}
    for slug, meta in main.items():
        t = (meta or {}).get("title") or ""
        if t:
            by_title.setdefault(norm(t), []).append((slug, (meta or {}).get("authors") or ""))
    alias = {}
    for a in data.get("alias") or []:
        name = (a or {}).get("alias") or ""
        if name and a.get("slug"):
            alias.setdefault(norm(name), a["slug"])
    return main, by_title, alias


def entry_slug(english, authors, by_title, tokset=None):
    """官方快照标题匹配，同名以作者重合消歧；词集与模糊兜底；无解返回 None。"""
    n = norm(english) if english else ""
    if not n:
        return None
    cands = by_title.get(n) or []
    if len(cands) == 1:
        return cands[0][0]
    if len(cands) > 1:
        best = max(cands, key=lambda c: author_overlap(authors, c[1]))
        if author_overlap(authors, best[1]) >= 0.4:
            return best[0]
        return None
    # 词集兜底（忽略冠词 the）：语序颠倒（"animals, moral status of" ≡ "The Moral Status of Animals"）
    if tokset is not None:
        toks = frozenset(n.split("-")) - {"the"}
        keys = tokset.get(toks) or []
        slugs = []
        for k in keys:
            for slug, aut in by_title[k]:
                if not authors or author_overlap(authors, aut) >= 0.4:
                    slugs.append(slug)
        if len(set(slugs)) == 1:
            return slugs[0]
        # 截断标题兜底：SUMMARY 英文是快照标题去集群前缀后的后缀（≥2 词、唯一命中）
        if len(n.split("-")) >= 2:
            tail = [k for k in by_title if k.endswith("-" + n)]
            if len(tail) == 1:
                return by_title[tail[0]][0][0]
        # 子条目短标题匹配：SUMMARY 全称（"Animals, moral status of"）以快照短标题结尾
        if len(n.split("-")) >= 3:
            hits = [k for k in by_title if k != n and len(n) - len(k) >= 4
                    and n.endswith("-" + k) and len(k.split("-")) >= 2]
            if len(hits) == 1:
                return by_title[hits[0]][0][0]
            if len(hits) > 1:
                cands = [s for k in hits for s, aut in by_title[k]
                         if not authors or author_overlap(authors, aut) >= 0.4]
                if len(set(cands)) == 1:
                    return cands[0]
    close = difflib.get_close_matches(n, list(by_title), n=2, cutoff=0.85)
    if len(close) == 1 or (len(close) == 2 and close[0] != close[1]
                           and difflib.SequenceMatcher(None, n, close[0]).ratio()
                           > difflib.SequenceMatcher(None, n, close[1]).ratio() + 0.05):
        cands = by_title[close[0]]
        # 模糊匹配必须有作者重合佐证（无作者行可能是导航节点，禁走模糊兜底）
        if authors and author_overlap(authors, cands[0][1]) >= 0.4:
            return cands[0][0]
    return None


def parse_lines(path):
    out = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            m = LINE.match(line.rstrip("\n"))
            out.append((i, m, line.rstrip("\n")))
    return out


class Mapper:
    def __init__(self):
        self.main, self.by_title, self.alias = load_snapshot()
        self.tokset = {}
        for k in self.by_title:
            self.tokset.setdefault(frozenset(k.split("-")) - {"the"}, []).append(k)
        self.used = {}       # slug -> line_no（去重）
        self.review = []     # 无法解析被丢弃/挂起的行
        self.children = set()  # 有更深缩进子行的行号（导航节点判定用）
        self.deferred = []     # 派生 slug 行：finalize 二次裁决
        self.deferred_drop = set()
        self.stats = {"front": 0, "entry": 0, "alias": 0, "dup": 0, "junk": 0, "nav": 0, "review": 0}

    def finalize(self):
        """derived 行二次裁决：正式条目已占用的 slug 让位（真实条目优先于派生/导航行）。"""
        for dslug, line_no, title, old_path in self.deferred:
            if dslug in self.used:
                self.stats["dup"] += 1
                self.deferred_drop.add(line_no)
                self.review.append({"line_no": line_no, "title": title, "path": old_path,
                                    "reason": "派生 slug %s 与正式条目重复，行已移除" % dslug})
            else:
                self.used[dslug] = line_no

    def resolve(self, title, old_path, line_no):
        """返回新路径或 None（丢弃）。"""
        if title.strip() in FRONT:
            self.stats["front"] += 1
            return FRONT[title.strip()]
        if old_path.startswith(JUNK_PREFIXES) or old_path in JUNK_FILES:
            if title.strip() not in FRONT:
                self.stats["junk"] += 1
                self.review.append({"line_no": line_no, "title": title, "path": old_path,
                                    "reason": "开发文档/垃圾链接，已从 SUMMARY 移除"})
                return None
        if "— see" in title or "——见" in title:
            # 别名：取 "— see" 之前、"——见/—见" 之后的英文别名文本，在快照 alias 表映射到目标
            left = title.split("— see")[0]
            if "——见" in left:
                left = left.split("——见")[-1]
            elif "—见" in left:
                left = left.split("—见")[-1]
            eng, _ = split_title(left)
            target = self.alias.get(norm(eng)) if eng else None
            if not target:
                # 兜底：右段（see 之后）按目标条目标题匹配
                right = title.split("— see", 1)[-1].split("——见", 1)[-1]
                reng, raut = split_title(right)
                target = entry_slug(reng, raut, self.by_title, self.tokset)
            if not target:
                self.stats["review"] += 1
                self.review.append({"line_no": line_no, "title": title, "path": old_path,
                                    "reason": "别名目标无法解析"})
                return None
            # 别名指向的目标可与正文条目同 slug（这正是 see-alias 的语义），不占用 used
            self.stats["alias"] += 1
            return target + "/index.md"
        eng, authors = split_title(title)
        slug = entry_slug(eng, authors, self.by_title, self.tokset)
        if slug and slug in self.used:
            self.stats["dup"] += 1
            self.review.append({"line_no": line_no, "title": title, "path": old_path,
                                "reason": "slug 与其他行重复"})
            return None
        if slug:
            self.used[slug] = line_no
            self.stats["entry"] += 1
            return slug + "/index.md"
        # 解析失败：真实条目（有作者）保留派生 slug 行待人工核对；导航节点保留缩进链 README
        if authors and eng:
            dslug = norm(eng)
            if dslug:
                # 路径暂定，不占用 used；finalize 中正式条目优先
                self.deferred.append((dslug, line_no, title, old_path))
                self.stats["entry"] += 1
                self.review.append({"line_no": line_no, "title": title, "path": old_path,
                                    "reason": "英文标题与快照不匹配，已用派生 slug %s，待人工核对" % dslug})
                return dslug + "/index.md"
        if line_no in self.children:
            self.stats["nav"] += 1
            self.review.append({"line_no": line_no, "title": title, "path": old_path,
                                "reason": "纯导航节点（无作者、快照无对应条目页），链到 README"})
            return "README.md"
        self.stats["review"] += 1
        self.review.append({"line_no": line_no, "title": title, "path": old_path,
                            "reason": "无法解析（无作者且无子词条）"})
        return None


def rewrite_toc(src, dst, mapper):
    lines = parse_lines(src)
    for idx in range(len(lines) - 1):
        i, m, _ = lines[idx]
        j, m2, _2 = lines[idx + 1]
        if m and m2 and len(m2.group(1)) > len(m.group(1)):
            mapper.children.add(i)
    pend = []
    for i, m, raw in lines:
        if not m:
            continue
        indent, title, old_path = m.group(1), m.group(2), m.group(3)
        newp = mapper.resolve(title, old_path, i)
        if newp is None:
            continue
        pend.append((i, indent, title, newp))
    mapper.finalize()
    out, kept = [], 0
    for i, m, raw in lines:
        if not m:
            out.append(raw)
            continue
        if m.group(0) and i in mapper.deferred_drop:
            continue
        hit = next(((ind, t, p) for ln, ind, t, p in pend if ln == i), None)
        if hit is None:
            continue
        ind, t, p = hit
        out.append("%s* [%s](%s)" % (ind, t, p))
        kept += 1
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    return kept


def cmd_rebuild():
    sm = Mapper()
    n1 = rewrite_toc(os.path.join(ROOT, "SUMMARY.md"), os.path.join(ROOT, "SUMMARY.md"), sm)
    mm = Mapper()
    n2 = rewrite_toc(os.path.join(ROOT, "mu-lu-s.md"), os.path.join(ROOT, "mu-lu-s.md"), mm)
    print("SUMMARY kept=%d stats=%s" % (n1, json.dumps(sm.stats, ensure_ascii=False)))
    print("mu-lu-s kept=%d stats=%s" % (n2, json.dumps(mm.stats, ensure_ascii=False)))
    with open(os.path.join(OUT, "rebuild-review.json"), "w", encoding="utf-8") as f:
        json.dump({"summary": sm.review, "mu-lu-s": mm.review}, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "slug-map.json"), "w", encoding="utf-8") as f:
        json.dump({s: {"line_no": ln} for s, ln in sorted(sm.used.items())}, f, ensure_ascii=False, indent=1)
    print("review items: %d" % (len(sm.review) + len(mm.review)))


def cmd_stubs():
    lines = parse_lines(os.path.join(ROOT, "SUMMARY.md"))
    created = skipped = 0
    for i, m, raw in lines:
        if not m:
            continue
        title, path = m.group(2), m.group(3)
        mm = re.fullmatch(r"([a-z0-9])/([A-Za-z0-9][A-Za-z0-9.\-]*)\.md", path)
        if not mm:
            continue
        d = os.path.join(ROOT, mm.group(1))
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, path)
        if os.path.exists(p):
            skipped += 1
            continue
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("# " + unescape(title) + "\n")
        created += 1
    print("chinese stubs created=%d skipped=%d" % (created, skipped))


def cmd_toletters():
    """ADR-0009 一次性迁移：根级 <slug>.md → <letter>/<slug>.md；yuanwen 同构；SUMMARY/mu-lu-s 链接改写。"""
    tracked = set(l.strip() for l in subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.splitlines() if l.strip())
    moved = git_moved = 0

    def mv(src, dst, is_tracked):
        nonlocal moved, git_moved
        if os.path.exists(dst):
            print("  碰撞跳过:", dst)
            return
        d = os.path.dirname(dst)
        if d:
            os.makedirs(d, exist_ok=True)
        if is_tracked:
            subprocess.run(["git", "mv", src, dst], cwd=ROOT, check=True, capture_output=True)
            git_moved += 1
        else:
            os.rename(src, dst)
        moved += 1

    def letter_of(stem):
        return stem[0].lower() if re.fullmatch(r"[A-Za-z0-9]", stem[:1]) else "1"

    skip_roots = {"README.md", "SUMMARY.md", "mu-lu-s.md", "PROGRESS.md", "yi-zhe-shuo-ming.md",
                  "AGENTS.md", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md"}

    # 1) 中文侧：根级 <slug>.md → <letter>/<slug>.md
    for fn in sorted(os.listdir(ROOT)):
        stem, ext = os.path.splitext(fn)
        if ext != ".md" or fn in skip_roots:
            continue
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.\-]*", stem):
            continue
        mv(fn, letter_of(stem) + "/" + fn, fn in tracked)

    # 2) 英文侧 yuanwen：<slug>.md / <slug>.<x>.md → <letter>/<...>
    yw = os.path.join(ROOT, "yuanwen")
    for fn in sorted(os.listdir(yw)) if os.path.isdir(yw) else []:
        stem, ext = os.path.splitext(fn)
        if ext != ".md" or fn == "SUMMARY.md":
            continue
        base = stem.split(".", 1)[0]
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.\-]*", base):
            continue
        mv("yuanwen/" + fn, "yuanwen/" + letter_of(base) + "/" + fn, ("yuanwen/" + fn) in tracked)

    # 3) SUMMARY/mu-lu-s：](<slug>.md) → ](<letter>/<slug>.md)
    for name in ("SUMMARY.md", "mu-lu-s.md"):
        txt = open(os.path.join(ROOT, name), encoding="utf-8").read()

        def repl(m):
            path = m.group(1)
            if "/" in path or path in skip_roots:
                return m.group(0)
            stem = path[:-3]
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.\-]*", stem):
                return m.group(0)
            return "](%s/%s)" % (letter_of(stem), path)

        new, n = re.subn(r"\]\(([^)]+\.md)\)", repl, txt)
        if n:
            open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n").write(new)
        print("%s 链接改写 %d 处" % (name, n))
    print("toletters: moved=%d (git mv %d)" % (moved, git_moved))


def tracked_files():
    st = subprocess.run(["git", "ls-files", "yuanwen/"], cwd=ROOT, capture_output=True, text=True)
    return set(l.strip() for l in st.stdout.splitlines() if l.strip())


def cmd_flatten():
    """ADR-0008 一次性迁移：<slug>/index.md → <slug>.md；yuanwen 同构；SUMMARY/mu-lu-s 链接改写。"""
    tracked = set(l.strip() for l in subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.splitlines() if l.strip())
    moved = git_moved = 0

    def mv(src, dst, is_tracked):
        nonlocal moved, git_moved
        if os.path.exists(dst):
            print("  碰撞跳过:", dst)
            return
        if is_tracked:
            subprocess.run(["git", "mv", src, dst], cwd=ROOT, check=True, capture_output=True)
            git_moved += 1
        else:
            os.rename(src, dst)
        moved += 1

    # 1) 中文侧：根级 <slug>/index.md → <slug>.md（jian-yi-shu 为叙事拆分目录，不动）
    for d in sorted(os.listdir(ROOT)):
        dd = os.path.join(ROOT, d)
        if not os.path.isdir(dd) or d in ("yuanwen", "jian-yi-shu", "progress"):
            continue
        idx = os.path.join(dd, "index.md")
        if os.path.isfile(idx) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.\-]*", d):
            mv(d + "/index.md", d + ".md", d + "/index.md" in tracked)
        if os.path.isdir(dd) and not os.listdir(dd):
            os.rmdir(dd)

    # 2) 英文侧 yuanwen：<slug>/index.md → <slug>.md；<slug>/<x>.md → <slug>.<x>.md；图片 → assets/<slug>/
    yw = os.path.join(ROOT, "yuanwen")
    for d in sorted(os.listdir(yw)) if os.path.isdir(yw) else []:
        dd = os.path.join(yw, d)
        if not os.path.isdir(dd) or d in ("assets",):
            continue
        for fn in sorted(os.listdir(dd)):
            src = os.path.join(dd, fn)
            stem, ext = os.path.splitext(fn)
            if ext == ".md":
                rel = d + ".md" if fn == "index.md" else d + "." + stem + ".md"
            else:
                adir = os.path.join(yw, "assets", d)
                os.makedirs(adir, exist_ok=True)
                rel = "assets/" + d + "/" + fn
            mv("yuanwen/" + d + "/" + fn, os.path.join(yw, *rel.split("/")), ("yuanwen/" + d + "/" + fn) in tracked)
        if os.path.isdir(dd) and not os.listdir(dd):
            os.rmdir(dd)

    # 3) SUMMARY/mu-lu-s：](<slug>/index.md) → ](<slug>.md)
    for name in ("SUMMARY.md", "mu-lu-s.md"):
        txt = open(os.path.join(ROOT, name), encoding="utf-8").read()
        new, n = re.subn(r"\]\(([^)]+?)/index\.md\)", r"](\1.md)", txt)
        if n:
            open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n").write(new)
        print("%s 链接改写 %d 处" % (name, n))
    print("flatten: moved=%d (git mv %d)" % (moved, git_moved))


def cmd_check():
    bad = 0
    for name in ("SUMMARY.md", "mu-lu-s.md"):
        for i, m, raw in parse_lines(os.path.join(ROOT, name)):
            if not m:
                continue
            p = m.group(3)
            if not os.path.isfile(os.path.join(ROOT, *p.split("/"))):
                print("BROKEN %s:%d %s -> %s" % (name, i, m.group(2)[:40], p))
                bad += 1
    main, _, _ = load_snapshot()
    missing = [s for s in main
               if not os.path.isfile(os.path.join(ROOT, s[0].lower(), s + ".md"))
               or not os.path.isfile(os.path.join(ROOT, "yuanwen", s[0].lower(), s + ".md"))]
    print("broken links=%d ; snapshot entries without yuanwen mirror=%d / %d"
          % (bad, len(missing), len(main)))
    for s in missing[:10]:
        print("  ", s)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "rebuild":
        cmd_rebuild()
    elif cmd == "stubs":
        cmd_stubs()
    elif cmd == "flatten":
        cmd_flatten()
    elif cmd == "toletters":
        cmd_toletters()
    elif cmd == "check":
        cmd_check()
    else:
        print(__doc__)
        sys.exit(2)
