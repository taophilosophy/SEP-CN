# 053 批次实施记（第二十六～三十二批）

> 指针：验收线现状与下一批入口见 [`spec.md`](spec.md) §11；本文件是**已完成批次**的实施记（缺陷／修法／实测／教训），一例一节。早期批次（十四～二十五批）见 `spec.md` 同名节与 [`execution-log/`](execution-log/index.md)。

## 10.26 第二十六批：脚注引用形与内部链接消歧（2026-11-23）

**缺陷一（脚注形漏记）**：`extract_note_forms` 只认 `<a href="notes.html#note-…">` 一种写法，四类 H0 异形全漏：
- 片段不带 `note-` 前缀：`href="notes.html#complex" name="note-complex"` 显示 `1`（binarium）、`#supplement-4` 显示 `4`（chance-randomness）、`#1`+`name="note-1"`（bayes 类）；
- 属性序反置：`<a name="note-1" href="notes.html#1">`（logical-constants）；
- 方括号与 `</sup>` 之间有空白：`…</a>]\n </sup>`（bell-theorem）。
漏记 → R 一律出规范形 → 页面差（12 件）。

**缺陷二（双 sup）**：md 对这类异形写作 `^{[[^note-N]]}`（sup＋方括号已被 C 显式编码）；R 的 `_note_ref` 仍发完整 `<sup>[<a>N</a>]</sup>`，与外层叠成双层 sup。

**缺陷三（锚文数字抢位）**：`links` 账只记 text/href，锚文为数字（`20`）时同文多处出现（裸 `[20]` 标记 vs `(<a>20</a>)`），R 的游标法会把链接挂错位置（possible-worlds）。

**缺陷四（lead 的四种系统性错位与连锁饿死）**：短锚文一旦本行无匹配即 defer，而 defer 的链接**阻塞队头**——一条卡死则该页其后所有链接永不消费（首扫实测：plato-laws 58 条、connectives-logic 37 条、logic-algebraic-propositional 32 条全由单条卡死放大）。错位根因四类：
- **行首列表记号**：C 把 H0 的 `<ol><li>` 转成 md 字面 `5. `，锚文紧跟记号时行内左邻只剩 `5.`，与账里跨行前文恒不符（plato-laws 编号前提 `H`）；
- **单希腊降级**：账侧把 `\(\phi\)` 整段抹掉，md 侧对应位置是 ADR-0049 降级后的 `*φ*`，尾词错位一格（connectives-logic `#ref-34`：账 `. (note` 对 md `φ. (note`）；
- **可见脚注号**：H0 留文 `[19]`，md 侧写作 `[^note-19]`（已被剥），两侧尾词不同（implicature `(1)`）；
- **注释残片**：H0 夹写 `<!-- … 1958 -->`，账尾词取到 `1958 -->`（findlay）。

**缺陷五（幽灵链接）**：H0 里被 `<!-- -->` 停用的 `<a>`（整行文献项）仍被 `extract_links` 采入账——md 无锚文可消费，入账即永久卡头。正文区内 9 条／4 页（findlay 5、logic-combinatory 2、privacy-health 1、logic-intuitionistic 1）；外围区（TOC/相关条目）另有 253 条本就被剔区排除。

**修法**：
- note_forms 扫描放宽（任意属性序、任意片段前缀），规范形判据＝「被 `<sup>[` … `]</sup>` 包住（**容空白**）且锚文＝片段去 `note-` 前缀」；非规范形记**完整替代片段**（含或不含外层 sup），R 原样发。
- R 侧 `_bare`（md 为 `^{[` … `]}` 包裹）时只发锚；**B3.1 判官（无账）仍发双层 sup**——C 对 `#N`+`name=`+`<strong>` 异形不回折为裸 `[^note-N]`，往返只有外层 sup 才能复现 `^{[[^note-N]]}`。
- `links` 账增 `lead`＝锚文左侧**最后两个词**（空白归一、小写；按字符取上下文会被 H0／md 折行差异打乱，词边界才是折行不变量）；R 按词比对优先选位，本行无匹配即 defer。消歧**只对短锚文（≤3 字符）**生效：长锚文本身足够唯一，强加词比对反因折行/标记差异误伤（无条件比对曾使未消费链接 1,850→2,896）。
- 两侧同式归一（缺陷四）：账侧 `extract_links` 入口**注释整体抹白**（保偏移，兼治缺陷五）并剥 `\(…\)`／`[…数字…]`；R 侧 `_lead_ctx` 剥 `[^key]`、`$…$`、`[N]`、行首列表与引用记号，且**两侧词表都只认含 ASCII 字母的词**（数字/标点尾词不可判即放行旧游标法）。

**实测**：脚注形 12 件全转池。全量双通道（建池 → judge 独立复扫 → B3.1）：**pool 1,731→1,746（93.2%）／gap 142→127／stale 0**，池占页 **47.21%**，judge 与建池**逐件同值**；`scan_vs_head` delta 只有 gap→pool 15、**失池 0**；B3.1 **1,638 不变**（0 转绿 0 转红）。链接消歧的独立评测（`script/tmp/eval_links2.py`，逐页跑 `restore_links` 不装配）：lead 版未消费 1,815 条，摘掉 lead 的对照 1,812 条——残差仅 implicature 2／publicity 1，而 plato-laws／connectives-logic 等 127 条饿死全部消除。

**判例（chance-randomness，字节等值 ≠ 位置正确）**：摘掉 lead 时该件能 pool，但装配把 `#thm2` 的锚文 `2` 挂到了跨文件链 `supplement B.<a href="#thm2">2</a>.` 上——H0 该处实为 `supplement <a href="algorithmic-randomness.html#B.2">B.2</a>`，错位被**整段 m 补丁**吞掉而字节全等。lead 版此处不再误挂，故该件回落 gap；真缺口是下一批的靶子：**带片段的裸兄弟文件链**（`href="other.html#frag"`，既不以 `../` 也不以 `#` 起头）不入 `links` 账，且 C 在 md 侧把这类链的片段整个丢弃（`chance-randomness.basic-chance.md` 无 `#A.2`），全库正文区 **73 页 514 条**。

**教训**：①「规范形」判据要写成两侧可证的形式（H0 形态 ↔ md 形态 ↔ R 输出）；②账里存「完整替代片段」而非字段组合，R 原样发才有唯一解；③同一判据在 B3.1（无账）与 B3.2（有账）两侧允许输出不同，只要各自闭环；④**游标法加过滤必须防卡头**：defer 语义会由一条放大成整页，任何消歧判据都要能在“不可判”时退化为旧法（放行），且退化路径要与账侧**同式**；⑤字节等值可能由补丁池掩盖错位——判“位置正确”要看锚文落点本身，不能只看 sha。

## 10.27 第二十七批：带片段的裸兄弟文件链（2026-11-23）

**缺陷**：`extract_links` 只收 `../`（跨词条）与 `#`（页内锚）两族；H0 的**裸兄弟链** `href="other.html#frag"` 不入账。C 在 md 侧把这类链**整个丢弃**（全库 md 侧 `.md#frag` 链 0 条），锚文成纯文本，差异只能靠补丁池硬兜。正文区 **73 页 514 条**（无片段的 `other.html` 另有 616 条，md 已保 `slug.target.md` 形、R `_link` 可还原，**不入账**——收了会双发）。

**修法**：账 href 过滤放宽收 `^[A-Za-z0-9._-]+\.html#.+`；R `_link` 增同形分支（`<a href="other.html#frag">` 原样发）。

**次生缺陷一（折行破锚）**：`wrap_html` 词级折行会把新插入的锚文从中间折断，而 H0 整行不折（original-position 判例：`Constructivism,\nObjectivity…`）→ 文字层错位、`_sub_diff` 对不齐。修法：**整锚作一个不可折单元**（锚起点允许折行）；H0 正文 129,369 条锚里仅 54 条锚文内含换行（0.04%），锚不可折是全库实证口径。

**次生缺陷二（嵌套插入）**：C 会把 H0 的「锚文＋后随普通文字」合并成一条 md 链（original-position：`[The Argument… and the Four Stage Sequence](difference-principle.html)`），账再往这段文字里插锚，产出 `<a>` 文字段里带字面 `[..](..)`——H0 从不嵌套 `<a>`。修法：护栏——候选落在既有 md 链接文字段（与 `_link` 同一取域式）内即弃此候选。普查 136 页存在同文异处情形，护栏只拒嵌套位、不改其他位。

**实测**：第一版（无两护栏）全量 **+1／−1**（chance-randomness 转、original-position 失池）——净零不予采纳；护栏后全量双通道（建池 → judge 独立复扫 → B3.1）：**pool 1,746→1,748（93.3%）／gap 127→125／stale 0**，池占页 **47.27%**，judge 与建池逐件同值；`scan_vs_head` delta＝**gap→pool 2（chance-randomness、determinism-causal）、失池 0**；B3.1 **1,638 不变**。抽样 26 页（原 pool 随机 25＋original-position）护栏后 27/27 可池。链接独立评测：未消费 1,829 条（＋13＝figdesc/补充材料族，其锚文在 md 已并入保留链接或文字有异，见上）。

**教训**：①新账入「可发锚」必须配两项防线：锚不可折＋不嵌套——插入会改变折行与链接语法环境，三条规则要一起上，单上任何一条都只是把差异换个形态；②收益预估要按「原 gap 的受影响页」算（73 页里只有 12 页原为 gap，其余 61 页差异已被池兜住），本批净收益 2 件符合该上界；③「补丁池兜住的页」不是稳态——新账一变就可能翻面，凡扩账都要全量复扫。

## 10.28 第二十八批：宏 ↔ 裸字形之希腊-cursive 区（2026-11-23）

**缺陷**：`_em` 的孤立希腊斜体判别 `re.fullmatch(r"[A-Za-zα-ωΑ-Ω]+", …)` 只覆盖 U+03B1–03C9；C 单希腊降级产出的 `ϱ`(U+03F1)、`ϑ`(U+03D1)、`ϖ`(U+03D6) 落在希腊-cursive 补充区，判别失败 → 右逆发 `<em>ϱ</em>` 而非 `\(\varrho\)`（qm-decoherence 判例：md `*ϱ*` 对 H0 `\(\varrho\)`）。`φ`（U+03C6，属主区）不受影响——varphi 的歧义走既有的按件 `greek` 宏序账。

**修法**：判别字符类扩到整个希腊与希腊扩展块 `[\u0370-\u03FF]`（`GREEK_REV` 的键集本就全落此区）。一行改动，C 侧零改动。

**实测**：定点 10 件（ϱ/ϑ/varphi 混合族）→ 5 件即回池（其余 5 件另有显示式取域等结构性差异，非本族）。全量双通道（建池 → judge 独立复扫 → B3.1）：**pool 1,748→1,758（93.9%）／gap 125→115／stale 0**，池占页 **47.63%**，judge 与建池逐件同值；`scan_vs_head` delta＝**gap→pool 10（qm-decoherence、time-travel-phys、ergodic-hierarchy、games-abstraction、logic-paraconsistent、connectives-logic、equivME、formal-belief、logic-games、rationality-normative-nonutility）、失池 0**；B3.1 **1,638 不变**。缺口普查刷新为 **md_extra 76／h0_extra 13／text 9／math 8／star 4／digit 3／entity 2**（math-delim 细分 23→15）。

**教训**：①字符类要按 Unicode **块**写，不要按“我以为的希腊字母”手抄范围——希腊-cursive 变体（03D0–03FF）常被漏；②一行 R 修复的收益评估也要全量复扫：定点族只看见 5 件，全量带出 10 件（`ϖ`/`ϵ` 等旁支字形同区受益）；③φ/varphi 歧义与字形判别是两条独立通道，别混在一个修复里。

## 10.29 第二十九批：账锚方括号保护（2026-11-23）

**缺陷**：`restore_links` 插入 `[锚文](href)` 时直接用原文切片，H0 有些锚文自带方括号（promises 判例：`Problematic Promisees and the Uptake Condition (&sect;5.1]`——上游原文即以 `]` 收尾）。裸 `[]` 会让 `_link` 的链接语法匹配失效，`[..](..)` 整段留在文字层。全库账锚含方括号 **223 条／23 页**（discourse-representation-theory 86、platonism 72、leibniz-exoteric 14…）。

**修法**：插入前把锚文里的 `[`/`]` 换占位符 `\x06`/`\x07`，`_link` 出口还原。纯 R，一行式改动 + 一句还原。

**实测**：定点 8 件含方括号页全部可池；全量双通道 **pool 1,758→1,759（93.9%）／gap 115→114／stale 0**，池占页 **47.64%**，judge 与建池逐件同值；`scan_vs_head` delta＝gap→pool 1（promises）、**失池 0**；B3.1 **1,638 不变**。缺口普查刷新为 **md_extra 75／h0_extra 13／text 9／math 8／star 4／digit 3／entity 2**。另 4 件含方括号的 gap 页（diagrams／discourse-representation-theory／game-theory／whitehead）余差为显示式取域与段数错位，非本族。

**教训**：①「整段可池」不等于「位置正确」——18 件含方括号页此前全靠补丁吞差，规则修好后池字节反而增大但语义正确（池不是唯一 KPI）；②插入型的账（链接/注号）都要考虑锚文本身的语法字符（`[]`、`*`、`$`）；③收益上界仍按「原 gap 的受影响页」算，本批 5 件 gap 里只修好 1 件。

## 10.30 第三十批：引块形态账（bq，前置件）（2026-11-23）

**缺陷**：`_render_bq` 一贯发 `<blockquote><p>…</p></blockquote>`；H0 另有 **6,120 处裸装引块（首子非 `<p>`，798 页）**，内容直接排在标签里。套 `<p>` 每处多 4 个段，整页 `_sub_diff` 对不齐（descriptions Δ109、desert Δ44、ambiguity Δ9 判例）。

**修法**：账增 `bq`＝按文档序的 0/1 序列（1＝裸装，首子 `<p>`/`<table>` 记 0），只记有裸装的页（798 页）；R `_render_bq` 按游标消费，裸装分支不套 `<p>`、行分隔用 H0 拼写 `<br />`。切区与 `extract_links` 同式（TOC／学术工具／相关条目各自引块不算）。

**实测**：全量双通道 **pool 1,759／gap 114／stale 0（0 转池／0 失池）**；B3.1 **1,638 不变**。定性：**前置件**——32 件 `m:<p | u:text` 首裂族全部推进到下一层（descriptions Δ109→3、ambiguity Δ9→5），段数相等的 gap 件 3→10 件；全库重聚类的首裂签名分布显著前移。下一层主靶（按首裂签名计数）：`u:<strong | m:<dt` 11 件（`<dl class="sentag">` 定义列表，H0 有 dt/dd、A 侧发段落）、`u:text | m:</li` 10 件（松散列表 `<li><p>…</p></li>`）、`u:text | m:<p` 7 件、`m:<p | u:<span` 6 件。

**教训**：①账只能记「md 里不可辨」的形态差；裸装与否正是这种（C 统一转 `> …`）——但一个账只解一层，解完首裂会推进到下一层，**要按「首裂签名聚类」排队而不是按族名清单排队**；②0 转池的前置件也值得上：它让后续每一族的可对齐面变大，且失池风险为零（B3.1 无账路径不变）。

## 10.31 第三十一批：`_link` URL 白名单（2026-11-24）

**缺陷**：`_link` 对 md 里**一切** `[…](…)` 形态都当链接还原。但 md 链接的 URL 是**闭集**（全库普查 25,679 条：`http(s):`／`../assets/`／`../`／`#`／`notes.html#`／`slug(.slug)*.md`／`X.html(#frag)?`）；闭集之外的 `](…)` 是**上游记号的字面文本**——ambiguity 判例：H0 原文 regimented 记号 `[∀<em>x</em>:Bachelor(…)](Unmarried(<em>x</em>,<em>w</em>))`，md 原样保留，R 把它吃成 `<a href="Unmarried(x,w)">` 坏锚，文字层多出一对括号差。

**修法**：`_link` 入口加白名单 `_MD_URL`（闭集七形态），不匹配即原样保留整段匹配文本。

**插曲（白名单首版过紧）**：md 形态含**下划线**（`spacetime-holearg.leibniz_equivalence.md`），首版 `[a-z0-9-]+` 拒掉该合法链 → spacetime-holearg 失池；普查 944 条 md 链的实际字符集（`[a-z0-9_-]` 段名）后放宽为 `[a-z0-9_-]+(\.[A-Za-z0-9_-]+)*\.md`，复测 24/24 可池。

**实测**：全量双通道 **pool 1,759→1,760（94.0%）／gap 114→113／stale 0**，池占页 **47.68%**，judge 与建池逐件同值；delta＝gap→pool 1（ambiguity）、**失池 0**；B3.1 **1,638→1,639（+1）**——白名单同时修好一件往返件。缺口普查刷新为 **md_extra 74／h0_extra 13／text 9／math 8／star 4／digit 3／entity 2**。

**逐件取证定调（下一阶段）**：`script/tmp/greedy1.py`（模拟 `_sub_diff` 贪心延伸，直击文字流永不衔接处）抽 9 件取证，剩余 gap 均为**真实内容差**而非形态差；全 113 件取证普查（`script/tmp/forensic_all.py` → `gap-forensics.json`）聚类为 **B_extra 29**（H0 有文 A 缺：缺图注如 anderson-john photo caption、缺书目条目如 al-qudat、C 列表标记丢失如 anaphora `(1)`）／**A_extra 15**（A 有文 H0 缺：疑似 C 位移/重复）／**order 1**（kant-development `mv²` 对 `mv2` 上标形）／**other 68**（区间错位，需逐件开窗取证）。不再有可批量修的机制族——下一阶段按件定通道：C 侧保真（dl 拍平、列表标记）／R 侧修复账／账外原文补记。

**教训**：①「`[…](…)` 形态＝链接」是过强假设——语法匹配必须配语义白名单；②白名单收窄要先普查**全部**合法形态（含下划线、大写段名），漏一类就失池一件；③首裂签名聚类给出的是**表层**裂点，真失败点要用贪心延伸探针（`greedy1.py`）直取。

## 10.32 第三十二批：头部图组位移（photo_pre_h1 账）与 pubinfo 行位假设（2026-11-24）

**缺陷一（pubinfo 行位假设）**：合成层只认 md 前三行的 `**First published…**`；H0 有头部图段的件，C 的 md 把图注行插在 pubinfo 前把它挤出前三行 → pubinfo 落成普通段落，整页段结构错位（whitehead 判例）。

**缺陷二（头部图组序）**：H0 的照片/题注块在 `<h1>` **之前**（`<div class="figure wide">` img＋题注），C 的 md 把 h1 提到首行、图与题注块留在其后；R 按 md 序发则段序错位（26 页，取证普查 B_extra 29 件的主力）。

**缺陷三（连锁）**：重排后题注行（纯斜体）落进主循环 `i<=3` 的作者行免发区被误吃，真作者行反被发段（berlin 判例）。

**修法**：
- pubinfo 合成层去行位上限，改为全文首个匹配行（`_PUBINFO_DONE` 只发一次）。
- 账增 `photo_pre_h1`（H0 首个 `<h1>` 前有 `<img>` 记 1，26 页）；R 装配内部把「首个含 `![` 行＋紧邻题注行（非标题/pubinfo/列表、≤200 字符）」提到行序最前（保块间空行；img 行在 pubinfo 后即正文图，不重排）。yuanwen 不动，B3.1 无账不重排。
- 作者行免发改**精确匹配**（`*%s* % ", ".join(meta_authors)`）＋重排跟走的题注行排除；`i<=3` 兜底保留。
- `article_build.build` 头部块原位化：h1 **之前**的块（头部图段）不再卷进 `<div id="preamble">`，按原位发在 h1 前（H0 序＝照片段→h1→pubinfo→preamble）。

**实测**：定点 21 件头部图族 19/21 可池（berlin、meinong 余 figure 包裹层形态，留逐件取证）。全量双通道（建池 → judge 独立复扫 → B3.1）：**pool 1,760→1,774（94.7%）／gap 113→99／stale 0**，池占页 **48.18%**，judge 与建池逐件同值；delta＝**gap→pool 14**（anderson-john／bradley／church／emerson／hartley／james／johann-herbart／montaigne／prior／reichenbach／reid／royce／russell／whitehead）、**失池 0**；**B3.1 1,639→1,652（+13）**——pubinfo 行位假设同时压着 13 件往返件。缺口普查刷新为 **md_extra 63／h0_extra 12／math 8／text 7／star 4／digit 3／entity 2**。

**教训**：①「行位假设」是隐形耦合——合成层只认前三行，任何头部插行都会连锁破坏 pubinfo 与作者行两处；②重排会触发免发区的宽松匹配误吃（题注也是纯斜体行），宽松匹配必须配精确形态清单；③取证普查的 B_extra 标签是启发式，真因要用贪心延伸探针逐件开窗（whitehead 的「缺图注」实为段序错位＋行位假设双重因）。
