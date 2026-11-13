# 译文侧公式审计台账 — L

判定口径：`公式数`=站点渲染真值口径（math-plugin protectMath）；
`宏展开`=按 local.js 表就地展开的处数；`缺陷`=D1 残留下界定符 / D2 公式内中文 /
D3 零宽字符 / D4 % / D5 # / D6 $ 不成对 / D7 与 en 多重集差分。

| 词条 | 公式数 | 宏展开 | 缺陷 | 残余可渲染失败 |
| ---- | ---- | ---- | ---- | ---- |
| l/lakatos.md | 5 | — | 0 | 0（全量编译通过） |
| l/langer.md | 4 | — | 0 | 0（全量编译通过） |
| l/logic-dynamic.md | 670 | ldquo×1；rdquo×1 | D7 12 | 0（全量编译通过） |
| l/logic-fuzzy.md | 266 | — | D6 1；D7 21 | 0（全量编译通过） |
| l/logic-hybrid.md | 263 | amp×3 | D2 2；D7 4 | 0（全量编译通过） |
| l/logic-linear.md | 174 | bang×34；quest×34；lpar×18；Up×18；amp×16；Down×14 | D7 10 | 0（全量编译通过） |
| l/logic-preference.md | 459 | llbracket×9；rrbracket×9；coloneq×3 | D1 29；D7 13 | 0（全量编译通过） |
| l/logic-provability.md | 358 | Prov×46；PA×28；Diamond×28；bs×12；GL×10；Proof×3 | D1 1；D2 1；D7 31 | 0（全量编译通过） |
| l/logic-relevance.md | 361 | amp×60；True×4；False×4；prurel×3 | D7 14 | 0（全量编译通过） |
| l/logic-substructural.md | 398 | amp×8 | D7 26 | 0（全量编译通过） |
| l/logical-consequence.md | 121 | tonk×3；amp×2 | 0 | 0（全量编译通过） |
