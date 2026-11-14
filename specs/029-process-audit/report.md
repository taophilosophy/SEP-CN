# 流程全量审计报告（2026-11-15）

**审计口径**：IEEE 1028 Audit（独立方对照标准与判据的符合性评价，只评不改）；**判据**：rules/09 流程过程标准（ADR-0044）、rules/04 阶段细则、tasks/README 协议、specs/001 contracts/cli.md、specs/004 四方分类对照表、specs/025 规范基线；**范围**：规则体系、状态机与任务语料（1,203 件）、信息项、评审体系、度量、CI 门禁。

## 一、符合性结论（按维度）

| 维度 | 判据 | 结果 |
| ---- | ---- | ---- |
| 状态合法性 | tasks JSON state ∈ ORDER[kind] | **通过**——非法状态 0 |
| 语料完整 | JSON 可解析、顶层 dict | **通过**（7 件顶层 list 均为 tasks/manifests/ 批量裁定清单，合法形态，见 F2） |
| 凭证三要素 | steps[].actor/at/evidence 非空 | **通过**——全库缺失 0 |
| 状态分布对账 | 028 §5 回退 manifest | **通过**——done 224／s2.5_checked 198／cleared 153／pending 621，与回退清单＋023 承接口径一致 |
| progress↔task_ops 同步 | STATES == ORDER | **通过**（逐元素相等；s24/s25 挂钩已接线） |
| CLI 契约同步 | cli.md vs task_ops 命令面 | **一项缺口**（F1：reopen 未登记） |
| 规则一致性 | 09↔04↔06↔tasks/README↔data-model↔cli 交叉引用 | **通过**——无矛盾、无失效链接；09 框架层不复制 04 细则（单一事实源守住） |
| 遗留引用 | “audited”残检 | **通过**——全部为历史记录（ADR-0040/0043）、更名注记或工具输出字段名（baseline_audit/en_integrity 的 audited 计数与状态名无关），无活引用失效 |
| 门禁矩阵（缺陷类×检查面） | doctrine 09 §2.1 | **通过**——A 事实性→check_academic、B 术语→check_terms、C 语言→check_prose、D 格式→check_style/tables_images、数学→check_math(_zh)、图片→check_images、引号→check_quotes；语体类（文言/AI 腔/「一个」）按 ADR-0033 语义判定＋密度统计，非缺口 |
| check_all | 10 项 | **通过**（审计时点全绿） |

## 二、发现与处置

| # | 级别 | 发现 | 处置 |
| ---- | ---- | ---- | ---- |
| F1 | Minor | `specs/001 contracts/cli.md` 的 task_ops 命令清单缺 `reopen`（工具自 ADR-0033 即有） | 已补登记（审计随附处置） |
| F2 | Minor | `tasks/README.md` 存储约定缺 `tasks/manifests/` 目录登记（fang-fa-lun S2 的批量裁定清单入库位，7 件顶层 list 文件由此而来） | 已补登记 |
| F3 | Minor | 早期 specs 版本/状态头缺失（抽测 018 无；15289 五属性之「版本/状态」不齐；ADR-0041 §9 仅约束新 spec） | 018 已补头并注记冻结去向；其余早期 spec 登记为**存量豁免**，随各自修订补齐，不批量追溯 |
| F4 | Info | 术语机检仅 check_terms（登记册自洽硬拦＋定点告警），词条面术语一致性主要靠 s2.4 人工走查 | 按 ADR-0043 独立环节设计执行；覆盖面随 specs/008 查证扩展滚动增强 |
| F5 | Info | 度量三要素中「灭错率/差错率」尚无阈值来源 | 待 specs/028 R2 基线报告；rules/09 §5 已前置「无基线不设门」 |

## 三、审计留痕

* 本报告＋处置 diff 为审计凭证；审计为只读评价，F1–F3 处置为文档补登记，不涉及语料与状态。
* 下次审计建议时点：specs/028 滚动执行一个字头批次后（验证 s2.4/s2.5 增项凭证实跑形态），或 doctrine 复审周期 2027-01-21。
