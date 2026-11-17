# specs/039 执行记录

## 2026-11-16 · P1 治理层（已推送 8c2ed13f2）

* 立 [ADR-0063](../../rules/adr/0063-中文体例归一入s2.4双轴与转换保真不变量.md)（accepted），把三轮裁定固化为条文：s2.4 三轴、尾序 canonical（`脚注` 末位）、编号点号式、I2/I3 不变量、补丁准入谓词与 C1–C4、判定权只读、revert 扩 s2.4（含 done）、规则可判性四件套、LaTeX 第三轮否决。
* 规则落点：`rules/04` s2.4 节改双轴＋勘误轴、状态机两处括注、回退段补 416 口径；`rules/05` 新增“判定权与规则所有权”（含 fixer 放行自检三项、测量效度判例）；`rules/08` 新增 §14；`rules/README` 判例两条；`rules/adr/README` 索引；`AGENTS.md` 硬约束表增“体例归一”“派生保真”两行。
* 门禁：`check_all` 11 项全绿（未新增门，避免与 P9 重叠）。

## 2026-11-16 · P2 工具层

| 工具 | 变更 | 验证 |
| ---- | ---- | ---- |
| `tools/check_pairs.py` | 体例轴四则（`tail-order` 含脚注末位、`heading-number` 点号式与跳号、`h1-form` 作者括号＋英文题一致性、`errata-apply` 勘误落地）＋`--gate` 只对 `HARD_RULES` 计退出码；桩件与带点子文档豁免 | `a/abhidharma`（脚注前置）报 `tail-order`＋编号；`a/abduction`（裸号）报 4 条编号；`a/anscombe`（点号＋canonical）零 issue 退出 0 |
| `tools/check_en_patches.py` | C2 准入谓词（空白差／标记差）、字段齐备、`--strict` 升硬、`admission_bad` 计数 | 现存 3 条池内补丁全部判 `blank`（`admission_bad=0`，命中计数 3/3 相符） |
| `tools/check_yuanwen_fidelity.py`（新） | I2-lite 基线钉交叉核对（`md-hand-edited`／`source-drift`／`no-baseline`）＋`--deep` 的 I3 字母多重集比对（数字只作软信号） | A 字头 160 件 I2-lite 零异常 |
| `tools/task_ops.py` | `_style_gate` 挂 `advance --step s24`（`check_pairs --gate`＋`check_style`）；`revert-state` 目标态扩 `s2.4_termchecked`、源态集扩 `s2.5_checked`，加“历史无 s2/s24 记录即拒”守卫 | 单测 `tools/tests/test_adr0063.py` 21 例全绿 |

### I3 标定过程（白名单 v0，实测）

按 40 件、60 件两轮抽样逐个定性，形成白名单与判据：

| 差异类 | 定性 | 处置 |
| ---- | ---- | ---- |
| 目录（`div#toc`）文本 | 导航非内容 | 深度配对剥除 |
| 行内标签断词（`<em>A</em>s`） | 渲染同形 | 块级标签断词、行内标签不断词 |
| `References（引用注释）` ↔ `Bibliography` | 转换器命名 | 折叠同义节题 |
| 书目转 `[^key]:` 定义、Notes 段归位 | 合法移位 | 多重集判据（序列不敏感） |
| 作者行（`citation_author`）、`（原文脚注）` 括注、底稿注记行 | 转换器构造 | 显式剔除 |
| 图 alt 长说明 → 图注文 | 转换器构造（ADR-0037） | alt≥40 字入源流，短 alt 视为装饰 |
| 上下标 `G<sub>1</sub>` vs `G₁` | NFKD 同形 | NFKD 归一 |
| 注号、有序列表号、书号 | 两侧字面形态不对称 | 数字不入主判据，报 `digits` 软信号（数字面归三校数字对账／`check_math`） |

抽样结果：60 件 → 6 件残留（`aesthetic-testimony` 多 142 字母、`al-khunaji` 缺 294 字母等），已作为缺陷候选，待全量台账定性。

### 全量台账（1873 件，2026-11-16）

| 项 | 结果 |
| ---- | ---- |
| I2-lite 基线钉 | **零异常**（`md-hand-edited` 0、`source-drift` 0；仅 2 件 `no-baseline`）——全库 `yuanwen` 与转换登记一致，无手改产物 |
| I3 `--deep` | 1871 件可比，**381 件差异**（20.4%）：缺字为主 139、多字为主 205、双向 37；量级 >200 字母 109 件 |

**残差定性（重要，防误判为缺陷）**：抽 `formal-belief`（缺 49307 字母）、`logic-many-sorted`、`sartre`、`buber` 逐句核对，被报“html 独有”的句子（如 “The heart of subjective probability theory…”）**在 md 中确实存在**。根因是**数学定界符跨度两侧不等价**：html 侧 `\(…\)` 与 md 侧 `$…$` 覆盖范围不同（转换器可能合并/断开跨度），剥离后文本缺口位置不同，叠加多重集后表现为大额字母差。故 381 件**不能计入内容缺陷**，属工具噪声。

结论与后续：I3 暂列**审计档**（不进门禁）；门禁面先用 I2-lite（已零异常）＋`check_math`（公式数与内容）＋三校数字对账覆盖数学件。I3 若要升门，须先解决数学跨度归一（候选方案：两侧统一替换为同一哨兵并保证跨度边界来自同一解析，或仅在无数学件上启用）。

## 待办（P3–P9）

* 全量 `--deep` 台账与逐条定性（转换器缺陷 → 修 `yuanwen.py`；白名单缺项 → 登记）。
* 基线钉 I2-lite 全量跑，确认零 `md-hand-edited`。
* 30 件重复 H1 修 `yuanwen.py`（`citation_title` 前置条件），`expect=30` 定点重转。
* 勘误表 31 行／17 slug 落地核对（§8.1 yorck 零动作、§8.2 四件核读法＋译注）。
* 存量归一（编号 2076、脚注移段 87）与 416 件回退重走。

## 2026-11-16 · 补丁池目录化（用户裁定：补丁不是虚拟的，放固定文件夹独立存放）

| 项 | 内容 |
| ---- | ---- |
| 布局 | `baseline/en-patches/<id>.patch`（一补丁一文件，unified diff＋头注释字段，带 1 行上下文）＋`INDEX.json`（生成物，禁手改）；旧 `baseline/en-patches.json` 已删除 |
| 解析唯一实现 | 新增 `tools/en_patch_lib.py`（parse/load/admission），转换器、离线体检、迁移脚本共用 |
| 应用语义 | 行锚定：`find` 取整行、命中数必须 == `expect`、上下文行须在 html 中出现；失配抛 `PatchMismatch`（该件转换硬失败）。`git apply --check` 作独立预演（不写 en/） |
| 等价性证明 | 3/3 补丁：新行锚定应用 ≡ 旧 token 应用（逐字节），**yuanwen 产物无需重转** |
| 体检 | `check_en_patches --strict`：3/3 通过、`admission_bad=0`、`index_bad=0`、`git_check_bad=0` |
| 单测 | 新增 `tools/tests/test_en_patches_dir.py` 13 例；`test_adr0063` 池用例改读目录；两文件 **34 例全绿** |
| 文档 | AGENTS 硬约束行、`rules/04` s0 出口、`rules/README` 两则判例、ADR-0062 附记（只追加）、ADR-0063 §6、`contracts/cli.md` 权属行 |
| 迁移脚本 | `specs/039-md-standardization/bin/migrate_en_patches.py`（`--refresh` 幂等再生；本次 `--refresh` 用） |

## 2026-11-16 · P5 EN 收口：R2 守卫修复与英文镜像全量重转

用户批准"全量重转一次，零差异即基线成立；有差异停下列清单"。首轮重转 0 失败但产生 **368 件**差异——非零，遂停下复核。

| 项 | 结果 |
| ---- | ---- |
| 差异定性 | R1 孤立希腊字母文字化（ADR-0049 决策 6）＋R2 裸排环境包裹；抽样发现 R2 **双重包裹**：`$$ \begin{align}…\end{align} $$` → `$$ $$\begin{align}…\end{align}$$ $$` |
| 根因 | `tools/yuanwen.py` 的 `NAKED_ENV_RE` 守卫用 `(?<!\$)`/`(?!\$)`，只查紧邻一字符；SEP 输出 `$$ \begin` 隔一个空格即漏判 |
| 修法 | 新增 `_wrap_naked_env`（剥离空白后判"已定界即不动"）；单测 4 例（带空格已定界/裸排/紧贴/`$$` 计数），`test_yuanwen` **59 例全绿** |
| 重转 | 全量 1873 次、0 失败、**344 件**改动（较首轮少 24 件，即唯一差异为双包者） |
| 验证① 词面守恒 | 344 件逐行剥数学/markdown/希腊字母后比对：**0 件不守恒** |
| 验证② 环境在 `$$` 外 | HEAD 44 处/20 件 → 现 **28 处/15 件**（16 处系双包造成的假违规被修掉） |
| 验证③ 门禁 | `check_all` 11 项全绿；`en/` 与补丁池零改动；`baseline/entries.json` 随重转重算 344 件 `yuanwen.sha256` |
| 残差登记 | 剩余 28 处＝**22 处单 `$` 包裹显示环境**（`$\begin{align*}…$`）＋6 处其他排布；R2 未覆盖的另一类，未修，列 P5 残差待体例裁定（改 `$$` 属改既有形态） |
| 口径意义 | 本次重转让 `yuanwen` 首次真正等于 `convert(en ⊕ patches)`；"存量不回改"期间派生物与转换器已脱钩，双包缺陷即其证据 |

## 2026-11-16 · P5 续：R2 改状态感知（真页面实测驱动）

上节"残差 28 处"经**真页面渲染**复核后大幅修正——多数是我文本普查器的假阳性。

| 项 | 结果 |
| ---- | ---- |
| 渲染验证方法 | dev 服务器（端口 81）＋Chrome headless CDP（`specs/038` 的 mob.mjs 复用），取 `g[data-mml-node="merror"]` 与字面 `$$` 计数 |
| **单 `$` 包 `align*`（negation 4 处）** | **渲染正常**：`display=null` 但 `mtable` 正常、段落高度容纳、无裁切无重叠（间距 16px vs 块级 20px，仅视觉略紧）。**判定非缺陷，不改**，登记口径 |
| 真缺陷（第二次 R2 缺陷） | **数学内部的环境被再包一层**：`$$ \frac{$$…$$}{} $$`、`$$\left[ $$…`、`& $$…`。页面实测 hempel 2 merror（“Extra close brace or missing open brace”）＋4 处字面 `$$`，social-choice 4、word-meaning 2、qm 5 |
| 根因 | R2 守卫只看紧邻一个字符，看不出"该环境已在 `$$…$$`/`$…$` 内部" |
| 修法 | `wrap_naked_envs` 改为**单遍状态机**：`$$`/`$` 开关判定定界内/外，状态按行重置（还原后公式单行）；数学内一律原样。`test_yuanwen` **62 例全绿** |
| 重转（第三轮） | 0 失败，**仅 8 件 9 行**改动（全部为删除嵌套 `$$`）：discourse／hempel／intuitionism／principia／qm-consistent-histories／social-choice／type-theory-church／word-meaning |
| 复探 | hempel **0**、social-choice **0**；`{$$` 残留全库 **0** |
| 剩余 4 处（上游内容，非转换层） | word-meaning 1：`\left[ \begin{align*}…\end{align*} \right]` 环境嵌进矩阵括号（上游 TeX 结构）；qm 3：重复 `\label` 名。按 ADR-0062 不改 en/、不属转换器缺陷，登记待勘误表定性 |
| 门禁 | `check_all` 11 项全绿 |
| 附带发现（登记） | `baseline/entries.json` 每次全量重转都把**全部**词条的 `converted_at` 刷新，内容未变者也刷新 → 本次 1881 行时间戳抖动，掩盖真变更、增大并行冲突面。建议转换器改为“md 字节未变则不写/不更新时间戳”，另立小卡 |



## 2026-11-17 · P7 存量归一＋P4 试金石＋免抖动写入＋门禁 12 项（用户裁定：不进行实际翻译流程，做其余工作）

| 项 | 结果 |
| ---- | ---- |
| P7 归一（工具 `bin/normalize_zh.py`，--check 钉 → 写 → 幂等） | N 编号加点 **2076 行/367 件**；N2 编号对齐 yuanwen（H2/H3 逐字随原文 token）**53 处/16 件**（含 intellectual-property `4.5→4.4` 错号、aesthetic-testimony 补点、kaspi/kilvington 重复号）；F 脚注移段 **88 件**。合计 376 件 |
| 词面守恒 | 376 件剥编号后行多重集与 HEAD 全等；不等者仅 3 件＝此前已存在的 P6 未提交件（xenocrates/xenophanes/yorck），非本轮造成 |
| P4 试金石（results/p4-touchstone.md） | anscombe/abduction/abhidharma/social-procedures/tarski-truth/stub 六类判定全符预期；合成件行为由 35 例单测覆盖 |
| 检查器修正（假阳性清零） | pubinfo 限首节前题头区（书目 def 与正文叙述不再误报）；h1-form 容嵌套作者括号＋norm_title 剥 `*`/反引号；H3 形态规则撤销（编号一致性由 N2 对齐保证） |
| 全库残差（登记，翻译面依赖） | 硬档 19 处/13 件：尾节缺失 10（P8 依赖）＋编号 9（对齐跳过件，zh 缺节致计数不等）；`h1-form`/`pubinfo-form`/`errata-apply`/`note-anchor` 全零。**中文体例全库硬门挂起至 P8 完成**，登记前置清单即本行 |
| 免抖动写入 | `_write_if_changed`（md/补充材料/SUMMARY 同字节不写盘）＋`update_baseline` 嵌套免抖（仅 converted_at 变化视为未变，不写盘、保留旧时间戳）。两处教训：patch 为嵌套结构（平面比较恒假）、比较须把旧侧 converted_at 排除在键集合外 |
| 免抖动证明 | 全量重转（第 6 轮）`yuanwen/`＋`baseline/entries.json` **零改动**；同时即 I2 重放等值的确定性证明（同源 HTML ⊕ 补丁必得同 md） |
| 门禁 11→12 项 | `check_all` 增“转换保真（yuanwen≡基线）”`--gate`（I2-lite 全库零异常）；中文体例全库硬门挂起至 P8（前置清单见上） |
| 挂起（翻译面，本轮不动） | P6 余 14 slug＋12 件 cleared 译注小卡；P8 回退 416 件重走 s2.4（含句内括注→节迁移 365 件）；P9 中文体例全库硬门 |

## 2026-11-17 · P9 前置：I3 哨兵标定试跑＋双重题名收口（用户批准三项：①30 件重复 H1 ②工作区分线 ③I3 试做）

| 项 | 结果 |
| ---- | ---- |
| ① 双重题名（P5 尾） | 根因两类：26 件旧模板正文同文 `<h1>`（figure 先于题，`startswith('# ')` 守卫漏判）＋4 件**上游字面 `#`**（disjunction 例句 `<dd># Absolument…`、(31) 紧贴 `#Absolument`）。修法：`_drop_duplicate_h1`（同文去重、异文不动禁静默丢文）＋p/dd 发射 `_escape_leading_hash`（`\#` 转义，文字照录）。定点重转 30 件：词面守恒 30/30 全等、全库重复 H1 清零、`check_all` 12 项绿（79ead5c77） |
| ② 工作区分线 | 3 件 ADR-0062 收尾（journal/en-errata/036 log）已由并行会话收编（9cc7cc794），本轮树净 |
| ③ I3 哨兵标定 | `strip_math_ex` 三计数（spans/oversize/unclosed）＋SENTINEL＋对称性分类；9 例单测；试金石 5 件（3 件噪声隔离✓、1 件无回退✓、sartre/buber 反转**真缺陷**）；全库 8m14s：381 混杂 → 320 math-asymmetric（判据不适用）＋195 真候选。**新缺陷族：书目嵌套 `<li>` 丢弃，129 包受影响**（登记归 018/023 保真线，另立修复卡）。详见 `results/i3-sentinel-trial-20261117.md` |
| P9 升门前置（更新） | ①195 件逐条定性；②书目嵌套 li 修复（expect≈129）；③math-asymmetric 320 件中 203 兼差件复核；④中文体例全库硬门（挂起至 P8） |

## 2026-11-17 · 书目条目蒸发修复（I3 标定发现项落地，用户批准）

**归因修正（重要）**：前节「书目嵌套 `<li>` 丢弃」归因**作废**——嵌套 li 经实证本会进入 bib_entries（夹具与真件 A/B 双证）。真机制＝**`build_cite_keys` 无姓氏路径整条 `continue`**：主文献区条目以年份起首（作者＝条目主体本人），节首 `prev_surnames` 为空、`_section_author('Bibliography')` 无「Works by X」可依 → sartre 191 进 161 出，30 条文献（含 rybalka-1936b「F. Alcan」整条）蒸发。工具 915 行注释「定义行必须保留，否则整条文献从产物消失」正是本条应守的原则。

| 项 | 结果 |
| ---- | ---- |
| 修法 | `build_cite_keys(entry_texts, fallback_author=None)`：无姓氏且无前条可继承时用 `<slug>` 兜底键（键=`sartre-1936a` 式，与既有键约定一致）；pats 不匹配＝未引用 def，不强生文内标记；调用点传 `fallback_author=slug`（1270 行）。ul/ol 分支不动（首版补丁打错层，已回退） |
| 试金石 | sartre cite_defs 161→**191**（+30 精确吻合）、buber 102→**144**、F. Alcan 落盘 |
| 全量重转 | **79 件改动、新增 def 行 897**、正文标记重挂 3 处；免抖动下其余 1794 件零改动 |
| 词面守恒 | 9 件初筛“不合格”逐件解剖＝两类良性：①转义类 5 件（blockquote/行首字面 `#`→`\#`，文字零变化，首版转义修复的延续）；②键位重排类 feyerabend（恢复的 1991 条目入键后既有引注重挂——**落点经页码核验正确**：`(Feyerabend 1991, p. 526)`→`-1991-2`＝Conversation def，pp. 487–527 含 526；Conversation 条目仍在册）。词级守恒（剥标记/还原转义后 old−new 字母差）＝**0 缺字** |
| 复算 | sartre/buber I3 `--deep` 归零；`check_all` 12 项全绿 |
| 遗留 | ①「134 包嵌套 li」扫描量的是良性结构属性，与缺陷无关，作废；②500+ 候选面（195−sartre/buber 等）仍待逐条定性；③zh 侧对应件的 defs 差额由回炉/翻译面消化（用户裁定不动） |

## 2026-11-17 · P8 回退执行（加强复核：先补机检可达性，再动状态机）

| 项 | 结果 |
| ---- | ---- |
| **复核发现（阻断级）** | `revert-state --to s2.4_termchecked` 的既定语义是「checkpoint 视为已完成，随后正常推进即 s25」；而 `_term_gate/_style_gate` 只挂 `step=="s24"`（前驱须 `s2_checked`）。**回退件历史中 s24 已消费，advance s24 不可达** → 416 件重走会整体绕过三轴硬门。按 ADR-0043「s2.4 增项并入 s25 凭证」先例，s25 并挂术语＋体例＋勘误三轴（+审计双钩）。ADR-0063 已补记（2026-11-17），rules/04 状态机括注同步。`TestS25ThreeAxes` 3 例锁定（正常路径复检／回退后复检／体例轴失败阻断） |
| 台账（只读预跑） | `bin/revert_ledger.py`：回退面 **414 件**（s2.5 395／r2 16／r3 1／done 2，glossary 与无 zh_doc 的 legacy 任务除外），三轴机检 **绿 359／红 55**；红灯 `quote-spacing 43 件次、bold-spacing 17、heading-number 15、italic-cjk 14、curly-quotes 10、tail-order 5、no-html 1`。结果 `results/revert-ledger-20261117.{json,md}` |
| 台账副产（真实漏网） | **P7 归一器枚举 `[a-z]/*.md` 漏掉 `1/` 非字母目录**：`1/18thGerman-preKant.md` 6 处裸号标题未归一 → 已补点并与 yuanwen 编号对齐（硬档余量 0）；`bin/normalize_zh.py` 枚举扩 `[0-9a-z]`。历史 specs/011 一次性脚本同形枚举，属战役遗留不再改 |
| 回退执行 | `bin/revert_batch.py`（dry-run 默认、`--execute` 写、幂等跳已回退）：先 3 件试金石（append-only revert-state 步抽验通过），再全量 **356 件**，共 **359 件**置 `s2.4_termchecked`，0 失败、3 skipped（已回退）。快照留 `state/p8-snapshot-before-revert.json`（可复算/回滚） |
| 回退后状态面 | `s2.4_termchecked 359／s2.5_checked 53／r2 1／r3 1／done 1／cleared 166／pending 617`；红 55 件按原状态留存，待修后并入 |
| 复核门禁 | `check_all` 12 项全绿（过程中发现并修正 ADR 补记 2 处直角引号） |

## 2026-11-17 · P8 红件清障：机械体例修复器（53 行）＋二轮回退 37 件

| 项 | 结果 |
| ---- | ---- |
| 修复器 v1 事故（记录） | 首版 `style_fix.py` 全行扫描：bold 674／italic 662（检查器仅报 17／14）——**在照录豁免区（书目/脚注定义行）动手**。教训与 memory 的「style 修复器事故链」同型：修复器不得自带判据，必须**由判官点名后动手**。已废弃 v1 计数 |
| 修复器 v2 设计 | 只改 `check_style` 点名的**行与规则**（quote-spacing／bold-spacing／italic-cjk／no-html）；**逐行改→临时文件复判→该行目标规则清零且无新违例才保留，否则回滚该行**；dry-run 不碰原文件（临时文件复判） |
| 执行 | 55 件 57 目标行：**改 55／回滚 1／残余 2**；试金石 3 件（lakatos／object／zhu-xi）词面等值、余 issue 0、二跑幂等 0 改动 |
| 复判 | `check_all` 12 项全绿 |
| 二轮台账 | `results/revert-ledger-after-stylefix-20261117.json`：55 红 → **绿 37／红 18**（curly-quotes 10／heading-number 9／tail-order 5／quote-spacing 2／bold-spacing 1） |
| 二轮回退 | 37 件（3 试金石＋34 全量）→ `s2.4_termchecked`；累计回退 **396 件**，余 18 件红留原状态 |
