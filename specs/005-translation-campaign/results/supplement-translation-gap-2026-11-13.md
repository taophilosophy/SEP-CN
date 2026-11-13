# 词条补充材料译文缺口清单（2026-11-13 全库扫描）

## 方向声明（rules/08 §1）

- 意图：查清中文词条正文所链、本地却不存在的 `<slug>.<x>.md` 文件究竟是什么，并给出可复核的缺口台账。
- 目标：判定缺口性质、列出全部实例、标明英文源与原文镜像位置。
- 非目标：本轮不翻译任何补充材料，不改正文链接，不新建任务 JSON。
- 验收判据：`check_all.py` 9 项全绿；清单中每个目标路径均能在 `en/` 与 `yuanwen/` 两侧定位到同名源；文件数可由下列扫描口径复算。

## 扫描口径

遍历 `git ls-files` 中 `<letter>/*.md` 的 Markdown 内联链接，取形如 `<slug>.<x>.md` 的相对路径；
排除外链、锚点、含占位符（`<`、`SLUG`）的示例链接，以及 `specs/`、`en/`、`yuanwen/`、生成物预览。

- 缺件引用总次数：49
- 不同缺件文件数：31
- 英文源 `en/<slug>/<x>.html` 齐备：31 / 31
- 原文镜像 `yuanwen/<letter>/<slug>.<x>.md` 齐备：31 / 31
- 英文源合计体积：597.3 KB
- 已落地的同类文件：8 个（如 `a/abduction.peirce.md`、`p/peter-damian.supplement.md`），证明命名与落地机制可用，属逐条漏译。

## 结论

这些文件是 SEP 的补充材料（Supplementary Documents）：主编条页面之外、由 `index.html` 相对引用的独立 HTML，
通常是长篇论证、形式化推导、史料年表或图版说明。本项目 `rules/01` 第 11、57 行规定其镜像形态为
`<letter>/<slug>.<x>.md`，与主词条同目录平铺，不进入 `SUMMARY.md` 目录。

因此本项缺口是**译文未落地**，不是抓取或管线缺陷：`fetch_entry.py` 与 `yuanwen.py` 已按契约把英文源和原文镜像全部收齐，
中文侧只译了主词条并保留了链接。站点 `ignoreDeadLinks: true`，故 `check_all.py` 不报错，读者点击却会落空。

## 缺口台账

| 中文目标路径 | 引用次数 | 正文所用中文标题（去重） | 英文源 | 源 KB |
| ---- | ---- | ---- | ---- | ---- |
| `a/ancient-soul.supplement.md` | 1 | 补充材料：伯内特论希腊人的灵魂概念 | `en/ancient-soul/supplement.html` | 13.0 |
| `a/axiom-choice.choice-and-type-theory.md` | 1 | 选择公理与类型论 | `en/axiom-choice/choice-and-type-theory.html` | 25.5 |
| `b/brouwer.strongcounterex.md` | 1 | 强反例 | `en/brouwer/strongcounterex.html` | 13.9 |
| `b/brouwer.weakcounterex.md` | 1 | 弱反例 | `en/brouwer/weakcounterex.html` | 15.0 |
| `d/descartes-works.history.md` | 1 | 笛卡尔的法学论文 | `en/descartes-works/history.html` | 18.0 |
| `i/imprecise-probabilities.supplement-formal.md` | 2 | 形式附录 | `en/imprecise-probabilities/supplement-formal.html` | 29.5 |
| `i/imprecise-probabilities.supplement-historical.md` | 1 | 历史附录 | `en/imprecise-probabilities/supplement-historical.html` | 41.0 |
| `i/intrinsic-extrinsic.grounding-theories.md` | 1 | 内在性奠基理论补论 | `en/intrinsic-extrinsic/grounding-theories.html` | 15.3 |
| `i/intrinsic-extrinsic.non-disjunctive.md` | 1 | 非析取理论补论 | `en/intrinsic-extrinsic/non-disjunctive.html` | 17.9 |
| `i/intrinsic-extrinsic.relational-theory.md` | 2 | 内在性的关系性说明 | `en/intrinsic-extrinsic/relational-theory.html` | 20.4 |
| `j/japanese-aesthetics.ginkakuji-kinkakuji.md` | 1 | 银阁寺银阁与金阁寺金阁大图 | `en/japanese-aesthetics/ginkakuji-kinkakuji.html` | 12.2 |
| `j/japanese-aesthetics.ginkakuji.md` | 1 | 银阁寺银沙滩与向月台大图 | `en/japanese-aesthetics/ginkakuji.html` | 12.0 |
| `j/japanese-aesthetics.late-spring.md` | 1 | 晚春》剧照放大序列 | `en/japanese-aesthetics/late-spring.html` | 12.3 |
| `j/japanese-aesthetics.ryoanji.md` | 1 | 龙安寺枯山水庭园大图 | `en/japanese-aesthetics/ryoanji.html` | 12.4 |
| `j/japanese-aesthetics.splashed-ink.md` | 1 | 雪舟《泼墨山水 | `en/japanese-aesthetics/splashed-ink.html` | 11.9 |
| `j/japanese-aesthetics.tokyo-story.md` | 1 | 东京物语》剧照放大序列 | `en/japanese-aesthetics/tokyo-story.html` | 12.3 |
| `k/kant-judgment.supplement1.md` | 7 | 共同性原则、康德的概念论与康德的非概念论 | `en/kant-judgment/supplement1.html` | 29.4 |
| `k/kant-judgment.supplement2.md` | 3 | 判断、信念与科学认识 | `en/kant-judgment/supplement2.html` | 21.2 |
| `k/kant-judgment.supplement3.md` | 1 | 康德逻辑的表面局限与混乱是否会损害其判断理论？ | `en/kant-judgment/supplement3.html` | 20.5 |
| `k/kant-judgment.supplement4.md` | 3 | 使用的种类；判断的各种使用 | `en/kant-judgment/supplement4.html` | 25.2 |
| `k/kant-judgment.supplement5.md` | 5 | 补全康德判断形而上学之图景 | `en/kant-judgment/supplement5.html` | 26.8 |
| `k/kochen-specker.proofvc1.md` | 1 | VC1 证明 | `en/kochen-specker/proofvc1.html` | 14.4 |
| `l/logic-fuzzy.readings-by-topic.md` | 1 | Bibliography Sorted by Topic | `en/logic-fuzzy/readings-by-topic.html` | 42.2 |
| `l/logic-relevance.logic-b-dj-dk.md` | 1 | 逻辑 $\mathbf{B}, \mathbf{DJ}$ 与 $\mathbf{DK}$ | `en/logic-relevance/logic-b-dj-dk.html` | 14.5 |
| `l/logic-relevance.logice.md` | 1 | 逻辑 $\mathbf{E}$ | `en/logic-relevance/logice.html` | 14.1 |
| `l/logic-relevance.logicnr.md` | 1 | 逻辑 $\mathbf{NR}$ | `en/logic-relevance/logicnr.html` | 14.4 |
| `l/logic-relevance.logicr.md` | 2 | 逻辑 $\mathbf{R}$ | `en/logic-relevance/logicr.html` | 14.1 |
| `l/logic-relevance.logics.md` | 1 | 逻辑 $\mathbf{S}$ | `en/logic-relevance/logics.html` | 13.6 |
| `s/spacetime-holearg.active-passive.md` | 1 | 主动与被动协变性 | `en/spacetime-holearg/active-passive.html` | 21.5 |
| `s/spacetime-holearg.gauge.md` | 1 | 作为分析规范自由度之模板的空穴论证 | `en/spacetime-holearg/gauge.html` | 27.0 |
| `s/spacetime-holearg.leibniz-equivalence.md` | 2 | 通过地图投影直观理解莱布尼茨等价 | `en/spacetime-holearg/leibniz-equivalence.html` | 15.8 |

## 后续处置建议（本轮不执行）

1. 按 `rules/04` 流程先行逐条建任务，先登记术语再动笔，三校留 `evidence`；不得据既有中文主词条措辞反推补充材料。
2. 零信任：以 `en/<slug>/<x>.html` 与 `yuanwen/` 镜像为底稿，回源核对版本钉（pubinfo、存档版名、SHA-256）。
3. 体例照 `a/abduction.peirce.md`：H1 中文标题、来源引用块、说明行、正文分段守恒。
4. 落地后复核本清单引用处可解析；`ignoreDeadLinks` 不宜作为长期豁免依据。
