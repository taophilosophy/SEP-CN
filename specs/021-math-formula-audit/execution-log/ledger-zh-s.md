# 译文侧公式审计台账 — S

判定口径：`公式数`=站点渲染真值口径（math-plugin protectMath）；
`宏展开`=按 local.js 表就地展开的处数；`缺陷`=D1 残留下界定符 / D2 公式内中文 /
D3 零宽字符 / D4 % / D5 # / D6 $ 不成对 / D7 与 en 多重集差分。

| 词条 | 公式数 | 宏展开 | 缺陷 | 残余可渲染失败 |
| ---- | ---- | ---- | ---- | ---- |
| s/schema.md | 63 | — | D7 2 | 0（全量编译通过） |
| s/scientific-explanation-20th.md | 92 | Pr×2 | D7 4 | 0（全量编译通过） |
| s/social-procedures.md | 173 | — | D7 5 | 0（全量编译通过） |
| s/spacetime-holearg.md | 62 | — | D7 28 | 0（全量编译通过） |
| s/stebbing.md | 10 | — | 0 | 0（全量编译通过） |
