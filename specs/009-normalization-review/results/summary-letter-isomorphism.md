# SUMMARY ## A–Z 分节 ↔ 上游 contents.html 字母区 同构复核

- 日期：2026-10-30（首轮 c7d68354；同日批次二落地后本表为**终版**）
- 口径：全量列表行（含嵌套，`kind+slug` 树形文档序对齐）；上游源 = 最新快照 `en/_catalog/20261028T054741Z-contents.html` 的 `<h2>A</h2>`…`<h2>Z</h2>` 区
- 工具：`script/letter_isomorphism_audit.py`、`script/rebuild_summary_from_upstream.py`（树序重排生成器）、`script/sync_yuanwen_summary.py`（均为 gitignore 本地脚本）；逐条明细 `summary-letter-isomorphism.json`
- 四维：D1 条目有无 / D2 所在节 / D3 节内树序 / D4 别名对应

## 终版结论（批次二落地后）

| 维度 | 首轮 | 终版 | 手段 |
| ---- | ---- | ---- | ---- |
| D1 条目有无 | 上游独有 0；SUMMARY 独有 7（裁定保留） | **不变，零缺载** | 七条锚定至主题邻域（continental-rationalism→理性主义簇、pineal-gland→笛卡尔簇、qm-action-distance→量子力学簇、time-experience→时间簇、wyclif-political→威克里夫簇；wisdom/scientific-explanation 走集群母映射） |
| D2 所在节 | 真错位 5 + 设计差异 9 | **真错位 0**；集群挂靠设计差异 1（biology-developmental 随集群母落 B 区） | 全库树序重排（df83b456）：行序/嵌套深度/集群归属 1:1 随上游，5 条错位行归位 |
| D3 节内树序 | drift 349 | **由构造归零**（重排后 SUMMARY 树序≡上游树序；audit 旧口径退役，残余=占位行插入与单行化罗列的口径噪声） | 同上 |
| D4 别名 | 上游独有 40（双现别名） | **双向 0（557=557）** | 批次二补 40 条别名导航行 + 4 条占位集群母行（\*艺术与美学/\*公平/\*生命伦理学/\*动机）；新译名 3 条登记入册（阿里斯提普斯/劳特利→ren-ming-biao，智能设计论→yi-zhe-shuo-ming） |

## 首轮明细存档（2026-10-30 上午，处置记录见各节标注）

## D1 SUMMARY 独有 7 条（全部 baseline 在册）

| slug | 依据 |
| ---- | ---- |
| pineal-gland、qm-action-distance、wisdom、wyclif-political | 撤稿留存（009 底数「正式 1872+撤稿留存 6」成员；wisdom 保留裁定见 c75cc794/2eecf911，wyclif-political 见 bb561408） |
| continental-rationalism、scientific-explanation、time-experience | 历史缺载补回条目（ADR-0009 补回 6 条之列；上游目录页未列、SEP 站内在册） |

## D2 所在节差异 14 条逐条定性

设计差异（SUMMARY 排序键使然，不修）：

| 行 | slug | SUMMARY 节→上游区 | 定性 |
| ---- | ---- | ---- | ---- |
| 292 | biodiversity | B→E | 上游按倒装键 `ecology: biodiversity` 挂 E；SUMMARY 按显示主题 biodiversity→B |
| 504 | computational-linguistics | C→L | 上游挂 `language, philosophy of: computational` 集群区；SUMMARY 按 computational→C |
| 1308 | korean-buddhism (lv1) | J→K | SUMMARY 挂日本哲学集群；上游 K 区独立 |
| 1448 | modality-medieval (lv1) | L→M | 集群挂靠差异 |
| 1516 | information-biological (lv1) | L→I | 上游 `information: biological` 集群区 |
| 1987 | mathematics-explanation | P→M | 上游倒装 `explanation, in mathematics`；SUMMARY 按 mathematics→P |
| 1988 | mathematical-practice | P→M | 同上 |
| 2329 | economic-democracy (lv1) | S→D | 上游倒装 `democracy, economic`；集群挂靠 |
| 1299 | john-italos | J→I | 人名键：SUMMARY 按名 John、上游按姓 Italos |

真错位 5 条（锚定事故/排位错误，四维审计锁定为现状；**修复需单独裁定**，走结构改动流程）：

| 行 | slug | SUMMARY 节→上游区 | 说明 |
| ---- | ---- | ---- | ---- |
| 155 | lawphil-naturalism | A→N | 顶层行插在 A 区阿拉伯集群嵌套块中间，且阻断 L150 集群块嵌套 |
| 1385 | value-pluralism | K→V | 夹在 `knowledge, value of` 与 `knowledge how` 之间 |
| 1629 | naturalism | M→N | 正式条目排 M 区 |
| 2095 | utilitarianism-history | P→U | 排 P 区末 |
| 2368 | epistemic-utility | S→E | 排 S 区 |

## D3 节内树序 drift 349 条构成

- **placeholder ~130**：SUMMARY 自建集群导航占位行（链 README），上游无对应——设计使然。
- **alias ~18**：SUMMARY 别名行按别名主题排、上游挂目标条目区——系统性设计差异。
- **normal ~150**：各节内 LCS 85%+（如 M 区 194/227、A 区 206/240），drift 呈**成段位移**——SUMMARY 显示主题键 vs 上游倒装键的局部次序差 + 集群块挂靠位置差；无孤立漂移条目。
- 明细见 JSON `D3.<字母>.drift`。

## D4 别名双向

- 首轮：SUMMARY 别名行 517 slug ↔ 上游别名 557 slug；SUMMARY 独有 **0**；上游独有 40 条全部双现（正式行已被 SUMMARY 收录；含自指怪条目 `abortion, ethics of — see abortion, ethics of`，按 mu-lu-s 规则不收录）。
- 终版：批次二补 40 条别名导航行（中文裁定原则见 `script/d4_alias_table.py` 头注：同词自指引沿用既有先例、集群省略式子题直译、真别名通行译名）→ **557=557 双向归零**。

## 后续（更新于批次二落地后）

- ~~真错位 5 条修复~~ 已随全库树序重排落地（df83b456 + 本轮批次二提交）。
- 集群挂靠设计差异 1 条（biology-developmental 随集群母落 B 区）与 Z 区 18 条站务集群母（前言已置顶）登记豁免。
- 过程教训已规则化：`rules/05-ci-and-tools.md`「生成器与批量改写脚本」（写回前置门/幂等/逐行身份追踪/基线还原/观察驱动调试五条），AGENTS.md 硬约束速览加指针。
- 复核脚本与 JSON 可随上游新快照复跑回归。
