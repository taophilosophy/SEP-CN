# -*- coding: utf-8 -*-
"""参考文献结构盘点与中文文献定位（specs/001 biblio-analysis 优化建议 5，2026-10-28）。

对 en/<slug>/index.html 文献节（Bibliography 及变体标题）：
  1. 标题变体与条目量分布；
  2. 链接域分布（ctext.org/archive.org/doi 等回溯通道）；
  3. 疑似中国文献三探针（实体解码后）：节内汉字 / 典籍专名 / 作者位拼音姓氏。
用途：s1 一校与质检定位需按 ADR-0011 还原的条目，不必全量人扫。

用法:
  python tools/biblio_audit.py [slug...]
  python tools/biblio_audit.py --all
输出: stdout JSON。退出码: 0（分析工具，不做门禁）。
"""
import argparse
import io
import json
import os
import re
import sys
from collections import Counter
from html import unescape
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import load_json, repo_path, utcnow_iso  # noqa: E402

if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
LI_RE = re.compile(r"<li[\s>]", re.I)
A_RE = re.compile(r'<a[^>]+href="(https?://[^"]+)"', re.I)

CJK_RE = re.compile(r"[\u3400-\u9fff]")
KANA_RE = re.compile(r"[\u3040-\u30ff]")

# 典籍与学者专名（词边界，大小写敏感；只收罗马化形态中低噪声的）
CLASSIC_RE = re.compile(
    r"\b(Analects|Lun\s?yu|Mencius|Mengzi|Mozi|Zhuangzi|Laozi|Lao\s?Tzu|"
    r"Daodejing|Tao\s?Te\s?Ching|Xunzi|Han\s?Feizi|Yijing|I\s?Ching|"
    r"Huainanzi|Shiji|Liezi|Guanzi|Chunqiu|Gongsun\s?Long|Wang\s?Yangming|"
    r"Zhu\s?Xi|Xiong\s?Shili|Feng\s?Youlan|Hu\s?Shih|Liang\s?Shuming|"
    r"Zhang\s?Dongsun|Nishida|Dogen)\b")

# 作者位罗马化姓氏：条目 “Surname, F.,” 形态（仅文献节内使用，噪声可控）
SURNAME = (
    "Cai|Cao|Chang|Chao|Chen|Cheng|Cheung|Chiang|Chong|Chu|Chuan|Chung|"
    "Dong|Feng|Gao|Gong|Guo|Han|Hong|Hsieh|Hsiao|Hsu|Hu|Hua|Huang|"
    "Hui|Hung|Ji|Jia|Jiang|Jin|Kong|Kung|Kwong|Lao|Lei|Li|Liang|Liao|Lin|"
    "Ling|Liu|Lo|Long|Lu|Luo|Mei|Meng|Mi|Miao|Mo|Mou|Ni|Nie|Niu|Ou|Pan|Pang|"
    "Peng|Pi|Qi|Qian|Qin|Qiu|Qu|Ren|Ruan|Shang|Shao|Shen|Sheng|Shi|Shou|Shu|"
    "Si|Song|Su|Sui|Sun|Tai|Tan|Tang|Tao|Teng|Tian|Ting|Tong|Tu|Wan|Wang|"
    "Wei|Wen|Wong|Wu|Xi|Xia|Xiang|Xiao|Xie|Xin|Xing|Xiong|Xu|Xue|Yan|Yang|"
    "Yao|Ye|Yi|Yin|Ying|Yong|You|Yu|Yuan|Yue|Yun|Zeng|Zha|Zhai|Zhang|Zhao|"
    "Zhen|Zheng|Zhong|Zhou|Zhu|Zhuang|Zou")
AUTHORPOS_RE = re.compile(r"\b(?:%s),\s*[A-Z]\." % SURNAME)

HEADING_CANON = {
    "bibliography": "Bibliography",
    "secondary literature": "Secondary Literature",
    "primary literature": "Primary Literature",
    "references": "References",
    "further reading": "Further Reading",
    "recommended reading": "Recommended Reading",
    "selected bibliography": "Selected Bibliography",
}
BIB_CANONS = set(HEADING_CANON.values())


def probe_text(text):
    """文献节纯文本 → 探针结果。text 须已实体解码、去标签。"""
    return {
        "cjk": bool(CJK_RE.search(text)),
        "kana": bool(KANA_RE.search(text)),
        "classic_hits": sorted({m.group(0) for m in CLASSIC_RE.finditer(text)}),
        "authorpos_hits": len(AUTHORPOS_RE.findall(text)),
    }


def likely_chinese(probe):
    """三探针 → 疑似含中国文献（汉字/典籍专名任一，或作者位姓氏 ≥2）。"""
    return (probe["cjk"] or bool(probe["classic_hits"])
            or probe["authorpos_hits"] >= 2)


def analyze_slug(slug):
    """单词条 → 文献节盘点；无文献节返回 None。"""
    p = repo_path("en", slug, "index.html")
    if not os.path.isfile(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as fh:
        html = unescape(fh.read())  # 实体解码：上游汉字以 &#…; 形式出现
    heads = [(m.start(), TAG_RE.sub("", m.group(1)).strip())
             for m in H2_RE.finditer(html)]
    out = {"slug": slug, "sections": []}
    for i, (pos, text) in enumerate(heads):
        canon = None
        low = text.lower()
        for k, v in HEADING_CANON.items():
            if low == k or low.startswith(k):
                canon = v
                break
        if canon is None:
            continue
        end = heads[i + 1][0] if i + 1 < len(heads) else len(html)
        seg = html[pos:end]
        plain = TAG_RE.sub("", seg)
        probe = probe_text(plain)
        domains = Counter(urlparse(m.group(1)).netloc for m in A_RE.finditer(seg))
        sec = {"heading": canon, "items": len(LI_RE.findall(seg)),
               "links": sum(domains.values()),
               "top_domains": dict(domains.most_common(4)),
               "probe": probe, "likely_chinese": likely_chinese(probe)}
        out["sections"].append(sec)
    return out if out["sections"] else None


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true", help="全库（baseline 登记词条）")
    args = ap.parse_args(argv)
    base = load_json(repo_path("baseline", "entries.json"))
    slugs = args.slugs or ([r["slug"] for r in base["entries"]] if args.all else [])
    if not slugs:
        print(json.dumps({"error": "用法: biblio_audit.py <slug>... | --all"},
                         ensure_ascii=False))
        return 2
    flagged, errors = [], []
    total_items = 0
    domain_all = Counter()
    for i, slug in enumerate(slugs):
        if i % 250 == 0:
            sys.stderr.write("[biblio_audit] %d/%d\n" % (i, len(slugs)))
        try:
            r = analyze_slug(slug)
        except Exception as e:  # noqa: BLE001
            errors.append({"slug": slug, "error": str(e)})
            continue
        if r is None:
            continue
        for sec in r["sections"]:
            total_items += sec["items"]
            for dom, n in sec["top_domains"].items():
                domain_all[dom] += n
        if any(sec["likely_chinese"] for sec in r["sections"]):
            flagged.append(r)
    print(json.dumps({
        "ran_at": utcnow_iso(), "audited": len(slugs),
        "total_items": total_items,
        "flagged_entries": len(flagged),
        "top_link_domains": dict(domain_all.most_common(12)),
        "flagged": flagged, "errors": errors,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
