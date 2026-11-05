# SUMMARY ## A–Z 分节 ↔ 上游 contents.html 字母区 同构复核

* 日期：2026-10-30 首轮（c7d68354）→ 批次二（df83b456）→ **2026-10-31 批次三终版（本轮提交）**
* 口径：全量列表行（含嵌套，`kind+slug` 树形文档序对齐）；上游源 = 最新快照 `en/_catalog/20261028T054741Z-contents.html` 的 `<h2>A</h2>`…`<h2>Z</h2>` 区
* 工具：`script/letter_isomorphism_audit.py`（四维）、`script/rebuild_summary_from_upstream.py`（树序重排生成器，--inject 消费构造行）、`script/verify_tree_isomorphism.py`（**独立树序复核器**，difflib 身份对齐+深度豁免清单）、`script/sync_yuanwen_summary.py`（均为 gitignore 本地脚本）；逐条明细 `summary-letter-isomorphism.json`
* 四维：D1 条目有无 / D2 所在节 / D3 节内树序 / D4 别名对应

## 终版结论（批次三落地后，独立复核器验收）

| 维度 | 首轮 | 终版 | 手段 |
| ---- | ---- | ---- | ---- |
| D1 条目有无 | 上游独有 0；SUMMARY 独有 7（裁定保留） | **不变，零缺载** | 七条锚定至主题邻域 |
| D2 所在节 | 真错位 5 + 设计差异 9 | **真错位 0**；集群挂靠设计差异 3（biology-developmental B→D、moral-animal M→A、god-necessary-being N→G——同为 CLUSTER_MAP 预绑定的「集群归属行跟随集群母」决策呈现，与首轮 korean-buddhism 同类） | 全库树序重排（df83b456） |
| D3 节内树序 | drift 349 | **独立复核器验收：深度不一致 0、字母节不一致 0**（树序 2709 节逐项身份对齐；差异余量 22+17=全部登记豁免：上游重复罗列 16 别名+5 词条位、SUMMARY 锚定行 8+占位引用 4+D1 保留 5） | 批次一重排+批次三 22 条占位集群母补建（生物学/认知/物理学/时空/科学理论/柏拉图主义等，译名皆通名循既有占位惯例不另登记术语册），父集群母齐全后子行深度全部归位 |
| D4 别名 | 上游独有 40（双现别名） | **双向 0（557=557）** | 批次二补 40 条别名导航行；新译名 3 条登记入册 |

## mu-lu-s 同步核对（2026-10-31，用户指令）

* **mu-lu-s.md 零变更即完成同步**：批次二/三新增 66 行（40 别名导航+26 占位导航）均属 rules/01「别名词条与 * 前缀占位母词条预期不收录」类，mu-lu-s 覆盖面不受重排影响。
* `tools/check_mulu_s.py`：HARD ERRORS 0——坏链 0、SUMMARY 路径全覆盖（缺口 3=前言 2+占位 1，全部预期豁免）、**共有路径标题不一致 0**、重复收录 0。
* mu-lu-s 与 SUMMARY 的正式条目覆盖：1872 正式条目全在 mu-lu-s 分类视图中（覆盖缺口 0）。
* 深度豁免登记：`evolution-development`、`theories-biological-development`、`diagrams` 三行为 CLUSTER_MAP 绑定行的罗列子行（位置同构、深度形态差），verify_tree_isomorphism.py DEPTH_EXEMPT 清单存档。

## 过程教训（已规则化）

* 占位行落位失败的兜底掩盖：四轮 apply 各 +1 行累积——`rules/05-ci-and-tools.md`「生成器与批量改写脚本」五条纪律（写回前置门/幂等/逐行身份追踪/基线还原/观察驱动调试），AGENTS.md 硬约束速览有指针。
* 验证器对齐歧义教训：difflib 在重复身份节点（集群罗列+归一化）上选点歧义会产生误报——深度不一致需结合「上游前行=树父」校验区分真差异与对齐噪声；重复身份场景优先用多重集对照或显式豁免清单。
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

* **placeholder ~130**：SUMMARY 自建集群导航占位行（链 README），上游无对应——设计使然。
* **alias ~18**：SUMMARY 别名行按别名主题排、上游挂目标条目区——系统性设计差异。
* **normal ~150**：各节内 LCS 85%+（如 M 区 194/227、A 区 206/240），drift 呈**成段位移**——SUMMARY 显示主题键 vs 上游倒装键的局部次序差 + 集群块挂靠位置差；无孤立漂移条目。
* 明细见 JSON `D3.<字母>.drift`。

## D4 别名双向

* 首轮：SUMMARY 别名行 517 slug ↔ 上游别名 557 slug；SUMMARY 独有 **0**；上游独有 40 条全部双现（正式行已被 SUMMARY 收录；含自指怪条目 `abortion, ethics of — see abortion, ethics of`，按 mu-lu-s 规则不收录）。
* 终版：批次二补 40 条别名导航行（中文裁定原则见 `script/d4_alias_table.py` 头注：同词自指引沿用既有先例、集群省略式子题直译、真别名通行译名）→ **557=557 双向归零**。

## 后续（更新于批次二落地后）

* ~~真错位 5 条修复~~ 已随全库树序重排落地（df83b456 + 本轮批次二提交）。
* 集群挂靠设计差异 1 条（biology-developmental 随集群母落 B 区）与 Z 区 18 条站务集群母（前言已置顶）登记豁免。
* 过程教训已规则化：`rules/05-ci-and-tools.md`「生成器与批量改写脚本」（写回前置门/幂等/逐行身份追踪/基线还原/观察驱动调试五条），AGENTS.md 硬约束速览加指针。
* 复核脚本与 JSON 可随上游新快照复跑回归。
