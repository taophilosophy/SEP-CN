# 译文侧公式审计台账 — Q

判定口径：`公式数`=站点渲染真值口径（math-plugin protectMath）；
`宏展开`=按 local.js 表就地展开的处数；`缺陷`=D1 残留下界定符 / D2 公式内中文 /
D3 零宽字符 / D4 % / D5 # / D6 $ 不成对 / D7 与 en 多重集差分。

| 词条 | 公式数 | 宏展开 | 缺陷 | 残余可渲染失败 |
| ---- | ---- | ---- | ---- | ---- |
| q/qm-relational.md | 116 | ket×4；lsq×2；rsq×2 | D7 4 | 0（全量编译通过） |
| q/qm.md | 260 | ket×100；braket×27 | D7 14 | 0（全量编译通过） |
| q/qt-entangle.md | 62 | ket×51 | D7 1 | 0（全量编译通过） |
| q/quantum-bayesian.md | 45 | — | D7 6 | 0（全量编译通过） |
| q/quine-nf.md | 159 | rsquo×5；amp×5 | D7 8 | 0（全量编译通过） |
