# 术语判读台账与机械替换回溯工具（specs/031）

**版本** v1.0 ｜ **状态** 生效（已落地）｜ **日期** 2026-11-15 ｜ **权威** [ADR-0048](../../rules/adr/0048-术语落地差异处置标准.md)（跟进项 ①②）｜ **工具** `tools/check_terms.py`、`tools/mech_audit.py`

## 1. 目的

ADR-0048 把术语差异处置定为“定性 D1–D5 → 三出口（修复／登记／豁免）→ 复跑 → 写 evidence”。但这两条要求在工具层缺落点：

* **判读不可复算**：`check_terms --docs` 的告警只打印到 stdout，谁判了、判成哪一类、走了哪个出口，全靠任务 evidence 的自由文本；没有台账，就没有“每条告警都判过”的机检口径，也没有“豁免必须附理由与复核人”的强制。
* **机械替换回溯是战役内工具**：`specs/015-style-register-review/bin/mech_audit.py` 硬编码 17 条收口清单、输出写死 `specs/015/results/`、只审破折号，不能作为常态工具在任意词条上跑。

本规格把这两件事工具化。

**非目标**：不判 D 类（机器不替人做语境判断）；不把台账校验升入 `check_all` 硬门（ADR-0048 决策 8）；不改 `check_terms` 既有告警/硬错误口径；不动译文与登记册内容。

## 2. 交付物与功能需求

| ID | 交付 | 验收判据 |
| ---- | ---- | ---- |
| FR-1 | `check_terms.py --docs <doc>… --ledger <path>`：把本次定点核销的每条告警写成台账骨架（`schema: sep-cn-term-ledger/1`），行含 `doc / term / translation / variants / head / status`（`missing` 或 `ripple`）与空白的 `d_class / exit / evidence / source / reviewer` | 台账行数 = 告警数；`status` 与 stdout 告警类型一一对应；无告警时写空 `rows` |
| FR-2 | `check_terms.py --check-ledger <path>`：台账闭合校验——`d_class ∈ {D1,D2,D3,D4,D5,n/a}`、`exit ∈ {fix,register,exempt}`、`evidence` 非空、`exit=exempt` 须有 `reviewer`、**`d_class ∈ {D3,D4,D5}` 须有 `source`（查证凭证）**；`n/a` 须在 evidence 说明“概念未出现”之类理由 | 闭合台账 exit 0；缺项/越界 exit 1 并按行打印违例；不读登记册、不跑文档核销 |
| FR-3 | `tools/mech_audit.py`：自 `specs/015` 迁入并泛化——位置参数给 slug、`--since DATE`、`--marker CHAR`（默认不按标点过滤）、`--out PATH`（默认 `state/mech-audit-latest.json`）；保留 `pure / conn / susp` 分类与“只产候选、不作定性”纪律 | 对给定 slug 产出与原器同构的 JSON（`slug/commit/date/cat/why/old/new/path/cur_lineno`）；无硬编码词条清单；`--out` 可注入（测试用） |
| FR-4 | `rules/03` 作业顺序条的“机械替换回溯”指向 `tools/mech_audit.py`；`specs/015` 原器保留为战役存档，不改历史记录 | 指针可达；015 目录内容零改动 |
| FR-5 | 单元测试：FR-1 台账生成、FR-2 闭合/违例两态、FR-3 分类器与 diff 配对 | `python -m unittest discover -s tools/tests` 全绿 |

## 3. 口径与约束

1. **台账是工作底稿，不是门禁**：`--ledger` 只写文件，不改退出码；`--check-ledger` 独立入口，由会话在 s2.4 收口时手工调用（或写进批次脚本），不进 `check_all`。
2. **机器只填事实，不填判断**：骨架的 `d_class/exit/evidence/source/reviewer` 一律留空，由判读者填写；工具不得预填 D 类。
3. **回溯只产候选**（沿 2026-11-12 用户裁定）：`pure` 是“仅标点/空白变动”的签名，`conn` 是小词块补丁（术语换形常落此类），`susp` 须人工判读；任何一类都不得直接当违规处理。
4. **默认值安全**：`mech_audit` 不写入仓库内固定路径（默认落 `state/`，属运行态白名单目录）；`--since` 缺省不设下界，避免“只审某战役之后”的隐性遗漏。

## 4. 执行记录

见 [execution-log.md](execution-log.md)。
