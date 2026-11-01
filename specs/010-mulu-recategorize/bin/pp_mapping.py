# -*- coding: utf-8 -*-
"""specs/010 PhilPapers 全量映射引擎。

第一版：节/子节级确定性映射 + 标题关键词细化，输出 TSV 与边界集（低置信条目清单）供人工逐条判定。
TSV 列：slug \t 中文标题 \t 现节路径 \t PP大类 \t PP子类 \t 来源 \t 备注
来源：auto-rule（规则命中）/ manual-pending（待人工）
"""
import io
import re
import os
from collections import OrderedDict

# PhilPapers 七大类
HW = 'History of Western Philosophy'
TR = 'Philosophical Traditions'
ME = 'Metaphysics and Epistemology'
VT = 'Value Theory'
SL = 'Science, Logic, and Mathematics'
PM = 'Philosophy, Misc'

# 西史断代 → (PP大类, PP子类)
WEST_MAP = [
    ('早期希腊哲学', HW, 'Ancient Greek and Roman Philosophy'),
    ('中期希腊哲学', HW, 'Ancient Greek and Roman Philosophy'),
    ('晚期希腊哲学', HW, 'Ancient Greek and Roman Philosophy'),
    ('教父哲学与早期经院哲学', HW, 'Medieval and Renaissance Philosophy'),
    ('中世纪哲学通论', HW, 'Medieval and Renaissance Philosophy'),
    ('经院哲学', HW, 'Medieval and Renaissance Philosophy'),
    ('文艺复兴与早期近代哲学', HW, 'Medieval and Renaissance Philosophy'),
    ('启蒙运动和早期现代哲学', HW, '17th/18th Century Philosophy'),
    ('近代女性哲学家', HW, '17th/18th Century Philosophy'),
    ('19 世纪西方哲学', HW, '19th Century Philosophy'),
    ('20 世纪西方哲学', HW, '20th Century Philosophy'),
    ('现代女性哲学家', HW, '20th Century Philosophy'),
    ('马克思主义与西方马克思主义', HW, '19th/20th Century Philosophy'),
]
# 区域哲学 → (PP大类, PP子类)
REGION_MAP = [
    ('中国哲学', TR, 'Asian Philosophy'),
    ('印度哲学', TR, 'Asian Philosophy'),
    ('日本哲学', TR, 'Asian Philosophy'),
    ('韩国哲学', TR, 'Asian Philosophy'),
    ('犹太哲学', TR, 'Philosophical Traditions, Miscellaneous'),
    ('伊斯兰哲学', TR, 'Philosophical Traditions, Miscellaneous'),
    ('非洲哲学', TR, 'African/Africana Philosophy'),
    ('非裔哲学', TR, 'African/Africana Philosophy'),
    ('拉丁美洲哲学', TR, 'Philosophy of the Americas'),
    ('欧洲哲学', TR, 'European Philosophy'),
]
# 通论 ## 学科 → (PP大类, PP子类)（默认值；### 子节/标题关键词可细化）
TONG_MAP = [
    ('语言哲学与逻辑学', SL, 'Logic and Philosophy of Logic'),
    ('法哲学', VT, 'Philosophy of Law'),
    ('认识论', ME, 'Epistemology'),
    ('形而上学', ME, 'Metaphysics'),
    ('教育哲学', PM, 'Philosophy, Miscellaneous'),
    ('心理学与心灵哲学', ME, 'Philosophy of Mind'),
    ('社会学哲学', SL, 'Philosophy of Social Science'),
    ('文化哲学', PM, 'Philosophy, Miscellaneous'),
    ('经济哲学', SL, 'Philosophy of Social Science'),
    ('决策理论', ME, 'M&E, Miscellaneous'),
    ('博弈论', ME, 'M&E, Miscellaneous'),
    ('科学哲学', SL, 'General Philosophy of Science'),
    ('神学与宗教哲学', ME, 'Philosophy of Religion'),
    ('伦理学（道德哲学）', VT, 'Normative Ethics'),
    ('女性哲学与性哲学相关', VT, 'Philosophy of Gender, Race, and Sexuality'),
    ('美学', VT, 'Aesthetics'),
    ('政治哲学', VT, 'Social and Political Philosophy'),
    ('出生哲学与死亡哲学', PM, 'Philosophy, Miscellaneous'),
]
# ### 子节级细化（节内 ### 标题前缀 → 子类覆盖）
SUB_MAP = [
    # 语言哲学与逻辑学
    ('语言哲学与逻辑学', '逻辑学家', SL, 'Logic and Philosophy of Logic', '人物'),
    ('语言哲学与逻辑学', '逻辑史', SL, 'Logic and Philosophy of Logic', 'history'),
    ('语言哲学与逻辑学', '语义学', ME, 'Philosophy of Language', ''),
    ('语言哲学与逻辑学', '语用学', ME, 'Philosophy of Language', ''),
    ('语言哲学与逻辑学', '经典逻辑', SL, 'Logic and Philosophy of Logic', ''),
    ('语言哲学与逻辑学', '非经典逻辑', SL, 'Logic and Philosophy of Logic', ''),
    ('语言哲学与逻辑学', '形式逻辑', SL, 'Logic and Philosophy of Logic', ''),
    # 科学哲学子节
    ('科学哲学', '物理学哲学', SL, 'Philosophy of Physical Science', ''),
    ('科学哲学', '化学哲学', SL, 'Philosophy of Physical Science', 'chemistry'),
    ('科学哲学', '数学哲学', SL, 'Philosophy of Mathematics', ''),
    ('科学哲学', '生命科学哲学', SL, 'Philosophy of Biology', ''),
    ('科学哲学', '医学', VT, 'Applied Ethics', 'medical ethics'),
    ('科学哲学', '技术哲学', SL, 'General Philosophy of Science', 'technology'),
    ('科学哲学', '信息和数字文化哲学', SL, 'Philosophy of Computing and Information', ''),
    ('科学哲学', '认知神经哲学', SL, 'Philosophy of Cognitive Science', ''),
    ('科学哲学', '科学方法论', SL, 'General Philosophy of Science', ''),
    ('科学哲学', '科学认识论', ME, 'Epistemology', 'social epistemology of science'),
    ('科学哲学', '科学实在论', SL, 'General Philosophy of Science', 'realism'),
    ('科学哲学', '混沌理论', SL, 'Philosophy of Physical Science', ''),
    ('科学哲学', '因果推理', ME, 'Metaphysics', 'causation'),
    # 心灵哲学子节
    ('心理学与心灵哲学', '认知科学', SL, 'Philosophy of Cognitive Science', ''),
    ('心理学与心灵哲学', '情感哲学', ME, 'Philosophy of Mind', 'emotion'),
    ('心理学与心灵哲学', '知觉', ME, 'Philosophy of Mind', 'perception'),
    # 伦理学子节
    ('伦理学（道德哲学）', '元伦理学', VT, 'Meta-Ethics', ''),
    ('伦理学（道德哲学）', '行动哲学与理由论', ME, 'Philosophy of Action', ''),
    ('伦理学（道德哲学）', '社会正义', VT, 'Social and Political Philosophy', ''),
    ('伦理学（道德哲学）', '人权', VT, 'Social and Political Philosophy', 'human rights'),
    ('伦理学（道德哲学）', '应用伦理学', VT, 'Applied Ethics', ''),
    ('伦理学（道德哲学）', '社会伦理学', VT, 'Normative Ethics', 'social ethics'),
    ('伦理学（道德哲学）', '道德心理学', VT, 'Normative Ethics', 'moral psychology'),
    ('伦理学（道德哲学）', '伦理学理论与伦理学家', VT, 'Normative Ethics', '人物'),
    # 神学与宗教哲学子节
    ('神学与宗教哲学', '佛教（印度佛教）', TR, 'Asian Philosophy', 'Buddhist'),
    ('神学与宗教哲学', '基督教', ME, 'Philosophy of Religion', 'Christian'),
    # 美学
    ('美学', '美学史', VT, 'Aesthetics', 'history'),
    ('美学', '艺术哲学', VT, 'Aesthetics', 'art'),
    # 政治哲学
    ('政治哲学', '政治哲学史', VT, 'Social and Political Philosophy', 'history'),
    ('政治哲学', '种族哲学', VT, 'Philosophy of Gender, Race, and Sexuality', 'race'),
    # 形而上学
    ('形而上学', '自由意志', ME, 'Metaphysics', 'free will'),
    ('形而上学', '因果关系', ME, 'Metaphysics', 'causation'),
    ('形而上学', '模态实在论', ME, 'Metaphysics', 'modality'),
    ('形而上学', '时间与空间哲学', ME, 'Metaphysics', 'time and space'),
    ('形而上学', '本体论', ME, 'Metaphysics', 'ontology'),
    ('形而上学', '哲学中的神秘传统', ME, 'Philosophy of Religion', 'mysticism'),
    # 女性哲学
    ('女性哲学与性哲学相关', '性哲学', VT, 'Philosophy of Gender, Race, and Sexuality', 'sex'),
    ('女性哲学与性哲学相关', '性别与酷儿哲学', VT, 'Philosophy of Gender, Race, and Sexuality', 'gender/queer'),
    ('女性哲学与性哲学相关', '女性主义哲学', VT, 'Philosophy of Gender, Race, and Sexuality', 'feminist'),
]
# 标题关键词覆盖（在节默认与子节规则之后兜底细化）
KW_MAP = [
    ('民主', VT, 'Social and Political Philosophy'),
    ('自由主义', VT, 'Social and Political Philosophy'),
    ('正义', VT, 'Social and Political Philosophy'),
    ('权利', VT, 'Social and Political Philosophy'),
    ('女', VT, 'Philosophy of Gender, Race, and Sexuality'),
    ('性别', VT, 'Philosophy of Gender, Race, and Sexuality'),
    ('酷儿', VT, 'Philosophy of Gender, Race, and Sexuality'),
    ('伦理', VT, 'Normative Ethics'),
    ('道德', VT, 'Normative Ethics'),
    ('德性', VT, 'Normative Ethics'),
    ('存在主义', HW, '20th Century Philosophy'),
    ('现象学', HW, '20th Century Philosophy'),
    ('诠释', HW, '20th Century Philosophy'),
    ('结构主义', HW, '20th Century Philosophy'),
    ('法兰克福', HW, '20th Century Philosophy'),
    ('批判理论', HW, '20th Century Philosophy'),
    ('物理', SL, 'Philosophy of Physical Science'),
    ('量子', SL, 'Philosophy of Physical Science'),
    ('宇宙', SL, 'Philosophy of Physical Science'),
    ('时间', ME, 'Metaphysics'),
    ('空间', ME, 'Metaphysics'),
    ('数学', SL, 'Philosophy of Mathematics'),
    ('逻辑', SL, 'Logic and Philosophy of Logic'),
    ('语言', ME, 'Philosophy of Language'),
    ('意义', ME, 'Philosophy of Language'),
    ('真理', ME, 'Metaphysics'),
    ('心灵', ME, 'Philosophy of Mind'),
    ('意识', ME, 'Philosophy of Mind'),
    ('认知', SL, 'Philosophy of Cognitive Science'),
    ('知识', ME, 'Epistemology'),
    ('怀疑', ME, 'Epistemology'),
    ('证据', ME, 'Epistemology'),
    ('信念', ME, 'Epistemology'),
    ('宗教', ME, 'Philosophy of Religion'),
    ('神学', ME, 'Philosophy of Religion'),
    ('上帝', ME, 'Philosophy of Religion'),
    ('艺术', VT, 'Aesthetics'),
    ('美', VT, 'Aesthetics'),
    ('文学', VT, 'Aesthetics'),
    ('电影', VT, 'Aesthetics'),
    ('音乐', VT, 'Aesthetics'),
    ('法律', VT, 'Philosophy of Law'),
    ('法哲学', VT, 'Philosophy of Law'),
    ('惩罚', VT, 'Philosophy of Law'),
    ('政治', VT, 'Social and Political Philosophy'),
    ('国家', VT, 'Social and Political Philosophy'),
    ('战争', VT, 'Social and Political Philosophy'),
    ('和平', VT, 'Social and Political Philosophy'),
    ('殖民', VT, 'Social and Political Philosophy'),
    ('移民', VT, 'Social and Political Philosophy'),
    ('全球', VT, 'Social and Political Philosophy'),
    ('经济', SL, 'Philosophy of Social Science'),
    ('社会', SL, 'Philosophy of Social Science'),
    ('生物', SL, 'Philosophy of Biology'),
    ('进化', SL, 'Philosophy of Biology'),
    ('遗传', SL, 'Philosophy of Biology'),
    ('生态', SL, 'Philosophy of Biology'),
    ('环境', VT, 'Applied Ethics', 'environmental'),
    ('动物', VT, 'Applied Ethics', 'animal ethics'),
    ('食品', VT, 'Applied Ethics', 'food'),
    ('死亡', PM, 'Philosophy, Miscellaneous'),
    ('生育', VT, 'Applied Ethics', 'reproductive ethics'),
    ('生命', PM, 'Philosophy, Miscellaneous'),
    ('决策', ME, 'M&E, Miscellaneous'),
    ('博弈', ME, 'M&E, Miscellaneous'),
    ('理性', ME, 'Epistemology', 'rationality'),
    ('行动', ME, 'Philosophy of Action'),
    ('能动', ME, 'Philosophy of Action'),
    ('情感', ME, 'Philosophy of Mind'),
    ('爱', ME, 'Philosophy of Mind', 'love/emotion'),
    ('幸福', VT, 'Normative Ethics', 'well-being'),
    ('福祉', VT, 'Normative Ethics', 'well-being'),
    ('教育', PM, 'Philosophy, Miscellaneous'),
    ('记忆', ME, 'Epistemology', 'memory'),
    ('因果', ME, 'Metaphysics', 'causation'),
    ('可能性', ME, 'Metaphysics', 'modality'),
    ('同一', ME, 'Metaphysics', 'identity'),
    ('个人同一', ME, 'Metaphysics', 'personal identity'),
    ('虚无', ME, 'Metaphysics', 'nothingness'),
    ('无穷', SL, 'Philosophy of Mathematics', 'infinity'),
    ('悖论', SL, 'Logic and Philosophy of Logic', 'paradox'),
]


def resolve(h1, h2, h3, title):
    """返回 (大类, 子类, 来源, 备注)。h3 可为 None。"""
    # 子节级
    for sec, sub, cat, sub2, note in SUB_MAP:
        if (h2 or '').startswith(sec) and h3 and h3.startswith(sub):
            return cat, sub2, 'auto-rule', note
    # 区级
    for prefix, cat, sub2 in WEST_MAP:
        if (h2 or '').startswith(prefix):
            return cat, sub2, 'auto-rule', ''
    for prefix, cat, sub2 in REGION_MAP:
        if (h2 or '').startswith(prefix):
            return cat, sub2, 'auto-rule', ''
    for prefix, cat, sub2 in TONG_MAP:
        if (h2 or '').startswith(prefix):
            # 标题关键词兜底细化——仅在同一 PP 大类内部生效，跨大类一律守节上下文
            # （节上下文优先：如法哲学节的"证据的法律概念"守 Philosophy of Law，
            #   不因"证据"关键词被拽到 Epistemology；美学节的"悲剧悖论"守 Aesthetics）
            for kw, cat2, sub3, *rest in KW_MAP:
                if kw in title and cat2 == cat:
                    return cat2, sub3, 'auto-kw', (rest[0] if rest else '')
            return cat, sub2, 'auto-rule', ''
    return None, None, 'manual-pending', ''


def main():
    lines = io.open('mu-lu-s.md', encoding='utf-8').read().split('\n')
    h1 = h2 = h3 = None
    rows = []
    pending = 0
    for ln in lines:
        if ln.startswith('# ') and not ln.startswith('## '):
            h1, h2, h3 = ln[2:].strip(), None, None
        elif ln.startswith('## '):
            h2, h3 = ln[3:].strip(), None
        elif ln.startswith('### '):
            h3 = ln[4:].strip()
        m = re.match(r'^(\s*)\* \[((?:\\.|[^\]])*)\]\(([a-zA-Z0-9._/\-]+\.md)\)(.*)$', ln)
        if m:
            slug = m.group(3).split('/')[-1][:-3]
            title = m.group(2)
            if h1 in ('前言', '关于'):
                rows.append((slug, title, '%s>%s>%s' % (h1 or '', h2 or '', h3 or ''),
                             'nav', '站点导航', 'auto-rule', '非词条'))
                continue
            cat, sub, src, note = resolve(h1, h2, h3, title)
            if cat is None:
                pending += 1
                rows.append((slug, title, '%s>%s>%s' % (h1 or '', h2 or '', h3 or ''),
                             '', '', 'manual-pending', ''))
            else:
                rows.append((slug, title, '%s>%s>%s' % (h1 or '', h2 or '', h3 or ''),
                             cat, sub, src, note))
    os.makedirs('specs/010-mulu-recategorize/results', exist_ok=True)
    with io.open('specs/010-mulu-recategorize/results/philpapers-mapping.tsv', 'w',
                 encoding='utf-8', newline='\n') as f:
        f.write('slug\t标题\t现节\tPP大类\tPP子类\t来源\t备注\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print('总条目:', len(rows), ' 自动映射:', len(rows) - pending, ' 待人工:', pending)
    # 待人工分布
    from collections import Counter
    c = Counter(r[2].split('>')[1] if r[2].split('>')[1] else r[2].split('>')[0]
                for r in rows if r[5] == 'manual-pending')
    for k, v in c.most_common(20):
        print('  待人工 %4d  %s' % (v, k))


if __name__ == '__main__':
    main()
