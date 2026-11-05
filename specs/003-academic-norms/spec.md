# Feature Specification: 学术规范门禁（tools/check_academic.py）

**Feature Branch**: `003-academic-norms` | **Created**: 2026-10-27 | **Status**: Implemented（T001–T005 完成，2026-10-27）

**Input**: 用户指令（2026-10-27）：“新增一整套流程，确保项目整体符合哲学学术规范并落地。”规范总纲 `rules/07-academic-norms.md`，决策记录 ADR-0006。本 feature 是该流程的机器可判定部分。

## 背景事实

* 全量重译战役铺开中：SUMMARY 正式词条约 1804，非存根译文仅 1 篇（alcmaeon，s1_checked）——规范此时落地，此后每篇译文生而合规。
* 学术规范此前散落 rules/02（参考文献照录）、rules/03（术语与古典编号）、rules/04（三审三校）；无文内版本事实要求，无引文完整性机检，无 AI 幻觉引文纪律。
* `baseline/entries.json`（入库）逐 slug 登记 `pubinfo`（`first_published`/`substantive_revision`，英文月名格式如 "Apr 10, 2003"）、`authors`、`zh_doc`（部分为 null，部分路径滞后于目录重建）。
* 任务 JSON（`tasks/<字母>/<slug>.json`）登记 `version_pin`（pubinfo_date + archive_edition + sha256）与 `steps`（每步含 evidence）。
* AI 会话生成的参考文献/引注存在幻觉风险：编造条目、补全页码、“规范化”译名——哲学翻译的学术事故。
* 脚注式引注 `[^key]` 与文末 `[^key]:` 定义失配 = 读者无法回溯出处。

## User Scenarios & Testing

### User Story 1 — 版本事实核对（P1）

运行检查器，非存根词条缺“首次发表于……”版本事实行、或行内日期与 baseline `pubinfo` 不一致 → 硬错误并报文件与行号；一致 → 通过。

**Independent Test**: 人为改动 alcmaeon 版本事实行的年份运行一次命中；恢复后命中消失。

**Acceptance Scenarios**:

1. **Given** alcmaeon 译文行 `*首次发表于 2003 年 4 月 10 日；2025 年 7 月 18 日实质修订。*` 与 baseline（Apr 10, 2003 / Jul 18, 2025），**When** 运行，**Then** 不报。
2. **Given** 文内首发年份被改成 2002，**When** 运行，**Then** `pubinfo-mismatch` 报该文件与两侧日期。
3. **Given** 删除版本事实行，**When** 运行，**Then** `pubinfo-missing` 硬错误。

### User Story 2 — 引注配对（P1）

`[^key]` 引用与文末 `[^key]:` 定义失配 → 硬错误，报 key 与行号。

**Acceptance Scenarios**:

1. **Given** 正文含 `[^k1]` 而文末无定义，**When** 运行，**Then** `orphan-ref`。
2. **Given** 文末有 `[^k2]: ……` 而正文无引用，**When** 运行，**Then** `orphan-def`。

### User Story 3 — 结构完整性（P2，默认告警）

非存根词条缺 `## 参考文献`、缺 `## 学术工具`（“如何引用本词条”）、参考文献节缺“照录”说明、译注未闭合或落入参考文献节 → 告警；`--strict` 升硬错误。

**Acceptance Scenarios**:

1. **Given** 删除某词条参考文献节标题，**When** 默认运行，**Then** 告警 `biblio-missing`、退出码 0；**When** `--strict`，**Then** 退出码 1。

### User Story 4 — 任务版本钉与凭证（P1）

任务 JSON 缺 `version_pin` 三字段（pubinfo_date/archive_edition/sha256）任一 → 硬错误；`state=done` 的任务步骤缺 evidence（或步数不足）→ 硬错误。

**Acceptance Scenarios**:

1. **Given** 某任务 sha256 被抹空，**When** 运行，**Then** `task-pin-missing`。
2. **Given** 某 done 任务 s3 步 evidence 为空，**When** 运行，**Then** `task-evidence-missing`。

## Requirements

* **FR-001**: 全库扫描词条文档：排除目录（rules、specs、tasks、tools、en、yuanwen、script、node_modules、pending、public、baseline、state、qian-yan、fang-fa-lun、jian-yi-shu、guan-yu、点前缀目录）与根级非词条 md（README/SUMMARY/mu-lu-s/yi-zhe-shuo-ming/PROGRESS/AGENTS 等）；仅处理首非空行为 `#`（H1）的 md。
* **FR-002**: 存根判定：全文件非空行 ≤10（含 H1）为存根，跳过结构类检查；别名/占位词条天然落此层。
* **FR-003**: baseline 定位：先按 `zh_doc` 精确匹配（casefold、正斜杠归一、相对 `--root`），未中再按 slug 词元匹配文件名（hyphen 边界、长 slug 优先）；歧义或未中 → 告警 `baseline-lookup-miss`，pubinfo 检查跳过。
* **FR-004**: 日期比对：英文月名（缩写/全名前缀）→（年， 月， 日）元组；文内版本事实行在前 30 非空行内查找，行内前两个中文日期分别对 `first_published`/`substantive_revision`；baseline 缺该字段则跳过对应比对；版本事实行缺失或超窗 → 硬错误。
* **FR-005**: 脚注配对：跳过围栏代码块；引用集合与定义集合对称差 → `orphan-ref`/`orphan-def`。
* **FR-006**: 分级：US1/US2/US4 为硬错误（退出码 1）；US3 默认告警；`--strict` 全部升硬。
* **FR-007**: `--docs <路径>...` 定点模式只查文档不查任务；`--root`/`--baseline`/`--tasks-dir` 注入参数供单元测试。
* **FR-008**: 只读不修改任何数据文件；纯标准库；UTF-8 无 BOM、LF；输出人类可读报告（含 文件：行号），风格对齐 `check_terms.py`。

## Edge Cases

* baseline `zh_doc` 为 null 或路径滞后（目录重建中间态，如 alcmaeon 登记为 `a/alcmaeon.md` 而实际在 `argument/`）：slug 词元回退命中；本工具不依赖 SUMMARY.md（其 90 条缺失路径属并行会话重建中间态）。
* baseline 无 `pubinfo` 字段：跳过版本事实检查（缺省件显式跳过，不报错）。
* 文内出现译注（`（译注：……）`）多个：逐个校验闭合与位置。
* `[^key]` 出现在代码块/数学块内：跳过不计。
* 集群子词条文件名含父 slug 片段：slug 词元长者优先，避免错配；歧义时报告警不猜。
* 英文月名大小写混杂（“March”“Mar”）：按前 3 字符 casefold 解析；解析失败 → 告警 `baseline-lookup-miss`（pubinfo 不可核）。

## Success Criteria

* 全库首检 0 硬错误（alcmaeon 合规，或发现的问题已定点修复并复检通过）。
* 单测覆盖四类 User Story 与主要 Edge Case，`python -m unittest discover -s tools/tests` 全绿。
* 接入 checks.yml（push 复核），rules/05、rules/README、AGENTS.md、tools/README 登记齐全。

## Assumptions（裁定登记）

* 2026-10-27 用户指令“新增一整套流程，确保项目整体符合哲学学术规范并落地”——rules/07 + ADR-0006 + 本 spec + check_academic.py 为其落地载体。
* 存根阈值 10 非空行为实现参数（`STUB_BODY_LINES`），误伤时在工具内调整。
* 战役铺开期结构类缺口仅告警不红灯；词条 s3/r3 验收以 `--docs --strict` 把关——避免翻译中间态阻塞 CI。
* 不改 rules/04 状态机与 task_ops 契约；学术审校通过 s1/s3/r3 挂钩实现。
