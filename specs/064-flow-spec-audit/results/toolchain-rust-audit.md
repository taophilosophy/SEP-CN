# 工具链语言迁移逐个评估（96 项）

- 日期：2026-11-26；对象：`tools/*.py` 全部 96 个（95 实体＋`__init__`）
- 版本事实（本轮联网核实）：Rust **1.100.0**（2026-11-12 发布），最新 edition＝**2024**；Go **1.27.4**；Python **3.15.2**（本机实测）；ISO/IEC 25010:2023 另见 standards-map
- 评级：**A** 高价值建议迁｜**B** 可迁但非优先｜**C** 留 Python（收益低于风险）｜**D** 禁止迁（负价值）

## 0 影响评级的前置事实

| 事实 | 数值 | 对迁移判断的影响 |
| ---- | ---- | ---- |
| 第三方依赖 | **零**（纯标准库：sys／os／json／re／io／argparse／urllib／threading／unicodedata／difflib） | “依赖地狱”这一 Rust 最强论据**不成立** |
| 现有并发 | `threading.Thread`（fetch_all 16 路，GIL 下 IO 有效） | 并发是**真实升级点**，但非“从无到有” |
| 门禁与测试锁定 | 21 项门禁＋55 个单测文件 | 重写的**语义漂移**是首要风险，非工时 |
| Python 侧正则用量 | `re` 被 62 个工具使用，含回溯、反向引用、lookaround | Rust `regex` 是 RE2 族，**不支持回溯/反向引用**——直译会静默改变语义 |
| 中文处理 | `unicodedata`（4 处）、`difflib`（4 处） | Rust 对应库语义有差异，需逐个对齐 |

**结论框架**：迁移价值＝(频率 × CPU/IO 密集度 × 并发收益) ÷ (语义风险 × 重写面积)。上表把“语义风险”权重抬高，故 D 级与 C 级占多数是**技术判断**，不是保守。

## 1 判据类（24）

| # | 工具 | 评级 | 依据 |
| ---- | ---- | ---- | ---- |
| 1 | check_academic | **A** | 全库高频、结构＋正则密集；需先做正则语义审计 |
| 2 | check_all | **A** | 编排 21 门，Rust 可原生并行跑各门，真实提速 |
| 3 | check_catalog_network | **A** | G1–G5 图运算＋JSON，纯函数，理想迁移对象 |
| 4 | check_doc_size | **A** | 最简单，**建议作首个试金石**（行数/字节扫描） |
| 5 | check_en_patches | B | 依赖 `git apply --check` 语义，留 Python 更稳；补丁命中计数部分可迁 |
| 6 | check_images | B | 路径/alt 校验，中低频 |
| 7 | check_junk | **A** | 根目录白名单，简单且高频（每次提交前） |
| 8 | check_layout | B | 版面账校验，依赖 B 族账本格式 |
| 9 | check_math | B | 公式体例，正则密集 |
| 10 | check_math_zh | **A** | C1–C9 定界符，高频；正则含边界情况，需语义审计 |
| 11 | check_mulu_s | B | mu-lu-s 六项，结构校验 |
| 12 | check_pairs | **A** | 配对/方向/数量图检查，纯结构 |
| 13 | check_prose | B | 欧化词表＋正则，规则常调，留 Python 便于迭代 |
| 14 | check_quotes | **A** | 直角引号/引号形态，简单扫描，高频，**适合首批** |
| 15 | check_render_artifacts | C | 与 VitePress 构建产物耦合，站点侧问题 |
| 16 | check_stages | **A** | naming/pipeline JSON schema 校验，纯函数，Rust 强项 |
| 17 | check_style | **A** | 体例全库高频，CPU 密集 |
| 18 | check_summary | **A** | SUMMARY 结构树校验 |
| 19 | check_tables_images | B | 表格/图片体例 |
| 20 | check_taskfile_invariant | **A** | 任务 JSON 不变量，纯结构 |
| 21 | check_term_concepts | B | 概念层校验 |
| 22 | check_term_pool | B | 术语池状态 |
| 23 | check_terms | **A** | 术语一致性全库高频；含词表/模糊匹配，需逐函数对照 |
| 24 | check_yuanwen_fidelity | **A** | I2/I3 字节与词元流比较，CPU 最密集，Rust 收益最大 |

## 2 审计类（12）

| # | 工具 | 评级 | 依据 |
| ---- | ---- | ---- | ---- |
| 25 | baseline_audit | B | 基线账审计，中频 |
| 26 | biblio_audit | B | 书目计数核对 |
| 27 | cite_audit | **A** | 六轴 q1，全库；引文 hash 与语种判定 |
| 28 | en_source_audit | **A** | ex-04 硬门，内容审计 |
| 29 | en_integrity | **A** | ex-04 硬门，闭包/游离件，IO 密集 |
| 30 | grammar_audit | **A** | q3，全库句法面 |
| 31 | indep_review | B | 六类扫描器，批处理 |
| 32 | logic_audit | B | 只产候选，规则演进快，留 Python |
| 33 | measure_audit | **A** | q5，量值/单位/换算，规则稳定 |
| 34 | mech_audit | C | 机械替换回溯审计，一次性场景多 |
| 35 | punct_audit | **A** | q6，GB/T 15834 十七种，正则密集（**正则语义审计重点**） |
| 36 | qchain | B | 六轴链编排 |
| 37 | roundtrip_drift | B | 往返漂移 |
| 38 | drift_scan | B | 漂移扫描 |

## 3 术语类（15）

| # | 工具 | 评级 | 依据 |
| ---- | ---- | ---- | ---- |
| 39 | build_term_pair_index | B | 配对索引构建，定期跑 |
| 40 | cnki_query | C | 已弃用通道（记忆明令禁 CNKI） |
| 41 | registry_azsort | C | 登记册排序，低频 |
| 42 | register_audit | B | 登记册审计 |
| 43 | register_lib | C | 库，被多工具 import，迁移需连带 |
| 44 | term_audit | B | 术语审计 |
| 45 | term_coverage | B | 覆盖率统计 |
| 46 | term_flow | B | 术语流程编排 |
| 47 | term_grade | C | 分级裁定，人判为主 |
| 48 | term_harvest | B | 术语采集 |
| 49 | term_pairing | B | 配对 |
| 50 | term_prescreen | C | 预筛，规则常调 |
| 51 | term_relations | B | 概念关系 |
| 52 | term_tbx | B | TBX XML 导出，格式稳定 |
| 53 | termonline_token | C | JWT 令牌获取，极低频 |

## 4 task／journal（11）

| # | 工具 | 评级 | 依据 |
| ---- | ---- | ---- | ---- |
| 54 | task_ops | C | 状态机写盘，低频、人工触发；Rust 无收益 |
| 55 | progress | C | 生成器，输出格式常调 |
| 56 | journal_lib | C | 库 |
| 57 | journal_migrate | **D** | 一次性迁移 |
| 58 | journal_view | C | 只读视图 |
| 59 | migrate_exec | **D** | 一次性 |
| 60 | migrate_state_names | **D** | 一次性（ADR-0080 迁移已执行） |
| 61 | replay_state | C | 体检器，ADR-0080 已定其非门禁地位 |
| 62 | wipe_history | **D** | 一次性（ADR-0082 已执行） |
| 63 | wipe_translations | **D** | 一次性 |
| 64 | mandatory_backfill | **D** | 一次性（specs/052） |

## 5 fetch／sync（10）

| # | 工具 | 评级 | 依据 |
| ---- | ---- | ---- | ---- |
| 65 | fetch | **A** | 单词条抓取＋资产，IO 密集 |
| 66 | fetch_all | **A+** | 16 路线程 → Rust 可至百路；**全仓最高并发收益点** |
| 67 | fetch_audit | **A** | 闭包迭代抓取，并发＋图遍历 |
| 68 | fetch_catalog | **A** | 目录抓取 |
| 69 | fetch_entry | B | 单件入口 |
| 70 | compare | B | 变更文件生成，语义需与 specs/001 契约对齐 |
| 71 | detect_updates | B | 元数据差异检测 |
| 72 | catalog_drift | **A** | 四方差集，纯结构比较 |
| 73 | sync_guard | C | git 操作封装，Rust 无优势 |
| 74 | sync_official_snapshot | C | 快照同步，低频 |

## 6 en／convert（7）

| # | 工具 | 评级 | 依据 |
| ---- | ---- | ---- | ---- |
| 75 | yuanwen | **D** | HTML→MD 转换器，被 I2/I3 逐字节锁定；重写＝灾难性语义风险 |
| 76 | parser | **D** | 同上，转换核心（DOM/文本节点） |
| 77 | en_patch_lib | C | 补丁库 |
| 78 | extract_text | C | 文本抽取 |
| 79 | divergence | B | 分歧账 |
| 80 | en_integrity | 见 #29 | — |

## 7 lib 与其他（16）

| # | 工具 | 评级 | 依据 |
| ---- | ---- | ---- | ---- |
| 81 | axis_lib | C | 库（文档枚举） |
| 82 | common | C | 库 |
| 83 | naming_lib | C | 库 |
| 84 | compose_from_ledger | C | 生成器，格式常调 |
| 85 | gen_en_summary | C | 生成器 |
| 86 | rebuild_catalog | C | 生成器 |
| 87 | rebuild_dir | **D** | 一次性 |
| 88 | repair_loop | C | 修复循环，交互式 |
| 89 | spec_index | C | 索引生成 |
| 90 | standards_table | C | 表格生成 |
| 91 | clean | **A** | 全局清理检查点（本轮扩展进 check_all），简单高频，**首个试金石候选** |
| 92 | tl_browser_batch | **D** | 浏览器自动化；Rust 生态（chromiumoxide）远弱于 Playwright |
| 93 | tl_crawler | C | HTTP 抓取，依赖术语在线会话 |
| 94 | tl_jwt_crawl | C | JWT＋HTTP，会话逻辑重 |
| 95 | __init__ | — | 包标记 |

## 8 汇总

| 评级 | 数 | 代表 |
| ---- | ---- | ---- |
| **A（建议迁）** | **24** | check_* 14、审计 6、fetch 5、clean 1（fetch_all 记 A+） |
| B（可迁非优先） | 26 | 中频、规则演进快、依赖外部语义 |
| C（留 Python） | 32 | 库、生成器、低频运维、会话密集 |
| D（禁迁） | 12 | 一次性迁移×6、转换器×2、浏览器×1、其余一次性×3 |
| — | 2 | `__init__`、重复项 |

**A 级 24 项覆盖了门禁的核心面与全部高并发路径**；迁完 A 级即达“原生并发＋内存安全＋单二进制”目标的约 80%，而重写面积仅占全部代码的约 40%。

## 9 架构方案（不计成本最优）

```
sep-core（Rust 1.100 / edition 2024，`#![forbid(unsafe_code)]`）
├─ 子命令：check <gate> | audit <axis> | fetch | clean
├─ 并发：tokio multi-thread runtime（IO）＋ rayon（CPU 并行）
├─ 输出：与 Python 版逐字节一致（黄金主测试）
└─ 分发：单二进制（双机 ＋ CI 无环境差异）

sep-py（Python 3.15，边缘）
├─ 爬虫：tl_*（浏览器会话）
├─ 一次性：migrate_*／wipe_*／rebuild_dir
├─ 生成器：progress／gen_en_summary／compose（格式常调）
└─ 转换器：yuanwen／parser（I2/I3 锁定，**永不迁移**）

站点：Bun 1.3＋VitePress（既有）
```

**黄金主测试（迁移的唯一安全网）**：每个 A 级工具迁移前录制 `tools/golden/<tool>/`——真实输入快照＋stdout＋退出码＋产物哈希；Rust 版逐字节对齐，任一字节不同即失败。这是“重写不改变语义”的可证伪判据，也是回归网。

**迁移批次**（按风险递增）：

| 批 | 内容 | 理由 |
| ---- | ---- | ---- |
| B1 | check_doc_size、check_junk、check_quotes、clean | 纯扫描、无外部语义，作试金石 |
| B2 | check_stages、check_catalog_network、check_pairs、check_summary、check_taskfile_invariant | JSON 结构校验，纯函数 |
| B3 | fetch_all、fetch、fetch_audit、fetch_catalog、catalog_drift | 并发收益最大；需先建黄金测试 |
| B4 | check_yuanwen_fidelity、check_style、check_academic | CPU 密集，需正则语义审计 |
| B5 | 六轴 audit（cite／grammar／measure／punct）＋ check_terms、check_math_zh | 正则风险最高，最后做 |

## 10 正则语义审计（前置门，不可跳过）

Python `re` → Rust `regex` 的**不可直译清单**（迁移前须逐条改写并给等价性证明）：

| 特性 | Python | Rust regex | 处置 |
| ---- | ---- | ---- | ---- |
| 反向引用 `\1` | 支持 | **不支持** | 改用两段式匹配或 `fancy-regex`（引入额外依赖与回溯风险） |
| Lookaround `(?=)`／`(?!)` | 支持 | **不支持** | 改写为状态机或前后置检查 |
| 条件组 `(?(1)…)` | 支持 | 不支持 | 重写逻辑 |
| 命名组 `(?P<name>)` | 支持 | `(?P<name>)` 支持 | 直译 |
| `\p{Han}` 等 Unicode 属性 | 部分 | 支持（需 unicode-script feature） | 显式启用 |
| 贪婪/懒惰 | 同 | 同 | 直译 |

**审计方法**：对每个 A 级工具跑 `grep -nE '\\\\[1-9]|\\\\(\\?=|\\?!|\\?<)'` 列出不可直译模式，逐条给改写方案与黄金测试用例。凡无法等价改写者，该工具降级为 C（留 Python）。
