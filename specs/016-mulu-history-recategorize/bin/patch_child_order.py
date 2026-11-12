# -*- coding: utf-8 -*-
"""一次性补丁：为 generate.py 增加人物子条目哲学体例排序。"""
import os

P = os.path.join(os.path.dirname(__file__), 'generate.py')
s = open(P, encoding='utf-8').read()

INSERT = '''
# 人物子条目的哲学体例排序：生平/总论 → 逻辑/方法 → 形而上学 → 认识论
# → 自然哲学/心灵 → 伦理学 → 政治哲学 → 美学 → 宗教哲学 → 文本/评注/影响
RANK_RULES = [
    (0, ['生平', '著作', '思想发展', '发展历程', '导论', '总论', '概述', 'life and works', 'development', 'introduction']),
    (10, ['逻辑', '方法论', '方法', '判断', '辩证法', '分析', '论证', '范畴', '命题', '语言', '克拉底鲁', 'logic', 'method', 'judgment', 'dialectic', 'categor', 'language']),
    (20, ['形而上学', '本体论', '存在', '实体', '模态', '可能世界', '因果', '矛盾律', '巴门尼德', '智者篇', 'metaphysics', 'ontology', 'substance', 'modal', 'caus', 'non-contradiction']),
    (30, ['认识论', '知识', '观念', '真理', '怀疑', '理性', '先验', '直观', '经验', '泰阿泰德', 'epistemolog', 'knowledge', 'idea', 'truth', 'skeptic', 'reason', 'transcendental']),
    (40, ['自然哲学', '物理学', '数学', '生物学', '心理学', '心灵', '意识', '知觉', '感觉', '空间', '时间', '运动', '动物', '蒂迈欧', 'natural philosophy', 'physics', 'mathematic', 'biolog', 'psycholog', 'mind', 'conscious', 'perception', 'space', 'time', 'motion', 'animal']),
    (50, ['伦理学', '道德', '德性', '义务', '功利', '善', '恶', '友爱', '理想国', 'ethics', 'moral', 'virtue', 'duty', 'utilitarian', 'good', 'evil', 'friendship']),
    (60, ['政治', '法', '社会', '正义', '自由', '权利', '法律篇', 'political', 'law', 'social', 'justice', 'liberty', 'right']),
    (70, ['美学', '艺术', '美', '崇高', '诗歌', '修辞', 'aesthetic', 'art', 'beauty', 'sublime', 'poetry', 'rhetoric']),
    (80, ['宗教', '神学', '信仰', '上帝', '启示', '秘所思', 'religion', 'theolog', 'faith', 'god', 'revelation', 'myth']),
    (90, ['文本', '传承', '评注', '解释', '影响', '接受', 'text', 'transmission', 'commentar', 'interpret', 'influence', 'reception']),
]

SPECIFIC = {
    'plato-cratylus': 10, 'plato-sophstate': 20, 'plato-metaphysics': 20,
    'plato-parmenides': 20, 'plato-theaetetus': 30, 'plato-timaeus': 40,
    'plato-ethics': 50, 'plato-ethics-politics': 50, 'plato-friendship': 50,
    'plato-ethics-shorter': 50, 'plato-laws': 60, 'plato-rhetoric': 70,
    'plato-aesthetics': 70, 'plato-myths': 80,
    'aristotle-logic': 10, 'aristotle-categories': 10, 'aristotle-metaphysics': 20,
    'aristotle-noncontradiction': 20, 'aristotle-causality': 20,
    'aristotle-natphil': 40, 'aristotle-biology': 40, 'aristotle-psychology': 40,
    'aristotle-de-motu': 40, 'aristotle-mathematics': 40, 'aristotle-ethics': 50,
    'aristotle-politics': 60, 'aristotle-rhetoric': 70, 'aristotle-aesthetics': 70,
    'aristotle-text': 90, 'aristotle-commentators': 90,
    'kant-leibniz': 0, 'kant-development': 0, 'kant-judgment': 10,
    'kant-transcendental-idealism': 20, 'kant-metaphysics': 20,
    'kant-hume-causality': 20, 'kant-reason': 30, 'kant-conceptualism': 30,
    'kant-mathematics': 40, 'kant-science': 40, 'kant-spacetime': 40,
    'kant-mind': 40, 'kant-hume-morality': 50, 'kant-moral': 50,
    'kant-social-political': 60, 'kant-aesthetics': 70, 'kant-religion': 80,
    'descartes-works': 0, 'descartes-method': 10, 'descartes-modal': 20,
    'descartes-ontological': 20, 'descartes-ideas': 30,
    'descartes-epistemology': 30, 'descartes-mathematics': 40,
    'descartes-physics': 40, 'pineal-gland': 40, 'descartes-ethics': 50,
    'leibniz-exoteric': 0, 'leibniz-modal': 20, 'leibniz-causation': 20,
    'sufficient-reason': 20, 'leibniz-mind': 40, 'leibniz-physics': 40,
    'leibniz-ethics': 50, 'leibniz-evil': 80, 'leibniz-logic-influence': 90,
    'spinoza-attributes': 20, 'spinoza-modal': 20, 'spinoza-epistemology-mind': 30,
    'spinoza-physics': 40, 'spinoza-psychological': 40, 'spinoza-political': 60,
    'locke-moral': 50, 'locke-freedom': 50, 'locke-personal-identity': 40,
    'locke-philosophy-science': 40, 'locke-on-medicine': 40, 'locke-political': 60,
    'real-essence': 20, 'hume-newton': 40, 'hume-freewill': 20,
    'hume-religion': 80, 'hume-aesthetics': 70, 'hume-moral': 50,
    'hobbes-moral': 50, 'hobbes-science': 40,
}


def child_rank(r):
    if r['slug'] in SPECIFIC:
        return SPECIFIC[r['slug']]
    t = r['title'].lower()
    for rank, keys in RANK_RULES:
        for k in keys:
            if k in t:
                return rank
    return 90
'''

s = s.replace('def esc_title(t):', INSERT + '\n\ndef esc_title(t):')
s = s.replace(
    "    for c in children.get(r['slug'], []):\n        emit_entry(out, c, children, level + 1, path_map)",
    "    kids = children.get(r['slug'], [])\n    kids.sort(key=lambda c: (child_rank(c), sort_key(c)))\n    for c in kids:\n        emit_entry(out, c, children, level + 1, path_map)")
open(P, 'w', encoding='utf-8').write(s)
print('patched')
