# 执行日志：全库 A–Z 审阅战役

## 2026-10-28 会话 1（开工）

* 建立审阅任务：本规格（spec.md）落盘，用户指令与裁定（批准批量比较、不计成本、补充 SUMMARY/mu-lu-s 比对）登记进 Assumptions。
* 开工核查：git 基点 a67abfb2；工作区有并行会话未提交改动（baseline/entries.json 三条 converted_at、catalog-verdict.json wisdom REMOVE 候选），本战役不触碰其语义，生成物届时自然收敛。
* 集合关系核定：baseline 1878 = 上游 catalog 1872 全量 + 6 条撤稿留存（已知例外）；别名不占词条包。

## 目录层结果（2026-10-28 会话 1）

* `fetch_catalog.py`：抓取最新 contents.html（快照 `en/_catalog/20261027T192545Z-contents.html`，本地时间戳为 UTC 2026-10-27T19:25Z）——**上游零漂移**：added/removed/renamed/alias_changed 全空，1872 正式词条 + 654 别名与基线目录一致。
* `summary_sync.py report`：重新生成 `specs/001-sep-sync-pipeline/catalog-verdict.json`——add 71（既有登记的 74→71 上游增量 intake 待办）、remove 6（全部为已裁定保留的撤稿留存词条）、mapped 1801；与裁定文档一致，无新增矛盾。
* `check_mulu_s.py`：HARD ERRORS 0；SUMMARY↔mu-lu-s 已知 3 项预期缺口（mu-lu-s.md 自身、版权说明页、1 占位母词条），无新增。
* `check_summary.py`：HARD ERRORS 0。
* 结论：**SUMMARY 与 mu-lu-s 同上游网页 A–Z 目录一致**；无待裁定差异。

## 逐词条 A–Z 批量比较结果（2026-10-28 会话 1，完成）

* 全量 1878/1878 完成（8 路 × 每路 5 秒，1544 秒）；凭证 `results/review-log.jsonl`（一行一条：compare + en_integrity + check_math 三步）。
* **compare（在线 vs en/ 基线）**：1877 条零漂移；1 条变更——`qm-action-distance` 在线已从"撤稿横幅+正文"退化为 **Document Not Found 软 404 页**（正文仅存归档版），compare.py 变更文件已落盘 `specs/001-sep-sync-pipeline/compare/qm-action-distance.json`；该词条保留依据本就是归档版基线（裁定 c75cc794/2eecf911），zh 侧为未翻译存根，无需译文侧动作。其余 5 条撤稿留存词条（wisdom 等）实测在线正文仍在且与基线零漂移。
* **en_integrity（en/ 包）**：全绿。
* **check_math（md 公式）**：232 条 warn（行内 `$` 失衡，渲染歧义警告；check_math 退出码只由 missing 驱动，无公式丢失）。
* **idiolects 单词条 integrity 假警报**：单词条模式下 `inbound_map` 只扫给定包，看不见 linguistics → `../idiolects/appendix.html` 的跨词条引用；`--all` 全库模式信用该引用（19:50Z 终证与本次 21:11Z 收尾凭证均 clean）。

## 并行会话观察（2026-10-28 会话 1）

开工后发现同工作树有并行会话在改 `tools/check_math.py`、`.vitepress/math-plugin.mjs`、README、sync-headers 工作流并新增 `tools/tests/test_check_math.py`（数学渲染方向）。本战役对工具只读、凭证只写 specs/007-review-campaign/**，提交严格限本战役文件；check_math 如被并行改动，瞬时失败由续跑机制兜底，收尾阶段以最终版工具复验。

## 英语markdown 全库复核结果（2026-10-28 会话 1，完成）

* **en_integrity --all 收尾凭证**（`results/en-integrity-full.json`，21:11Z）：audited 1878、clean 1878、硬发现 0、错误 0；MathJax 456 / 内联 864 / 公式图片资产 2，与既有终证一致。
* **重转换零写入复核**（`bin/yuanwen_recheck.py`，真实 convert_entry 代码路径 + 写操作窥探比对；因并行会话在途不动 baseline）：
  * 正文 md 1878：**1877 字节保真**；1 条漂移 `whitehead.md`（图片自链接包裹，cbb07a78 图片接线与重转换间的毫末不一致，随在途会话下次重转换收敛）；
  * 补充材料 541 条漂移：全部为在途 `convert_supplement` 站点框架剥离修复的预期方向（在盘大、重转小），待并行会话提交+重转换后归零；
  * 图片资产镜像（yuanwen/assets/ ↔ en/）：**0 漂移**；历史遗留清理目标：0；失败：0。

## markdown 全要素审阅结果（2026-10-28 会话 1，新增任务，完成）

`bin/check_markdown.py` 对全部 4360 个 md 文件（git 追踪 1939 ∪ yuanwen/ 语料 2421）逐个复核（凭证 `results/mdqa-full.json`）。最终硬问题 **676**，全部定性归位：

| 类别 | 数量 | 定性与归属 |
|---|---|---|
| 脚注悬空 | 457 | yuanwen：181 条补充材料 `[^note-N]`（在途 convert_supplement 附载修复将收敛，D14 家族）+ 276 条作者-年份引用键无定义（formal-epistemology 57、impossible-worlds 53、connectives-logic 48 等——link_citations 引用匹配缺口，**新发现**，移交镜像责任会话） |
| 断链 | 167 | 全部为 yuanwen/SUMMARY.md 导航行指向 zh 侧页面（README/mu-lu-s/qian-yan/guan-yu 在 yuanwen/ 无镜像对应），结构缺口，移交镜像责任会话 |
| 未换行收尾 | 46 | yuanwen 补充材料，在途重转换将收敛 |
| 表格列数 | 5 | pm-notation.md 上游固有倒置表结构（数据行在前），镜像照录，登记为上游噪声 |
| CRLF | 1 | qian-yan/ci-hui-biao.md——并行会话正在做登记册归一化（yi-zhe-shuo-ming.md 已由其修复），留待其收敛避免写冲突 |

* **中文词条（zh 域 1807 存根）与 meta 域：零硬问题**。
* 检查器对误报源做了守卫：引用块内 `[^key]` 体例说明文字（7856 处）、数学记号伪链接（`[*Gx*](` 等）、meta 文档 `[^..]` 示例文字；孤儿脚注定义 134,643 条为 yuanwen 设计使然（参考文献全量转脚注、正文只标实际引用组），聚合计数不逐条报。
* 图片：1,755 处 `![]()` 引用全部在盘存在（0 缺失）；外链 17,250 处只计数不抓取。

## 并行会话观察（更新）

本战役运行期间并行会话：提交 cbb07a78（yuanwen 转换器修复+全量重转换+复审计，ADR-0010 图片接线 10019 图）；在途修改 tools/yuanwen.py（convert_supplement 框架剥离）、tools/check_math.py（+18 行）、.vitepress/math-plugin.mjs、sync-headers 工作流、新增 test_check_math.py；归一化登记册（yi-zhe-shuo-ming.md CRLF→LF 已修，ci-hui-biao.md 在途）。本战役对共享文件只读、凭证只写 specs/007-review-campaign/**，提交严格限本战役文件。

## 收工（2026-10-28 会话 1）

九门禁复跑见提交前记录；本战役产物全部分批提交，未 push。
