# specs/015 交接卡（语体全局复核）

更新：2026-11-11（pc6）。进度只认 `results/verdicts.jsonl`，不认会话记忆。

## 已完成

* 规则与门禁：`rules/02` 语体与文风条款、`rules/04` 二校/r1 通读、ADR-0033、`check_academic` 的 `task-style-attest`（只查语义复核留痕）、`task_ops.py reopen`（done→pending）。
* 2026-11-10：J 批 12 条 done 全部语义通读（classical：jayaraasi、john-norris、johann-sturm；mixed：john-italos、jaina-philosophy；余 7 modern），5 条已置空。
* 2026-11-11：全库快速复核（用户指令「每个 .md 随机抽查 3 段，语义分析，同类条目置空」）。方法：每文件随机 3 段语义抽样 + `bin/register_metrics.py` 的真·之/的比与文言句式定位（剔除“之一/之后/之间”等现代固定搭配；**命中数不作判定依据**）。新判 23 条，入 `verdicts.jsonl`（累计 35 条）。

| verdict | 本轮词条 | 处置 |
| ---- | ---- | ---- |
| classical | intentionality-ancient、james-mill、israeli、early-modern-india | 置空（cleared） |
| mixed | africana、aesthetics-18th-german | 置空（cleared） |
| modern（保留） | buddha、davidson、legrand、confucius、korean-philosophy、natphil-ren、albalag、kukai、dai-zhen、knowledge-acquaindescrip、newton-philosophy、cudworth、luxemburg、peter-damian、peter-damian.supplement、telesio、gorampa | none（其中 davidson/legrand/dai-zhen/knowledge-acquaindescrip/gorampa 有个别文言句，列入定点改写） |

* 本轮 6 条置空均按 ADR-0033：`reopen` → `clear`，正文仅余 H1，任务状态 `cleared`，旧 steps 与账本保留为历史凭证。其中 james-mill、early-modern-india 原为 `s3_checked`（在途），按同一语义手工追记 `reopen` 步后回 `pending`，再经 `clear` 工具门置空。
* 判定分界（与 015 先例一致）：真·之/的 ≥0.35 或文言句式成段 → classical/mixed；<0.35 且主体句法为现代汉语 → modern（个别文言句按定点改写登记，不整篇回炉）。john-italos（0.53）判 mixed 的既有先例即此线的上端。

## 待办

1. `results/queue.jsonl` 现 391 条 done 词条（2026-11-13 重生成，done 计数随各批收口增长）。全量逐条通读按 done 时间升序推进，结论追加 `verdicts.jsonl`；判 classical/mixed 即 `reopen` + `clear`。
2. 通读口径：排除 `>` 引块中的直接引文、典籍原文、碑铭、题记原引文与参考文献照录区；判据是“当代中文学术读者能否自然读懂”，不按关键词命中数判定。
3. 破折号：`bin/dash_scan.py` 只排复核优先级；本轮 verdicts 的 `dash` 字段一律记 `pending`（破折号线未评），由 `dash-verdicts.jsonl` 另线推进。
4. 定点改写候选（不置空，待语体全量复核完成后统一处理）：davidson 一处文言收束句、legrand「危乎殆哉」、dai-zhen「欲两部分俱成全」句、knowledge-acquaindescrip 散见文言成分、gorampa「既已……便……」句。
5. 每批复核后重生成 queue 与 `PROGRESS.md`，跑 `check_all.py`，提交相关文件。

## 2026-11-13 软复核开工（用户裁定：全量逐条通读；只登记不处置）

* 用户裁定「软全局复核」= 覆盖不软、处置软：全量逐条通读照旧，但本轮**只写 verdicts＋证据句，不 reopen 不置空**，汇总后另行裁定处置。
* 首批 5 条（M 批 done，兼补 s2 语体留痕）：mandeville、marsilius-padua、model-organisms、moral-learning、music，全部判 `modern`（`dash=ok`），`action=none`；证据句见 `verdicts.jsonl`。s2 evidence 已按 ADR-0033 追补「语体：」结论，`check_all` 9 项复绿。
* 台账口径：`verdicts.jsonl` 累计 266 条（modern 255／classical 7／mixed 4；`israeli` 置空前后各记一条，故行数比唯一词条多 1）。按 done 时间升序推进，每 5 条一批提交；本轮（2026-11-13 起）已推进 211 条（第 1–43 批），全部判 modern。
* 已登记的非语体瑕疵（只登记不处置）：aesthetics-existentialist「小説」异体字、aesthetics-race「现像学／交又性」错字、anselm 论证编号重排、aesthetics-18th-french 标记残缺、dynamic-choice L175 成分残缺、identity-personal「个人同一性／人格同一性」术语并存、incompatibilism-theories 参考文献 L233 年份占位 YEAR、incommensurability 脚注键缺空格、intellectual-property 两节同编 4.4、ibn-ezra 照录区 Crirical、ibn-sina L77 星号嵌套错乱、integrity 参考文献标题未译且清单与正文节次不一致、kant-leibniz「necessitates」未译＋两处空参考文献标题、kant-mind「先验证成」疑误＋三处空标题、kochen-specker 与 kant-metaphysics 正文多处英文虚词残留（moreover/purported/again/somewhat/therefore 等）、kant-metaphysics 4.2 标题层级不一致、binarium 方括号年份引用与 *proporitionem* 拼写、kant-hume-morality 英文词夹入＋空 Secondary Sources、kant-reason 键名损坏 [^ów-1993]、kant-science「上图」指代悬空（图缺失）＋「三条标准」只列两条、kant-social-political 空 Secondary Sources＋多处正文引用未挂键标、kierkegaard 年表加粗斜体标记错乱＋「dedicated」英文夹入、knowledge-analysis「intended」夹入＋条件编号与正文引称脱节、knowledge-value「accrued／informing」夹入＋空 Works Cited、korean-buddhism「specifically／outlook」夹入＋大行「公→空」疑误、kumaarila「*Indra*ndash;」实体残件＋三空小节＋Kellner／Thompson 年份不符、aristotle-causality Broadie 1987 键目错配＋「PRactice／Phyiscs」拼写、timon-phlius 英文说明句未译＋年份一字线体例、condemnation 全文正文零键标＋四空小节、truth-coherence Candlish／Wright／Knight 三处年份不符、bauer 半角括号与英文括注通篇（see／Left-Hegelian 等）＋「AufklÄrung」拼写、hume-aesthetics 键标几乎全缺＋人名译名混用、bayle 行末英文注释全未译＋四空小节、analogy-medieval 正文引用零键标＋「Mittalters／Traditione」拼写、behaviorism L61 键挂错＋Stich 年份误（1998→1984）、bergson Soulez & Worms 2002 双键误挂＋「Chavalier／Suzaane／Annalles」拼写、olympiodorus「辛普里丘／辛普利修斯」两体＋Opsomer 正文 2011 而键 opsomer-2010＋「Olymiodorus／Twi／Kollegaus」拼写、scholem 正文两整段约二十种文献无键标＋`Kabbalah` 英文夹入＋原始文献区六个无名「**•**」标记、nicole-oresme 九处「XIV$^e$ siècle」LaTeX 残件＋相关词条 19 项半数保留英文倒序、environmental-aesthetics 十余处「英文原词＋中文括注」＋Hill & Daniel 2008／Hanich 2023 与键目年份不符、bayes-theorem「Brinbaum／Sphon／Scientiarium／Fascimile」拼写误＋`Halina 1988` 以名代姓（键 mortimer-1988）、imprecise-probabilities L5 缺字「要思想家」（重要）＋`$p(X) \gt 0.5$` LaTeX 残件＋图片替代文本英文未译、newton 文献表格 **[O] 缩写重复**（Opticks 与 Observations 同标）＋加粗斜体标点错乱＋`lumierè` 重音误、buridan 脚注区约二十处引用零键标＋专著参考节三节全空且条目堆于末节、erotic-art 正文引用零键标＋四十余处「英文原词＋中文括注」＋「柯林武德／科林伍德」「库珀／柯柏」两体、rationalism-early-modern 正文引用零键标＋索尔·胡安娜生年 1645／1648 两体＋Adams 1994 与 Morrison 2017 键目不符＋二十余个英文空小节、xenocrates 引号三层嵌套＋[^horky-2013]/[^horky-2013-2] 与 [^isnardi-2012]/[^isnardi-2012-2] 同文重复登记＋「卡尔克顿」（迦克墩）、holkot「Slotemaker and Witt 2015」八处双挂键（单篇论文＋合著书）＋七条 Quaestiones quodlibetales 各立一键、august-rehberg 照录区条目全部悬空＋「Blankburg／Ansalt／Bielenfels」拼写＋副署行加粗、representation-medieval **第 6 节排在第 5 节之前**＋Olivi 三译名并存＋brower-2008 页码 1937–243 疑误、henricus-regius「See also…」「Many of Regius' disputations…」两条英文残句无主＋文献区三节全空＋「Regius 1654」十余次作句首主语、necessary-sufficient 正文引 (i)–(xiii) 而列表全为 1./2. 编号全面脱节＋Nebel 2018 与 von Fintel 1998 键目年份不符、qt-entangle 正文仅两处挂键＋Herbst 2014／Al–Safi 2013 与键目年份不符＋NIST 新闻链接直入正文、simon-faversham 尾注引用零键标＋「拉杜尔夫／拉杜尔弗斯·布里托」两体＋donati-2003 出版项错乱、**peirce-benjamin 三子姓名脱落姓氏（James Mills Peirce 等）＋「Petersen 1955」键目误**、cordemoy「áction／Academie Français／Le Mettre／Occasinalismo」法文拼写误＋全文用弯单引号、reinach 文献区四小节英文全空＋[^von-nd]/1977/1984 把《Ästhetik》拆三条、intuitionism-ethics 引证约三分之二零键标＋U+2010 连字符密布＋prichard-1912 双 doi 并列、william-sherwood 编辑史叙述零键标＋图片路径指向 ../yuanwen/assets/＋「Tractactum」拼写、gersonides「阿弗罗狄西亚／阿芙罗蒂西亚」两体＋Goldstein 1988 与 North 1986 无对应条目、**penbygull 全篇正文零键标＋L23 整条文献嵌入正文＋夏普三名两体**、african-ethics 全篇零键标＋「Gbadegesin／Gbadagesin」两体、logic-relevance `\True`／`\False` 宏残件＋「Grishen／Routely」拼写＋十余条英文评价未译、logic-fuzzy「Nguyen & Walker 2000／Ross 2010／Goguen 1975」与键目年份不符＋`Łukasiewicz, Thomas` 编者名误、paradox-suspense 裸页码与零键标＋《Touching the Void》片名年份存疑、**langer 文献键五套前缀错位（`eugene-1951a` 实为 Langer 1951a 等）＋`langer-` 前缀指三人＋文献键当年份用**、la-forge「（Otegem, 2002: II, 485–536）」等四处引证未挂键（Garber 1987／Nadler 2010 之 Nadler 年份与 [^nadler-2011] 不符、Shapiro 未键）＋序言页码标记 `ã2`／`ù3` 疑为 à／û＋「## References（引用注释）」与三节文献小标题未译且全空＋照录区十处拼写／体例误（Pierre Claire 与 P. Clair 两体、Renates des Cartes、Radner, Dasie、certésien、出版项倒置等）＋相关词条 10 项以「|」分隔未链。


## 2026-11-13 改裁：先偿还后继续（全量偿还）

* 用户新指令「发现一个错误纠正一个，先偿还然后继续」取代上节「只登记不处置」：已登记瑕疵不再搁置，逐条核实修正。
* 两项裁定（AskUserQuestion，2026-11-13）：偿还范围＝**全量偿还**（含整篇脚注键悬空、空节重建、处理行重复合并、文献键前缀重构等大件，不只硬错）；留痕方式＝**台账追加修复记录**（`verdicts.jsonl` 只追加，不改原记录）。
* 修复记录格式：`{"kind":"repair","slug","path","fixed":[{ "where":"L12","issue","fix","basis":"en/…:L…"}…],"en":"en/<letter>/<slug>.md","at":ISO,"reviewer":"M2-015-soft-20261113"}`。判定原则不变：零信任，一律回 `en/` 核对后再改；原文如实缺键／本无该节者，不补齐、记为「原文无」。
* 统计口径：`Counter(r['verdict'])` 类批次计数一律先滤 `r.get('kind')!='repair'`；`queue.jsonl` 只认 verdict 记录。
* 偿还完成后自本卡「待办 1」的断点（第 43 批之后）继续逐条通读，此后边读边修，不再积压。

### 偿还流水（按台账顺序，逐条一提交）

| 词条 | 修项 | 提交 |
| ---- | ---- | ---- |
| advance-directives | 2 处英文残留（robust／otherwise）＋L49 句法残缺 | 540b5f0df |
| action | L333 英文残留 presumably | 92e60f3d8 |
| actualism-possibilism-ethics | 现实主义定义两处标记残缺、§2.4 强调符错乱、§4.2 *M*/M**、两处《拖延教授∗》、a fortiori 未译 | bd5702865 |
| abduction | L167 拉丁语 a fortiori 未译 | 65a3070c5 |
| al-khunaji | L40 两处斜体残缺、L223／L225 英文论题名未译、L262 阿语术语标记错乱 | d185ce435 |

其后各条不再逐行列表，**以 `verdicts.jsonl` 中 `kind=repair` 记录为准**（只追加，一条一词条；`fixed` 为改动、`verified` 为经核判不改）。截至 2026-11-14T05:10Z 已偿还 40 条、改动 66 处、经核不改 9 处；经核不改的典型：doxography-ancient（长句属文风）、aesthetics-critical-theory／aesthetics-of-everyday（同上）、identity-personal（通俗义与哲学术语有意分译）、independence-large-cardinals（译者译注）、integrity（五分法漏项系 SEP 源文疏漏）、aesthetic-concept（两名并存系原文并列）、incompatibilism-theories（YEAR 占位系 SEP 缺陷，已按正文补 2003）。

## 2026-11-14 源头修正：en 勘误＋转换器缺陷＋全量重转（ADR-0038）

* 偿还途中回 `en/` 核对，查实「正文零键标」这一大类主要不在译者：`tools/yuanwen.py` 的 `build_cite_keys` 匹配式「姓氏＋非逗号非括号 60 字内＋年份」卡死在逗号上，SEP 通行的「姓, 年份」式一格不命中。全库 1872 条中 124 条 `cite_markers=0` 而其 `cite_defs` 最高 262（african-ethics 34／analogy-medieval 75／althusser 126／arabic-islamic-metaphysics 262）。
* 已修：匹配式容许逗号（分号仍作边界），三条回归测试锁死（`tools/tests/test_yuanwen.py`）。
* 依 ADR-0038（用户裁定「en 就地改正＋重算哈希」）：`en/` 十六文件二十二处源头勘误（`YEAR`、`3s`、`Limmbo`、`511229`、`Einstein1949b`、`Shelby-Bigge`、`Birkaüser`、`Sijthooff`、`Pyschology`、`Complexiy`、`Cambridh=ge`、`die Alcmeone`、`Nazionnale`、`tradtion`、`Selgson`、`O'Neil`、`Lakatos1978a`、`Axelrod 198,`、Axelrod 两条并录等），逐条凭证见 `specs/001-sep-sync-pipeline/results/en-errata.md`；可争议年份（Mansfeld 2013、Scanlon/Nagel 1981、Alesina 1999、Hutcheson 1744）与 langer 键名前缀体系列为「待考不改」。
* 全量重转 `--all-baselined --summary`：1872 条零失败，`cite_markers` 145,251 → 161,312（+16,061），`cite_defs` 231,060 → 231,061（Axelrod 拆条＋1）；零挂键条目 124 → 98，其余 98 条多为「年份＋页码」无作者式的引称组或缺作者-年份括注（如 albert-saxony 按题名引称），属设计边界，需更强启发式，暂不强挂。
* 重转后自检：34 个补充材料文件的 `note-*` 悬空引用为**重转前既有**（binarium 26、burke 1 等），非本次回归。
* 影响：已译成品的「正文未挂键」不再是「原文没键」——偿还时以新版 `yuanwen` 为基准补挂；同一引证组挂多键时按文献表顺序追加，中文侧补挂须按句内顺序人工确认。

## 2026-11-14 续：转换器缺陷之八「姓 (年份)」式引称＋全量重转

* `build_cite_keys` 只在圆括号内找姓名，SEP 通行的「姓 (年份)」式（`Following van der Kuijp (1989)`、`as Skow (2008, 2011) argues`、`Lewis (1986: 220–247)`）整类永不命中：`cite_markers=0` 的 96 条中 55 条属此类（haecceitism 165 处、decision-causal 114 处、kant-metaphysics 75 处）。
* 修法：括号内容须为「年份／年份加页码」（`BARE_CITE_RE`）且姓名紧贴括号左侧（容许 `’s`）才挂键；括号内含散文或裸年份无邻名者不挂。四条回归测试锁死。
* 全量重转：1872 条零失败，`cite_markers` 161,312 → 203,188（+41,876），`cite_defs` 231,061 → 230,985（Rancière 键名改拼写后少 1 等）；零挂键条目 98 → 79，存量大改如 ordinary-objects 10→605、haecceitism 0→141、mereology 568→810。
* 试金石：haecceitism 0→141，抽查键标落点均为真引称。

### 偿还流水（2026-11-14 晚起）

| 词条 | 要点 | 提交 |
| ---- | ---- | ---- |
| emotion-Christian-tradition | Bash 2019→2020、Lazarus 1993→1991、Doubleday 倒置、Startle 缺逗号、schlechthinnig | dfe3c7d9c |
| epistemology-language-tibetan | 两条书目导引译出、双句号、三处拼写（en 同改） | f02220cc8 |
| arabic-islamic-mysticism | Sabziwārī 卒年 1797→1873、Nicholson 页码倒置、ḥikam 标音、Hunsberger 正名 | e3e5d51cb |
| equal-ed-opportunity | 「一等化」误译、Levinson 误挂键、书目页码 1137、机构名补全 | b90f41d7d |
| emilie-du-chatelet | 书目十余处拼写与编者标记、Hagengruber/Hutton 年份 2012、Nagel 题名冒号 | b5aa38262 |
| gelukpa | 引称中文化、Stages／lam gtso 转写、照录说明并条 | 742878aa5 |
| emerson | 双 H1 合并、junzi、[思]想、书目体例、56 条定义加空行 | 96f88454e |
| antonio-rosmini | 书目区重建（缩写表＋卷次嵌套）、theou dikē、十条→九条 | 877763ac7 |
| film | oeuvre／François／Noël、Kracauer／Rancière 键名、Badiou 书名 Cinema、Murray Smith | 051b73653 |

## 2026-11-15 续：转换器缺陷之九「年份起首文献条目」

* SEP 文献节惯例：小节「Works by X」之下条目只写年份（`1913, “On the constitution…”`）。旧建键式无姓可扫、直接丢弃整条，于是正文挂了键、文献表却无条目——bohr-correspondence 的「玻尔著作」13 条蒸发。全库 176 词条 2867 条。
* 修法：文献节小节标题随条目传入（`(text, section)`），`_section_author` 认「Works by X／X’s Works」取姓；节切换重置 `prev_surnames`。回归测试 3 条。
* 全量重转：1872 条零失败，`cite_markers` 203,188 → 204,835（+1,647），`cite_defs` 230,985 → 231,358（+373）。
* 偿还时注意：此类词条的中文书目往往整节缺失，须按 yuanwen 补全并分置小节（bohr-correspondence 已示范）。

## 注意

* 置空会改变 `PROGRESS.md` 的 done 计数与批次统计（生成物实时推导），不要手工回填。
* 旧账本（如 `tasks/j/jayaraasi.ledger.yaml`）仍在库内，仅作违规记录；重译时覆盖前先确认新建。
* 若并行会话正在写同一条目，先 `git status` 与 mtime 判落定再动。
* 抽样工具：`bin/register_metrics.py`（指标与证据句，`--json` 落 `script/tmp/register_metrics.json`）、`bin/review_cards.py`（复核卡）。二者只定位、不判级。
