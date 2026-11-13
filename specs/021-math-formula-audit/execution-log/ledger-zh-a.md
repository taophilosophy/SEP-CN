# 译文侧公式审计台账 — A

判定口径：`公式数`=站点渲染真值口径（math-plugin protectMath）；
`宏展开`=按 local.js 表就地展开的处数；`缺陷`=D1 残留下界定符 / D2 公式内中文 /
D3 零宽字符 / D4 % / D5 # / D6 $ 不成对 / D7 与 en 多重集差分。

| 词条 | 公式数 | 宏展开 | 缺陷 | 残余可渲染失败 |
| ---- | ---- | ---- | ---- | ---- |
| a/abilities.md | 2 | — | 0 | 0（全量编译通过） |
| a/abstract-objects.md | 236 | — | D3 13；D7 33 | 0（全量编译通过） |
| a/action.md | 8 | amp×9 | D7 1 | 0（全量编译通过） |
| a/actualism-possibilism-ethics.md | 335 | lamp×21；at×9；rO×5 | D2 3；D6 1；D7 46 | 0（全量编译通过） |
| a/al-khunaji.md | 164 | amp×1 | D7 2 | 0（全量编译通过） |
| a/alberic-paris.md | 8 | — | 0 | 0（全量编译通过） |
| a/algebra-logic-tradition.md | 92 | ORjev×7 | 0 | 0（全量编译通过） |
| a/arabic-islamic-phil-math.md | 85 | — | D7 5 | 0（全量编译通过） |
| a/axiom-choice.md | 547 | bA×64；sH×40；inn×37；bB×33；bPhi×31；sA×17 | D7 29 | 0（全量编译通过） |
