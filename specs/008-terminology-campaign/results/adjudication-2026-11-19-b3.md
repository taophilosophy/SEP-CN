# 术语在线精确命中裁定报告（批三）2026-11-19

口径：用户裁定「不需要人工判读，全量，不计成本，从既有词条逐个研判」；数学门类/数学哲学命中一律入研判管线，按既有词条语境（yuanwen/ 忠实镜像）逐条定夺。

研判对象：b2 落册后剩余精确命中，滚动提取 397 词（10 块 → 修正去重后 7 块），逐条判定。

## 汇总

| 判定 | 件数 | 处置 |
| ---- | ---- | ---- |
| ADOPT（审定读法直接登记） | 163 | 落册 |
| ADJUST（按条目语境改读，依据列双录审定原读与研判理由） | 93 | 落册 |
| REJECT（拒录：普通词/多义随文/假命中/同概念合并） | 133 | 持久化 `rejects-2026-11-19-b3.json`，后续批次不再回流 |

落册 256 行（`rowspec-2026-11-19-b3-verdicts.json`），池 publish 256，`check_terms` 绿。

## 改读要点（93 条中抽样）

| 原文 | 审定读法 | 研判读法 | 定性 |
| ---- | ---- | ---- | ---- |
| hard problem of consciousness | 意识的难问题 | 意识难题 | 中文哲学界通行形 |
| modularity | 构件性（克隆植物生态学） | 模块性 | 审定学科误置（心智模块性） |
| whiteness | 白度（色度学） | 白人性 | 批判种族理论与 Blackness=黑人性 对偶 |
| analyticity | 解析性（数学） | 分析性 | 与 analytic=分析的 词族一致 |
| fetishism | 恋物症（性医学） | 拜物教 | 马克思商品拜物教语境 |
| manipulation | 手法（中医骨伤） | 操纵 | 阿多诺文化工业/操纵论证 |
| mentalism | 心理主义 | 心灵主义 | 避让 psychologism=心理主义 |
| feminist theory | 女权主义理论 | 女性主义理论 | 库内女性主义词族一致 |
| meritocracy | 能力主义 | 贤能政治 | 避让 ableism=能力主义；儒家语境 |
| endurance | 续航时间（航空） | 持存 | 形上学持久性理论（与 perdurance 对偶） |
| Uniqueness | 独创性（著作权） | 唯一性 | 限定摹状词语境 |
| literal interpretation | 望文生训（训诂禁忌） | 字面解释 | 诠释学中性方法论词 |
| liberation | 解离（选矿） | 解放 | 妇女解放/宗教解脱语境 |
| reliability | 信度（心理测量） | 可靠性 | 可靠主义词族 |
| truth function | 真假值函数 | 真值函数 | 通行形 |
| empowerment 类审定义误置 | — | — | 见各行依据列 |

## 去重与流程修复（本批）

1. 拒录清单持久化（`results/rejects-*.json`），提取器加载排除——b3 二轮提取 574→491→（修正后）397，已处理词不再回流。
2. 变体合并（一行一概念）：moral judgement/moral judgment、social relation(s/ship)、sense modality/sensory modality、a priori probability/prior probability、measuring instrument(s)、special science(s)、Chinese room argument、logical relation(ship) 等全部并入主导形。
3. 修漏挂：`verdict-b2-04/05` 曾误写目录（script/tl-review 缺 tmp），119 条判定未入库，已补合并新插入 81 行。
4. 修遗漏：b2-01 三条在推理中已判但漏写 JSON（Addition、additional condition、adult education），本批补记并持久化为拒录，杜绝三度回流。
