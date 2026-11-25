# 实施计划：064 全流程全要素审计与规范化

- 规格：`specs/064-flow-spec-audit/spec.md`（rev 5）
- 日期：2026-11-26；状态：**待批（暂不开工）**——本文件是设计，不是执行记录
- 与 `spec.md` 的分工：spec 管“做什么、为什么、验收”；本文件管“怎么做、依赖什么、怎么回退”；`tasks.md` 管“按什么顺序做、每步的验收”。

## 1 技术上下文

| 项 | 内容 |
| ---- | ---- |
| 语言／版本 | Rust **1.100.0**（edition 2024）、Python **3.15.2**、Bun 1.3（站点）；**Go 不引入** |
| 依赖 | Rust：白名单 crate（tokio／rayon／serde／serde_json／regex／sha2／walkdir／memchr／clap），`Cargo.lock` 入库，`cargo-deny` 审计许可证；Python：**维持零第三方依赖**（仅标准库）；Bun：既有 vitepress |
| 存储 | JSON 文件：`baseline/registry-long.json`、`state/registry-temp.json`、`rules/{naming,pipeline,standards}.json`、`tasks/*.json` |
| 测试 | Rust `cargo test`（单元＋集成）；Python `unittest`（遗留 55 文件）；**黄金测试**（跨语言，Python 编排） |
| 目标平台 | Windows（M1，本机构建）、Linux（CI，交叉编译） |
| 项目类型 | CLI 工具链＋数据校验＋文档生成 |
| 性能目标 | 全库 1873 件门禁批 ≤ 30 s（16 核）；抓取 128 并发且礼貌限速；单工具启动 ≤ 50 ms |
| 约束 | `#![forbid(unsafe_code)]`；不引入 FFI／PyO3；不改 I2 产物；不改 JSON 契约的既有字段语义 |
| 规模 | 96 工具（A 26 迁移）／1873 词条／21 门禁（+1 项）／64 规格卡 |

## 2 架构决策

### 2.1 语言分层（按变化率分派，不按偏好）

| 层 | 语言 | 判据 |
| ---- | ---- | ---- |
| 稳态内核（判据、字节比对、结构校验、门禁编排） | Rust | 逻辑稳定、性能敏感、类型可建模 |
| 并发抓取 | Rust（tokio multi-thread） | 与内核同二进制，复用 HTTP／限速／重试 |
| 语义锁定层（转换器、爬虫、一次性、生成器） | Python | I2 字节锁定、Playwright 唯一、改格式摩擦最低 |
| 站点 | Bun | 既有 |

### 2.2 二进制与调用边界

```
sep (Rust, 单二进制)
├─ sep check --all | --gate <name>
├─ sep fetch --config A|B [--only slug]
├─ sep audit --axis q1..q6
├─ sep clean --check | --go
└─ sep registry register|verify|prune

调用协议（唯一契约）：
  stdout: --json 单行 JSON（schema 固定）
  exit:   0 通过 / 1 告警或失败 / 2 用法错误
  stderr: 人类可读诊断
```

Python 遗留工具继续以 `python tools/x.py` 形态存在；`sep` 通过子进程调用它们（`sep check --all` 聚合时）。

### 2.3 数据契约

| 文件 | schema | 变更规则 |
| ---- | ---- | ---- |
| `baseline/registry-long.json` | `sep-registry/v1` | 只追加／状态更新；`id` 不复用 |
| `state/registry-temp.json` | 同上（`kind: temp`） | 本机写，不入库 |
| `rules/naming.json` | `sep-naming/v2` | 阶段轨入册（063） |
| `rules/pipeline.json` | `sep-pipeline/v3` | 增 `status`／`retired_into`／`retired_date` |
| `rules/standards.json` | 四层不变，增 `schema_version` | 25010:2023 纳登 |

### 2.4 黄金测试布局

```
tools/golden/
├─ <tool>/
│  ├─ input/            # 输入快照（裁剪到最小可复现集）
│  ├─ expected.json     # {stdout_sha256, exit_code, artifacts:{path: sha256}}
│  └─ meta.json         # 录制时间、源版本（commit）、工具版本
└─ run_golden.py        # 编排：对每个 tool 跑新实现，逐字节比对
```

**录制时机**：迁移前用现行 Python 版在真实输入上录制；**任何输入裁剪须保持判定结果不变**（裁剪后 Python 版重跑通过才可用）。

**比对规则**：stdout 逐字节；退出码相等；产物 sha 相等；`--json` 输出按键序归一后比较（JSON 键序不保证）。

## 3 阶段与依赖

| 阶段 | 产物 | 依赖 | 可并行 |
| ---- | ---- | ---- | ---- |
| **S-1** | **端到端试金石**（060 §5.4 第一梯队 3 件走完整流程，产出 findings） | — | **最先**，独立于其余 |
| S0 | 黄金测试框架＋register 骨架 | — | 与 S1 并行 |
| S1 | `tools/registry.py`＋两表建表（首批：catalog／errata／patches） | — | 与 S0 并行 |
| S2 | `clean --check` 入 check_all 第 22 项 | S1（表消费） | — |
| S3 | Python 现代化（pyproject／ruff／mypy／uv） | — | 与 S0–S2 并行 |
| S4 | Rust 骨架 `sep`（clap＋json＋退出码规范） | S0 | — |
| S5 | B1 迁移（doc_size／junk／quotes／clean） | S0、S4 | — |
| S6 | B2 结构校验（stages／catalog_network／pairs／summary／taskfile_invariant） | S5 | — |
| S7 | B3 抓取（fetch_all 等 5 项）＋压测 | S6 | — |
| S8 | 正则语义审计 → B4（yuanwen_fidelity／style／academic） | S6 | 与 S7 并行 |
| S9 | B5（六轴 audit＋terms／math_zh） | S8 | — |
| S10 | 063 阶段轨实施（naming v2、check_stages ⑩–⑮、stage_of、ADR-0090） | S1 | 与 S5–S9 并行 |
| S11 | 案 B 退役（ADR-0091、pipeline/naming retired、rules/04 注记） | S10 | — |

**关键路径**：**S-1** → S0 → S4 → S5 → S6 → S7/S8 → S9；S10→S11 为独立支线（只动 JSON 与 Python 校验器）；S-1 的 findings 可能调整全部后续顺序。

## 4 迁移与回退

| 变更 | 回退方式 | 窗口 |
| ---- | ---- | ---- |
| 新增 Rust 二进制 | 从 PATH 移除即回退；Python 版保留到该工具黄金测试连续稳定 30 天 | 全程 |
| 登记表建表 | 删两个 JSON 文件；clean 退回 ADR-0003 行为 | 立即 |
| check_all 第 22 项 | 从 GATES 移除一行 | 立即 |
| pipeline/naming retired 字段 | 删字段；063 阶段状态回 accepted | 立即 |
| rules/04 注记 | 删注记行 | 立即 |

**不可回退项**：无。所有 P0 变更均设计为可逆；唯一不可逆的是“黄金测试录制后的行为基线”，但它只是新增文件。

## 5 风险登记

| # | 风险 | 概率 | 影响 | 缓解 |
| ---- | ---- | ---- | ---- | ---- |
| R1 | Rust regex 语义与 Python `re` 不一致 | 高 | 判据静默错判 | S8 前置正则审计；无等价改写者留 Python；黄金测试必须覆盖 Unicode／边界用例 |
| R2 | 重写引入行为漂移 | 中高 | 门禁假绿／假红 | 黄金测试为唯一验收；未过黄金测试不得替换 Python 版 |
| R3 | 双机／CI 构建差异 | 中 | 本地绿 CI 红 | 三份锁文件＋`rust-toolchain.toml`；CI 与本地同容器镜像 |
| R4 | 登记表与既有事实源重复（第二本账） | 中 | 账实不符 | AX22 单源公理＋S1 首批只登三件；`en/` 不登记 |
| R5 | 缓存清理误删用户草稿 | 低 | 数据丢失 | `script/`／`en/`／`yuanwen/` 在 clean 的 SKIP 集；`--go` 需显式 |
| R6 | 并行会话在途改动造成门禁红误判 | 高 | 归因耗时 | 门禁红先看 mtime 与最近提交归属；本卡不碰他人文件 |
| R7 | 064 自身文档膨胀（>1000 行／100 KB） | 中 | 门禁红 | spec 现 561 行／37 KB；新增内容优先入 results/；接近 800 行时拆分 |

## 6 验收（对应 spec §9）

1. `sep check --all` 输出与 `python tools/check_all.py` 等价（同一批输入，退出码与告警集一致）。
2. 黄金测试：A 级 26 项全部有录制与通过记录。
3. 登记表：两表 schema 校验通过；`verify` 对 protect 条目零 orphaned。
4. `clean --check` 在干净工作区退出 0，在注入一个 `*.tmp` 后退出 1。
5. 三份锁文件在库；`cargo-deny` 无拒绝许可证。
6. 案 B 影响面 12 处逐项核对（spec §3.3）。

## 7 宪章检查（Constitution Check）

| 原则 | 本方案如何满足 |
| ---- | ---- |
| 零信任 | 黄金测试逐字节对齐；不改 I2 产物；转换器不迁移 |
| 可追溯 | 登记表 sha＋时间三戳；锁定日期版本钉 |
| 单一事实源 | 登记表不复制 entries.json／tasks；pipeline 仍是节点唯一源 |
| 流程先行 | 本卡先立规格与公理，实施另批；无“边写边定” |
| 体例即契约 | JSON schema 版本化；CLI 退出码固定 |
| 知难行易 | 正则审计前置；黄金测试先建后迁 |
