# execution-log（specs/040-coherence-audit）

## 2026-11-17 全系统融洽性审计（一轮完成）

* 开工：方向声明（rules/08 §1）；基点核对（HEAD a442806f7，origin/main 持平，三处遗留脏区未触碰）；`check_all` 12 项全绿为审计基线。
* 语料 100% 覆盖：宪法＋rules/README＋rules/01–09 全文；65 件 ADR 全件状态扫描＋决策关键件（0043/0051/0062/0063/0064/0065）精读；tasks/README、cli.md 契约；59 具工具（17 具门禁谓词全文＋42 具 docstring 层）；.github/workflows 7 件清单核对。
* 形式模型与计算：`bin/audit_coherence.py`（从 task_ops/check_all 权威实现导入，非转抄）；三轮建模修正——①tuple 前驱按实现语义改并集展开（并坐实为 F-02 发现）、②clear/reopen/revert 命令边入图、③viol 判定按 k2 过滤去跨 kind 泄漏。产物 `results/audit-report.json`（schema sep-cn-coherence-audit/1）。
* 采样实证：`rebuild_dir.py check` 实测（0 断链 0 缺镜像，F-26 降级为 docstring 面）；checks.yml:32 读码证实消费 `--list-gates`；AGENTS.md:34/57 计数与实际一致（11+1=12、--all 15）。
* 交付：spec.md（Φ 良构性定理＋工具链充分性定理＋四层判定模型）；results/findings.md（F-01…F-29 问题清单＋六条正向结论，唯一问题清单文件）。
* 裁定：系统融洽（结构层成立，文档层 29 项登记缺陷，零架构级矛盾）。全部缺陷未修——按用户指令只登记。
* 收工自查：本次改变了哪个决策/产物/门禁——新增 specs/040 四文件（spec/bin/results×2/log），未改动任何既有文件与门禁；复跑 check_all 确认无回归后提交推送。

## 2026-11-17 第二轮：全部修复＋复算（用户指令"不计成本解决问题，然后再重新计算"）

* **代码层**：task_ops.py 状态机收口（STEP_EXPECT_PREV 元组表删除，`expected_prev(kind, step)` 由 ORDER 推导唯一前驱＋目标态越界守卫——F-01/02/03；audit 别名归一保留，三例单测先红后绿）；check_pairs 承载谓词收紧＋docstring 硬档补 pubinfo-form（F-27）；check_style RULES/docstring 补 quote-spacing（F-28）；check_junk 重复键（F-29）；check_academic 0057→0058、check_tables_images 0036→0037（F-12）；四处补丁池旧路径 docstring（F-15）；sync_guard 积压线文案（F-16）；render_artifacts"待登记"（F-17）；compose_from_ledger 废弃留档（F-25）；rebuild_dir docstring 现役面澄清（F-26）；GATES 四件套注释块（F-10）。
* **文档层**：tasks/README（revert 口径、update s2.4 作用域）、cli.md（revert 口径、挂钩清单）、rules/04（s25 挂钩、reopen 边界改 ADR-0051）、rules/05（CI 清单补 fidelity、计数四处、工具表 +15 行＝59/59、判定权补引号行、四件套条款、cnki_query 冻结标注）、rules/06（计数、GPG 归一、force 授权期边界、定岗取消）、rules/09（P5/P6 挂钩、计数两处）、rules/03（CNKI 优先级冻结标注）、rules/01（en 冻结口径、行数声称）、rules/02（quote-spacing 入清单）、AGENTS.md（定岗两处）。
* **治理层**：新立 **ADR-0066**（规则体系一致性收口与定岗取消收编：定岗取消、GPG 归一、force 授权期、CNKI 冻结、滞后文本对齐）；adr/README 索引补 0066、修 0017 状态、0028 标注取代关系。
* **验证**：负向冒烟四过（update+draft 拒／pending→s0 拒／s0→s1 拒／正规链过）；单测 447 例全绿；rebuild_dir check 实测 1872 件 0 断链；check_all 12 项全绿。
* **复算**：audit_coherence.py 升级为修复后实现建模＋tripwire（schema v2），A–G 零红灯；报告直写 results/audit-report.json（LF）。
* 并行面：同会话窗口并行会话提交 0e884dd41（fidelity I3 标定）已随本次推送一并上远端；其 yuanwen.py 在途改动未触碰、未纳入提交。

