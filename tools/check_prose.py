# -*- coding: utf-8 -*-
"""语言质量预检（反欧化；ADR-0020，告警级，不进 CI）。

用法: python tools/check_prose.py <路径>... [--strict]
输出: stdout JSON {files, issues:[{path,line,rule,detail}]}

规则（余光中《怎样改进英式中文》清单的机检子集，阈值见各则）:
      long-sentence（单句 >=70 汉字，以 。；！？ 分段）
      passive-bei（单句 >=2 个“被”）
      weak-verb（进行/作出/加以/予以 + 抽象名词）
      de-chain（“的”三连，或单句 >=6 个“的”）
      plural-men（类名词+“们”：作者们/科学家们等）
      as-one（“作为一个”）
      exists-there（“存在着”）
      dang-shihou（“当……的时候”）
      tense-adverb（“曾于/已于”+数字年：时态词冗余，2026-11-14 扩项 specs/027）
      conj-he-verb（并列连词“和/与/及”连接动词对，或“，和”接分句；2026-11-14 扩项）
      chenggong-de（“成功地”：既成即冗余副词；2026-11-14 扩项）

豁免: 围栏代码块与行内代码、数学定界符 $…$/$$…$$、表格行、标题行、
      脚注定义行、参考文献节（含 ADR-0011 还原的中文著录行，非叙述散文）、
      竖线列表行（如"相关词条"A｜B｜C 行，含 ≥2 个未转义 |）、
      "进行中/进行中的"（体貌义，非弱动词结构），
      词内"的"——"目的论""目的"（名词与术语，非结构助词；2026-11-08 S5），
      词内"被"——"被动"（术语"主动/被动"，非被字句标记；2026-11-08 S5），
      汉字占比 <50% 或汉字数 <8 的行（公式、链接、英文镜像行）。

退出码: 0 无问题（告警级，默认不拦提交）；1 有 issue（仅 --strict 时）。
告警不替代逐句校对（rules/02）：每条告警逐条人工判断后修改或豁免，
禁止机械改写；重复出现的同类误报按 S5 沉淀为白名单而非放宽阈值。
"""
import json
import re
import sys

sys.path.insert(0, __file__.rsplit("\\tools", 1)[0].rsplit("/tools", 1)[0])

from tools.common import read_text  # noqa: E402

HAN = r"\u4e00-\u9fff\u3400-\u4dbf"
RULES = ("long-sentence", "passive-bei", "weak-verb", "de-chain",
         "plural-men", "as-one", "exists-there", "dang-shihou",
         "tense-adverb", "conj-he-verb", "chenggong-de")

SENT_SPLIT_RE = re.compile(r"[。；！？]")
BIB_HEADING_RE = re.compile(
    r"^#{1,6}\s*(?:参考文献|Bibliography|References（引用注释）)\s*$", re.I)
MATH_RE = re.compile(r"\$\$.+?\$\$|\$[^$]+\$")
CODE_SPAN_RE = re.compile(r"`[^`]*`")

WEAK_RE = re.compile(r"(?:进行(?!中)|作出|加以|予以)了?(?:进一步|初步)?[%s]{2}" % HAN)
MEN_RE = re.compile(
    r"(?:作者|科学家|哲学家|读者|批评者|辩护者|支持者|反对者|回应者|论者"
    r"|逻辑学家|认识论者|参与者|使用者|观察者|行动者)们")
AS_ONE_RE = re.compile(r"作为一个")
EXISTS_RE = re.compile(r"存在着")
DANG_RE = re.compile(r"当[^。；！？\n]{1,20}的时候")
DE_CHAIN_RE = re.compile(r"[%s]的[^。；！？\n]{0,12}的[^。；！？\n]{0,12}的" % HAN)
HAN_RE = re.compile(r"[%s]" % HAN)
# 2026-11-14 扩项（specs/027 FR-002；余光中《从西而不化到西而化之》判例 6-9/38）
TENSE_RE = re.compile(r"曾于|已于")
_VERB = ("帮助|支持|讨论|研究|分析|处理|审查|评估|评价|比较|考察|制定|制订|建立"
         "|发展|维护|保护|改进|改善|提高|加强|推广|应用|实施|执行|使用|利用|探索"
         "|检验|验证|构造|证明|论证|反驳|批判|批评|阐述|描述|刻画|界定|区分|辨析"
         "|推翻|放弃|接受|采纳|拒绝|促成|阻止|避免|消除|解决|通过|批准")
CONJ_HE_VERB_RE = re.compile(r"(?:%s)的?(?:和|与|及)(?:%s)" % (_VERB, _VERB))
CONJ_HE_CLAUSE_RE = re.compile(r"，和")
CHENGGONG_RE = re.compile(r"成功地")


def check_line(path, lineno, line, issues):
    text = MATH_RE.sub("\x00", line)
    text = CODE_SPAN_RE.sub("\x00", text)
    if text.lstrip().startswith("[^"):
        return
    if text.count("|") >= 2:  # 竖线列表行（相关词条等），非叙述散文
        return
    han = HAN_RE.findall(text)
    body = re.sub(r"\s", "", text)
    if len(han) < 8 or len(han) * 2 < len(body):
        return
    for sent in SENT_SPLIT_RE.split(text):
        s_han = HAN_RE.findall(sent)
        if len(s_han) < 8:
            continue
        excerpt = sent.strip().replace("\x00", "")[:40]
        if len(s_han) >= 70:
            issues.append({"path": path, "line": lineno,
                           "rule": "long-sentence",
                           "detail": "单句 %d 汉字（阈值 70）：%s" % (len(s_han), excerpt)})
        if sent.count("被") >= 2:
            # "被动"为术语（主动/被动），不是被字句标记（S5 白名单 2026-11-08）
            # "被试"为名词（实验被试），不是被动标记（S5 白名单 2026-11-09）
            if sent.replace("被动", "\x00\x00").replace("被试", "\x00\x00").count("被") >= 2:
                issues.append({"path": path, "line": lineno,
                               "rule": "passive-bei",
                               "detail": "单句 %d 个“被”：%s" % (sent.count("被"), excerpt)})
        de_text = sent.replace("目的论", "\x00\x00\x00").replace("目的", "\x00\x00")
        if DE_CHAIN_RE.search(de_text) or de_text.count("的") >= 6:
            issues.append({"path": path, "line": lineno,
                           "rule": "de-chain",
                           "detail": "“的”连用或密度过高：%s" % excerpt})
        # "创作出"为"创作+出"，非弱动词"作出"（S5 白名单 2026-11-09）
        if WEAK_RE.search(sent.replace("进行得", "\x00\x00\x00").replace("创作出", "\x00\x00\x00")):
            issues.append({"path": path, "line": lineno,
                           "rule": "weak-verb",
                           "detail": "弱动词（进行/作出/加以/予以+名词）：%s" % excerpt})
        if MEN_RE.search(sent):
            issues.append({"path": path, "line": lineno,
                           "rule": "plural-men",
                           "detail": "类名词+“们”：%s" % excerpt})
        if AS_ONE_RE.search(sent):
            issues.append({"path": path, "line": lineno,
                           "rule": "as-one",
                           "detail": "“作为一个”冠词直译：%s" % excerpt})
        if EXISTS_RE.search(sent):
            issues.append({"path": path, "line": lineno,
                           "rule": "exists-there",
                           "detail": "“存在着”存在句直译：%s" % excerpt})
        if DANG_RE.search(sent):
            issues.append({"path": path, "line": lineno,
                           "rule": "dang-shihou",
                           "detail": "“当……的时候”直译框架：%s" % excerpt})
        if TENSE_RE.search(sent):
            issues.append({"path": path, "line": lineno,
                           "rule": "tense-adverb",
                           "detail": "时态词冗余（曾于/已于，时间靠语境）：%s" % excerpt})
        if CONJ_HE_VERB_RE.search(sent) or CONJ_HE_CLAUSE_RE.search(sent):
            issues.append({"path": path, "line": lineno,
                           "rule": "conj-he-verb",
                           "detail": "“和/与”连接动词或分句（改并/且或顿号）：%s" % excerpt})
        if CHENGGONG_RE.search(sent):
            issues.append({"path": path, "line": lineno,
                           "rule": "chenggong-de",
                           "detail": "“成功地”既成即冗余：%s" % excerpt})


def check_file(path):
    issues = []
    in_biblio = False
    in_fence = False
    for lineno, line in enumerate(read_text(path).splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("#"):
            in_biblio = bool(BIB_HEADING_RE.match(line))
            continue
        if in_biblio:
            continue
        if line.startswith("|"):
            continue
        check_line(path, lineno, line, issues)
    return issues


def main(argv):
    args = [a for a in argv if a != "--strict"]
    strict = "--strict" in argv
    if not args:
        print(__doc__)
        return 2
    issues = []
    for path in args:
        issues.extend(check_file(path))
    print(json.dumps({"files": len(args), "issues": issues},
                     ensure_ascii=False, indent=2))
    return 1 if strict and issues else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
