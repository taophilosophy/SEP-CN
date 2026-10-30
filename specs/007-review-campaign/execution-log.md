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

### 补遗反思与 HTML 比对（2026-10-29 会话，用户指令"先反思补遗，比对HTML"）

* **反思结论：political-philosophy 裁定下早了**。初次裁定只探了五代近期归档且未走 archinfo——正规路径（archinfo.cgi + 归档目录比对）揭示真身：条目实为 **wyclif-political**（Stephen Lahey《John Wyclif's Political Philosophy》），win2020–spr2025 归档均在（正文 HTML 64KB 实证），spr2025 后撤稿，在线 URL 现 200+软 404 页（curl 状态码 200 会骗人，fetch_entry 软 404 内容检测才是真相——"比对HTML"一语中的）。老语料错挂 slug 为 political-philosophy。
* **更正执行**：`fetch_entry --archive-edition spr2025 wyclif-political`（归档包 2 文件入库）→ 元数据补正（归档路径漏解析 citation_title/authors，从 en/ 原始 HTML 读回——摩擦 #10）→ apply-add 恢复词条（w/wyclif-political.md，SUMMARY 嵌套于 Wyclif 主行下）→ mu-lu-s 行改指真身 → directory_audit 裁定集 6→7（撤稿留档 spr2025 实证）→ 三验证全绿（check_summary/check_mulu_s/逐行审计 0 findings）。
* **新增摩擦**：#9 apply-add 对标题内嵌方括号（如 [Gianfrancesco]）未做 `\[` 转义，check_mulu_s 解析器不认（abelard 先例已转义）——已手工转义，工具待修；#10 fetch_entry --archive-edition 漏解析 citation 元数据——已手工补正，工具待修。
* 教训沉淀：**移除裁定前必须 archinfo + 多代归档内容比对**（"比对HTML"＝状态码之外还要验内容形态）；软 404 检测必须走内容特征而非状态码。

## 既有译文逐段 vs 原始 HTML 全量比对（2026-10-29 会话，用户指令"全部译文逐段不计成本与html直接比较，禁止抽查"）

### 方法

* 比对链：zh 译文块 ↔ yuanwen 块（1:1 同构）↔ en/ 原始 HTML（保真由 yuanwen_recheck drift=0 + en_integrity 全审闭环承担——"直接比较 HTML"的两段式实现）。
* 对齐器：specs/007-review-campaign/bin/para_align.py（EN/ZH 块切 + 图组折叠 + 转换器块切伪影规整 + notes.html 键控配对）。
* 覆盖：既有全部译文 4 件——abduction（主+补）、alcmaeon、spacetime-holearg；**454 个位置对 + 8 个 notes 键控对，逐对核验，零抽查**。

### 机械校验（先行清场）

* 参考文献/脚注定义照录：abduction 125/125（键集、序、归一化文本全等）、alcmaeon 81/81（fuzzy ≥0.75）、spacetime 86/86 ✓。

### 逐对语义核验结果

* **abduction 86 对**：1 处衍字（#57"第二个不*没*有那么一般"）——已修；其余全对位（引用组/脚注标记/斜体/书名号/括注全一致）。
* **abduction.peirce 11 对**：2 处已修——CP 5.172 皮尔士引文照录英文与全篇引文译出体例不一（已译）；"按现代 conception"英文残留（已改"按现代构想"）。
* **alcmaeon 70 对**：0 语义缺陷；3 个古典人名未汉译（Theano/Pausanias/Hecataeus，ren-ming-biao 体例应为古典汉译）——归 alcmaeon 责任会话（s1_checked 在途）。
* **spacetime-holearg 124 对 + 图 4 幅（alt/题注全译）+ notes 8 对**：0 语义缺陷；上游笔误 "aargues"（§9.1）镜像如实保留、zh 已正确翻译。
* **对齐器在审阅中暴露并修复的三类自身缺陷**：公式定界符状态机误判（沿用 check_markdown 修复经验）、图组块数不同构（yuanwen 3 块/图 vs zh 2 块/图，模板首跑确认形态）需图组折叠、转换器断句+链接块切伪影需结构规整。

### 结论

既有全部译文（4 件、约 6.5 万字）与原始 HTML 的逐段比对**完成，无未处置的语义缺陷**；3 处笔误/体例问题当场修复，3 处人名汉化建议移交 alcmaeon 责任会话。逐对凭证：results/para-align.jsonl（464 行）。

### 收尾门禁

* 逐段比对修复后的复验：check_style 0、check_academic 0（新增**补充材料豁免**：`<slug>.<x>.md` 按模板不设独立参考文献/学术工具节、无独立版本钉，由主词条承载——摩擦 #11）、check_math 0、check_terms 0；**check_all 7 项全绿**（并行会话的在途项已由其收敛）。

## 复核反思（2026-10-29 会话，用户指令"先复核反思"）

### 门禁与残留扫描

* check_all 7 项全绿 ✓
* 逐件英文残留扫描（正则 `(?<=[\u4e00-\u9fff])\s+[a-z]{4,}`）：
  - abduction：1 处（H1 括注"abduction"——模板 §2 #1 规定格式，非缺陷）
  - abelard：0 处 ✓
  - abhidharma：6 处 → **4 处实残已修**（rival→论敌、mass→总体、dharma 清单×2 标斜体），2 处为技术术语保留（§1.2 节标题 Dharma→dharmas 对应 yuanwen 结构；\*dharma\* 斜体技术词）
  - african-sage：3 处 → 0 实残（H1 括注"sage philosophy"模板格式；onisegun×2 为约鲁巴技术词保留）

### 深层反思：翻译质量诚实评估

**做得好的**：
1. 结构对位严格：四件 220/220、217/217、150/150、90/90 块 1:1，无漏节漏段
2. 术语纪律：每件先查双表、再 termonline 查证、后进正文；冲突时以发布表既定译法为准（underdetermination 实证）
3. 文献照录：abduction 125/125、abelard 97/97、abhidharma 95/95、african-sage 43/43——键集/序/归一化文本全等
4. 引文体例：所有 EN 引文均译出（阿德勒/威廉姆森/汤姆逊/皮尔士 CP 引文/舒尔茨等），保留原文括注（CP 5.172 等）

**做得不够的（自我批评）**：

1. **英文残留反复出现**——四件中有三件存在英文残留。根因：写作时思维在双语间切换，中文句子中嵌入英文原词（rival/mass/various/definitive/involves/encapsulated 等）。二校本应逐条排查，但我的二校修改清单是自报的、没有独立工具拦截。**改进**：把正则扫描做成 check_style 的正式子规则（非括注、非斜体标记内的独立英文词→报 issue），而非事后人工补查。

2. **abelard 拼接事故**——defs 拼接起点匹配 `### ` 误命中正文节标题，把 EN 正文 150 行灌进 zh 文件；连续三轮修复才收敛。根因：没有一个专门的 defs 拼接工具，每次用临时脚本、每次写不同的匹配逻辑。**改进**：写 `specs/007/bin/splice_defs.py`（输入 slug，自动定位 defs 起点=`[^` 首行，自动转换引号，自动核键集），消除临时脚本。

3. **六道证据是自报的**——每个 step 的 evidence 字段是我自己写的描述。独立校验仅 style/academic/math/terms 四个机械工具。语义层面的"一校对照原文逐节核销"和"复审逐句回核"没有独立凭证。**改进**：逐段对齐器（para_align.py）已是独立凭证，应在 s1/r1 证据中引用其输出文件（para-align-summary.json），而非口头声明。

4. **翻译深度的诚实评估**——我读一段 EN 写一段 ZH，对哲学概念的把握依赖源文上下文。但：(a) 长句中的从句嵌套偶尔简化；(b) 专业术语的中文选择依赖既有登记册，未登记的以学界惯例直裁；(c) 引文的"译出"是翻译而非回查经典汉译本（如康德/亚里士多德引文应查已有的商务印书馆译本）。**改进**：终审 r3 应增加"经典汉译本回查"步骤。

5. **术语登记的时机滞后**——我边翻译边遇到新术语，但登记是事后批量做的（10 条/批）。这导致正文写作时未先查术语册，可能有已经登记但被我遗漏的译法。**改进**：翻译前先通读全文提取术语候选→查双表→登记→再开始写正文。

### 流程偏差登记

* 71 任务直接 task_ops create，未走 campaign.py claim 批次——需在 specs/005 账本补记
* defs 拼接用临时脚本而非入库工具——已识别，待建 splice_defs.py
* 摩擦清单累计 11 项，已修 5 项（#1 引用注释豁免 #2 同题歧义 #11 补充材料豁免 + 2 项对齐器缺陷），余 6 项待修

### 下批次改进措施（可检验）

| 措施 | 检验方式 |
|---|---|
| defs 拼接工具化（splice_defs.py） | abelard/abhidharma/african-sage 重跑不产生 EN 正文混入 |
| check_style 增英文残留子规则 | abhidharma 修后 0 issue（已验证）|
| s1/r1 证据引用 para-align-summary.json | 下一批任务 JSON 可查 |
| 翻译前术语预提取 | 下一批术语注册数下降但覆盖不降 |
| 经典汉译本回查 | 下一批 r3 证据含回查记录 |


## 2026-10-30 A批续译：abrabanel done + done 词条残留清修复

### abrabanel（第 7 件 A 批词条，六道 done）

* 全译：导语+七节（生平与著作/信仰理性神话/美与爱/美的哲学/爱的哲学/人的终极目的/接受史与影响）+67 脚注全译+refs 48 条 defs 照录（Editions 6+Secondary Literature 42），键集 115/115 与 yuanwen 一致
* para_align 驱动表纳入 abrabanel 并全量重跑：208/208 段全对齐 0 残留（顺带对 abelard/african-sage/abduction/peirce 四件回归复核通过；alcmaeon 78 段、spacetime-holearg 91 段残留为各自责任会话既有状态）
* 拉丁转写撇号处置：Telunah 'al / mir'â / al-'ishq / l'âme 等非词邻接撇号触发 curly-quotes；按"转写记号非引号"改 U+02BC（ʼ），词内撇号（Kena'ot 类）维持 ASCII 豁免
* 门禁：check_all 7 项全绿；任务九步（clear/draft/s1/r1/.../done）逐道留证

### done 词条残留清修（零信任复查遗留）

* abhidharma：拼接事故残迹清除——"## Notes to Abhidharma" 残节+重复引块+`<!--DEFS-->` 残标记（此前反思考查遗漏，本次 check_markdown 全库扫描暴露线索后定位）
* abner-burgos：EN 未译 6 处——dedicated×3（note-6/note-19/§4 首段）、individual×1（§4）、extensive×1（§1）、corpus×1（§2）；逐处按语义改写（如"即以此书为研究主题""致力于决定论与自由意志的问题"），禁机械替换
* 两文件修后 check_style 0 issue、check_academic 0 硬错误

### abortion 任务记录补录（commit 4f8dda26 上报件落地）

* 缺陷：done 状态仅 4 步（s1/s2/done/done），clear/draft/s3/r1/r2/r3 六步漏记，触发 task-evidence-missing 门禁硬错误、check_all 全红
* 处置：按"另行上报不代改"裁定精神单独处理——既有 4 步不动，追加 6 步如实补录（每步标注"补录（原推进漏记）"并注明依据 commit），done 步数 4→10；补录非杜撰，工作产物与门禁输出均可复核
* 教训：done 步必须逐道推进，"六道并轨"只能在步内 evidence 说明，不能省步

### 移交（并行会话责任件，不代改）

* spacetime-holearg：check_markdown zh scope 5 hard——crlf×1 + link-broken×4（补篇 spacetime-holearg.active-passive/leibniz-equivalence×2/gauge 链接目标不存在）；另 para-align 91 段 EN 残留（数学推导段未译）。归其责任会话处理
* abelard：行尾缺换行（final-newline hard）——本会话文件，已修

### 下一步

* a 批续译：余 153 件（abracadabra 起），流程同本件（defs 拼接按注/文献两类入口分流）

## 2026-10-30 A批续译：abrabanel done；加粗坍缩事故定损修复

### abrabanel（第 7 件 A 批词条，六道 done）

* 全译：导语+七节（生平与著作/信仰理性神话/美与爱/美的哲学/爱的哲学/人的终极目的/接受史与影响）+67 脚注全译+refs 48 条 defs 照录（Editions 6+Secondary Literature 42），键集 115/115 与 yuanwen 一致
* para_align 驱动表纳入 abrabanel/abhidharma 并全量重跑：abrabanel 208/208 段全对齐 0 残留；abhidharma 171/174 配对，3 条 EN"残留"经核对为布局差异（zh 把文献 defs 排在学术工具之前、EN 在文件尾），内容逐一 grep 验证在位
* 拉丁转写撇号处置：Telunah 'al / mir'â / al-'ishq / l'âme 等非词邻接撇号触发 curly-quotes；按"转写记号非引号"改 U+02BC（ʼ），词内撇号（Kena'ot 类）维持 ASCII 豁免
* 门禁：check_all 7 项全绿（本会话文件范围）；任务九步（clear/draft/s1/s2/s3/r1/r2/r3/done）逐道留证

### 加粗坍缩事故（定损→修复→固化）

**现象**：para_align 复核时发现 abduction 正文段只剩加粗碎片。定损：某个先前会话的加粗处理脚本以跨行正则吞掉相邻 `**…**` span 之间的全部文本（段内前缀、段间文本乃至整段），并合并段落。

**波及面（三签名扫描：pubinfo 行尾挂文本 / 同行双加粗仅隔空白 / 段首加粗）**：

| 文件 | 处态 | 处置 |
|---|---|---|
| a/abduction.md | 工作区未提交（HEAD 干净） | `git checkout` 恢复；确认 216 段完好 |
| a/abelard.md | 同上 | checkout 恢复 + 重放行尾换行修复 |
| a/abner-burgos.md | 同上 | checkout 恢复 + 重放 6 组 EN 未译修复（corpus/extensive/individual/dedicated×3） |
| a/abhidharma.md:83 | 已入库（2e8270da 连带提交） | Cox 整段从 `2e8270da^` 取回原文，按现行 bold-spacing 风格调校（`** 是什么 **`→`**是什么**`） |
| a/abortion.md:406-407 | 已入库（d9481067 建文件时即带伤） | 列表 `*` 与斜体 `*` 焊成 `**`；按 EN 源重建两列表项（*Brain in a Vat* / *Philosophy Talk*） |

**根因与教训**：

1. para_align 只对块配对、不比对块内文字——坍缩减块恰被其 EN 侧归一化抵消，"全对齐"假通过。**补偿控制**：新增 `specs/007/bin/check_bold_collapse.py`（三签名扫描，本日全库复扫 0 候选）；后续翻译词条收工前必跑。
2. 事故跨两个入库提交（2e8270da 把带伤行当修复提交；d9481067 建文件即带伤），说明"门禁绿"不等于"内容完好"——体例门禁不校验加粗 span 间文本存在性。
3. 涉事脚本未定位到具体文件（多脚本候选）；凡批量正则改写 .md 的工具，必须先跑坍缩扫描再入库。

### 顺带清理（本日）

* abhidharma：`git show HEAD` 核实残节（## Notes to Abhidharma+重复引块+`<!--DEFS-->` 残标记）未入库，checkout 后自然消除
* abelard：行尾换行（check_markdown zh scope final-newline）已修

### 任务记录补录（commit 4f8dda26 上报件落地）

* 缺陷：abortion done 仅 4 步（s1/s2/done/done），六道中间步漏记，触发 task-evidence-missing、check_all 全红
* 处置：既有 4 步不动，追加 6 步如实补录（每步标注"补录（原推进漏记）"并注明依据 commit），4→10 步；补录非杜撰，工作产物与门禁输出可复核
* 教训：done 步必须逐道推进；"六道并轨"只能在步内 evidence 说明，不能省步

### 移交（非本会话责任件，不代改）

* spacetime-holearg：check_markdown zh scope 5 hard（crlf×1+link-broken×4，补篇链接目标不存在）+para-align 91 段 EN 残留——归并行会话
* advance-directives：并行会话正在译（工作区 M，11 处 orphan-ref 为 defs 未拼接的在途态），不代改；本日 check_all 因此红，属在途噪音
* alcmaeon：para-align 78 段 EN 残留（s1_checked 在途），归其责任会话

### 下一步

* a 批续译：余 153 件（abracadabra 起）；收工前跑 check_bold_collapse


## 2026-10-30 A批第8件：abilities done

* 全译：导言+五节（分类学/能力中的诸区分/假设式理论/非假设式理论/应用）+致谢节；refs 81 条 defs 经 splice_defs 照录拼接（键序 81/81 一致、EN 混入无）；作者-年份引用组 [^key] 标记保留
* 术语裁定：倾向 dispositions / 可供性 affordances / 新倾向主义 new dispositionalism / 条件句分析 CA / 模态分析 MA / 双向力 two-way power / 潜能 potentiality / 其他可能性原则 PAP；相关词条八项题名取自 SUMMARY（残疾的定义与模型、行动、相容论、直陈条件、倾向、自由意志的不相容论论证、关于如何做某事的知识、模态逻辑）
* 体例：自写稿沿用 EN 斜体强调致 59 处 italic-cjk——convert_italic 转换后仍余 18 处"闭合 ** 后紧跟全角开括号"缺空格（AFTER_PUNCT 豁免表只收闭括号），批量补齐；check_style 0 issue
* 收工门禁：check_bold_collapse 0 候选（事故后新增必跑项）；check_academic --strict 0 硬错误；check_markdown zh scope abilities 0 hard；para_align 256/256 对（zh 残留=致谢段，EN 侧无独立对应块，良性）
* 任务九步逐道留证；a 批进度 8/160


## 2026-10-31 A批第9件：abraham-daud done

* 全译：导言+七节（引言/生平/主要著作/*ER* 的结构与来源/主要主题七小节/接受/结语）；note-1/2 译入脚注节；refs 58 条文献 defs 照录拼接（含 note 键总集 60/60 与 yuanwen 一致）
* 转写符号第二轮：闪米特转写 ‘/’（ayin/hamza）触发 curly-quotes 配对——凡与拉丁字母相邻者改 U+02BC（7 行），中文单引号引语不动；abrabanel 同款处置的推广
* 术语/题名：书题《崇高的信仰》《传统之书》《世代之书》《拯救书》《治疗书》《哲学家的意图》《政治体制》《生命之泉》；克雷斯卡斯《主之光》沿用 abner-burgos；人名依登记表（伊本·盖比鲁勒、伊本·西那（阿维森纳）首次括注、犹大·哈列维、萨阿迪亚·果昂）；相关词条七项取自 SUMMARY
* para_align 137/137 对；7 条 EN defs "残留"经键多重集+逐条 grep 证为 defs 前置布局错位、零缺失（与 abhidharma 同类裁定）
* 任务九步逐道留证；a 批进度 9/160
