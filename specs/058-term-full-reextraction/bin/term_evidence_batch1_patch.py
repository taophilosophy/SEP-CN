# -*- coding: utf-8 -*-
"""批次 1（50 行薄依据）审定库核证落地：6 行补审定凭证、4 行记异形/异义不改。"""
import io, sys
sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, term_path

TSV = 'termonline-b1-2026-11-24.tsv'
p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and c[0]:
            idx.setdefault(norm_key_quote(c[0]), i)

ADD = [
 ('absolutism', '审定名词库（termonline-all·自然辩证法名词 03.139，2024）作“绝对主义”，与本行一致（2026-11-24 JWT 直连，凭证 %s）' % TSV),
 ('action at a distance', '审定名词库（termonline-all·自然辩证法名词 03.399，2024，物理学哲学）作“超距作用”，与本行一致（2026-11-24 JWT 直连，凭证 %s）' % TSV),
 ('algebraic semantics', '审定名词库（termonline-all·计算机科学技术名词 02.0875，2018，程序理论）作“代数语义”，与本行一致（2026-11-24 JWT 直连，凭证 %s）' % TSV),
 ('alternating Turing machine', '审定名词库（termonline-all·计算机科学技术名词 02.0332，2018，可计算性与计算复杂性）作“交替图灵机”，与本行一致（2026-11-24 JWT 直连，凭证 %s）' % TSV),
 ('anaphora', '审定名词库（termonline-all·语言学名词 01.147，2011，理论语言学核心术语）作“回指”，与本行一致（2026-11-24 JWT 直连，凭证 %s）' % TSV),
 ('anorexia nervosa', '审定名词库（termonline-all·行为医学名词 16.192，2022；消化病学名词 1.08，2022）作“神经性厌食”，亦作“神经性厌食[症]”，与本行一致（2026-11-24 JWT 直连，凭证 %s）' % TSV),
]
NOTE = [
 ('ad hoc', '审定库仅收下位“ad hoc hypothesis 特设性假说”（自然辩证法名词 06.191，2024），非本词条；现行“特设性的”不改'),
 ('agreeableness', '审定库（海峡两岸心理学名词，2016）作“亲和性”，系对照库非审定公布库，且与大陆大五人格通行“宜人性”不合；现行译法保留'),
 ('antecedent/consequent', '审定库数学名词作“前项／后项”（04.0072／04.0073，1993），属代数几何异义；逻辑学“前件／后件”不改'),
 ('accuracy/adroitness/aptness', '审定库“accuracy＝准确度”属农学、兽医、地球物理异域同形；索萨 AAA 术语不改'),
]
n = 0
for key, note in ADD + [(k, '（2026-11-24 复核）' + v) for k, v in NOTE]:
    i = idx[norm_key_quote(key)]
    c = [x.strip() for x in lines[i].strip().strip('|').split('|')]
    if note not in c[4]:
        c[4] = c[4].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(c) + ' |'
    print('补', key); n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patched=%d' % n)
