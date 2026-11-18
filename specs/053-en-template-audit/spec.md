# 053 — EN 语料模板审计与勘误装配线

**版本** v1.0 ｜ **状态** P0 已执行、P1–P4 待批批次 ｜ **日期** 2026-11-19 ｜ **权威** 用户「批准053」（四阶段方案审定）＋「三族分目、目录结构执行国标等」（ADR-0076） ｜ **承接** specs/047（已批待实施）、ADR-0070 建议③④⑤、specs/044 B0/B1 全量基线

## 0. 方向声明（rules/08）

- **目标**：①三族审计产物分目（模板契约 T／补丁 P／勘误装配 E，ADR-0076）；②实施 specs/047 结构反向核验（堵 I2 自证盲区）；③B0 判据增强五项＋例外登记册落地；④新发现定性分流续批；⑤译注挂载批次＋挂载台账（勘误 ID→词条→圈号锚点）。
- **非目标**：不翻译（ADR-0072 边界）、不改 en/ 任何字节（ADR-0062）、不打破规则所有权（判据增强归 specs/044、白名单登记口径归 specs/039、判定权三权分立 ADR-0063）、不引入 LaTeX 中转层（ADR-0063 §7 否决）。
- **验收判据**：①047 判定器对负向样本（构造丢一节/丢一脚注 md）必报；②全量跑账本闭合（new 缺陷皆有四出口之一去向）；③每条新发现登记出口，无「机检全绿＝已验证」表述（ADR-0070）；④译注台账建立后勘误表每件「译注队列」可对应词条内实际圈号锚点，errata-apply 轴全绿；⑤check_all 全绿、提交推送、`origin/main..main` 为空。

## 1. P0 三族分目（已完成，2026-11-19）

目录形态＝**baseline/ 三类目平铺**（ADR-0076，用户三方案预览选定）：

```
baseline/
├─ en-template/     # T：template-contract.md（正典）＋anomalies.json（空册）＋README
├─ en-patches/      # P：原位不动（三律＋命中计数硬校验不变）
└─ en-errata/       # E：en-errata.md（自 specs/001 results 收编）＋divergences.json（自 baseline 根收编）＋README；note-anchors.json（P4 建账）
```

标准依据（组合推导，建书 2026-11-17 结论＋2026-11-19 条款回核）：**无国标直接规定仓库目录结构**；GB/T 26162-2021（等同 ISO 15489-1:2016）分类方案按职能分 T/P/E 三类目；DA/T 22-2015 §3.2 整理五步（组件＝一补丁一文件/一账一文件、分类＝三职能类目、排列＝节序、编号＝P-00N 档号、编目＝README 卷内目录）＋§5.4.1 档号五原则；GB/T 18894-2016 规范存储结构与元数据关联（layout.json 七问字段）；IEEE 828 受控库 vs 工作区分界（机检工作产物留 specs/*/results/）。

已修复引用面：代码常量 2（`check_pairs.ERRATA_PATH`、`divergence.DIV_PATH`）＋docstring 4（fetch_entry/compare/baseline_audit/en_source_audit）＋活文档（AGENTS.md、rules/README 判例＋标准清单、rules/04、rules/06、specs/001 contracts/cli.md、specs/036、specs/001 spec.md 历史指针）。补丁文件头与 INDEX 的 `source: en-errata.md §N` 为相对节号引用，迁移后仍有效，不动（补丁 sha 钉在 INDEX）。

## 2. P1 结构反向核验（实施 specs/047，判官只读）

- `specs/047-structural-reverse-check/bin/verify_structure.py`：md → 结构树（blocks：标题/脚注/图/表/公式块/列表）↔ HTML → 结构树（复用 `tools/parser.parse_entry`），五维比对（分节 h2/h3 数量与层级序列、脚注引用↔定义一一对应序一致、图表公式块数量与文档序、列表层级、citation/参考文献条目数）。
- 差异三类：真丢文（交人审）／合法移位（白名单须人审登记）／纯格式差。
- 判据先用测试词条（1–5）校准 → 负向测试（构造丢一节/丢一脚注 md，判定器必报）→ 评估全量 → 全量跑产 `results/structure-scan.json`。
- 边界：与 ADR-0063 §7 LaTeX 否决不冲突（stdlib `html.parser`＋自有 md 解析，无派生层）。

## 3. P2 B0 判据增强＋例外登记册（归属 specs/044 后续，specs/053 消费）

ADR-0070 建议③五项：节号连续性、pubinfo↔archinfo 交叉、math_delim 位置配对（非仅计数）、孤立可疑字符（悬空 `\)`/`\[`/`\` 残迹）、引用闭包接入 en_integrity。
例外登记册＝`baseline/en-template/anomalies.json`（空册已建）：B0 增强后新报上游原生变异逐条人审定性入册（upstream-native/judged-ok/exempt），登记三字段（谁审/何时/审什么）；已知变异类清单见 `template-contract.md` §9。

## 4. P3 定性分流续批

新发现逐条四出口：文字层→勘误表续批＋`divergence.py register`（机器账）；格式层→补丁池（C1–C4 全过）；转换器缺陷→改 `tools/yuanwen.py` 全量重转（禁只改产物）；上游原生→anomalies.json 登记。预期产出校正：B0 全量已闭合（new=0），新发现主要来自 P1 结构轴与 P2 判据增强；**勘误续批为主、补丁增长为辅**（044 实测：模板失败几乎全是文字层）。

## 5. P4 译注挂载批次＋台账

- 对受勘误影响的已译词条（有正文面）按 ADR-0065 圈号锚点挂译注；建 `baseline/en-errata/note-anchors.json` 台账：勘误 ID→slug→圈号序号→凭证行。
- errata-apply 机检收口（check_pairs 体例轴）；勘误表每件「译注队列」字样销账。
- 未来词条由 s2.4 勘误轴自然承载（判据已接线），台账只管存量挂载状态。

## 6. 边界与并行

- 术语轴（specs/008/050）与进度主战场不在本 spec；与并行会话共树作业遵守逐文件 staging 纪律。
- 批次开工立卡钉基准、列作废条件；新手段先小样本试金石；自报完成须独立复算（rules/08 §9–12）。
