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

## 2026-11-21 B3.2 第五批：star 族分诊与词内闭星修复

**方法**：star 257 件先子模式普查（a_extra 172／shift 54／b_extra 31），a_extra 172 件经 replace 窗口标签判定 **172/172 全部 r_pair**（H0 对应处均有真 em，无一 md_extra）——星族主流是 R 配对错位。判例回源（africana）：H0 `T<em>he Sociology…Chang</em>e`（em 从词中起排），md `T*he…Chang*e`＝词内开星＋**词内闭星**。

**修复**：`_intra_word_open` 决断条件改「第一个紧闭星右邻**非数字**」即进文字形态判定（多词含空白／单词内全字母）。旧判据只认右邻非字母数字——词内闭星 `Chang*e` 的右邻字母 `e` 漏判，整对星字面化；`(G*1)…(G*2)` 右邻数字排除不回退。**纯增量规则**：改前改后成功路径不变。

**同批回退记录（嵌套星三轮）**：①歧义预模拟（can_close∧can_open）②括号左邻收紧 ③贪心残留（n_lit/n_runs≥4）——三轮 B3.1 净退化 3→7 件均大于 B3.2 收益（+1），全部回退至 da27aa026。根因定性：C 对嵌套 em 转不出外层星（`<em>A<em>B</em>C</em>` → `A[*B*]C`，外层整个丢失），H0 字面星残留（al-farabi-metaphysics `*is more deserving…of*` 即字面星字符）与真嵌套在 md 扁平形态上**不可区分**。专项开放：候选＝账记 em 嵌套结构／yuanwen.py 转出嵌套标记。

**实测**：池 **1,274（68.0%）／缺口 599／stale 0**（第四批 1,272／601）；池占页 **31.79%**；chrome 1,873/1,873 不变；B3.1 **1,452/1,873 持平、集合级 0 退化**。判例：africana 转池（269 补丁）。

**教训**：①分诊先行——172/172 全 r_pair 的结论直接推翻「H0 字面星为主」的猜测，把主力从不可解的嵌套问题转到可修的词内闭星；② Census 的锚坐标系必须与判定坐标系一致（ukey 流 vs 原文，首轮 118/172 noanchor 全是坐标错位）；③「replace 窗口原段拼接」是判定 H0 标签形态的最短路径（无需全文定位）；④判据迭代以 B3.1 全库净退化数做止损线，止损要果断（三轮教训累计）。
## 2026-11-21 B3.2 第六批：C 侧转义改造与结构化强调（B3.1 1,452→1,569，池 1,274→1,359）

**方法**：接第五批回退结论——R 侧形态试探三轮不收敛的根因在 C 侧有损（md 里字面 `*`／`$` 与定界符不可区分、嵌套强调整块丢失）。本批先改产生方（C），再让判下方（R）跟着简化，全程以 B3.1 集合级对照做止损线，每轮全量重转＋全库复跑。

**C 侧改造**（`tools/yuanwen.py`）：

| 项 | 旧缺陷 | 新语义 |
| ---- | ---- | ---- |
| 文本层转义 | 标签外字面 `*`/`$` 直通 md，与定界符不可分 | `_esc_lit` 逐字转义 `\`→`\\`、`*`→`\*`、`$`→`\$`（单射；R 占位还原） |
| 强调转换 | 四条单层正则（em/i、strong、b 降级），嵌套整块失配、外层被兜底剥壳丢失（strong 套 em 679 处/77 件、em 套 strong 81/38、em 套 em 255/82） | `_emph_tags_to_md` 栈式单趟：同类嵌套压平、异类嵌套照发、空白外移（`&nbsp;`/U+2028）、缺闭合回删、孤立闭标签忽略、跨 `<br>` 引块行不发表、相邻同类合并 |
| 数学体美元 | `\($\ell\)`／`\(n \cdot $10{,}000\)` 包成 `$$…$`，右逆无法分辨定界符 | 行内体 `$` 全转义 `\$`；显示体只转边缘（体内 `$…$` 是真嵌套，qm-consistent-histories 判例） |
| 空公式 | `\(\)` 产出 `$$`（propositional-function） | 空体不产定界符 |
| 裸排环境 | `\begin{align*}` 走文本层转义成 `\begin{align\*}`，ENV 正则不匹配、整块失去数学语义（epistemology-visual-thinking） | 数学占位后先暂存 env（ENV_SPAN_RE），收尾补 `$$` 包裹（体单行不变量保持） |
| 希腊斜体嵌套 | `<em>\(\psi\)-ontic</em>` → `**ψ*-ontic*`／`*…*φ*…*`，右逆误配（qm-retrocausality／tense-aspect） | `_mark_math_in_emph` 标记强调内数学占位符，希腊字母分支改出裸字符 |

**R 侧配套**（`bin/reassemble.py`）：`_star_parse` 改 run 逐星消费（整 run 全作开星优先→按 slot 最内层先闭；`*q***P**`＝闭 em 1 星＋开 strong 2 星）；撤 `_intra_word_open` 与“左邻字母数字不开星”全部试探；code 段占位；`\$`/`\*`/`\\`/`\#` 占位还原；数学改扫描式占位（显示体允许成对单美元）；`\(\d+\*+\)` 记号星占位撤除（吞掉合法闭星，histfem-condorcet `(1786*)` 判例）。

**检查器配套**（`tools/check_yuanwen_fidelity.py`）：`strip_math_ex` 增 `dollars=False`——html 侧裸 `$` 恒为字面（全库实测正文区 728 处/105 件皆币值，真公式一律 `\(\)`/`\[\]`），旧式按数学跨度剥会把 `$0.75…$1` 中间正文吞掉、与 md 侧 `\$` 字面成假不对称；作者行剔除限 count=1（图注整行 em 恢复后 `^\*…\*$` 会误删，berlin 判例）。

**实测**：B3.1 **1,569/1,873（83.8%）**，集合级 **0 退化**（转绿 117／转红 0）；B3.2 建池 **1,359（72.6%）／缺口 514／stale 0**（+85 件转池）；池占页 **34.70%**（31.79%→34.70%，T7 如实同报：池增大＝规则覆盖扩展＋嵌套标签入池，验证力相应下降）；chrome 1,873/1,873 不变；I2/I3 `--gate` 0 issue（1,873 全过），深比对软信号 305（math-asymmetric 252＋text-stream 53；2026-11-17 基线 322）。中间轮次：1,467→1,521→1,562→1,551（反斜杠转义引入 17 件转红，加 `\\` 还原后恢复）→1,569。

**教训**：①判据试错的终点是语义层——把字面/定界在产生方（C）转义分离后，R 侧三轮不收敛的形态试探问题整体消失；②C 改动必须全量重转（含 entries.json sha 登记）并以 B3.1 集合级对照止损，任何“顺手修一处”都要全库复跑（第 4 轮反斜杠转义一次性引入 17 件转红，靠集合对照当场定位）；③嵌套强调的正确表示是栈不是更强的正则；md 扁平形态表达不了的结构（em 套 em、跨行 em）宁可压平／不发表并交池补，也不产歧义星流；④检查器与转换器要同批改：字段语义变了（`$` 不再是数学定界符），对称面（html 侧 strip 规则）不同步改就会整批假阳性。

## 2026-11-22 B3.2 第七批：图注定界修正（池 1,359→1,483，79.2%）

**方法**：第六批后 514 件缺口族普查（`script/tmp/b32_families2.py`）：star 204／md_extra 156／h0_extra 59／text 37／digit 34／math 19／entity 3／ok? 2。star 204 逐件首差定位，主流为图注标签：H0 `<span class="figlabel">Figure 1:</span>`，C `figure_to_md` 注入 `*Figure 1:*` 后仍走 `inline_to_md`，被第六批的文本层全转义写成 `\*Figure 1:\*`（字面星）——**第六批的语义改动波及既有注入点**（判例 action-perception／actualism-possibilism-ethics／animal-social-cognition）。

**修复**：`figure_to_md` 注入点改占位符（`\x17N\x17`），`render_blocks` 完成后还原为真定界星。md 回到真 em，R 正常配对出 `<em>`，`<span class="figlabel">` 的还原归 B3.2 格式层池。

**实测**：B3.1 **1,569/1,873 持平，集合级 0 退化 0 改善**（与第六批基线逐件一致）；B3.2 建池 **1,483（79.2%）／缺口 390／stale 0**（+124 件转池）；池占页 **38.49%**（T7 如实同报）。

**遗留族（390）**：md_extra（md 与 en 同步差，specs/001 线不修规则）／h0_extra（书目结构元素：`<ol>` 手排号 `1.`、缩写键块 `[AOP]…`、文献分节标题 `Primary Literature`／`Secondary Literature`、表题 `Table 1`、交叉引用注 `See section 2, above.`——需账记列表与分节形态，待批）／text／digit。

**教训**：改转换层语义（转义）时必须回头扫**同一层里的字符串注入点**（`'*%s*' % …` 这类手工拼定界符的旧代码），否则旧注入会被新语义当字面处理——本轮 204 件即此因。

## 2026-11-22 B3.2 第八批：链接题注守卫与公式形态账（池 1,483→1,486）

**缺陷一**：links 账把内文引用挂到题注标签上（belief-merging：H0 `Table 1` 出现序 0,2,3,4,5,6 全在正文，第 1 次是题注 span）。先试“全局出现序＝账 nth”精确匹配，**全库实测池 −9**（1,483→1,474，失池 17 件：md 与 H0 出现次数不等时全错位），已回退；终法＝保留文档序游标＋题注跳过守卫（md 侧 `*Xxx N:*` 题注行、锚文在行首且后接 `:` 不作为链接位）。

**缺陷二**：裸排显示环境多出定界符——C 的 `wrap_naked_envs`（ADR-0049 决策 6）把裸 `\begin{align}` 包成 `$$…$$`，md 里两种形态都成 `$$`，R 一律发 `\[…\]`。新增结构账 `math_forms`（文档序 `br`／`naked`，289 件有账；`article_ledger.extract_math_forms`），R 按游标还原，账记 `naked` 时只发环境体。

**实测**：池 **1,486（79.3%）／缺口 387／stale 0**（上批 1,483/390）；转池 4（axiom-choice／belief-merging／confirmation／decision-theory），失池 1（discourse-representation-theory，公式游标错位）；池占页 **38.59%**；B3.1 **1,569 不变**（两账在 B3.1 路径下均传 None）。

**教训**：账里的精确序号不等于更好的定位——账 nth 与 md 实际出现次数不等时精确匹配会全盘错位；启发式＋局部守卫更稳。转换层为渲染加的包裹必须同时入账（`math_forms`），否则右逆无从还原。

## 2026-11-22 B3.2 第九批：字面编号段落转义（池 1,486→1,513）

**缺陷**：H0 有 `<p>\n1. (Quantity) According…` 形式的作者手打字面编号段落，全库 **224 处／35 件**（kilvington 35、alyngton 29、causation-law 16、rationality-historicist 15、fallacies 13）。md 行首 `N.` 被 markdown 当有序列表，右逆发 `<ol>` 吞号，文字层缺 `1.`。

**修复**：C 侧 `_escape_leading_hash` 从“只转 `#`”扩为块级行首双义转义，新增 `^(\d+)\.` → `\1\\.`（仅块首，不涉软换行）；R 侧 `\.` 先占位 `\x18`、收尾还原 `.`，字面 `1.` 回到 `<p>` 内。全量重转 1,873 件。

**实测**：B3.1 **1,585（+16，转红 0）**（转绿 alyngton／arnauld／causation-law／economics／fallacies／fatalism／kaspi-joseph／learning-formal／mind-indian-buddhism／nonexistent-objects／rationality-historicist／reference／teleological-arguments／tibbon／toleration／transcendental-arguments）；池 **1,513（80.8%）／缺口 360／stale 0**，转池 27、失池 0，池占页 **39.50%**。

**教训**：行首结构义要在 C 侧全部枚举（标题 `#`、列表号 `N.`……），只做一半就是漏网；转义点用“反斜杠＋原字符”（`N\.`）而不是占位符，md 可读性与右逆可逆性兼得。

## 2026-11-22 B3.2 第十批：导航区逐字与书目定义表入账（池 1,513→1,529）

**缺陷一**：`toc_block` 账内逐字，但 `wrap_article` 把 toc 的 `<li>` 一并交 `wrap_html`——标签计入宽度使短项被折（`2.1\nValue-Feelings`），`split(" ")` 又坍掉 H0 双空格（`2.  Axiology`→`2. Axiology`），文字段错位致整页 `unaligned text units`（alain-locke）。修复：`wrap_article` 切出 `<div id="toc">…</div>` 不折（同 related-entries 处理，配平守卫防嵌套 div）；顺带 `wrap_html` 连续空格保真（H0 439 件正文有词间双空格）。

**缺陷二**：书目区缩写键块 `<dl class="sentag …"><dt>[AOP]</dt><dd>…</dd>` 被 C 折成散文段落，而 `scan_bib` 的 `BI_START` 不含 `<dl>`，`bib_seq` 无 dl 位，`_render_bib` 整块漏发（23 件全 gap）。修复：账新增 `bib_dl`（`attrs`＋`pairs: [[dt_pidx, dd_pidx, dt_attrs, dd_attrs]]`，纯整数与属性、**文字仍取自 md 段**）；`extract_bib_seq` 逐对按可见文等值在 References 散文序定位，空 `<dt> </dt>` 不占位（contract-law），配对不全回落散文序逐件发 `p`；`_render_bib` 按账发 `<dl>`/`<dt>`/`<dd>`。账重抽：变更 26 件，新增键只有 `bib_dl`。

**实测**：池 **1,529（81.6%）／缺口 344／stale 0**（上批 1,513/360）；转池 16（addams-jane／alain-locke／contract-law／japanese-philosophy／kant-conceptualism／kant-hume-morality／leibniz-evil／luxemburg／meister-eckhart／nietzsche-aesthetics／reid-ethics／rorty／scholem／srigupta／vasubandhu／wilhelm-wundt），失池 0；池占页 **39.65%**。B3.1 本批不动（只改 R/账）。

**残留族**：dd 内嵌 `<ol>`（heidegger）／书目区首段说明被丢（leibniz-exoteric）／书目区整节位置漂移（bruno）／交叉引用注 `see note 20`→空键 `[^note-]`（ratnakirti／boethius-dacia）／dl 文字折进脚注定义（leibniz-ethics／levinas）／字符漂移 `10−35` vs `10-35`（ibn-sina-natural，同步线）。

**教训**：文本处理器作用于整页时，任何“逐字”区间都必须整体退出处理链（否则破坏文字段对齐，代价是整页 gap）；列表结构在 C 侧一律降级为散文，还原信息必须入账，且账只记索引与属性、文字归 md；配对失败要回落不硬发。

## 2026-11-22 B3.2 第十一批：链接落位守卫组与账归一化转义（池 1,529→1,567）

**缺陷一**：散文链接与标题同文时被挂到 `<h2>` 上（bruno：`<h2><a href="#Oth">Other Internet Resources</a></h2>`），标题带标签致区段切分认不出 OIR，整节并进 main-text。修：标题行不消费链接（全库正文标题内 href 链接 0 件）。

**缺陷二／三**：短锚文（`1`）落进数学体 `$…=1$`（infinity）或列表标记 `1. `（trinity）；锚文跨度跨过强调闭星致 `<a>` 跨 `<em>`（infinity）。修：`_math_spans` 区间守卫、列表标记区间守卫、跨度内定界星**就地**扩展（不配平即弃候选，远处吞字禁止）；撤除锚文 `replace("*","\\*")` 旧法（字面星 C 侧已是 `\*`，旧法反把定界星打成字面星）。

**缺陷四**：`norm_md` 不还原反斜杠转义，C 的 `1\.`、`(\*)` 在可见文等值上全失配，书目 `dl` 配对回落散文（heidegger）。修：`\*` 先占位再还原，其余 `\x` 还原字面。

**实测**：池 **1,567（83.7%）／缺口 306／stale 0**，转池 38、失池 0，池占页 **41.00%**。首版守卫单独上线时全库 −2（infinity／trinity），按失池件逆向定位才见裸星与数学体两处真因——净值为正不等于无损。

## 2026-11-22 B3.2 第十二批：行首列表标记转义与书目引块位次账（B3.1 1,585→1,592／池 1,578）

**缺陷一**：H0 引块首行 `+ Mind is a congeries…` 的 `+` 成 md 无序列表标记（berkeley）。修：C `_escape_leading_hash` 增行首 `[-+] `→`\-`／`\+`，R `\x19`／`\x1a` 还原。

**缺陷二**：H0 `<a href="notes.html#">note 20</a>` 空片段生成空键 `[^note-]`（ratnakirti）。修：空片段按纯文字照录。

**缺陷三**：书目区内容引块两侧同丢——`BI_START` 不含 `<blockquote>`、R 的 References 区把区内所有 `>` 行当 C 注入固定注跳过（20 件有账）。修：账增 `bq` 位次（只记位次不记文字），R 抽 `_render_bq` 供主循环与 References 区共用，区内内容引块按位次发射。

**实测**：B3.1 **1,592（+7，转红 0）**（aquinas／hamann／hume-religion／justice-distributive／leibniz-mind／scheler／theophrastus）；受影响 21 件定点重建＋judge 拼接 → 池 **1,578（84.3%）／缺口 295／stale 0**，11 件 gap→pool、0 反退，池占页 **41.34%**。

**教训**：“跳过某类行”必须写明跳过谁（固定注精确前缀，而非区内所有 `>`）；同一渲染分支两处出现先抽函数；账记位次、文字归 md。

## 2026-11-22 B3.2 第十三批：书目区无年份散文落段（C 侧定案）

**缺陷**：书目区 `<p>` 散文（作者说明、引用约定等）与 li/dl 条目同流进 `build_cite_keys`，无年份者落到以首词为作者的 `-nd` 伪键定义（leibniz-exoteric 的键成了 `note-nd`、dilthey 成 `an-nd`）；账侧 `defs` 列表排除 `note-` 前缀（真脚注判据），R 的 `bib_defs` 同样排除——散文段两侧同丢，装配时整段消失（h0_extra 骨干）。

**修复**：C 侧 `p` 分支分流——书目区无四位年份的 `<p>` 直接落段（文字照录，不再进 `build_cite_keys`）；含年份者维持定义流（可能被正文引用）。`-nd` 伪键全库普查：877 件 3,194 条，正文引用数 **0**（无键语义损失风险）。

**样本试金石**：12 件重转＋4 对照，B3.1 0 退化（berkeley 顺带转绿）、池 2 件 gap→pool（leibniz-exoteric／berkeley）、0 反退；首测的 6 件假性反退是测试注入漏了 `bib_tree` 等字段（节点索引错位一格），重抽账后消失——**注入式测试必须带全 bib_* 字段**。

**全量重转**：1,873 件（md 变更 292 件）。连带修两处账侧缺陷：①`md_prose` 把书目区表格行计入散文序、R 侧 `ps` 只收 `<p>` 块 → 含表格件 `p` 索引越界静默跳过（anselm）；②`norm_md` 未剥脚注标记 `[^key]` → 带标记的书目散文 `pd` 定位失败（clauberg）。

**实测**：B3.1 **1,616（+27，转红 3）**；B3.2 池 **1,602（85.5%）／缺口 271／stale 0**，转池 24、失池 0，池占页 **42.00%**。转红 3 件（engels／foucault／kant-religion）＝书目区年份起首条目键名漂移，属 W8（R 重建书目单 ul 与 H0 分节邻接不同）。

## 2026-11-22 B3.2 第十四批：表题 caption 回带（池 1,602→1,615）

**缺陷**：R 已按 `***Table 1***` 紧贴表格的 md 形发 `<caption>`，但 `article_build.render_tables` 按结构账重建表格位形时只发 `<table>`＋行列，题注被丢（24 件 H0 含 caption、21 件 gap）。

**修复**：`render_tables` 从 R 侧表格块取回 `<caption>…</caption>` 原样带回（文字仍来自 md）。

**实测**：24 件定点重建＋judge 拼接 → 池 **1,615（86.2%）／缺口 258／stale 0**，转池 13、失池 0，池占页 42.43%。bayes-theorem 仍 gap：整表并入 28 KB u 补丁，`&nbsp;&nbsp;` 与 H0 `&nbsp;` 的计账在 `tx` 切片失配（自洽门拦下）。

**教训**：`re.sub` 重建整块前先问“原块里被丢弃的还有哪些”——账记位形、R 备忘其余，两者都要核。

## 2026-11-22 B3.2 第十五批：书目区标题与 R 同名项对齐（池 1,615→1,616）

**缺陷**：`_render_bib` 区标题恒取 `bib[0]`（“Bibliography”），H0 的 bibliograph div 首题未必同名（epistemology-latin-america 首题 `7. Religious Epistemology`）——预发标题与 seq 跳过的不是同一项。

**修复**：标题取 `bib_heads` 中与 R 同名项（记 `_skip_h`），seq 中该项及其之前标题一律跳过；div 边界差交池。

**影响面**（账普查）：1,869 件同名项在第 1 位（行为恒等）、1 件在第 2 位（转池）、2 件无 bib_heads（旧路径）。

**实测**：池 **1,616（86.3%）／缺口 257／stale 0**，池占页 42.45%。aristotle-ethics 余两处专项（`bib_heads` 抽取遇嵌套 div 早断；C 的 `in_bib` 按标题文本置位）。

## 2026-11-22 B3.2 第十六批：书目区取域同源与注释剔除（池 1,616→1,619）

**缺陷一**：`extract` 取 bib 区用 `(.*?)\n</div> ` 非贪婪正则，嵌套 div 早断（aristotle-ethics bib_heads 只剩 3 项）→ 一律改 `_bib_region`，账变更 18 件，aristotle-ethics 转池。
**缺陷二**：H0 书目区整条注释掉的 `<li>` 被账照收（C 已丢弃）→ `_bib_region` 剔除 `<!--…-->`，账变更 17 件，chimeras／jefferson 转池。
**实测**：池 **1,619（86.4%）／缺口 254／stale 0**，转池 4、失池 0，池占页 42.54%。**

## 2026-11-22 B3.2 第十七批：致谢区识别三轴（池 1,619→1,636）

**缺陷一**：`render_page` 认致谢区只按 `lv==3 and txt=="Acknowledgments"` 精确串；全库 741 个致谢头里 23 件不合（`Acknowledgements` 12／`Acknowledgment` 3／h2 级 5+3）→ 整节落进 main-text、发在正文末尾，u 键序整体错位（普查归入 h0_extra）。改前缀匹配 `^Acknowl`＋级别 h2/h3。
**缺陷二**：尾部区按固定次序 bib→acad→oth→rel→ack 发；H0 civil-disobedience 的致谢在书目之后、学术工具之前。改为按各区首块在 `rest` 的位次排序发射（md 序＝H0 序）；全库区序普查 1,872 件仅 2 件非 canonical。
**缺陷三**：致谢一律包 `<div id="acknowledgments">`、题恒 h3；H0 有 6 件无包层（fallacies／formalism-mathematics／logic-linear／natural-properties／scientific-revolutions／social-procedures）。账新增一位 `ack_div`，级别与锚形按 `hids` 取。
**账变更面**：全库重抽 747 件，**只有 `ack_div` 一个字段**变化，其余逐件逐值等。
**实测**：26 件定点重建（25 唯一）→ 池 **1,636（87.4%）／缺口 237／stale 0**，转池 17、失池 0，池占页 **43.12%**；check_all 17 项全绿。余 8 件已缩到单点（`>` 前缀泄漏、related 首位 `|` 等）。
**W8 定案**：接受残留不修——修法成本实测 1,580 条／121 件键名改判（或 19 件重置风险、或账补丁全量重算）换 3 件（0.16%）且仅键名标签，三件 B3.2 均 pool。

## 2026-11-22 B3.2 第十八批：related 前导竖线＋希腊宏四类闩死（池 1,636→1,659）

**缺陷一（related 前导竖线）**：H0 的 related `<p>` 有以 ` |` 起的三件（realism／feminist-science／friedrich-lange，md 原样保留），`_render_rel` 逐项发分隔符而首项前的前导竖线无人发。账增 `rel_lead`（变更恰 3 件一字段），渲染补回。
**缺陷二～四（希腊宏）**：①紧贴定界星的孤立希腊（`\(\omega\)<em>-liar</em>`、`*stit*\(\varphi\)`）旧出裸字符丢公式身份 → 改公式形 `\(\omega\)`；②`_mark_math_in_emph` 闭标签无回溯，跨型嵌套（`<em>…<i>G</i> …\(\varphi\)</em>`）在 `</i>` 早断 → 改 `</\1>`；③斜体内旧约定出裸字符（靠外层斜体覆盖渲染），B3.2 页缺公式形 → 一律公式形（md `*…\(\phi\)…*` ↔ H0 `<em>…\(\phi\)…</em>` 逐字符一致且右逆稳定）。
**\$ 双源不可分（回退登记）**：C 的 `\$` 与 H0 已有 `\$` 在 md 同形（dutch-book 18 裸 `$` vs decision-causal 17 `\$` 现池），一律反演会打坏后者 → 回退留注，正解需 `math_dollar` 逐 span 按位账。
**实测**：全量重转 md 变更 44 件（39 主件＋5 补件）；**B3.1 集合对照 1,616＝1,616，0 绿 0 红，净 0**（缺陷二首版曾在 logic-epistemic 引入 −1，缺陷三修复即归零）；41 件定点重建 → 池 **1,659（88.6%）／缺口 214／stale 0**，转池 19、失池 0，池占页 **44.13%**；check_all 17 项全绿。余 17 件仍 gap（`unaligned text units`；common-knowledge 为 `apply verify failed`）。
**教训**：“防误配”的裸字符约定须用右逆可证性检验——裸字符丢公式身份则 B3.2 必错，公式形两判据同时成立；正则闭标签无回溯＝嵌套一破全漏；不可反演的双源一律入账或登记。

## 2026-11-22 B3.2 第十九批：layout 陈年刷新＋嵌套引块渲染（池 1,661→1,685）

**缺陷一（layout 记录陈旧）**：页面壳（版权年/站点年/era 骨架号）来自 `baseline/en-template/page-layout.json`（H0 派生快照）；上游重发后未刷新即整页错。全库比对版权年与记录：仅 3 件不一致——modality-varieties（2021→2026，era 换代）、type-theory（2022→2026）、plato-ethics-shorter（记录 None，抽取报 `copyright-parse`，留待）。修法：`script/tmp/refresh_layout.py` 只抽指定 slug 并**合入**既有 JSON（保留其余 1,871 条），骨架新 key 补齐；重建 2 件均转池。
**缺陷二（嵌套引块 `> >`）**：md 的嵌套引块此前只剥一层、`>` 留成字面文字，u 键多出 `>` 整页错位——全库 31 件（29 gap／2 pool），是缺口最大单一机制。修法：`_render_bq` 按「嵌套行／普通行」切段递归渲染嵌套 `<blockquote>`（深度上限 4）。
**歧义判据**：H0 亦有正文以字面 `>` 起（`&gt;<em>Thoroughgoing…`），C 落 md 成 `> >*…`（标记后无空格）；嵌套标记恒为 `> > text`（有空格）——全库 82 有空格／11 无空格。故 `NEST_RE` 要求 `>` 后空白或行尾；首版 `^>\s?` 误吞 scientific-representation（B3.1 转红），收紧归位。
**实测**：31 件重建 → 池 **1,661→1,685（89.9%）／缺口 188／stale 0**，转池 25、失池 0，池占页 **44.98%**；余 5 件各含他病。**B3.1：31 件子集对照 +1 转绿（ceteris-paribus）0 转红，全库 1,616→1,617**；check_all 17 项全绿。
**教训**：布局记录是派生基线，上游重发后须定点刷新；md 的 `> >` 双源以“标记后空白”区分（与 `\$`、书目题后尾字同属 md 同形多源）；B3.1 止损可只跑受影响子集，前提是改动作用域能被结构谓词界死。

## 2026-11-22 B3.2 第二十批：书目散文 `note-<年>` 伪键归位（池 1,685→1,692）

**缺陷**：书目区顶层 `<p>` 散文含四位年份时 C 仍建条目键（首词＋年份 → `note-2005`／`note-1831` 伪键），而账 `defs` 与 R `bib_defs` 按 `note-` 前缀一律当脚注排除——该段既非书目定义也非脚注，`pd` 定位得 `null`，页面整段丢。全库 7 件全 gap。
**修法**：脚注判据改「`note-<id>` 且后缀不是四位年份」（账 `_is_note_key` 与 R `NOTEDEF_KEY_RE` 同判据）；伪键不改 C、不重转——账里有了定义，`pd` 即按可见文定位、原位发 `<p>`。
**判据取证**：全库 `[^note-…]` 键 176，非纯数字后缀 27（真脚注 sh 形），四位年份后缀恰 7；数字最大值 2024（本族之一）故不用号段而用年份词边界 `\b`（防 `note-2005-2` 冲突序号误判）。
**实测**：账重抽变更恰 7 件（bib_indices/seq/tree，vienna-circle 另涉 bib_ids）；7 件重建 → 池 **1,692（90.3%）／缺口 181／stale 0**，转池 7 失池 0，池占页 45.25%；**B3.1 +6（1,617→1,623，ibn-gabirol 仍红属他病）**；check_all 17 项全绿。
**教训**：“排除某类键”的判据须与产生方语义对齐（`note-` 前缀兼载真脚注与伪键）；同一判据在账与 R 两处必须同步；修 md 侧缺陷不必动 C——账能定位即可由 `pd` 原位发出。
### 加强复核事故记（2026-11-23，双通道复核首战即命中）

**现象**：全量 judge 复扫爆出 463 件 `stale`（r 段哈希失配），而拼接基线报 stale 0。
**取证**：①同机三进程装配同词条字节一致（排除进程间非确定性）；②并行会话提交未触及 053 基线（git 取证）；③失配件（abduction）的池建档停在第九、十批，而第十一～二十批的发射层改动（toc 不折/书目 dl/表题回带/区标题对齐/致谢三轴/嵌套引块/note 键判据）改变了未重建件的页面字节；④抽 5 件重建全部即回池——**池过期，非规则回归**。
**根因**：定点重建＋拼接的汇报口径有假象——「stale 0」继承的是**记录时的旧判**，不是当前状态的复测；每次发射层改动后未重建件的记录照抄，掩盖了池过期面的累积。
**修法**：全量重建池＋全量 judge 复扫为**收官基线**（唯一可信的全局数）；此后凡发射层（R/账/build）有改动的会话，收工前必须全量复扫或如实标注「N 件沿用旧记录未复扫」。
**双通道纪律（用户 2026-11-23 批准）**：拼接数与全量数不一致即回查——本次若只看拼接基线即漏过 463 件池过期。

## 2026-11-23 第二十一批：sup/sub 实体拼写与字形右逆（B3.1 +14／转池 +10）

**缺陷**：C 的 `_subsup_md` 跑在 `unescape` 之前，`<sup>&minus;</sup>` 落 md 为 `^{−}`；R 侧原样发裸 `<sup>−</sup>`，C 再见裸 `−` 即折成原生 `⁻` → B3.1 破（logic-connexive 首差）；页面侧亦与 H0 实体形不符。
**取证**：全库 H0 sup/sub 内文剥标签剥实体后**零裸非 ASCII**；实体拼写一字符一拼零歧义（60 字符）；`<sup>-</sup>`（ASCII 23）与 `<sup>&minus;</sup>`（76 页）由 md 形态可判（`⁻` 只来自 ASCII，`^{−}` 只来自实体）。
**修法（纯 R，不动 C、不重转）**：`SUPSUB_ENT` 60 字符表（只收非 ASCII，`&`/`<`/`>` 由入口转义负责，避免 `&amp;gt;` 双转义）；`_supsub_inner` 逐字符写实体形；`SUP_REV`/`SUB_REV` 同形多源取 ASCII 键。
**实测**：受影响 67 件（`affected_supsub.py`）→ **B3.1 +14 转绿／0 转红**；56 件可装配件重建 → **转池 10／失池 0**（池 1,696→1,706），既有 33 件池文件逐字节未变。
**教训**：实体形本身是「反演的抓手」——只要 H0 的拼写唯一，写实体形既保 B3.1 又保 B3.2；判据必须建立在**全库普查**上而非个案。

## 2026-11-23 第二十二批：apply verify failed 的跨岛实体差（9/9 转池）

**缺陷**：9 件补丁自洽门失败。①`ent_spans` 回传 a 侧位置却被当 b 坐标用（`&nbsp;&nbsp;` 对 `&nbsp;` 长度不等即漂移）；②实体差区间跨「文字岛」（`</b>&nbsp;</td> <td…>&nbsp;` 被 `plain()` 合并），整段 `after` 一次落地 → 第二个实体重复。
**修法**：`ent_spans` 改 `[b_pos, before, after, a_pos]` 四元组；`layout_items` 标记按当前文字岛裁剪落地（岛内 b 原文 ≡ plain 坐标）。
**实测**：9/9 通过自洽门并转池（`{'rule': 0, 'pool': 9, 'gap': 0}`，池占页 65.38%）。
**教训**：坐标系统一要在函数签名上显式化（a/b 两侧位置各归其位）；`plain()` 抹标签处即坐标边界，跨岛操作必须先裁岛；补丁自洽门是唯一可靠拦截点。

## 2026-11-23 第二十一/二十二批收官（双通道全量复扫）＋批准项①再分族

**双通道收官**：全量重建池 → `{'pool': 1715, 'gap': 158, 'stale': 0}`，池占页 **46.14%**；全量 judge 复扫同值 → **pool 1,715（91.56%）／gap 158／stale 0**；B3.1 全量 **1,637/1,873（87.4%）**。与定点拼接预期（1,696＋10＋9＝1,715；1,623＋14＝1,637）**逐项吻合**；`scan_vs_head.py` 显示 delta 只有 gap→pool 19 件、失池 0；重建后既有池文件逐字节未变（工作树零改动）。I2/I3 gate 0 issue；check_all 17 项全绿。
**批准项①（md_extra 再分族）**：分类器从「窗口标签」升级为「`plain()` 文字流首差 + 差异内容形态」（`fam_md_extra2.py`＋`classify_diff_content.py`）。109 件结果：数学定界/宏形 25（宏↔裸字形 ≈11、`&nbsp;` 填充 ≈6、引号/prime 实体 4、定界符形 1）／脚注引用形 12／管道格 raw 表被转义 10／空白实体 5／表管与标记 2／其余 55。族定义与判例已登记 §11。
**教训**：字节级首差会被折行差异劫持，分族必须走文字流；「窗口里有某标签」不等于该标签是缺陷承载者。

## 2026-11-23 第二十三批（math_dollars 按位账）与第二十四批（题后散字＋裸名条目）

**第二十三批**：行内公式 `\$` 双源（原文裸 `$` vs `\$` 在 md 同形）。账新增 `math_dollars`＝`[[体内指纹, "db…"]]`（`d` 裸 `$`／`b` `\$`），指纹按体内文字（`\$`/`$` 换哨兵后 sha1）锚定，避开 span 序号漂移。R 侧按指纹消费右逆，未命中原样。全账 14 件 71 条（`d` 31／`b` 40）；定点重建 **转池 3／失池 0**（dutch-book、proof-theory、rationality-normative-utility），`b` 类件池文件逐字节未变。
**第二十四批**：(a) 题后散字——H0 文献区标题与首个块之间的裸文字（3 件），账 `bib_heads` 第 4 位存原文片段、R 原样接题后；片段内链接从 `links` 账剔除防假 link_miss；块级边界须含 `</li>`、`<!--`（首版漏 `li` 吞掉 augustine／plato-ethics 列表）。(b) 裸名条目——删 C 的「纯人名即跳过」规则，照常建 `-nd` 键保定义行（无年份即无 pats，不挂文内标记）；爆炸半径经 C 内复算＝1 件 2 条（leibniz-ethics），只重转该件（md +4 行）。
**实测**：3 件中 2 件转池（boethius-dacia、gregory-rimini；hobbes-science 余折行宽度）；leibniz-ethics B3.1 ✓、B3.2 转池。
**双通道收官**：全量重建 → `{'pool': 1721, 'gap': 152, 'stale': 0}`，池占页 **46.32%**；全量 judge 同值 → **pool 1,721（91.87%）／gap 152／stale 0**；B3.1 全量 **1,637**（本批不改 B3.1 口径）。与定点预期（1,715＋3＋2＋1＝1,721）逐项吻合。
**教训**：①内容锚比序号账耐 C 侧丢弃/降级；②「不入 md 的原文片段」其内含链接须同步出账，两侧账必须成套；③保真优先级：文字是本体重名是辅助物，"免得残名而丢文字"是倒置。

## 2026-11-23 第二十五批：嵌套表与管道格内 raw 表（池 1,721→1,731）

**缺陷链**：①md 管道格内 C 存的 raw `<table>` 被 `_inline_md_to_html` 入口文本层转义成 `&lt;table`（B 侧文字流多出标签源码）；②该转义正则非贪婪取域，遇内层表早断，外层剩余半截也变文字（benjamin）；③账与 build 的表块取域同样非贪婪，嵌套表外层被记成乱序残形；④`&nbsp;`-only 格记 'd' 而 md 落空白 → R pool 与账 non-x 计数不等 → 整表回退。
**修法**：`table_spans`（深度配平＋**注释抹白保偏移**）与 `stash_nested` 账/build 共用；`render_tables` 顶层块迭代、内层原样还原；`_inline_md_to_html` 按 span 暂存 raw 表 + `_table_restore` 逆 `_sanitize_table_html`（`&#42;`/`&#124;`/`\\<`/img 前缀/`$…$`）；`&nbsp;`-only 记 'x'。
**插曲（重要）**：首版把 `table_spans` 的配平栈直接扫原文，被 `<!--pdf include <table …-->` 注释压高，paradox-simpson 的 7 表被读成顶层 2 → 该件由 pool 转 gap；注释抹白后账/asm/H0 三方表数一致（5/5/5），该件回归。另做过「退回全表计数」对照实验：只得 6 pool（含 paradox-simpson），劣于嵌套配平的 10+1，故定案配平。
**实测**：18 件（17 嵌套＋paradox-simpson）→ **转池 10／失池 0**；B3.1 子集 **+1（pm-notation）／0 转红**。全量双通道：**pool 1,731（92.4%）／gap 142／stale 0**，池占页 **46.62%**；B3.1 **1,638**；`scan_vs_head` delta 只有 gap→pool 10。
**教训**：嵌套取域必须深度配平且账/R 共用实现；HTML 注释里的标签污染配平栈（扫结构先抹白注释、保偏移）；`&nbsp;` 这类非文字字符的空位口径两侧必须同判；C 消毒过的原文还原须按逆序逐步撤销。

## 2026-11-23 第二十六批：脚注引用形与内部链接消歧（池 1,731→1,746）

**缺陷**：①`extract_note_forms` 只认 `<a href="notes.html#note-…">`，四类 H0 异形全漏（片段无 `note-` 前缀：`#complex` 显示 1、`#supplement-4` 显示 4；属性序 `name` 在前；`]`\n` </sup>` 有空白）；②md 对异形写作 `^{[[^note-N]]}`，R 仍发完整 sup 形 → 双层 sup；③`links` 账只记 text/href，锚文为数字时同文多处出现即抢位。
**修法**：note_forms 扫描放宽（任意属性序/片段前缀），规范形＝被 `<sup>[`…`]</sup>` 包住（容空白）且锚文＝片段去前缀；非规范形记完整替代片段；R 侧 `_bare` 只发锚（有账时），无账（B3.1 判官）仍发双层 sup 以保往返；`links` 增 `lead`＝锚文左侧最后两个词，R 优先按词选位、本行无匹配即 defer（消歧只对 ≤3 字符短锚文生效）。
**勘误（同日收口修订）**：首版 `lead` 用 14 字符上下文，中间态全量扫得 1,751；收口把两侧归一后才定案——账侧 `extract_links` 入口注释抹白（保偏移）＋剥 `\(…\)` 与 `[数字]`，R 侧 `_lead_ctx` 剥 `[^key]`／`$…$`／`[N]`／行首列表与引用记号，词表只认含 ASCII 字母的词。未做归一时短锚文会由一条卡死放大成整页饿死：plato-laws 58、connectives-logic 37、logic-algebraic-propositional 32（行首 `5. ` 记号／`\(\phi\)` 对 `*φ*` 降级）、implicature（可见脚注号 `[19]`）、findlay（注释残片 `1958 -->`）。另发现**幽灵链接**：注释内停用的 `<a>` 入账（正文区 9 条／4 页），提取时抹白注释即除。链接独立评测（`script/tmp/eval_links2.py`）lead 版未消费 1,815 条，摘 lead 对照 1,812 条（残差 implicature 2／publicity 1）。
**实测**：全量双通道 **pool 1,731→1,746（93.2%）／gap 142→127／stale 0**，池占页 **47.21%**，judge 与建池逐件同值；`scan_vs_head` delta 只有 gap→pool 15、**失池 0**；B3.1 **1,638 不变**（0 转绿 0 转红）；缺口普查 md_extra 84／h0_extra 13／math 12／text 9／star 4／digit 3／entity 2。
**判例**：chance-randomness 在“无 lead”时能 pool，但装配把 `#thm2` 的 `2` 误挂到跨文件链 `B.2` 上、被整段补丁掩盖；真缺口是带片段的裸兄弟链（`href="other.html#frag"`，73 页 514 条）未入账 → 第二十七批。
**教训**：①消歧判据必须能在“不可判”时退化为旧游标法，且退化路径两侧同式；②defer 语义会由一条卡死放大成整页，任何 filter 都要先查卡头风险；③注释里的停用标签是账的污染源，凡扫 HTML 先抹白注释保偏移；④字节等值 ≠ 位置正确——补丁池能吞掉错位，验证要看锚文落点。

## 2026-11-23 第二十七批：带片段的裸兄弟文件链（池 1,746→1,748）

**缺陷**：`extract_links` 只收 `../`（跨词条）与 `#`（页内锚）两族，H0 的 `href="other.html#frag"`（裸兄弟链）不入账，而 C 在 md 侧把这类链的片段整个丢弃（全库 md 侧 `.md#frag` 0 条），差异只能靠补丁池硬兜——正文区 73 页 514 条。
**修法**：账 href 放宽收 `^[A-Za-z0-9._-]+\.html#.+`（无片段的 616 条不收：md 已保 `slug.target.md`、R `_link` 可还原，收了双发）；R `_link` 增同形分支原样发。
**次生缺陷与护栏**：①`wrap_html` 词级折行会把新插入的锚从中间折断，H0 却整行不折（original-position 判例）→ 改**整锚不可折**（H0 正文 129,369 条锚仅 54 条内含换行，0.04%，实证口径）；②C 把 H0「锚文＋后随普通文字」合并成一条 md 链，账再插入即嵌进链接文字段、产出 `<a>` 内字面 `[..](..)`（H0 从不嵌套 `<a>`）→ 候选落在既有 md 链接文字段内即弃。
**实测**：无护栏首版全量 **+1／−1**（chance-randomness 转、original-position 失），净零不予采纳；加两护栏后全量双通道 **pool 1,746→1,748（93.3%）／gap 125／stale 0**，池占页 **47.27%**，judge 与建池逐件同值；delta＝gap→pool 2（chance-randomness、determinism-causal）、**失池 0**；B3.1 **1,638 不变**；随机抽 25 件原池页＋original-position 复测 27/27 可池。缺口普查刷新为 md_extra 83／h0_extra 13／math 11／text 9／star 4／digit 3／entity 2。
**教训**：①扩“可发锚”的账必须与折行、嵌套两条防线同批上，单上只把差异换个形态；②收益上界要按「受影响页中原为 gap 的件数」算（73 页仅 12 件原为 gap，其余 61 件已被池兜住），本批得 2 件符合该量级；③“池兜住”不是稳态，扩账会让旧池翻面，仍须全量复扫收官。

## 2026-11-23 第二十八批：宏 ↔ 裸字形之希腊-cursive 区（池 1,748→1,758）

**缺陷**：`_em` 的孤立希腊斜体判别字符类只写到 U+03B1–03C9，C 单希腊降级产出的 `ϱ`(U+03F1)、`ϑ`(U+03D1)、`ϖ`(U+03D6) 落在希腊-cursive 补充区，判别失败 → 右逆发 `<em>ϱ</em>` 而非 `\(\varrho\)`（qm-decoherence 判例：md `*ϱ*` 对 H0 `\(\varrho\)`）。`φ` 属主区不受影响，varphi 歧义另有按件 `greek` 宏序账。
**修法**：判别字符类扩到整块 `[\u0370-\u03FF]`（`GREEK_REV` 键集本就在此区）。一行 R 改动，C 侧零改。
**实测**：定点 10 件混合族 → 5 件即回池（其余 5 件另有显示式取域差）。全量双通道（建池 → judge 独立复扫 → B3.1）：**pool 1,748→1,758（93.9%）／gap 125→115／stale 0**，池占页 **47.63%**，judge 与建池逐件同值；delta＝gap→pool 10（qm-decoherence、time-travel-phys、ergodic-hierarchy、games-abstraction、logic-paraconsistent、connectives-logic、equivME、formal-belief、logic-games、rationality-normative-nonutility）、**失池 0**；B3.1 **1,638 不变**。缺口普查刷新为 md_extra 76／h0_extra 13／text 9／math 8／star 4／digit 3／entity 2。
**教训**：①字符类按 Unicode 块写，别手抄“希腊字母”范围（cursive 变体 03D0–03FF 最易漏）；②一行修复也要全量复扫——定点只见 5 件，全量带出 10 件（`ϖ`/`ϵ` 等同区受益）；③字形判别与 φ/varphi 歧义是两条通道，不合并修。

## 2026-11-23 第二十九批：账锚方括号保护（池 1,758→1,759）

**缺陷**：`restore_links` 插入 `[锚文](href)` 用原文切片，H0 部分锚文自带方括号（promises：`Problematic Promisees and the Uptake Condition (&sect;5.1]`，上游原文即以 `]` 收尾），裸 `[]` 使 `_link` 匹配失效，`[..](..)` 整段留在文字层。全库账锚含方括号 223 条／23 页（discourse-representation-theory 86、platonism 72、leibniz-exoteric 14…）。
**修法**：插入前把锚文 `[`/`]` 换 `\x06`/`\x07` 占位，`_link` 出口还原。
**实测**：全量双通道 **pool 1,758→1,759（93.9%）／gap 115→114／stale 0**，池占页 **47.64%**，judge 与建池逐件同值；delta＝gap→pool 1（promises）、**失池 0**；B3.1 **1,638 不变**。缺口普查刷新为 md_extra 75／h0_extra 13／text 9／math 8／star 4／digit 3／entity 2。另 4 件含方括号 gap 页余差为显示式取域/段数错位。
**教训**：①整段可池≠位置正确——18 件含方括号页此前全靠补丁吞差，规则修好后池字节略增但语义正确；②插入型账都要防锚文自带的语法字符（`[]`、`*`、`$`）；③收益上界仍按「原 gap 的受影响页」算（5 件 gap 修好 1 件）。

## 2026-11-23 第三十批：引块形态账 bq（前置件，池 1,759 不变）

**缺陷**：`_render_bq` 一律发 `<blockquote><p>…</p></blockquote>`，H0 另有 6,120 处裸装引块（首子非 `<p>`，798 页），每处多 4 段，整页 `_sub_diff` 对不齐（descriptions Δ109、desert Δ44、ambiguity Δ9）。
**修法**：账 `bq`＝文档序 0/1 序列（1＝裸装；首子 `<p>`/`<table>` 记 0），只记有裸装的 798 页；R `_render_bq` 按游标消费，裸装不套 `<p>`、行分隔用 `<br />`；切区同 `extract_links`。
**实测**：全量双通道 **pool 1,759／gap 114／stale 0（0 转池／0 失池）**，B3.1 **1,638 不变**。定性前置件：32 件 `m:<p | u:text` 首裂族推进到下一层（descriptions Δ109→3、ambiguity Δ9→5），段数相等的 gap 件 3→10。重聚类首裂签名：`u:<strong | m:<dt` 11、`u:text | m:</li` 10、`u:text | m:<p` 7、`m:<p | u:<span` 6 等。
**教训**：①按「首裂签名聚类」排队，不按族名清单排队——一个账只解一层，解完推进到下一层；②0 转池的前置件也值得上：扩大后续各族的可对齐面，且 B3.1 无账路径不动、失池风险为零。

## 2026-11-24 第三十一批：`_link` URL 白名单（池 1,759→1,760、B3.1 1,638→1,639）

**缺陷**：`_link` 对 md 一切 `[…](…)` 形态都当链接；但 md 链接 URL 是闭集（普查 25,679 条七形态），闭集外的 `](…)` 是上游记号的字面文本（ambiguity：H0 原文 `[∀x:Bachelor(…)](Unmarried(x,w))`），被吃成 `<a href="Unmarried(x,w)">` 坏锚。
**修法**：`_link` 入口白名单 `_MD_URL`（七形态），不匹配原样保留。
**插曲**：首版 `[a-z0-9-]+` 漏下划线（`spacetime-holearg.leibniz_equivalence.md`）→ 该件失池；普查 944 条 md 链字符集后放宽为 `[a-z0-9_-]+(\.[A-Za-z0-9_-]+)*\.md`，复测 24/24。
**实测**：全量双通道 **pool 1,760（94.0%）／gap 113／stale 0**，池占页 **47.68%**，judge 与建池逐件同值；delta＝gap→pool 1（ambiguity）、**失池 0**；B3.1 **1,639（+1）**。缺口普查刷新为 md_extra 74／h0_extra 13／text 9／math 8／star 4／digit 3／entity 2。
**逐件取证定调**：新探针 `script/tmp/greedy1.py`（模拟 `_sub_diff` 贪心延伸直击文字流永不衔接处）抽 9 件：剩余 gap 均为**真实内容差**（缺图注／C 列表标记丢失／dl 拍平标签错位／缺段／注号形残差），无批量机制族——下一步逐件取证定通道（C 侧保真 vs R 侧修复账）。
**教训**：①语法匹配必须配语义白名单；②白名单要先普查全部合法形态（下划线、大写段名易漏）；③首裂签名是表层裂点，真失败点用贪心延伸探针直取。
