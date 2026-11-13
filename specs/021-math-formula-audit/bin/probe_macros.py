# -*- coding: utf-8 -*-
r"""019 探针：统计译文公式中使用的宏名（含 SEP 全站自定义宏候选）。"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, '..', 'results')
MACRO_RE = re.compile(r'\\([a-zA-Z]+)')
# TeX 原语与 AllPackages 已覆盖的常见宏（仅作对照样本，不穷举）
KNOWN = set('''alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta
iota kappa lambda mu nu xi pi rho sigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
frac sqrt text textbf textit textrm mathrm mathbf mathit mathsf mathtt
mathrm mathbb mathcal mathfrak mathscr operatorname mbox hbox
le ge ne approx equiv sim simeq cong propto ll gg prec succ subset supset
subseteq supseteq in notin ni cup cap setminus emptyset forall exists neg
land lor lnot to rightarrow leftarrow leftrightarrow Rightarrow Leftarrow
Leftrightarrow mapsto implies iff sim leftrightarrow longrightarrow
langle rangle lceil rceil lfloor rfloor ldots cdots vdots ddots dots
sum prod int oint lim inf sup max min
times cdot ast star circ bullet div pm mp oplus otimes odot
quad qquad , ; : ! ~ space
left right big Big bigg Bigg middle
hat bar vec dot ddot tilde widehat overline underline
binom choose atop over
partial nabla infty aleph hbar ell wp Re Im
pmod bmod mod
begin end
'''.split())


def main(mode):
    path = os.path.join(RESULTS, f'{mode}.jsonl')
    cnt = collections.Counter()
    files = collections.defaultdict(set)
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            r = json.loads(line)
            for m in MACRO_RE.finditer(r.get('x', '')):
                name = m.group(1)
                if name in KNOWN:
                    continue
                cnt[name] += 1
                files[name].add(r.get('f'))
    print(f'{mode}: distinct unknown macros {len(cnt)}; occurrences {sum(cnt.values())}')
    for name, n in cnt.most_common(40):
        print(f'  {name:12s} {n:6d}  files={len(files[name])}  e.g. {sorted(files[name])[0]}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'render-zh')
