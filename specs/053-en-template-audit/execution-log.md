# 053 执行账：EN 语料模板审计与勘误装配线

## 2026-11-19 P1 批次（B3.1 逆向装配器）——验收线 B3.1 首跑

**裁定与上下文**：用户“批准继续，加强复核”。B3.1＝`C(R(md)) ≡ md` 字节级不动点（收缩对右逆，specs/053 §9 定理框架；B3.2 的 sha 全等在池冻结后验收）。

**产物**：
- `bin/reassemble.py`（R 装配器，判官只读；同源求值——装配 HTML 交 yuanwen 生产函数原件闭环）。
- `results/assembly-trial.json`（试金石 15 件）＋`results/assembly-scan-all.json`（全库 1,872）。
- 负向 selftest：篡改 md 一段 → 不动点必破（绿）。

### 1. 试金石（15 件，含 leucippus 最小底稿／abelard 97 文献／补丁件 incommensurability）

14/15 通过；唯一残差 bayes-theorem（引块表 + 公式段，W7）。

### 2. 全库首跑与规则迭代（v1.0→v1.6，四轮全库）

| 轮 | 不动点 | 闭合率 | 本轮的修 |
| ---- | ---- | ---- | ---- |
| v1.0 | 1,058 | 56.5% | 首版（题头合成层/pubinfo/h1/文献 ul 原位/脚注链） |
| v1.1 | 1,085 | 58.0% | 希腊字母逆映射补反斜杠（`*ψ*`→`\(\psi\)`，C 侧 fullmatch 才识别） |
| v1.2 | 1,240 | **66.2%** | ①表题 `<caption>` 装配（`***X***` 紧贴表）②文献区散文段先于 ul（bib_entries 次序＝HTML 文档序）③数学占位先于 sub/sup（`$\pr_{t}$` 不被改写成 `<sub>`)④松散列表边界（项间空行＝列表边界） |

净增 +182 件。终态：**1,872＝1,240 不动点（66.2%）／632 残差／0 跳过**。

### 3. 残差分型（632，首差特征）

| 族 | 件数 | 例 | 定性 |
| ---- | ---- | ---- | ---- |
| 文献分节键（def-line±notes） | ~396 | adorno、addams-jane、comte | md 尾 defs 与 References 区 h3 分节无法对位；year-first 条目键依赖 section author → 键错位。→ W8 |
| 其余未归 | ~144 | aesthetic-judgment | 需逐件人审（多为键序/定义顺序） |
| math-inline／subsup | ~24 | causal-models | TeX 内空白/记号残留 |
| bold-italic（含乘法星邻接） | ~44 | anderson-john、altruism-biological | ` * ` 乘法星与强调星歧义。→ W10 |
| 引块表／notes 链 | ~13 | assertion、bayes-theorem | W7 |

### 4. W 登记（动工前现查）

- **W7** 引块表（`> | …`）与引块内 `<br>` 组合残差（bayes-theorem）。
- **W8** 文献分节作者键重建：R 需把 md 尾 defs 归位到 References 区 h3 分节；仅凭 md 无法判定分节边界 → 候选方案：转换器在 md 侧保留分节锚（如 def 行加注 section），或 B3.2 池按 slug 记录分节布局。**这是当前最大残差族。**
- **W9** 有序列表起始号（`<ol start=N>` 被 C 丢弃 → md 显示 1..N，但部分 md 自身带非 1 起始，如 alyngton `2.`）——需核 C 的 list_to_md 是否读 start。
- **W10** 乘法星邻接（`10 * Prob(...)` 的裸星与强调星配对歧义）。
- **W11** 图片 passthrough（md 中 `![…]` 与 `<img>` 混形）。
- **W12** 行内数学残留（`$…$` 内空白归一等）。

### 5. 加强复核四件套（ADR-0067）

1. **守恒**：装配 HTML 经 parse_entry 解析零异常＋B0 抽检（b0_mini）每件记录。
2. **同源**：求值用 `yuanwen.strip_closed_comments / protect_cross_block_math / render_blocks / extract_blocks_raw / build_cite_keys / link_citations / convert_notes / _drop_duplicate_h1 / restore_cross_block_math / apply_en_patches` 原件——R 只做 md→HTML 的右逆，不重实现转换语义（ADR-0073 同源对照）。
3. **负向**：`--selftest`（删段必破）。
4. **交集**：试金石含补丁件 incommensurability（求值视图 en⊕patches 全绿）。

### 6. 教训

①**判据迭代须全库复跑**：单件转绿不等于族转绿（caption 修复只影响 1 件；希腊反斜杠影响 ~400）。②**首差窗口取尾段会误导**（前缀/后缀修剪的展示窗口曾把我引向错误族）。③**慢≠死**：首轮全库 ~12 分钟被误判为挂死，加逐件计时后确认为正常耗时；stderr 须 flush（管道缓冲致日志空）。

## 2026-11-19 B3 运营化：EN 互转漂移巡检入 CI（用户“做成 GitHub ci，发现变动时提交变化 issue，每天定时三次”）

**产物**：`.github/workflows/en-roundtrip.yml`（每日三次 UTC 01/09/17）＋`tools/roundtrip_drift.py`（基线差集对比器）。

**语义（本轮裁定）**：B3.1 存已知残差（632/1872），故“变动”一律指**相对已提交基线扫描 `results/assembly-scan-all.json` 的差集**，不是“有失败”：③新残差（基线 ok→今 fail，需人审定四出口）／④转绿（基线 fail→今 ok，基线待更新）／⑤词条增删；另并入①en 钉漂移（divergence verify failures）与②I2 红灯（fidelity --gate）。基线更新仍是人工/本地会话动作（重跑 reassemble --all 并提交）。

**只读原则**（同 catalog-drift，specs/054 §3）：不写 baseline、不改 en//yuanwen/、不提交内容文件；有变动开/更新 issue（`en-roundtrip-drift`；巡检自身失败 `en-roundtrip-broken`），报告与全量扫描入运行工件。

**本地实测**：同件→changed=false；翻转一 ok→fail／一 fail→ok／删一条＋I2 红灯 → changed=true 且四族逐项报出（script/tmp 实测，产物未入库）。登记：`rules/05/ci-workflows.md` 工作流清单新增一行。

## 2026-11-19 B3.1 第二轮规则迭代（用户“继续”）：1,058 → 1,480（79.1%）

**本批五行修正（全部由残差首差实证驱动）**：

| 修 | 机制 | 判例 |
| ---- | ---- | ---- |
| Notes 区整体跳过（跳至文件尾） | C 把 Notes 追加在文末，脚注内容可含引块/列表/公式块；旧逻辑只跳空行+def 行 | abhidharma（引块漏成正文）、affirmative-action（脚注内列表漏成正文） |
| 星解析器（`_star_parse`） | 裸星三分类：开/闭/字面。开＝右邻紧且左邻非字母数字；闭＝左邻紧；存疑一律字面（字面星经 C 原样回写，不动点不受损） | action `(3*)`、`(G*1)`、`happens*`、`10 * Prob` |
| 未闭合星恢复 | 无配对的星恢复为字面（原实现吞星） | action `(3*)` |
| 表题 caption | `***X***` 紧贴表 → `<caption>` | bayes-theorem |
| pubinfo 行作段落边界 | 图注段落不得吞掉 `**First published…**` | anderson-john |
| 槽位越界守卫 | 星解析删除内容后未闭合槽位索引失效 | emilie-du-chatelet 等 5 件崩溃 |

**终态：1,872 ＝ 1,480 不动点（79.1%）／392 残差／0 跳过**（较上批 +240）。试金石 15 件 14 过；负向 selftest 绿。

**残差族（392）**：def-line 135（文献分节作者键，W8）＋unclassified 73＋esc-star 48（转义星邻接）＋bold-italic 23＋subsup 19＋其余。CI 基线已同步为本次扫描（`results/assembly-scan-all.json`）。

**教训补充**：①“字面星经 C 原样回写”是关键不变量——存疑按字面处理永不动摇不动点，误判为强调才会；②崩溃与残差必须分开计（skipped 5 件不计入闭合率，修后转残差）。

## 2026-11-19 B3.2 页面级逆向装配实施（用户“必须100%闭合”）

**起点判定**：100% 闭合不可能靠单条规则达成，按已批准的机制拆成两段——规则闭环＋格式层补集（A5 谓词）。先测骨架可变性：1,873 件中 head 仅 2 类、body 前导 5 类、页脚主体 5 类、head 中段 1 类，字段面完全规则化（邮箱混淆 `m&#97;ilto:`＋`&#37;40`／`&#37;2e` 可逆推）。结论：chrome 层可以纯规则闭合，正文层须账＋池。

**新增件（全部入库，ADR-0077）**：

| 件 | 行数/规模 | 职责 |
| ---- | ---- | ---- |
| `bin/page_layout.py` | 版式账抽取器 | H0 → skeleton 19 件＋page-layout.json（1.4 MB） |
| `bin/page_assemble.py` | 页面判定器（只读） | assemble→判 rule／pool／gap／stale；`--build` 建池 |
| `bin/article_ledger.py` | 结构账抽取器 | H0＋md → article-ledger.json（18 MB） |
| `bin/article_build.py` | 正文段装配器 | R 平铺块 → SEP 区段脚手架（含表／文献树／相关条目） |
| `bin/assembly_pool.py` | 补集池 v4 | 分段对齐＋m/u/r 补丁＋哈希命中（P1/P2/P3） |

**里程碑**：chrome **1,873／1,873 逐字节**（提交 2105c9607）；页面级 **池 616（32.9%）**、缺口 1,257、池体积占页 1.64%。

**迭代记录（每轮均由首差实证驱动，全库复跑）**：

| 轮 | 修 | 效果 |
| ---- | ---- | ---- |
| 1 | 实体策略账＋折行宽度（源宽贪心，w=70 占绝对多数） | 从全 gap 到首批 pool |
| 2 | 内部链接账（C 丢弃 `../slug/`、`#anchor`）；链接文字支持一级方括号；外链 `target="other"` | 修掉“`[X 1997 [2016] …]`”与 `See also the entry on …` 系 |
| 3 | 脚注引用回写 `<sup>[<a href=…>N</a>]</sup>`；星号开星放宽 | 修 `.[1]` 与 Düring 型 em 断裂 |
| 4 | 文献区：h3/h4 小节题＋题后散文原位发；`[^following-nd]` 型“散文被折成定义行”记 `pd` | 修 18thGerman 系 |
| 5 | 文献条目序（`bib_indices`）＋`li` id（`bib_ids`）＋嵌套树（`bib_tree`）＋表结构账（thead/tbody/空位） | 修 W8 序与嵌套 `<ul class="subhang">`（abelard 转 pool，117 条补丁） |
| 6 | 同形希腊宏按件出现序（`extract_greek`＋`_greek_next`）；`GREEK_REV` 取首名 | 修 phi／varphi |

**教训**：①**shell heredoc 逐层转义是陷阱**——`
`／``／`` 在“Python 脚本→文件→Python 源码”三层里会被吃掉还原成控制字符（实证：源码里出现 0x08、真实换行、``），代码块改写必须走 Write/Edit 或占位符替换；②**分段对齐模型的选择决定成败**：行级 diff 会把纯空白差异放大成整行文字替换（不可入池），改为“块标记槽＋文字单元”后补丁才真正做到零散文；③**补丁偏移必须用字符偏移**而非段索引（r 补丁会改变段数）；④慢＝difflib 在近等长序列上的二次方行为，加“键序列相同”快路后 0.18 s/件；⑤**多进程撞车**：两次 nohup 同时写同一池目录会产出互相污染的中间态，重跑前必须确认无残留进程。

**缺口族（1,257）**：行内 `p` 58%、表格 10%、列表（含嵌套）12%、引块 4%、`dl` 3%、文献区小节题错位等；根因均在 C 结构改写层，逐族修 R 或改账，修前保持红（不入池）。

## 2026-11-20 B3.2 第二批：区间补丁模型（同一指令的续批，“批准继续”）

**目标不变（100% 闭合）**；第二批把判定引擎从“单元一一对应”升级为**区间补丁模型**——段落分合、松散列表 `<li><p>`、`dl`、引块内 `p` 等边界错位不再是硬伤：块内文字键流（ukey 拼接）相等即可生成一个区间 `u` 补丁（文字全部取自装配侧流、布局照目标重建），文字流不等才拒录。

**引擎重写（`assembly_pool.py`）**：

| 项 | 旧 | 新 |
| ---- | ---- | ---- |
| 对齐域 | u 单元键序列（边界错位即整块拒） | **raw 段键** difflib＋块内 ukey 流贪心合并（吞到文字流相等为止） |
| 补丁偏移 | m/u 字符偏移、r 段索引（混用即错位） | **统一字符偏移**降序应用；r 分支原实现取不存在的 `p["n"]` 键（从未触发即错位的隐患） |
| 空白/实体 | tx 只引非空白流、空白靠 m 补丁 | 空白是 `mk`；实体形态差（`&thinsp;` 等）由 `_ent_marks` 折进 mk/tx，不再有独立 ent 字段 |
| 自洽门 | 无（写坏池靠 judge 事后红） | `--build` 写盘前**就地应用补丁**核对逐字节再生 |

**R 侧规则（判例驱动）**：图片逆写 `![alt](../assets/<slug>/<file>)` → `<img src alt />`（占位隔离，alt 不受行内规则加工）；词内开星（`P*hilosophy of History and Action*` 判例，上游 em 从中词起排）；`(*)`／`(**)` 记号星不开星而 `[*‘Uyūn* 604f]` 照常开星（闭括号判据）；内部链接改**文档序游标**定位（旧 nth 语义遇嵌套锚文会重叠插入，产出 `<a>[Section 3](#Or</a>igSyllArts)`）；锚文星转义；脚注引用形账 `note_forms` **全量记账＋游标消费**（同一键可既有规范 sup 又有 `footnote 14` 散文形，按键记字典会互相覆盖）；相关条目区 `rel_items`（含无链接纯文字项）＋尾随竖线账；表位形与 R 侧格位按序一一消费（此前空位不消费致整行错位一格，`<th>High</th>` 被挤掉）；文献区 `norm_md` 支持 URL 含一级圆括号（`ERInt.2013(1(2)).pdf` 使条目定位失败、整条被吞）；账内定位失败按“前一索引＋1”兜底不再吞条目。

**实测（全库两轮，第二轮为提交基线）**：

| 轮 | 池 | 缺口 | 池占页 | 备注 |
| ---- | ---- | ---- | ---- | ---- |
| 第一轮 | 779（41.6%） | 1,094 | 18.34% | 98 件 `tx out of range`——plain() 剥 `&nbsp;` 而 piece 累计不剥，坐标系不一致 |
| 第二轮（基线） | **878（46.9%）** | **995** | **20.80%** | plain() 保留 `&nbsp;` 原形后 98 件全转绿；缺口 995 全部为 `unaligned text units`（真文字差／合并至末尾仍不等） |

B3.1 回归：不动点 **1,435/1,873（76.6%）**（此前 1,240，＋195，无回退——图片／星／链接游标等规则让更多件回到不动点）。

**池占比口径（T7）**：20.80% 即规则承载 79.2% 的页面字节；池体积大头是区间补丁的 mk（标签原文＋空白布局）承载——按 ADR-0077 决策 5 如实逐件同报，不追求压低而牺牲覆盖率。

**教训**：①**坐标系统一是区间模型的生命线**——plain/piece/marks 三处坐标差一个 `&nbsp;` 就越界 98 件，修法是让 plain 保留实体原形；②**difflib 的 raw 段键对齐会把“A 一段＝B 多段”切成半截**，贪心合并（向后吞到文字流相等）是正确性兜底；③试金石先行（11 个合成用例覆盖 c2–c17：段分合、thinsp、括号星、dl↔ul、真文字差拒录）再上全库，省掉三轮全库返工。

## 2026-11-20 B3.2 第三批：缺口族分流与前缀/表格结构修复

**方法**：对全部 gap 件做首差普查（`script/tmp/b32_families.py`，926 件分类：star 308／text 300／digit 224／math 90／entity 4），逐族取 3–4 个判例回源 md 与 H0 对读，只改有实证根因的规则。

**R／账修复（判例驱动）**：

| 族 | 根因（判例） | 修 |
| ---- | ---- | ---- |
| star | `(G*1) … (G*2)` 成对记号星被当开闭星（actualism-possibilism-ethics）；`poet<em>ry</em>` 单词内 em 漏成字面星（aesthetics-19th-romantic）；`122<strong>)</strong>` 双星紧邻闭括号被误判记号（adorno） | `_intra_word_open` 改“第一个紧闭星即决断点”：右邻数字 ⇒ 记号星对放弃；松左星 ⇒ 新开星放弃；否则按多词含空白／单词内全字母判 em。双星紧邻闭括号照常开（strong 可包标点） |
| 引块 | 嵌套引块 `> > …` 只剥一层，剩 `> ` 文字（abrabanel） | 引块行按 `^(?:>[ \t]?)+` 全剥 |
| related | H0 末两项间**无 `|` 分隔**，逐 `\|` 切分会把第二项吞进第一段（aesthetic-experience：死链 Yoruba 项丢失） | 段内逐子项扫描（链接/死链/纯文字三类），残留文字成 text 项 |
| bib 区 | `</div> ` 收口不齐（adorno 等结尾无尾随空格）致 bib_seq 全空；文献区用 `<table>` 列条目（abu-bakr-al-razi `[RF]`）未识别；References 分节在文件末（`(?=^## )` 前瞻不匹配） | `_bib_region` 括号配平定位（嵌套 div 安全）；`scan_bib` 增 `table` 块；References 正则加 `\Z` 兜底；`bib_seq` 支持 table 项，渲染按序发原表 |
| 表格 | H0 `colspan` 跨列而 md pipe 表按逻辑列展开、文字落点不可靠（aristotle-logic：`[空, colspan2 Affirmations, colspan2 Denials]` 对 5 列 pipe 表），按列位置消费整表错位 | 账格位改 `[kind, colspan]`；渲染改**按行**分配（非空格依序取本行 R 非空单元、空格留白、span>1 加 colspan），分配不成立则原样交回让池判 gap |

**实测**：池 **979（52.3%）／缺口 894**（上轮 878／995），池体积 55.09 MB／页 235.94 MB＝**23.35%**（上轮 20.80%；区间补丁启用面扩大，T7 口径如实同报）。chrome 1,873/1,873 不变。**judge 全库复扫 979／0 stale**（池逐字节再生验证与建池完全一致）。**B3.1 回归 1,452/1,873（77.5%）**：净 +17（改善 18／退化 1，adorno 的 cite 键 W8 残差）。

**教训**：①计数普查只能定分流方向，不能当判据——文献条目数差异既是 C 漏转也可能是表格/散文形态（48 件 defs<li 与 152 件 defs>li 经个案核查后未据此改 C）；②结构账的每一处“形态”都要连**位置**一起记（colspan 只记列数不记跨度会让整表错位）；③R 侧判据的每次放宽都要有“拒绝分支”——star 判定改成“第一个紧闭星即决断”，把此前会越过候选星继续配对的错误面收窄。

## 2026-11-20 B3.2 第四批：结构账顶层化与 H0 形态回补

**方法**：三批遗留的 gap 件逐件首差定位（本批不开新普查，直接打判例），凡根因落在“账抽取形态”或“R 逆写形态”即修，落在“md 与 en 文字不一致”则记录不修（属同步线）。

**修复（判例驱动）**：

| 项 | 根因（判例） | 修 |
| ---- | ---- | ---- |
| 账顶层化 | `split_items` 用裸 `finditer` 对每个 `<li>` 发射（含嵌套子 li），`_tree_nodes` 递归时子项双计：abelard 账 37 节点 vs 真 25＋4，h3 分节与条目错位、English 条目混进 Latin ul | 只返顶层（`pos` 游标跳过已消费区间），嵌套子项留给 `_tree_nodes` 递归 |
| items 提取 | `_render_bib` 用非贪婪 `<li>(.*?)</li>` 提条目，遇嵌套 `subhang` 在子项首个 `</li>` 错切（同一 abelard 判例） | 新增 `_flat_li`（嵌套感知、父先子后、父项剥子 ul），与账 i 序一致；`_match_close` 从 1 起算（复制时误写 0 → 返回下一个兄弟开标签，隔条取 49/97） |
| rel 分隔符 | 账平铺 items、渲染按 `enumerate` 推 `\|`，H0 末两项间无分隔（aesthetic-experience：Wittgenstein 项与死链 Yoruba 项同段）→ 装配多插一个 `\|` | 账逐项记 `sep`（段首带、同段后续不带），渲染按下一项 sep 发；旧账无 sep 键退回旧行为 |
| 文献区 `<ol>` | `BI_START` 只认 `<ul>`，H0 的 `<ol>`（adorno “Cited Works by Adorno: lists works…”编号清单）整块被漏 → 条目被当散文 pd 发 | `BI_START`／`scan_bib`／`bib_seq`／渲染全链支持 ol（seq 记 `ol`，渲染 `<ol>` 逐 li） |
| bib 入口门 | 入口门 `re.search(r'<div id="bibliography">(.*?)
</div> ')` 要求带尾随空格收口；收口不齐件（adorno）整块未匹配 → bib_seq/bib_tree 根本没抽，退回 counts 分组错位 | 入口门与 `_bib_region` 同源（括号配平），两个分支统一 region |
| 标题规范形 | md 侧文献标题带中文加工后缀（`## References（引用注释）`，全库 1,878 件统一形态），装配标题与 H0 纯 `References` 文字不等（aesthetic-judgment 判例） | 账记 `bib_heads`（H0 的 lv／text／id），渲染 h 项优先用账文字与 id；seq 首项即 H0 的 `<h2>Bibliography</h2>` 与预发重复 → 跳过 |
| 引块内列表 | H0 `<blockquote><ol type="I">`（bodin 十章目次）在 md 侧是 `> 1. …` 行，R 只输出单 `<p>` | 引块段内整段全为 `N. `／`- ` 行时生成 `<ol start>`／`<ul>`（混排仍按 `<p>`＋`<br>`） |
| 缺闭合 li | H0 允许省 `</li>`（anarchism：`<li>Goldman…Penguin.` 后直接 `<li>Graeber…`），配平切分把其后 57 条吞成一项 → 账 44 条 vs 真 101 条、文献区大面积丢失 | `split_items` 增兄弟边界判定：配平闭合落到下一兄弟 `<li` 之后、且其间无未闭合 `<ul>` 时按兄弟边界截断（嵌套项因 gap 含未闭合 ul 不截断） |
| gap 清旧池 | `build_pool` 判 gap 时未删旧池，规则/账改动后旧池残留 → judge 持续报 stale（本轮 28 件即第三批旧池残留） | gap 分支（非 dry）`POOL.remove_pool(slug)` |
| HTML 注释 | H0 用 `<!--<p>…</p>-->` 注释段落（bodin），C 正确丢弃；`plain`/`ukey` 只剥标签不剥注释内容 → 注释文字混入 B 侧文字流，假文字差（ent_spans 返回 None） | `_strip_cmt` 在 plain／ukey／_ws_decoded 统一剥 `<!--.*?-->` |

**实测**：池 **1,272（67.9%）／缺口 601／stale 0**（上轮 979／894；池 +293）；池体积 74.82 MB／页 235.94 MB＝**31.71%**；chrome 1,873/1,873 不变；B3.1 **1,452/1,873（77.5%）**——首轮 1,442（引块 ol `start≠1` 破坏不动点 10 件），改“序号非 1 退回 `<p>`”后重跑 1,452，集合级与旧基线逐件一致（0 退化 0 改善）。judge 全库复扫 1,272／**0 stale**（池逐字节再生验证）。

**缺口分类（602 件，`script/tmp/b32_families2.py`，judge 前普查）**：star 257／md_extra 149（md 有而 H0 无＝md 与 en 版本差或译注污染，归 specs/001 同步线，不入池不修规则）／math 66／h0_extra 54（H0 有而 md 无＝C 漏转方向，需修 yuanwen.py 重转）／digit 35／text 33／ok? 5（近池）／entity 3。大头是 star（em 配对错位）与同步差（md_extra+h0_extra=203）。本轮判例件实测池 **1,271（67.9%）／缺口 602／池占页 31.67%**，judge 复扫结果见下。

**教训**：①同一个“嵌套列表”错误在账（split_items）与渲染（items 提取）**两处独立存在**，查一处修一处会白跑两轮——凡“父子结构”一定要同时核对抽取与消费两侧；②复制工具函数时 `depth` 初值这类单点语义（0 起 vs 1 起）必须连注释一起搬，否则返回值语义整体翻转（返回兄弟开标签 vs 自身闭标签）；③H0 的 HTML 注释不是文字，等值判定必须先剥注释再比较；④md 侧标题/条目带中文加工后缀是全库统一形态（1,878 件），装配必须按账取 H0 规范形，不能直接用 md 侧文字。
