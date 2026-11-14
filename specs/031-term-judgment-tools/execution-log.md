# 执行记录（specs/031）

## 2026-11-15 立项与落地

**授权**：用户「全部批准」（ADR-0048 跟进项 ①②）。

**产物**

| 项 | 文件 | 说明 |
| ---- | ---- | ---- |
| 规格 | `spec.md` | FR-1..FR-5 |
| 台账生成 | `tools/check_terms.py` `--ledger` | 定点核销时写 `sep-cn-term-ledger/1` 骨架，事实字段填好、判读字段留空 |
| 台账校验 | `tools/check_terms.py` `--check-ledger` | D 类／三出口／evidence／D3–D5 source／exempt reviewer；闭合 0，违例 1 |
| 回溯工具 | `tools/mech_audit.py` | 自 `specs/015-style-register-review/bin/mech_audit.py` 泛化迁入：去硬编码清单，增 `--since/--marker/--out`，默认输出 `state/mech-audit-latest.json`；分类器与「只产候选」纪律不变 |
| 测试夹具 | `tools/tests/fixtures/check_terms/ledger_registry.md` | 三行同「首现=demo」，覆盖 missing 与 ripple 两态 |
| 单元测试 | `tools/tests/test_check_terms.py`（+6）、`tools/tests/test_mech_audit.py`（+9） | 台账写出、参数错误、未填拒收、闭合通过、D3–D5 缺凭证拒收、exempt 缺复核人拒收、不可读文件；分类器三档与 diff 配对 |
| 规则指针 | `rules/03`（作业顺序→`tools/mech_audit.py`）、`rules/05`（工具表补 `mech_audit`、`check_terms` 行按双表与台账口径重写） | 单一事实源：工具行为以代码与 rules/05 为准 |

**验证**

* `python -m unittest tools.tests.test_check_terms tools.tests.test_mech_audit` → 27 tests OK。
* 冒烟（真实词条）：`--ledger state/… --docs a/abelard.md` 产出 1 行（Diderot missing），`--check-ledger` 未填 3 处违例、填 `D2/fix/evidence` 后 0 违例；临时件已删。
* `python tools/check_terms.py` → 硬错误 0（自洽 0）。

**口径声明**

1. 台账/校验均**不进 `check_all`**（ADR-0048 决策 8）：机器不判语境，台账闭合由 s2.4 收口时手工调用。
2. `mech_audit` 默认输出落 `state/`（运行态），不写 `specs/` 战役目录；`specs/015` 原器与历史记录零改动，保留为战役存档。
3. 本次未改任何译文与登记册内容。
