# -*- coding: utf-8 -*-
"""mu-lu-s 分类目录：71 条 intake 新词条的语义归类插入（specs/007 移交闭环）。

锚定=现有行文本片段（唯一），继承锚行缩进；chained=插在前一条新行之后。
位置语义：after=锚行后插入；before=锚行前插入。幂等：已存在目标行则跳过。
"""
import io
import json
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MU = "mu-lu-s.md"

# slug → (锚文本片段, after|before)
PLAN = [
    ("abortion", "生物伦理理论 theory", "after"),
    ("bioethics-latin-america", "a/abortion.md", "after"),
    ("aesthetics-race", "日常美学", "after"),
    ("paradox-of-tragedy", "a/aesthetics-race.md", "after"),
    ("aesthetics-critical-theory", "黑格尔的美学", "after"),
    ("langer", "克罗齐的美学", "after"),
    ("landmann-kalischer", "18 世纪的德国美学", "after"),
    ("music", "西方音乐哲学史：自 1800 年以来", "after"),
    ("al-khunaji", "i/ibn-sina-logic.md", "after"),
    ("arabic-islamic-liar", "a/al-khunaji.md", "after"),
    ("al-qudat", "安萨里 al-Ghazali", "after"),
    ("ibn-taymiyya", "伊本·阿拉比", "after"),
    ("alberic-paris", "阿伯拉尔 Abelard", "after"),
    ("marsilius-padua", "威克里夫的政治哲学", "after"),
    ("john-italos", "拜占庭哲学 Byzantine", "after"),
    ("gianfrancesco-pico", "乔瓦尼·皮科·德拉·米兰多拉", "after"),
    ("cyrenaics", "伊壁鸠鲁 Epicurus", "before"),
    ("animal-communication", "c/cognition-animal.md", "after"),
    ("animal-social-cognition", "a/animal-communication.md", "after"),
    ("animal-thought", "a/animal-social-cognition.md", "after"),
    ("algorithmic-fairness", "e/ethics-ai.md", "after"),
    ("epistemology-ai", "a/artificial-intelligence.md", "after"),
    ("branching-time", "时间逻辑 temporal", "after"),
    ("capitalism", "社会主义 socialism", "after"),
    ("chinese-painting-calligraphy", "中国哲学与中医", "after"),
    ("descartes-ethics", "笛卡尔的观念论", "after"),
    ("clauberg", "d/descartes-ethics.md", "after"),
    ("common-ground-pragmatics", "语用学 pragmatics", "after"),
    ("cugoano", "自由主义 liberalism", "after"),
    ("dai-zhen", "清代哲学 Qing philosophy", "after"),
    ("dehumanization", "人性 human nature", "after"),
    ("disability-well-being", "残疾与医疗卫生配给", "after"),
    ("doxastic-voluntarism", "信念 belief (Eric Schwitzgebel)", "after"),
    ("engels", "分析马克思主义", "after"),
    ("existentialism-mexican", "存在主义 existentialism (Kevin Aho)", "after"),
    ("experimental-aesthetics", "实验哲学 experimental philosophy (Justin Sytsma", "after"),
    ("experimental-jurisprudence", "e/experimental-aesthetics.md", "after"),
    ("feminism-objectification", "分析女性主义 analytic philosophy (Ann Garry)", "after"),
    ("gauge-theories", "q/quantum-field-theory.md", "after"),
    ("george-eliot", "密尔", "after"),
    ("ideology", "法律与意识形态 and ideology", "after"),
    ("locke-on-medicine", "洛克的政治哲学", "after"),
    ("logic-preference", "偏好 preferences", "after"),
    ("logic-provability", "证明论的发展", "after"),
    ("mandeville", "亚当·斯密的伦理学", "after"),
    ("mathematical-practice", "m/mathematical-style.md", "after"),
    ("model-organisms", "i/information-biological.md", "after"),
    ("montessori-maria", "教育哲学 education", "after"),
    ("moral-demands-permissions", "超义务 supererogation", "after"),
    ("moral-learning", "道德心理学的经验主义研究", "after"),
    ("moral-responsibility-empirical", "道德责任 moral responsibility (Matthew Talbert)", "after"),
    ("nietzsche-aesthetics", "尼采的伦理与政治哲学", "after"),
    ("ontology-is", "i/information-biological.md", "after"),
    ("philanthropy", "利他主义 altruism (Richard Kraut)", "after"),
    ("prioritarianism", "平等主义 egalitarianism", "after"),
    ("psychotherapy", "精神病学哲学 psychiatry", "after"),
    ("rationalism-early-modern", "大陆理性主义 Continental Rationalism", "after"),
    ("ratnakirti", "印度佛教哲学中的心灵", "after"),
    ("srigupta", "r/ratnakirti.md", "after"),
    ("yogacara", "s/srigupta.md", "after"),
    ("sikh-philosophy", "y/yogacara.md", "after"),
    ("realism-about-metaphysics", "对形而上学实在论的挑战", "after"),
    ("religion-evolutionary", "文化演化 cultural", "after"),
    ("religious-commitment-reason", "宗教认识论 epistemology of", "after"),
    ("scientific-explanation-20th", "科学解释的因果方法", "after"),
    ("sign-language-semantics", "动态语义 dynamic", "after"),
    ("social-procedures", "社会选择理论 social choice", "after"),
    ("theodicies", "恶的问题 problem of", "after"),
    ("truth-primitivist", "真理 truth (Michael Glanzberg)", "after"),
    ("weighing-reasons", "行动的理由：正当性", "after"),
    ("wisdom-analytic", "智慧 wisdom (Sharon Ryan)", "after"),
]


def zh_line(slug, path):
    """从 SUMMARY.md 取新词条的显示行文本（与 intake 行一致）。"""
    for l in open("SUMMARY.md", encoding="utf-8"):
        if "](%s)" % path in l:
            return l.strip()
    raise SystemExit("SUMMARY 无该词条行: %s" % path)


def main():
    wanted = {}
    for slug, _, _ in PLAN:
        letter = slug[0]
        wanted[slug] = "%s/%s.md" % (letter, slug)

    lines = open(MU, encoding="utf-8").read().split("\n")
    existing = set()
    for i, l in enumerate(lines):
        for slug, path in wanted.items():
            if "](%s)" % path in l:
                existing.add(slug)
    done, skipped, failed = 0, [], []
    for slug, anchor_frag, pos in PLAN:
        path = wanted[slug]
        if slug in existing:
            skipped.append(slug)
            continue
        row = zh_line(slug, path)
        # 找锚行：片段必须在含 .md 的行中唯一命中
        cand = [i for i, l in enumerate(lines) if anchor_frag in l and ".md" in l]
        if not cand:
            failed.append((slug, "锚未找到: " + anchor_frag))
            continue
        if len(cand) > 1:
            failed.append((slug, "锚不唯一(%d): %s" % (len(cand), anchor_frag)))
            continue
        ai = cand[0]
        anchor_line = lines[ai]
        indent = anchor_line[: len(anchor_line) - len(anchor_line.lstrip())]
        new_row = indent + row
        if pos == "after":
            lines.insert(ai + 1, new_row)
        else:
            lines.insert(ai, new_row)
        done += 1
    with open(MU, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print(json.dumps({"inserted": done, "skipped_existing": skipped,
                      "failed": failed}, ensure_ascii=False, indent=1))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
