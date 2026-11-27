# 主线与节点全表

**日期**：2026-11-17｜**性质**：清单（只读核对，不含实施）
**依据**：`rules/04-translation-workflow.md` 全文、`tools/task_ops.py` 的 `ORDER`／`STEPS`、`specs/042` v3、`jian-yi-shu/journal-schema.json`
**用途**：实施 W2（落 `rules/pipeline.json`）时的直接输入；亦为“某个环节插在哪、插完谁要重走”的判定表

---

## 一、三条主线，不要混成一条

| 主线 | 回答什么 | 载体 | 节点数 |
|---|---|---|---|
| **数据主线** | 一份译文从抓取到验收经过哪些工位 | `pipeline.json` 的 `nodes` | 18 |
| **调度主线** | 哪一批、谁认领、何时开工 | `ledger.json` ＋ `tasks/manifests/` ＋ `claim` | 4 层 |
| **返工主线** | 改进判据或改错时，哪些条目的哪一段重走 | `journal` 的 `attempt` | 按需分支 |

数据主线是唯一的“主干”；调度挂在条目集合上，返工挂在分支上，两者都不改主干顺序。

---

## 二、数据主线：三段 18 节点

### Seg1 英语文本提取（5 节点）

| # | id | 类型 | 强制 | 输入 | 作业 | 判据命令 | 产物 | 降级档 |
|---|---|---|---|---|---|---|---|---|
| 1 | `P1` | pipe | 是 | 上游 SEP 页面 | 抓取 HTML，算 SHA-256 | `fetch_audit` | `en/<slug>/index.html` ＋ `lock` 事件 | replace |
| 2 | `P2` | pipe | 是 | HTML | 转英文 markdown，3.1 格式差异以虚拟补丁打入 | `check_en_patches`、`divergence` | `yuanwen/<letter>/<slug>.md` | replace |
| 3 | `P3` | pipe | 是 | P2 的 markdown | 渲染回结构，反校 HTML 的节层级／列表层级／表列数／脚注序号 | `check_yuanwen_fidelity` | 反校报告 | replace |
| 4 | `s0` | pipe | **是** | `en/` ＋ `yuanwen/` | 双轴：HTML 本体核查（真实性／截断／死链／公式／表格／锚点）＋镜像轴保真（逐段人审、书目逐条计数） | `en_integrity`、`en_source_audit`、`divergence` | `s0` 事件 | replace |
| 5 | `F1` | format | 是 | 段 1 全部产物 | 段内格式闭合 | 零差异亦须记录 | `F1` 事件 | widen |

### Seg2 中文翻译（5 节点 ＋ 1 个入口动作）

| # | id | 类型 | 强制 | 输入 | 作业 | 判据命令 | 产物 | 降级档 |
|---|---|---|---|---|---|---|---|---|
| — | `cleared` | 状态 | 是 | 可信英文基线已登记 | 置空旧译文 | 无判据（可由 git 回溯） | `cleared` 事件 | — |
| 6 | `P4` | stage | 是 | `yuanwen` ＋ 术语库 ＋ 全局勘误表 | 摘录术语、注入 `errata` 参考读法与标题 | `check_terms` | 术语摘录 ＋ 提示词 | tighten |
| 7 | `draft` | stage | 是 | P4 产物 | 初译：step1 忠实版 ＋ step2 语言优化版，双版留档 | — | 译文 ＋ 双版账本 | replace |
| 8 | `s1` | stage | 是 | `draft` ＋ `yuanwen` | 逐节核销漏译／错译／事实错误（人名、年代、编号）；残留外文碎片为 0 | `check_pairs` | 对照记录 | tighten |
| 9 | `s2` | stage | 是 | `s1` 产物 | 去欧化、倒装、死译；语体确认（现代汉语学术书面语） | `check_prose`、`check_style` | 修改 diff ＋ 语体结论 | tighten |
| 10 | `F2` | format | 是 | 段 2 全部产物 | 段内格式闭合 | 零差异亦须记录 | `F2` 事件 | widen |

`cleared` 只在 `retranslate` 序列存在；`update` 序列无此态（上游修订不清空，只改变更段）。

### Seg3 审阅校对（8 节点）

| # | id | 类型 | 强制 | 输入 | 作业 | 判据命令 | 产物 | 降级档 |
|---|---|---|---|---|---|---|---|---|
| 11 | `s2.4` | stage | **是** | `s2` 产物 | 三轴：术语（`check_terms`）→ 体例（`check_style`）→ 勘误（`check_pairs --gate`） | 同左，顺序挂 | 三轴记录 | tighten |
| 12 | `s2.5` | stage | **是** | `s2.4` 产物 | 两轴：逐段比较格式与内容 → 全局比较（节集合、脚注键位总数、书目条数、密度） | `check_math_zh`、`check_quotes`、`check_tables_images`、`check_academic --strict` | 审计记录（`changes:` 开头） | tighten |
| 13 | `X1` | pipe | **否** | `s2.5` 产物 | 形态横向清账：跨词条形态正典化（节名、行形态、空格、分类子标题） | 告警级；残余 0 或全部登记豁免 | 清账凭证 | replace |
| 14 | `s3` | stage | 是 | X1 之后 | 体例三校：引号、空格、连接号三形、表号表题、顿号、题注 | `check_style`、markdownlint、`check_academic` | s3 凭证（含适用规范基线结论） | tighten |
| 15 | `R1` | review | **是** | `s3` 产物 | 初审：Verity（受众适切性）抽查 ＋ 语体签字 | 需独立于译者 | 自审记录 | replace |
| 16 | `R2` | review | **是** | `R1` 产物 | 复审：逐句回核原文与逻辑 | 问题单（位置＋改前改后，禁机械批量） | 复核记录 | replace |
| 17 | `R3` | review | **是** | `R2` 产物 | 终审：终稿验收 ＋ CI 全绿 | `--mandate` 必填（ADR-0054） | 验收签字 | replace |
| 18 | `F3` | format | 是 | 全部 | 段内格式闭合 | 零差异亦须记录 | `F3` 事件 | widen |

---

## 三、可插位：18 个节点 = 19 个插入位

插入只需在 `pipeline.json` 加一行（`prev` 指向左邻），**既有节点编号不变**。每个位置的代价是“下游谁要重走”：

| 插入位 | 典型用途 | 下游重走面 | 依据 |
|---|---|---|---|
| P1 之前 | 上游可用性预检 | 全链 | 改输入 |
| P1–P2 | HTML 实体与编码规范化 | 全链（实体被修正则 P2 结果变） | 改输入 |
| P2–P3 | 表格结构规范化 | **无**（走虚拟补丁） | 只改格式 |
| P3–s0 | 图注编号与 alt 文本核对 | 无（原地补记录） | 只补记录 |
| s0–F1 | 段 1 格式项 | 无 | 段内格式 |
| F1–P4 | 双语文档基线比对 | Seg2／Seg3 全重走 | 改译文输入 |
| P4–draft | 提示词增补（如 errata 注入） | `draft` 起重走 | 改生成条件 |
| draft–s1 | 双版账本完整性校验 | `s1` 起重走 | 改输入 |
| s1–s2 | 语体规则收紧 | `s2` 起重走 | tighten |
| s2–F2 | 段 2 格式项 | 无 | 段内格式 |
| F2–s2.4 | 体例口径统一 | `s2.4` 起重走 | tighten |
| s2.4–s2.5 | 术语主形复核单列 | 无（原地补记录） | 只补记录 |
| s2.5–X1 | 跨词条统计对账 | 无 | 只补记录 |
| X1–s3 | 形态项前置 | `s3` 起重走 | 改输入 |
| s3–R1 | 验收清单增项 | `R1` 起重走 | replace |
| R1–R2 | 逻辑链专项 | `R2` 起重走 | replace |
| R2–R3 | 交付打包检查 | `R3` 起重走 | replace |
| R3–F3 | 交付物清单核对 | 无 | 段内格式 |
| F3 之后 | 发布后置（站点、索引、登记册） | 无（不属产品线） | 见 §五 |

**判据只有一条**：新节点的判据能否让下游既有 `pass` 产生新的失败。能则重走，不能则原地补记录。

---

## 四、调度主线（4 层，挂在条目集合上）

| 层 | 载体 | 粒度 | 谁写 | 与数据线的关系 |
|---|---|---|---|---|
| 战役 | `specs/005-translation-campaign/ledger.json` | 全库 1,885 条 | `campaign.py` | 决定“哪些条目进入数据线” |
| 波次 | `tasks/manifests/2026-*-batch*.json` | 每批数十条 | 批次计划书 | 决定“这批走多远” |
| 认领 | `claim`（A–Z 字头 ＋ 条目） | 条目或 `(entry, section)` | 会话自行认领 | 决定“谁在哪个节点上写” |
| 分支 | `journal` 的 `attempt` | 受影响条目集合 | `journal_ops rework` | 决定“返工不覆盖主干” |

四层之间**只有引用关系，没有包含关系**：一个波次可跨字头，一个分支可跨波次。

---

## 五、返工主线：接入点与合并规则

返工从任一节点开分支，**不改写主干事件**：

```
main:    P1 → P2 → P3 → s0 → … → s3 → R1 → R2 → R3
                                    ↘
attempt-a:                          rework{from_node:s2.4} → 重走 s2.4…R3 → merge
```

| 规则 | 内容 |
|---|---|
| 起点 | `from_node` 可为任意已 `pass` 节点 |
| 终点 | 必须过 `mandatory_minimum`（`s0`、`s2.4`、`s2.5`、`R1`、`R2`、`R3`）方可 `merge` |
| 冲突 | 同一节点再次 `rework` 时并列新 `attempt`，不覆盖旧分支 |
| 驳回 | `merge{verdict:reject}` 保留分支与理由，供后续复查 |
| 范围 | `scope` 限定条目集合，分支可只作用于 1 条 |

---

## 六、本轮核对发现的三处结构缺口

### 缺口一：`s0` 与 `P1–P3` 的相对位置在规则里无法表述（已补）

`rules/04` 写“HTML 在前”，但 `P1`／`P2`／`P3` 不在状态机里，规则无从规定 `s0` 相对它们的位置。逻辑上必须先有 P2 的 `yuanwen` 才能做镜像比对，先有 P3 的反校才能信任 `yuanwen`——即 `P2 → P3 → s0`。这条顺序此前只存在于工具实现里，没有条文。本轮已在 `journal-schema.json` 用 `prev` 显式固定。

### 缺口二：`X1` 有作业、无状态（有意为之，但代价明确）

ADR-0047 明文“不属于六道、不改任务状态机”。后果是它既不能被 `saturate` 判定，也不能被 `progress` 统计——即“这条清账做过没有”在任务视图里查不到，只在 `specs/030` 的批次凭证里。这是设计选择，不是疏漏；代价是清账覆盖率无法机检。

### 缺口三：`update` 序列是死路径（零任务使用）

`ORDER` 定义了 `update` 的 11 态序列，但 1,199 条任务的 `kind` 只有 `retranslate`（1,197）、`glossary-maintenance`（1）、`daily-check`（1），无一为 `update`。上游修订实际走 `reopen --upstream-sync` 打回 `pending` 后按 `retranslate` 重走。该序列应删除，否则每次改 `ORDER` 要同步维护一条无人走的分支。

---

## 七、与现行 `rules/04` 的差异汇总

| 项 | 现行 | 本表 | 性质 |
|---|---|---|---|
| 节点总数 | 11 个状态 ＋ 1 影子环节 ＋ 3 工具节点 | 18 个统一节点 | 归一 |
| `P1`–`P3` | 工具实现，无状态、无条文位置 | 显式节点，有 `prev` 与判据 | 补条文 |
| `s0` 位置 | “cleared 之后、draft 之前”（相对作业序不明） | `P3` 之后、`F1` 之前 | 补顺序 |
| `X1` | 不入状态机 | 节点，`mandatory: false` | 保留不入，但可统计 |
| `F1`／`F2`／`F3` | 无 | 三个段末闭合节点 | 新增 |
| `update` 序列 | 定义但零使用 | 建议删除 | 废弃 |
| `cleared` | 状态机内 | 保留为“仅入口态”，非作业节点 | 归类 |

---

## 附：机读形态

`jian-yi-shu/journal-schema.json` 的 `nodes` 已同步为 18 项，`prev` 链自 `P1` 至 `F3` 闭合无悬挂；`mandatory_minimum.nodes = ["s0","s2.4","s2.5","R1","R2","R3"]`；`state_only_entry` 单独登记 `cleared`。
