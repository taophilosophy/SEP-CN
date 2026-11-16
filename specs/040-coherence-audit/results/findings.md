# findings：全系统融洽性审计问题清单（specs/040）

唯一问题清单文件（用户指定"列举到某个文件中"）。严重度：**P1**＝架构级矛盾（本次为零）；**P2**＝应修（口径相反/越界转移/门禁漂移）；**P3**＝登记（陈旧、错引、死条目）。每条带证据位置；计算器 `bin/audit_coherence.py` 产出 `audit-report.json` 佐证。修复均待用户/治理会话裁定，本清单不改动任何文件。

## A. 状态机 LTS（tools/task_ops.py 实现 vs tasks/README.md 声明）

* **F-01 [P2] update 任务可漂入 retranslate 专用态**。`advance` 只校验当前态 ∈ ORDER[kind]（task_ops.py:167-168），不校验目标态：update 任务在 s0_source_checked 后可执行 `--step draft`，状态落 `drafted`——该态不在 update 声明序列（tasks/README.md:36-39）。计算实证：viol_target＝{"kind":"update","from":"s0_source_checked","step":"draft","to":"drafted"}。修法一行：advance 内加"目标态 ∈ ORDER[kind]"前置。
* **F-02 [P2] expect 元组是并集语义，"禁跳步"在两处弱化**。STEP_EXPECT_PREV（task_ops.py:55-62）以 tuple 表达"按 kind 的前驱"，但实现是 `cur not in expect`（task_ops.py:161-166）＝任意 kind 可取任一元素：retranslate 任务可 pending→s0（**跳过 clear 及其基线哈希 gate**）、可 s0→s1（**跳过 draft 初译**）。tasks/README.md:56 注释（"retranslate 在 cleared 后、update 在 pending 后"）只是意图非约束。修法：按 kind 分解 tuple 或加 kind 判定。
* **F-03 [P3] audit 别名死条目**。task_ops.py:157-158 先把 `audit` 归一为 `s25` 再查表，STEP_EXPECT_PREV["audit"]="s2_checked"（:59）永不读取，且其字面值（s2_checked）与实际生效语义（须 s2.4 前驱）不符。登记后删除或改注。
* **F-04 [P2] revert 口径两处文档滞后 ADR-0063**。tasks/README.md:60 与 contracts/cli.md:78 仍写"仅 s3_checked 及其后"；ADR-0063 已扩目标态 `s2.4_termchecked`、源态集扩 `s2.5_checked`（rules/04:16 与 task_ops.py:307-326 已改）。
* **F-05 [P3] update s2.4 作用域概括失真**。tasks/README.md:37 "s2.4_termchecked（仅变更段）" vs rules/04:14/63 "术语轴仅变更段；**体例轴与勘误轴跑全文档**（文档级不变量）"。
* **F-06 [P3] 步级挂钩登记缺项**。实际挂钩 > 文档记载：s25 还挂 `check_style`（specs/028 O1，task_ops.py:353-367）——cli.md:189 与 rules/04:73 只记 check_math_zh；s3/r3 还挂 `check_math_zh --strict`（task_ops.py:370-388）——cli.md:189 只记 check_academic、rules/09 §2 P5/P6 同漏。

## B. 门禁映射 Γ（tools/check_all.py GATES vs rules/05 登记）

* **F-07 [正向] 门禁锚完备且 CI 单一事实源实证**。11 项 GATES 全部在 rules/05 工具表有行；checks.yml:32 实跑 `check_all.py --list-gates` 生成矩阵，本地/CI 同源。工作流清单 7 件与磁盘 7 件一致。
* **F-08 [P2] 门禁计数六处漂移**（实际：11 门禁＋单测＝12，`--all`＝15）。AGENTS.md:34/57 正确；rules/05:27 "check_all 10 项"、rules/05:66 "十项门禁 + 单元测试"、rules/06:66 "九项门禁…共 10 项""--all…共 12 项"、rules/09:73 与 rules/09:81 "check_all 10 项" 均过时；rules/05:11 CI 矩阵清单缺第 11 项 fidelity（转换保真）。
* **F-09 [P2] rules/05 工具表缺 16 具**（在库 59 具）：`summary_sync`（intake 唯一入口，cli.md:180）、`sync_guard`（收工必跑）、`rebuild_dir`、`repair_loop`、`term_coverage`、`term_flow`、`term_relations`、`registry_azsort`、`gen_en_summary`、`en_patch_lib`、`common`（共享库）、`compose_from_ledger`、`migrate_exec`（已废弃）、`termonline_token`、`tl_browser_batch`、`tl_crawler`。判定权表（rules/05:119-135）另缺 check_quotes 一行。
* **F-10 [P3] 可判性四件套无登记面**。rules/08 §14 要求升门填"机检谓词/预期命中数/幂等证明/一行回退"，但 GATES 无此字段、rules/05 工具表无此列——四件套仅在 ADR-0063 语境出现，未制度化（结构性缺口）。

## C. ADR 链（rules/adr/）

* **F-11 [P3] ADR-0017 索引状态与正文不符**。rules/adr/README.md:51 索引标 proposed；正文 `0017-参考文献双形态澄清.md` 头部"accepted（已裁定，2026-11-13 收口）"。
* **F-12 [P2] ADR 语义错引（工具 docstring）**。check_academic.py:18/418/428 引 ADR-0057（SUMMARY 占位母行去链接）作语体留痕步级时点依据——应为 ADR-0058（语体留痕步级时点口径）；check_tables_images.py:2/12/14 引 ADR-0036（词汇表并网）作表格图片体例依据——应为 ADR-0037（表格与图片体例）。
* **F-13 [正向] 链闭合**。0001–0065 编号无缺口；全库（AGENTS/rules/tasks/cli/tools）引用 60 个 ADR 号零悬空；26 处取代/修订关系显式（0005/0007/0008 部分被取代、0038 决策 1←0062、0040 决策 5←0043、0050 边界一←0051、0028②←0059、0020②r3←0054、0062 决策 4←0065）。

## D. 文档声称 vs 数据事实

* **F-14 [P2] rules/01:80 行数声称过时**。"当前最大 rules/05 74 行"——实际 rules/03 174 行（rules/05 151 行）；该句以假数据为"全部达标"背书。
* **F-15 [P3] 补丁池旧路径 4 处**。divergence.py:7、en_source_audit.py:8/23、task_ops.py:251 docstring 仍写 `baseline/en-patches.json`；ADR-0062 附记已目录化为 `baseline/en-patches/`（唯一解析实现 en_patch_lib.py）。
* **F-16 [P3] sync_guard 沿用已作废积压线文案**。sync_guard.py:14-15（docstring "作业途中应 ≤1，收工时必须为 0"）与 :184（cmd_status 输出同口径"ADR-0028"）——ADR-0059/rules/06:57 明文作废积压线、收工核对改为 `git log origin/main..main` 为空。
* **F-17 [P3] check_render_artifacts.py 文首仍写"待登记 rules/05"**（已登记：rules/05:17 与 render-artifact-audit.yml 行）。
* **F-18 [正向] 数据-文档对账吻合**。divergences 活跃 0／tombstones 113（ADR-0062 回退后语义一致）；补丁池 INDEX 3＝正本 3；baseline 1872 件、钉 4524、yuanwen 记录 1872；勘误表 §八起 31 行；done witness 2 件、version_pin 完备 2/2。

## E. 规范层语义冲突（O/F 冲突通读裁定）

* **F-19 [P2] rules/03 内 CNKI 新旧口径并存**。rules/03:18（译名依据优先级第 1 档＝"知网系权威源：CNKI 翻译助手（dict.cnki.net）、术语在线"）vs rules/03:167（2026-11-14 裁定：术语在线与 CNKI 翻译助手**不再新增查询**，存量凭证可作证据）。优先级节未标注禁用；rules/05:61 `cnki_query.py` 行同样未标注。
* **F-20 [P2] rules/01 仍载已作废的就地改正线**。rules/01:70 "四类勘误可就地改、逐条登记 baseline/divergences.json，ADR-0038/0045" vs ADR-0062 决策 1（en/ 绝对冻结，"就地改正"授权作废）。同日清扫已改 rules/README 判例与 rules/04，rules/01 漏改。
* **F-21 [P2] rules/04 仍载已作废的 reopen 边界一**。rules/04:126 "s2.5_checked 在途件不适用（状态机 reopen 仅限 done），其变更经派工单 A2 以 changes: 挂现有流水吸收" vs ADR-0051 决策 2（R3 在途绕过**含 s2.5_checked**，"ADR-0050 边界一与派工单 A2 路径自此作废"；task_ops.py:433-441 实现已按新口径）。
* **F-22 [P2] GPG 口径两 rules 相反**。rules/06:38 "一律 `git commit --no-gpg-sign`（2026-11-15 S8 收编）" vs rules/05:151 "提交默认免签、**无需** `--no-gpg-sign`（2026-11-06 根治）"。两文件同级、无上位裁决，新条文反而复旧。
* **F-23 [P3] force push 允许与禁止并存**。rules/06:26 "已裁定允许重写 git 记录（含 force push）"（tag 护栏语境）vs rules/06:57、rules/05:150 "--force 仍禁"（ADR-0059）。特例授权未互相标注边界，易被援引为日常依据；取舍待用户。
* **F-24 [P3] 双机定岗：库内条文与用户记忆裁定不一致（待裁定）**。rules/06:54-55 与 AGENTS.md 仍载 ADR-0028 定岗（M1 只做词条翻译）；项目记忆载 2026-11-16 用户裁定"取消定岗、任一机可做全部工作"。库内无对应 ADR（按 rules/06 §变更管理，规则修订应走 ADR）——或补 ADR 收编，或确认记忆失真。证据等级：项目记忆，非库内。

## F. 工具层登记与实现卫生

* **F-25 [P3] compose_from_ledger.py 停留旧布局**。docstring 仍写 `tasks/h/<slug>.ledger.yaml` 与 `h/<slug>.md`（现行：tasks/<首字母>/、<letter>/<slug>.md）；是否仍可运行未验证，建议标注已废弃或升级。
* **F-26 [P3] rebuild_dir.py docstring 陈旧但实现可用**。文首仍写 ADR-0007 形态 `<slug>/index.md`；实测 `rebuild_dir.py check` 在现行 ADR-0009 平铺形态下 0 断链 0 缺镜像（rules/06:68 引用有效）——只改 docstring。
* **F-27 [P3] check_pairs 两则**。docstring 体例轴清单（:18-28）漏列 `pubinfo-form`，而 HARD_RULES 实含（:50-51）；errata-apply 承载存在性谓词过宽——"译注"二字全文命中即认（:238-239），与 ADR-0065 正典形态（节条目＋锚点对称）不对齐，存在漏报面。
* **F-28 [P3] check_style 的 quote-spacing 未入规则清单**。规则 :162/:179 落地（2026-11-15 O2），但 RULES 常量（:35-36）、docstring、rules/02:153 规则清单与 rules/05:43 工具行均未列。
* **F-29 [P3] check_junk.py ROOT_ALLOW 字典重复键**。`node_modules` 定义两次（:86、:99，后者覆盖前者，语义恰一致；代码卫生）。

## 正向结论（计算验证通过面）

1. 状态机两 kind 全态可达、无死端；文档（tasks/README＋rules/04）与实现逐态对账 0 缺。
2. 11 项门禁全部有规范锚并在 rules/05 工具表登记；CI 矩阵由 `--list-gates` 生成，同源无多查。
3. ADR 编号连续、60 个引用零悬空、26 处取代显式；65 件状态字段除 F-11 外一致。
4. 数据面对账吻合（F-18）；write_json_verified/write_text_verified 读回核验在位（common.py:79-136）。
5. 判官只读成立：check_yuanwen_fidelity、check_en_patches、divergence verify 均无写盘路径（读码证实）；写者（yuanwen.py、task_ops.py）与判官分离。
6. 目的命题 Φ 良构且工具链对其充分（spec.md 定理一/二）；残差五项均有显式补偿控制。
