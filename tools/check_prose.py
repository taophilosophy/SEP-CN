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

豁免: 围栏代码块与行内代码、数学定界符 $…$/$$…$$、表格行、标题行、
      脚注定义行、参考文献节（含 ADR-0011 还原的中文著录行，非叙述散文）、
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
         "plural-men", "as-one", "exists-there", "dang-shihou")

SENT_SPLIT_RE = re.compile(r"[。；！？]")
BIB_HEADING_RE = re.compile(
    r"^#{1,6}\s*(?:参考文献|Bibliography|References（引用注释）)\s*$", re.I)
MATH_RE = re.compile(r"\$\$.+?\$\$|\$[^$]+\$")
CODE_SPAN_RE = re.compile(r"`[^`]*`")

WEAK_RE = re.compile(r"(?:进行|作出|加以|予以)了?(?:进一步|初步)?[%s]{2}" % HAN)
MEN_RE = re.compile(
    r"(?:作者|科学家|哲学家|读者|批评者|辩护者|支持者|反对者|回应者|论者"
    r"|逻辑学家|认识论者|参与者|使用者|观察者|行动者)们")
AS_ONE_RE = re.compile(r"作为一个")
EXISTS_RE = re.compile(r"存在着")
DANG_RE = re.compile(r"当[^。；！？\n]{1,20}的时候")
DE_CHAIN_RE = re.compile(r"[%s]的[^。；！？\n]{0,12}的[^。；！？\n]{0,12}的" % HAN)
HAN_RE = re.compile(r"[%s]" % HAN)


def check_line(path, lineno, line, issues):
    text = MATH_RE.sub("\x00", line)
    text = CODE_SPAN_RE.sub("\x00", text)
    if text.lstrip().startswith("[^"):
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
            issues.append({"path": path, "line": lineno,
                           "rule": "passive-bei",
                           "detail": "单句 %d 个“被”：%s" % (sent.count("被"), excerpt)})
        if DE_CHAIN_RE.search(sent) or sent.count("的") >= 6:
            issues.append({"path": path, "line": lineno,
                           "rule": "de-chain",
                           "detail": "“的”连用或密度过高：%s" % excerpt})
        if WEAK_RE.search(sent):
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
