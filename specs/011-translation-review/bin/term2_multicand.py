# -*- coding: utf-8 -*-
"""specs/011：双词术语多候选异译搜索。

对裁定台剩余术语对，用学界通行候选异译批量搜 zh 正文：
  命中 → 异形译出（记录用形，登记册加亦作或保持）；
  全 miss → 真缺口（输出该词条 zh 长度与术语 EN 频次，供深查）。
"""
import io
import os
import re
import collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)

# 每对术语的候选异译（学界通行；首个=登记主形）
CAND = {
    "conditional analysis": ["条件句分析", "条件分析"],
    "specific ability": ["特殊能力", "特定能力"],
    "violinist case": ["小提琴家案例", "小提琴家思想实验", "小提琴家论证", "小提琴家例子"],
    "current self": ["当前自我", "现在的自我", "当下自我", "现在自我"],
    "earlier self": ["先前自我", "过去的自我", "以前自我", "较早自我"],
    "eternal truths": ["永恒真理", "永恒真理解"],
    "ontological commitments": ["本体论承诺", "存在论承诺", "本体论许诺"],
    "efference copy": ["传出副本", "传出复本", "运动副本", "输出副本"],
    "Sensus Communis": ["共同感", "通感", "感官共通感", "常识"],
    "aesthetic attitude": ["审美态度"],
    "tea ceremony": ["茶道", "茶道仪式", "茶之汤"],
    "moral justification": ["道德辩护", "道德证成", "道德正当化", "道德辩护"],
    "sense perception": ["感官知觉", "感觉知觉", "感性知觉"],
    "visual perception": ["视知觉", "视觉感知", "视觉知觉"],
    "mental states": ["心灵状态", "心理状态", "精神状态"],
    "practical reason": ["实践理性"],
    "human nature": ["人性"],
    "human action": ["人类行动", "人的行动", "人的行为"],
    "human agency": ["人类能动性", "人的能动性", "人的施动性"],
    "original position": ["原初状态", "原始状态", "原初立场", "原始地位"],
    "bona fide": ["真实的", "真正的", " bona fide"],
    "general ability": ["一般能力", "普遍能力"],
    "practical knowledge": ["实践知识", "实践之知"],
    "moral luck": ["道德运气"],
    "moral responsibility": ["道德责任"],
    "possible worlds": ["可能世界"],
    "intentional object": ["意向对象", "意向客体"],
    "mental content": ["心灵内容", "心理内容", "思想内容"],
    "moral status": ["道德地位"],
    "moral worth": ["道德价值", "道德 Worth"],
    "personal identity": ["人格同一性", "人格同一"],
    "principle of sufficient reason": ["充足理由律", "充足理由原则"],
    "state of nature": ["自然状态"],
    "civil society": ["市民社会", "公民社会"],
    "natural right": ["自然权利", "自然正当"],
    "natural law": ["自然法"],
    "sufficient reason": ["充足理由", "充分理由"],
    "early modern": ["近代早期", "早期近代", "近世", "近代早期"],
    "religious belief": ["宗教信念", "宗教信仰"],
    "moral psychology": ["道德心理学"],
    "moral realism": ["道德实在论"],
    "moral anti-realism": ["道德反实在论", "道德非实在论"],
    "ethical naturalism": ["伦理自然主义"],
    "ethical non-naturalism": ["伦理非自然主义"],
    "moral motivation": ["道德动机"],
    "moral judgment": ["道德判断"],
    "moral sentiment": ["道德情感", "道德感"],
    "common sense": ["常识"],
    "common sense philosophy": ["常识哲学"],
    "moral reasoning": ["道德推理"],
    "moral education": ["道德教育"],
    "moral character": ["道德品格", "道德品质"],
    "moral virtue": ["道德德性", "道德美德", "德性"],
    "intellectual virtue": ["理智德性", "理智美德"],
    "moral duty": ["道德义务", "道德责任"],
    "moral obligation": ["道德义务"],
    "moral permission": ["道德允许", "道德许可"],
    "moral requirement": ["道德要求"],
}


def body(p):
    t = io.open(p, encoding="utf-8").read()
    m = re.search(r"^#{1,3}\s*(?:参考文献|Bibliography|References|学术工具|如何引用|Related Entries|延伸阅读)", t, re.M)
    return t[:m.start()] if m else t


def main():
    rows = [l.rstrip("\n").split("\t") for l in
            io.open("specs/011-translation-review/results/term2-verdict.tsv", encoding="utf-8")]
    cache = {}
    res = collections.defaultdict(list)
    for slug, en, zhreg, _, _ in rows:
        cands = CAND.get(en)
        if not cands:
            res[("NOCAND", en, zhreg)].append(slug)
            continue
        if slug not in cache:
            cache[slug] = body(slug + ".md")
        zh = cache[slug]
        hit = [c for c in cands if c.strip() and c in zh]
        if hit:
            res[("HIT", en, zhreg)].append((slug, hit[0]))
        else:
            res[("MISS", en, zhreg)].append(slug)
    with io.open("specs/011-translation-review/results/term2-multicand.txt", "w", encoding="utf-8") as f:
        for (k, en, zhreg), v in sorted(res.items()):
            f.write("%s\t%s\t%s\t%s\n" % (k, en, zhreg, v))
    print("HIT(异形已译) %d 对 | MISS(真缺口) %d 对 | NOCAND %d 对" % (
        sum(1 for k in res if k[0] == "HIT"),
        sum(1 for k in res if k[0] == "MISS"),
        sum(1 for k in res if k[0] == "NOCAND")))


if __name__ == "__main__":
    main()
