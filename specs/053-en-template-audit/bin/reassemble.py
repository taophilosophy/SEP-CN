# -*- coding: utf-8 -*-
r"""B3.1 逆向装配器 R（specs/053 §7/§9；收缩对 C∘R=id_md）。

定理 T6/T7 语境：md 是转换器 C 的像，R 只需为每个 md 找到一个原像使
C(R(md)) == md（字节级）。歧义处（希腊字母、被丢链接、拆分标题）按收缩对
性质任意选定原像，不追求 R∘C=id。

设计（同源对照，ADR-0073）：R 不重实现转换语义——装配出的 HTML 交给
yuanwen 的同一套生产函数（extract_blocks_raw→render_blocks→build_cite_keys→
link_citations）求值。引注标记 [^bib-key] 从正文剥除（link_citations 确定性
重生成）；[^note-N] 还原为 <a href="notes.html#N">；Notes（原文脚注）节与
[^note-N]: 定义剥除（convert_notes 从 notes.html 再生）；References（引用注释）
改名 Bibliography 并剥固定注（render_blocks 再生）。

加强复核（ADR-0067 四件套内建）：
  ①守恒——R(md) 经 parse_entry 解析零错误＋marker/pubinfo B0 抽检；
  ②同源——求值用生产函数原体（本文件只做 md→HTML 的右逆）；
  ③负向——--selftest 篡改 md 一段必须破坏不动点；
  ④交集——试金石含补丁件（P-001 incommensurability，求值视图 en⊕patches）。

用法:
  reassemble.py [slugs...] [--out PATH]      # 缺省试金石：leucippus＋11 校准件
  reassemble.py --selftest                   # 负向证伪
退出码: 0 全部不动点成立；1 有失败；2 用法/selftest 失败。
只读判官：不写 en/、yuanwen/、baseline（R 的输出只在内存）。
"""
import argparse
import hashlib
import html as _html_mod
import io
import json
import os
import re
import sys
import time

html_unescape = _html_mod.unescape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I 模式不带脚本目录

from tools import parser, yuanwen  # noqa: E402
from article_ledger import table_spans  # noqa: E402  （表块扫描与账同一实现）
from tools.common import repo_path, read_text  # noqa: E402

if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8")

TRIAL = ["leucippus", "david", "elias", "peirce-benjamin", "evolution",
         "reism", "holes", "lady-masham", "richard-sophister", "cockburn",
         "penbygull", "crathorn", "incommensurability", "abelard",
         "bayes-theorem"]

MD_HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
MD_DEF_RE = re.compile(r"^\[\^([^\]\s]+)\]:(.*)$", re.S)
# 脚注键：`note-<id>`，例外＝后缀四位年份者（书目区散文段被 C 当条目建键，
# `note-2005` 判例）——与 article_ledger._is_note_key 同判据（账与 R 同语料）
NOTEDEF_KEY_RE = re.compile(r"^note-(?!1[5-9]\d\d\b|20\d\d\b)\S+$")
MD_LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.])\s+(.*)$")
OL_ITEM_RE = re.compile(r"^(\d+)\.\s+(.*)$")
UL_ITEM_RE = re.compile(r"^[-*+]\s+(.*)$")
SUB_MAP = getattr(yuanwen, "SUB_MAP", {})
SUP_MAP = getattr(yuanwen, "SUP_MAP", {})
GREEK_UNI = getattr(yuanwen, "GREEK_UNI", {})
GREEK_C_DEFER = getattr(yuanwen, "GREEK_C_DEFER", set())
GREEK_REV = {}
for _k, _v in GREEK_UNI.items():
    GREEK_REV.setdefault(_v, _k)  # 同形多宏取首名（phi 优先于 varphi）
def _rev_pref_ascii(mp):
    """字形 → 源字符：同形多源取 ASCII 源。

    H0 的 sup/sub 内文零裸非 ASCII（全库普查），`⁻`/`₋` 只可能来自 ASCII
    `-`；C 的 `−`（U+2212）键在 H0 无对应裸形（`&minus;` 走实体通道），
    故取 ASCII 键才可逆（logic-connexive 判例）。
    """
    rev = {}
    for k, v in mp.items():
        if v not in rev or (ord(rev[v]) > 127 and ord(k) < 128):
            rev[v] = k
    return rev


SUP_REV = _rev_pref_ascii(SUP_MAP)
SUB_REV = _rev_pref_ascii(SUB_MAP)
# sup/sub 内文的 H0 实体拼写表（全库普查 60 字符：一字符一拼、剥标签剥实体后
# 零裸非 ASCII；含 `<sup><i>L</i>(&#8477;)</sup>` 一类带标签内文）。只收非 ASCII
# 字符——`&`/`<`/`>` 在 `_inline_md_to_html` 入口（见上文转义行）已成实体形，
# 与 H0 拼写一致，再映射会双转义（`&amp;gt;` 判例）。
# 铁律：C 的 `_subsup_md` 跑在 `unescape` 之前，内文写裸字符会被折成原生字形
# （B3.1 破）；写实体形则 C 视作“不可映射”保留 `^{…}`，解码后与 md 相等。
SUPSUB_ENT = {
    "\u00a9": "&copy;",
    "\u00b7": "&middot;", "\u00e8": "&egrave;", "\u0242": "&#578;",
    "\u0387": "&#903;", "\u0393": "&Gamma;", "\u0394": "&Delta;",
    "\u0398": "&Theta;", "\u03a0": "&Pi;", "\u03a6": "&Phi;",
    "\u03a9": "&Omega;", "\u03b1": "&alpha;", "\u03b2": "&beta;",
    "\u03b3": "&gamma;", "\u03b4": "&delta;", "\u03b7": "&eta;",
    "\u03b8": "&theta;", "\u03ba": "&kappa;", "\u03bb": "&lambda;",
    "\u03bc": "&mu;", "\u03bd": "&nu;", "\u03be": "&xi;",
    "\u03bf": "&omicron;", "\u03c0": "&pi;", "\u03c4": "&tau;",
    "\u03c6": "&phi;", "\u03c8": "&psi;", "\u03c9": "&omega;",
    "\u2009": "&thinsp;", "\u2013": "&ndash;", "\u201c": "&ldquo;",
    "\u2020": "&dagger;", "\u2032": "&prime;", "\u2033": "&Prime;",
    "\u2119": "&#8473;", "\u211d": "&#8477;", "\u2135": "&alefsym;",
    "\u2192": "&rarr;", "\u2203": "&exist;", "\u2208": "&isin;",
    "\u2212": "&minus;", "\u2217": "&lowast;", "\u221e": "&infin;",
    "\u2227": "&and;", "\u2228": "&or;", "\u227c": "&#8828;",
    "\u2283": "&sup;", "\u2295": "&oplus;", "\u2297": "&otimes;",
    "\u2298": "&#8856;", "\u2308": "&lceil;", "\u2309": "&rceil;",
    "\u25a1": "&#9633;", "\u25ca": "&loz;", "\u266f": "&#9839;",
    "\u29b8": "&#10680;", "\ud835\udd39": "&#120121;",
}


def _supsub_inner(x):
    """`^{…}`/`_{…}` 内文 → H0 拼写（命中实体表者写实体形，余者原样）。

    表只含非 ASCII 字符，故 R 自己插入的标签（`<sub>`/`<em>`，如 `^{n₀}` ←
    H0 `<sup>n<sub>0</sub></sup>` 的嵌套降级）天然不受影响。表外字符（`½`
    等 H0 从不出现者）原样，交装配补集池吸收。
    """
    if not any(c in SUPSUB_ENT for c in x):
        return x
    return "".join(SUPSUB_ENT.get(c, c) for c in x)
_EM = None  # 按件实体策略（codepoint → 实体串）；reassemble_article 入口设置
_GREEK = None  # 按件希腊宏账（同形字 phi/varphi 按出现序），入口设置
_GREEK_IDX = {}
_LINKS = None  # 按件内部链接账（[{text,href}]，文档序）；C 丢弃的内部链接由此还原
_LINKS_USED = None  # 已消费标记
_LINK_SEEN = None  # 各锚文已过历的词界出现次数（旧 nth 定位，已弃用）
_LINK_IDX = None  # 文档序游标：下一条待消费的链接账条目
_ITAL = "em"  # 按件斜体标签名（em/i）
_GREEK_FORM = None  # 按件希腊字形态："em" 表示 <em>&alpha;</em> 而非宏
_MATH_FORMS = None  # 按件显示公式形态账（文档序 "br"／"naked"）
_MATH_DOLLARS = None  # 按件行内公式美元源形账（[[体内指纹, "db…"]]，消费式）
_MATH_IDX = [0]     # 显示公式游标（reassemble_article 重置）
_ITAL_NAMES = []    # 文档序预排的斜体希腊 (字形, 宏名)，哨兵 \x15k\x15 索引
_SUP_POS = None     # 上下标同页双源按位账（cp → ["ent"|"tag", …]，文档序）
_SUP_IDX = {}       # 双源游标 (tag, cp) → 已消费次数
_BQ = None          # 按件引块形态账（0＝首子 <p>/<table>，1＝裸装文字），文档序
_BQ_IDX = [0]       # 引块游标
_PUBINFO_DONE = [False]  # pubinfo 合成层只发一次（行位不设限：whitehead 判例）
_PHOTO_PRE = [False]     # 头部图账：题注段须在 h1 前（C 把 h1 提到 md 首行）
_CAPTION_LINE = [""]     # 重排跟走的题注行（作者行 i<=3 兜底须排除它）

_NOTE_FORMS = None  # 按件非规范脚注引用形（文档序列表 [{n, form}]）
_NOTE_IDX = [0]  # note_forms 消费游标（跨行持续；reassemble_article 重置）
_NOTE_SEEN = {}  # 已按规范形输出的键计数（游标跳过判据）


def _stripped_map(s):
    """去 md 记号（*、\\、_{…}/^{…} 括号）后的可见串 + 位置映射。"""
    out, pos, stack = [], [], []
    i = 0
    while i < len(s):
        if s.startswith("_{", i) or s.startswith("^{", i):
            stack.append(1)
            i += 2
            continue
        c = s[i]
        if c == "}" and stack:
            stack.pop()
            i += 1
            continue
        if c in "*\\":
            i += 1
            continue
        out.append(c)
        pos.append(i)
        i += 1
    return "".join(out), pos


def _occ_positions(flat, t):
    pat = "(?<![A-Za-z0-9])" + re.escape(t) + "(?![A-Za-z0-9])"
    return [m.start() for m in re.finditer(pat, flat)]


def _lead_ctx(flat, i):
    """锚文左侧**最后两个词**（小写；与账 extract_links 同式）。

    按字符取上下文会被 H0／md 折行位置不同打乱（R 逐行匹配），词边界才是
    折行不变量。md 引注标记 `[^key]` 在 H0 无形（H0 是同处的可见文），须先
    剥掉再取词，否则左邻词恒不相同（game-theory 引文链判例）。"""
    pre = re.sub(r"\[\^[^\]]*\]", "", flat[:i])
    pre = re.sub(r"\[\d+\]", "", pre)            # 可见脚注号（账侧同剥）
    pre = re.sub(r"\$[^$]*\$", "", pre)          # md 数学段（H0 侧账已抹）
    pre = re.sub(r"\s+", " ", pre).strip().lower()
    # 行首列表／引用记号不算词：C 把 H0 的 `<ol><li>` 转成 md 字面 `5. `，锚文
    # 紧跟记号时行内左邻只剩 `5.`，与账里跨行的前文词恒不符，短锚文随即 defer
    # 并连锁饿死全页（plato-laws `H` 前提列表判例：58 条饿死）。剥掉后前缀为空
    # 即“不可判”，按旧法放行。
    pre = re.sub(r"^(?:>\s*)+", "", pre)
    pre = re.sub(r"^(?:\d+|[a-z]{1,3})[.)]|^[-+]", "", pre).strip()
    parts = pre.split(" ") if pre else []
    # 只认**含 ASCII 字母**的词：H0 侧账把 `\(…\)` 剥净，md 侧对应位置常是
    # ADR-0049 降级后的裸希腊字母（`\(\phi\)`→`*φ*`）或标点残片，恒与账尾词
    # 错位一格（connectives-logic `#ref-34` 判例）。数字/标点词也不是左邻
    # 语义，滤掉后两侧一致；全被滤空即“不可判”，按旧法放行。
    parts = [w for w in parts if re.search(r"[A-Za-z]", w)]
    return " ".join(parts[-2:])


def _math_spans(s):
    """行内数学区间 [(起, 止)]（与 _scan_stash_math 同判据、不占有）。"""
    spans = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == "\\" and i + 1 < n:
            i += 2
            continue
        if c != "$":
            i += 1
            continue
        if s.startswith("$$", i):
            j = _display_end(s, i + 2)
            if j >= 0:
                spans.append((i, j + 2))
                i = j + 2
                continue
        else:
            j = _inline_end(s, i + 1)
            if j >= 0:
                spans.append((i, j + 1))
                i = j + 1
                continue
        i += 1
    return spans


def restore_links(line):
    """按账还原内部链接：**文档序游标**（账序＝H0 文档序）。

    旧法按“锚文第 nth 次词界出现”定位，遇嵌套锚文会重叠插入：H0 三处
    链接 `Section 3`／`Section 3`／`Section 3 above` 而 md 三处可见文皆
    为 `Section 3 above`，旧法把第 1 处同时判给前两条，产出
    `<a>[Section 3](#Or</a>igSyllArts)`（al-farabi-logic 判例）。改为顺序
    推进：每条从本行已消费位置之后取首个词界出现，账序与文序同时对位。

    题注标签不参与：C 注入的 `*Table 1:*`／`*Figure 1:*`（figlabel）与内文
    引用同形，游标会把链接挂到题注标签上（belief-merging 判例：H0 的
    `Table 1` 出现序 0,2,3,4,5,6 全在正文，第 1 次是题注 span）。2026-11-22
    试过「全局出现序＝账 nth」的精确匹配，全库实测池 −9（1,483→1,474，失池
    17 件：md 与 H0 的出现次数不等时反而全错位），已回退为游标法＋题注跳过。
    """
    global _LINK_IDX
    if not _LINKS:
        return line
    if re.match(r"\s*#{1,6}\s", line):
        # 标题行不消费链接：C 的标题一律无链接，而内文“见下文 Other Internet
        # Resources 一节”这类散文链接与标题同文，游标前置失配时会把链接挂到
        # 标题上（bruno 判例：`<h2><a href="#Oth">` 使区段切分认不出 OIR 头，
        # 整节并进 main-text）。全库正文标题内 href 链接 0 件，跳安全。
        return line
    flat, pos = _stripped_map(line)
    # 既有 md 链接的**文字段**（行坐标；与 `_link` 同一取域式）
    mdtxt = [(m.start(1), m.end(1)) for m in re.finditer(
        r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\((?:[^()\s]|\([^()]*\))*\)", line)]
    is_caption = bool(re.match(r"\s*\*[^*\n]", line))
    picks = []
    ceiling = 0
    j = _LINK_IDX or 0
    while j < len(_LINKS):
        lk = _LINKS[j]
        t = lk.get("text") or ""
        if not t:
            j += 1
            continue
        st = None
        mspans = _math_spans(line)
        mk = re.match(r"\s*\d+[.)] ", line)
        mk_end = mk.end() if mk else 0
        # 候选序：H0 记的**左邻字符**优先（`(<a>20</a>)` 的 `(`；同文另有
        # 裸 `[20]` 标记时不再抢位，possible-worlds 判例），其余顺次兜底
        cands = _occ_positions(flat, t)
        if not cands and len(t) >= 2 and re.match(r"[A-Za-z]", t):
            # 词内锚兜底（plato-ethics-shorter 判例：H0 折行劈词
            # `Hippias M<a href="#16">ajor</a>`，md 里 "ajor" 无词界可寻，
            # 26 条 link_miss 全由此起）。严格版：左邻片段须与账 lead 末词
            # 逐字相等（大小写不敏感）、片段起点是词界、锚文收在词界——
            # 三者齐备才认，否则宁可 defer（宽松子串版曾在 daoism 误挂，
            # 池 raw +35 而 items 不变，2026-11-24 判例）。
            _lead0 = lk.get("lead") or ""
            _lw = (_lead0.split(" ") or [""])[-1]
            if _lw and re.fullmatch(r"[A-Za-z]+", _lw):
                for m in re.finditer(re.escape(t), flat):
                    p = m.start()
                    q = p - len(_lw)
                    if q < 0 or flat[q:p].lower() != _lw:
                        continue
                    if q > 0 and flat[q - 1].isalnum():
                        continue
                    r = p + len(t)
                    if r < len(flat) and flat[r].isalnum():
                        continue
                    cands.append(p)
        _lead = lk.get("lead") or ""
        # 消歧只对**短锚文**（≤3 字符，多为数字/编号）生效：这类锚文同文
        # 多处出现且无法从上下文分辨（possible-worlds `20`、infinity `2`）。
        # 长锚文本身已足够唯一，强加词比对会因折行/标记差异误伤——全量
        # 实测：无条件词比对使未消费链接由 1,850 涨到 2,896。
        _short = len(t) <= 3
        _lwords = []
        if _lead:
            _lwords = _lead.split(" ") if _short else _lead.split(" ")[-1:]
            _lwords = [w for w in _lwords if re.search(r"[A-Za-z]", w)]
        if _lwords:
            _pref = []
            for c in cands:
                _ctx = _lead_ctx(flat, c)
                _cw = _ctx.split(" ") if _ctx else []
                if not _cw:
                    _pref.append(c)      # 行首无左邻词：不可判，按旧法放行
                    continue
                n = min(len(_cw), len(_lwords))
                if _cw[-n:] == _lwords[-n:]:
                    _pref.append(c)
            if _pref:
                cands = _pref
            elif _short:
                # 短锚文且本行候选左邻词全不符 → 该链接不在本行（留待后续行）
                break
            # 长锚文无匹配：按旧游标法（不 defer，避免连锁饿死同页后续链接）
        for cand in cands:
            if cand < ceiling:
                continue
            if (is_caption and cand == 0
                    and flat[len(t):len(t) + 1] == ":"):
                continue          # 题注标签位（`*Table 1:*`）：链接在正文
            a0 = pos[cand]
            if any(s0 <= a0 < e0 for s0, e0 in mspans):
                continue          # 数学体内不挂链接（infinity 判例：锚文 `1`
            #                   在 `$…=1$` 里被吃，右逆发 `\(…=1\)` 破坏公式）
            if a0 < mk_end:
                continue          # 有序列表标记位（trinity 判例：锚文 `1` 落在
            #                   `1. ` 标记上，行首成 `[1](…)`，列表解析失效）
            _be = pos[cand + len(t) - 1] + 1
            if any(s0 < _be and a0 < e0 for s0, e0 in mdtxt):
                continue          # 锚文落在既有 md 链接的文字段内：H0 从不嵌套
            #                   `<a>`，插进去只会把字面 `[..](..)` 留在链接文字里
            #                   （original-position 判例：C 把 H0 的「锚文＋后随
            #                   普通文字」合并成一条 md 链）
            # 跨度内定界星不配对时就地扩展（只认紧邻星）：可见跨度可跨过强调
            # 闭星（`*interpretations* of probability`），直接插入会让 <a> 跨
            # <em> 边界；扩展成 `[*interpretations* of probability](…)` 两边
            # 都合法。不能就地配平则弃此候选，绝不向远处吞字。
            b0 = pos[cand + len(t) - 1] + 1
            ok = True
            for _ in range(4):
                if len(re.findall(r"(?<!\\)\*", line[a0:b0])) % 2 == 0:
                    break
                if (a0 > 0 and line[a0 - 1] == "*"
                        and (a0 < 2 or line[a0 - 2] != chr(92))):
                    a0 -= 1
                elif line[b0:b0 + 1] == "*" and line[b0 - 1:b0] != chr(92):
                    b0 += 1
                else:
                    ok = False
                    break
            if not ok:
                continue
            st = cand
            break
        if st is None:
            break  # 本条不在本行（或在已消费区之前）——留待后续行
        picks.append((a0, b0, j, lk))
        ceiling = st + len(t)
        j += 1
    _LINK_IDX = j
    for a, b, idx, lk in sorted(picks, key=lambda x: -x[0]):
        # 锚文原样搬入（字面星在 C 侧已转义为 `\*`）；跨度已含就地配平的定界星
        # 方括号换成占位符：md 链接文字不允许裸 `[]`，H0 有些锚文自带 `(§5.1]`
        # 这类方括号（promises 判例；全库 223 条／23 页），不保护则 `[..](..)`
        # 语法塌成字面文本。`_link` 出口还原。
        seg = line[a:b].replace("[", "\x06").replace("]", "\x07")
        line = line[:a] + "[" + seg + "](" + lk["href"] + ")" + line[b:]
        _LINKS_USED[idx] = True
    return line


def _unsubsup(s, rev, tag):
    """连续同族上/下标字形段 → 单个 <sup>/<sub> 标签（C 只在整段可映射时产字形）。

    若该字符在按件 `entities` 账里（H0 原位就是实体形，如 `&sup2;`），不转
    标签——留给 `encode_outside_math` 发回实体（kant-science `mv²` 判例：
    H0 是 `&sup2;` 而 C 的 md 是裸 `²`，转 `<sup>2</sup>` 即错）。同页双源
    （`&sup2;` 与 `<sup>2</sup>` 并存）由 `sup_pos` 账按位定：文档序每次出现
    读原位形态，"ent" 留实体通道、"tag" 发标签（kant-science／proclus 判例）。"""
    if not rev:
        return s
    _keep = set(_EM or {})
    rev_all = rev
    dual = _SUP_POS or {}   # 账按 cp 平铺（上标/下标字形本不相交）
    rev = {c: n for c, n in rev.items() if c not in _keep or c in dual}
    if not rev:
        return s
    cls = "".join(re.escape(c) for c in rev)

    def rep(m):
        # 连续同族字形合并为**单个**标签（`<sub>n</sub><sub>+</sub>…` 会把
        # 字节流拆碎：adduction 判例 1,116→1,160）；双源/留实体处断组
        outs = []
        buf = []

        def flush():
            if buf:
                outs.append("<%s>%s</%s>" % (tag, "".join(buf), tag))
                del buf[:]

        for c in m.group(0):
            if c in dual:
                k = _SUP_IDX.get((tag, c), 0)
                _SUP_IDX[(tag, c)] = k + 1
                if k < len(dual[c]) and dual[c][k] == "ent":
                    flush()
                    outs.append(c)
                    continue
                buf.append(rev_all[c])
                continue
            if c in _keep:
                flush()
                outs.append(c)
                continue
            buf.append(rev_all[c])
        flush()
        return "".join(outs)
    return re.sub("[%s]+" % cls, rep, s)


def encode_outside_math(s, policy):
    """文本层非 ASCII 字符按件内实体形态回写；数学段与占位公式原样保留。"""
    if not policy:
        return s
    keep = []

    def st(m):
        keep.append(m.group(0))
        return chr(3) + str(len(keep) - 1) + chr(3)

    s = re.sub(r"""\\\([^)]*\\\)|\\\[[^\]]*\\\]|\d+""", st, s)
    s = "".join(policy.get(c, c) for c in s)
    for i, v in enumerate(keep):
        s = s.replace(chr(3) + str(i) + chr(3), v)
    return s


def _inline_end(s, i):
    """行内数学收口位置（`$` 下标）；扫不到 −1。`\\x` 转义对整体跳过。"""
    n = len(s)
    j = i
    while j < n:
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "$":
            return j
        j += 1
    return -1


def _display_end(s, i):
    """显示数学收口位置（`$$` 起始下标）；体内成对单美元跳过，失败 −1。"""
    n = len(s)
    j = i
    while j < n:
        if s[j] == "\\":
            j += 2
            continue
        if s.startswith("$$", j):
            return j
        if s[j] == "$":
            k = _inline_end(s, j + 1)
            if k < 0 or s.startswith("$$", k):
                return -1      # 内层配对与收口 `$$` 打架：判定失败，按字面留
            j = k + 1
            continue
        j += 1
    return -1


def _strip_sup_wrap(f):
    """`<sup>[ … ]</sup>` → 内层（md 已自带外层 sup 方括号时用；容空白）。"""
    m = re.fullmatch(r"<sup>\s*\[(.*)\]\s*</sup>", f, re.S)
    return m.group(1) if m else f


def _blank_dollars(body):
    """行内公式体内 `\\$`/`$` 统一换哨兵、折叠空白后的指纹（与账 extract_math_dollars
    同式；空白折叠同因：H0 与 md 换行位置不同，formal-epistemology 判例）。"""
    body = re.sub(r"\s+", "", body)
    for ch in ("\\$", "$"):
        body = body.replace(ch, "\x00")
    return hashlib.sha1(body.encode("utf-8")).hexdigest()[:16]


def _math_dollar_fix(body):
    """按账把行内公式里的 `\\$` 还原成原文形：`d`→裸 `$`，`b`→保留 `\\$`。

    无账命中（指纹不符/已消费/该件没记）一律原样——存疑不动，交补集池。
    """
    if not _MATH_DOLLARS or "\\$" not in body:
        return body
    key = _blank_dollars(body)
    pat = None
    for i, ent in enumerate(_MATH_DOLLARS):
        if ent[0] == key:
            pat = ent[1]
            del _MATH_DOLLARS[i]
            break
    if pat is None:
        return body
    out, i, j = [], 0, 0
    while i < len(body):
        if body.startswith("\\$", i):
            out.append("$" if j < len(pat) and pat[j] == "d" else "\\$")
            j += 1
            i += 2
            continue
        out.append(body[i])
        i += 1
    return "".join(out)


def _scan_stash_math(s, stash):
    """md 数学段扫描占位（`$…$` / `$$…$$`，转义感知，显示体允许成对单美元）。

    C 侧把 H0 `\\(…\\)` 写成 `$…$`、`\\[…\\]` 写成 `$$…$$`；显示体内部可合法
    含成对单美元（qm-consistent-histories 判例 `\\text{ for $\\alpha\\neq\\beta $ }`）。
    逐字符扫描：`\\x` 转义对整体跳过；`$$` 开显示段，单个 `$` 开行内段。
    收不到口一律按字面留原样（存疑不吞）。"""
    out, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c == "\\" and i + 1 < n:
            out.append(s[i:i + 2])
            i += 2
            continue
        if c != "$":
            out.append(c)
            i += 1
            continue
        if s.startswith("$$", i):
            j = _display_end(s, i + 2)
            if j >= 0:
                out.append(stash(s[i:j + 2]))
                i = j + 2
                continue
        else:
            j = _inline_end(s, i + 1)
            if j >= 0:
                out.append(stash(s[i:j + 1]))
                i = j + 1
                continue
        out.append(c)
        i += 1
    return "".join(out)


def _inline_md_to_html(text):
    """md 行内 → 行内 HTML（inline_to_md 的右逆；只覆盖 C 像内出现的形）。"""
    s = text
    # 嵌套表原样透传：md 管道格内可含 C 存的 raw `<table>…</table>`
    # （altruism-empirical／benjamin 等，C 的行内表暂存把内层表整段塞进格）。
    # 结构由 render_tables 按账**递归**重建，此处只护住不被文本层转义成
    # `&lt;table`（旧式：整段变文字，B 侧文字流多出 4 KB 标签源码）。
    tbl_store = []

    def _stash_tbls(text):
        """按**深度配平**取顶层表区间占位：非贪婪正则会在内层 `</table>` 早断
        （benjamin 判例：外层表剩半截被转义成 `&lt;/td&gt;…`）。"""
        spans = table_spans(text)
        if not spans:
            return text
        base = len(tbl_store)
        tbl_store.extend(text[st:en] for st, en in spans)
        for k in range(len(spans) - 1, -1, -1):
            st, en = spans[k]
            text = text[:st] + "\x07T%d\x07" % (base + k) + text[en:]
        return text

    s = _stash_tbls(s)    # 文本层转义：C 在输出端 unescape，R 必须先把字面 & < > 编码回实体——
    # 否则 md 里的 <URL> 尖括号在装配 HTML 中被当标签吃掉（bayes-theorem 判例）
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # 字面转义星（\*）占位保护——必须在强调解析前隔离，否则 *H\** 会被
    # 拆成 *H** 破配对（bayes-theorem 判例）；解析后还原为裸 *
    # 注意：必须放在数学占位之后（下方），否则数学体内的 `\*`（TeX 转义星，
    # axiom-choice 判例 `\mbox{using (\*)}`）会被当正文星还原成 `*`。
    # 图片（C 的 _image 像：`![alt](../assets/<slug>/<file>)`）→ <img>。
    # 先占位后还原：alt 是属性文字，不得经受星/上下标/数学规则
    # （action-perception 的长 alt 含 `[` 与 `]`，须容一级方括号）
    img_store = []

    def _stash_img(alt, url):
        m2 = re.fullmatch(
            r"\.\./assets/[a-z0-9-]+/([A-Za-z0-9._%+-]+)", url)
        src = m2.group(1) if m2 else url
        img_store.append('<img src="%s" alt="%s" />' % (src, alt))
        return "\x03%d\x03" % (len(img_store) - 1)

    def _stash_imgs(s):
        """图片占位：平衡方括号扫描。旧正则只容一级嵌套 `[...]`，而 C 把 H0
        的 alt 属性原样搬运，7 页 alt 含 2–5 级（word-meaning／
        generalized-quantifiers／negation／computational-linguistics／
        geometry-finitism 等），字面 `![` 漏进正文层（negation 判例）。
        另有上游 alt 自身方括号不平衡（emotion `…'ACTIVATION' ]north], …`，
        H0 属性原笔误）：平衡扫描失败时按行内 URL 锚定兜底（`](…)` 前无
        杂字，alt 取到该 `]` 为止）。"""
        out, i, n = [], 0, len(s)
        while i < n:
            j = s.find("![", i)
            if j < 0:
                out.append(s[i:])
                break
            d, k = 1, j + 2
            while k < n and d:
                c = s[k]
                if c == "\\":
                    k += 2
                    continue
                if c == "[":
                    d += 1
                elif c == "]":
                    d -= 1
                k += 1
            e = -1
            if not d and k <= n and k < n and s[k] == "(":
                e = s.find(")", k)
            url = s[k + 1:e] if e >= 0 else ""
            if e < 0 or not url or re.search(r"\s", url):
                # 兜底：不平衡 alt（emotion 判例）——非贪婪取行内 `](url)`
                m = re.match(r"!\[([^\n]*?)\]\(([^)\s]+)\)", s[j:], re.S)
                if m:
                    out.append(s[i:j])
                    out.append(_stash_img(m.group(1), m.group(2)))
                    i = j + m.end()
                    continue
                out.append(s[i:j + 2])
                i = j + 2
                continue
            out.append(s[i:j])
            out.append(_stash_img(s[j + 2:k - 1], url))
            i = e + 1
        return "".join(out)

    s = _stash_imgs(s)
    # 引注标记剥除——link_citations 确定性重生成（keys 同源）
    s = re.sub(r"\[\^(?!note-)[^\]\s]+\]", "", s)
    # 注释引用 → 锚链接（NOTE_REF_RE 可匹配的两种 href 形任选其一）
    # 注释引用 → 站点原始形（<sup>[<a href="notes.html#note-N">N</a>]</sup>；
    # 方括号在 sup 内——C 侧 NOTE_REF_RE 的规范形）；非规范形（H0 直接写
    # `see <a href="notes.html#note-14">footnote 14</a>`，agent-modeling
    # 判例）由按件账 note_forms 给原形——账按文档序存列表，游标逐个消费
    # （同一键可既有规范脚注又有散文原形，按键记字典会互相覆盖）
    def _note_ref(nm):
        n = nm.group(1)
        # md 已把外层 sup+方括号写成 `^{[ … ]}`（`^{[[^note-7]]}`，legal-reas-prec
        # 判例）：此时只发锚自身，否则与外层 `<sup>[ ]</sup>` 叠成双 sup。
        _pre = nm.string[max(0, nm.start() - 3):nm.start()]
        _post = nm.string[nm.end():nm.end() + 2]
        _bare = _pre.endswith("^{[") and _post.startswith("]}")
        forms = _NOTE_FORMS or []
        k = _NOTE_IDX[0]
        if k < len(forms) and forms[k]["n"] == n:
            _NOTE_IDX[0] = k + 1
            f = forms[k]["form"]
            if f:
                if _bare:
                    f = _strip_sup_wrap(f)
                return f
        else:
            # 账/文序不一致：前进一格保后续对齐，本处仍出规范形
            _NOTE_IDX[0] = k + 1 if k < len(forms) else k
        # 无账/规范形：装配（有账）时按 md 的 `^{[ … ]}` 包裹只发锚，单层
        # sup 与 H0 等值；B3.1 判官（无账）必须保留**双层 sup**——C 对
        # `#N`+`name=`+`<strong>` 这类异形不回折为裸 `[^note-N]`，只有外层
        # sup 才能让 C(R(md)) 复现 `^{[[^note-N]]}`（legal-reas-prec 判例）。
        anchor = '<a href="notes.html#note-%s">%s</a>' % (n, n)
        if _bare and _NOTE_FORMS is not None:
            return anchor
        return "<sup>[%s]</sup>" % anchor

    s = re.sub(r"\[\^note-([^\]\s]+)\]", _note_ref, s)
    # 数学先占位——TeX 内的 _{x}/^{x} 不得被下面的 sub/sup 规则改写
    # （dutch-book 判例：$\pr_{t}$ 曾变 $\pr<sub>t</sub>$ → C 出 ₜ）
    # 扫描式而非正则：C 把 H0 `\[ … \]` 整体包成 `$$…$$`，显示体内可以合法
    # 出现成对的单美元（qm-consistent-histories 判例 `\text{ for $\alpha
    # \neq\beta $ }`），任何 `[^$]` 型正则都会在第一个内部美元处断段、把收尾
    # `$$` 让给下一次匹配，产出 `$$$$`（identity-time／logic-intensional 判例）
    math_store = []

    def _stash_math(seg):
        math_store.append(seg)
        return "\x02%d\x02" % (len(math_store) - 1)

    s = _scan_stash_math(s, _stash_math)
    # 正文层字面星/美元/反斜杠占位（数学占位之后：数学体内的 `\*`/`\$`
    # 属 TeX，不得还原）。`\\` 必须先于 `\*`/`\$` 处理——C 侧把正文层孤立
    # 反斜杠双写成 `\\`（questions 判例），先吃掉成对方能正确切分转义对。
    s = s.replace("\\\\", "\x12")
    s = s.replace("\\*", "\x01")
    s = re.sub(r"(?<!\\)\\\$", "\x05", s)
    # C 侧行首 `#`（“不合语法”标记）转义成 `\#`（yuanwen 行首标题防线）
    s = s.replace("\\#", "\x13")
    # C 侧字面编号段落 `1\.`（H0 `<p>\n1. …`，alyngton 判例）：点号转义防
    # 被 markdown 当有序列表；此处还原字面 `1.`，行首 `N.` 不再触发列表分支
    s = s.replace("\\.", "\x18")
    # C 侧行首列表标记形 `\+ `/`\- `（berkeley 判例：引块首行 `+ Mind is…`）
    s = s.replace("\\+", "\x19")
    s = s.replace("\\-", "\x1a")
    # 原生上/下标 Unicode 字形 → <sup>/<sub>：C 的 _subsup_md 在“整段可映射”
    # 时直接产 Unicode 字形（6<sup>th</sup> → 6ᵗʰ），右逆须还原为标签段
    s = _unsubsup(s, SUP_REV, "sup")
    s = _unsubsup(s, SUB_REV, "sub")
    # 链接（分类还原；页内锚/index.html 链接 C 本就丢弃 → 纯文本）
    _MD_URL = re.compile(r"(?:https?:|\.\./|#|notes\.html#)"
                         r"|^[a-z0-9_-]+(\.[A-Za-z0-9_-]+)*\.md$"
                         r"|^[A-Za-z0-9._-]+\.html(#.+)?$")

    def _link(m):
        t, url = m.group(1), m.group(2)
        t = t.replace("\x06", "[").replace("\x07", "]")   # 账插入的方括号占位还原
        if not _MD_URL.match(url):
            # md 链接 URL 是闭集（普查 25,679 条：http／assets／../／#／notes／
            # slug(.slug)*.md／X.html(#frag)?）。闭集之外的 `](…)` 是**上游记号
            # 的字面文本**（ambiguity 判例：`[∀x:Bachelor(w,x)](Unmarried(x,w))`
            # 是 H0 原文的 regimented 记号），当链接吃掉会产生 `<a href=
            # "Unmarried(x,w)">` 这类坏锚。原样保留整段匹配。
            return m.group(0)
        if url.startswith(("http://", "https://")):
            # 站点惯例：外链带 target="other"（正文 21,345:1,440 实测；异形入补集）
            return '<a href="%s" target="other">%s</a>' % (url, t)
        m2 = re.fullmatch(r"\.\./assets/[a-z0-9-]+/([A-Za-z0-9._%+-]+)", url)
        if m2:
            return '<a href="%s">%s</a>' % (m2.group(1), t)
        m3 = re.fullmatch(r"([a-z0-9-]+)\.([a-z0-9-]+)\.md", url)
        if m3:
            return '<a href="%s.%s">%s</a>' % (m3.group(2), "html", t)
        # 内部链接账还原形（C 丢弃的两族：跨词条 `../slug/`、页内 `#anchor`）
        if url.startswith(("../", "#")):
            return '<a href="%s">%s</a>' % (url, t)
        # 带片段的裸兄弟链（账插入形 `other.html#frag`）：md 原本不保这类链
        if re.fullmatch(r"[A-Za-z0-9._-]+\.html#.+", url):
            return '<a href="%s">%s</a>' % (url, t)
        return t  # 其他页内／index.html 链接——C 原样丢链接保文本
    # 链接文字可含一级方括号（书目形 `[Ervin 1997 [2016] available online](url)`），
    # 但不得吞掉外层字面括号（`[[text](url)]` 取内层）；URL 可含一级圆括号
    s = re.sub(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]"
               r"\(((?:[^()\s]|\([^()]*\))*)\)", _link, s)
    # 记号星（`(1*)` 注解记号）不再需要 R 侧占位：C 已把正文层字面星统一
    # 转成 `(1\*)`，到此处是 `\x01`。旧占位 `\(\d+\*+\)` 反而吞掉合法强调的
    # 闭星（histfem-condorcet `(1786*)` 判例），已撤除。
    # 行内代码（先占位：代码内 `*` 是字面字符，2026-11-21 C 侧结构化转义后
    # md 里裸星只剩强调定界符，若不隔离代码段会被 _star_parse 误当定界符）
    code_store = []

    def _stash_code(m):
        code_store.append("<code>%s</code>" % m.group(1))
        return "\x11%d\x11" % (len(code_store) - 1)

    s = re.sub(r"`([^`]*)`", _stash_code, s)
    # sub/sup 记号（_{x}/^{x}）→ 标签；原生 Unicode 字形已由 C 直接产出，
    # R 不识别（原样文本，C 亦原样）。数学占位符内的记号不受影响。
    def _sup_sub_repl(tag):
        def rep(m):
            # 前接字面 TeX 命令（`\x12`＋字母，C 侧双写反斜杠的裸排环境漏在
            # 正文层：`\\phi_{100}`，formal-epistemology 判例）时保留字面，
            # 不下标——H0 该处是正文层 TeX 文本而非 md 上标记号
            if re.search("\x12[A-Za-z]+$", s[:m.start()]):
                return m.group(0)
            return "<%s>%s</%s>" % (tag, _supsub_inner(m.group(1)), tag)
        return rep

    s = re.sub(r"_\{([^}]*)\}", _sup_sub_repl("sub"), s)
    s = re.sub(r"\^\{([^}]*)\}", _sup_sub_repl("sup"), s)
    # 强调／粗体（单层；C 的 em 先于 strong，嵌套粗斜体在像内为 ***x***——
    # 简形词条未出现，残差清单登记）
    # 强调／粗体：小型星解析器——C 输出的强调定界符恒“紧”（内侧无空格，
    # _md_emphasis strip 保证），据此把裸星三分类：开／闭／字面（W10：
    # happens* 与 10 * Prob 的乘号/记号星不再被误配对）
    s = _star_parse(s)
    # 实体策略（按件位，见 article_ledger 的 entities 账）：文本层非 ASCII 字符
    # 按件内固定形态回写为实体；数学段与已占位公式不参与
    if _EM:
        s = encode_outside_math(s, _EM)
    # 数学占位还原（$x$ → \(x\)；$$x$$ → \[x\]）
    # 行内公式里的 `\$` 双源（H0 裸 `$` 与原文 `\$` 在 md 同形）由
    # `math_dollars` 账按体内指纹逐 span 判定（第二十三批）；无账命中原样保留。
    for idx, val in enumerate(math_store):
        if val.startswith("$$"):
            body = val[2:-2]
            # 显示体形态按账：H0 裸排环境（`\begin{align}` 无 `\[…\]` 包裹）
            # 原样发，不补定界符——C 的 wrap_naked_envs 只是渲染层约定，
            # 右逆必须与 H0 逐字节一致（belief-merging 判例）
            if (_MATH_FORMS and _MATH_IDX[0] < len(_MATH_FORMS)
                    and _MATH_FORMS[_MATH_IDX[0]] == "naked"):
                rep = body
            else:
                rep = r"\[" + body + r"\]"
            _MATH_IDX[0] += 1
        else:
            rep = r"\(" + _math_dollar_fix(val[1:-1]) + r"\)"
        s = s.replace("\x02%d\x02" % idx, rep)
    # 字面星还原（占位符 \x01 → 裸 *，在 HTML 文本层即普通字符）
    s = s.replace("\x01", "*")
    # 字面美元还原（C 侧 \$ 像 → 裸 $）
    s = s.replace("\x05", "$")
    # 字面反斜杠还原（C 侧双写的 `\\` → 裸 `\`）
    s = s.replace("\x12", "\\")
    # 行首 `#` 还原
    s = s.replace("\x13", "#")
    # 字面编号段落的点号还原（`1\.` → `1.`）
    s = s.replace("\x18", ".")
    # 行首列表标记形还原（`\+ `/`\- ` → 裸 `+ `/`- `）
    s = s.replace("\x19", "+")
    s = s.replace("\x1a", "-")
    # 嵌套表还原（结构重建在 render_tables 层；此处先撤销 C 的消毒）
    for idx, tag in enumerate(tbl_store):
        s = s.replace("\x07T%d\x07" % idx, _table_restore(tag))
    # 图片占位还原（alt 内已有文本层转义，不再加工）
    for idx, tag in enumerate(img_store):
        s = s.replace("\x03%d\x03" % idx, tag)
    # 代码段还原（含字面星，不再参与任何规则）
    for idx, tag in enumerate(code_store):
        s = s.replace("\x11%d\x11" % idx, tag)
    return s


def _unstash_math_tbl(t):
    """嵌套表内 `$…$`／`$$…$$` → `\\(…\\)`／`\\[…\\]`（C 消毒的逆）。"""
    out, i, n = [], 0, len(t)
    while i < n:
        if t[i] == "\\" and i + 1 < n:
            out.append(t[i:i + 2])
            i += 2
            continue
        if t.startswith("$$", i):
            j = _display_end(t, i + 2)
            if j >= 0:
                out.append("\\[" + t[i + 2:j] + "\\]")
                i = j + 2
                continue
        elif t[i] == "$":
            j = _inline_end(t, i + 1)
            if j >= 0:
                out.append("\\(" + t[i + 1:j] + "\\)")
                i = j + 1
                continue
        out.append(t[i])
        i += 1
    return "".join(out)


def _table_restore(tag):
    """C 的 `_sanitize_table_html` 逆变换（嵌套表原样还原时必须逐步撤销）。

    顺序取消毒的逆序：`&#42;`→`*`、`\\\\<`→`\\<`、`&#124;`→`|`、
    `src="../assets/<slug>/"`→`src="`、`$…$`→`\\(…\\)`。`<font>` 剥壳与
    空白压行不可逆（前者交补丁池、后者只是排版差）。"""
    tag = tag.replace("&#42;", "*")
    tag = re.sub(r"\\\\(?=<)", r"\\", tag)
    tag = tag.replace("&#124;", "|")
    tag = re.sub(r'(<img\b[^>]*\ssrc=")\.\./assets/[a-z0-9-]+/', r"\1", tag, flags=re.I)
    return _unstash_math_tbl(tag)


def link_misses():
    """未消费的内部链接账条目数（账与 md 不一致的硬信号）。"""
    if not _LINKS:
        return []
    return [lk for i, lk in enumerate(_LINKS) if i not in (_LINKS_USED or {})]


def _em(inner):
    """孤立希腊斜体回写 \\(\\alpha\\)（ADR-0049 逆映射，反斜杠必须有——C 侧
    fullmatch r'\\\\([A-Za-z]+)' 识别的是带杠命令名）；其余内容包 <em>。"""
    m0 = re.fullmatch("\x15(\\d+)\x15", inner)
    if m0:
        # 文档序预排哨兵（_plan_ital_greek）：名字已按全文档序定位
        k = int(m0.group(1))
        if k < len(_ITAL_NAMES):
            glyph, name = _ITAL_NAMES[k]
            if _GREEK_FORM == "em":
                return "<%s>%s</%s>" % (_ITAL, glyph, _ITAL)
            return r"\(\%s\)" % name
    m = re.fullmatch(r"([A-Za-z\u0370-\u03FF]+)", inner)
    if m and m.group(0) in GREEK_REV and m.group(0) not in GREEK_C_DEFER:
        if _GREEK_FORM == "em":
            return "<%s>%s</%s>" % (_ITAL, inner, _ITAL)
        name = _greek_next(m.group(0))
        return r"\(\%s\)" % name
    return "<%s>%s</%s>" % (_ITAL, inner, _ITAL)


def _greek_cp(tok):
    """宏名或字形 → 账内码位（GREEK_UNI 的 phi/varphi 同形取 φ）。"""
    if tok in GREEK_UNI:
        return GREEK_UNI[tok]
    if tok in GREEK_REV:
        return tok
    return None


def _plan_ital_greek(md, greek):
    """文档序预排斜体希腊宏名 → (md′, [(字形, 宏名)…])。

    C 把 H0 的孤立希腊公式（`\\(\\phi\\)`）转成 `*φ*` 斜体，md 只剩字形；账
    `greek` 记的是 **H0 全文档宏出现序**（数学段与斜体混排）。R 原按“斜体出
    现序”从账首顺取，凡与数学段交错即错位（ramsey 判例：第 8 处该 varphi
    取了 phi）。此处按文档序数：数学段内每次宏/字形占一位，斜体字形取其文
    档序号的名字，并把斜体改写成 `\\x15<序号>\\x15` 哨兵——位置信息随文本
    走，旁路（题注/表格）漏处理也不会让后续错位。围栏代码与反引号段跳过
    （R 先占位保护，其中的 `$` 与希腊字不入账）。"""
    if not greek:
        return md, []
    cnt = {}
    names = []
    out = []
    i, n = 0, len(md)
    math_re = re.compile(r"\\phi(?![A-Za-z])|\\varphi|[\u03c6\u03d5]")

    def take(cp):
        k = cnt.get(cp, 0)
        cnt[cp] = k + 1
        return k

    while i < n:
        c = md[i]
        if md.startswith("```", i):
            j = md.find("```", i + 3)
            j = n if j < 0 else j + 3
            out.append(md[i:j])
            i = j
            continue
        if c == "`":
            m = re.match(r"`+", md[i:])
            run = m.group(0)
            j = md.find(run, i + len(run))
            j = n if j < 0 else j + len(run)
            out.append(md[i:j])
            i = j
            continue
        if c == "\\" and i + 1 < n:
            out.append(md[i:i + 2])
            i += 2
            continue
        if c == "$":
            if md.startswith("$$", i):
                j = _display_end(md, i + 2)
                if j >= 0:
                    for m in math_re.finditer(md[i + 2:j]):
                        cp = _greek_cp(m.group(0).replace("\\", ""))
                        if cp:
                            take(cp)
                    out.append(md[i:j + 2])
                    i = j + 2
                    continue
            else:
                j = _inline_end(md, i + 1)
                if j >= 0:
                    for m in math_re.finditer(md[i + 1:j]):
                        cp = _greek_cp(m.group(0).replace("\\", ""))
                        if cp:
                            take(cp)
                    out.append(md[i:j + 1])
                    i = j + 1
                    continue
            out.append(c)
            i += 1
            continue
        if c == "*":
            m = re.match(r"\*([^*\n]+)\*", md[i:])
            if m:
                inner = m.group(1).strip()
                if (len(inner) == 1 and inner in GREEK_REV
                        and inner not in GREEK_C_DEFER):
                    cp = _greek_cp(inner)
                    seq = (greek or {}).get(cp) or []
                    k = take(cp)
                    nm = seq[k] if k < len(seq) else GREEK_REV.get(inner)
                    if nm:
                        names.append((inner, nm))
                        out.append("*\x15%d\x15*" % (len(names) - 1))
                        i += m.end()
                        continue
            out.append(c)
            i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out), names


def _greek_next(cp):
    """按件希腊宏：账内按出现序取，缺省用规范名。"""
    seq = (_GREEK or {}).get(cp)
    if seq:
        i = _GREEK_IDX.get(cp, 0)
        if i < len(seq):
            _GREEK_IDX[cp] = i + 1
            return seq[i]
    return GREEK_REV.get(cp)


def _star_parse(s):
    """md 星号 → HTML 强调（C 输出定界符恒紧：内侧无空格）。

    2026-11-21 起 C 侧把全部正文层字面星转义 `\\*`，md 裸星只剩定界符，故
    改为“按 run 逐星消费”：先由内向外闭（em 在内层，先闭；`***x***` 一次
    run 连闭两级），再用剩余星开（`**` 先于 `*`，与 C 的嵌套次序一致）。
    这样 `*q***P**`（em 紧接 strong 的相邻强调，bayes-theorem 判例）能正确
    拆成“闭 em 1 星 + 开 strong 2 星”，旧“整 run 定级”会误判为三连开星。
    旧“词内开星形态判定”（_intra_word_open）与“左邻字母数字不开星”保守
    试探随之撤除——乘法星/记号星不再需要在 R 侧猜。
    """
    parts = re.split(r"(\*+)", s)
    out = []
    marks = {}  # 'strong'/'em' -> out 中内容起始下标
    runs = {}   # slot -> 原始 run（未闭合时回填字面）

    def _close(kind):
        start = marks.pop(kind)
        content = "".join(out[start:])
        del out[start:]
        runs.pop(start, None)
        if kind == "em":
            out.append(_em(content.strip()))
        else:
            out.append("<strong>%s</strong>" % content)

    def _open(kind):
        slot = len(out)
        marks[kind] = slot
        out.append("")
        runs[slot] = "**" if kind == "strong" else "*"
        return slot

    for i, p in enumerate(parts):
        if i % 2 == 0:
            out.append(p)
            continue
        run = parts[i]
        before = parts[i - 1]
        after = parts[i + 1] if i + 1 < len(parts) else ""
        prev_tight = bool(before) and not before[-1:].isspace()
        next_tight = bool(after) and not after[:1].isspace()
        n = len(run)
        can_open_st = (n >= 2 and next_tight and "strong" not in marks)
        can_open_em = (n >= 1 and next_tight and "em" not in marks)
        # ① 整 run 可全作开星（无同级已开）时优先开——C 的嵌套形态
        #    `*ital **bold** end*`：em 未闭、`**` 是内层加粗的开，不得误当闭 em
        full_open = ((n == 1 and can_open_em) or (n == 2 and can_open_st)
                     or (n == 3 and can_open_st and can_open_em))
        if full_open:
            if n == 3:
                slot = _open("strong")
                marks["em"] = slot        # 同槽：`***x***` 的 em 在内层
                runs[slot] = "***"
            else:
                _open("strong" if n == 2 else "em")
            continue
        # ② 先闭：最内层优先（slot 大者后开先闭）；同槽时三级连闭先闭 em
        while n and prev_tight:
            if "em" in marks and "strong" in marks:
                if marks["em"] == marks["strong"]:
                    inner = "em" if n >= 3 else "strong"
                else:
                    inner = "em" if marks["em"] > marks["strong"] else "strong"
            elif "em" in marks:
                inner = "em"
            elif "strong" in marks:
                inner = "strong"
            else:
                break
            if inner == "strong":
                if n < 2:
                    if "em" in marks:   # 星数不够闭 strong，先闭更外的 em 腾位
                        _close("em")
                        n -= 1
                        continue
                    break
                _close("strong")
                n -= 2
            else:
                _close("em")
                n -= 1
        # ③ 残余星再开（n 已在闭星中递减，须就地重判），最后按字面
        if n >= 2 and next_tight and "strong" not in marks:
            _open("strong")
            n -= 2
        elif n >= 1 and next_tight and "em" not in marks:
            _open("em")
            n -= 1
        if n > 0:
            out.append("*" * n)
    # 未闭合星恢复为字面
    for slot, run in runs.items():
        if slot < len(out) and out[slot] == "":
            out[slot] = run
    return "".join(out)


def _td(cell):
    return "<td>%s</td>" % _inline_md_to_html(cell.strip())


def _render_bq(q, _depth=0):
    global _BQ_IDX
    _bare_bq = 0
    if _BQ:
        i = _BQ_IDX[0]
        if i < len(_BQ):
            _bare_bq = _BQ[i]
            _BQ_IDX[0] = i + 1

    """`>` 行（已剥一层前缀）→ 引块 HTML。主循环与 References 区共用。

    空 `>` 行＝段落分隔；连续非空行＝同段内 <br>（richard-sophister 判例：
    C 侧块内 BR_MARK 恢复为 \n 后每行加 '> '，无空行分隔）。
    嵌套：调用方只剥一层，剥后仍以 `>` **加空白/行尾**起的行属内层引块（md
    `> > x`），递归渲染成嵌套 `<blockquote>`——旧实现把 `>` 当字面文字留在
    正文，u 键多出 `>` 整页错位（logic-connexive／abrabanel 等 29 件，
    2026-11-22）。
    歧义判据：H0 有正文以字面 `>` 起（`&gt;<em>…`，scientific-representation
    判例），C 落 md 成 `> >*…`（标记后无空格）——与嵌套标记 `> > text`
    （有空格）靠“标记后是否空白”区分，故 NEST_RE 要求 `>` 后为空白或行尾。"""
    NEST_RE = re.compile(r"^>(?:\s|$)")

    def _blocks(lines):
        out, cur = [], []
        for line in lines:
            if line.strip():
                cur.append(line)
            elif cur:
                out.append(cur)
                cur = []
        if cur:
            out.append(cur)
        return out

    def _runs(block):
        """块内按「嵌套行 / 普通行」切连续段，保序。"""
        out, cur, isnest = [], [], None
        for ln in block:
            n = bool(NEST_RE.match(ln.lstrip()))
            if isnest is None or n == isnest:
                cur.append(ln)
                isnest = n
            else:
                out.append((isnest, cur))
                cur, isnest = [ln], n
        if cur:
            out.append((isnest, cur))
        return out

    paras = []
    for block in _blocks(q):
        for isnest, run in _runs(block):
            if isnest and _depth < 4:
                sub = [NEST_RE.sub("", ln, count=1) if NEST_RE.match(ln.lstrip())
                       else ln for ln in run]
                paras.append(("__nested__", sub))
            else:
                paras.append(("p", run))
    if not paras:
        return ""
    if (len(paras) == 1 and paras[0][0] == "p"
            and paras[0][1][0].strip().startswith("|")):
        rows = _pipe_rows("\n".join(paras[0][1]))
        cells = [[_td(c) for c in r] for r in rows]
        trs = "".join("<tr>%s</tr>" % "".join(cs) for cs in cells)
        return "<blockquote><table>%s</table></blockquote>" % trs
    inner = ""
    for kind, p in paras:
        if kind == "__nested__":
            inner += _render_bq(p, _depth + 1)
            continue
        if p[0].strip().startswith("|"):
            rows = _pipe_rows("\n".join(p))
            cells = [[_td(c) for c in r] for r in rows]
            trs = "".join("<tr>%s</tr>" % "".join(cs) for cs in cells)
            inner += "<table>%s</table>" % trs
        elif p and all(OL_ITEM_RE.match(x.strip()) for x in p if x.strip()):
            # 引块内有序列表（C 把 H0 的 <ol> 转成 `> 1. …` 行，bodin 判例）：
            # 整段全为列表项才转 <ol>，且序号必须从 1 起——start≠1 时 C 的
            # ol→md 不认 start（W9 残差），回写 `> 1.` 破坏 B3.1 不动点
            # （boole 等 10 件判例），此时维持旧 <p>
            items = [OL_ITEM_RE.match(x.strip()) for x in p if x.strip()]
            if int(items[0].group(1)) == 1:
                lis = "".join("<li>%s</li>" % _inline_md_to_html(m.group(2))
                              for m in items)
                inner += "<ol>%s</ol>" % lis
            else:
                inner += "<p>%s</p>" % "<br>".join(
                    _inline_md_to_html(x) for x in p)
        elif p and all(UL_ITEM_RE.match(x.strip()) for x in p if x.strip()):
            lis = "".join("<li>%s</li>" % _inline_md_to_html(
                UL_ITEM_RE.match(x.strip()).group(1))
                for x in p if x.strip())
            inner += "<ul>%s</ul>" % lis
        else:
            if _bare_bq:
                # H0 裸装引块（首子非 <p>，全库 6,120 处／798 页）：内容直接排在
                # <blockquote> 里，不套 <p>。套了每处多 4 段、整页 _sub_diff
                # 对不齐（descriptions Δ109、desert Δ44 判例）。行分隔用 H0
                # 拼写 `<br />`。
                inner += "<br />".join(_inline_md_to_html(x) for x in p)
            else:
                inner += "<p>%s</p>" % "<br>".join(
                    _inline_md_to_html(x) for x in p)
    return "<blockquote>%s</blockquote>" % inner


# ------------------------------------------------------------ 块级逆写 ----

def reassemble_article(md, authors, entity_map=None, links=None, greek=None,
                       italics=None, greek_form=None, note_forms=None,
                       math_forms=None, math_dollars=None, bq=None,
                       photo_pre_h1=None, sup_pos=None):
    """md（主档全文）→ (title, article_html)。不动点验证在调用方闭环。

    entity_map：按件实体策略（codepoint → 实体串）；None 表示不编码。
    links：内部链接账（C 丢弃的 `../slug/` 与 `#anchor` 链接），按文档序还原；
           未消费条目经 LINK_MISSES 暴露给判官（账/文不一致即红）。
    greek：按件希腊宏覆盖（同名不同宏：pi/varphi 之类 C 侧同形不可分）。"""
    global _EM, _LINKS, _LINKS_USED, _LINK_SEEN, _LINK_IDX, _GREEK, _GREEK_IDX
    # 空 citation_author meta 不造作者行（与 yuanwen.py 同步：plato-ethics-shorter
    # 判例，H0 带 content="" 的 meta，`'*%s*' % ''` 即孤立 '**'）
    authors = [a for a in (authors or []) if a and a.strip()]
    global _ITAL, _GREEK_FORM, _NOTE_FORMS, _MATH_FORMS, _MATH_DOLLARS
    global _ITAL_NAMES, _SUP_POS, _SUP_IDX
    md, _ITAL_NAMES = _plan_ital_greek(md, greek)
    _SUP_POS = sup_pos or None
    _SUP_IDX = {}
    global _BQ
    _BQ = bq or None
    _BQ_IDX[0] = 0
    _PUBINFO_DONE[0] = False
    _PHOTO_PRE[0] = bool(photo_pre_h1)
    _CAPTION_LINE[0] = ""
    _GREEK = greek
    _GREEK_IDX = {}
    _EM = entity_map
    _NOTE_FORMS = note_forms
    _MATH_FORMS = math_forms
    _MATH_DOLLARS = [list(e) for e in (math_dollars or [])]
    _MATH_IDX[0] = 0
    _LINKS = links or []
    _LINKS_USED = {}
    _LINK_SEEN = {}
    _LINK_IDX = 0
    _NOTE_IDX[0] = 0
    _NOTE_SEEN.clear()
    _ITAL = italics or "em"
    _GREEK_FORM = greek_form
    lines = md.split("\n")
    if _PHOTO_PRE[0]:
        # 头部图组提前：H0 的照片/题注块在 `<h1>` 之前，C 的 md 把 h1 提到首行、
        # 图与题注块留在其后（berlin 的题注还是独立块）；R 按 md 序发则段序
        # 错位（全库 26 页）。取「首个含 `![` 行到 pubinfo 行」整组提前；img 行
        # 在 pubinfo 之后（正文图）或相距过远则不动。行重排只在装配内部，
        # yuanwen 不动；B3.1 无账不重排。
        k0 = next((k for k, ln in enumerate(lines) if "![" in ln), None)
        if k0 is not None:
            grp = [lines[k0]]
            j = k0 + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            # 紧邻题注行（berlin 型：题注是独立块）：非标题/pubinfo/列表、
            # 短行才跟走；whitehead 型题注与图同行，不进此分支
            if (j < len(lines) and len(lines[j]) <= 200
                    and not lines[j].lstrip().startswith(("#", "|"))
                    and not PUBINFO_LINE_RE.fullmatch(lines[j].strip())
                    and not MD_LIST_RE.match(lines[j].strip())):
                # H0 的 img 与题注是 figure 内**两块**，保块间空行
                grp.append("")
                grp.append(lines[j])
                take = (k0, j)
                _CAPTION_LINE[0] = lines[j]
            else:
                take = (k0,)
            rest = [ln for k, ln in enumerate(lines) if k not in take]
            lines[:] = grp + rest
    if _LINKS:
        infence = False
        new = []
        for ln in lines:
            if ln.strip().startswith("```"):
                infence = not infence
                new.append(ln)
                continue
            new.append(ln if infence else restore_links(ln))
        lines = new
    out = []          # HTML 片段
    title = None
    i = 0
    n = len(lines)
    bib_defs = []     # 文献定义（非 note-*），两遍扫描：先收集
    for ln in lines:
        dm = MD_DEF_RE.match(ln)
        if dm and not NOTEDEF_KEY_RE.match(dm.group(1)):
            bib_defs.append(dm.group(2).strip())
    bib_ul_emitted = False
    # 作者行精确匹配串（meta_authors 拼接；C 生成 md 的作者行即此形态）。
    # 行重排后作者行可能落到 i>3，免发改精确比对（whitehead 判例：题注是
    # 纯斜体行，重排后落进 i<=3 被宽松匹配误吃）。
    _author_join = "*%s*" % ", ".join(authors) if authors else None
    while i < n:
        ln = lines[i]
        stripped = ln.strip()
        if not stripped:
            i += 1
            continue
        # 前三行的合成层（C 再生，R 不装配）：pubinfo 行与作者行
        if not _PUBINFO_DONE[0] and PUBINFO_LINE_RE.fullmatch(stripped):
            # 合成层不设行位上限：图注/credit 行会把 pubinfo 行挤出前三行
            # （whitehead 判例：`[![…](…) *Photo by…*` 插行后 pubinfo 落成普通
            # 段落，整页段结构错位）。全文首个匹配行合成一次。
            out.append(_pubinfo_html([stripped]) or "")
            _PUBINFO_DONE[0] = True
            i += 1
            continue
        if (re.fullmatch(r"\*[^*]+\*", stripped)
                and stripped != _CAPTION_LINE[0]
                and (i <= 3 or (_author_join and stripped == _author_join))):
            i += 1
            continue
        m = MD_HEAD_RE.match(ln)
        if m:
            lv = len(m.group(1))
            text = m.group(2).strip()
            if lv == 1:
                # h1 直接装配（像内词条的 H1 多来自 article h1 块；meta 前缀
                # 仅在 md 不以 '# ' 开头时触发——装配后恒以 '# ' 开头）
                out.append("<h1>%s</h1>" % _inline_md_to_html(text))
                i += 1
                continue
            if text == "References（引用注释）":
                out.append("<h2>Bibliography</h2>")
                i += 1
                # 剥固定注（render_blocks 再生）；区内按文档序发题与散文段
                # （文献题可至 h4、题后散文须原位——18thGerman 判例），
                # 定义行统一在区末 ul 发射（B3.1 键序＝md 定义序）
                while i < n and (not lines[i].strip()
                                 or lines[i].startswith("> ")
                                 or lines[i].strip() == ">"):
                    i += 1
                while i < n:
                    s2 = lines[i].strip()
                    if not s2:
                        i += 1
                        continue
                    if s2.startswith("> ") or s2 == ">":
                        # 区内容引块（berkeley 判例：`### Berkeley's Works` 下
                        # 的 `[W]` 版本条目以 `>` 块排）。旧实现把区内所有 `>`
                        # 行一律跳过——原意只是跳过 C 注入的“原文参考文献已转
                        # 为脚注引用”固定注（已在区首 while 消费）
                        q = []
                        while i < n and lines[i].startswith(">"):
                            q.append(lines[i][1:].lstrip(" "))
                            i += 1
                        bq = _render_bq(q)
                        if bq:
                            out.append(bq)
                        continue
                    mh = MD_HEAD_RE.match(lines[i])
                    if mh:
                        lv2 = len(mh.group(1))
                        if lv2 <= 2:
                            break
                        out.append("<h%d>%s</h%d>" % (
                            lv2, _inline_md_to_html(mh.group(2).strip()), lv2))
                        i += 1
                        continue
                    if MD_DEF_RE.match(lines[i]):
                        i += 1
                        continue
                    if s2.startswith("|") or MD_LIST_RE.match(lines[i]):
                        break
                    out.append("<p>%s</p>" % _inline_md_to_html(s2))
                    i += 1
                if bib_defs and not bib_ul_emitted:
                    lis = "".join("<li>%s</li>" % _inline_md_to_html(d)
                                  for d in bib_defs)
                    out.append("<ul>%s</ul>" % lis)
                    bib_ul_emitted = True
                continue
            if text.startswith("Notes（原文脚注"):
                # 注释节是 C 在文末追加的末节（其后仅 cite defs），脚注内容可含
                # 引块/列表/公式块——一律跳到文件尾（affirmative-action 判例：
                # 只跳空行+def 行会把脚注里的列表漏成正文）
                i = n
                continue
            out.append("<h%d>%s</h%d>" % (lv, _inline_md_to_html(text), lv))
            i += 1
            continue
        if stripped.startswith(">"):
            # 引块：整块收集（含引块表）；剥 '> ' 前缀。
            # 空 `>` 行＝段落分隔；连续非空行＝同段内 <br>（richard-sophister 判例：
            # C 侧块内 BR_MARK 恢复为 \n 后每行加 '> '，无空行分隔）
            # 注意：只剥一层——`> > x` 是**嵌套引块**，剥成单层会破坏 B3.1
            # 不动点（C 转回 `> x` ≠ md 的 `> > x`；abrabanel/heraclitus/evil
            # 等 20 件实测回退）。嵌套层级的正确渲染待专项（需生成嵌套
            # <blockquote>），此处维持单层语义。
            q = []
            while i < n and lines[i].startswith(">"):
                q.append(lines[i][1:].lstrip(" "))
                i += 1
            bq = _render_bq(q)
            if bq:
                out.append(bq)
            continue
        if MD_DEF_RE.match(ln):
            # 定义行已两遍扫描收集（note-* 由 convert_notes 再生，文献由
            # Bibliography 区 ul 再生）——主循环一律跳过
            i += 1
            while i < n and lines[i].strip():
                i += 1
            continue
        if stripped.startswith("|"):
            rows, i = _pipe_rows_collect(lines, i)
            out.append(_table_html(rows))
            continue
        if MD_LIST_RE.match(ln):
            items, i = _collect_list(lines, i)
            out.append(_list_html(items))
            continue
        # 段落：连续非空、非结构行
        para = [stripped]
        i += 1
        while i < n and lines[i].strip() and not _is_block_start(lines[i]):
            para.append(lines[i].strip())
            i += 1
        text = " ".join(para)
        # 表题：table_to_md 输出 '*cap*' 紧贴表格（cap 自身可为 **bold**，
        # 故 md 形为 ***X***）——逆装配为 <caption>（bayes-theorem 判例）
        # 定界不得以 `**`（粗体）成对包裹——那可能是正文粗体段
        # （presupposition 判例）；单星（`*Table 1:*`）、三星开头
        # （`***Table 1***`／`***Table 5**: …*`，bayes-theorem 判例）仍是表题
        _cap_ok = text.startswith("*") and (
            not text.startswith("**") or text.startswith("***"))
        cm = re.fullmatch(r"\*(.+)\*", text) if _cap_ok else None
        j = i
        while j < n and not lines[j].strip():
            j += 1
        if cm and j < n and lines[j].strip().startswith("|"):
            rows, i = _pipe_rows_collect(lines, j)
            out.append(_table_html(rows, cap_md=cm.group(1)))
            continue
        out.append("<p>%s</p>" % _inline_md_to_html(text))
    # 文献 ul 已在 References（引用注释）分支原位发射（bib_ul_emitted 守卫）；
    # 文末不再发射——尾部 ul 落在 in_bib 区间外会被渲染成 md 列表（leucippus 判例）
    return title, "\n".join(out)


def _strip_md(text):
    return text.strip()


PUBINFO_LINE_RE = re.compile(r"\*\*First published[^*]*\*\*")


def _is_block_start(ln):
    s = ln.strip()
    return (not s or s.startswith(">") or s.startswith("|")
            or MD_HEAD_RE.match(ln) or MD_DEF_RE.match(ln)
            or MD_LIST_RE.match(ln) or PUBINFO_LINE_RE.fullmatch(s))


def _pubinfo_html(lines):
    for ln in lines:
        s = ln.strip()
        if s.startswith("**First published") and s.endswith("**"):
            inner = s[2:-2]
            return '<div id="pubinfo"><em>%s</em></div>' % inner
    return None


_CELL_SEP = re.compile(r"(?<!\\)\|")


def _split_pipe_cells(line):
    r"""按**未转义** `|` 分格，再把 `\|` 还原为格内字面管道。

    C 侧对格内字面管道转义为 `\|`（H0 `<td>|</td>` 判例，william-jevons／
    spinoza-attributes）；整行 `str.split("|")` 会把 `\|` 当分格符，`\` 留成
    格尾字面。"""
    parts = _CELL_SEP.split(line.strip())
    if parts and parts[0] == "":
        parts = parts[1:]
    if parts and parts[-1] == "":
        parts = parts[:-1]
    return [p.replace("\\|", "|") for p in parts]


def _pipe_rows(body):
    rows = []
    for ln in body.split("\n"):
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = _split_pipe_cells(s)
        if re.fullmatch(r"[\s:|-]+", s.strip("|")):
            continue  # 分隔行
        rows.append(cells)
    return rows


def _pipe_rows_collect(lines, i):
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        s = lines[i].strip()
        cells = _split_pipe_cells(s)
        if not re.fullmatch(r"[\s:|-]+", s.strip("|")):
            rows.append(cells)
        i += 1
    return rows, i


def _table_html(rows, cap_md=None):
    cells = [[_td(c) for c in r] for r in rows]
    trs = "".join("<tr>%s</tr>" % "".join(cs) for cs in cells)
    cap = ""
    if cap_md is not None:
        cap = "<caption>%s</caption>" % _inline_md_to_html(cap_md)
    return "<table>%s%s</table>" % (cap, trs)


def _collect_list(lines, i):
    items = []  # (indent, ordered, text)
    base_indent = len(lines[i]) - len(lines[i].lstrip())
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            break  # 松散列表：项间空行即列表边界（C 每 <ul> 紧排输出；
            # 桥接会把两个列表并成一个——atheism-agnosticism 判例）
        m = MD_LIST_RE.match(ln)
        if not m or (len(ln) - len(ln.lstrip())) < base_indent:
            break
        ind = len(ln) - len(ln.lstrip())
        ordered = m.group(2)[0].isdigit()
        items.append((ind, ordered, m.group(3)))
        i += 1
    return items, i


def _list_html(items):
    """一层列表 → <ul>/<ol><li>（嵌套缩进扁平化＝C list_to_md 的可逆形）。"""
    ordered = items[0][1]
    tag = "ol" if ordered else "ul"
    lis = "".join("<li>%s</li>" % _inline_md_to_html(tx) for _, _, tx in items)
    return "<%s>%s</%s>" % (tag, lis, tag)


# ------------------------------------------------------------ 求值闭环 ----

def convert_from_parts(slug, title, authors, article_html, notes_html=None):
    """同源求值：replicate convert_entry 主链（读映射原体），不落盘。"""
    authors = [a for a in (authors or []) if a and a.strip()]  # 空 meta 不造作者行
    article = yuanwen.strip_closed_comments(article_html)
    article, stash = yuanwen.protect_cross_block_math(article)
    ctx = yuanwen.Ctx(slug)
    yuanwen.render_blocks(yuanwen.extract_blocks_raw(article), ctx)
    md = "\n".join(ctx.out).strip()
    if not md.startswith("# "):
        md = "# %s\n\n%s" % (title, md)
    md = yuanwen._drop_duplicate_h1(md)
    if authors:
        md = md.replace("\n\n", "\n\n*%s*\n\n" % ", ".join(authors), 1)
    if notes_html:
        note_defs = yuanwen.convert_notes(notes_html, slug)
        if note_defs:
            md += "\n\n## Notes（原文脚注）\n\n" + "\n\n".join(note_defs)
    keys = yuanwen.build_cite_keys(ctx.bib_entries, fallback_author=slug)
    if keys:
        md, _, _used = yuanwen.link_citations(md, keys)
        md += "\n\n" + "\n\n".join("[^%s]: %s" % (k["key"], k["text"])
                                   for k in keys)
    md = yuanwen.restore_cross_block_math(md, stash)
    return md


def judge_slug(slug, baseline):
    rec = baseline.get(slug)
    if not rec:
        return {"slug": slug, "ok": False, "skipped": "not in baseline"}
    en_idx = repo_path("en", slug, "index.html")
    md_path = repo_path("yuanwen", rec.get("zh_doc") or "")
    if not os.path.exists(en_idx):
        return {"slug": slug, "ok": False, "skipped": "no en package"}
    if not os.path.exists(md_path):
        return {"slug": slug, "ok": False, "skipped": "no yuanwen md"}
    html0 = read_text(en_idx)
    md0 = io.open(md_path, encoding="utf-8").read().rstrip("\n")
    try:
        html1 = yuanwen.apply_en_patches(slug, html0)
    except Exception as ex:  # noqa: BLE001——判官报告，不中断全量
        return {"slug": slug, "ok": False, "skipped": "patch: %s" % ex}
    m = re.search(r'<meta name="citation_title" content="([^"]*)"', html1)
    authors = [html_unescape(a) for a in
               re.findall(r'<meta name="citation_author" content="([^"]*)"', html1)]
    notes_path = repo_path("en", slug, "notes.html")
    notes_html = read_text(notes_path) if os.path.exists(notes_path) else None
    title, article_r = reassemble_article(md0, authors)
    if not title:
        title = m.group(1) if m else slug
    # ①守恒抽检：装配体可解析＋marker/pubinfo 命中（mini-B0）
    pr = parser.parse_entry(article_r)
    b0_mini = {"sections": len([b for b in pr["blocks"]
                                if b["type"].startswith("h")]) > 0,
               "parses": True}
    # ②同源求值闭环
    md2 = convert_from_parts(slug, title, authors, article_r, notes_html)
    ok = md2 == md0
    res = {"slug": slug, "ok": ok, "md_len": len(md0),
           "b0_mini": b0_mini}
    if not ok:
        # O(n) 首差定位（difflib.SequenceMatcher autojunk=False 在大文件近等串
        # 上二次方，abelard 150KB 实证卡死——改前后缀修剪）
        pre = 0
        while pre < min(len(md0), len(md2)) and md0[pre] == md2[pre]:
            pre += 1
        suf = 0
        while (suf < min(len(md0), len(md2)) - pre
               and md0[len(md0) - 1 - suf] == md2[len(md2) - 1 - suf]):
            suf += 1
        res["first_diff"] = {"op": "replace",
                             "md": md0[max(0, pre - 60):len(md0) - suf + 60][-140:],
                             "asm": md2[max(0, pre - 60):len(md2) - suf + 60][-140:]}
    return res


def selftest(baseline):
    """负向证伪：篡改 md 任一段 → 不动点必须破坏。"""
    slug = "leucippus"
    rec = baseline[slug]
    md0 = io.open(repo_path("yuanwen", rec["zh_doc"]), encoding="utf-8").read()
    md0 = md0.rstrip("\n")
    lines = md0.split("\n")
    # 删一个正文段（首个非空、非结构、非定义行）
    idx = next(i for i, ln in enumerate(lines)
               if ln.strip() and not _is_block_start(ln) and i > 3)
    bad = "\n".join(lines[:idx] + lines[idx + 1:])
    html0 = read_text(repo_path("en", slug, "index.html"))
    authors = [html_unescape(a) for a in
               re.findall(r'<meta name="citation_author" content="([^"]*)"',
                          html0)]
    m = re.search(r'<meta name="citation_title" content="([^"]*)"', html0)
    title, article_r = reassemble_article(bad, authors)
    md2 = convert_from_parts(slug, m.group(1) if m else slug, authors,
                             article_r, None)
    return {"ok": md2 != bad, "slug": slug}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    baseline = {r["slug"]: r for r in json.load(io.open(
        repo_path("baseline", "entries.json"), encoding="utf-8"))["entries"]
        if isinstance(r, dict) and r.get("slug")}
    if args.selftest:
        res = selftest(baseline)
        print(json.dumps({"schema": "sep-cn-b31-selftest/1", "selftest": res},
                         ensure_ascii=False, indent=1))
        return 0 if res["ok"] else 2
    slugs = sorted(baseline) if args.all else (args.slugs or TRIAL)
    entries, n_ok, n_fail, n_skip = [], 0, 0, 0
    t0 = time.time()
    for idx, slug in enumerate(slugs, 1):
        ts = time.time()
        try:
            r = judge_slug(slug, baseline)
        except Exception as ex:  # noqa: BLE001——单件异常不中断全量
            r = {"slug": slug, "ok": False, "skipped": "error: %s" % ex}
        r["sec"] = round(time.time() - ts, 3)
        if r["sec"] > 5:
            sys.stderr.write("[b31] 慢件 %.1fs %s\n" % (r["sec"], slug))
            sys.stderr.flush()
        if args.all and idx % 50 == 0:
            sys.stderr.write("[b31] %d/%d 已过 %.0fs\n"
                             % (idx, len(slugs), time.time() - t0))
            sys.stderr.flush()
        entries.append(r)
        if r.get("skipped"):
            n_skip += 1
        elif r["ok"]:
            n_ok += 1
        else:
            n_fail += 1
    payload = {"schema": "sep-cn-b31-assembly/1",
               "generated_by": "specs/053 bin/reassemble.py",
               "total": len(entries), "ok": n_ok, "fail": n_fail,
               "skipped": n_skip, "entries": entries}
    out = args.out or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "results", "assembly-trial.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    sys.stderr.write("[b31] 总 %d：不动点 %d／失败 %d／跳过 %d → %s\n"
                     % (len(entries), n_ok, n_fail, n_skip, out))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
