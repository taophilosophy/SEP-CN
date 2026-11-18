# baseline/en-template/ — T 类目：HTML 模板契约（卷内目录）

SEP 词条 HTML 模板的契约正典与例外登记区（ADR-0076）。库内无单一“模板文件”——契约由本目录承载：文字契约（`template-contract.md`）＋例外/变异登记册（`anomalies.json`）；契约的代码化在 `tools/parser.py`，判官在 `tools/en_source_audit.py` 与 `specs/044-b0b1-baseline/bin/`（B0 十谓词）。

| 文件 | 角色 | 写者 | 门禁 |
| ---- | ---- | ---- | ---- |
| `template-contract.md` | 模板契约正典：结构事实＋B0 十谓词＋转换映射＋例外登记口径 | specs/053 维护（修订走 ADR） | — |
| `anomalies.json` | 例外/变异登记册：上游原生（非缺陷）变异逐条人审登记（ADR-0070 建议④口径：豁免＝已人审后豁免，非免检） | specs/053 P2 起批次 | 判官消费（禁静默兜底） |

判据求值视图＝`en ⊕ [../en-patches/](../en-patches/)`（与 `yuanwen.convert_entry` 同源，ADR-0073 同源对照条）。
