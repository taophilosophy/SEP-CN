#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEP Friends 版式仿排:词条中文 md -> 双栏横排 PDF(specs/035)。

用法:
  uv run --with typst --with pymupdf python specs/035-entry-pdf/bin/entry_pdf.py <slug> [选项]

选项:
  --edition TEXT  页脚/封面的版本文案(默认 "2025 年夏季版")
  --out DIR       输出目录(默认 script/tmp/entry-pdf)
  --no-preview    不渲染 PNG 预览

依赖: pandoc 在 PATH;typst/pymupdf 由 uv --with 注入(非标准库,不入 tools/)。
自举: 霞鹜文楷屏幕阅读版与主仓 Medium 经 gh release download 下载到
  script/tmp/sep-pdf/fonts/(本地缓存,不入库);SEP 标志取
  plato.stanford.edu/symbols/sepman-red.png(单请求,礼貌抓取)并转黑。

约定: 失败显式化、禁止静默跳过(specs/035 spec.md)。
退出码: 0 成功;1 输入/解析错;2 依赖或自举失败;3 编译失败。
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "entry_pdf_template.typ"
FONTS = REPO / "script" / "tmp" / "sep-pdf" / "fonts"
ASSETS = REPO / "script" / "tmp" / "sep-pdf"
DEFAULT_OUT = REPO / "script" / "tmp" / "entry-pdf"


def die(code, msg):
    print("[entry_pdf] 错误:", msg, file=sys.stderr)
    sys.exit(code)


def resolve_doc(slug):
    """slug -> zh 词条 md 路径:先试 <letter>/<slug>.md,再回 tasks/ 登记。"""
    cand = REPO / slug[0] / (slug + ".md")
    if cand.exists():
        return cand
    tjson = REPO / "tasks" / slug[0] / (slug + ".json")
    if tjson.exists():
        data = json.loads(tjson.read_text(encoding="utf-8"))
        for it in (data if isinstance(data, list) else [data]):
            if isinstance(it, dict) and it.get("slug") == slug and it.get("zh_doc"):
                p = REPO / it["zh_doc"]
                if p.exists():
                    return p
                die(1, "tasks 登记的 zh_doc 不存在: %s" % p)
    die(1, "找不到词条文件: %s(也无 tasks/%s/%s.json 登记)" % (cand, slug[0], slug))


def ensure_fonts():
    FONTS.mkdir(parents=True, exist_ok=True)
    for fname, repo in (("LXGWWenKaiScreen.ttf", "lxgw/LxgwWenKai-Screen"),
                        ("LXGWWenKai-Medium.ttf", "lxgw/LxgwWenKai")):
        if (FONTS / fname).exists():
            continue
        r = subprocess.run(["gh", "release", "download", "--repo", repo,
                            "--pattern", fname, "--dir", str(FONTS), "--clobber"],
                           capture_output=True, text=True)
        if r.returncode != 0 or not (FONTS / fname).exists():
            die(2, "字体自举失败(%s %s): %s;可手动: gh release download --repo %s "
                   "--pattern %s --dir %s" % (repo, fname, r.stderr.strip(), repo, fname, FONTS))
    print("[entry_pdf] 字体就绪:", FONTS)


def ensure_logo_black(outdir):
    """SEP 思考者标志:取 sepman-red.png(单请求)转纯黑;已存在则复用。"""
    dst = outdir / "sepman-black.png"
    if dst.exists():
        return
    src = ASSETS / "sepman.png"
    if not src.exists():
        import urllib.request
        url = "https://plato.stanford.edu/symbols/sepman-red.png"
        try:
            urllib.request.urlretrieve(url, src)  # 代理经环境变量;失败显式化
        except Exception as e:
            die(2, "标志下载失败(%s): %s;可手动抓取保存为 %s" % (url, e, src))
    import pymupdf
    pix = pymupdf.Pixmap(str(src))
    n, w, h = pix.n, pix.width, pix.height
    data = pix.samples
    out = bytearray(w * h * 3)
    for k in range(w * h):
        if n == 4 and data[k * n + 3] < 128:
            v = 255  # 透明底 -> 白
        else:
            lum = (data[k * n] * 30 + data[k * n + 1] * 59 + data[k * n + 2] * 11) // 100
            v = 0 if lum < 140 else 255
        out[k * 3:k * 3 + 3] = (v, v, v)
    pix2 = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, w, h), False)
    for y in range(h):
        for x in range(w):
            k = (y * w + x) * 3
            pix2.set_pixel(x, y, (out[k], out[k + 1], out[k + 2]))
    pix2.save(str(dst))


def parse_entry(md_text):
    """解析 H1(中英题/作者)、pubinfo、剥离工作底稿注记,拆封面导语与正文。"""
    lines = md_text.split("\n")
    m = re.match(r"^#\s+(.*?)\s*\(([^()]+)\)\s*$", lines[0].strip())
    if not m:
        die(1, "H1 不符『中英题 (作者)』体例: %s" % lines[0][:80])
    zh_en, author = m.group(1), m.group(2).strip()
    mm = re.search(r"(?<=[\u4e00-\u9fff])\s+(?=[A-Za-z\u2018\u2019\"])", zh_en)
    if not mm:
        die(1, "中英文标题切分失败: %s" % zh_en)
    zh_title, en_title = zh_en[:mm.start()].strip(), zh_en[mm.end():].strip()

    pubinfo = None
    kept = []
    for l in lines[1:]:
        s = l.strip()
        if pubinfo is None and len(s) < 80 and ("*" in s or s.startswith(">")) \
                and ("首次发表于" in s or "实质性修订" in s or "实质修订" in s):
            pubinfo = re.sub(r"[>*]", "", s).strip()
            continue
        if "原文参考文献已转为脚注引用" in s:  # 工作底稿注记,不入 PDF
            continue
        kept.append(l)
    if pubinfo is None:
        die(1, "未找到 pubinfo 行(首次发表于/实质性修订)")

    body = "\n".join(kept)
    parts = re.split(r"\n(?=## )", body, maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():
        die(1, "未找到正文节(## 起首)")
    intro, rest = parts[0], parts[1]
    paras = [p for p in intro.split("\n\n") if p.strip()]
    cover_lead = paras[0] if paras else ""
    rest_intro = "\n\n".join(paras[1:])
    if rest_intro:
        rest = rest_intro + "\n\n" + rest
    return zh_title, en_title, author, pubinfo, cover_lead, rest


def transform_body(rest_md):
    """行内 [^key] -> 内联脚注 ^[...];脚注定义 -> 书目段落(悬挂缩进由模板节注入)。"""
    def_re = re.compile(r"^\[\^([a-z0-9-]+)\]:\s*(.*)$")
    lines = rest_md.split("\n")
    defs, out, i = {}, [], 0
    while i < len(lines):
        l = lines[i]
        dm = def_re.match(l)
        if dm:
            text = dm.group(2)
            j = i + 1
            while j < len(lines) and lines[j].startswith((" ", "\t")) and lines[j].strip():
                text += " " + lines[j].strip()  # 缩进续行并入定义
                j += 1
            defs[dm.group(1)] = text.strip()
            out.extend(["", text.strip(), ""])
            i = j
            continue
        out.append(l)
        i += 1
    body = "\n".join(out)
    missing = set(re.findall(r"\[\^([a-z0-9-]+)\](?!:)", body)) - set(defs)
    if missing:
        die(1, "行内脚注引用无定义: %s" % sorted(missing))
    n_refs = 0

    def sub(mo):
        nonlocal n_refs
        n_refs += 1
        return "^[" + defs[mo.group(1)].replace("]", "\\]") + "]"

    body = re.sub(r"(?<!\[)\[\^([a-z0-9-]+)\](?!:)", sub, body)
    return body, len(defs), n_refs


def pandoc(md_text, name, workdir):
    mdp = workdir / (name + ".md")
    typ = workdir / (name + ".typ")
    mdp.write_text(md_text, encoding="utf-8", newline="\n")
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "typst", "--wrap=none",
                        mdp.name, "-o", typ.name], cwd=str(workdir),
                       capture_output=True, text=True)
    if r.returncode != 0:
        die(2, "pandoc 失败(%s): %s" % (name, r.stderr.strip()))
    return typ.read_text(encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="SEP Friends 版式仿排 PDF 生成器(specs/035)")
    ap.add_argument("slug")
    ap.add_argument("--edition", default="2025 年夏季版")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--no-preview", action="store_true")
    args = ap.parse_args()
    slug = args.slug.strip()
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    doc = resolve_doc(slug)
    print("[entry_pdf] 词条:", slug, "->", doc)

    need = shutil.which("pandoc")
    if not need:
        die(2, "pandoc 不在 PATH")
    try:
        import typst  # noqa: F401
        import pymupdf  # noqa: F401
    except ImportError as e:
        die(2, "缺依赖 %s;用 uv run --with typst --with pymupdf python 运行" % e)

    ensure_fonts()
    ensure_logo_black(outdir)

    md_text = doc.read_text(encoding="utf-8")
    zh_title, en_title, author, pubinfo, cover_lead, rest = parse_entry(md_text)
    body_md, n_defs, n_refs = transform_body(rest)
    print("[entry_pdf] 书目条数:", n_defs, "| 内联脚注:", n_refs)

    body_typ = pandoc(body_md, "body", outdir)
    body_typ = re.sub(r"(==\s*参考文献)",
                      r"\1\n#set par(hanging-indent: 1.15em, spacing: 0.95em, first-line-indent: 0em)",
                      body_typ, count=1)
    intro_typ = pandoc(cover_lead, "intro", outdir)

    main_typ = TEMPLATE.read_text(encoding="utf-8")
    entry_url = "https://plato.stanford.edu/entries/%s/" % slug
    for k, v in (("%%ZH_TITLE%%", zh_title), ("%%EN_TITLE%%", en_title),
                 ("%%AUTHOR%%", author), ("%%PUBINFO%%", pubinfo),
                 ("%%EDITION%%", args.edition), ("%%ENTRY_URL%%", entry_url),
                 ("%%INTRO%%", intro_typ), ("%%BODY%%", body_typ)):
        main_typ = main_typ.replace(k, v)
    mainp = outdir / "main.typ"
    mainp.write_text(main_typ, encoding="utf-8", newline="\n")

    font_paths = [str(FONTS)]
    winfonts = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    if winfonts.exists():
        font_paths.append(str(winfonts))
    import typst
    pdf = outdir / (slug + ".zh.pdf")
    try:
        typst.compile(str(mainp), output=str(pdf), font_paths=font_paths)
    except Exception as e:
        die(3, "typst 编译失败: %s" % e)

    import pymupdf
    d = pymupdf.open(str(pdf))
    print("[entry_pdf] PDF:", pdf, "|", pdf.stat().st_size, "bytes |", len(d), "页")
    if not args.no_preview:
        for p in range(min(len(d), 3)):
            d[p].get_pixmap(dpi=95).save(str(outdir / ("preview-%d.png" % (p + 1))))
        d[len(d) - 1].get_pixmap(dpi=95).save(str(outdir / "preview-last.png"))
        print("[entry_pdf] 预览:", outdir / "preview-*.png")


if __name__ == "__main__":
    main()
