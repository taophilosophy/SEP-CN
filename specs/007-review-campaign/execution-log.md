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

## 全量复核（2026-10-28 会话 2，用户指令"全量复核"，intake 后全库重验）

* **目录层**：fetch_catalog 重抓（快照 20261028T054741Z）——上游零漂移（1872+654 全空 diff）；check_summary / check_mulu_s HARD ERRORS 0；SUMMARY 正式词条 1878 = 上游全量（intake 后缺口 0）。
* **A–Z 逐词条三步扫描（第 2 轮）**：1878/1878 done（8 路 × 每路 5 秒，2419 秒），结果与首轮**完全一致**（含 232 条 math warn 的集合逐一相同）——1877 零漂移 / qm-action-distance 在线 DNF / idiolects 单词条模式假警报，0 瞬时错误。两轮一致 = 收敛到不动点。凭证 results/review-log.jsonl（第 2 轮重置重建，首轮证据在 git 史 f4e6d340）。
* **en_integrity --all（第 2 轮凭证 results/en-integrity-run2.json）**：audited 1878、clean 1878、硬发现 0、错误 0；MathJax 456 / 内联 864 不变。
* **重转换零写入复核（第 2 轮）**：**drift=0、image_drift=0、failures=0**——首轮的 541 条补充材料漂移与 whitehead.md 毫末差异已随并行会话的转换器提交+全量重转换收敛，镜像与转换器字节一致。
* **markdown 全要素（第 2 轮 results/mdqa-run2.json）**：4442 文件（+82：71 个 intake 桩 + 并行会话新文件）。硬问题 683，与首轮的差集全部定性：
  * qian-yan/ci-hui-biao.md CRLF **已收敛**（并行会话登记册归一化落地，首轮遗留归零）；
  * specs/001-sep-sync-pipeline/spec.md CRLF 189 处——本会话 Edit 引入，**已修复**（归一化 LF）；
  * s/spacetime-holearg.md（crlf + 4 断链）——并行会话在途编辑中，登记待其收敛；
  * yi-zhe-shuo-ming.md 又被并行会话写回 CRLF——其在途，登记；
  * tools/tests/fixtures/check_terms/registry5.md 表格缺列——check_terms 的**故意测试夹具**（测试缺列容忍），非缺陷；
  * 457 脚注悬空 / 46 未换行收尾 / 5 pm-notation 表格——与首轮相同，归属不变（镜像会话）。
* **九门禁**：SUMMARY 结构 / 分类目录 / 单体文件 / 垃圾入库 / 术语一致 / 管线单测全绿；哲学学术规范 1 失败——全部为并行会话在途（ren-ming-biao.md 登记册被误扫为词条 ×3、alcmaeon ADR-0011 旧措辞，check_academic.py 正被其修改中）。
* **task-pin-missing ×4 裁定（本战役 intake 任务）**：aesthetics-race / animal-thought / engels / epistemology-ai 的 version_pin 缺 archive_edition——经 fetch_entry 重查 + archinfo.cgi 实测（http-log 凭证 + 在线响应比对）：4 条均为**"尚未被存档"新词条**（"is not yet archived ... Winter 2026 edition"），archinfo 解析器只处理已存档格式，**archive_edition 为空是正确数据**（版本钉依 pubinfo + sha256 成立，存档版名待首次归档）；警告属固有类别，check_academic 可考虑容忍 never-archived 条目（移交并行会话）。

## 待办解决（2026-10-28 会话 3，用户指令"先解决1、3、4、5"+"禁止机械判断，从语义分析"）

### 检查器三类机械误判根治（footnote-dangling 457→117 真值）

语义对盘核验发现 340 条悬空为**检查器自身的公式状态机缺陷**，逐一实证修复：

1. **货币表卡死**（formal-epistemology 548 行 `$+$$19`）：表格行先于公式状态机判定；
2. **TeX 转义美元 `\$$`**（impossible-worlds 181 行 `$\$$`）：扫描前剥离转义美元；
3. **相邻内联边界 `$a$$b$`**（settheory-early 130 行等）：转换器产出的显示公式全部单行闭合（全库 0 独占行、0 跨行块实证），**跨行状态机整个废除**，改为逐行剥离成对 `$…$` 生成式 + 残差记 info。

修复后 117 条悬空与全量对盘真缺数**完全一致**（0 误报）。

### 117 条真缺的语义定性（移交镜像会话）

两类转换器脚注接线缺陷，上游注释语义本体都在：

* **补充材料自产注键无定义**（axiom-choice note-sup1..7、binarium note-* 等）：上游补充页的注释本体存在（或引用存在），转换器生成 note-supN 键名的引用但未附定义；
* **数字锚点 notes 未接线**（logical-constants 26 条等）：上游 `notes.html#1` 数字锚点形态未被注段定义提取覆盖。

归属 tools/yuanwen.py 脚注管线（镜像会话活跃开发线：646 件归零、D14 附载皆此类），移交时语义与证据齐备。

### yuanwen/SUMMARY.md 断链 167→0（本会话修复）

write_summary 原为逐字符拷贝，zh 侧导航行（README/mu-lu-s/qian-yan/guan-yu）在 yuanwen/ 下无对应文件。修复：拷贝时对「yuanwen/ 下不存在而仓库根存在」的链接目标改写 `../` 前缀（168 处改写），复验断链 0、硬问题 0。

### mu-lu-s 分类缺口 ×71 → 0（item 1 完成）

71 条语义归类插入（bin/mulu_classify_71.py，锚=现有行文本片段唯一命中+继承缩进，chained 链式锚修正 11 处字母笔误后 71/71 落位）。语义锚定举例：堕胎的伦理学→生命伦理簇、阿夫扎勒丁·胡纳吉→伊本·西那逻辑学后、倾向逻辑→偏好、可证性逻辑→证明论发展后、规范 gauge 理论→量子场论后、戴震→清代哲学后、宝称/室利笈多/瑜伽行派/锡克哲学→印度佛教簇、智慧（当代分析哲学）→智慧词条后。check_mulu_s：正式条目覆盖缺口归零（余 4 项=登记册自身/版权说明/占位母词条/并行在途 political-philosophy），HARD ERRORS 0。

### item 3（并行会话在途项）状态

* CNKI/审定名词库通道：**已通**（termonline-standard 实测 abortion→5 hits 凭证入库）；
* never-archived version_pin 豁免：并行会话已落地（5b40df70），本战役 4 条告警清零 ✓；
* RELEASE-NOTES.md 误扫、yi-zhe-shuo-ming.md CRLF 回潮、political-philosophy intake：并行会话在途（其文件在写窗口内），未触碰。

## A 批全流程翻译测试（2026-10-29 会话，用户指令"先补遗、再以A开头的所有词条为例进行全流程翻译测试，以期完善"）

### 补遗收口

* 上游增量 add=0（71 条已吸收）；political-philosophy 遗留桩裁定移除（上游 404、目录无此条、归档五代全 404 实证；apply-remove FR-022），mu-lu-s 残行清除；正式词条 1879→1878。
* summary_sync report 反向标题索引**同题歧义盲区修复**（此前漏检根因："political Philosophy" 与五个同题上游词条撞题被静默放行；今歧义转人工裁定）。

### 首件全流程：溯因 abduction（六道走完，done）

* 流程：claim a 批（ses-007-rev）→ 账本 intake/fetch/translate 推进（附计数 note）→ 批内 147 个任务补建（累计 160/160）→ abduction 六道 done。
* 译文：a/abduction.md 正文四节全译（~2.2 万字）+ 补充材料 a/abduction.peirce.md；参考文献 125 条 [^key] defs 逐字符照录（键序与 yuanwen 一致），文内标记 48/48 配对。
* 术语：登记 10 条（ampliative 扩展性、theoretical virtues 理论美德、经验等价、非充分决定性、坏堆论证、规则循环、荷兰赌、解释主义、信念(度)的认识论、最差解释推理），termonline 查证在案；双表同步（发布表 +9，1 条 dup 既有）。
* 门禁：check_style 0、check_academic --strict 0、check_math 0、check_terms 0 硬错误、glossary_lint 我的条目清零。

### 工作流摩擦清单（"以期完善"的实质产出，共 8 项）

1. **check_academic 引用注释方案盲区**（已修）：镜像转换器把整份文献表转为 [^key] defs、文内只挂已链接引用组——77 条未引用 defs 被误判 orphan-def。已加"参考文献节内定义豁免"（与 D14 跨文件豁免同类）。alcmaeon 若改用 defs 形态将同样受益。
2. **summary_sync report 同题歧义盲区**（已修）：反向标题索引对同题多词条静默放行；歧义现在转人工裁定。
3. **biblio-note ADR-0011 措辞**：节首说明必须含"中国文献译为中文"（alcmaeon 同样待修——并行会话在途项）。
4. **术语登记必须查双表**：只查登记册会撞发布表既定译法（underdetermination 实证：发布表既有"非充分决定性"）。S2① 应改为"查双表"。
5. **publish_terms.py 已过时**：向 5 列登记册插 4 列行（ADR-0012 前 tools），008 现行 SOP 为手工双表同步——工具应标记废弃或升级。
6. **task_ops s1 双路径未记档**：STEP_EXPECT_PREV s1=("drafted","pending") 为有意设计（已有成稿免 clear-draft 循环），contracts/cli.md 未载，建议补记。
7. **干执行残留任务状态**：演练后状态复位 pending 但 steps 留痕，重跑时 clear/draft 历史与新流程交错（abduction 实证）；建议演练复位时清 steps。
8. **领批次前未读批次账本**：a 批 fetch/convert 事实早已满足而账本停在 intake——建议 campaign.py status 增加"事实满足可 advance"提示列。

### 批次进度

* a 批 translate：1/160 done（abduction）；159 待译（任务已全部建立）。
