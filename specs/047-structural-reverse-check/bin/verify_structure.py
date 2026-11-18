# -*- coding: utf-8 -*-
r"""B2 结构反向核验（specs/047；判据编位 specs/044 §1.3）：md 结构树 ↔ HTML 结构树五维比对。

盲区定位（ADR-0070 附录 6–9）：I2 是自证（转换器 bug 两边都错机检不见），本判定器把
md 解析回结构，与 HTML 结构比对，抓“两边都错”。

五维（specs/047 §1；v1.1 试金石修正后的实现口径）：
  1 分节   h2/h3/h4 序列逐字比对；转换器契约改名白名单：
           HTML h2 "Bibliography" ≡ md "References（引用注释）"；
           md "Notes（原文脚注）" 仅当存在 notes.html（脚注并入主档）。
  2 脚注   注释引用键位↔定义一一对应且序一致（HTML notes.html name= 锚 ↔ md [^note-N]）；
           定义总账＝Bibliography 节 li 数＋notes 条目数。
  3 图·表·公式块  图＝资产图 src 基名序（parse_entry images ↔ md ![]()，站点框架图天然互斥）；
           表＝article 内 <table 计数（blockquote 嵌套表 parse_entry 不计，用原文计数）↔
           md 管道表组数；公式块＝\[...\] 数↔md 行级 $$ 数。
  4 列表   正文 li 数（剔除 TOC li 与 Bibliography li——TOC 不入 md、文献转脚注定义）
           ↔ md 列表项行数；ol/ul 容器序记 advisory。
  5 引用   md 脚注定义总账核（同维 2-d）；citation meta 在 H1 侧无对应行，advisory 记录。

差异只报不判（ADR-0070）：机检产候选，kind 粗分（count/order/pairing），人审为判。

用法:
  verify_structure.py [slugs...] [--out PATH]   # 缺省试金石 5 件（specs/044 同一固定种子名单）
  verify_structure.py --all [--out PATH]        # 全库 1,872
  verify_structure.py --selftest                # 负向证伪（丢节/丢脚注/丢表行必报）
退出码: 0 全过；1 有不匹配（报告在案）；2 用法/selftest 失败。
只读判官（ADR-0063 三权分立）：不写 en/、不写 yuanwen/、不改任何被判定对象。
"""
import argparse
import difflib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from tools import parser
from tools.common import repo_path

# stdout 重包守卫（specs/039 判例：多检查器同进程导入时勿重包 stdout）
if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8")

TRIAL = ["delmedigo", "genotype-phenotype", "phil-bio-latin-america",
         "spinoza-modal", "williams-bernard"]

MD_HEADING_RE = re.compile(r"^(#{2,4})\s+(.*?)\s*$")
MD_DEF_RE = re.compile(r"^\[\^([^\]\s]+)\]:", re.M)   # 键可含变音符（hübsch-1883）
MD_REF_RE = re.compile(r"\[\^([^\]\s]+)\](?!:)")
MD_IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
MD_TABLE_SEP_RE = re.compile(r"^\s*>?\s*\|[\s:|-]+\|\s*$")
MD_TABLE_ROW_RE = re.compile(r"^\s*>?\s*\|.*\|\s*$")
MD_LIST_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.]\s+)")
MD_NOTEDEF_RE = re.compile(r"^note-\d+$")
MD_MATH_BLOCK_RE = re.compile(r"\$\$.*?\$\$", re.S)
HTML_DISPLAY_MATH_RE = re.compile(r"\\\[.*?\\\]", re.S)

# 转换器契约的尾节改名白名单（template-contract §6 尾节正典；合法移位登记面）
SEC_RENAME_HTML = {"bibliography": "References（引用注释）"}
MD_SECTION_DROP_IF_NOTES = "Notes（原文脚注）"


_SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉ₐₑₒₓᵢ", "0123456789aeoxi")
_SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")


def _norm_heading(text):
    """标题归一化（两侧同用）：剥标签＋实体解码＋折叠空白＋剥强调＋剥数学定界符/
    花括号（HTML 侧 \\(B\\) vs md 侧 $B$ 等表示差属转换契约合法形）＋上下标转 ASCII。
    h2 内嵌 <a name> 锚点必须剥除（abduction 族实证）。"""
    import html as _html
    t = _html.unescape(re.sub(r"<[^>]+>", "", text or ""))
    t = _norm(t)
    for ch in "\\()[]{}$":
        t = t.replace(ch, "")
    return t.translate(_SUB).translate(_SUP).strip()


def _norm(text):
    """规范化：折叠空白＋剥 md 强调标记（HTML 侧 parser 已剥标签；md 标题保留 *…*）。"""
    t = re.sub(r"\s+", " ", text or "").strip()
    return t.replace("*", "").replace("_", "").replace("`", "").strip()


def load_baseline():
    path = repo_path("baseline", "entries.json")
    with io.open(path, encoding="utf-8") as f:
        recs = json.load(f)
    if isinstance(recs, dict):
        recs = recs.get("entries", [])
    return {r["slug"]: r for r in recs if isinstance(r, dict) and r.get("slug")}


def _article_of(html_text):
    m, e = parser.HEAD_RE.search(html_text), parser.TAIL_RE.search(html_text)
    return html_text[m.end():e.start()] if (m and e) else html_text


def notes_defs_of(notes_text):
    """notes.html 条目 id 序。三代形态：
    旧（bayes）：<a href="index.html#note-N" name="N">；
    新（spinoza）：<div id="note-N">；
    又旧（animal-thought）：<a id="note-N">。"""
    ids = re.findall(r'<div[^>]*\bid="note-([A-Za-z0-9_-]+)"', notes_text)
    if not ids:
        ids = re.findall(r'<a[^>]*\bid="note-([A-Za-z0-9_-]+)"', notes_text)
    if not ids:
        ids = re.findall(r'href="index\.html#note-[^"]*"[^>]*\bname="([^"]+)"',
                         notes_text)
    if not ids:  # 形态兜底：任意 name="N" 数字锚
        ids = re.findall(r'\bname="(\d+)"', notes_text)
    return ids


# ---------------------------------------------------------------- HTML 侧 ---

def _strip_tags(text):
    import html as _html
    return _html.unescape(re.sub(r"<[^>]+>", "", text))


def _is_refs_heading(low):
    """文献区标题（任意层级）：Bibliography／References（改名前后的原文形）。"""
    return low == "bibliography" or low == "references"


def html_tree(html_text):
    pr = parser.parse_entry(html_text)
    article = _article_of(html_text)
    t = {"math_display": len(HTML_DISPLAY_MATH_RE.findall(article))
         + len(re.findall(r"\$\$.*?\$\$", article, re.S)),  # SEP 第三形：直书 $$
         "tables": article.count("<table"), "tr": article.count("<tr"),
         "img_srcs": [im["src"] for im in pr["images"]],
         "note_ref_seq": parser.NOTE_REF_RE.findall(article),
         "sections": [], "refs_li": 0}
    # 分节走原文正则（parse_entry 对 div 包裹的标题不开块——v1.5 修正）；
    # 改名白名单任意层级生效。
    heads = [(int(m.group(1)), m.start(), m.end(),
              _norm_heading(m.group(2))) for m in
             re.finditer(r"<h([234])\b[^>]*>(.*?)</h\1\s*>", article, re.S | re.I)]
    renamed = []
    for lv, _, _, tx in heads:
        low = tx.lower()
        if low in SEC_RENAME_HTML or low == "references":
            tx = SEC_RENAME_HTML["bibliography"]
        renamed.append((lv, tx))
        t["sections"].append(("h%d" % lv, tx))
    # Bibliography/References 区域的顶层 li——直接用 parse_entry 块账（与 md 转换
    # 同源，ADR-0073）；入区=任意层级标题命名 bibliography/references，
    # 出区=层级 ≤ 入区层级的非文献标题（h3 子节滞留区内）
    toc_li = 0
    refs_li = 0
    seen_heading = False
    in_refs = False
    last_refs_level = 9
    for b in pr["blocks"]:
        bt = b["type"]
        if bt in ("h2", "h3", "h4"):
            seen_heading = True
            tx = _norm(b["text"])
            low = tx.lower()
            if _is_refs_heading(low):
                in_refs = True
                last_refs_level = int(bt[1])
            elif in_refs and int(bt[1]) <= last_refs_level:
                in_refs = False
        elif bt == "li":
            if not seen_heading:
                toc_li += 1
            elif in_refs:
                refs_li += 1
    t["toc_li"] = toc_li
    t["refs_li"] = refs_li
    t["li_total"] = sum(1 for b in pr["blocks"] if b["type"] == "li")
    t["li_body"] = max(0, t["li_total"] - toc_li - refs_li)
    return t


# ----------------------------------------------------------------- md 侧 ----

def md_tree(md_text):
    lines = md_text.splitlines()
    t = {"sections": [], "li_total": 0, "ol_items": 0, "ul_items": 0,
         "tables": 0, "table_rows": 0, "math_display": 0,
         "img_basename_seq": [], "defs": [], "refs_seq": [], "notedefs": []}
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = MD_HEADING_RE.match(ln)
        if m:
            t["sections"].append(("h%d" % len(m.group(1)), _norm_heading(m.group(2))))
            i += 1
            continue
        if MD_DEF_RE.match(ln):
            i += 1
            continue  # 定义行不计列表/表格
        if MD_TABLE_ROW_RE.match(ln):
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if MD_TABLE_SEP_RE.match(nxt):
                t["tables"] += 1
                j = i + 2  # 表体行（表头之后连续管道行）
                while j < len(lines) and MD_TABLE_ROW_RE.match(lines[j]) \
                        and not MD_TABLE_SEP_RE.match(lines[j]):
                    t["table_rows"] += 1
                    j += 1
                i = j
                continue
        if MD_LIST_RE.match(ln):
            t["li_total"] += 1
            if re.match(r"^\s*\d+[.]\s+", ln):
                t["ol_items"] += 1
            else:
                t["ul_items"] += 1
        for im in MD_IMG_RE.finditer(ln):
            t["img_basename_seq"].append(im.group(1).rstrip("/").split("/")[-1])
        i += 1
    t["math_display"] = len(MD_MATH_BLOCK_RE.findall(md_text))
    t["defs"] = MD_DEF_RE.findall(md_text)
    t["refs_seq"] = MD_REF_RE.findall(md_text)
    t["notedefs"] = [k for k in t["defs"] if MD_NOTEDEF_RE.match(k)]
    return t


# ---------------------------------------------------------------- 比对器 ----

def _seq_diff(a, b):
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            out.append({"op": tag, "html": [str(x) for x in a[i1:i2]][:6],
                        "md": [str(x) for x in b[j1:j2]][:6]})
    return out


def compare(ht, mt, notes_defs):
    """五维比对 → {dim: {ok, kind, detail}}；只报不判。"""
    dims = {}

    # 1 分节（md 侧按契约裁掉两类转换器生成节：主档 Notes 节——内容并入脚注定义账，
    # 判据=存在注释定义即可；'Notes to …' 补充材料注节——HTML 侧在 supplement.html）
    has_notes = bool(notes_defs) or bool(mt["notedefs"])
    ms = [(lv, tx) for lv, tx in mt["sections"]
          if not tx.startswith("Notes to ")
          and not (tx == MD_SECTION_DROP_IF_NOTES and has_notes)]
    d = _seq_diff(ht["sections"], ms)
    dims["sections"] = {"ok": not d, "kind": "order-mismatch" if d else None,
                        "html_n": len(ht["sections"]), "md_n": len(ms),
                        "detail": d[:4]}

    # 2 脚注（注释引用↔定义配对 + 定义总账）
    notes_defs = notes_defs or []
    note_seq_html = [x[5:] if x.startswith("note-") else x
                     for x in ht["note_ref_seq"]]  # href 形态两代：#1 与 #note-1
    note_seq_md = [k[5:] for k in mt["refs_seq"] if MD_NOTEDEF_RE.match(k)]
    pairing_ok = note_seq_html == note_seq_md
    ids_ok = mt["notedefs"] == ["note-%s" % x for x in notes_defs]
    ledger_expected = ht["refs_li"] + len(notes_defs)
    surplus = len(mt["defs"]) - ledger_expected
    ledger_ok = surplus >= 0  # 赤字＝真丢文候选硬判；富余＝拆条/子注合法族（T7 衰减面，登记）
    dims["footnotes"] = {
        "ok": pairing_ok and ids_ok and ledger_ok,
        "kind": None if (pairing_ok and ids_ok and ledger_ok) else "pairing-mismatch",
        "html_note_refs": len(note_seq_html), "md_note_refs": len(note_seq_md),
        "html_notes_items": len(notes_defs), "md_notedefs": len(mt["notedefs"]),
        "refs_li": ht["refs_li"], "md_defs": len(mt["defs"]),
        "ledger_expected": ledger_expected, "ledger_surplus": surplus,
        "detail": {"pairing_ok": pairing_ok, "ids_ok": ids_ok,
                   "ledger_deficit": surplus < 0}}

    # 3 图·公式块（硬判）＋表（v1 advisory：复杂表以原样 HTML 嵌入 md 单元格的
    # passthrough 契约形刚发现，口径待专项定性——047 execution-log W2）
    html_img_base = [os.path.basename(s) for s in ht["img_srcs"]]
    fig_ok = html_img_base == mt["img_basename_seq"]
    math_ok = ht["math_display"] == mt["math_display"]
    dims["figtablemath"] = {
        "ok": fig_ok and math_ok,
        "kind": None if (fig_ok and math_ok) else "count-mismatch",
        "html_imgs": len(ht["img_srcs"]), "md_imgs": len(mt["img_basename_seq"]),
        "html_math": ht["math_display"], "md_math": mt["math_display"],
        "advisory_tables": {"html_tables": ht["tables"], "md_pipe_tables": mt["tables"],
                            "html_tr": ht["tr"],
                            "md_pipe_rows": mt["tables"] + mt["table_rows"]},
        "detail": {"figures_ok": fig_ok, "math_ok": math_ok}}

    # 4 列表（v1 advisory：ol→块引/表格的渲染语义待专项定性，见 047 execution-log W1；
    # ul 面与 ol 面分开记录）
    dims["lists"] = {"ok": True, "advisory": {
        "html_li_body": ht["li_body"], "md_li": mt["li_total"],
        "toc_li": ht["toc_li"], "refs_li": ht["refs_li"],
        "md_ordered": mt["ol_items"], "md_unordered": mt["ul_items"]}}

    # 5 引用（定义总账已并入维 2-d；citation meta 无 md 对应行，advisory）
    dims["citations"] = {"ok": True,
                         "advisory": {"html_refs_li": ht["refs_li"],
                                      "md_defs_total": len(mt["defs"]),
                                      "ledger_expected":
                                          ht["refs_li"] + len(notes_defs or [])}}
    return dims


def judge_slug(slug, baseline):
    rec = baseline.get(slug)
    if not rec:
        return {"slug": slug, "ok": False, "skipped": "not in baseline/entries.json"}
    zh_doc = rec.get("zh_doc")
    en_idx = repo_path("en", slug, "index.html")
    md_path = repo_path("yuanwen", zh_doc) if zh_doc else None
    if not os.path.exists(en_idx):
        return {"slug": slug, "ok": False, "skipped": "no en package"}
    if not md_path or not os.path.exists(md_path):
        return {"slug": slug, "ok": False, "skipped": "no yuanwen md（specs/001 接入面）"}
    html_text = io.open(en_idx, encoding="utf-8").read()
    md_text = io.open(md_path, encoding="utf-8").read()
    notes_path = repo_path("en", slug, "notes.html")
    notes_defs = []
    if os.path.exists(notes_path):
        notes_defs = notes_defs_of(io.open(notes_path, encoding="utf-8").read())
    ht = html_tree(html_text)
    mt = md_tree(md_text)
    dims = compare(ht, mt, notes_defs)
    return {"slug": slug, "ok": all(d["ok"] for d in dims.values()), "dims": dims}


# ---------------------------------------------------------------- selftest --

def _corrupt(lines, mode):
    lines = list(lines)
    if mode == "drop-section":
        idx = next(i for i, ln in enumerate(lines)
                   if MD_HEADING_RE.match(ln) and ln.startswith("## "))
        del lines[idx]
    elif mode == "drop-footnote":
        idx = next(i for i, ln in enumerate(lines) if MD_DEF_RE.match(ln))
        del lines[idx]
    elif mode == "drop-math-block":
        idx = next(i for i, ln in enumerate(lines) if ln.startswith("$$"))
        del lines[idx]
    return "\n".join(lines)


def selftest(baseline):
    """负向证伪：丢节/丢脚注/丢表行必须报出；Golden 不作断言（存量差异走对账）。"""
    results = []
    md0 = io.open(repo_path("yuanwen", baseline["abelard"]["zh_doc"]),
                  encoding="utf-8").read()
    html_text = io.open(repo_path("en", "abelard", "index.html"),
                        encoding="utf-8").read()
    ht = html_tree(html_text)
    mt = md_tree(_corrupt(md0.splitlines(), "drop-section"))
    results.append({"case": "drop-section",
                    "detected": not compare(ht, mt, [])["sections"]["ok"]})
    b_md = io.open(repo_path("yuanwen", baseline["bayes-theorem"]["zh_doc"]),
                   encoding="utf-8").read()
    bht = html_tree(io.open(repo_path("en", "bayes-theorem", "index.html"),
                            encoding="utf-8").read())
    bnotes = notes_defs_of(io.open(repo_path("en", "bayes-theorem", "notes.html"),
                                   encoding="utf-8").read())
    mt = md_tree(_corrupt(b_md.splitlines(), "drop-footnote"))
    results.append({"case": "drop-footnote",
                    "detected": not compare(bht, mt, bnotes)["footnotes"]["ok"]})
    # 数学块负向：动态取首个“全过且含显示公式”的词条（action 的数学账本身
    # 属候选族，不可作干净底稿）
    math_slug = None
    for slug in sorted(baseline):
        r = judge_slug(slug, baseline)
        if r.get("ok") and (r.get("dims", {}).get("figtablemath", {})
                            .get("md_math") or 0) >= 1:
            math_slug = slug
            break
    if math_slug:
        a_md = io.open(repo_path("yuanwen", baseline[math_slug]["zh_doc"]),
                       encoding="utf-8").read()
        aht = html_tree(io.open(repo_path("en", math_slug, "index.html"),
                                encoding="utf-8").read())
        mt = md_tree(_corrupt(a_md.splitlines(), "drop-math-block"))
        results.append({"case": "drop-math-block(%s)" % math_slug,
                        "detected": not compare(aht, mt, [])["figtablemath"]["ok"]})
    else:
        results.append({"case": "drop-math-block", "detected": False})
    ok = all(r["detected"] for r in results)
    return {"ok": ok, "cases": results}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    baseline = load_baseline()
    if args.selftest:
        res = selftest(baseline)
        print(json.dumps({"schema": "sep-cn-b2-selftest/1", "selftest": res},
                         ensure_ascii=False, indent=1))
        return 0 if res["ok"] else 2
    slugs = sorted(baseline) if args.all else (args.slugs or TRIAL)
    entries, n_ok, n_skip, n_fail = [], 0, 0, 0
    for slug in slugs:
        r = judge_slug(slug, baseline)
        if r.get("ok") and "dims" in r:
            # 过件瘦身：只留计数面（细节仅在失败件保留——文件体积，对照 044 444KB）
            slim = {}
            for k, v in r["dims"].items():
                slim[k] = {f: v[f] for f in v if f not in ("detail", "advisory")}
            r["dims"] = slim
        entries.append(r)
        if r.get("skipped"):
            n_skip += 1
        elif r["ok"]:
            n_ok += 1
        else:
            n_fail += 1
    payload = {"schema": "sep-cn-b2-structure/1",
               "generated_by": "specs/047 bin/verify_structure.py",
               "total": len(entries), "ok": n_ok, "fail": n_fail,
               "skipped": n_skip, "entries": entries}
    out = args.out or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "results", "structure-scan.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sys.stderr.write("[b2] 总 %d：过 %d／不匹配 %d／跳过 %d → %s\n"
                     % (len(entries), n_ok, n_fail, n_skip, out))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
