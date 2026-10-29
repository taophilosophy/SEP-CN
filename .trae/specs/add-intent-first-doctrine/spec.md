# 新增“知难行易”软件工程理论并落实为全局规则 Spec

## Why

2026-10-29 用户指令：新增软件工程理论并落实为全局规则；从一刻哲学中提取“知难行易”——必须先明白自己的任务方向与目标，手段是次要的；必须清楚明白地理解用户到底要干什么。

现状缺口：

- **理论侧**：`rules/reference/engineering-doctrine/` 已有 32 条总纲的工程转译，但“方向先于手段”的依据散落在 `00-philosophy.md` §3 六问、§8 推论、补充总纲 31、十七 历史存在论、二十一 革命与改革，没有独立文档，无法被直接引用与验收。
- **规则侧**：`rules/` 是全局规则唯一存放处，但 01–07 均未规定“开工前必须先确认任务方向、目标与验收判据”；`AGENTS.md` 开工五分钟从 git 状态与门禁开始，直接进入执行。
- **后果**：AI 会话与贡献者容易出现“先动手后理解”“手段替代目标”“猜测式实现”“用工具或流程证明完成”等失败模式，返工成本由后续会话与用户承担。

## What Changes

- 新增参考理论文档 `rules/reference/engineering-doctrine/00b-zhinan-xingyi.md`：把“知难行易”作为**项目侧提炼**（明确非源文原文），依据 00a §2 第十七、二十一条、§3 补充总纲 31 与 00-philosophy §3/§6/§8，给出知/行分层定义、四条命题、开工四问、反模式、方向声明卡与失效条件。
- 新增约束性规则 `rules/08-intent-first.md`：方向声明先行、需求不明先问不猜、手段后置且可替换、以验收判据而非工具/流程验收完成、可逆快行/不可逆先知后行、知—行闭环、形式主义自检。
- 新增 ADR `rules/adr/0018-知难行易全局规则.md`，记录决策与代价（每任务一次复述成本），并登记 `rules/adr/README.md` 索引。
- 同步索引与入口：`rules/README.md`（规则索引 + 规则地图 `rules/01-08` + 快速判例）、`AGENTS.md`（开工第 0 步、硬约束速览、按任务类型必读）、`rules/reference/engineering-doctrine/README.md` 与 `NOTICE.md`（变更记录）、`specs/004-engineering-doctrine/spec.md`（复审记录追加本次变动，跨界修改理由见 ADR-0018）。
- **修订宪法 v1.2.0**：在 `.specify/memory/constitution.md` 追加第七条核心原则“VII. 知难行易（先明方向，后择手段）”（I–VI 编号与内容不动，避免破坏既有引用），版本号 1.2.0、Last Amended 2026-10-29；提交信息注明“修订宪法 v1.2.0”。
- **BREAKING**：无（不改变既有规则编号、工具行为或产物格式；08 与宪法 VII 均为新增编号）。

## Impact

- Affected specs: `specs/004-engineering-doctrine/spec.md`（仅复审记录追加一行）
- Affected code: 无代码变更；`rules/` 规则文本、`AGENTS.md`、参考方法论目录、项目宪法
- 受影响文档：`.specify/memory/constitution.md`、`README.md`、`CONTRIBUTING.md`、`rules/README.md`、`rules/06-governance.md`
- 受影响会话：全部（翻译、结构、管线、站点、治理）——开工流程新增一次方向确认

## ADDED Requirements

### Requirement: 知难行易理论文档

系统必须提供 `rules/reference/engineering-doctrine/00b-zhinan-xingyi.md`，作为“知难行易”的参考方法论唯一出处，且满足：

1. **来源可核验**：逐条标注 00a 的条目与章节位置；不得把“知难行易”写成源文原文或伪造引文；命名出处仅作溯源注记，不作论证依据。
2. **内容完整**：知（方向层）与行（手段层）的定义；四条命题——方向错误时执行力放大损失、手段可替换、知是行的前提而非替代、形式主义手段表演；开工四问（谁要什么 / 为什么现在 / 什么算完成 / 什么不做与谁承担代价）；六类反模式；方向声明卡模板；失效条件与复审触发（与 doctrine §9 自反条款一致）。

#### Scenario: 读者核对来源

- **WHEN** 任何会话阅读 00b 的任一命题
- **THEN** 该命题都能在 00a 或 00-philosophy 找到对应依据条目，且明示“项目侧提炼”而非源文原文

### Requirement: 约束性规则 08（任务意图与方向先行）

系统必须提供 `rules/08-intent-first.md`，适用于全部会话与任务类型，条文至少覆盖：

1. 开工前方向声明（意图复述、目标/非目标、验收判据），写入任务记录或 spec；
2. 需求不明先问不猜；临时假设显式标 `[假设]` 且验证前置；
3. 手段后置且可替换：说明选择理由、替代方案与替换条件；禁止以工具/流程使用作为完成证据；
4. 以验收判据加证据定义完成，不以提交数、文档长度或工时衡量；
5. 可逆决策快行、不可逆决策先知后行（结构重排、批量改写、发布等衔接 `rules/06` 破坏性动作前置条件）；
6. 知与行的闭环：明确方向后立即执行最小可验证步骤，不以“未想清楚”为由停滞；
7. 收工自检：本次工作改变了哪个决策、产物或门禁，否则视为形式主义。

#### Scenario: 接收含糊指令

- **WHEN** 用户指令存在两种以上合理解释或未给验收判据
- **THEN** 会话先复述意图并提问确认，在得到答复前列出候选方案与各方案影响，不直接实施

#### Scenario: 手段替代目标

- **WHEN** 会话以“已运行某工具、已走完某流程、文档已写”作为完成理由
- **THEN** 按规则 08 第 4 条驳回，须给出验收判据与证据

### Requirement: 宪法修订 v1.2.0（新增第七条原则）

`.specify/memory/constitution.md` 必须新增 **VII. 知难行易（先明方向，后择手段）**，内容至少覆盖：

1. 任务方向、目标、非目标、验收判据与代价承担者（知）先于工具、流程与实现路径（行）；
2. 手段是可替换的次要变量，不得反客为主；不以工具使用、流程走完或文档篇幅判定完成；
3. 需求含糊时先问、先复述、先求证，禁止猜测性实施；
4. 可逆决策允许快速试错，不可逆决策必须方向先行并留证据；
5. 与本宪法 I（零信任）、IV（流程先行）衔接，操作性展开指向 `rules/08-intent-first.md`。

I–VI 条的编号与内容保持不变；版本号为 1.2.0，Last Amended 为 2026-10-29。

#### Scenario: 宪法版本与原则计数一致

- **WHEN** 审阅者打开宪法、`rules/README.md`、`README.md`、`CONTRIBUTING.md`
- **THEN** 宪法为 v1.2.0 且含七条原则，权威层“核心原则”表述均为七项并列出“知难行易”，无“六项”残留（历史发布说明与历史 ADR 除外）

### Requirement: 治理登记与索引一致

系统必须完成全局登记，使规则体系自洽：

1. `rules/adr/0018-知难行易全局规则.md` 存在且符合 ADR 记录格式；`rules/adr/README.md` 索引含 0018；
2. `rules/README.md` 规则索引含 08，规则地图“约束性规则”为 `rules/01-08`，快速判例含方向声明判例；
3. `AGENTS.md` 开工五分钟含“方向确认”步骤、硬约束速览含“知难行易”、按任务类型必读表指向 `rules/08`；
4. `rules/reference/engineering-doctrine/README.md` 目录表含 00b，`NOTICE.md` 变更记录含 2026-10-29 行；
5. `specs/004-engineering-doctrine/spec.md` 复审记录追加本次变动（跨界修改理由见 ADR-0018）；
6. `rules/01`–`07` 各任务入口条款、`tasks/README.md`、`specs/005` 与 `specs/008` 会话开工卡同步方向声明要求。

#### Scenario: 索引核对

- **WHEN** 审阅者打开 `rules/README.md` 与 `rules/adr/README.md`
- **THEN** 08 与 0018 均已登记，链接指向真实文件，规则地图编号范围与磁盘一致

### Requirement: 质量门通过

系统必须在交付前通过既有门禁与体例检查，不新增工具：

- `python tools/check_all.py` 七项全绿（结构/分类/单体/垃圾/术语/学术规范/单测）；
- 新增与修改文件不超过 300 行/30KB（规则文本阈值），UTF-8 无 BOM、LF 换行；
- 中文正文引号仅 “”‘’，不出现直角引号（U+300C–U+300F）；代码块内容不篡改。

#### Scenario: 收工验收

- **WHEN** 全部改动完成
- **THEN** `check_all.py` 汇总“全绿”，且文档大小与引号体例检查无告警

## MODIFIED Requirements

### Requirement: 全局规则索引（既有）

`rules/README.md` 的规则索引与规则地图必须覆盖全部约束性规则文件。新增 08 后，索引表须新增一行，规则地图“约束性规则”范围由 `rules/01-07` 更新为 `rules/01-08`。

#### Scenario: 新增规则后的索引

- **WHEN** `rules/08-intent-first.md` 落地
- **THEN** `rules/README.md` 两处同步更新，无遗漏、无死链

### Requirement: 宪法原则计数表述（既有）

`README.md`、`CONTRIBUTING.md`、`rules/README.md`、`rules/06-governance.md` 与 `AGENTS.md` 中“六项核心原则 / 宪法六原则”的表述必须同步为七项，并列出新增的“知难行易”；历史文档（`RELEASE-NOTES.md`、ADR-0016 等）按当时事实保留，不改写。

#### Scenario: 计数表述检索

- **WHEN** 检索“六项核心原则”“宪法六原则”
- **THEN** 仅历史文档命中，权威层与入口文档无残留

## REMOVED Requirements

无。
