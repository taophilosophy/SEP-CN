# 日志与编辑规划


> 本日志按 ADR-0004 分卷：卷一（2026-11-15 及以前）见 [日志卷一](ri-zhi-yu-bian-ji-gui-hua-1.md)，卷二（2026-11-16 至 11-20）见 [日志卷二](ri-zhi-yu-bian-ji-gui-hua-2.md)，卷三（2026-11-21）见 [日志卷三](ri-zhi-yu-bian-ji-gui-hua-3.md)；本页为卷四（2026-11-22 起）。

# 项目日志（卷四：2026-11-22 起）

## 2026-11-22 遗留问题处置（用户指令“解决遗留问题”，specs/055 收口）

* **误报改判与根因修复**：见上条改判注；`build_mapping.py` en_key 双规则（跳全角注记段＋作者段括号平衡截断）＋`bin/test_en_key.py` 九例回归全过；对 00ee29e44^ 重放全管线，mapping.tsv 仅 4 行 en_key 归正（kochen-specker/social-procedures/logic-provability/feminism-objectification），写回净增量 1 行移位，mulu-map 重建 G1–G4 全绿。
* **共用工作树 checkout 误收事故（登记）**：重放用 `git checkout 00ee29e44^ -- mu-lu-s.md` 污染暂存区，被并行会话 s25 提交（ca31f15d8）扫入，分支 mu-lu-s 一度回退、G3 变红；原子修复提交 6e701789b 恢复新结构＋mulu-map 同步，已推送复绿。防线登记：共用工作树禁按路径 checkout 旧版，重放一律临时 worktree；已补录并行危害记忆。
* **门禁分工**：本线 mulu_s 五项＋catalog-net G1–G4 全绿；`check_all` 仅 `管线单元测试` 一红——系并行会话 specs/053 线在途 `tools/yuanwen.py` 转换器改动（test_em_with_trailing_star_escaped），由其线收口，本线不越权。
* **PROGRESS 阻塞 2 件核实**（haecceitism/hamann 逐段对齐未配对）：属翻译战役待派工项（两件均为仅标题骨架、未开工），非清理类可解项，维持登记不动。
## 2026-11-22 阻塞清零与两条重译转入正常翻译频道（用户指令“解决阻塞，重译的进入正常翻译频道”）

* **事实**：PROGRESS 阻塞 2 件（haecceitism／hamann）即此前“待用户派工”的两条重译——ADR-0075 §5 跨机收编的截断中间态稿（EN 块配对仅 50/249、68/263），当时裁定“停 s0_source_checked 并 block，修复属后续批次”。
* **解除**：`task_ops advance --unblock` 两件（actor 主会话-20261122，证据引用户指令＋边界语义）；steps append-only 留史，ADR-0075 的“待派工”边界就此解除，两件沿 retranslate 状态机正常推进（现态 s0_source_checked，下一节点 drafted）。
* **频道语义**：旧稿为截断中间态，重译时整体置换，逐段对齐由 LQ 段落账本（specs/006）按 EN 块重建——无需对旧稿做对齐修复；blockers 为调度侧字段（ADR-0068，journal 未迁移），unblock 步不入 journal（与 block 同族跳过）。
* **计数**：PROGRESS 重生成——阻塞 2→0，在途 55→57，journal 分母 1197→1199，未开工 748 不变。
* **下步**：两件按正常频道排队待起草（与 748 未开工件同队列，无特殊派工边界）；拾起时按 ABCDE 全周期 SOP 走 drafted→…→done。
## 2026-11-22 上游巡检顺序门：目录差异先行，正文比较以目录干净为前置（用户指令“上游比较正文b123 ci应先调用目录差异比较ci，无问题再继续比较正文差异”）

* **落点**：`catalog-drift.yml`（每日三班 b1/b2/b3＝UTC 01/09/17，目录漂移与上游正文变更检测同工作流两段）——正文比较段（`detect_updates --archinfo --verify-web`，抓 new.html＋≤40 条 archinfo/index.html 核内容钉）原为 `if: always()` 无条件跟跑，现改为 `steps.drift.outputs.changed == 'false'` 显式干净才执行。
* **语义**：目录有漂移（changed=true）或抓取失败/结论不可得（changed 未设）→ 正文比较跳过（fail-closed），新增“正文比较跳过标记”step 打一行原因；issue 正文“上游变更待办”空值分支改“跳过（目录漂移未清，先落地目录同步，下轮巡检恢复）”，报告区无 queue.md 且漂移时注明跳过；理由＝目录未同步时正文比较基线失真（增删改名未落地，差集不可采）。
* **文档**：rules/05/ci-workflows.md 的 catalog-drift 行同步顺序门语义；YAML 解析验证通过，四态推演（干净/漂移/抓取失败/比较器崩溃）逐一核对。
* **门禁基线**：本线涉及面全绿；全库 17 项中 2 红（008 线在途台账超限、053 线 yuanwen.py 在途单测）均系并行会话工作面，与本改动无关。
## 2026-11-22 mu-lu-s 空壳骨架缺陷修复与大小类对照（用户指令“你变动了哪些大小类目录，列出来比较”）

* **缺陷披露**：用户索要大小类对照，对照脚本（compare_headings.py）反检出 00ee29e44 起 mu-lu-s.md 混入**旧四区空壳骨架 138 节**（世界哲学（欧洲以外）／科学哲学／哲学通论整树空标题＋西史内犹太哲学旧位等），与新六区 populated 树并存——build_mapping 旧标题路径整树播种缺陷所致；check_mulu_s（只验链接行）与 G3（自洽重放）均不拦，此前“结构正确”的汇报不成立，如实更正。
* **修复链**：①播种移除，纯父节改由条目路径祖先合成；②序键两连修——合成节点码点序乱序改“子树最小首现序”（文档序回归）、节注 setdefault 伪实节点改按“有无直接条目”判定；③根层显式 H1 序（前言/关于/西史/传统/形上认识论/价值理论/科学逻辑数学）；④check_mulu_s 增第 6 项**空节硬拦**（旧版基线 0 空节验证安全，rules/05/tools.md 同步）；⑤对照脚本补子树全枚举。
* **重放纪律**：旧版输入走 `git show > results/快照副本`＋build_mapping argv 传参（共用工作树 checkout 禁令执行）；write_mulus --apply 守恒 1883 进=出；check_mulu_s 六项全绿（空节 0）；mulu-map 重建 G1–G4 全绿；**保序审计**：26 个保留父节中 9 处子序差异恰为 NODE_ORDER 批准的重要性重排（古代希腊居首、康德黑格尔居前等），其余全数文档序保持。
* **对照结论**（heading-diff.txt 入库）：旧 250 节点 → 新 251 节点＝保留 112＋迁移 127＋撤销 11＋新设 12；撤销↔新设对应：世界哲学（欧洲以外）→哲学传统、科学哲学→科学、逻辑与数学、哲学通论→形而上学与认识论＋价值理论、伦理学解散四升三迁、语言哲学与逻辑学拆分、政治哲学→政治与社会哲学、女性主义哲学→性别种族性、物理/生物/认知/信息四学科改名。
## 2026-11-22 分类体系定案维持（用户指令“除了西方哲学史必须保留…先查询再问我”＋修订“西史允许内部分类修订”）

* **六源检索**：PhilPapers 七类（Arabic-Islamic 挂 Asian 内）／IEP 四轴（科学哲学挂 M&E、逻辑数学与伦理同域）／REP 主题·地区·时期·宗教四轴／LCC B 类（BC 逻辑·BH 美学·BJ 伦理·BL-BP 宗教独立）／人大复印 B1–B9（逻辑·美学·宗教·科技哲学独立）／大百科“史＋分支”二分。
* **四问裁定（全选推荐项）**：顶层维持六区（甲）；西史区名保留＋内部断代制维持；逻辑维持科学、逻辑与数学内；宗教哲学维持形上认识论内、传统区维持八区域平列；元哲学不增设（M&E Misc 13 条就近安放，PP 杂类两区本库不设）。
* **落点**：specs/055 spec §Assumptions 定案登记；mu-lu-s.md 零改动；现行体系经六源比对后维持原判。
## 2026-11-22 人名表 CJK 全量复核（用户指令“继续复核 summary 条目的中日韩人名，以及全量复核人名表整体”）

* **SUMMARY 条目侧**：SUMMARY 里以人名为条目名的中日韩条目共 12 个（孔子、老子、庄子、荀子、朱熹、王阳明、戴震、空海、西田几多郎、和辻哲郎、日常美学之斋藤百合子，及诸“见……”别名行），条目定名逐一与人名表译法对账一致；人名表→SUMMARY 无漂移。
* **CJK 行全量**：按籍属筛出中日韩台（含高丽）行 224 条逐行过目，并以既有凭证（韩国学典／Wikidata／GND／上游自带汉字）核底；源文回读确认 SEP 词条全文罗马化、不含汉字，汉字回译只能靠外部权威，无“原文对照”可走。
* **实体修复 8 行**（凭证 `specs/013-person-attribution/results/cjk-review-2026-11-22.tsv`）：Morrison, Robert 身份正列——首现实为 Isis 105（2014）论文作者 Robert G. Morrison（b. 1969，鲍登学院，伊斯兰天文学史；exa 凭证 uchicago doi／Bowdoin 官网页），原行误并 1782–1834 年来华传教士马礼逊（GND 119420953），改“保留英文＋美国／科学史＋1969–”（ADR-0022）；Ichikawa Kon 市川昆→市川崑（官方网页用字）；Huan Tan 生卒 fl. 2023→前43–28（SEP 原文 43 BCE–28 CE）；Liu Bei 0161–0223→161–223；Murasaki Shikibu 0978–1016→978–1016（零填充格式归一）；Bodhidharma 籍属 中国→印度（南天竺）／中国（来华僧）（SEP“an Indian monk”）；Paek Munbo 依据换源（撤不合格引用，改韩国学典 E0022117＋人物综合库）；Parreut, John 列位移正列并补首现。
* **机检复扫**：person_review_flags 全表 4,594 行——flagged 0（上一轮 2 项已修）、重复组 0、保留英文形 41；缺籍属／生卒 924 为既存欠账（668 缺两项／60 缺籍属／196 缺生卒）。
* **欠账清偿开线**：`person-missing.txt` 924 键的 GND（lobid）批量取证已在后台续跑（`gnd-raw-2026-11-20.jsonl` 逐键候选＋断点，礼貌间隔 5s）；判定器 `gnd_adjudicate.py` 已备（严谓词：Person 型＋同名严格＋生卒不矛盾，同名多候选一律降存疑；古人生卒纪元码不自动填），吸取 Huan Tan 误并教训，自动接受名单仍须人工过目后才写回。
## 2026-11-22 mu-lu-s 逐条目研判收官：1883 行全量台账、28 条 MOVE 落地（specs/056，用户指令“逐条目研判不计成本”）

* **台账**：b1–b11 十一批连续覆盖 seq 1–1883 无缺号；**KEEP 1855／MOVE 28／HOLD 0**，逐行含裁定＋依据＋凭证（题名自释／本地冻结摘要／Related Entries／010 PP 咨询锚；PP 区域冲突按 ADR-0048 判噪音不采信）。MOVE 集中于史区断代错挂（牛顿、波义耳挂莱布尼茨-沃尔夫；但丁挂文艺复兴）、概念条目错挂人物簇（实践理性挂康德、图式挂康德）、传统区人物误归（阇耶罗师挂耆那教、曷利沙挂专题）。
* **应用**：`bin/apply_moves.py` 逐条删除→重解析标题树→按（档，英文字题）定位插入；`enlightenment` 整簇搬运（嵌套子条 `progress` 随簇达成，其独立 MOVE 行幂等跳过）；守恒 1883 进=1883 出。
* **应用阶段反检**：①b1 台账 slug 笔误 2 处（`pseudo-dionysius`→`pseudo-dionysius-areopagite`、`james-of-viterbo`→`james-viterbo`），seq↔slug 全量对账后修正；②`skepticism` 由 KEEP 改判 MOVE——`skepticism-medieval` 迁出后“怀疑论”节成空壳（门禁第 [6] 项硬拦反检），总条自元认识论归位，一改两得。
* **门禁**：check_mulu_s 六项 0 硬错；catalog-net G1–G4 全绿（mulu-map 重建 rows=links=1883，G3 重放全等）；check_all 17 项全绿。
* **教训**：①台账入库前必须与文档序全量对账 seq↔slug，笔误到应用阶段才暴露则返工面更大；②应用器要原生支持簇搬运与幂等重放（嵌套成员单列 MOVE 行＝随簇达成，重放跳过而非报错）；③结构判定不重复实现——应用器自带“空节预警”因区间语义与门禁“整子树”语义不同漂移出 42 条误报，最终仍交权威门禁。
## 2026-11-22 概念属人物者归人物簇（specs/056 b12，用户指令“概念属于人物的应归类到人物，有问题读取原文”）

* **判定法（三路定向扫描）**：①`en/<slug>/index.html` 标题英文所有格（129 条命中）；②mu-lu-s 中文侧“某某的…”结构（57 条，交叉验证）；③“Person on/in X”模式（143 条，确认史区人物簇已完备）。广谱“标题含人物姓氏”（488 条）因单名误配过多、多为“X in 领域”正确形态，按“漏报好于误报”不采。
* **原文核实**：19 条候选逐条读 `en/` 首段，全部确属对应人物学说条目（如 Bolzano 条自指 “see the general entry on Bolzano”、Goodman 条首段点名 Nelson Goodman、newton-stm 首段即绝对时空奠基）。
* **落地（`results/adjudication-b12.tsv`，17 行／19 行移动）**：CLUS 同节簇化 14 条（wittgenstein ×3、lewis-metaphysics、al-farabi ×4、ibn-rushd、ibn-sina ×3、bolzano、mally）；MOVECLUS 跨节移簇 3 条（church 类型论→逻辑史簇、goodman 美学→分析语言哲学簇、newton-stm＋2 子条→史区牛顿簇）。新应用器 `bin/apply_clusters.py`：删块→定位母条→插簇末尾、统一缩进 2、守恒断言。
* **例外 KEEP**：人物条不在库（Butler／Adam Smith／Nozick／Croce／Beardsley／Shaaban Robert）与定理/悖论/问题类（Bell、Skolem、Curry、Fitch、Gödel、Molyneux、囚徒困境、Hilbert 纲领、Arrow）留学科节；`schema`／`practical-reason`／`dualism`／`personalism` 经原文复核确为通题，b1–b11 搬出裁定不变。
* **门禁**：守恒 1883；check_mulu_s 六项 0 硬错；G1–G4 全绿（mulu-map 重建）；check_all 17 项全绿。
* **教训**：簇化与移节是两种动作（缩进即归类），应用器须分开（b12 单列批次，b1–b11 覆盖校验排除之）；“属人物”判据只在标题层可机械判定（所有格/中文明示），内容层判据（学派/主义通题）必须回原文。
## 2026-11-22 mu-lu-s 几方互转检查（用户指令“mu-lu-s的几方互转，检查”）

* **检查器**：`specs/056/bin/check_mulus_interplay.py`（只读，可复跑）；报告 `results/interplay-check-2026-11-22.md`。几方＝mu-lu-s.md（正文）／baseline/mulu-map.json（归类账＋骨架）／SUMMARY.md（路径与文字源）／上游目录（G1–G2）。
* **I1 往返恒等**：磁盘账重放＝文件（逐字节）、现抽账重放＝文件、磁盘账＝现抽账（rows＋skeleton 全等）——三等式全真。
* **I2 账内一致**：1883 行、order 连续 0..1882、路径零重复、骨架锚合法且单调；indent 仅 0／2（1712 独立＋171 簇成员）。
* **I3 文字跟随**：账内文字 ≡ SUMMARY 文字（转义归一）0 不一致、路径 0 缺失。
* **I4 负向探针（判据有效性反证）**：text／indent／swap／skeleton／delete 五种单点微扰全部被重放捕获——G3 判据非空转。
* **结构不变量**：59 簇／171 成员，缩进成员无孤儿（向上必达 ind=0 母条）、无深度>2；跨字母目录簇成员 28 条属正常（概念随主题母条，如 protagoras→sophists）。
* **门禁**：G1–G4、check_mulu_s 六项、check_all 17 项全绿。
## 2026-11-22 EN 逆向装配第七批：图注定界修正（池 1,359→1,483，79.2%）

* **定位**：第六批后 514 件缺口族普查（star 204／md_extra 156／h0_extra 59／text 37／digit 34／math 19）。star 族主流是图注标签——H0 `<span class="figlabel">Figure 1:</span>`，C `figure_to_md` 注入的 `*Figure 1:*` 定界星被第六批的文本层全转义写成字面 `\*Figure 1:\*`（判例 action-perception／animal-social-cognition 等 204 件）。
* **修复**：注入点改占位符（`\x17N\x17`），块渲染后还原为真定界星；md 回到真 em，R 正常出 `<em>`，span 还原归格式层池。
* **实测**：B3.1 1,569 持平、集合级 0 退化；B3.2 建池 **1,483（79.2%）／缺口 390／stale 0**（+124 件），池占页 38.49%（T7 如实同报）。
* **教训**：改转换层语义（转义）时必须回扫同层的手工字符串注入点（`*%s*` 一类），否则旧注入被新语义当字面——本轮 204 件即此因。
## 2026-11-22 人名表缺项清偿：GND＋Wikidata 双通道（924 条欠账的可自动化边界）

* **口径**：924 行为“缺籍属或生卒”的存量。GND 规范档全查 924/924（`gnd_person_fetch.py`）；Wikidata 全查 924/924（`wd_person_fetch.py`，wbsearchentities＋wbgetentities，取 P569／P570／P27／P106），另对“Last, First”复合键 141 条以“First Last”回查（`wd_recheck2.py`，等值命中 45）。
* **判定谓词四级收紧**（`gnd_adjudicate.py`）：词集等值（非包含）→ 泛名闸（去冠词介词后显著词少于 2 判存疑）→ 职业闸（Missionar／Holzbildhauer／Drehbuchautor 等非哲学家职业）→ 仅规范名等值（婚姻名、异体名只判存疑）。收紧由三例同名误并逼出：An Hyang（朝鲜儒者安珦）配到现代编剧；Alan Macdonald 配到 Pritchard, Alan；Kratz／Lekebusch 配到 Gadamer 家属。
* **判定分布**：GND 接受 10／佐证 22／存疑 492／查无 400；Wikidata 接受 24／佐证 13／存疑 81（其余行非缺项队列或无等值候选）。双源交叉（GND∩WD 同起始年）仅 1 条，单源 32 条。
* **写回**（`apply_person_debt2.py` → `results/debt-fill-2026-11-22.tsv`，45 项）：生卒 9（双源一致 1＋GND 单源人工白名单 8）、籍属 1（P27 中文国名唯一）、佐证 35（不改值，只在依据列记标目）。缺项 924→922。另将 Wikidata 取回的繁体“法國”改简体 1 处。
* **门禁**：`person_review_flags.py` 复扫 flagged 0／重复 0；`check_terms` 退出 0；`check_all` 17 项全绿。
* **结论**：这条欠账**大部分无法由权威库自动清偿**——现代学者多无规范档，古人生卒本就无确证，同名污染又使单源不可直接写回。剩余 922 条只能逐条人工研究（回所属词条原文定人），自动化通道到此为止。
* **教训**：①同名误并的第一道闸必须是**词集等值**而非包含（Alan 包含于 Pritchard, Alan 即典型漏口）；②泛名闸与职业闸是必要的第二、三道，缺一则存疑池被污染；③单源接受一律走人工白名单并落盘复查，不凭临时判断直接写表。
## 2026-11-22 人名缺项再清：回读原文括注 41 条＋GND→Wikidata P227 桥 6 条（缺项 922→902）

* **通道甲（原文括注，零信任回源）**：按“首现”逐条读 en/<slug>/index.html，抽 “Name (生卒)” 紧括号式；只认含间隔号或带 c./d./b./fl. 标记者（单裸年几乎都是出版年，“Name (2005) … 111–120” 一类书目页码串占首版假阳性绝大多数）。逐条过目后写 35 条、弃 4（David／Hippo／Moses／Shakespeare 命中皆同名异人：Hartley 之子、Augustine of Hippo、《提本》之子、Schlegel 译事年代）。
* **正则修正**：助词分支 `\s+of\s+` 未接本体，导致 “Dietrich of Freiberg (…)”“Alexander of Aphrodisias (…)” 整串失配、退化为只抓末词；补上助词后本体落位，另放行 “1240/1250–1318/1320” 式斜杠年。第二批新增 6 条（Alexander of Aphrodisias fl. 约200／Dietrich 约1250–1310／Electress Sophie 1630–1714／Nicholas of Otranto –1235／Siger of Courtrai 约1280–1341／Zeno (of Citium) 前335–前263），弃 1（Solomon 命中的是 Ibn Gabirol）。合计 41 条，缺生卒 855→814（P227 批再降至 811）。
* **通道乙（P227 桥）**：GND 已按规范名等值锚定、惟规范档无年份的 121 键，以 haswbstatement:P227=<gndId> 反查 Wikidata，取同一实体生卒。准入四闸：恰一命中／精度不低于年／生卒不同值（剔除活跃期代理）／职业不涉可疑族。判定：接受 9／存疑 30／查无 82。
* **接受集逐条再核（本人履历与双向国别栏）**：Matthen（本人 CV“Born Bangalore, India on 2nd April, 1948… Citizen of Canada”）、Solère（IdRef 069192642：1960，法国，CNRS）、Melia（fr.wikipedia 1935／英国籍）、Forsythe（维基：美国实验经济学家）、Squatrito（1979，与其 LSE 履历 2001 年本科毕业相符）、Song Xing（宋钘 前370–前291）。拒 3：Batterman（Q89298775 记 1900，与本行所引当代物理哲学家不合，疑 GND 并档）、Meskin（ORCID 自动条目同挂 1950 与 1934）、Platek（描述 Canadian statistician，与递归论学者不符）。
* **写回**：生卒 6＋籍属 4（Matthen 加拿大（生于班加罗尔）／Solère 法国／Forsythe 美国／Melia 英国）。缺生卒 814→811，缺籍属 727→723；合并后缺生卒 808、缺籍属 720，任一缺 899。门禁 check_all 17 项全绿。
* **负结果（判为不可自动化）**：①“<国别形容词> philosopher <人名>”同位语全库仅 1 处可得（hegel 的 Klaus Hartmann），通道作废；②GND 等值多候选细分筛 116 键只出 18 条，逐看 10 条是泛名单词、其余职业明显不合，机械收窄不可采；③剩余 811 条中 92 条依据已注明“现代学者”（在世或当代，生卒本无），其余多为当代学者与无规范档的古代小人物。
* **教训**：①正则助词分支必须自带本体，否则整串退化为只抓末词；②单裸年、斜杠年、fl. 三种式样须分别判；③规范库并档会把错年份带进 P227 桥，故身份闸之外还必须看人的描述，接受集一律逐条过目。
## 2026-11-22 阿拉伯语人名全量重判（用户指令“有大量重名现象”）

* **队列**：两路口径取并集——结构路（mu-lu-s 伊斯兰哲学一节 39 篇条目首现）125 行＋词形路（al-／ibn／Abū／ʿAbd／Mullā 等阿语专名元素）209 行，并集 233 行；再以严格词形剔除梵巴日名误入，收窄为 **127 行**。碰撞扫描：同主译 1 组（且系梵名误入）、同词干 13 组、重复键 0、裸单名 64 行（其中阿语仅 5）。
* **四处同人重复登记，已合并**：①Dashtakī, Ghiyāt al-Dīn ≡ Dashtakī, Ghiyāth al-Dīn Manṣur（原文 medieval-philosophy 明言“the al-Dashtakīs, father and son (d. 1498, d. 1542)”，父 Ṣadr al-Dīn d.1498／子 Ghiyāth al-Dīn d.1541–42）；②al-Kirmānī ≡ Kirmānī, Ḥamīd al-Dīn；③Qummī, Saʿīd ≡ Qummī, Qāḍī Saʿīd；④al-Shīrāzī, Quṭb al-Dīn ≡ Shīrāzī, Quṭb al-Dīn（均 1236–1311）。另 Abd al-Latif ≡ ʿAbd al-Laṭīf al-Baghdādī（词汇表并网旧形）。
* **同一 nisba 两写，已统一**：朱尔加尼→朱尔贾尼；库特卜丁／古特布丁→库特布丁·设拉子（中文维基与金宜久《伊斯兰教辞典》均作库特布丁）；阿尔-法尔加尼→法尔加尼、阿尔-巴塔尼→巴塔尼（冠词不音译，与表内法拉比／比鲁尼同例）。
* **原文回读补生卒 15 条**（另撤回 1、改格式 1）：Fanārī –1430、Qayṣarī –1350、Nasafī –1300 前、Sabziwārī –1873、Zunūzī ʿAbdallāh –1841/42 与 ʿAlī –1889/1900、Dargazīnī –1133、Abū Ḥātim al-Rāzī –934、Sijistānī Abū Yaʿqub –971 后、al-Ṭabarī fl. 9 世纪（原文指名 ʿAlī ibn Sahl Rabban al-Ṭabarī）、Ibn Tibbon Moses fl. 1244–1283、Nūrī –1830/31、Ibn Daud c. 1110–1180、Dashtakī Ṣadr al-Dīn –1498、Iblīs 不适用。
* **同名陷阱两处**：①mysticism 句“Taftazānī (c. 1322–1390 CE) and Jurjānī (1097–1127 CE) went to India”，括注与句内蒙古期年代冲突，疑赛义德·谢里夫·朱尔贾尼（1340–1413）之讹——撤回上轮所填 fl. 1097–1127，改记存疑并注“译文该处须加译注”；②Mullā ʿAlī Nūrī 系伊斯法罕师（d. 1830–1），拒赴德黑兰，德黑兰学派创始者实为其徒 Zunūzī 之子 Āqā ʿAlī Mudarris（d. 1889）——表内 Nurī 与 Zunuzī 两代三行分立无误（Nūrī → ʿAbdallāh → ʿAlī）。
* **未采、留待人工**：Josef Ibn Haviva／Josef Ibn Shem Tov 原文无生卒（已在依据注明存缺）；籍属 25 行仍缺（原文少明言，nisba 只能推地域，按零信任不作推定填表）；ʿAbd al-Qāhir al-Jurjānī（d. 1078）与 Abū al-Ḥakam ʿAmr al-Kirmānī（d. 1066）原文有出现而表内无行，属“表未收”，非重名。
* **门禁**：行 4594→4589（合并 5 行）；重复键 0；check_all 17 项全绿。
* **教训**：①尼萨巴（nisba）族最易误判的不是两个人写重，而是一行同时罩着几个人——合并前必须回原文看“父／子”“师／徒”的代词链；②同一人名元素在表内两写（加尼／贾尼、布丁／卜丁）比错译更难发现，须按 nisba 归族比对；③原文括注本身也会讹（Jurjānī 1097–1127），照录即错，须与句内年代互校。
## 2026-11-22 缺项逐条研究（第五通道）：散文式生卒，命中率 0.4%

* **做法**：对剩余 795 条缺生卒行，全库 1,873 篇扫“Name … died／born／flourished (in) YEAR”一类非括号表述，逐条出证据后人工判读。
* **结果**：命中 6 键，可用 3 条——Dionysius of Chalcedon（fl. 约前320）、Euphantus of Olyntus（生年早于前349）、Panthoides（fl. 约前280–前275），皆 en/dialectical-school 原文；另 3 条（Francine／Helene／Johann Friedrich）系他人句中名字片段，弃。
* **判读**：五条通道至此穷尽——GND 全查（接受 10／佐证 22）、Wikidata 全查（24／13）、P227 桥（121 键取 6）、原文括注（1,873 篇取 41＋6）、散文式（795 键取 3）。**剩余 792 条缺生卒基本上不在 SEP 文本与规范库中**：多数为当代学者（生年未刊），少数为无规范档的古代小人物；继续只能逐人查专门文献，命中率仅百分之几。
* **门禁**：check_all 17 项全绿；缺生卒 795→792，缺籍属 720，任一缺 897。
## 2026-11-22 阿语人名籍属逐人查证（用户指令“结合原文分析，不要机械判断，联网查证”）

* **做法**：不以 nisba 机械推定。阿语子集 25 行缺籍属，逐行先回 en/ 原文取语境（查有无“Persian”“also from Rayy”“Saʿīd al-Qummi”一类明示），再按人物／学派查权威工具书（Encyclopaedia Iranica、EI2、TDV İslâm Ansiklopedisi、Oxford Encyclopedia、Encyclopaedia Judaica）。
* **结果**：22 行落定，另 2 行（Josef Ibn Haviva／Josef Ibn Shem Tov）经 Judaica 补证，仅 Jurjānī 一行仍空（其人本身存疑，见上一段）。籍属 720→696。
* **反例（机械推断必错）**：al-Dārimī 的 nisba 不是地名，而是 Tamīm 族 Dārim 支；据 TDV 实为锡吉斯坦人、居赫拉特。若照字面推作“达里姆（撒马尔罕一带）”即误。
* **原文先于工具书的三处**：①Abū Ḥātim al-Rāzī 原文“also from Rayy”直接给地；②ʿAzīz al-Dīn Nasafī 原文“Persian Sufi authors”直接给族属；③Saʿīd al-Qummi 原文自带地名。三者不必外查即定，工具书仅作复核。
* **两处生卒处置**：①Ghiyāth al-Dīn Dashtakī 1462–1542→**1462–1541**（原文 mulla-sadra 作 d. 948 AH/1541，Iranica 作 866–948/1462–1541；原值 1542 系 Wikidata，改从原文）；②Fanārī 保留 **–1430**（SEP），依据列注 TDV 作 1431，不擅改。
* **工具书冲突不折中**：Joseph ibn Shem Tov 卒年 Encyclopaedia Judaica 作 c. 1460、Wikipedia 作 1480，取前者入表，异说写进依据；Haviva 生卒（约 1340–1420 一说）因无权威确年，生卒留空只填籍属。
* **计数**：缺生卒 792→791，缺籍属 720→696，任一缺 897→876。门禁 17 项全绿。
## 2026-11-22 EN 逆向装配第八批：链接题注守卫与公式形态账（池 1,483→1,486）

* **缺陷一**：`links` 账把内文引用挂到题注标签上（belief-merging 判例：H0 的 `Table 1` 出现序 0,2,3,4,5,6 全在正文，第 1 次是题注 span）。先试“全局出现序＝账 nth”精确匹配——全库实测池 −9（1,483→1,474，失池 17 件），已回退；终法＝文档序游标＋题注跳过守卫。
* **缺陷二**：裸排显示环境多出定界符（C 的 `wrap_naked_envs` 包 `$$`，右逆一律发 `\[…\]`）。新增结构账 `math_forms`（文档序 `br`／`naked`，289 件有账），R 按游标还原。
* **实测**：池 **1,486（79.3%）／缺口 387／stale 0**；转池 4、失池 1；池占页 38.59%；B3.1 1,569 不变。
* **教训**：账里的精确序号≠更好的定位（账 nth 与 md 出现次数不等时全盘错位）；转换层为渲染加的包裹必须入账。
## 2026-11-22 巡检 issue 口径改为“只报目录漂移、干净即关”（用户裁定）

* **起因**：用户质疑 issue #52“无变化还发布”。实为目录四方全等、正文队列有 `culture-cogsci`／`delusion` 的 new.html 修订；旧条件是“漂移或队列非空”即开 issue，且同一队列逐班重复评论（无指纹去重；本地未落地则逐班复现）。
* **改动**：`catalog-drift.yml` 只在 `changed == 'true'` 开/更新 issue；`changed == 'false'` 时自动关闭打开中的 `sep-upstream-sync` issue；正文变更检测保留但只落工件，issue 不报条数、队列不参与开关。`sep-sync-broken` 留人工，不自动关。
* **同步**：`rules/05/ci-workflows.md` 工作流表、`specs/054` 执行记录各补一段。
## 2026-11-22 mu-lu-s 细分升级：三节拆分独立＋全库 164 节细分 511 子节（specs/057，用户指令“不要管规模能细分就细分。全盘复核所有条目。现象学、存在主义、诠释学需要拆分独立，内部也需要再划分”）

* **s1 三节拆分**：原“存在主义与诠释学”合并节解散 → 现象学运动／存在主义／诠释学三个独立 H3，各带 H4（共 17 个）。PP 取证：Phenomenology 子类＝Husserl/Heidegger/Henry…，Existentialism 子类＝Beauvoir*／Camus／Jaspers／Sartre，Hermeneutics 子类＝Gadamer／Ricoeur——三者均按人物/学派设子类，本地照此。
* **s2 全库细分**：`bin/inventory.py` 逐区盘点（有 ≥2 直接条目且无子节的节点共 165 个）→ 逐节设计映射 `results/s2-map-*.tsv` → `bin/apply_map.py` 应用。五区分批：史区 67 节/205 子节、传统区 25/86、形上认识论 28/83、价值理论 25/70、科学区 19/67；合计 164 节 511 子节。节点 249→780（H4 402、H5 155），链接行守恒 1883。
* **细分判据**：主题/学派/阶段互斥即分，不设规模门槛（单人 H4 允许，与 PP person 子类及“非理性主义”三人节先例一致）；人物簇母条独占其 H4（避免“#### 舍勒 ＋ * 舍勒”双重列名）；H4 内多人组再拆 H5；语义同质不可分者保持并说明。
* **应用器纪律**：现有条目集合必须与映射集合严格相等（不丢不增）、簇子条随母、节注保留、全局守恒断言；试金石为史区单区先行验证闭环后再放量。
* **门禁**：check_mulu_s 六项 0 硬错（空节 0）；G1–G4 全绿（mulu-map 重建）；check_all 17 项全绿。
* **教训**：①映射表为唯一事实源，slug 笔误由应用器“缺块”断言当场拦截（porngraphy→pornography 一例）；②“能细分就细分”的正确粒度是主题/学派级，而非每人都设子节（人物层级已由簇表达）；③大工程分区分批提交，每批独立过门禁，回滚面可控。
## 2026-11-22 巡检目录漂移结案：embodied-cognition 作者增补 Guy Dove

* **漂移**：contents.html 唯一差异＝`embodied-cognition` 作者 “Lawrence Shapiro and Shannon Spaulding”→“Lawrence Shapiro, Shannon Spaulding, and Guy Dove”；ADD/REMOVE/RENAME 全空。
* **落地**：今日快照 `20261122T021217Z` 经 `fetch_catalog --reparse` 重写 `baseline/catalog.json`；`summary_sync report` add 0／remove 0／mapped 1873；SUMMARY／mu-lu-s／H1 三处作者并列增补（H1 走 `check_summary --sync-headers`）；`mulu-map` 经 `--build-mulu` 跟随；`rebuild_catalog --build/--check` 逐字节全等（残差池仍 194）；`check_catalog_network --gate` G1–G4 全绿，本地漂移复算 `changed=false`。
* **顺带发现（门禁缺口）**：`yuanwen/SUMMARY.md` 镜像自 11-19 落地后即 stale（argument／gadamer／hedonism 作者、privacy-health 标题、日志分卷行均未跟随）；现有门禁只查 `SUMMARY-en.md`（G2），不查中文镜像。已用 `yuanwen.py --summary` 重生成，但该缺口尚无门禁覆盖。
* **教训**：作者变更没有专用 CLI，需手工改三处显示层并重建 `mulu-map`；镜像目录类派生物同样需要“生成器＋门禁”成对存在。
## 2026-11-22 缺项逐条研究：三条新通道与古代中世纪逐人查证

* **通道六（年份窗口）**：全库 1,873 篇取“人名 ±200 字内含年份”的窗口，命中 305 键／718 段；逐段判读后仅得 2 条可用——An Hyang（1243–1306，原文直给）与一条世纪式；其余绝大多数是书目页码／DOI。定为低精度通道，不再单独跑。
* **通道七（世纪式括注）**：2 条——Kaṇāda（2 世纪 CE，照源）、Joane Petrizi（12 世纪）。
* **通道八（断代标记式）**：姓名 20 词内须出现 died／fl.／flourished／active，且标记词后 60 字含年份；34 键命中，可采 7 条：Diodorus Cronus（–前284）、Euhemerus（fl. 约前300）、Eusebius（–约339）、Jaimini（fl. 约1千纪初）、Laozi（fl. 前6世纪，传统断代照源）、Richard Rufus（–约1260）、Alcmaeon（约前6世纪末–前5世纪初，原文自述学界分歧大）。精度明显高于窗口法。
* **逐人查证 17 人**（原文＋LC 规范档／IEP／TDV／Provisionalia／A Companion to Philosophy in the Middle Ages／New Catholic Encyclopedia）：安珦 1243–1306；阿莫尼俄斯 约435/445–517/526（SEP 自条首句）；Stephanus of Alexandria fl. 约580–约640；Numenius fl. 约150（LC“active approximately 150”）；Eudorus fl. 约前50–前25；Lucian 约125–约200；Diagoras fl. 前5世纪；Durandus 约1270/75–1334；Gerald Odonis 约1285–1349；Stephen Tempier –1279；John of Dacia fl. 约1280；Alphonsus Vargas –1366；Gundissalinus 约1110–1190后；Joscelin of Soissons –1152；Robert Halifax 约1300–1350后；Aristoteles 与 Artemidorus fl. 约前250（原文“can be dated around 250 BC”）。
* **判据留空**：Aëtius（作者身份与断代本身有争论）、Elias（SEP 专文即在讨论其人是否实有）、Hippo（同名数人未定）、Damon／Homer／Theocritus 等无权威确年者——宁可空着，不凭印象填。
* **计数**：缺生卒 792→765，缺籍属 696，任一缺 876→863。门禁 17 项全绿（中途 catalog-net 因并行会话重生成英文目录短暂转红，其收口后自愈；本轮两次提交均只带自己路径）。
## 2026-11-22 B3.2 第九、十批：字面编号转义、导航区逐字、书目定义表入账

* **第九批（C＋R）**：H0 手打字面编号段落（全库 224 处／35 件）在 md 行首被当有序列表，右逆发 `<ol>` 吞号。C 侧 `_escape_leading_hash` 新增 `^(\d+)\.`→`\1\\.`（块首，含引文块内 `2.0211` 类），R 侧 `\.` 占位还原；全量重转 1,873（yuanwen 变更 131 文件 691 行，全为转义）。B3.1 1,569→1,585（+16，转红 0）；池 1,486→1,513（转池 27、失池 0）。
* **第十批（R＋账）**：①`wrap_article` 不再折导航区 toc（账内逐字被折行器破坏：短项误折＋双空格坍缩，致整页 `unaligned text units`），并修 `wrap_html` 连续空格保真；②新增结构账 `bib_dl`（书目区 `<dl>` 缩写键块的 dt/dd→md 散文段索引＋标签属性，文字仍取自 md），`_render_bib` 按账还原 `<dl>/<dt>/<dd>`；账重抽变更 26 件。池 1,513→1,529（转池 16、失池 0），缺口 344。
* **残留族**（下批入口）：dd 内嵌 `<ol>`（heidegger）／书目区说明段被丢（leibniz-exoteric）／书目区整节位置漂移（bruno）／交叉引用注空键（ratnakirti、boethius-dacia）／dl 文字折进脚注定义（leibniz-ethics、levinas）／`10−35` 字符漂移（ibn-sina-natural，属同步线）。
* **教训**：文本处理器作用于整页时，“逐字”区间必须整体退出处理链；列表结构 C 侧一律降级为散文，右逆靠账记索引＋属性、文字归 md；配对失败回落不硬发。
## 2026-11-22 specs/057 s3：mu-lu-s 二次下钻 141 节／373 子节

* **动因**：s2 每区只下一层，仍有 348 个节点“直属条目≥2 且无子节”。用户指令“继续按细类分类”。
* **盘点口径修正**：mu-lu-s 条目一律缩进 0、层级靠标题表达，故归属须按“条目前最近标题”判；首版按缩进判把每个祖先节点重复计入（候选条目 6377 对实际 1883）。`bin/inventory_all.py` 修正后候选 348／1349；合出文件超 ADR-0004 门禁，改按区分档到 `results/s3-inventory/s3-inv-<区>.md`（文件名按区固定、生成前清旧档）。
* **管线升级**：新增 `bin/build_map.py`——设计 JSON（路径→子节→slug）→ TSV，写前断言“路径唯一命中／设计 slug 集等于现状直属母条集／无跨节重复”，把 slug 笔误从 apply 阶段提前到设计阶段；s3c–e 全走此管线，均一次通过。
* **五批**：史区 8 节／21 子节、传统区 11／22、形上认识论 44／129、价值理论 40／104、科学区 38／97；合计 141 节 373 子节，节点 780→1153（H4 476、H5 444、H6 10），链接守恒 1883。
* **判据收紧**：并列人物组不再下钻（拆单人子节即“#### 名字 ＋ * 名字”双重列名，违母条独占）；节点名已表达二分且条目序即分组序者不拆；单条成节仅限独立类目。剩余 503 节（3 条 178、2 条 297）逐节复核后判定为语义最细单位（并列主题／并列人物／成对分类），清单留档。
* **H6 落地**：H5 节点细分即 H6（史区毕达哥拉斯主义、学园怀疑主义、新柏拉图主义总论与先驱、笛卡尔学派四处）；check_mulu_s 与 mulu-map 重放均不假设层级上限，重放只存骨架标题行。
* **门禁**：每批 check_mulu_s 六项 0 硬错（空节 0）、G1–G4 全绿、check_all 17 项全绿；五批各自提交推送。
## 2026-11-22 生卒反查：表值回原文逐条比对，十二处订正、十三处上游笔误入勘误

* **方法**：已有生卒的 3,826 行回 `en/` 逐条比对同名括注（`script/tmp/audit_dates_vs_en.py`），得分歧 102 条；每条回原句核实体所指，产物 `specs/013-person-attribution/results/date-audit-2026-11-22.tsv`，逐条判定台账 `date-audit-2026-11-22-verdicts.tsv`。
* **表值订正 12 行**：Dong Zhongshu（源内两存，表留约前195–前104，依据注 han-dynasty 与另两条 179–104 BCE 两说）；Albo 1365→约1380（SEP 专条＋EJ＋NCE，GND 1365 为异说）；Bessarion 1408→1403（SEP 三处＋Britannica，GND 1408 为少数说）；Biel 1418→约1410；Kilwardby 1200→约1215（SEP 专条＋ODNB）；Porzio 1544→1554（SEP 源内矛盾，Treccani DBI 定卒于 1554-08-27）；Sebond c.1400→约1385；Samuel Ibn Tibbon 约1150–1230→约1165–1232（SEP 专条 tibbon）；Hartlib 约1600–1670→约1600–1662（GND 1670 系与同句 Comenius 混同）；Caterus 1657→约1590–1655（Verbeek／Wilson／Mori 三家＋SEP 正文）；Amo 1753→约1703–约1759（卒年无定说，1756/1758/1759 诸说并列）；Matsudaira 译名松平义悌→松平义建（Wikidata Q11530568 ja 标目松平義建，生卒 1800–1862；SEP 括注 1824–83 系 Walthall 1998 沿袭之误，属其子德川庆胜）。
* **同名异人一处**：Friedrich Bachmann 原填 GND 117534706（神学家 1860–1947），SEP scholz 条实为朔尔茨门下数学家（1909–1982，GND 117707481），已改生卒与籍属；中文件 scholz.md 本就作 1909—1982，可互证。
* **依据复核两行**：Nāgārjuna（twotruths-india 作 ca. 100 BCE–100 CE，专条与通行 c. 150–250）；Dietrich of Freiberg（专条 c. 1250–1310，albert-great 条作 1240/1250–1318/1320）。
* **上游笔误 13 处／12 人入勘误表 §11**：Comte 1898、Figo 1547、Morgan 1856、Cooper 1954、Clauberg 1655、Pufendorf 1684、Francke 1723（两词条）、Ailly 1330、Algarotti 1721、Gresham 1597、Fourier 1873、松平义建 1824–83。均逐条联网取证；题名内年份（suarez 书目 Caterus 1597–1641、bodin 论文题名 Gentili 1522–1608）判为文献原样，不入表。
* **在途译文勘误落地 5 件**（均 s2.4_termchecked）：natphil-ren、occasionalism（两处）、nicole-oresme、18thGerman-preKant、kokugaku-school——改正确读法并加句内译注，残余门（译注外错年）归零。
* **假分歧 27 条**：公元前记号跨括号 10、书目页码与通信年份等 17；学界异说 47 条（差多在 1–15 年，表值有据，不据单条括注改动）。
* **计数**：人名表 4,589 行；缺生卒 763、缺籍属 695、任一缺 861（本批为值订正与勘误，不增减缺项）。上一批九（Basil 约330–379／罗马帝国（卡帕多西亚·该撒利亚）；Godfrey of Fontaines 约1250–1306（或1309）／布拉班特（方丹））并入本次提交。
* **门禁**：`python tools/check_all.py` 17 项全绿。
## 2026-11-22 续：反查余项补齐三人，历史人物逐人查证六人

* **可补未补三人**（反查时见原文有据、表内缺项）：Alexinus –前264→约前339–前265（SEP dialectical-school c. 339–265，Dorandi 1999）；George Rust 卒于1670→约1628–1670（SEP henry-more 括注）；Francesco Vimercato 卒于1569→1512–1569（SEP natphil-ren 括注）。
* **历史人物六人**（逐人回原文核实体所指后联网查证）：Anne-Thérèse de Lambert 1647–1733／法国（巴黎）（IEP、BnF、Larousse；原文拼作 Anne-Thésèse，系 Thérèse 之误，原文列照录）；William Blount, Lord Mountjoy 约1478–1534／英国（德比郡·巴顿布卢特）（DNB）；Louis Bourguet 1678–1742／法国（尼姆；后归纳沙泰尔）（HLS、DSB）；Hendrik of Bergen 1449–1502／尼德兰（卑尔根 op Zoom）（nl 维基据 Contemporaries of Erasmus）；Sébastien Basson 约1573–（卒年不详）／法国（约 1573 生于梅斯一带，1625 离 Die 后无考）；Bernard of Arezzo fl. 1335–36／意大利（托斯卡纳）（SEP autrecourt 通信年代＋Courtenay 省籍考）。
* **判据留空**：Boston Crummell（仅知其十三岁被卖、成年获自由，生卒无考）；Apollonius Cronus（仅知为狄奥多罗斯之师、昔兰尼人，无确年）；狄奥多罗斯五女 Argeia、Artemisia 等（仅知为逻辑学家，无确年）；Akṣapāda（传说人物，原文只给《正理经》约 100 CE，不给其人年代）。宁可空着，不凭印象填。
* **计数**：缺生卒 763→757，缺籍属 695→690，任一缺 861→855。门禁 17 项全绿。
## 2026-11-22 续二：键形归一补捞，批五批六共回收十七人

* **键形归一补捞**（新通道）：缺生卒 750 键按去括注、逗号倒置、取末词等变体对全库括注再扫一遍（`script/tmp/variant_harvest.py`），得 52 命中；剔除页码、他人误配后回收 10 人——Gaozu (Han) 前256–前195（原文 “formerly Liu Bang, 256–195 BCE”）、Gedündrup（一世达赖）1391–1474、村田珠光 1423–1502、徐敬德 1489–1546、圆光 542–640、真谛 499–569、王符 82–167、矢野玄道 1823–1887、William Hamilton 1788–1856、Zygmunt Schmierer ?–1943。此前漏网主因是键形不一（如 “Emperor Wu of Han” 对 “Emperor Wu (Han)”）。
* **批五七人**：二程（程颢 1032–1085／程颐 1033–1107，中国大百科全书）；忠宣王 1275–1325（原文只给在位 1308–1313，籍属随之由在位年改正为高丽）；崔汉绮 1803–1879（原文直给）；William Crathorn fl. 1330s（SEP 专条）；查理一世 1600–1649、二世 1630–1685（英国国王）、五世 1500–1558（首现 erasmus 语境＝神圣罗马皇帝；nicole-oresme、newton 语境为法王查理五世 1338–1380，同形异人，必要时另立条目）。
* **假召回示例（不入表）**：Solomon 1021/2–57/8 系所罗门·伊本·盖比鲁勒；Philo 159/8–84/3 系拉里萨的斐洛；“Emperor Wu (Han) r. 502–549”系梁武帝；Aḥmad ibn al-Muʿtaṣim 条 833–842 系其父在位年，不可当生卒。
* **计数**：缺生卒 763→740，缺籍属 695→675，任一缺 861→838。
## 2026-11-22 续三：仅缺籍属行清账（批七—批九，四十七人）

* **批七（18 人）**：仅缺籍属行按“名从地名／原文自述／规范档”逐人补：Akalaṅka Bhaṭṭa（印度·耆那教天衣派，原文 Digambara Jaina）、Ammonius Hermeiou（埃及·亚历山大里亚）、Aristoteles 与 Artemidorus（古希腊，辩证学派）、Augustine（罗马帝国·塔加斯特）、Cicero（古罗马·阿尔皮努姆）、Dante（意大利·佛罗伦萨）、Dietrich of Freiberg（德国·弗莱堡）、Durandus（法国·圣普尔桑）、汉诺威选帝侯夫人索菲（德国·汉诺威，生于海牙）、Eudorus（古希腊·亚历山大里亚）、Euphantus（古希腊·奥林托斯）、Eusebius（罗马帝国·凯撒利亚）、Fichte（德国·拉梅瑙）、Furlanus（克里特，Quaestio 2015 证其为克里特出身的希腊-威尼斯人）、Gundissalinus（西班牙·托莱多）、Shaul Ashkenazi（克里特·干尼亚，Encyclopaedia Judaica）、Albrecht Becker-Freyseng（德国）。另将裸名 Cordemoy 行并入 Cordemoy, Géraud de（同一人，别名与首现并集，表行 4589→4588）。
* **批八（21 人）**：Joachim Lange（德国）、John of Dacia（丹麦）、Joscelin of Soissons（法国·苏瓦松）、Malliṣeṇa（印度·耆那教）、Miyahiro Sadao（日本）、Nicholas of Otranto（意大利）、Gerald Odonis（法国·诺曼底奥东）、Richard Rufus（英国·康沃尔）、Samantabhadra（印度·耆那教）、Shahrazurī（伊拉克·沙赫拉祖尔）、Siger of Courtrai（比利时·科特赖克）、Sotion（古希腊）、Stephanus of Alexandria（埃及）、Stephen Tempier（法国·奥尔良）、Tsuruya Ariyo（日本）、Vidyānanda（印度·耆那教）、John Winchelsey（英国·温切尔西）、季蒂昂的芝诺（塞浦路斯·基提翁）、Ṭabāṭabāʾī（伊朗·大不里士）、G.F. Stout（英国）、Girolamo Armellini（意大利·法恩扎；并据 Ereticopedia 补生卒约1470–约1550）。
* **批九（8 人）**：洪大容 1731–1783（原文直给）、贺茂在满 1706–1751（国学院大学《神道百科》：1706 生于京都、1751 卒于江户）、奇大升 1527–1572（四七论辩文献）、嘉曹杰 1364–1432（Treasury of Lives，生于卫藏）、Philip van Limborch 1633–1712（荷兰哲学辞典）、本都的赫拉克利德 约前390–约前310（LC 规范档据 OCD）、欧塞尔的朗贝尔 fl. 约1250（SEP 专条，身份三家未定）、Johann Froben 约1460–1527（Britannica：哈默尔堡生、巴塞尔卒）。
* **计数**（本线累计）：缺生卒 763→732，缺籍属 695→628，任一缺 861→790；表 4,588 行。剩余以当代引用作者为主（无公开生年），历史人物已基本清出。
## 2026-11-22 续四：批十九人，历史人物尾巴收口

* **批十（9 人）**：甘地 1869–1948（印度·波尔班达尔；印度政府纪念馆年表）；弗里德里希·艾伯特 1871–1925（德国·海德堡）；丰臣秀吉 1537–1598（日本；生月日无确证）；普鲁士国王弗里德里希一世（旧称弗里德里希三世）1657–1713（普鲁士·柯尼斯堡）；汉娜（牛顿之母）约1616–1679（英国·林肯郡；Wikipedia 作 circa 1616，非旧传 1610）；普伊的约翰 1270–1350（法国·摩泽尔普伊；1321-07-27 撤回）；居伊·特雷纳 约1260–1342（加尔默罗会总会长，Bio-Bib 档）；沙佩勒的戈斯温（比利时·列日，生卒无考）；阿勒的约翰（法国·巴黎，生卒无考）。
* **留空说明**：Menander I（King Milinda）断代有前165／前155 两说，未取；Holbach 本轮未及联网核实，暂留；Giles of Feno 籍属无考（原文只作 “possibly Giles of Feno”）。
* **计数**（本线累计）：缺生卒 763→725，缺籍属 695→620，任一缺 861→783。剩余基本为当代引用作者（无公开生年，不宜凭空填）与少数无确年的古人。
## 2026-11-22 续五：霍尔巴赫与腓特烈大帝补齐

* 霍尔巴赫 1723–1789（法国，生于普法尔茨埃德斯海姆；Wikipedia 与 Voltaire Foundation：1723-12-08 受洗、1789-01-21 卒于巴黎）；普鲁士弗里德里希二世（腓特烈大帝）1712–1786（柏林生、波茨坦卒；SEP 原文作 the crown prince (later Friedrich II)）。
* 计数：缺生卒 725→723，缺籍属 620→618，任一缺 783→781。King Milinda（弥兰陀王）断代前165／前155 两说未取，仍留空。
## 2026-11-22 目录五方同步：官方基线快照刷新＋G5 门禁

* **核查**：四方门 G1–G4 全绿，`catalog_drift --latest` 报 changed=false（目录差集全 0），`summary_sync report` add 0／remove 0／mapped 1873，en-SUMMARY 最新，中文镜像仅 `../` 前缀差。唯一失配：`rebuild_dir check` 用的 `.github/sep-baseline/official-snapshot.json` 自 11-15 后无生成器/门禁，停留在 11-14 快照，仍含上游已撤下的 privacy-medicine，误报缺镜像。
* **同步**：新增 `tools/sync_official_snapshot.py`（--check／--write，解析沿用旧周检脚本，护栏 main≥1800、alias≥600）；写回最新快照：main 1872→1873（+inquiry、+privacy-health、−privacy-medicine）、history 改名、6 处作者增补、alias 同步。`rebuild_dir check` 转为 0 缺镜像／1873。
* **防线**：`check_catalog_network` 四子门扩为五子门，G5 断言 official-snapshot ≡ 最新 contents 解析 ≡ catalog 账；负向探针转红、写回转绿。同族缺口（派生物无生成器/门禁）第二次，按 ADR-0039 升级。
* **门禁**：五子门全绿，check_all 17 项全绿。
## 2026-11-22 specs/057 s3g：史区时间序修正

* **缘起**：用户指出“早期希腊自然哲学不应该在最上面”。实查相反——`古代哲学` 下是“古典希腊哲学 → 早期希腊自然哲学”，时间倒置。
* **修正 7 处**：古代哲学（早期自然→古典→希腊化罗马→专题）、古典希腊（智者→苏格拉底→柏拉图→亚里士多德→小苏格拉底）、唯理论（笛卡尔→剑桥柏拉图→斯宾诺莎→莱布尼茨-沃尔夫）、经验论（培根霍布斯→洛克→贝克莱→休谟→常识学派→英国道德宗教）、德国古典（康德→费希特→谢林→黑格尔）、浪漫主义（维柯前置）、现象学（布伦塔诺学派前移，后接慕尼黑哥廷根→胡塞尔→经典→海德格尔→法国）。
* **工具**：`bin/reorder_blocks.py`（设计 JSON→父节唯一、子节集合严格相等、整块搬运含簇与深子节、守恒 1883）。首跑因标题名取到外层残留变量、7 块全成“人物”，集合断言当场拦下未落盘。
* **保留**：现代哲学 H3 仍是思潮群编排（非严格年代）；“罗马哲学与拜占庭”跨时段混合块待议。
* **门禁**：check_mulu_s 0；mulu-map 重建；五子门绿；check_all 17 项全绿。
## 2026-11-22 specs/057 s3h：现代区年代序＋罗马混合块拆分

* **现代哲学 H3 改年代序**：非理性主义（叔本华／克尔凯郭尔）→ 后黑格尔与马克思主义 → 功利主义 → 实证主义 → 新康德主义 → 英国观念论 → 实用主义 → 分析哲学 → 现象学 → 存在主义 → 诠释学（s1 链保留）→ 法兰克福学派 → 结构主义 → 后结构主义 → 解构 → 现代政治哲学。
* **“罗马哲学与拜占庭”拆分**：原 H4 无任何拜占庭条目（拜占庭已在中世纪区单列），名不副实。拆为“罗马共和国哲学”（西塞罗）与“罗马帝国学术与医学”（亚历山大、盖伦），嵌回希腊化序列：怀疑主义与新学园 → 罗马共和国 → 罗马帝国学术 → 新柏拉图主义。
* **工具**：`bin/split_rome.py`（原块 H5 集合断言＋零残留＋守恒 1883）。踩坑：原块 H5 顺序是“逍遥派评注”在前，硬编码有序断言首跑失败，改集合断言。
* **门禁**：check_mulu_s 0；mulu-map 重建 1883；五子门绿；check_all 17 项全绿。
## 2026-11-22 B3.2 第十一、十二批：链接落位守卫组与书目引块账

* **第十一批（R＋账）**：①标题行不消费链接（bruno：散文链接挂到 OIR 标题上致整节并进 main-text）；②链接不落数学体（infinity `$…=1$` 被吃）与有序列表标记（trinity `1. `）；③锚文跨强调闭星时就地扩展配平（不配平即弃，禁远处吞字），撤除锚文裸星转义旧法；④`norm_md` 还原 C 的转义（`1\.`、`(\*)`），书目 dl 配对恢复（heidegger）。池 1,529→1,567，转池 38、失池 0。
* **第十二批（C＋R＋账）**：①行首 `+ `／`- ` 转义（berkeley 引块首行）；②`notes.html#` 空片段按纯文字（ratnakirti 空键 `[^note-]`）；③书目区内容引块 `bq` 位次账＋`_render_bq` 抽出（20 件，berkeley 的 `[W]` 条目）。B3.1 1,585→1,592（+7，0 转红）；定点重建 21 件 → 池 1,578（84.3%）缺口 295。
* **教训**：净值为正不等于无损——首版守卫单独上线全库 −2（infinity／trinity），逐件定性才见裸星与数学体两处真因；“跳过某类行”必须按精确前缀写清跳过谁；渲染分支两处出现先抽函数。
## 2026-11-22 B3.2 第十三批：书目区无年份散文落段

* **缺陷**：书目区 `<p>` 散文与条目同流进建键，无年份者落成以首词为“作者”的 `-nd` 伪键定义（leibniz-exoteric 成 `note-nd`），账与 R 两侧都按 note- 前缀排除 → 装配整段消失（h0_extra 骨干）。
* **修复**：C 侧书目区无年份 `<p>` 直接落段（全量普查 `-nd` 伪键 877 件 3,194 条、正文引用 0），含年份者维持定义流；连带修 `md_prose` 表格行致 `p` 索引越界（anselm）与 `norm_md` 不剥脚注标记（clauberg）。
* **实测**：全量重转（md 变更 292 件）；B3.1 1,592→1,616（+27，转红 3）；池 1,578→1,602（85.5%）缺口 271，转池 24、失池 0。
* **残留**：B3.1 转红 3 件（engels／foucault／kant-religion）属 W8 键名漂移（R 重建书目并成单 ul 与 H0 分节邻接不同），正解＝按 `bib_groups` 分节重建 ul；md_extra 167 属同步线。
## 2026-11-22 B3.2 第十四批：表题 caption 回带

* **缺陷**：`article_build.render_tables` 按结构账重建表格时丢了 R 已生成的 `<caption>`——24 件 H0 含题注、21 件 gap（bayes-theorem 等）。
* **修复**：重建时从 R 侧表格块取回 `<caption>…</caption>` 原样带回。
* **实测**：24 件定点重建＋judge 拼接 → 池 1,602→1,615（86.2%）缺口 258，转池 13、失池 0；门禁 17 项全绿。
* **教训**：`re.sub` 重建整块前先问“原块里被丢弃的还有哪些”；账记位形、R 核其余。
## 2026-11-22 B3.2 第十五批：书目区标题对齐

* 区标题改取 `bib_heads` 与 R 同名项，seq 跳过该项及之前标题；影响面账普查 1,869 恒等／1 件转池／2 件旧路径，池 1,616（86.3%）缺口 257。
* aristotle-ethics 余两处专项：`bib_heads` 抽取遇嵌套 div 早断（应改 `_bib_region` 同源）；C 的 `in_bib` 按标题文本置位（应按 `div#bibliography`）。
## 2026-11-22 B3.2 第十六批：书目区取域同源与注释剔除

* bib 区取域统一 `_bib_region`（嵌套 div 早断致 bib_heads 缺项）；剔除 H0 注释掉的条目（C 已丢弃，账不得看见）。池 1,616→1,619（86.4%）缺口 254，转池 4 失池 0。
* 余族（habermas 的子树吞标题、hobbes-science／friedrich-lange／singular-terms-medieval 等分节题）待专项。
## 2026-11-22 specs/057 s3i：布伦塔诺单列为现象学前驱

* **缘起**：用户指出布伦塔诺本人不是现象学家，应作独立前驱放在现象学里。原结构“布伦塔诺学派与早期现象学／布伦塔诺／* 布伦塔诺”既混先驱与学派，又双重列名。
* **改法**：现象学运动内新增 H4“现象学前驱”，直接列布伦塔诺母条（含判断理论簇），置于总论之后；原 H4 保留斯图姆夫与马蒂／厄棱费尔与迈农／特瓦尔多夫斯基三个 H5。
* **依据**：布伦塔诺 1874《经验立场的心理学》的意向性主题为胡塞尔所承，但其本人属 19 世纪德国心理学—哲学，不属现象学运动。
* **工具**：`bin/split_brentano.py`（搬块、删同名 H5、母条唯一、无残留、守恒 1883）。
* **门禁**：check_mulu_s 0；mulu-map 重建 1883；五子门绿；check_all 17 项全绿。
## 2026-11-22 B3.2 第十七批：致谢区识别三轴

* 致谢区题此前只认 `Acknowledgments` 精确串且恒 h3＋固定包层；23 件拼写变体（Acknowledgements／Acknowledgment）或 h2 级、6 件 H0 无包层（fallacies 等）。改三轴：前缀匹配＋级别随 hids＋包层按账位 `ack_div`；区序改按 md 标题次序（全库仅 2 件非 canonical）。
* 账全库重抽 747 件变更恰只有 `ack_div` 一字段。26 件定点重建：池 1,619→1,636（87.4%）缺口 237，转池 17 失池 0，池占页 43.12%；门禁 17 项全绿。
* W8 键名漂移定案接受残留：取证 engels 22 条全漂移（R 单 ul 与 H0 分节邻接不同），修法成本 121 件键名改判换 3 件，不修。
## 2026-11-22 specs/057 s3j：布伦塔诺最终归位（描述心理学·现象学前驱）

* **用户裁定**：节名“描述心理学（现象学前驱）”，放到与现象学同级（H3）上面。
* **结构**：现代哲学下 分析哲学 → **描述心理学（现象学前驱）**（布伦塔诺母条＋判断理论簇）→ 现象学运动 → 存在主义…；现象学运动内不再有布伦塔诺节。
* **依据**：s3i 评估留档——SEP 称 forerunner 非成员；其自我定位为描述心理学（偶称 phenomenology）；PhilPapers 归 19 世纪奥地利哲学；Spiegelberg “not yet in the movement”。
* **工具**：`bin/promote_brentano.py`（H4 块升格 H3、插现象学运动前、母条唯一、旧节零残留、守恒 1883）。
* **门禁**：check_mulu_s 0；mulu-map 重建 1883；五子门绿；check_all 17 项全绿。
## 2026-11-22 B3.2 第十八批：related 前导竖线＋希腊宏四类闩死

* related 区的 H0 前导竖线（realism／feminist-science／friedrich-lange）入账一位 `rel_lead` 补发。
* 希腊宏两向收口：紧贴定界星与斜体内一律出公式形（`\(\omega\)` / `*…\(\phi\)…*`），`_mark_math_in_emph` 闭标签改回溯（跨型嵌套不再早断）；md 变更 44 件，B3.1 集合对照净 0（1,616 持平，0 绿 0 红）。
* 41 件定点重建：池 1,640→1,659（88.6%）缺口 214，转池 19 失池 0，池占页 44.13%；门禁 17 项全绿。
* `\$` 双源不可分（H0 裸 `$` 与 `\$` 在 md 同形）回退留注，待 `math_dollar` 逐 span 按位账专项。
## 2026-11-22 specs/057 s3l–s3m：B 类名实修正＋美学/语言哲学集中分组

* **用户裁定**：即使只有一条也应分类（撤销“单条类目不动”的保留）。
* **s3l（B 类）**：结构主义与符号学→结构主义与精神分析（实际只有拉康）；蒙田移入怀疑论与科学方法、原节改名女性人文主义；言论/结社自由移入自由强制宽容（新建 H5 表达自由）、自主权并入自主家长强制、删空的“自由与权利”；生命哲学与实证主义→早期影响与旁支；人格主义升 H3；宗教与科学去冗余 H4 层。工具 `bin/edit_ops.py`。
* **s3m（A1/A2）**：美学 18 条→总论与理论/美学史/跨学科三个 H3；语言哲学 22 条→真理理论/总论与专题两个 H3；艺术哲学、语义学、语用学原样保留在后。工具 `bin/group_direct.py`（只动直属条目、保留现有子节）。
* **门禁**：两批均 check_mulu_s 0、mulu-map 重建 1883、五子门绿、check_all 17 项全绿。
## 2026-11-22 specs/057 s3n–s3p：A 类剩余大节全部归类（34＋26＋48 条）

* **s3n**：形而上学 10 条→总论与解释/属性与立场；应用伦理学 11 条→生命伦理与动物/战争恐怖主义/商业财产慈善；社会科学哲学 13 条→社会选择/社会本体论/方法论与历史哲学。
* **s3o**：计算与信息哲学 26 条→计算理论/人工智能与认知/信息与逻辑/计算史与专题。
* **s3p**：物理科学哲学 48 条→量子力学与诠释（24）/统计物理（5）/时空与引力（7）/宇宙学（3）/专题与人物（9）。
* 现有子节（本体论等 6、社会伦理学等 3、教育哲学、技术哲学、化学哲学）原样保留在新区块之后；单条不豁免，全部归入细类。
* **门禁**：各批 check_mulu_s 0、mulu-map 重建 1883、五子门绿、check_all 17 项全绿。
## 2026-11-22 specs/057 s3q：最后一条单条归位，H2 直属条目清零

* 逻辑学与逻辑哲学 H2 的最后 1 条直属条目“图式 Schema”移入“经典逻辑与传统逻辑／经典逻辑总论”。
* 至此全库 **H2 直属条目 = 0**：每个条目都处在至少两层细类之下（H1→H2→H3/H4…），节点 1175，守恒 1883。
* 门禁：check_mulu_s 0、mulu-map 重建、五子门绿、check_all 17 项全绿。
## 2026-11-22 B3.2 第十九批：layout 陈年刷新＋嵌套引块渲染

* 页面壳记录（版权年/站点年/era 骨架）来自 page-layout.json 派生快照；全库比对只有 3 件陈旧，定点刷新 2 件（modality-varieties、type-theory）即转池。plato-ethics-shorter 抽取报 `copyright-parse`，留待。
* 嵌套引块（md `> >`）此前只剥一层、`>` 留字面，全库 31 件（29 gap）是缺口最大单一机制；`_render_bq` 改递归渲染嵌套 `<blockquote>`，歧义判据＝标记后是否有空白（82/11）。31 件重建：池 1,661→1,685（89.9%）缺口 188，转池 25 失池 0，池占页 44.98%；B3.1 子集对照 +1 转绿 0 转红（1,616→1,617）；门禁 17 项全绿。
## 2026-11-22 B3.2 第二十批：书目散文 note-<年> 伪键归位

* 书目区散文含年份时 C 建 `note-2005` 类伪键，账/R 按 `note-` 前缀当脚注排除 → `pd` 定位 null、整段丢；判据改“后缀非四位年份”，7 件全转池。
* 账重抽只动 7 件 bib_*；池 1,685→1,692（90.3%）缺口 181，池占页 45.25%；B3.1 +6（1,617→1,623）；门禁 17 项全绿。
## 2026-11-22 specs/057 s3r–s3s：主题型节点第三层下钻

* **s3r（12 节→35 子节）**：量子力学与诠释 24 拆基础/诠释/量子信息/场论引力/量子意识；真理理论 11 拆实质理论/紧缩多元/形式修正；语言哲学总论 11 拆逻辑形式/命题/意义规则；AI 9、物理专题 9、美学总论 8、时空 7、跨学科美学 6、计算理论 6、信息逻辑 6、统计物理 5、计算史 5 同批二分或三分。
* **s3s（18 节→36 子节）**：名含“A 与 B”的节点按两类拆开（形上本体论六组、美学史/跨学科、AI 两组、物理两组、社科方法论与历史）。
* **边界**：人物并列组不拆（双重列名属结构禁令）；剩余 ≥3 条节点 223 个（H5 103/H4 112/H3 8）主体为人物组与同族理论并列，已到语义最细。
* **顺带**：修并行会话已提交日志里的直角引号 2 处（check_quotes 转红），改弯引号恢复全绿。
* **门禁**：check_mulu_s 0、mulu-map 重建 1883、五子门绿、check_all 17 项全绿；节点 1244。
## 2026-11-23 specs/057 s3t：全部复核与批准

* **独立复算**：s3a–s3s 共 16 个结构提交逐批链接重算均为 1883（16/16）；纯移动批 s3g 120/120、s3h 341/339 ±行相等。全局：重复路径 0、SUMMARY 双向差仅 5 个站点页（预期）、条目深度 H1 10/H3 63/H4 775/H5 987/H6 48、H2 直属条目 0。
* **抽样判读**：20 组整子树（描述心理学、人格主义、结构主义与精神分析、女性人文主义、怀疑论与科学方法、罗马两节、早期影响与旁支、表达自由、立场、模糊性、宗教与科学、18 世纪美学、量子力学诠释、AI 论证、文化演化与历史、经典逻辑总论等）归类全部正确。
* **结论：批准**。改判表无改判项；回退链 state/mulus-before-s3*.md。证据三件套与逐批表见 specs/057 results/s3t-final-review.md。
* **门禁**：check_mulu_s 0、五子门 G1–G5 绿、check_all 17 项全绿。
## 2026-11-23 specs/057 s3u：目录行逐条审计（翻译／分类／格式）

* **工具**：`bin/audit_catalog_lines.py`（A 格式形态、B1 作者对照 catalog、B2 英文题名对照 entries.json 钉、D 全量清单按区分档 s3u-review/）。
* **格式**：38 条异常全部为解析器误报或预期形态（站点页、`\[别名\]` 转义、题名内括号、罗马字长音、内嵌括号作者），无真实缺陷；行文字与 SUMMARY 逐字一致（G3）。
* **翻译**：作者漂移 2 条已修（saadya Pessin→Hegedus、closure-epistemic Luper→Alspector-Kelly；SUMMARY/mu-lu-s/词条 H1 三处同步，en-SUMMARY 重生成）；英文题名 69 条低重合全部为倒装题名的既定展开，与 entries.json 逐一吻合，非缺陷。
* **分类**：全量清单 1712 条逐条通读，修正 4 条错位（schema→连接词演绎、counterfactuals→非经典专题、reism→逻辑史学派、wesley-salmon→科学解释）；wilson（John Cook Wilson）核实维持；其余 1708 条正确。
* **门禁**：check_mulu_s 0、mulu-map 重建 1883、五子门绿、check_all 17 项全绿；审计文件按 ADR-0004 分档。
## 2026-11-23 加强复核：双通道首战命中 463 件池过期（收官基线 pool 1,696/45.43%）

* 用户裁定“全部批准。加强复核”：第十七～二十批与 §11 五项入口获批；复核升级双通道（拼接数须全量复扫确认）。
* 复核矩阵：B3.1 全量复扫 1,623＝基线逐件一致；B3.2 全量复扫初扫爆 463 件 stale——取证排除非确定性与并行干扰，定位为“池建档停在第九、十批，后续发射层改动改变未重建件页面字节”，抽 5 件重建全部回池，定性池过期非规则回归。
* 修法：全量重建池＋全量 judge 复扫收官——**pool 1,696（90.5%）／gap 177／stale 0／池占页 45.43%，失池 0**；另 4 件拼接误记 gap 实为 pool（记录双向陈旧）。抽样 25 件独立验证全过；I2/I3 0 issue；check_all 17 绿；账/layout --check 过。
* 教训：拼接的 stale 0 是旧判继承非当前复测；全局数字必须全量复扫为准，收工口径改为“全量复扫收官或如实标注未复扫面”。

## 2026-11-25 specs/060 六轴工序试金石名单固定（长度与格式复杂度全库扫描）

* **扫描**：`bin/entry_scale_scan.py` → `results/entry-scale-scan.json`（1,881 词条；长度按字符／汉字／正文汉字，复杂度按 14 类构件对数加权）。冠军：长度 `h/habermas`（105,946 字符／37,025 汉字），格式复杂度 `l/logic-preference`（18 公式块＋17 LaTeX 环境＋362 行内公式），构件多样性 `i/imprecise-probabilities`（12/14 类）。
* **裁定**：用户指令“将以上几篇优先列为试金石条目……将政策固定下来”。§5.4 由抽象三件制改为固定名单：第一梯队 `habermas`／`logic-preference`／`environmental-aesthetics`；第二梯队 `imprecise-probabilities`／`action`／`axiom-choice`／`newton-principia`；第三梯队单项极值观察件 `logic-dynamic`／`japanese-aesthetics`／`kokugaku-school`／`digital-art`。名录增删须用户裁定并在 §5.4 留痕。
* **计量轴**：原“计量密集件”为预设，全库实测无天然密集件（无歧义单位串最高 14 处，`i/intrinsic-extrinsic`），q5 判据改在第一梯队三件上同验，存量面走 `measure_audit`。
* **门禁**：check_doc_size OK、check_junk 0 命中、check_quotes 0 违例；check_all 结果见提交前复跑。

## 2026-11-25 节点标识三层落地（ADR-0080）：复核计算否证“100% 重放”

* **批准**：用户“B1/2 复核计算后全部批准”。先计算后落地：`tools/replay_state.py` 对 1,200 条任务严格重放，吻合 803——376 条为回补 pass 不迁移状态（ADR-0075）、16 条 `cleared` 不是事件、3 条缺 pass、2 条无 journal。原评估案的“重放 100%”前提被实测否证，验收改为**映射双档**（迁移后逐条 new==aliases[old]，435 条 0 不符）＋**重放分类不变**（0 漂移）。
* **落地**：`rules/naming.json`（22 identifier，ex／tr／rv／sg 号段含预留；name 带版本；state 由 identifier 派生）；`pipeline.json` id 全换 identifier，`label` 移出管线（S7 禁命名属性回写）；journal 4,276 事件与 steps 不改写，旧名（`s0`／`s24`／`s25`／`audit`／`S3`／`R1–R3`）作输入别名；`check_stages` 增 S7 六条；`rules/09` 角色号 R1–R4 去代号（原与节点别名撞车）。
* **迁移**：435 条 tasks.state 改写（s2.4→rv-01 408、drafted→tr-02 16、s0→ex-04 5、s2.5→rv-02 3、r2→sg-02 3），765 条 pending／cleared 不动；报告 `results/state-migration.json`。
* **门禁**：单测 605 绿（新增 test_naming 12 例）；check_stages 22 项、check_all 17 项全绿。

## 2026-11-25 全库置空重译（ADR-0081）：译文只留 H1、进度归零

* **用户裁定**：“既有中文翻译全部置空，除了 H1。所有进度全部置空。不计成本代价。”
* **执行**：`tools/wipe_translations.py`（先 3 件试金石）——SUMMARY 1,868 件正文：427 件截为 H1、1,440 件本已仅 H1、1 件缺 H1（tarski-truth）按词条名补回；SUMMARY 外 8 件补充材料同口径置空。1,200 条任务：done 走 `reopen`、在途 `reopen --upstream-sync`、pending `clear`、cleared 有正文截 H1；1 条 clear gate 未过（tarski-truth）按裁定强制置空并留痕；blockers 全解。逐件报告 `results/wipe-2026-11-25.json`。
* **事实不动**：journal 与 steps 不删不改，仅追加约 1,054 个 rework；`en/`、`yuanwen/`、基线钉、登记册、勘误表原样保留。
* **纪元**：`rules/epoch.json` 声明 2026-11-25T00:00:00Z 为进度纪元；progress／journal_view／账实不变量只统计纪元后的 pass。PROGRESS 重算：核心段 0、在途 0、强制集 0、饱和 0、有正文 0、骨架 1,873、账实不符 0。
* **门禁**：I1/I2 严格档 0 违例；check_stages 22 项、check_all 17 项全绿。

## 2026-11-25 置空翻译历史（ADR-0082）：journal 与 steps 清零、纪元撤除

* **用户追加授权**：“允许置空翻译历史。”据此不再以 P5／ISO 15489-1 保留旧过程记录——处分对象是翻译过程（事件与 steps），不含源钉、登记册、勘误与目录。
* **执行**：`tools/wipe_history.py`——journal 1,199 文件（7,566 行）截为 0 字节（条目仍在账、seq 重启）；1,200 条任务 steps 6,536 条置空（state 仍 cleared、version_pin／zh_doc／created_at 保留）；`state/axis` 19 个旧工单删除。
* **撤除纪元**：`rules/epoch.json`、`tools/epoch_lib.py` 删除；progress／journal_view／账实不变量去掉纪元过滤（历史既空，过滤器失去对象）。ADR-0081 第 4 条由 0082 取代，正文置空条款继续有效。
* **校验**：I1/I2 严格档 0 违例；PROGRESS 核心段 0／在途 0／强制集 0／饱和 0／有正文 0；check_stages 与 check_all 复跑见提交前结果。

## 2026-11-25 全流程国标／国际规范复核（specs/061）：登记册三分与三处过期

* **方法**：22 节点（ADR-0080 口径）× 三层清单（`rules/standards.json` 9 采纳＋1 不采纳／`rules/README.md` 29 行引用清单／`specs/025` 研读日志）× 联网版本核验（57 项，官方来源，检索日 2026-11-25）。
* **结构问题**：引用与登记无闭环——`verify_standards` 只查“已登记项有承接”，查不出“正文引用了未登记标准”；CY/T 118／121／170／171、GB/T 8170 都是正文引用而登记册缺席（G1/G10/G13）。
* **版本**：`ISO/IEC/IEEE 12207:2017` 已于 2026-04-29 废止（现行 12207:2026）；`ISO 15489-1:2016` 与 `ISO 17100:2015` 均转 90.92（2026-11-06／2025-08-04）；`ISO 18587` DIS 第 2 版把范围扩为非人类译文输出，预计 2026 年底；`ISO 5060:2024` 实为 2024-02 发布。
* **制度偏离**：三审同人（ADR-0020 冷置补偿）对《图书质量保障体系》第八条与 ISO 17100 复核分离要求；journal／steps 清空（ADR-0082）对 ISO 15489／GB/T 26162／GB/T 18894／DA/T 22。两项均未在登记册声明。
* **缺失国标**：GB/T 19682-2005（译文质量评定与检测）与 CY/T 123-2015（中文译著：结构、首现括注、译者注独立注码、原文错误用译者注）未登记，而二者正是项目多数实践的直接依据。
* **交付**：`specs/061-standards-realignment-2026/spec.md`（矩阵、G1–G16、P0/P1/P2、D1–D5）＋ `version-audit.md`（57 项版本事实与来源）。**未实施**，待用户裁定 D1–D5。

## 2026-11-25 规范登记册 v2 与 D1–D5 落地（ADR-0083／0084）

* **用户裁定**：specs/061 的 P0 与 D1–D5 全部批准（C／B／B／B／B）。
* **登记册**：`rules/standards.json` 升 v2——`cited` 61 项（标准号、版本状态、落点、来源、检索日）、`adopted` 23 项、`deviations` 5 项、`not_adopted` 5 项；`rules/README.md` 标准表改由 `tools/standards_table.py` 生成（标记区间不手改）。版本校正：12207:2026、15489／17100 修订中、18587 DIS、5060 2024-02、24229:2022、999 FDIS、25964-1 新版、10112／3101 修订中；补登 GB/T 19682、CY/T 123／118／121／170／171、GB/T 8170／44227、ISO 11669、ISO/IEC 11179-5 等。
* **V5**：`verify_standards` 增“规则正文标准号可解析到登记册”，首跑命中 6 处真实缺口（GB/T 19682、ISO 8601、GB/T 32424、CY/T 174、ISO/IEC 15939），补登后全绿；V5 与标准表同步均入 `check_all`（19 项）。
* **D1**：`sg-03` 终审 actor 强制不同于初译／初审／复审，冷置不再替代分离；前两审同人登记为偏离 V01。
* **D2**：LLM 辅助初译按译后编辑（ISO 18587／GB/T 40036）；task 增 `translation_mode` 与 `pe{level,system,disclosure}`，`tr-02` 机检字段与“译后编辑／PE”留痕。
* **D3**：GB/T 19682 采基本／特殊要求，评定仍用 CY/T 266＋ISO 5060。
* **D4**：清史偏离 V02 登记；自本日起新事件与 steps 恢复只追加。
* **D5**：`baseline/term-concepts.md` 概念层建立（键／定义／学科域／概念关系），`tools/check_term_concepts.py` 告警级；2026-12-01 起新术语须同时有概念行。
* **校验**：单测 611 绿；check_all 19 项全绿。

## 2026-11-25 标准条款补遗（ADR-0086）

* **rules/10 新建**：`rules/10-standards-clauses.md` 集中承载 CY/T 123-2015 条款锚点（4.4.3／4.4.5／5.2.4／5.2.5／5.5／5.6／5.7／5.8／5.9.2／5.10／5.14／6）、CY/T 154-2017 条款映射与机检子集（仅 8.1→cjk-spacing、8.2→quote-spacing、5.8.2→curly-quotes、5.12.2／12.2.2→connector-form 四类）、转写系统表（ISO 9:1995＋Amd 1:2024、233-2:1993／233-3:2023、259:1984、843:1997、3602:1989、7098:2015、15919 FDIS 在研、24229:2022、15924:2022）、ISO 5060 评分卡七维＋分层抽样（sha256 定序、≥10% 且 ≥20 段、Critical 转全量）＋评估者能力、TBX 字段映射。
* **G4 机检**：`task_ops` 建账写 `project_spec` 六项（ISO 11669:2024），`tr-02` 前校验非空；CLI 增六参；单测 31。
* **G8 导出**：`tools/term_tbx.py` 导 TBX Core（DCT；GB/T 44227-2024 MOD ISO 30042:2019），实跑 8,951 概念；6 项单测（含分节重复表头、转义、id 唯一）。
* **登记册**：ISO 999:1996／GB/T 22466-2023 由 cited 改列 not_adopted（网页无索引对象，CY/T 123 5.11.4 以译名对照表替代）；ASTM F2575-25／SAE J2450_201608 版本校正；ISO 30042 第 3 版 CD→DIS、GB/T 44227 MOD 补正；补 ISO 15924:2022（cited 60）与 ISO 11940 不采纳。
* **校验**：check_all 19 项全绿；V5 通过（60 cited，23 adopted）。

