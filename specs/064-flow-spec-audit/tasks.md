# 任务清单：064 全流程全要素审计与规范化

- 输入：`specs/064-flow-spec-audit/spec.md`（rev 5）、`plan.md`、`results/axioms-v3.md`
- 状态：**全部 pending**（用户 2026-11-26 裁定“暂不开工”；本清单是待批施工图）
- 格式：`[ID] [P?] [阶段] 描述（含文件路径与验收）`；`[P]`＝不同文件、无依赖，可并行

## 阶段 S-1 端到端试金石（2026-11-26 批准；**按件按段拆任务，不一次性**）

> 名单引用 `specs/060` §5.4；按现状 22 节点跑（不先实施方案 B），用现有 Python 链。一件一段一任务、各自收口；上表未勾满不进入下一段。产出 findings 回填 spec §18.4。
> 优先级：先 habermas 走完，再 logic-preference，再 environmental-aesthetics；第二／三梯队每件单列一个任务，按轴启用。

### habermas（第一梯队 1/3）

- [x] T130 [S-1] ex-04 源审计（en_integrity＋en_source_audit，含候选定性）——完成 2026-11-26；hard=0／warn 5；见 `results/e2e-habermas.md`
- [ ] T131 [S-1] G13 豁免清单落地（`rules/11-source-side.md` §5.3）——**已完成**（2026-11-26），本任务仅作勾销与规则地图登记
- [ ] T132 [S-1] tr-02 样章（§1–§2，约 3,000 字）：验证段落账本、step1／step2、术语注入——验收：账本守恒、样章可读
- [ ] T133 [S-1] tr-02 全量（余下各节，分 4–6 批 checkpoint）——验收：全文入库、账本段落数守恒
- [ ] T134 [S-1] tr-03 一校（对照英文源逐节核销）——验收：对照记录；残留外文 0
- [ ] T135 [S-1] tr-04 二校（语体、反欧化）——验收：`check_prose` 告警清零或逐条豁免
- [ ] T136 [S-1] rv-01 术语与勘误（术语轴＋体例轴＋勘误轴）——验收：三段 evidence
- [ ] T137 [S-1] rv-02 全局一致性（两轴比较校对）——验收：两轴记录＋机检输出
- [ ] T138 [S-1] rv-03–08 六轴（q1→q6 顺序固定）——验收：各轴凭证落 `state/axis/`
- [ ] T139 [S-1] rv-09 体例终校——验收：`check_style` 0 issue
- [ ] T140 [S-1] sg-01／sg-02（初审＋复审）——验收：自审与复核记录
- [ ] T141 [S-1] sg-03 终审（需用户显式指定 `--mandate`）——验收：CI 全绿＋签字

### logic-preference（第一梯队 2/3）

- [ ] T142 [S-1] ex-04 源审计——验收：同 T130 口径
- [ ] T143 [S-1] tr-02 样章（§1–§2）——验收：公式定界符与 362 处行内公式样本无损
- [ ] T144 [S-1] tr-02 全量——验收：全文入库
- [ ] T145 [S-1] 校次链 tr-03／tr-04——验收：同 T134／T135
- [ ] T146 [S-1] rv-01／rv-02／rv-09——验收：同 T136／T137／T139
- [ ] T147 [S-1] 六轴 rv-03–08（重点 q2 逻辑、q5 计量、q6 标点）——验收：各轴凭证
- [ ] T148 [S-1] sg 链——验收：同 T140／T141

### environmental-aesthetics（第一梯队 3/3）

- [ ] T149 [S-1] ex-04 源审计（重点：369 条文献条目）——验收：书目计数
- [ ] T150 [S-1] tr-02 样章（§1–§2）——验收：文献键位与脚注配对
- [ ] T151 [S-1] tr-02 全量——验收：全文入库
- [ ] T152 [S-1] 校次链与 rv 链（重点 q1 引文）——验收：引文 hash 锁定
- [ ] T153 [S-1] sg 链——验收：同 T141

### 第二梯队（每件一任务，核心 3 件全过后启用）

- [ ] T154 [S-1] `i/imprecise-probabilities`（14 类构件 12 类）全流程——验收：构件无丢失
- [ ] T155 [S-1] `a/action`（长文＋引文双密集）全流程——验收：同第一梯队口径
- [ ] T156 [S-1] `a/axiom-choice`（530 行内公式＋8 块＋4 表）全流程——验收：公式与表无损
- [ ] T157 [S-1] `n/newton-principia`（36,082 汉字＋3 图）全流程——验收：图与版式

### 第三梯队（单项极值，按轴专项启用）

- [ ] T158 [S-1] `l/logic-dynamic`（行内公式 602 处）——验收：公式定界符全配对
- [ ] T159 [S-1] `j/japanese-aesthetics`（图 33 幅）——验收：图注与 alt 齐备
- [ ] T160 [S-1] `k/kokugaku-school`（表 48 行）——验收：表格结构完整
- [ ] T161 [S-1] `d/digital-art`（唯一代码块）——验收：代码块闭合

### 汇总与回填（全部条目完成后）

- [ ] T162 [S-1] 汇总 `results/e2e-findings.md`（G13+，标阻断／非阻断）——验收：与各件记录逐条对应
- [ ] T163 [S-1] **案 B 复核**：据 ex-05／tr-05 实际作业记录核对 §3.2 净增 11 项——验收：覆盖／缺项结论
- [ ] T164 [S-1] **stage_of 联调**：逐站核对阶段派生（063 CT3／CT8）——验收：差异有解释
- [ ] T165 [S-1] 回填 spec：findings → G 清单 → P0 顺序与验收——验收：spec §17／§18.4 更新

## 阶段 S0 黄金测试框架（迁移的唯一安全网）

- [ ] T001 [P] [S0] 建 `tools/golden/` 目录结构与 `run_golden.py` 骨架（读 `expected.json`，跑命令，逐字节比对）——验收：对假 tool 的正反例各一，比对通过／失败各一。
- [ ] T002 [P] [S0] 定 `expected.json`／`meta.json` 格式（`stdout_sha256`、`exit_code`、`artifacts`、`commit`、`recorded_at`）——验收：schema 文档写入 `tools/golden/README.md`。
- [ ] T003 [S0] 实现录制模式 `run_golden.py --record <tool>`（跑现行 Python 版并落 expected）——验收：对 `check_doc_size` 录制成功且回放通过。
- [ ] T004 [S0] 实现 `--json` 归一比对（键序排序、浮点容差 0、换行符归一）——验收：两次运行同一工具结果相等。

## 阶段 S1 全局登记表

- [ ] T010 [P] [S1] 写 `baseline/registry-long.json` 初始骨架（`schema: sep-registry/v1`、`kind: long`、空 `entries`）——验收：JSON 可解析，含 15 字段说明。
- [ ] T011 [P] [S1] 写 `state/registry-temp.json` 初始骨架（`kind: temp`）——验收：同上；确认 `state/` 在 `.gitignore`。
- [ ] T012 [S1] 实现 `tools/registry.py register`（sha256／size／时间戳自动填；`id` 递增；拒重 path）——验收：登记 `baseline/catalog.json` 成功，重复登记报错。
- [ ] T013 [S1] 实现 `registry.py verify`（状态机求值：active／expired／orphaned／superseded；protect 缺件＝红）——验收：删一份已登记文件后 verify 报 orphaned。
- [ ] T014 [S1] 实现 `registry.py prune`（默认试运行；`--go` 删除；仅 temp＋expire）——验收：过期 session 条目在 `--go` 后文件消失、条目 pruned。
- [ ] T015 [S1] 首批登记三件：`catalog.json`、`en-errata/en-errata.md`、`en-patches/INDEX.json`（`permanent`／`protect`）——验收：verify 全绿。
- [ ] T016 [P] [S1] 写 `tools/golden/registry/` 用例（register→verify→prune 全链）——验收：黄金测试通过。

## 阶段 S2 清理检查点全局化

- [ ] T020 [S2] 扩展 `tools/clean.py`：`--check` 只读档（有垃圾退出 1）；消费两张登记表——验收：干净树退出 0；注入 `*.tmp` 退出 1；已登记 protect 文件不被列入删除。
- [ ] T021 [S2] 扫描面扩至 `target/`、`.ruff_cache`、`.mypy_cache`、`.pytest_cache`、`.vitepress/cache|dist`——验收：在各目录放占位文件均被识别。
- [ ] T022 [S2] `tools/check_all.py` GATES 增第 22 项（名称“缓存与临时物”）——验收：`--list-gates` 输出 22 项；CI 矩阵自动跟随。
- [ ] T023 [P] [S2] `.gitignore` 审计补齐（`target/`、`__pycache__/`、`*.pyc`、`.vitepress/cache`、`.vitepress/dist`）——验收：`git status` 不出现这些路径。
- [ ] T024 [P] [S2] `.github/workflows/checks.yml` 增只读 `clean --check` 步骤——验收：PR 上该 step 输出清单但不删除。

## 阶段 S3 Python 现代化（零风险，先行）

- [ ] T030 [P] [S3] 建 `pyproject.toml`（requires-python `>=3.15`、无运行时依赖、ruff/mypy 配置）——验收：`uv sync` 成功。
- [ ] T031 [P] [S3] `ruff format` 全量跑一遍（只格式化，不改语义）——验收：`git diff` 仅空白／引号风格；`check_all` 全绿。
- [ ] T032 [S3] `ruff check --select E,F,W,I` 清零（或逐条豁免留痕）——验收：`ruff check` 退出 0。
- [ ] T033 [S3] `mypy --strict` 从 `tools/{common,naming_lib,register_lib,axis_lib}.py` 起步——验收：四模块零错误；其余模块列入逐步清单。
- [ ] T034 [P] [S3] `uv.lock` 入库；CI 改用 `uv run`——验收：本地与 CI 解释器一致。

## 阶段 S4 Rust 骨架

- [ ] T040 [S4] `sep-core/` Cargo 工程（`rust-toolchain.toml` 钉 1.100、`#![forbid(unsafe_code)]`、clap 子命令骨架）——验收：`cargo build --release` 出单二进制。
- [ ] T041 [S4] 统一输出层（`--json` 单行、退出码 0/1/2、stderr 诊断）——验收：与 Python 版的退出码语义一致（黄金测试 T001 可验）。
- [ ] T042 [S4] `ci.yml` 增 Rust 构建与 `cargo test` 作业；交叉编译 linux——验收：CI 两平台产出二进制 artifact。
- [ ] T043 [P] [S4] `cargo-deny` 配置（许可证白名单、禁 yanked）——验收：`cargo deny check` 通过。

## 阶段 S5 B1 迁移（试金石批）

- [ ] T050 [S5] 迁移 `check_doc_size` → `sep check doc-size`——验收：黄金测试通过。
- [ ] T051 [S5] 迁移 `check_junk` → `sep check junk`——验收：同上。
- [ ] T052 [S5] 迁移 `check_quotes` → `sep check quotes`——验收：同上；含 Unicode 弯引号／直角引号用例。
- [ ] T053 [S5] 迁移 `clean` → `sep clean`（与 S2 的 Python 版并存）——验收：同上。
- [ ] T054 [S5] check_all 编排切换：四项改调 `sep`（保留 Python 回退开关）——验收：全库门禁输出与切换前一致。

## 阶段 S6 B2 结构校验

- [ ] T060 [S6] 迁移 `check_stages` → `sep check stages`（含 063 的 ⑩–⑮ 谓词）——验收：黄金测试＋063 反例试金石。
- [ ] T061 [S6] 迁移 `check_catalog_network`（G1–G5）——验收：黄金测试（用最新快照）。
- [ ] T062 [S6] 迁移 `check_pairs`——验收：黄金测试。
- [ ] T063 [S6] 迁移 `check_summary`——验收：黄金测试。
- [ ] T064 [S6] 迁移 `check_taskfile_invariant`——验收：黄金测试。
- [ ] T065 [S6] `sep check --all` 原生并行跑各门（rayon）——验收：全库 21 门 ≤ 30 s。

## 阶段 S7 B3 并发抓取

- [ ] T070 [S7] 迁移 `fetch_all`（tokio multi-thread，`--config A|B`，unchanged 不写盘不动钉）——验收：黄金测试＋1873 件 dry-run 计数一致。
- [ ] T071 [S7] 压测 16→64→128 路（礼貌限速、退避、逐请求留痕）——验收：128 路下无 429 风暴、日志完整。
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
- [ ] T093 [S9] 六轴 q 链编排（`sep audit --axis`）——验收：q1–q6 串行与并行结果一致。

## 阶段 S10 063 阶段轨实施（独立支线）

- [ ] T100 [S10] `rules/naming.json` 升 `sep-naming/v2`（stages 60／campaigns 6／marks 8／state_stage_map 19）——验收：schema 校验通过。
- [ ] T101 [S10] `check_stages` 扩至九谓词（⑨ 判据归属＋⑩–⑮ 文档承载）——验收：反例试金石三例必红。
- [ ] T102 [S10] 新增 `tools/stage_of.py`（派生视图，只读）——验收：1873 件均有输出；`--all` 分布与 tasks.state 聚合一致。
- [ ] T103 [S10] ADR-0090（阶段轨）——验收：ADR 索引更新，S7 登记表自洽。
- [ ] T104 [S10] specs/062 头注＋sop 映射行——验收：两行，不改正文。

## 阶段 S11 案 B 退役

- [ ] T110 [S11] ADR-0091（ex-05／tr-05 退役并入 rv-09）——验收：ADR 索引更新。
- [ ] T111 [S11] `pipeline.json` 增 `status`／`retired_into`／`retired_date`；`naming.json` 同步——验收：schema 校验通过。
- [ ] T112 [S11] rv-09 的 `does` 增净增 11 项——验收：与原 ex-05／tr-05 清单逐条对应。
- [ ] T113 [S11] `rules/04` 六道表注记；`specs/063` §1.3／AX8／AX9 同步——验收：无残留“ex-05 活跃”表述。
- [ ] T114 [S11] `progress.py` 增退役列；`PROGRESS.md` 重生成——验收：20 活跃＋2 退役。

## 依赖与并行总览

```
S-1（试金石，最先）──┬── 回填 findings
                     └── 案 B 复核（T125）
S0 ─┬─ S4 ─ S5 ─ S6 ─┬─ S7
    │                 └─ S8 ─ S9
S1 ─ S2
S1 ─────────────── S10 ─ S11
S3（独立，可全程并行）
```

## 验收门（每阶段收口）

1. 该阶段全部任务勾选；对应黄金测试通过。
2. `check_all` 全绿（并行会话在途红项须注明归属）。
3. 本节新增文件已入 `registry-long`（若属长期物）。
4. 提交信息含阶段号；推送后 `git log origin/main..main` 为空。
