# 任务清单：064 全流程全要素审计与规范化

- 输入：`specs/064-flow-spec-audit/spec.md`（rev 10）、`plan.md`、`results/axioms-v3.md`
- 状态：**1 项已验证（T131）；1 项部分执行（T130，机器面完成、人工定性未完）；93 项未开始**。合计 95 个编号工作项。用户 2026-11-26 裁定“暂不开工”；本清单是待批施工图
- 格式：`[ID] [P?] [阶段] 描述（含文件路径与验收）`；`[P]`＝不同文件、无依赖，可并行
- **粒度规则**：S-1 的 `T142–T161` 是工作包，不是可直接执行的原子任务；开工前须按 T130–T141 的“件×站段”模板拆为原子任务（从下一可用号顺序分配，不预写占位号）。T140 的 sg-01／sg-02、T141 的 sg-03 及任何 sg-03 行均须单列并检查 mandate。工作包不得整体勾选
- **门禁编号**：不预写“第 N 项”；以 `check_all.py --list-gates` 实际输出为准
- **ADR 编号**：不预占；实施前重读 `rules/adr/` 尾部取实际最大号

## 阶段 S-1 端到端试金石（2026-11-26 批准；**按件按段拆任务，不一次性**）

> 名单引用 `specs/060` §5.4；按现状 22 节点跑（不先实施方案 B），用现有 Python 链。一件一段一任务、各自收口；上表未勾满不进入下一段。产出 findings 回填 spec §18.4。
> 优先级：先 habermas 走完，再 logic-preference，再 environmental-aesthetics；第二／三梯队每件单列一个任务，按轴启用。

### habermas（第一梯队 1/3）

- [ ] T130 [S-1] ex-04 源审计——**机器面完成**（hard=0／warn 5，`results/e2e-habermas*.json`）；**人工定性未完**：2 个候选待核、1 个疑似真错待回源确认、3 个误报待按 rules/11 §5.3 复核留痕；未满足“候选总数／豁免计数／定性结论”三段证据，不得勾
- [x] T131 [S-1] G13 豁免清单落地（`rules/11-source-side.md` §5.3）——**已完成**（2026-11-26），本任务仅作勾销与规则地图登记；配套 ADR 留待治理轮
- [ ] T132 [S-1] tr-02 样章（§1–§2，约 3,000 字）：验证段落账本、step1／step2、术语注入——**前置：T130 人工定性完成**；验收：账本守恒、样章可读、候选逐条定性
- [ ] T133 [S-1] tr-02 全量（余下各节，分 4–6 批 checkpoint）——验收：全文入库、账本段落数守恒
- [ ] T134 [S-1] tr-03 一校（对照英文源逐节核销）——验收：对照记录；残留外文 0
- [ ] T135 [S-1] tr-04 二校（语体、反欧化）——验收：`check_prose` 告警清零或逐条豁免
- [ ] T136 [S-1] rv-01 术语与勘误（术语轴＋体例轴＋勘误轴）——验收：三段 evidence
- [ ] T137 [S-1] rv-02 全局一致性（两轴比较校对）——验收：两轴记录＋机检输出
- [ ] T138 [S-1] **[工作包]** rv-03–08 六轴（q1→q6 顺序固定）——执行前按轴拆六个原子任务；验收：各轴凭证落 `state/axis/`
- [ ] T139 [S-1] rv-09 体例终校——验收：`check_style` 0 issue
- [ ] T140 [S-1] **[工作包]** sg-01／sg-02（初审＋复审）——执行前按节点拆两项；验收：自审与复核记录
- [ ] T141 [S-1] sg-03 终审（需用户显式指定 `--mandate`）——验收：CI 全绿＋签字；不得因试金石批准自动执行

### logic-preference（第一梯队 2/3；工作包，须按站段拆分）

- [ ] T142 [S-1] ex-04 源审计——验收：同 T130 口径，含候选逐条定性
- [ ] T143 [S-1] tr-02 样章（§1–§2）——验收：公式定界符与 362 处行内公式样本无损
- [ ] T144 [S-1] tr-02 全量——验收：全文入库
- [ ] T145 [S-1] 校次链 tr-03／tr-04——验收：同 T134／T135
- [ ] T146 [S-1] rv-01／rv-02／rv-09——验收：同 T136／T137／T139
- [ ] T147 [S-1] 六轴 rv-03–08（重点 q2 逻辑、q5 计量、q6 标点）——验收：各轴凭证
- [ ] T148 [S-1] sg 链——验收：sg-01／sg-02 分列；sg-03 另核 mandate

### environmental-aesthetics（第一梯队 3/3；工作包，须按站段拆分）

- [ ] T149 [S-1] ex-04 源审计（重点：369 条文献条目）——验收：书目计数
- [ ] T150 [S-1] tr-02 样章（§1–§2）——验收：文献键位与脚注配对
- [ ] T151 [S-1] tr-02 全量——验收：全文入库
- [ ] T152 [S-1] 校次链与 rv 链（重点 q1 引文）——验收：引文 hash 锁定
- [ ] T153 [S-1] sg 链——验收：同 T141；分节点执行

### 第二梯队（工作包；核心 3 件至 sg-02 后启用，执行前须拆站段）

- [ ] T154 [S-1] `i/imprecise-probabilities`（14 类构件 12 类）全流程——验收：构件无丢失；拆为原子任务后方可执行
- [ ] T155 [S-1] `a/action`（长文＋引文双密集）全流程——验收：同第一梯队口径；拆为原子任务后方可执行
- [ ] T156 [S-1] `a/axiom-choice`（530 行内公式＋8 块＋4 表）全流程——验收：公式与表无损；拆为原子任务后方可执行
- [ ] T157 [S-1] `n/newton-principia`（36,082 汉字＋3 图）全流程——验收：图与版式；拆为原子任务后方可执行

### 第三梯队（工作包；单项极值，按轴专项启用，执行前须拆站段）

- [ ] T158 [S-1] `l/logic-dynamic`（行内公式 602 处）——验收：公式定界符全配对；拆后方可执行
- [ ] T159 [S-1] `j/japanese-aesthetics`（图 33 幅）——验收：图注与 alt 齐备；拆后方可执行
- [ ] T160 [S-1] `k/kokugaku-school`（表 48 行）——验收：表格结构完整；拆后方可执行
- [ ] T161 [S-1] `d/digital-art`（唯一代码块）——验收：代码块闭合；拆后方可执行

### 汇总与回填（全部条目完成后）

- [ ] T162 [S-1] 汇总 `results/e2e-findings.md`（G13+，标阻断／非阻断）——验收：与各件记录逐条对应；不得把工作包当完成
- [ ] T163 [S-1] **案 B 复核**：据 ex-05／tr-05 实际记录作 13 项×既有判据矩阵，并核 P12 段尾闭合——验收：保留／迁入／已覆盖／证据不足逐项有结论；**不得预写“净增 11 项”**；本任务结论前案 B 仍 blocked
- [ ] T164 [S-1] **stage_of 联调**：逐站核对阶段派生（063 CT3／CT8 候选）——验收：差异有解释并回写 063，不改实现迁就模型
- [ ] T165 [S-1] 回填 spec：findings → G 清单 → 后续工作包顺序——验收：spec §2.7／§18.4 更新，状态与证据一致

## 阶段 S0 契约测试框架（迁移的必要证据之一，非充分）

- [ ] T001 [P] [S0] 建 `tools/golden/` 与 `run_golden.py` 骨架：按 `meta.json` 的 `compare_mode` 选择 byte／canonical-json／artifacts；仅声明 byte-contract 的输出逐字节——验收：假 tool 正反例各一，且 JSON 键序变化不应误红。
- [ ] T002 [P] [S0] 定 `expected.json`／`meta.json` 格式（compare_mode、exit_code、result schema、artifacts、commit、tool_version、platform、dynamic_fields）——验收：schema 文档写入 `tools/golden/README.md`。
- [ ] T003 [S0] 录制模式 `run_golden.py --record <tool>`（跑现行 Python 版并落 expected）——验收：`check_doc_size` 录制成功且回放通过。
- [ ] T004 [S0] 实现 canonical-json 比对（键序、换行、显式动态字段；浮点容差须由 schema 指定，不擅自容忍）——验收：同输入两次结果相等，注入时间戳不误红。

## 阶段 S1 登记表候选（G23 未修正前 blocked）

- [ ] T010 [P] [S1] 写 `baseline/registry-long.json` 契约草案 **（不落文件）**：15 个字段、13 个无条件必填、条件必填规则、active-only path 唯一——验收：schema 评审通过；G23 关闭后方可实际建表。
- [ ] T011 [P] [S1] 写 `state/registry-temp.json` 契约草案（不入库；path 相对化优先）——验收：与 long 表 schema 差异仅 kind／TTL／machine 注记。
- [ ] T012 [S1] 实现 `registry.py register` 设计（sha／size／时间；id 递增；拒重 active path）——验收：设计测试用例，不执行写库。
- [ ] T013 [S1] 实现 `registry.py verify` 设计（active／expired／orphaned／superseded／pruned；时间与时钟显式）——验收：删除保护件的负向样本在测试沙箱报 orphaned。
- [ ] T014 [S1] 实现 `registry.py prune` 设计（默认 dry-run；`--go` 仅白名单、二次确认、可回退；不自动删）——验收：测试沙箱二次运行幂等，且未确认时不写盘。
- [ ] T015 [S1] 首批登记清单草案：`catalog.json`、`en-errata/en-errata.md`、`en-patches/INDEX.json`——验收：理由与单源边界评审；**不实际登记**。
- [ ] T016 [P] [S1] 写 `tools/golden/registry/` 用例（register→verify→prune 全链，沙箱）——验收：黄金测试通过；不触碰真实 baseline。

## 阶段 S2 清理检查点候选（冻结）

- [ ] T020 [S2] 扩展 `tools/clean.py` 契约：`--check` 默认 0；`--strict` 仅对保护件缺失／越界风险退 1；消费登记表为可选项——验收：干净树 0，注入 `*.tmp` 默认仍 0 并报告；`--strict` 对受保护缺失退 1。
- [ ] T021 [S2] 扫描面扩至 `target/`、`.ruff_cache`、`.mypy_cache`、`.pytest_cache`、`.vitepress/cache|dist`——验收：各目录占位文件均被识别且分类正确。
- [ ] T022 [S2] 评估 `check_all.py` GATES 增“缓存与临时物”——验收：先给预期命中量级与本地／CI 同档证明；编号由 `--list-gates` 实际输出决定，不预写 22。
- [ ] T023 [P] [S2] `.gitignore` 审计补齐（`target/`、`__pycache__/`、`*.pyc`、`.vitepress/cache`、`.vitepress/dist`）——验收：`git status` 不出现这些路径。
- [ ] T024 [P] [S2] 评估 `checks.yml` 是否需独立 `clean --check` 步骤；若 GATES 已覆盖则不重复——验收：不手写重复矩阵；工作流变更同步 rules/05。

## 阶段 S3 Python 现代化（受控变更，非零风险）

- [ ] T030 [P] [S3] 建 `pyproject.toml` 草案（requires-python `>=3.15`；区分 runtime／dev／optional；`cryptography`、`playwright` 列为可选）——验收：`uv sync` 在临时环境成功，且不改运行时行为。
- [ ] T031 [P] [S3] `ruff format` 按目录分批（先 lib 层），每批单独提交——验收：该目录 diff 仅格式；`check_all` 全绿；禁止全库一次格式化。
- [ ] T032 [S3] `ruff check --select E,F,W,I` 先出基线清单，再逐目录清零或逐条豁免——验收：每次收窄均有记录，不以总豁免刷绿。
- [ ] T033 [S3] `mypy` 从 `tools/{common,naming_lib,register_lib,axis_lib}.py` 起步，先宽松后 strict——验收：四模块零错误且无未说明 `type: ignore`；其余列逐步清单。
- [ ] T034 [P] [S3] `uv.lock` 影子 CI 验证后再切换；保留 `python` 直跑回退——验收：本地与 CI 解释器版本一致，失败可一键切回。

## 阶段 S4 Rust 骨架

- [ ] T040 [S4] `sep-core/` Cargo 工程（`rust-toolchain.toml` 钉 1.100、`#![forbid(unsafe_code)]`、clap 子命令骨架）——验收：`cargo build --release` 出单二进制。
- [ ] T041 [S4] 统一输出层（`--json` 结构化、0／1／2／3 退出语义、stderr 诊断）——验收：与 Python 版适配映射表一致（黄金测试可验）；不得把告警并入失败码。
- [ ] T042 [S4] 在 `.github/workflows/checks.yml` 或经批准的新工作流增 Rust 构建与 `cargo test`；Linux CI、Windows 本地分别验收——验收：两平台各产 artifact；工作流变更同步 rules/05。
- [ ] T043 [P] [S4] `cargo-deny` 配置（许可证白名单、禁 yanked）——验收：`cargo deny check` 通过。

## 阶段 S5 B1 迁移（试金石批）

- [ ] T050 [S5] 迁移 `check_doc_size` → `sep check doc-size`——验收：黄金测试通过。
- [ ] T051 [S5] 迁移 `check_junk` → `sep check junk`——验收：同上。
- [ ] T052 [S5] 迁移 `check_quotes` → `sep check quotes`——验收：同上；含 Unicode 弯引号／直角引号用例。
- [ ] T053 [S5] 迁移 `clean` → `sep clean`（与 S2 的 Python 版并存）——验收：同上。
- [ ] T054 [S5] check_all 编排切换：四项改调 `sep`（保留 Python 回退开关）——验收：全库门禁输出与切换前一致。

## 阶段 S6 B2 结构校验

- [ ] T060 [S6] 迁移 `check_stages` → `sep check stages`（保留 S1–S7；063 新增谓词以 `ST1–ST9` 命名，064 承载谓词以 `ST10–ST15` 命名）——验收：黄金测试＋反例试金石；不得把 `S1–S7` 与阶段号混写。
- [ ] T061 [S6] 迁移 `check_catalog_network`（G1–G5）——验收：黄金测试（用最新快照）。
- [ ] T062 [S6] 迁移 `check_pairs`——验收：黄金测试。
- [ ] T063 [S6] 迁移 `check_summary`——验收：黄金测试。
- [ ] T064 [S6] 迁移 `check_taskfile_invariant`——验收：黄金测试。
- [ ] T065 [S6] `sep check --all` 并行编排（I/O 型用 tokio，CPU 型再评 rayon）——验收：固定平台与输入，报告 P50／P95／峰值内存及与 Python 基线的比值；**不预设 30 s**。

## 阶段 S7 B3 并发抓取

- [ ] T070 [S7] 迁移 `fetch_all`（tokio multi-thread，`--config A|B`，unchanged 不写盘不动钉）——验收：黄金测试＋1873 件 dry-run 计数一致。
- [ ] T071 [S7] 逐级压测并发（从现行 16 路起，按站点响应与退避调整；不以 128 为预设目标）——验收：请求速率受控、429／封禁风险有记录、逐请求留痕完整、可一键降并发。
- [ ] T072 [S7] 迁移 `fetch`／`fetch_entry`／`fetch_catalog`／`fetch_audit`——验收：各自黄金测试。
- [ ] T073 [S7] 迁移 `catalog_drift`——验收：黄金测试（四方差集）。
- [ ] T074 [S7] `sep fetch --only <slug>` 定点重抓——验收：单件重抓后 en/ 与钉一致。

## 阶段 S8 正则审计与 B4

- [ ] T080 [S8] 正则语义审计脚本：对 A 级工具列不可直译模式（反向引用／lookaround／条件组）——验收：输出清单与逐条处置（改写／留 Python）。
- [ ] T081 [S8] 迁移 `check_yuanwen_fidelity`（I2 字节＋I3 词元流）——验收：黄金测试；全库 1873 件零差异。
- [ ] T082 [S8] 迁移 `check_style`——验收：黄金测试；告警集合与 Python 版完全一致（不是数量，是集合）。
- [ ] T083 [S8] 迁移 `check_academic`——验收：同上。

## 阶段 S9 B5（正则风险最高，最后）

- [ ] T090 [S9] 迁移 `cite_audit`／`grammar_audit`／`measure_audit`／`punct_audit`——验收：各黄金测试。
- [ ] T091 [S9] 迁移 `check_terms`／`check_math_zh`——验收：同上。
- [ ] T092 [S9] 迁移 `en_source_audit`／`en_integrity`——验收：同上。
- [ ] T093 [S9] 六轴 q 链编排（`sep audit --axis`）——验收：q1–q6 串行与并行的**告警集合与退出语义**一致；非确定性排序须在 schema 中规范化。

## 阶段 S10 063 阶段轨实施（独立支线）

- [ ] T100 [S10] `rules/naming.json` 升 `sep-naming/v2`（stages 60／campaigns 6／marks 8／state_stage_map 19）——验收：schema 校验通过。
- [ ] T101 [S10] `check_stages` 新增 `ST1–ST9`（063 设计；ST9 判据归属）；064 另拟 `ST10–ST15` 文档承载——验收：命名不与既有 S1–S7 冲突；反例试金石至少三例必红。
- [ ] T102 [S10] 新增 `tools/stage_of.py`（派生视图，只读）——验收：1873 件均有输出；`--all` 分布与 tasks.state 聚合一致；对无状态节点输出 `derived_from`，不伪造状态。
- [ ] T103 [S10] 阶段轨 ADR（号实施时取，不预占）——验收：ADR 索引更新；`check_stages` S7 命名词表自洽。
- [ ] T104 [S10] specs/062 头注＋sop 映射行——验收：仅两行，不改正文；若 063 设计未批准则不加“已实施”措辞。

## 阶段 S11 案 B 退役（**P12 阻断；未获新裁定不得执行**）

- [ ] T110 [S11] 案 B ADR（号实施时取）——**前置：用户就 P12／段尾闭合作新裁定**；验收：ADR 索引更新且记录段尾责任、迁移、回退。
- [ ] T111 [S11] `pipeline.json` 增 `status`／`retired_into`／`retired_date`；`naming.json` 同步——验收：schema 校验通过；P12 结构谓词仍绿或新 ADR 明确替代。
- [ ] T112 [S11] rv-09 的 `does` 按 T163 的逐项矩阵增补——验收：13 项各有“保留／迁入／已覆盖／证据不足”结论；**不得预写净增 11 项**。
- [ ] T113 [S11] `rules/04`／`rules/11` 注记；`specs/063` §1.3／AX8／AX9 同步——验收：无残留“ex-05 活跃”；P12 说明一致。
- [ ] T114 [S11] `progress.py` 增退役列；`PROGRESS.md` 重生成——验收：20 活跃＋2 退役，阶段计数为 32 非退役实项＋26 预留＋2 退役。

## 依赖与并行总览

```
D0 文档重审（本轮）
├─ D1 关联卡纠偏
│  └─ D2 P12／案 B 新裁定 ── T110–T114（阻断）
├─ E1 T130 人工定性 → 22 节点证据 → E2 至 sg-02 → sg-03 另授权
├─ S1 标准回写（另批）
├─ C1 清理／登记表（另批；G23 先修）
└─ A1 Python 现代化 → R1 单工具迁移证据（另批）

S0 测试框架 → S4 Rust 骨架 → S5 → S6 → S7／S8 → S9（均须独立立项）
S10 阶段轨（另批）→ S11（P12 阻断）
```

## 验收门（每个工作包收口）

1. 该包内原子任务全部完成且证据可复核；工作包不得整体勾选。
2. 对应契约／黄金／性质测试通过；若声称迁移等价，差异清单为空且抽核有记录。
3. 若新增长期物，先确认其不属于既有事实源；登记表未批准时不强求入表。
4. 提交只含相关文件；提交信息说明状态；推送后 `git log origin/main..main` 为空。
5. 任何“已证明／已相容／已完成”必须指向 verified 证据，不得以检查器全绿替代。
