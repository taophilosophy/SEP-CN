# specs/039 执行记录

## 2026-11-16 · P1 治理层（已推送 8c2ed13f2）

* 立 [ADR-0063](../../rules/adr/0063-中文体例归一入s2.4双轴与转换保真不变量.md)（accepted），把三轮裁定固化为条文：s2.4 三轴、尾序 canonical（`脚注` 末位）、编号点号式、I2/I3 不变量、补丁准入谓词与 C1–C4、判定权只读、revert 扩 s2.4（含 done）、规则可判性四件套、LaTeX 第三轮否决。
* 规则落点：`rules/04` s2.4 节改双轴＋勘误轴、状态机两处括注、回退段补 416 口径；`rules/05` 新增“判定权与规则所有权”（含 fixer 放行自检三项、测量效度判例）；`rules/08` 新增 §14；`rules/README` 判例两条；`rules/adr/README` 索引；`AGENTS.md` 硬约束表增“体例归一”“派生保真”两行。
* 门禁：`check_all` 11 项全绿（未新增门，避免与 P9 重叠）。

## 2026-11-16 · P2 工具层

| 工具 | 变更 | 验证 |
| ---- | ---- | ---- |
| `tools/check_pairs.py` | 体例轴四则（`tail-order` 含脚注末位、`heading-number` 点号式与跳号、`h1-form` 作者括号＋英文题一致性、`errata-apply` 勘误落地）＋`--gate` 只对 `HARD_RULES` 计退出码；桩件与带点子文档豁免 | `a/abhidharma`（脚注前置）报 `tail-order`＋编号；`a/abduction`（裸号）报 4 条编号；`a/anscombe`（点号＋canonical）零 issue 退出 0 |
| `tools/check_en_patches.py` | C2 准入谓词（空白差／标记差）、字段齐备、`--strict` 升硬、`admission_bad` 计数 | 现存 3 条池内补丁全部判 `blank`（`admission_bad=0`，命中计数 3/3 相符） |
| `tools/check_yuanwen_fidelity.py`（新） | I2-lite 基线钉交叉核对（`md-hand-edited`／`source-drift`／`no-baseline`）＋`--deep` 的 I3 字母多重集比对（数字只作软信号） | A 字头 160 件 I2-lite 零异常 |
| `tools/task_ops.py` | `_style_gate` 挂 `advance --step s24`（`check_pairs --gate`＋`check_style`）；`revert-state` 目标态扩 `s2.4_termchecked`、源态集扩 `s2.5_checked`，加“历史无 s2/s24 记录即拒”守卫 | 单测 `tools/tests/test_adr0063.py` 21 例全绿 |

### I3 标定过程（白名单 v0，实测）

按 40 件、60 件两轮抽样逐个定性，形成白名单与判据：

| 差异类 | 定性 | 处置 |
| ---- | ---- | ---- |
| 目录（`div#toc`）文本 | 导航非内容 | 深度配对剥除 |
| 行内标签断词（`<em>A</em>s`） | 渲染同形 | 块级标签断词、行内标签不断词 |
| `References（引用注释）` ↔ `Bibliography` | 转换器命名 | 折叠同义节题 |
| 书目转 `[^key]:` 定义、Notes 段归位 | 合法移位 | 多重集判据（序列不敏感） |
| 作者行（`citation_author`）、`（原文脚注）` 括注、底稿注记行 | 转换器构造 | 显式剔除 |
| 图 alt 长说明 → 图注文 | 转换器构造（ADR-0037） | alt≥40 字入源流，短 alt 视为装饰 |
| 上下标 `G<sub>1</sub>` vs `G₁` | NFKD 同形 | NFKD 归一 |
| 注号、有序列表号、书号 | 两侧字面形态不对称 | 数字不入主判据，报 `digits` 软信号（数字面归三校数字对账／`check_math`） |

抽样结果：60 件 → 6 件残留（`aesthetic-testimony` 多 142 字母、`al-khunaji` 缺 294 字母等），已作为缺陷候选，待全量台账定性。

### 全量台账（1873 件，2026-11-16）

| 项 | 结果 |
| ---- | ---- |
| I2-lite 基线钉 | **零异常**（`md-hand-edited` 0、`source-drift` 0；仅 2 件 `no-baseline`）——全库 `yuanwen` 与转换登记一致，无手改产物 |
| I3 `--deep` | 1871 件可比，**381 件差异**（20.4%）：缺字为主 139、多字为主 205、双向 37；量级 >200 字母 109 件 |

**残差定性（重要，防误判为缺陷）**：抽 `formal-belief`（缺 49307 字母）、`logic-many-sorted`、`sartre`、`buber` 逐句核对，被报「html 独有」的句子（如 “The heart of subjective probability theory…”）**在 md 中确实存在**。根因是**数学定界符跨度两侧不等价**：html 侧 `\(…\)` 与 md 侧 `$…$` 覆盖范围不同（转换器可能合并/断开跨度），剥离后文本缺口位置不同，叠加多重集后表现为大额字母差。故 381 件**不能计入内容缺陷**，属工具噪声。

结论与后续：I3 暂列**审计档**（不进门禁）；门禁面先用 I2-lite（已零异常）＋`check_math`（公式数与内容）＋三校数字对账覆盖数学件。I3 若要升门，须先解决数学跨度归一（候选方案：两侧统一替换为同一哨兵并保证跨度边界来自同一解析，或仅在无数学件上启用）。

## 待办（P3–P9）

* 全量 `--deep` 台账与逐条定性（转换器缺陷 → 修 `yuanwen.py`；白名单缺项 → 登记）。
* 基线钉 I2-lite 全量跑，确认零 `md-hand-edited`。
* 30 件重复 H1 修 `yuanwen.py`（`citation_title` 前置条件），`expect=30` 定点重转。
* 勘误表 31 行／17 slug 落地核对（§8.1 yorck 零动作、§8.2 四件核读法＋译注）。
* 存量归一（编号 2076、脚注移段 87）与 416 件回退重走。
