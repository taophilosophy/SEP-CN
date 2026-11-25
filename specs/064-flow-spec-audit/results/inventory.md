# 全要素清单与审计证据（实读，2026-11-26）

- 用途：specs/064 rev 2 的附表；每条附复算方式，便于独立复核
- 纪律：数字均为当次实读，不做推演；“待核”项显式标注

## 1 节点（22，案 B 后 20 活跃＋2 退役）

| 节点 | prev | 类型 | gate | 对象域 | 判据（owner 一致） | 案 B |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ex-01 | — | pipe | ✓ | source | fetch_audit | 活跃 |
| ex-02 | ex-01 | pipe | ✓ | conversion | check_en_patches、divergence | 活跃 |
| ex-03 | ex-02 | pipe | ✓ | conversion | check_yuanwen_fidelity | 活跃 |
| ex-04 | ex-03 | pipe | ✓ | source | en_integrity、en_source_audit | 活跃 |
| ex-05 | ex-04 | format | ✗ | — | **无** | **退役→rv-09** |
| tr-01 | ex-05 | stage | ✗ | term | check_terms | 活跃 |
| tr-02 | tr-01 | stage | ✗ | — | 无（人工） | 活跃 |
| tr-03 | tr-02 | stage | ✓ | — | check_pairs | 活跃 |
| tr-04 | tr-03 | stage | ✓ | — | check_prose | 活跃 |
| tr-05 | tr-04 | format | ✗ | — | **无** | **退役→rv-09** |
| rv-01 | tr-05 | stage | ✓ | term | check_terms、errata_check（缺工具） | 活跃 |
| rv-02 | rv-01 | stage | ✓ | — | check_math_zh、check_quotes、check_tables_images、check_academic | 活跃 |
| rv-03 | rv-02 | stage | ✗ | — | cite_audit | 活跃 |
| rv-04 | rv-03 | stage | ✗ | — | logic_audit | 活跃 |
| rv-05 | rv-04 | stage | ✗ | — | grammar_audit | 活跃 |
| rv-06 | rv-05 | stage | ✗ | — | register_audit | 活跃 |
| rv-07 | rv-06 | stage | ✗ | — | measure_audit | 活跃 |
| rv-08 | rv-07 | stage | ✗ | — | punct_audit | 活跃 |
| rv-09 | rv-08 | stage | ✓ | format | check_style、check_images、check_summary | 活跃（**净增 11 项**） |
| sg-01 | rv-09 | review | ✗ | — | review-verity（无工具，白名单） | 活跃 |
| sg-02 | sg-01 | review | ✗ | — | review-coherence（无工具，白名单） | 活跃 |
| sg-03 | sg-02 | review | ✓ | aggregate | ci_all（聚合，白名单） | 活跃 |

复算：`python -c "import json;d=json.load(open('rules/pipeline.json'));print(len(d['nodes']))"`

## 2 判据（26）

复算：`criteria_owner` 去 `note` 后键数。

| 判据 | owner | 有工具 | 有单测 |
| ---- | ---- | ---- | ---- |
| fetch_audit | ex-01 | ✓ | ✓ |
| check_en_patches | ex-02 | ✓ | ✓ |
| divergence | ex-02 | ✓ | ✓ |
| check_yuanwen_fidelity | ex-03 | ✓ | **✗** |
| en_integrity／en_source_audit | ex-04 | ✓ | ✓ |
| check_terms | tr-01、rv-01 | ✓ | ✓ |
| check_pairs | tr-03 | ✓ | **✗** |
| check_prose | tr-04 | ✓ | ✓ |
| errata_check | rv-01 | **✗** | ✗ |
| check_math_zh／check_quotes／check_tables_images／check_academic | rv-02 | ✓ | 部分 |
| check_style／check_images／check_summary | rv-09 | ✓ | ✓ |
| cite_audit | rv-03 | ✓ | ✗ |
| logic_audit | rv-04 | ✓ | ✗ |
| grammar_audit | rv-05 | ✓ | ✗ |
| register_audit | rv-06 | ✓ | ✗ |
| measure_audit | rv-07 | ✓ | ✗ |
| punct_audit | rv-08 | ✓ | ✗ |
| review-verity／review-coherence | sg-01／sg-02 | ✗（白名单） | — |
| ci_all | sg-03 | ✗（聚合） | — |

注：`check_terms` 出现两个 owner（tr-01 辅助、rv-01 硬拦）——AX20 单元素要求下，须在 `criteria_owner` 层明确“硬拦 owner＝rv-01”，tr-01 的挂载标 `assist`（当前结构是节点 criteria 列表并列，需实施时区分）。

## 3 工具（96）

| 类 | 数 | 代表 |
| ---- | ---- | ---- |
| check 判据 | 24 | check_all、check_stages、check_style、check_terms… |
| 术语 | 15 | term_*、register_*、tl_*（术语在线） |
| 审计 | 12 | en_source_audit、cite_audit、logic_audit、grammar_audit、register_audit、measure_audit、punct_audit、indep_review、qchain、mech_audit、drift_scan、roundtrip_drift |
| task／journal | 11 | task_ops、progress、journal_*、wipe_*、migrate_*、replay_state、mandatory_backfill |
| fetch／sync | 10 | fetch、fetch_all、fetch_catalog、fetch_entry、compare、detect_updates、catalog_drift、sync_guard、sync_official_snapshot |
| en／convert | 7 | en_integrity、en_patch_lib、yuanwen、parser、extract_text、divergence、wipe_history（记录类） |
| lib／其他 | 17 | common、naming_lib、register_lib、axis_lib、spec_index、standards_table 等 |

复算：`ls tools/*.py | wc -l`

## 4 规则（10）与作用面

见 spec §2.4 表。机检现状：`grep -c "applies_to" rules/*.md`＝0（全部无声明）。

## 5 文档（64 卡）

| 类 | 数 | 判据 |
| ---- | ---- | ---- |
| 三件套齐全（工具型） | 5 | 001、002、003、006、060 |
| spec＋plan | 1 | 005 |
| 单卡 | 56 | 其余 |
| 含 contracts | 5 | 001、006、008、012、054 |

复算：`for d in specs/*/; do ...`（见 spec §1）

## 6 阶段（60）与战役（6）、标记（8）

见 specs/063 §1.3／§1.4／§1.8。案 B 后：1.3.4、2.5 转 retired；活跃 58。

## 7 标准（96 条登记）

见 `standards-map.md`。

## 8 缺口证据索引

| 缺口 | 证据命令或位置 |
| ---- | ---- |
| G1 源侧规则真空 | `for id in ex-01 ex-02 ex-03 ex-05 tr-05; do grep -rl "$id" rules --include=*.md; done` → 仅 ex-01 命中 ADR-0080 |
| G2 三无节点 | pipeline.json 中 ex-05／tr-05 `criteria: []`；rules 零条款；测试零覆盖 |
| G3 errata_check | `ls tools/errata_check.py` → 不存在 |
| G4 测试薄 | `ls tools/tests/*.py` 55 文件，覆盖判据 7 项 |
| G5 标准双写 | specs/061 §5（22 行）与 specs/063 §1.3 标准列并存 |
| G6 三件套判据 | `.specify/templates/` 有模板，但 `rules/` 与 `specs/README.md` 无判据 |
| G7 判据—工具映射 | 无登记表，靠 `replace('-','_')` |
| G8 规则作用面 | `grep -c applies_to rules/*.md`＝0 |
| G9 规则↔阶段 | 063 stages 条目无 `rules` 字段 |
| G10 ADR 头 | 88 份中 28 份匹配 `^状态：` |
| G11 版本待核 | 061 `version-audit.md` 第 47／48 行 |
| G12 质量模型 | standards.json 无 25010 条目 |
