# -*- coding: utf-8 -*-
"""71 条上游增量 intake 驱动器（specs/001 upstream-increment，用户 2026-10-28 指令"进行补遗"）。

按 catalog-verdict.json add 清单顺序逐条执行 summary_sync.py apply-add
（译名裁定见 TITLES 映射，执行日志 specs/001-sep-sync-pipeline/intake-log.jsonl）。
apply-add 闭环：SUMMARY 插入 + 建桩 + baseline.zh_doc + yuanwen 转换。
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

TITLES = {
    "abortion": "堕胎的伦理学",
    "aesthetics-critical-theory": "批判理论中的美学",
    "aesthetics-race": "美学与种族",
    "al-khunaji": "阿夫扎勒丁·胡纳吉",
    "al-qudat": "艾因·古达特",
    "alberic-paris": "巴黎的阿尔贝里克",
    "algorithmic-fairness": "算法公平",
    "animal-communication": "动物交流",
    "animal-social-cognition": "动物社会认知",
    "animal-thought": "动物思维",
    "arabic-islamic-liar": "阿拉伯与伊斯兰哲学中的说谎者悖论",
    "bioethics-latin-america": "拉丁美洲的生命伦理学",
    "branching-time": "分支时间",
    "capitalism": "资本主义",
    "chinese-painting-calligraphy": "中国哲学中的美学：绘画与书法",
    "clauberg": "约翰内斯·克劳伯格",
    "common-ground-pragmatics": "语用学中的共同基础",
    "cugoano": "奥托巴·库加诺",
    "cyrenaics": "昔勒尼学派",
    "dai-zhen": "戴震",
    "dehumanization": "非人化",
    "descartes-ethics": "笛卡尔的伦理学",
    "disability-well-being": "残疾与福祉",
    "doxastic-voluntarism": "信念自愿论",
    "engels": "弗里德里希·恩格斯",
    "epistemology-ai": "人工智能认识论",
    "existentialism-mexican": "墨西哥存在主义",
    "experimental-aesthetics": "艺术与美学的实验哲学",
    "experimental-jurisprudence": "实验法理学",
    "feminism-objectification": "女性主义视角下的物化",
    "gauge-theories": "物理学中的规范理论",
    "george-eliot": "乔治·艾略特",
    "gianfrancesco-pico": "乔瓦尼·弗朗切斯科·皮科·德拉·米兰多拉",
    "ibn-taymiyya": "伊本·泰米叶",
    "ideology": "意识形态",
    "john-italos": "约翰·伊塔洛斯",
    "landmann-kalischer": "伊迪丝·兰德曼-卡利舍尔",
    "langer": "苏珊·朗格",
    "locke-on-medicine": "洛克论医学",
    "logic-preference": "偏好逻辑",
    "logic-provability": "可证性逻辑",
    "mandeville": "伯纳德·曼德维尔",
    "marsilius-padua": "帕多瓦的马西利乌斯",
    "mathematical-practice": "数学实践的哲学",
    "model-organisms": "模式生物",
    "montessori-maria": "玛丽亚·蒙台梭利",
    "moral-demands-permissions": "道德要求与许可/特权",
    "moral-learning": "道德学习",
    "moral-responsibility-empirical": "道德责任的实证进路",
    "music": "音乐哲学",
    "nietzsche-aesthetics": "尼采的美学",
    "ontology-is": "本体论与信息系统",
    "paradox-of-tragedy": "悲剧悖论",
    "philanthropy": "慈善",
    "prioritarianism": "作为价值理论的优先主义",
    "psychotherapy": "心理治疗的哲学",
    "rationalism-early-modern": "早期近代理性主义",
    "ratnakirti": "宝称",
    "realism-about-metaphysics": "形而上学的实在论与反实在论",
    "religion-evolutionary": "宗教的演化论进路",
    "religious-commitment-reason": "理性与宗教承诺",
    "scientific-explanation-20th": "20 世纪的科学解释理论",
    "sign-language-semantics": "手语语义学",
    "sikh-philosophy": "锡克哲学",
    "social-procedures": "社会程序的形式化进路",
    "srigupta": "室利笈多",
    "theodicies": "神义论",
    "truth-primitivist": "真理的原始主义理论",
    "weighing-reasons": "权衡理由",
    "wisdom-analytic": "当代分析哲学中的智慧",
    "yogacara": "瑜伽行派",
}


def main():
    v = json.load(open("specs/001-sep-sync-pipeline/catalog-verdict.json", encoding="utf-8"))
    slugs = [a["slug"] for a in v["add"]]
    missing = [s for s in slugs if s not in TITLES]
    if missing:
        print(json.dumps({"error": "缺译名裁定", "missing": missing}, ensure_ascii=False))
        return 2
    log_path = "specs/001-sep-sync-pipeline/intake-log.jsonl"
    ok, fail = 0, []
    with open(log_path, "a", encoding="utf-8", newline="\n") as log:
        for i, slug in enumerate(slugs, 1):
            p = subprocess.run([sys.executable, "tools/summary_sync.py", "apply-add",
                                slug, "--title-zh", TITLES[slug]],
                               capture_output=True, timeout=300)
            out = p.stdout.decode("utf-8", "replace").strip()
            err = p.stderr.decode("utf-8", "replace")[-300:]
            rec = {"idx": i, "slug": slug, "title_zh": TITLES[slug], "exit": p.returncode}
            try:
                rec["out"] = json.loads(out)
            except json.JSONDecodeError:
                rec["raw_out"] = out[:300]
            if p.returncode != 0:
                rec["err"] = err
                fail.append(slug)
            else:
                ok += 1
            log.write(json.dumps(rec, ensure_ascii=False) + "\n")
            log.flush()
            sys.stderr.write("[%d/%d] %s: exit=%s\n" % (i, len(slugs), slug, p.returncode))
            sys.stderr.flush()
    print(json.dumps({"added": ok, "failed": fail, "total": len(slugs)}, ensure_ascii=False))
    return 0 if not fail else 1


if __name__ == "__main__":
    if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.exit(main())
