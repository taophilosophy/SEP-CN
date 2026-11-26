# 节点级测试覆盖矩阵（T166 执行前复算）

- 日期：2026-11-26（064 rev 17）；状态：**只读复算，不执行 T166、不新增测试**
- 用途：替换 rev 1 的“测试 7/22／15 节点无单测”旧口径；T166 按本文件的 9 项缺口拆分原子任务
- 方法：AST 提取 `tools/tests/test_*.py` 的导入与 `test_*` 方法；`python -m unittest discover -s tools/tests` 实测 **709 个测试 OK**；逐节点对照 `rules/pipeline.json` 的判据
- 判定口径：**判据级完备**＝该节点每个判据至少有 1 个正例与 1 个反例；**部分**＝有测试但缺正例、反例或子规则；**N/A**＝无判据、人工签字或聚合门禁。判据级完备不表示子规则穷尽。

## 1 矩阵（22 节点）

| 节点 | 判据 | 现有测试证据 | 正例 | 反例 | 判定 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ex-01 | fetch_audit | `test_fetch_audit`（3 例：裸资产、注释/实体、垃圾形态） | 有 | 有 | 判据级完备 |
| ex-02 | check_en_patches、divergence | `test_en_patch_pool`（8）、`test_en_patches_dir`（19）、`test_en_patch_reverse`（4）、`test_divergence`（16） | 有 | 有（缺失/畸形即拒） | 判据级完备 |
| ex-03 | check_yuanwen_fidelity | `test_yuanwen_fidelity`（25）、`test_yuanwen_backslash`（8）、`test_yuanwen`（88，转换侧） | 有 | 有（未闭合/超长跨度） | 判据级完备 |
| ex-04 | en_integrity、en_source_audit | `test_en_integrity`（19）、`test_en_source_audit`（10） | 有 | 有（clean page／clean package） | 判据级完备 |
| ex-05 | —（`rules/11` §6 八项格式清单） | 无 | — | — | 无判据/无测试；T166 补格式闭合 |
| tr-01 | check_terms（辅助） | `test_check_terms`（42） | 有 | 有（匹配行静默通过） | 判据级完备 |
| tr-02 | —（人工初译） | 无 | — | — | N/A（人工） |
| tr-03 | check_pairs | `test_adr0063`（39）、`test_greek_style`（9） | 有 | 有 | **部分**：6 项硬规则中 `pubinfo-form` 行为未单测；子规则未穷尽 |
| tr-04 | check_prose | `test_check_prose`（18） | 有 | 有（干净中文/豁免） | 判据级完备 |
| tr-05 | —（人工/段内格式） | 无 | — | — | N/A（无判据） |
| rv-01 | check_terms、errata_check | `test_check_terms`（42）、`test_adr0063`（errata 与节级承载） | 有 | 有 | 判据级完备 |
| rv-02 | check_math_zh、check_quotes、check_tables_images、check_academic | `test_greek_style`（C10）、`test_check_quotes`（6）、`test_check_academic`（20）；`check_tables_images` 无测试 | 部分 | 部分 | **部分**：`check_tables_images` 无测试；`check_math_zh` 仅 C10 |
| rv-03 | cite_audit | `test_six_axis.test_cite_scan_finds_quote` | 有 | 无 | **部分**：缺干净样本、边界与 Unicode |
| rv-04 | logic_audit | `test_six_axis.test_logic_skeleton_covers_sentences`、`test_logic_trivial_channel` | 有 | 有（trivial） | **部分**：缺边界与 Unicode |
| rv-05 | grammar_audit | `test_six_axis.test_grammar_false_positive_whitelist` | 无 | 有 | **部分**：缺正例、边界与 Unicode |
| rv-06 | register_audit | `test_six_axis.test_register_flags_classical_and_you` | 有 | 无 | **部分**：缺反例、边界与 Unicode |
| rv-07 | measure_audit | `test_six_axis.test_measure_flags_missing_space` | 有 | 无 | **部分**：缺反例、边界与 Unicode |
| rv-08 | punct_audit | `test_six_axis.test_punct_flags_ascii_quote_and_ellipsis` | 有 | 无 | **部分**：缺反例、边界与 Unicode |
| rv-09 | check_style、check_images、check_summary | `test_check_style`（19）、`test_check_images`（12）、`test_check_summary_headers`/`test_check_summary_nav`（13，子进程） | 有 | 有 | 判据级完备 |
| sg-01 | review-verity（人工） | 无 | — | — | N/A（人工签字） |
| sg-02 | review-coherence（人工） | 无 | — | — | N/A（人工签字） |
| sg-03 | ci_all（聚合） | `test_check_all`（5，CLI 面） | — | — | N/A（聚合；门禁/CI 覆盖） |

## 2 汇总

| 类别 | 节点数 | 节点 |
| ---- | ---- | ---- |
| 判据级完备 | 8 | ex-01–04、tr-01、tr-04、rv-01、rv-09 |
| 部分覆盖 | 8 | tr-03、rv-02、rv-03–08 |
| 无判据/人工/聚合 | 6 | ex-05、tr-02、tr-05、sg-01–03 |

**T166 缺口清单（9 项）**：`tr-03`（check_pairs 全规则正反例）、`rv-02`（check_tables_images 与 check_math_zh 全规则）、`rv-03`–`rv-08`（六轴各补正反例＋边界/Unicode）、`ex-05`（`rules/11` §6 八项格式闭合）。`sg-01`–`sg-03` 不按单测补齐，写 N/A 理由。

## 3 与旧口径的差异

- rev 1 写“仅 ex-01／02／04／tr-01／tr-04／rv-02／rv-09 有可识别单测，测试 7/22，其余 15 节点无单测”。复算证明该表漏计 ex-03、rv-01、tr-03、rv-03–08：`test_yuanwen_fidelity`、`test_check_terms`、`test_adr0063`、`test_six_axis` 均已在库。
- 旧“7/22”与存档矩阵 `spec.md` §3.4 的“7/20”也不一致：该表内实际有 8 个 ✓。两项计数均撤销，不再引用。
- 本矩阵只证明“现有测试证据”的分布，不证明测试质量足以替代人审；T166 执行时仍按“每判据至少一正一反、六轴另加边界与 Unicode”验收。

## 4 复算凭证

| 检查 | 命令（摘要） | 结果 |
| ---- | ---- | ---- |
| 全量单测 | `python -m unittest discover -s tools/tests` | Ran 709 tests，OK |
| 测试方法清单 | AST 遍历 `tools/tests/test_*.py` | 55 个测试文件；方法名见各文件 |
| 判据清单 | `rules/pipeline.json` 的 `nodes[].criteria` | 26 判据、27 挂载项（`note` 不计） |
| 节点数 | `len(pipeline["nodes"])` | 22 |

本文件是 T166 的**执行前清单**，不是完成证据；不授权新增测试、不改任务状态。
