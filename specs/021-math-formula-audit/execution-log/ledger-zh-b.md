# 译文侧公式审计台账 — B

判定口径：`公式数`=站点渲染真值口径（math-plugin protectMath）；
`宏展开`=按 local.js 表就地展开的处数；`缺陷`=D1 残留下界定符 / D2 公式内中文 /
D3 零宽字符 / D4 % / D5 # / D6 $ 不成对 / D7 与 en 多重集差分。

| 词条 | 公式数 | 宏展开 | 缺陷 | 残余可渲染失败 |
| ---- | ---- | ---- | ---- | ---- |
| b/belief-merging.md | 262 | IC×71；mymod×6；mymax×3；mymin×2 | D7 16 | 0（全量编译通过） |
| b/bohr-correspondence.md | 129 | rH×8 | D7 17 | 0（全量编译通过） |
| b/boolalg-math.md | 173 | val×14；dom×4；range×2 | D7 7 | 0（全量编译通过） |
| b/brouwer.md | 6 | — | 0 | 0（全量编译通过） |
