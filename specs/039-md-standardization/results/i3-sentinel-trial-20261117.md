# I3 哨兵标定试跑报告（2026-11-17）

任务：specs/039 P9 前置卡点「I3 数学跨度归一」（用户批准第③项）。
工具：`tools/check_yuanwen_fidelity.py` v2（strip_math_ex 三计数＋哨兵＋对称性分类）；
单测 `tools/tests/test_yuanwen_fidelity.py` 9 例；全库试跑 8m14s，
原始输出 `i3-sentinel-trial-20261117.json`。

## 方法

1. **哨兵替换**：成对数学跨度内容统一替换为 `U+E000`（字母流判据下与空格等价，
   为将来序列比对预留标记）；转义感知扫描保留（`\left(` 截断问题 v1 已解）。
2. **三计数**：每侧统计 `spans`（成对数）/`oversize`（跨度 >6000 字符，转换器把相邻
   公式与中间正文并成大跨度）/`unclosed`（缺 closer 的独立 `$`、残缺 `\(`）。
3. **对称性分类**：两侧计数不等或任侧 oversize/unclosed → `math-asymmetric`
   （字母判据对该件不适用，审计档软信号单列，不混入 text-stream-diff）；
   对称且有字母差 → `text-stream-diff`（真候选）；转义 opener（`\$`）按字面。

## 试金石（开工判例）

| 件 | v1（2026-11-16） | v2 | 定性 |
| ---- | ---- | ---- | ---- |
| formal-belief | text-stream-diff 缺 49307 字母（噪声） | math-asymmetric-diff | 工具噪声隔离 ✓ |
| logic-many-sorted | 同上 | math-asymmetric-diff | ✓ |
| quine-nf | 同上 | math-asymmetric-diff | ✓ |
| abhidharma | 零 issue | 零 issue | 无回退 ✓ |
| sartre / buber | 误判为数学噪声 | **text-stream-diff（真候选）** | 见下节，实为真缺陷 |

## 全库数字（1871 件可比）

| 项 | v1（2026-11-16） | v2（本次） |
| ---- | ---- | ---- |
| 无差别 | 1490 | 1551 |
| math-asymmetric（判据不适用） | —（混入差异） | **320**（其中 203 兼有字母差，单列不判） |
| text-stream-diff（真候选） | 381（混杂） | **195** |

## 195 件候选聚类（词元特征）

| 族 | 件数 | 判读 |
| ---- | ---- | ---- |
| **书目嵌套/译本条目族** | ≥6（feyerabend/foucault/gadamer/james-ward/sartre/buber） | **真缺陷**：转换器丢弃书目 `<ul>` 内嵌套 `<li>` 子条目（sartre 缺 4193 字母，"F. Alcan" 整条蒸发；html 186 li vs md 166 defs） |
| Notes 号码族 | 9 | 多为注号/DOI 数字簿记（数字不入字母判据，word 层信号），待逐条定性 |
| 其他 | 180 | 抽样示 URL/DOI 断行、图注与链接文字差异，待逐条定性（P9 面） |

## 新缺陷族登记（归 specs/018/023 转换保真线）

**书目嵌套 `<li>` 丢弃**：全库扫描书目区含嵌套列表的包 **129 个**
（`expect≈129`，修复时以逐件 diff 复核为准）。修复方向：`yuanwen.py` 列表
分支支持 li 内嵌 ul/ol（子条目转 `[^key]:` 定义或缩进列表，随体例裁定）。
该修复属翻译面之外的转换器线，另立卡执行；修复前 129 包的 I3 letter 差异
不得据此判「译文缺陷」。

## 结论与后续

1. v2 分类器有效：噪声（数学边界）与真候选分离，381 → 320+195。
2. I3 仍列**审计档**（升门三前置：①195 件逐条定性；②书目嵌套 li 修复；
   ③math-asymmetric 320 件中 203 兼差件的复核）。本轮完成①的方法面与②③的定量底数。
3. 白名单候选增补：URL/DOI 断行差异（两侧均为机器标识符，簿记面已由
   `check_pairs dangling-link`／`en_integrity` 管辖）——待逐条定性后裁定是否入白名单。

---

## 修正与修复后复测（2026-11-17 晚，5645e67b7 之后）

**归因修正**：本报告「书目嵌套 `<li>` 丢弃」族定性**作废**——A/B 实证嵌套 li 本会进 bib_entries；真机制＝`build_cite_keys` 无姓氏路径整条 continue（主文献区年份起首条目节首无可继承姓氏，sartre 30 条蒸发）。「129 包」扫描量的是良性结构属性。详见 execution-log 2026-11-17 晚节。

**修复后全库复测**（`results/i3-post-citefix-20261117.json`）：

| 项 | 修复前 | 修复后 |
| ---- | ---- | ---- |
| text-stream-diff（真候选） | 195 | **164**（−31，键修复消解） |
| math-asymmetric（判据不适用） | 320 | 320 |
| math-asymmetric-diff | 203 | 234 |
| sartre / buber | 真候选 | **归零** |

**164 件聚类**：URL/DOI 族 36（断行与形态差，簿记面已由 check_pairs dangling-link/en_integrity 管，白名单候选）｜Notes 号码族 12（注号数字簿记）｜其他待定性 116（P9 逐条定性面，抽样含 html 侧标签断词形态差）。

**math-asymmetric-diff 234 件抽样 3/3 确认为跨度伪差**（html 未闭合 opener 致 TeX 字母漏入流、md 超限吞段）——审计档分类成立。
