# 全要素清单与审计证据（rev 10 复算）

- 用途：specs/064 rev 10 的事实底表；数字均为 2026-11-26 实读
- **时点注（rev 18）**：本表保留 rev 10 口径；测试、G4、G11、G15 与承载状态已由 rev 15／17 改写；流程 v2 见 `results/target-workflow.md` 与 spec §21；现行一律以 `spec.md` §2.7／§2.9 与 `results/test-coverage.md` 为准。
- 纪律：current 与 target 分列；“有值／N/A／未实现”分开；“待核”不用来掩盖未查
- 基点：`2ce7ac7fe`；工作树含他人既有 rev 9 改动，本轮已回读保留

## 1 节点（current 22，全非 retired）

| 节点 | prev | 类型 | gate owner | 判据 | 对象域 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ex-01 | — | pipe | ✓ | fetch_audit | source |
| ex-02 | ex-01 | pipe | ✓ | check_en_patches、divergence | conversion |
| ex-03 | ex-02 | pipe | ✓ | check_yuanwen_fidelity | conversion |
| ex-04 | ex-03 | pipe | ✓ | en_integrity、en_source_audit | source |
| ex-05 | ex-04 | format | ✗ | — | — |
| tr-01 | ex-05 | stage | ✗ | check_terms（辅助） | term |
| tr-02 | tr-01 | stage | ✗ | —（人工） | — |
| tr-03 | tr-02 | stage | ✓ | check_pairs | consistency |
| tr-04 | tr-03 | stage | ✓ | check_prose | grammar |
| tr-05 | tr-04 | format | ✗ | — | — |
| rv-01 | tr-05 | stage | ✓ | check_terms、errata_check（check_pairs 轴） | term |
| rv-02 | rv-01 | stage | ✓ | check_math_zh、check_quotes、check_tables_images、check_academic | 多域 |
| rv-03 | rv-02 | stage | ✗（T0） | cite_audit | cite |
| rv-04 | rv-03 | stage | ✗（T0） | logic_audit | logic |
| rv-05 | rv-04 | stage | ✗（T0） | grammar_audit | grammar |
| rv-06 | rv-05 | stage | ✗（T0） | register_audit | register |
| rv-07 | rv-06 | stage | ✗（T0） | measure_audit | measure |
| rv-08 | rv-07 | stage | ✗（T0） | punct_audit | punct |
| rv-09 | rv-08 | stage | ✓ | check_style、check_images、check_summary | format |
| sg-01 | rv-09 | review | ✗ | review-verity（人工） | review |
| sg-02 | sg-01 | review | ✗ | review-coherence（人工） | review |
| sg-03 | sg-02 | review | ✓ | ci_all（聚合） | aggregate |

复算：`len(json.load(open("rules/pipeline.json"))["nodes"]) == 22`。案 B 的 20＋2 是 target，不是现状。

## 2 判据（26）与承载体

- `criteria_owner` 去 `note` 后 26 键，值均为单元素。
- 例外承载体：`errata_check → check_pairs#errata-apply`（轴）、`review-verity`／`review-coherence`（人工）、`ci_all`（聚合）、`markdownlint`（外部告警）。
- **`errata_check` 不是“缺工具”**；其宿主与规则名均被 `check_stages` S5 和测试校验。

## 3 工具（96）与依赖

| 项 | 事实 |
| ---- | ---- |
| 文件 | 96 个 `tools/*.py`；55 个 `tools/tests/*.py` |
| 评级 | A26（25 A＋1 A+）／B29／C30／D10／包标记1 |
| 未评级/重复 | 已补 `campaign`、`summary_sync`；删除重复 `en_integrity` 行 |
| 直接非标准库导入 | `tl_crawler.py` → `cryptography`、`playwright`；其余 95 件未命中 |
| 门禁 | `check_all.py` 当前 21 项，开工实测全绿 |

复算方法：目录 glob＋AST 解析（不靠 grep 猜）；评级表按行解析并核对实际 stem。

## 4 规则（11 域／19 份）

`rules/*.md` 顶层是 10 个编号文件＋README；05 是目录，含 9 份约束性文档。故：

- 规则域：01–11 共 **11**；
- 约束性 Markdown：顶层 10＋`rules/05/` 9＝**19**（排除 README、ADR、reference）。

`applies_to` 目前不是规则头字段；是否建立、如何生成，属设计选择，不是事实。

## 5 规格卡（63）

| 形态 | 数 | 目录 |
| ---- | ---- | ---- |
| spec＋plan＋tasks | 6 | 001、002、003、006、060、064 |
| spec＋plan | 1 | 005 |
| 仅 spec | 56 | 其余；缺号 019（并入 021） |
| **合计** | **63** | — |

`specs/README.md` 是生成物，不手改。

## 6 阶段／战役／标记（063 设计）

- 阶段：60＝**34 实项＋26 预留**；案 B target＝32 非退役实项＋26 预留＋2 退役。
- 战役：6（设计值，不是 naming v1 已入册事实）。
- 标记：8（同上）。
- 当前 `rules/naming.json` 仍为 `sep-naming/v1`，未含 stages／campaigns／marks；不得把 063 设计当现状。

## 7 标准（96 条登记）

`rules/standards.json`：adopted 23／cited 60／not_adopted 8／deviations 5，合计 96。

- 身份、版本、采纳状态的单一源是该文件；条款细则在 `rules/10`。
- specs/061 §5 是 2026-11-25 的评估快照与证据，不是实时权威。
- 2026-11-26 官方复核：29148:2018 现行（2024 确认，DIS 在研）；15289:2019 现行（2025 确认，2026-06-11 转 90.92）；26514:2022 现行；25010:2023 为九特性、ICT／软件产品模型。
- 25010 不直接适用于译文质量；只能候选用于工具质量或显式类比。

## 8 缺口证据索引（详见 spec §2.7）

| 缺口 | 证据 |
| ---- | ---- |
| G1 源侧规则部分闭合 | `rules/11` 五节已立；T130 人工定性未完 |
| G2 两节点无判据 | pipeline 中 ex-05／tr-05 `criteria: []` |
| G3 `errata_check` | **关闭**：`criteria_carrier`＋`check_pairs#errata-apply`＋测试 |
| G4 测试薄 | 判据级完备 8/22；部分覆盖 8；ex-05 无判据无测试；T166 按 `results/test-coverage.md` 的 9 项 |
| G5 标准展示复制 | 061 §5／063 §1.3；源应为 standards.json＋rules/10 |
| G6 三件套判据 | 无成文判据；已立项 T167（G6＋G8 合并 ADR） |
| G7 工具—判据全量视图 | 判据侧已闭合；全量视图可生成，低优先 |
| G8 规则作用域 | 无 `applies_to`；已立项 T167 |
| G9 规则—阶段 | 设计上未关联，非必然缺陷 |
| G10 ADR 头 | 历史格式不均；不得改写历史 |
| G11 版本 | **部分闭合**：三项已核，登记回写（T169）未做 |
| G12 25010 | 不直接适用；可选类比 |
| G13 候选豁免 | rules/11 §5.3 已落地；人工定性与 ADR 待补 |
| G14 检测器噪声 | 单件 3/5 确定误报；不得外推为全局误报率 |
| G15 案 B 与 P12 | 退役 ex-05／tr-05 使 seg1／seg2 段尾失守；**已由裁定 A 关闭（案 B 不实施）** |
| G16 061 权威倒置 | 评估快照被当实时权威 |
| G17 证明有效性 | 旧文自相矛盾（称相容又承认红点） |
| G18 工具与依赖 | 评级表漏项／重复；直接依赖被“零依赖”掩盖 |
| G19 E2E 口径 | T130 未完成；原 18 行表已补为 22 节点；sg-03 需 mandate |
| G20 状态错位 | rev 5 头／rev 9 记录；任务粒度不一 |
| G21 无基线指标 | 30 s／50 ms／128 并发等无测量 |
| G22 063 模型缺陷 | CT3 前提误指 CT5；AX1 被 AX2 蕴含；CT7 族数不符 |
| G23 登记表设计 | 裁定不建表（2026-11-26）；只留 `clean --check` |
| G24 AGENTS 5 秒旧约束 | ADR-0069 已废除；已立项 T168 |
| G25 规则入口旧口径 | rules/README 写 P1–P28；naming authority 引 12207:2017；已立项 T168 |

本表不授权实施；G15 已由裁定 A 关闭，案 B 不实施。

**承载追溯（rev 17 更新；原 rev 12 文字保留在下）**：G4→T166（按 `results/test-coverage.md` 的 9 项）、G6／G8→T167、G11→T169（部分闭合）、G24／G25→T168；G14 仍无现成工作项；G23 关闭（不建表）。原 rev 12 曾写“G4／G6／G8／G14／G24／G25 无现成工作项”，已被 rev 15 取代。
