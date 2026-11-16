# findings：全系统融洽性审计问题清单与修复台账（specs/040）

唯一问题清单文件（用户指定"列举到某个文件中"）。第一轮（2026-11-17 上午）登记 F-01…F-29；用户指令"不计成本解决问题，然后再重新计算"后第二轮全部处置完毕，复算零红灯（`results/audit-report.json`，schema v2，A–G 全部性质通过）。严重度：P2＝应修、P3＝登记。修复分类：**已修复**（实现/文本改动）、**已收编**（ADR-0066 登记）、**留档**（标注废弃，不启用）。

## A. 状态机 LTS（tools/task_ops.py）

* **F-01 [P2] update 任务可漂入 retranslate 专用态——已修复**。`advance` 现经 `expected_prev(kind, step)` 由 ORDER 单一事实源推导：目标态不属于该 kind 序列即拒（task_ops.py）。负向冒烟：update+draft 被拒 ✓；单测 447 例全绿。
* **F-02 [P2] expect 元组并集语义（跳过 clear/draft）——已修复**。同上：合法前驱＝序内唯一直接前驱；retranslate pending→s0、s0→s1 均被拒（冒烟 ✓）。
* **F-03 [P3] audit 别名死条目——已修复**。STEP_EXPECT_PREV 整表删除；别名经 `step == "audit" → "s25"` 归一保留（s25 挂钩派发与 changes: 校验不受影响，三例单测回绿）。
* **F-04 [P2] revert 口径两处文档滞后——已修复**。tasks/README.md、contracts/cli.md 均改"--to s2.5_checked|s2.4_termchecked（源态 s2.5_checked 及其后；ADR-0043、ADR-0063 扩）"。
* **F-05 [P3] update s2.4 作用域概括失真——已修复**。tasks/README 改"术语轴仅变更段；体例/勘误轴全文档，ADR-0063"。
* **F-06 [P3] 步级挂钩登记缺项——已修复**。cli.md 职责权属行、rules/04 s25 节、rules/09 §2 P5/P6 门禁列补齐（s25＋check_style O1；s3/r3＋check_math_zh --strict）。

## B. 门禁映射 Γ（rules/05 登记）

* **F-07 [正向] 门禁锚完备且 CI 单一事实源实证——维持**。11/11 门禁在 rules/05 工具表；checks.yml:32 实跑 `--list-gates`。
* **F-08 [P2] 门禁计数六处漂移——已修复**。rules/05:11 补 fidelity；rules/05 两处、rules/06、rules/09 两处统一为"十一项门禁＋单元测试＝12 项；--all 15 项"。
* **F-09 [P2] rules/05 工具表缺 15 具——已修复**。补 15 行（summary_sync、sync_guard、rebuild_dir、repair_loop、term_coverage/term_relations、term_flow、registry_azsort、gen_en_summary、en_patch_lib、common、compose_from_ledger〔已废弃〕、migrate_exec〔已废弃〕、术语在线三件）；判定权表增"中文引号合规"行（check_quotes）。复算：在库 59 具＝登记 59 具。
* **F-10 [P3] 可判性四件套无登记面——已修复**。check_all.py GATES 注释块登记四件套（谓词＝命令、预期命中＝0、幂等＝只读、回退＝revert）；rules/05 判定权节增"升门四件套登记"条款。

## C. ADR 链

* **F-11 [P3] ADR-0017 索引状态不符——已修复**。索引改"accepted（2026-11-13 收口）"，与正文一致。
* **F-12 [P2] ADR 语义错引——已修复**。check_academic.py 三处 0057→0058；check_tables_images.py 三处 0036→0037。
* **F-13 [正向] 链闭合——维持并增强**。0001–0066 编号连续；62 个引用号零悬空；取代链显式。

## D. 文档声称 vs 数据事实

* **F-14 [P2] rules/01:80 行数声称过时——已修复**。改"当前最大 rules/03 174 行"（复算吻合）。
* **F-15 [P3] 补丁池旧路径 4 处——已修复**。divergence.py、en_source_audit.py×2、task_ops.py docstring 改 `baseline/en-patches/`（一补丁一文件）。
* **F-16 [P3] sync_guard 积压线文案——已修复**。docstring 与 cmd_status 输出改 ADR-0059 口径（提交即推；收工核对 origin/main..main 为空）。
* **F-17 [P3] check_render_artifacts"待登记"——已修复**（docstring 改"已登记 rules/05 与 render-artifact-audit.yml"）。
* **F-18 [正向] 数据-文档对账吻合——维持**（divergences 0/113、补丁池 3=3、基线 1872/钉 4524/yuanwen 1872、勘误表 §八起 31 行、done witness 2/2）。

## E. 规范层语义冲突（O/F）

* **F-19 [P2] rules/03 CNKI 新旧并存——已修复**。优先级第 1 档标注 2026-11-14 冻结裁定（不再新增查询）；rules/05 cnki_query 行同步标注。
* **F-20 [P2] rules/01 就地改正残留——已修复**。改 ADR-0062 绝对冻结口径（勘误表＋译注／补丁池／分歧账只承载上游真变）。
* **F-21 [P2] rules/04 已作废 reopen 边界一——已修复**。改 ADR-0051 R3 口径（在途含 s2.5_checked 经 --upstream-sync；旧边界注记为作废历史）。
* **F-22 [P2] GPG 口径两 rules 相反——已收编**。ADR-0066 决策 2：以 rules/05（2026-11-06 根治裁定）为权威，rules/06 复旧句废止（默认免签、无需 --no-gpg-sign、显式 -S）。
* **F-23 [P3] force push 允许/禁止并存——已收编**。ADR-0066 决策 3：重写记录限定用户显式授权期专属；日常禁 force（ADR-0059）。
* **F-24 [P3] 双机定岗裁定未收编——已收编**。**ADR-0066**（规则体系一致性收口与定岗取消收编）登记 2026-11-16 用户裁定"任一机可做全部工作"；rules/06 多机并行节改"分工不设岗"、AGENTS.md 两处改口径、adr/README 索引 0028 行标注取代关系。回退＝revert ADR-0066 提交。

## F. 工具层登记与实现卫生

* **F-25 [P3] compose_from_ledger 旧布局——留档**。docstring 顶部加"【已废弃留档，勿再执行】"（ADR-0007 时代一次性工具）；rules/05 表登记为已废弃。
* **F-26 [P3] rebuild_dir docstring 陈旧——已修复**。docstring 改"现役面＝check；toletters 一次性迁移；rebuild/stubs/yuanwen 遗留废弃"（check 实测 1872 件 0 断链）。
* **F-27 [P3] check_pairs 两则——已修复**。docstring 硬档清单补 pubinfo-form；errata-apply 承载谓词收紧为"节条目（圈号开头）或句内 `（译注：…）` 形态锚定"，不再全文搜"译注"。
* **F-28 [P3] check_style quote-spacing 未入清单——已修复**。RULES 常量、docstring、rules/02 检查节、rules/05 工具行四处补齐。
* **F-29 [P3] check_junk ROOT_ALLOW 重复键——已修复**（删首个 node_modules 定义，保留 ADR-0055 注记形）。

## 复算结论（第二轮）

`bin/audit_coherence.py`（升级为修复后实现建模＋tripwire）：**A–G 全部性质通过、零红灯面**。门禁 11+1=12（--all 15）；工具 59/59 登记；ADR 66 件、62 引用号零悬空；状态机全态可达无死端、严格前驱（越界与跳步在实现层被拒）；规范层 O/F 冲突清零。`check_all` 12 项全绿；管线单测 447 例全绿（含 task_ops 三例别名回归修复后回绿）。
