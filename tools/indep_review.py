# -*- coding: utf-8 -*-
"""独立形态审校扫描器（ADR-0047 独立审校流程的机检面）。

把横向缺陷类（跨件、与单件翻译状态无关的形态/正典化/一致性项）从零散挂账
收编为可复算的检查类，按字头分批执行。

用法:
  python tools/indep_review.py --scan [--class C]... [--letter A]...
  python tools/indep_review.py --classes          # 列出类别与判据
输出: stdout JSON {generated, scope, classes:{C:[{path,line,detail}...]}, counts:{...}}

类别（判据与权威见 rules/05、rules/07、ADR-0017/0046/0047）:
  bib-heading-form  参考文献节名非正典（W7）：zh 应为 `## 参考文献`
  pubinfo-form      出版信息行非斜体正典形 或 与 en 源有无不符（W8）
  bib-subsection    文献分类子标题丢失：en 有 Primary/Secondary Sources 而 zh 无分类子标题
  style             正文形态违例（check_style 全则，不含 quote-spacing）
  quote-adjacent    引号↔西文邻接缺空格（check_style 规则 quote-spacing）
  pairs             格式配对与引用一致七则（check_pairs，ADR-0046）

退出码: 0 扫描完成（告警级，不作门禁）；2 用法错误。
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import check_pairs, check_style  # noqa: E402
from tools.common import read_text  # noqa: E402

BIB_CANON = re.compile(r'^##\s*参考文献\s*$', re.M)
BIB_OLD = re.compile(r'^#{2,3}\s*(?:References（引用注释）|References|Bibliography)\s*$', re.M)
PUBINFO_LINE = re.compile(r'^>?\s*\*[^*\n]+\*\s*$')
PUBINFO_CANON = re.compile(r'^>?\s*\*首次发表于\s*\d{4}\s*年.*\*\s*$')
CJK = re.compile(r'[\u4e00-\u9fff]')
BIBSUB_ZH = re.compile(r'^#{3,4}\s*(?:主要文献|次要文献|主要来源|次要来源|一手文献|二手文献)',
                       re.M)
BIBSUB_EN = re.compile(r'<h3[^>]*>\s*(?:Primary|Secondary)\s+Sources?', re.I)

CLASSES = ("bib-heading-form", "pubinfo-form", "bib-subsection",
           "style", "quote-adjacent", "pairs")

# 已完整翻译的状态（存根与未动工件不属独立审校范围，ADR-0047）；旧名经 naming.json 归一
TRANSLATED = {"tr-02_checked", "tr-03_checked", "tr-04_checked", "rv-01_checked",
              "rv-02_checked", "rv-09_checked", "sg-01_checked", "sg-02_checked",
              "sg-03_checked", "done"}


def task_state(path):
    try:
        from tools import naming_lib
    except ImportError:  # 直连脚本运行（无包路径）
        import naming_lib
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    letter = os.path.basename(os.path.dirname(path))
    slug = os.path.splitext(os.path.basename(path))[0]
    p = os.path.join(root, "tasks", letter, slug + ".json")
    if not os.path.exists(p):
        return None
    try:
        t = json.load(io.open(p, encoding="utf-8"))
    except Exception:
        return None
    return naming_lib.normalize_state(t.get("state")) if isinstance(t, dict) else None


def zh_docs(letters=None):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = []
    for name in sorted(os.listdir(root)):
        if len(name) != 1 or not name.isalpha() or name != name.lower():
            continue
        if letters and name.upper() not in letters:
            continue
        d = os.path.join(root, name)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".md"):
                out.append(os.path.join(d, f))
    return out


def _en(path):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    slug = os.path.splitext(os.path.basename(path))[0]
    p = os.path.join(root, "en", slug, "index.html")
    return read_text(p) if os.path.exists(p) else None


def scan_bib_heading(path, text, en):
    hits = []
    for m in BIB_OLD.finditer(text):
        hits.append({"path": path, "line": text[:m.start()].count("\n") + 1,
                     "detail": "旧形态节名 %r（应为 `## 参考文献`）" % m.group(0).strip()})
    if not BIB_CANON.search(text) and not BIB_OLD.search(text) and en and "References" in en:
        hits.append({"path": path, "line": 0, "detail": "缺 `## 参考文献` 节"})
    return hits


def scan_pubinfo(path, text, en):
    hits = []
    lines = text.splitlines()
    found = False
    for i, ln in enumerate(lines, 1):
        if "首次发表于" not in ln or not PUBINFO_CANON.match(ln.rstrip()):
            if "首次发表于" in ln and (PUBINFO_LINE.match(ln) or ln.lstrip()[:1] in "*>"):
                if not PUBINFO_CANON.match(ln.rstrip()):
                    hits.append({"path": path, "line": i,
                                 "detail": "出版信息行非正典形（应 `*首次发表于 YYYY 年 M 月 D 日…*`）：%s"
                                           % ln.strip()[:50]})
            continue
        found = True
    if en:
        en_has = re.search(r"First published", en) is not None
        if en_has and not found:
            hits.append({"path": path, "line": 0,
                         "detail": "en 源有 First published 而 zh 缺出版信息行"})
        if not en_has and found:
            hits.append({"path": path, "line": 0,
                         "detail": "en 源无 First published 而 zh 有出版信息行"})
    return hits


def scan_bib_subsection(path, text, en):
    if not en or not BIBSUB_EN.search(en):
        return []
    if BIBSUB_ZH.search(text):
        return []
    return [{"path": path, "line": 0,
             "detail": "en 源书目含 Primary/Secondary Sources 分类，zh 未保留分类子标题"}]


def scan_style(path, text, en):
    issues, _warn = check_style.check_file(path)
    return issues


def scan_quote(path, text, en):
    issues, _warn = check_style.check_file(path)
    return [i for i in issues if i.get("rule") == "quote-spacing"]


def scan_pairs(path, text, en):
    return check_pairs.check_file(path)


SCANNERS = {
    "bib-heading-form": scan_bib_heading,
    "pubinfo-form": scan_pubinfo,
    "bib-subsection": scan_bib_subsection,
    "style": lambda p, t, e: [i for i in scan_style(p, t, e)
                              if i.get("rule") != "quote-spacing"],
    "quote-adjacent": scan_quote,
    "pairs": scan_pairs,
}


def main(argv):
    letters = set()
    want = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--classes":
            print(json.dumps({k: (SCANNERS[k].__doc__ or "").strip() for k in CLASSES},
                             ensure_ascii=False, indent=1))
            return 0
        if a == "--letter":
            letters.add(argv[i + 1].upper())
            i += 2
            continue
        if a == "--class":
            want.append(argv[i + 1])
            i += 2
            continue
        if not a.startswith("-"):
            letters.add(a.upper())
        i += 1
    classes = want or list(CLASSES)
    bad = [c for c in classes if c not in CLASSES]
    if bad:
        print(json.dumps({"error": "未知类别 %s；可用 %s" % (bad, list(CLASSES))},
                         ensure_ascii=False))
        return 2
    result = {c: [] for c in classes}
    nfiles = 0
    skipped = 0
    all_files = "--all-files" in argv
    for p in zh_docs(letters):
        st = task_state(p)
        if not all_files and st not in TRANSLATED:
            skipped += 1
            continue
        text = io.open(p, encoding="utf-8").read()
        en = _en(p)
        nfiles += 1
        for c in classes:
            try:
                result[c].extend(SCANNERS[c](p, text, en))
            except Exception as exc:  # 单文件异常不中断全批
                result[c].append({"path": p, "line": 0, "detail": "扫描异常：%r" % (exc,)})
    counts = {c: len(v) for c, v in result.items()}
    counts["_files"] = nfiles
    print(json.dumps({"scope": sorted(letters) or "全库",
                      "state_filter": "all" if all_files else sorted(TRANSLATED),
                      "files": nfiles, "skipped_not_translated": skipped,
                      "counts": counts, "classes": result},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
