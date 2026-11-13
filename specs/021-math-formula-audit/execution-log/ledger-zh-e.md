# 译文侧公式审计台账 — E

判定口径：`公式数`=站点渲染真值口径（math-plugin protectMath）；
`宏展开`=按 local.js 表就地展开的处数；`缺陷`=D1 残留下界定符 / D2 公式内中文 /
D3 零宽字符 / D4 % / D5 # / D6 $ 不成对 / D7 与 en 多重集差分。

| 词条 | 公式数 | 宏展开 | 缺陷 | 残余可渲染失败 |
| ---- | ---- | ---- | ---- | ---- |
| e/ecological-genetics.md | 45 | rG×10；rE×4 | 0 | 0（全量编译通过） |
| e/epiphenomenalism.md | 123 | — | 0 | 0（全量编译通过） |
| e/epistemology-evolutionary.md | 118 | Pr×6；frasl×1 | 0 | 0（全量编译通过） |
| e/epsilon-calculus.md | 227 | — | D7 23 | 0（全量编译通过） |
