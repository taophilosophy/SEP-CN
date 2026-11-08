# M 批进度对账与接管记录（2026-11-08）

**会话**：M-main-20261108　**范围**：`m/` 一批 139 条正式词条　**指派**：用户指令「计算、同步、纠正目前 M 词条的翻译进度，不使用子代理；现在由你负责翻 M」
**方法**：五方对账（沿用 `script/lmn_audit4.py` 口径）——SUMMARY 正式词条 × 成稿（行数/字节/节）× 任务 JSON 状态机 × 段落账本（段数与 step2 填充）× git 最后改动；另加结构三检（H1↔SUMMARY、baseline 覆盖、version_pin）。

## 1. 复算结果（2026-11-08 02:2x UTC 基线）

| 项 | 数值 | 依据 |
| --- | --- | --- |
| 正式词条 | 139 | SUMMARY `m/` 行 190 行 = 139 正式 + 51 别名/占位（`\*` 前缀，不建任务） |
| 英文基线 | 139/139 | `baseline/entries.json` |
| 转换镜像 | 139/139 | `yuanwen/m/` |
| 已成稿（>1 行） | 7 | 字节 31–70 KB；其余 132 条为单行占位（80 字节级） |
| **done** | **6** | `marsilius-inghen`、`mathematics-inconsistent`、`modesty-humility`、`molyneux-problem`、`montesquieu`、`moral-responsibility-empirical` |
| s3_checked（评审线） | 1 | `moral-demands-permissions`（账本 63/63、成稿 221 行；r1–r3 归 R-main-20261108，见 session-handoff §6，本会话不重复推进） |
| pending 任务 | 7 | `mandeville`、`marsilius-padua`、`mathematical-practice`、`model-organisms`、`montessori-maria`、`moral-learning`、`music` |
| 未建任务 | 125 | 139 − 14 |
| 待译（本会话责任） | **132** | 139 − done 6 − 评审线 1 |

## 2. 偏差与处置

* **账实零偏差**：无「有稿无任务」「done 无稿」「成稿状态滞后」三类偏差——与 §6 之 LMN-main-20261108 复算口径一致（M done 5→6 系 `moral-responsibility-empirical` 收口，已在该记录内）。
* **结构三检零缺陷**：139 条 H1 与 SUMMARY 条目文字逐字符一致；139 条基线齐备；14 份任务 JSON 的 `version_pin`（pubinfo + 存档版 + SHA-256）无缺失。
* **唯一需同步项是归属**：`ledger.json` 的 m 批 `claimed_by` 仍停在已收工会话 `LMN-main-20261108e`。处置：`campaign.py claim m --session M-main-20261108 --force` + `advance m translate --note`（计数依据写在注记里）。
* **PROGRESS.md**：`tools/progress.py` 重生成（生成物，不手改）。

## 3. 本会话作业计划

1. 先清 7 条 pending 任务（已建任务、已 cleared 前置齐备者从 `clear` 起步），再按 SUMMARY 序对 125 条未建任务逐条 `task_ops.py create --kind retranslate` 并走完整状态机。
2. 每条作业口径：`lq.py init` 建账本 → 双版直译（step1 忠实／step2 语言）分批落盘并即时提交 → `lq.py check`（HARD=0 为写回前置门）→ `compose --write` → `italic_to_bold_cjk` → s1（逐段核销＋文献还原＋相关词条逐条对 SUMMARY）→ s2（prose 告警清零或逐条留痕豁免）→ s3（体例四检）→ 交评审线（r1–r3 归 R-main，见 session-handoff §6）。
3. 术语与人名先登记后使用（`yi-zhe-shuo-ming.md`、`ren-ming-biao.md`）；并行会话占用共享登记册时按行键选择性暂存。
4. 单会话吞吐受源文体量限制（M 批单条 yuanwen 37–192 KB，平均约 100 KB），按条收口、高频小步提交；断点以 `campaign.py status` 现查为准。

## 4. 接管复算（2026-11-08 04:4x UTC，M-main-20261108 接续会话）

以 `script/lmn_audit4.py m` 复算五方对账，与 §1 基线一致，仅一处推进：

* **mandeville 收口到 drafted**：工作区遗留的 299 行成稿经三重验证后落盘提交（82eebb20）——`lq.py check` 守恒 HARD=0（88 段，软提示均为机械段/斜体转书名号正常项）；compose 干跑与工作区成稿逐字符 diff=0；`italic_to_bold_cjk` 转换 0 行（书名一律书名号）。任务 advance draft，evidence 留痕。
* **moral-demands-permissions 维持 s3_checked**：属评审线 R-main-20261108 队列（session-handoff §6），本会话不推进 r1–r3，非偏差。
* **PROGRESS.md 重生成**：全局 done 202 / 在途 234（含并行会话推进）；M 批任务 14、done 6、drafted 1、s3_checked 1、pending 6、未建 125。
* 归属无变化：m 批 claimed_by=M-main-20261108（§2 处置已由上一会话完成），接续会话沿用该身份记账。
* 待译口径更新：**132 条不变**（139 − done 6 − 评审线 1）；其中 1 条（mandeville）已到 drafted，作业主线为其 s1 逐段核销，其余按 §3 计划推进。

## 5. 接管复算（2026-11-08 12:1x UTC，M-main-20261108 第三段接续）

* **五方复算零偏差**：139 正式 = 成稿 8（done 6 + 在途 2）+ 单行 131；任务 14 = done 6 + drafted 1（mandeville）+ s3_checked 1（moral-demands-permissions，属 R-main 评审线）+ pending 6；未建 125。`script/lmn_audit4.py m` 与 `campaign.py status` 一致。
* **通知/纠正**：工作区遗留 mandeville 润色件（2026-11-08 19:12，33 段 step2 同步 + 段 51 step1 误译修正「bare bones notion 骨瘦如柴→极其粗略」）经三重核验收编——`lq.py check m mandeville` HARD=0（88 段，软提示均为机械段/斜体转书名号正常项）、`lq.py compose` 与成稿逐字符相等、抽检 5 段忠实无损；commit e3873bb4，任务 draft 凭证补记。
* **同步**：`tools/progress.py` 重生成（全局 done 213 / 在途 230）；`campaign.py advance m translate --note` 记复算口径与下一目标（commit f04c6d5b）。`claimed_by` 维持 M-main-20261108。
* **待译口径**：132 条（含 mandeville）。作业序：mandeville s1→s2→s3 → 6 条 pending（按源文词数升序）→ 125 条未建任务按 SUMMARY 序。

## 6. mandeville 三校收口（2026-11-08 13:0x UTC，本会话）

* **s1**：逐段核销 88/88（61 段叙述正文 + 19 节标题 + 机械段）；结构全等（脚注定义 90/90、marker 78/78、标题 27/27、相关词条 12/12 对 SUMMARY 逐字符一致）；修订 2 处——段 63 回源删增译「原始」、段 75 Smith 译名「史密斯」→「斯密」（ren-ming-biao Adam Smith 行）。
* **s2**：语言层修订 2 处（段 72 搭配、段 85 重复）；check_prose 2 条 de-chain 均为书名《蜜蜂的寓言：或，私人的恶德，公众的利益》内部「的」链误报，按 ADR-0020 逐条豁免。
* **s3**：check_style 0 issue、markdownlint 0 error（修 OIR 列表符号 - → *）、check_math 0、check_academic --strict OK。
* **状态**：mandeville s3_checked（commit a003522a），入 R-main-20261108 评审线（session-handoff §6），本会话不推进 r1–r3。
* **M 批在途**：2 条均在评审线（mandeville、moral-demands-permissions）；待译主线为 6 条 pending + 125 条未建任务。

## 7. 接管复算与归属纠正（2026-11-09 02:4x UTC+8，M-main-20261109）

**指令**：用户再次要求「计算、同步、纠正目前 M 词条的翻译进度，不使用子代理；现在由你负责翻 M」。本会话以新身份 M-main-20261109 接管 M 批，重算不引用旧记录。

**方法**：`script/m_audit_20261109.py`（五方对账：SUMMARY × baseline × yuanwen × 成稿 × 任务 JSON × 账本 × git 脏/未提交）+ `script/m_structure_check_20261109.py`（结构三检：H1↔SUMMARY、version_pin、基线/镜像覆盖）。

### 7.1 复算结果（2026-11-09 02:4x UTC+8）

| 项 | 数值 | 依据 |
| --- | --- | --- |
| 正式词条 | 139 | SUMMARY `m/` 190 行 = 正式 139 + 别名/占位 51 |
| 英文基线 | 139/139 | `baseline/entries.json` 逐 slug 命中 |
| 转换镜像 | 139/139 | `yuanwen/m/<slug>.md` |
| 成稿（>1 行） | 9 | 全部账本满段（见 §7.2 表） |
| done | 6 | marsilius-inghen、mathematics-inconsistent、modesty-humility、molyneux-problem、montesquieu、moral-responsibility-empirical |
| s3_checked（评审线） | 2 | mandeville、moral-demands-permissions |
| drafted | 1 | marsilius-padua（本次收编） |
| pending | 5 | mathematical-practice、model-organisms、montessori-maria、moral-learning、music |
| 未建任务 | 125 | 139 − 14 |
| **待译主线** | **130** | 139 − done 6 − 评审线 2 − 已 draft 1 |

结构三检零缺陷：139 条 H1 与 SUMMARY 条目文字逐字符一致（0 偏差）；139 条基线、139 条镜像齐备；14 份任务 JSON `version_pin`（pubinfo + 存档版 + SHA-256）无缺失；9 份成稿账本段数全部满填（88/88、80/80、74/74、34/34、91/91、36/36、57/57、63/63、107/107）。

### 7.2 偏差与处置

1. **marsilius-padua 状态滞后（唯一账实偏差）**：工作区遗留未提交初译（287 行、账本 74/74、2026-11-09 01:51 前后落盘），任务状态仍停 `cleared`。三重验收后收编——`lq.py check` 守恒 HARD=0（74 段）；`lq.py compose` 去 NOTE 行后与成稿逐字符 diff=0；抽检段 1（导语）与段 30（DP 定义引块）对照 yuanwen 忠实无增删。`task_ops advance --step draft` 留痕，commit `bf1bcf2b`（仅 3 个 M pathspec 文件）。
2. **认领归属纠正**：`ledger.json` 的 m 批 `claimed_by` 停在 M-main-20261108。处置：`campaign.py claim m --session M-main-20261109 --force` + `advance m translate --note`（复算口径写入注记）。
3. **PROGRESS.md**：`tools/progress.py` 重生成（生成物，不手改）；全局计数含并行会话在途任务，M 行以本表为准。
4. **评审线边界**：mandeville、moral-demands-permissions 属 R-main 评审线（session-handoff §6），本会话不推进 r1–r3；其余 s3_checked 收口后同样交评审线。

### 7.3 本会话作业序

1. marsilius-padua：drafted → s1（逐段核销 + 相关词条 NOTE 项「political philosophy: medieval Augustine」对 SUMMARY 回核）→ s2 → s3 → 交评审线。
2. 5 条 pending 按源文体量升序开工：model-organisms（94.7 KB）→ music（108.4 KB）→ moral-learning（111.5 KB）→ montessori-maria（125.2 KB）→ mathematical-practice（153.8 KB）；每条 `clear` → 账本 init → 双版分批落盘 → `lq.py check` → compose → 四检 → s1/s2/s3。
3. 125 条未建任务按 SUMMARY 序 `task_ops create --kind retranslate` 后逐条推进。
4. 收工前 `python tools/check_all.py` 全绿；账本与任务状态同步提交。

### 7.4 首批实作进展（2026-11-09 03:0x–04:0x UTC+8）

* **model-organisms 启动**：`task_ops clear`（baseline gate hash_ok）→ `lq.py init`（104 段 = body 100 + oir 4，biblio 照录 109 条）。
* **账本双版落盘 28/104 段**（段 1–28），分批提交：`b0534ebb`（段 1–14）、`20e52073`（段 15–28）；`lq.py check` 已填段残余 0（唯一 HARD 为段 11：初稿把源文斜体图题写成 `**`，已改回 `*图 1。*`，粗体化留给 compose 后 `italic_to_bold_cjk`）。
* **术语先行**：登记 25 行（模式生物学术语 13 + 表征论术语 12：实验生物、非模式生物、模型载体、表征范围/目标、外推、基因组作图/测序、NIH、HGP、威斯塔研究所、模式系统、本领库、最低限度/复杂模式生物、可操作性、替代物、探索性模型、负模型、解释键、DEKI 框架、标本、基础认知、系统发生亲缘关系、反思平衡）。
* **门禁**：`tools/check_all.py` 7/7 全绿；`tools/progress.py` 重生成（M 行 139/139/14/6 不变，model-organisms 由 pending 转 cleared）。
* **下一批次断点**：模型生物段 29 起（§2.2 范例与替代物 → §3 起）；余 76 段。

### 7.5 续作记录（2026-11-09 04:3x–05:1x UTC+8，goal round 1）

* 账本续译至 **70/104 段**：批次 3（段 29–42：范例与替代模型、探索性模型、负模型；`739538bd`）、批次 4（段 43–56：物质性与标准化、实验系统、本领库；`292a119c`）、批次 5（段 57–70：表 1a/1b/1c 本领库要素表、生物选择与 Krogh 原则；`25fc61c1`）。
* 术语登记再补 34 行（范例、替代模型、替身模型、替代性、内表型、Krogh 生物、调整型发育、细胞谱系、细胞凋亡、电压钳、活体测定、视角建模、生物人工物、认知物/技术物、实验系统、种质资源中心、生态型、饲养管理、共同构成的）。
* 已填 70 段全部残余 0（`lq.py check` 仅报未填段缺失）；表格段按 rules/02 居中形态（`:---:`）落盘。
* **下一断点**：段 71 起（§4.2 扩展理由范围 → §5 大数据 → 参考文献/学术工具/其他网络资源）。
