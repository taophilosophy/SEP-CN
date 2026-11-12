# -*- coding: utf-8 -*-
"""从 mapping.tsv 生成 mu-lu-s 预览稿（specs/016）。

只写 results/mu-lu-s.preview.md，不覆盖 mu-lu-s.md。
"""
import csv
import os
import re
from collections import OrderedDict
from importlib.util import spec_from_file_location, module_from_spec

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SRC = os.path.join(ROOT, 'mu-lu-s.md')
TSV = os.path.join(ROOT, 'specs', '016-mulu-history-recategorize', 'results', 'mapping.tsv')
OUT = os.path.join(ROOT, 'specs', '016-mulu-history-recategorize', 'results', 'mu-lu-s.preview.md')

ORDER = [
    'A11', 'A12', 'A13', 'A21', 'A22', 'A23', 'A24', 'A25',
    'A31', 'A32', 'A33', 'A34', 'A35', 'A9',
    'M11', 'M12', 'M13', 'M14', 'M21', 'M22', 'M31', 'M32', 'M33',
    'M41', 'M42', 'M51', 'M52', 'M65', 'M61', 'M62', 'M63', 'M64', 'M71', 'M72', 'M8', 'M9',
    'R1', 'R21', 'R22', 'R23', 'R3', 'R4',
    'N10', 'N11', 'N12', 'N13', 'N14', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26',
    'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N41', 'N42', 'N43', 'N44', 'N5',
    'C11', 'C12', 'C13', 'C21', 'C22', 'C23', 'C31', 'C32', 'C33', 'C34',
    'C41', 'C42', 'C43', 'C5', 'C61', 'C62', 'C71', 'C72', 'C73', 'C74', 'C75',
    'C81', 'C82', 'C83', 'C91', 'C92', 'C93', 'C94', 'C10', 'C11p',
    'C20', 'C201', 'C202', 'C203', 'C204', 'C205',
    'J1', 'J2', 'J3',
    'CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8', 'CH9',
    'IN1', 'IN2', 'IN3', 'IN4', 'IN5', 'IN6', 'IN7',
    'JP1', 'JP2', 'JP3', 'JP4',
    'KR1', 'KR2', 'KR3',
    'IS1', 'IS2', 'IS3', 'IS4',
    'AF1', 'AF2', 'AF3',
    'LA1', 'LA2',
]


def load_mapping():
    rows = list(csv.DictReader(open(TSV, encoding='utf-8'), delimiter='\t'))
    by_section = OrderedDict()
    for r in rows:
        by_section.setdefault(r['new_section'], []).append(r)
    return rows, by_section


def sort_key(r):
    try:
        return (int(r['sort_key']), r['title'])
    except ValueError:
        return (0, r['title'])


def build_path_map(lines):
    m = {}
    for ln in lines:
        mm = re.search(r'\[(.*?)\]\(([^)]*\.md)\)', ln)
        if mm:
            p = mm.group(2)
            m[p.split('/')[-1][:-3]] = p
    return m


def emit_section(out, path, rows, path_map, last):
    parts = path.split(' > ')
    # 只输出与上一节不同的层级
    common = 0
    while common < min(len(parts), len(last)) and parts[common] == last[common]:
        common += 1
    for i in range(common, len(parts)):
        out.append('#' * (i + 1) + ' ' + parts[i])
        out.append('')
    slugs = {r['slug'] for r in rows}
    roots = [r for r in rows if r['parent'] not in slugs]
    children = {}
    for r in rows:
        if r['parent'] in slugs:
            children.setdefault(r['parent'], []).append(r)
    roots.sort(key=sort_key)
    for r in roots:
        emit_entry(out, r, children, 0, path_map)
    out.append('')
    return parts



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
    'plato-cratylus': 10, 'plato-sophstate': 20.0, 'plato-metaphysics': 20.1,
    'plato-parmenides': 20.2, 'plato-theaetetus': 30, 'plato-timaeus': 40,
    'plato-ethics': 50.0, 'plato-ethics-politics': 50.1, 'plato-ethics-shorter': 50.2,
    'plato-friendship': 50.3, 'plato-laws': 60, 'plato-aesthetics': 70.0,
    'plato-rhetoric': 70.1, 'plato-myths': 80,
    'aristotle-categories': 10.0, 'aristotle-logic': 10.1,
    'aristotle-metaphysics': 20.0, 'aristotle-noncontradiction': 20.1,
    'aristotle-causality': 20.2, 'aristotle-natphil': 40.0,
    'aristotle-mathematics': 40.1, 'aristotle-biology': 40.2,
    'aristotle-psychology': 40.3, 'aristotle-de-motu': 40.4,
    'aristotle-ethics': 50, 'aristotle-politics': 60,
    'aristotle-rhetoric': 70.0, 'aristotle-aesthetics': 70.1,
    'aristotle-text': 90.0, 'aristotle-commentators': 90.1,
    'kant-development': 0.0, 'kant-leibniz': 0.1, 'kant-judgment': 10,
    'analytic-synthetic': 10.0, 'transcendental-arguments': 10.1,
    'kant-transcendental': 10.2, 'apriori': 10.3, 'innateness-history': 10.4,
    'kant-transcendental-idealism': 20.0, 'kant-metaphysics': 20.1,
    'kant-hume-causality': 20.2, 'kant-reason': 30.0, 'kant-conceptualism': 30.1,
    'kant-mathematics': 40.0, 'kant-science': 40.1, 'kant-spacetime': 40.2,
    'kant-mind': 40.3, 'kant-moral': 50.0, 'kant-hume-morality': 50.1,
    'kant-social-political': 60, 'kant-aesthetics': 70, 'kant-religion': 80,
    'descartes-works': 0, 'descartes-method': 10, 'descartes-modal': 20.0,
    'descartes-ontological': 20.1, 'descartes-ideas': 30.0,
    'descartes-epistemology': 30.1, 'descartes-mathematics': 40.0,
    'descartes-physics': 40.1, 'pineal-gland': 40.2, 'descartes-ethics': 50,
    'leibniz-exoteric': 0, 'leibniz-modal': 20.0, 'leibniz-causation': 20.1,
    'sufficient-reason': 20.2, 'leibniz-mind': 40.0, 'leibniz-physics': 40.1,
    'leibniz-ethics': 50, 'leibniz-evil': 80, 'leibniz-logic-influence': 90,
    'spinoza-attributes': 20.0, 'spinoza-modal': 20.1, 'spinoza-epistemology-mind': 30,
    'spinoza-physics': 40.0, 'spinoza-psychological': 40.1, 'spinoza-political': 60,
    'locke-personal-identity': 40.0, 'locke-philosophy-science': 40.1,
    'locke-on-medicine': 40.2, 'locke-moral': 50.0, 'locke-freedom': 50.1,
    'locke-political': 60, 'real-essence': 20,
    'hume-freewill': 20, 'hume-newton': 40, 'hume-moral': 50,
    'hume-aesthetics': 70, 'hume-religion': 80,
    'hobbes-science': 40, 'hobbes-moral': 50,
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


def esc_title(t):
    bs = chr(92)
    out = []
    for i, ch in enumerate(t):
        if ch in '[]' and (i == 0 or t[i - 1] != bs):
            out.append(bs + ch)
        else:
            out.append(ch)
    return ''.join(out)


def emit_entry(out, r, children, level, path_map):
    indent = '  ' * level
    path = path_map.get(r['slug'], f"{r['slug'][0]}/{r['slug']}.md")
    out.append(f"{indent}* [{esc_title(r['title'])}]({path})")
    kids = children.get(r['slug'], [])
    kids.sort(key=lambda c: (child_rank(c), sort_key(c)))
    for c in kids:
        emit_entry(out, c, children, level + 1, path_map)


def parse_original():
    lines = open(SRC, encoding='utf-8').read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith('# 前言'))
    about = next(i for i, l in enumerate(lines) if l.startswith('# 关于'))
    west = next(i for i, l in enumerate(lines) if l.startswith('# 西方哲学史'))
    theory = next(i for i, l in enumerate(lines) if l.startswith('# 哲学通论'))
    region = next((i for i, l in enumerate(lines) if l.startswith('# 区域哲学') or l.startswith('# 欧美以外哲学史')), theory)
    return lines, start, about, west, region, theory


def filter_theory(lines, theory_start, moved_slugs):
    block = lines[theory_start:]
    nodes = []
    for ln in block:
        m = re.match(r'^(#{1,3})\s+(.*)$', ln)
        if m:
            nodes.append(('h', len(m.group(1)), m.group(2).strip()))
            continue
        m = re.search(r'\[(.*?)\]\(([^)]*\.md)\)', ln)
        if m:
            slug = m.group(2).split('/')[-1][:-3]
            if slug in moved_slugs:
                continue
            nodes.append(('e', ln))
            continue
        if ln.strip():
            nodes.append(('t', ln))
        else:
            nodes.append(('b', ''))
    changed = True
    while changed:
        changed = False
        for i, n in enumerate(nodes):
            if n[0] != 'h':
                continue
            lvl = n[1]
            has_entry = False
            for j in range(i + 1, len(nodes)):
                if nodes[j][0] == 'h' and nodes[j][1] <= lvl:
                    break
                if nodes[j][0] == 'e':
                    has_entry = True
                    break
            if not has_entry:
                k = i + 1
                while k < len(nodes) and nodes[k][0] in ('t', 'b'):
                    k += 1
                del nodes[i:k]
                changed = True
                break
    out = []
    for n in nodes:
        if n[0] == 'h':
            out.append('#' * n[1] + ' ' + n[2])
        elif n[0] == 'b':
            out.append('')
        else:
            out.append(n[1])
    return out


def main():
    rows, by_section = load_mapping()
    lines, start, about, west, region, theory = parse_original()
    path_map = build_path_map(lines)
    moved = {r['slug'] for r in rows if not r['new_section'].startswith('哲学通论')}

    spec = spec_from_file_location('classify', os.path.join(os.path.dirname(__file__), 'classify.py'))
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)

    out = lines[:start]
    out += lines[start:west]
    last = []
    for key in ORDER:
        path = mod.S[key]
        sec_rows = by_section.get(path, [])
        if not sec_rows:
            continue
        last = emit_section(out, path, sec_rows, path_map, last)
    out += filter_theory(lines, theory, moved)
    open(OUT, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('out', OUT, 'lines', len(out))


if __name__ == '__main__':
    main()
