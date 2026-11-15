# s0 裁定表：字头 a（specs/036 §4.1，ADR-0052）

本表登记 s0 源审计（en_source_audit 告警）逐处定性；勘误类实体处置（就地勘误＋重转＋分歧账）属管线权属，此处仅登记候选与建议。

| # | 词条 | 告警 | 定性（ADR-0038 四类） | 处置建议 | 登记人 | 日期 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | abner-burgos | comma_no_space：`Rabbi Hasdai Crescas,who\nlater influenced Spinoza`（逗号后缺空格，HTML 渲染可见） | ①类 上游笔误 | 就地勘误 `Crescas,who`→`Crescas, who`；yuanwen 定点重转；分歧账登记 | A-rework-20261115 | 2026-11-15 |

已豁免/定性完毕不计行者（各词条 s0 evidence 已载）：

* autrecourt：punct_run `..`（拉丁引文省略号照录，非笔误）——豁免。
* antiochus-ascalon：heading_skip h2→h4（SEP 原生结构）——豁免（bauer 先例）。
* austin-john：heading_skip（同上豁免）；word_digit_eq `fall2021`（存档 URL 路径）——豁免。
* akan-person / advance-directives / albert-saxony / african-sage：heading_skip 或 0 告警——豁免/无。
