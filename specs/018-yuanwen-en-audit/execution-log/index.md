# 018 战役执行台账 — 索引

协议见 `../spec.md`。每词条一行详细台账在 `ledger-<letter>.md`；本文件只记字母级覆盖进度与会话接力点。

## 覆盖进度（有译文口径，随做随更）

**范围裁定（2026-11-13，用户）：先核实有译文的词条**——tasks state ∈ {drafted, s1–s3_checked, r1_reviewed, done} 共 **422 条**；无译文 1450 条待后续。

| 字母 | 有译文词条 | 已审计 | 发现项 | 修复词条数 | 译文同步数 | 台账文件 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| a | 63 | 10 | 8 | 1 | 1 | ledger-a.md |
| b–z | 359 | 未开始 | — | — | — | — |

## 转换器修复（避回归，spec A4）

| # | 缺陷 | 修法 | 回归防线 |
| ---- | ---- | ---- | ---- |
| 1 | 引块内 `<br>` 三行图式被并行成单行 | 行标记拆行（表格/列表/定义/代码区不动；`&nbsp;` 缩进保留） | 单测 3 例 |
| 2 | em/strong 标签内空白剥失致粘字 | 空白移到星号外侧 | 单测 2 例 |
| 3 | 纯 `<b>` 被兜底剥标签丢加粗 | 转 md 粗体（星交错内容维持降级） | 单测 1 例 |
| 4 | li/dd 内嵌真表被行内剥壳降为裸文本（020 移交「整表丢失」，实为 10 件 41 表） | `list_to_md`/`render_blocks` dd 分支按 CommonMark 内容列缩进渲染真表（文本行＋缩进表＋续文本） | 单测 2 例 |
| 5 | 嵌套表降级 `（嵌套表：…）`（020 移交 16 件 128 处；全库普查 83 张，多为公式盒布局表——分数横线、∑ 布局、推理规则盒） | 2026-11-14 裁定：消毒后原样 HTML 透传（font 剥壳、`\(\)`/`\[\]`→`$`/`$$`、img→`../assets/<slug>/`、`\|`→`&#124;`、单行化）；`table_to_md` 行解析前占位 + 外层剥壳防御 + `inline_to_md` 兜底占位 | 单测 5 例 |
| 6 | 旧转换器书目文本腐蚀（agrippa `Princenton`、marsilius `Lachoix`/`causasalité`/`J.-L-Solère`） | 重转即愈（en 逐字核证）；并入 4/5 的占位管线后不再复现 | regression_scan OTHER 逐件定性 |

全量重转（2026-11-14 会话 2，2421 文件）0 失败；regression_scan：2387 不变 / 34 OTHER 逐件定性（25 预期缺陷件 + 7 同类延伸至 supplement/appendix/figdesc——020 清单只扫主文件漏掉 + 2 旧腐蚀修正）/ 文件增删 0。check_math 130,236 条公式 0 丢失。

## 020 移交缺陷分诊结论（2026-11-14 会话 2）

* **误报结案三类**：findlay「断尾 6 行」（H/K/LU/PP/PW 五行上游本在 `<!-- -->` 注释内，浏览器不渲染、正文 0 引用、锚点 0 存活）；图片未引用 13 件（全部为 `../../symbols/` 学术工具图标有意剥除，或 `<!--pdf include…-->` 注释内 PDF 专版——浏览器可见的 `.svg` 版镜像均已接线；020 扫描未建注释语义模型）；`\(\)` 泄漏（384+15 处全在 `$$…$$` 内忠实嵌套、SUMMARY.md 转义字面量、typelogical/nonexistent 上游未闭合定界符保真——0 转换器泄漏）。
* **工具伪影定性**：mally-deontic en 19↔yw 34（yw 计入 notes.html 脚注表，en_tables 只读 index.html）；mereology 87↔95 与 2 行"缺失"（notes 表 + 配对错位，行 139/217 实在场）；saadya en 4↔yw 0（4 表在引用定义行内为 HTML 形态）；word-meaning「缺图」（alt 含 `]` 破 IMG_MD 正则，镜像行 176 实在场）。check_tables_images.py `TABLE_LINE` 已扩展认缩进表行；`script/t020_cmp.py` en_tables 已改注释剥离＋配平取表。

## 会话接力点

- 2026-11-13 会话 1：战役立项，spec 落盘。自 `a` 批 `abduction` 起按字母序推进。
- 2026-11-13 会话 1 更正：spec A3「yuanwen/ 为 gitignore 本地库」证伪——yuanwen/ 自 ADR-0027 起入库（4260 文件），修复产生 git 变更；表格图片两维抽为 020 战役先行（specs/020-table-image-audit/），其发现项同步记本台账。
- 2026-11-13 会话 1（020 战役代记）：表格/图片两维全库对账完成，**镜像侧缺陷清单**见 `specs/020-table-image-audit/results/mirror-defects.md`：嵌套表降级 16 件 128 处（字面 `（嵌套表：\| … \|）` 混入英文镜像）、整表丢失 8 件（logic-dialogical 48→29 等）、findlay 缩写表断尾 6 行、图片未引用 13 件、mereology 单表被拆多块。均属转换器（本战役维护），待修后由 020 复跑 `script/t020_cmp.py` 复核。
- 2026-11-14 会话 2：020 移交缺陷全部处置完毕（真缺陷 4/5 两类修复＋三类误报结案，见上两节）。**后续移交**：specs/023 三向回归审校战役（2026-11-14 用户裁定 A3）统一接管 en↔yuanwen↔译文逐行人审与译文轴回填——34 个修复文件中 27 件有对应译文（agrippa-nettesheim、altruism-empirical、benjamin、consciousness-representational、future-contingents、ibn-sina-logic、information-entropy、lambda-calculus、logic-conditionals、logic-connexive、logic-dialogical、lukasiewicz、mally-deontic、marsilius-inghen、medieval-syllogism、nonwellfounded-set-theory、pascal-wager、pm-notation、presupposition、proof-theory-development、pythagoras、reasoning-automated、saadya、sign-language-semantics、situations-semantics、typelogical-grammar、zeno-elea），其新增表格/公式盒内容按 ADR-0037 口径翻译落入译文，由 023 逐条回源定性推进；透传段的两处渲染根因（`\<<` 翻倍、裸 `*` 转实体）由 023 会话补修（commit 61361eb5d，5 单测）。
- 接力规则：后继会话先读本索引覆盖表，再读当前字母台账末尾的「接力指针」，从指到的词条继续；禁止跳条。
- **战役冻结（2026-11-14，用户裁定）**：剩余镜像轴审计与转换器维护移交 **specs/023-triple-regression-audit**；已核 10 条（abduction、abelard、abilities、abner-burgos、abortion、abrabanel、abhidharma、abraham-daud、abstract-objects、abu-bakr-al-razi）镜像轴结论沿用不重做，其译文轴由 023 照常审。023 的 ledger-a 从本台账接力指针所指词条（academic-freedom）起续。
