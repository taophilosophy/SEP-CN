# -*- coding: utf-8 -*-
r"""021 译文侧宏使用清点：区分
  (a) 可展开宏（在本词条 local.js 表内）——我们站点无宏表，须展开
  (b) 未知宏（既非 MathJax v3 标准、亦不在词条表）——真缺陷
  (c) 带参宏（值含 #1）——展开需按参数替换，单列
用法: python -I survey_macro_use.py [--detail]
输出 results/zh-macro-survey.json + stdout 汇总
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, '..', 'results')
sys.path.insert(0, HERE)
from align import load, strip_delims  # noqa: E402

MACRO_USE_RE = re.compile(r'\\([a-zA-Z]+)')
# MathJax v3 AllPackages 覆盖的常用宏（保守白名单，避免把标准宏当未知）
STANDARD = set('''alpha beta gamma delta epsilon varepsilon zeta eta theta
vartheta iota kappa lambda mu nu xi omicron pi rho varrho sigma varsigma tau
upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma
Upsilon Phi Psi Omega varGamma varDelta varTheta varLambda varXi varPi
varSigma varUpsilon varPhi varPsi varOmega
frac dfrac tfrac sqrt root text textbf textit textrm textsf texttt textnormal
mathrm mathbf mathit mathsf mathtt mathcal mathbb mathfrak mathscr
operatorname mbox hbox hfil hfill
le leq ge geq ne neq approx approxeq equiv sim simeq cong propto ll gg
prec precapprox succ succapprox subset subseteq supseteq supset sqsubset
sqsubseteq sqsupset sqsupseteq in notin ni owns cup cap setminus emptyset
varnothing forall exists nexists neg lnot land wedge lor vee to gets
rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow
Rightarrow Leftarrow leftrightarrows mapsto longrightarrow longleftarrow
longrightarrow Longleftrightarrow implies impliedby iff
langle rangle lceil rceil lfloor rfloor ldots cdots vdots ddots dots dotsc
dotsb dotsm dotsi dotso
sum prod coprod int iint iiint oint lim liminf limsup sup inf max min
arg argmax argmin det dim ker hom deg gcd exp log ln lg sin cos tan cot
sec csc arcsin arccos arctan sinh cosh tanh
times cdot ast star circ bullet div pm mp oplus ominus otimes oslash odot
bigcirc dagger ddagger amalg uplus sqcap sqcup
quad qquad enspace thinspace negthinspace hspace mathstrut phantom
left right big Big bigg Bigg bigl bigr Bigl Bigr middle
hat widehat bar overline vec overrightarrow dot ddot dddot tilde widetilde
underbrace overbrace underline overparen wideparen acute grave breve check
mathring
binom dbinom tbinom choose atop above over
partial nabla infty aleph beth gimel daleth hbar ell wp Re Im imath jmath
pmod bmod mod
begin end tag label nonumber notag
textstyle displaystyle scriptstyle scriptscriptstyle limits nolimits
not cancel bcancel xcancel
substack sideset Rule
Vert vert lVert rVert lvert rvert
backslash setminus smallsetminus
vdash dashv models vDash Vdash nvdash nvDash
Box Diamond square blacksquare triangledown triangle blur
unicode
stackrel stackrel overset underset
mathbbm boldsymbol bm
mathop mathbin mathrel mathopen mathclose mathpunct mathord mathinner
mathrm
complement surd
prime
flat natural sharp
aleph
checkmark
therefore because
colon
Phi
hslash
ell
mho
angle measuredangle sphericalangle
top bot
exists
forall
neg
imath
jmath
wp
Re
Im
aleph
infty
emptyset
varnothing
mapsto
longmapsto
hookrightarrow hookleftarrow
nearrow searrow swarrow nwarrow
rightsquigarrow leadsto
dashrightarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow
restriction
upharpoonright downharpoonright
lhook rhook
textperiodcentered
textbackslash
textbar
textless textgreater
textasciitilde
textasciicircum
textunderscore
textendash textemdash
textquoteleft textquoteright
textquotedblleft textquotedblright
ldots
cdots
vdots
ddots
'''.split())


def main():
    detail = '--detail' in sys.argv
    table = json.load(open(os.path.join(RESULTS, 'macro-table.json'),
                           encoding='utf-8'))
    seqs = load(os.path.join(RESULTS, 'render-zh.jsonl'))
    stats = collections.Counter()
    unknown = collections.Counter()
    unknown_files = collections.defaultdict(set)
    expand_use = collections.Counter()
    per_file = {}
    param_macros = collections.Counter()
    for slug, macros in table.items():
        for k, v in macros.items():
            if '#' in v:
                param_macros[(slug, k)] += 1
    for f, items in sorted(seqs.items()):
        base = os.path.basename(f)[:-3]
        slug = base.split('.')[0]
        macros = table.get(slug, {})
        used = collections.Counter()
        for kind, body in items:
            bare = strip_delims(kind, body)
            for m in MACRO_USE_RE.finditer(bare):
                name = m.group(1)
                if name in macros:
                    used[name] += 1
                    expand_use[name] += 1
                    stats['expandable'] += 1
                elif name in STANDARD:
                    stats['standard'] += 1
                else:
                    unknown[name] += 1
                    unknown_files[name].add(f)
                    stats['unknown'] += 1
        if used:
            per_file[f] = dict(used)
            stats['files_with_expandable'] += 1
    out = {'stats': dict(stats), 'expand_use': dict(expand_use),
           'unknown': {k: {'n': v, 'files': sorted(unknown_files[k])[:6]}
                       for k, v in unknown.most_common()},
           'per_file': per_file,
           'param_macros': [f'{s}:{k}' for s, k in param_macros][:20]}
    json.dump(out, open(os.path.join(RESULTS, 'zh-macro-survey.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False, indent=1))
    print('files needing expansion:', stats['files_with_expandable'])
    print('\n展开宏 top20:', dict(expand_use.most_common(20)))
    print('\n未知宏 top20:')
    for k, v in unknown.most_common(20):
        print(f'  {k:14s} {v:5d}  {sorted(unknown_files[k])[:3]}')
    print('\n带参宏样本:', out['param_macros'][:8])


if __name__ == '__main__':
    main()
