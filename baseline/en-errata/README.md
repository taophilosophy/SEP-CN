# baseline/en-errata/ — E 类目：勘误装配（卷内目录）

英文侧缺陷登记与承载的装配区（ADR-0076 三类目制）。格式层补丁在 [../en-patches/](../en-patches/)（P 类目），模板契约在 [../en-template/](../en-template/)（T 类目）。

| 文件 | 角色 | 写者 | 门禁 |
| ---- | ---- | ---- | ---- |
| `en-errata.md` | 全局勘误表：上游缺陷唯一人读登记处（ADR-0062 决策 3；自 `specs/001-sep-sync-pipeline/results/` 收编） | 各战役会话（人审登记） | `check_pairs` errata-apply 轴（中文承载校验） |
| `divergences.json` | 分歧账（机器账）：ADR-0045 双账语义，只承载上游真变（carry）与审计面（自 `baseline/` 根收编） | `tools/divergence.py` | `divergence.py verify`（check_all 第 10 项） |
| `note-anchors.json` | 译注挂载台账：勘误 ID→词条→圈号锚点（specs/053 P4 产物，建账时落盘） | specs/053 P4 批次 | `check_pairs` note-anchor |

纪律：

- en/ 绝对冻结（ADR-0062）：本目录只登记，不改 en/ 任何字节。
- 人读册与机器账由不同批次分别登记是常态；修账前先 grep 对方册勿重复写行（ADR-0045 先例）。
- 条目引用勘误表节号（§一…）；补丁档号 `P-00N` 沿 DA/T 22-2015 §5.4.1 档号五原则（唯一性、合理性、稳定性、扩充性、简单性）。
- 历史节（§一至§十）中的既有引用与凭证一律原样保留；本目录变更走 [ADR-0076](../../rules/adr/0076-英文侧审计产物三类目制.md)。
