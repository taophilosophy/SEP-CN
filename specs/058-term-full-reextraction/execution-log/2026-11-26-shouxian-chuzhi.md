# 首现待核 25 行处置（2026-11-26）

**范围**：`shu-yu-biao.md` 首现列含“待核”的 25 行（原记 23 行，后新增 2 行）。

**处置**（凭证 `../results/first-pending-disposition-2026-11-26.tsv`）：

| 组 | 条数 | 处置 |
| --- | --- | --- |
| 甲 | 8 | 源文有该词（变体形），首现改记为实际 slug：john-italos（erōtapokriseis）、gorampa（Evaṃ Chöden）、spacetime-convensimul（foliation 补充材料）、philo（kalos kagathos 分写）、contradiction（saptabhangi）、logic-india（syadvada）、literal-nonliteral-india（syat）、ehrenfels（zahlenfiguren） |
| 乙 | 14 | 全库去变音变体匹配仍未见原词（耆那术语为主），首现改“文献补编（源文未见原词，2026-11-26 核）” |
| 丙 | 3 | 仅见复合形或他义（kevala／nonsectarian movement／śruta-jñāna），不充首现，保持待核并在依据列注明 |

**方法复核**：先按 NFD 去变音符、撇号归一、连字符/空格互换、键元全覆盖做全库匹配；甲组 8 条逐条去变音复算命中（子代理初判与主代理字面 grep 的差异全部来自变音与分写）。

**发现（供 058 后续批次）**：既有首现含词审计（`bin/audit_first_contains.py`）只用键名前 5 字符作前缀且只查首现 slug，跨条目与变体形会漏；本次处置已按“全库 + 去变音”口径覆盖，建议该审计器下一轮采用同口径。

**幂等**：处置脚本二跑 0 行；处置前 25 行依据列均无“首现待核处置 2026-11-26”标记。
