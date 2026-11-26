# 项目日志（卷三：2026-11-21）

> 分卷说明见 [日志与编辑规划](ri-zhi-yu-bian-ji-gui-hua.md)。

本卷收录 2026-11-21 全天工作段（specs/053 第五～十六批、specs/055/057 收口、issue #51 与目录账处置等）。

## 2026-11-21 目录巡检 CI 输出治理（catalog-drift，用户指令“完善优化输出信息，禁止表情包”）

* **乱源定案（issue #49 实证）**：①yml issue 组装 echo 双引号内反引号未转义——bash 命令替换把 fetch_catalog/summary_sync/apply-add/rebuild_catalog/check_catalog_network 五个落地工具在只读巡检里真跑一遍，stdout JSON 拼进 issue 正文（issue 尾部两坨巨 JSON 的根因；且 fetch_catalog 无 --snapshot-only 会在 CI 检出区写 baseline/catalog.json）；②drift md 十向全零节各占两行刷“（0）无”；③queue md“源”行直接 json.dumps dict 原样；④fetch/drift/updates 三 step 日志要么 JSON 一坨要么零输出；⑤workflow 名带 emoji。
* **修法**：workflow 名去 emoji；issue 组装“落地”改一行指针（drift md 已有处置路线节，不再重复）；fetch/drift/updates 三 step 各打一行人话摘要（快照计数／十向漂移计数＋装配结论／队列计数＋前 10 条），机器 JSON 一律只落 RUNNER_TEMP 进工件；render_md 全零节折叠“其余 N 项均无差异：…”；render_queue_md 源行人话化（_human_source）；assembly_check 用 redirect_stdout 吞 build/compute 子打印（--quiet 下 stdout 干净）。
* **验证**：本地离线（--latest 快照）render_md/render_queue_md/摘要提取行全验；yml yaml.safe_load 校验；check_all 17 项全绿；提交 12bca3c62 后手动触发真实运行 success，日志三摘要行与 issue #49 新评论均达标（无裸 JSON、无空节刷屏、无 emoji）。
* **教训**：bash 双引号内反引号是命令替换，CI echo 里包命令必须防替换（已在 yml 头部立日志纪律注释）；--quiet 语义要覆盖全部 print 路径——import 调用的子函数 print 会直通 stdout。
* **收尾（用户批准关旧开新）**：旧 issue #49 已关闭（留说明：缺陷根因＋修复提交＋验证运行号）；重触发运行 44833333086 success，新建 issue #51 即新格式产出（无裸 JSON、无空节刷屏）。

## 2026-11-21 issue #51 落地：目录账补 inquiry＋两条上游修订钉前移置空待译（用户指令“全量进行，不进行实际翻译，既有存量 reopen --clear”）

* **mu-lu-s 补 inquiry**：认识论总论节“归纳问题”与 Knowledge How 之间补行；G3 门禁红暴露正确落法——mu-lu-s.md 由 baseline/mulu-map.json ⊕ SUMMARY 重放重建，手改文件属改弱势方，走 `check_catalog_network.py --build-mulu` 抽账收编（inquiry 入账 order 1172、后续顺延），重放全等。
* **modality-varieties／type-theory 上游修订（2026-11-20）**：compare.py 产变更文件（前者 7 节 8 处含 EpiMetMod/MetNomMod/StrModRea 新增节，后者仅导言 pubinfo 更新）；fetch_entry.py 钉前移（557ef0da／f289038b，pubinfo substantive_revision Nov 20 2026）；yuanwen.py 重转；分歧账两条均无存量登记，干净替换无 carry。
* **建账置空（ADR-0050 存量等价链）**：task_ops create --kind retranslate --from 变更文件 → clear（仅留 H1，旧文 git 历史保留）→ advance s0（挂 en_integrity＋en_source_audit，evidence changes: 开头）→ 停在 draft 前。关键发现：**update kind 已死**（create 拒收，ADR-0068 W5 pipeline.json 收编，cli.md 78 行文档过时待修）；ORDER[retranslate] 序列 pending→cleared→s0→draft…。
* **B 系列覆盖确认**：钉前移＋重转后 I2（check_all 第 14 项）与 en-roundtrip B3.1/B3.2 差集巡检自然覆盖这两条，变动按基线差集显形，基线重冻归 053 线（其会话同窗在动 reassemble＋scan 基线，已避开不碰）。
* **收尾**：check_all 17 项全绿，两笔提交（88b76c5ca 目录账／c68a7020b update 链）推送，issue #51 回帖关闭。待办：cli.md 的 --kind 文档修正、两条重译（用户后续派工）。
## 2026-11-21 B3.2 第五批：star 族分诊与词内闭星修复（specs/053，用户“继续”）

* **分诊**：star 257 件子模式普查（a_extra 172／shift 54／b_extra 31）；a_extra 172 件经 replace 窗口标签判定 **172/172 全部 r_pair**（H0 对应处均有真 em）——星族主流是 R 配对错位而非 md/en 不一致，可修。
* **判例回源（africana）**：H0 `T<em>he Sociology…Chang</em>e`（em 从词中起排），md `T*he…Chang*e`＝词内开星＋**词内闭星**。旧判据只认右邻非字母数字的闭星——词内闭星右邻字母 `e` 漏判，整对星字面化。
* **修复**：`_intra_word_open` 决断条件改“第一个紧闭星右邻**非数字**”即进文字形态判定；`(G*1)…(G*2)` 右邻数字排除不回退。纯增量规则：改前改后成功路径不变，只把失败路径转成功。
* **同批回退记录**：嵌套星对三轮判据（歧义预模拟／括号收紧／贪心残留）B3.1 净退化 3→7 件均大于收益（+1），全部回退。根因：C 对嵌套 em 转不出外层星（外层整个丢失），H0 字面星残留与真嵌套在 md 扁平形态上不可区分——专项开放。
* **实测**：池 **1,274（68.0%）／缺口 599／stale 0**（第四批 1,272／601）；池占页 **31.79%**；chrome 1,873/1,873 不变；B3.1 **1,452/1,873 持平、集合级 0 退化**；africana 转池（269 补丁）。
* **教训**：①分诊先行——172/172 全 r_pair 直接推翻“H0 字面星为主”的猜测，主力从不可解问题转到可修问题；②普查锚坐标系必须与判定坐标系一致（首轮 118/172 noanchor 全是 ukey 流与原文的坐标错位）；③“replace 窗口原段拼接”是判定 H0 标签形态的最短路径；④判据迭代以 B3.1 净退化数做止损线，止损要果断。

## 2026-11-21 遗留问题清扫（用户指令“解决所有遗留问题”）

* **事实修正**：modality-varieties／type-theory 置空前仅 H1 一行——实为存根件（从未翻译），上轮“存量直译”系误判；compare.py“译文存根”判定正确，无缺陷。置空路径对存根件语义无伤（结果等价：留 H1 待译）。
* **sync_guard 误拦修复**：`pre` 为空分支原先只打印不返回，继续走 rebase 被工作区未提交改动误拦；改为 HEAD==origin/main 时“已是最新”即返、远端有新提交时走 `merge --ff-only`（对工作区宽容，撞文件才拒），复现场景验证 exit 0。
* **update 死表述跟进（ADR-0050/0051/0068 文档对齐）**：cli.md 两处（create 的 --kind 仅 retranslate、行为段“update 类”改“上游修订件（--from 建账）”）；rules/04 五处（状态机表 update 行改写为按件况建账走 retranslate 链、s0 位置括注、s24/s25/不复查旧错三处字样）；AGENTS.md 两处（必读表与硬约束表“转 update 任务”改“建账置空待译”）。
* **workflow 名 emoji 清零**：八个 workflows 全部纯文字（catalog-drift 上一轮已改；本轮 checks/Auto-Assign/links/create-pdf/en-roundtrip/render-artifact-audit/format 七个；sed 对四字节 emoji 失败，改用 Python 按 Unicode 码点替换）。
* **PROGRESS 刷新**：journal 派生读数（正式词条 1873、已建任务 1199、账外 674）。
* **未动项**：两条重译仍待用户派工（上轮边界“不进行实际翻译”继续有效）；specs/008、specs/053、assembly-patches 仍为其他会话工作面。

## 2026-11-21 形式化完备性证明（issue #51 类处置线，用户指令“进行形式化完备性证明”）

* **落档**：`specs/054-catalog-network-replay/results/formal-proof-update-line.md`——续 044/053 家法（A/T 编号顺延，T9–T12）：T9 B 系列触发判定（挂载集交集空＋机检定义域覆盖＋三道显形面＋残差边界）、T10 变动标记完备性（九类变动→存储账→判官映射，“变动未记账即红灯”逐行构造）、T11 检测完备性（四路检测＋漏报面如实列出）、T12 流程保证（前置校验/机检/CI 终审/append-only 审计四层串联）。四问逐一对应定理，附可复算实证数据点。
* **证明期发现与处置（形式化的直接收益）**：journal lock 事件 schema 已定义但 fetch_entry 钉前移未落事件——T10 第 1 行审计缺口。补实现（upsert_baseline 尾部 _journal_lock，sha 同幂等不落）＋单测 2 项（test_fetch_entry 6/6 绿），三账（entries.json/upstream-snapshots/journal）齐备。
* **验证**：check_all 17 项全绿（含管线单测）；提交推送后 CI 终审。

## 2026-11-21 全流程独立审计（用户指令“审阅全流程”，ADR-0039 独立复算）

* **账实复算（不引旧结论，全 True）**：inquiry/modality-varieties/type-theory 三条 en 钉 sha↔实文件、yuanwen 登记↔实文件、source_sha 三查一致；两任务账 state=s0_source_checked、evidence changes: 前缀、version_pin 双钉；journal 各 pass(s0) 一条。inquiry zh md 为存根（1 行 H1，未译属预期）。
* **提交审计**：本会话 8 笔逐笔 --stat 抽查，无越界文件；specs/008/053/055/assembly-patches（其他会话）全程未碰；origin/main..main 空；check_all 独立重跑 17 项全绿。
* **发现一（登记不补写）**：两条任务 journal 无 lock 事件——钉前移时点先于 lock 补丁（3dcc94b31），事后补写将伪造 at 时间戳，登记为已知欠账，自下次钉前移起三账齐。
* **发现二（归属他线）**：开放 issue #50（EN 互转漂移，92 转差/25 转好/+inquiry/−privacy-medicine）开立于 2026-11-19，为本会话工作之前 B3.2 第四批修复的伴生差集，落地方向（重冻基线）对应 specs/053 线其他会话未提交的 assembly-scan-all.json——不越界，由 053 线关闭。（同日用户指令后由本会话关闭：差集已被第四/五批基线重冻吸收，最新 cron 无变动报告；⑤ 词条增删随目录账落地。）
* **发现三（功能性 emoji 登记）**：links.yml 第 50 行 grep 过滤 lychee 报告的行首 emoji 标记属解析外部产物格式，非输出装饰，保留。
* **文档复核**：rules/04/cli.md/AGENTS.md 改后表述准确；task_ops grep B 系列计数 0（T9(a) 断言成立）；八个 workflow name 行 emoji 清零。

## 2026-11-21 mu-lu-s 前沿分类重审（specs/055，用户指令“根据前沿学术界分类方法重新分类排序”）

* **选型**：两案骨架（PP 骨架＋本地细分 vs 现行四区＋校准）经用户裁定选**案一**；排序按主题聚簇＋重要性/影响力，史区人物簇也按重要性（016 生年序作废，断代 H2 保留时间序）；单一归类（check_mulu_s 第 5 项语义不变）。
* **锚点事实**：SEP 官方无公开分类体系（实测）；锚定 PhilPapers（国际事实标准），8 处模糊类目挂载点逐页核实（决策博弈/道德心理→行动哲学、技术→计算与信息、化学→物理科学、医学/教育 PP 有类、环境/生死→应用伦理、经济/文化→政治与社会、犹太→哲学传统）。
* **落地**：`mu-lu-s.md` 全量重排——H1 四区改六区（形而上学与认识论 387／价值理论 324／科学逻辑与数学 388／西方哲学史 594／哲学传统 180），14 簇整建制迁移，14 处学科枢纽 S 档＋98 处经典专题 A 档居前、余按英段字母序，标题节点 17 个父节按重要性显式重排；26 行节注随节迁移＋3 处旧路径引用同步修订；链接集合守恒 1883 进=出。
* **门禁**：check_mulu_s 五项全绿；mulu-map 重建 1883 行后 catalog-net G1–G4 全绿；check_all 17 项全绿（一次假红系试写产物触发 docsize＋临时目录竞态，删除后复绿）。
* **发现登记**：三处 SUMMARY 域标题缺陷（kochen-specker“ks 定理）”残段、logic-provability/feminism-objectification 作者括注截断）——属 017 标题体例修复线，另轮处置；详见 specs/055 results/execution-log.md。
  **（2026-11-22 改判）**：经取证系**审计误报**——四处（SUMMARY/H1/新旧 mu-lu-s）逐字一致完整，假象源于 en_key 启发式（作者名内嵌括号截断＋全角注记段内字母误起算）；SUMMARY/词条零改动，en_key 重写＋回归测试后对旧版重放，增量仅 kochen-specker 一行移位。

## 2026-11-21 人名表逐行研判全表收官（specs/013，用户指令“所有无法判断的和已经判断的术语，人名都必须逐个结合不同原文研判”）

* **终态**：4,594 行（26 张简报 s01–s26）逐行显式判定收官，判定台账零缺；凭证账 1,117 行；缺项告警 2,696 → 924（余量为合规留空，非漏判）。26 批每批覆盖核对＋写回＋对账＋推送，`origin/main..main` 恒零。
* **取证道**：简报（原典语境＋GND／WD 候选）→ marks 全行判定（KEEP/FILL/FIX/NOSOURCE，note 留痕）→ marks_to_ledger（--check＋再生）→ apply_person_meta 写回第 4/5/7/8 列 → check_terms 汇总对账。DEFER 定点补查五轮（wd_defer.py，130 键，约 40 键转 FILL）。
* **误配防线战果**：机采误配改判 13 件（林奈／Partee／Arthur Pap／Boyd／Price／Porzio／A. G. Walker／王莽／Eric Williams／左拉／扬雄／Searle／Hippolytus），拒绝误配 20 余件（建筑师／卡巴莱艺人／足球员／昆虫学家／贵族谱系库等）；日期错列族 15 件归正（权日身／白颐正／白文宝／朴世堂／愼後聃／李齐贤／李穑／朝鲜太祖／尹鑴／李kan／李震相／李恒老／李檗／李睟光／李承薰，凭韩国学典八条目＋WD）；混指键 13 族登记拆键队列（Leland／Cosimo／Crates／Nicholas V／Philip II／Pythodorus／Radcliff／Sotion／Vacca／Wimsatt／Sherman 伪人等）。明细见 specs/013 execution-log 2026-11-21 节。
* **管线修正**：marks_to_ledger 三处（defer 载序最后载入——修正五轮补查静默失效的关键 bug；nat/life 缺列回退现值防误抹；expand_src 进凭证行）；check_coverage.py 新增；fix_quotes.py 全库引号清洗 10,258 处。
* **门禁**：本线范围 16/17 绿；唯一红项“管线单元测试”系并行会话 specs/053 线在途 tools/yuanwen.py 改动（test_em_with_trailing_star_escaped），非本线产物，由其线收口。
* **事故对账（与 specs/055 线互相印证）**：s25 提交（ca31f15d8）扫入并行会话经 checkout 污染的暂存 mu-lu-s.md——我侧系 git commit 未带 pathspec 卷入整个暂存区；对方已于 6e701789b 原子修复并复绿。防线登记：共用工作树提交一律 `git commit -- <路径>`（只提交指定路径，无视暂存区残留），checkout 旧版一律临时 worktree。
* **下步**：术语表 r02–r31 逐行研判（约 6,100 行）＋待处置队列（拆键 13 族／键形全角 84／撞形 538）。
## 2026-11-21 术语线开工（specs/008 全表 6,109 行，继续“逐个结合不同原文研判”指令）

* **机制**：r 系简报（r01–r31，每张 200 条）→ marks（default＝KEEP，仅非 KEEP 键显式落记）→ term_marks_audit.py 汇总 per-line-adjudication 台账（含 s 系已判 1,054 行＋m 系专项件）→ 每批 pathspec 提交推送。已判 r01（KEEP 193／FLAG 7）、r02（KEEP 193／FLAG 6／FIX 1：Curry-Howard 连接号按 ADR-0041 改一字线）。
* **管线修正**：收集器载序改 s→m→r（r 系全量复判最后载入，显式判定权威胜出；修正前字母序 s 后载会压 r）。
* **竞态变体登记（自首）**：r03 批次我的收集器写盘撞并行会话文件锁报 OSError（Errno 22），但我未核实即 add+commit，把并行会话的台账再生＋note 改写（443/443）扫进我的提交（d7fb7e177），信息未提对方改动——内容零丢失（r03 七 FLAG 经对方再生入账），提交信息失实，以本条自首。防线：收集器/生成器跑完先验输出增量与行数再提交；写盘失败＝工作区可能已是对方再生版本，须 `git diff` 取证归属再动作。
## 2026-11-21 术语表逐行研判收官（r18–r31，全表 6,109 行判毕）

* **进度**：r01–r31 三十二批简报逐批判毕、逐批 pathspec 提交推送；台账 `per-line-adjudication-2026-11-20.jsonl` 6,240 条（含漂移补录 131 键），非 KEEP 779＝FLAG 726／FIX 19／MERGE 34，KEEP 5,461（FIX 40→19 见下条连接号更正）。
* **账闭合**：登记册现 7,109 行＝r 系简报 6,109 行＋开工前既有判定种子 1,000 行（`state/term-judged-seed.txt`，简报生成即以此排除）；补账核验“缺号 869 全部属种子”，非漏判。
* **实质发现举例**：pramāṇa 现译“量论”与 pramāṇavāda 撞形且失“量”义；skeptical theism 译“怀疑论神学”（theism 系有神论非神学）；syncretism“折中主义”与 eclecticism“折衷主义”同词形撞；vyatireka 现译“同无”与自注“异品无”矛盾（疑“异无”之误）；wujūb 原文列误填 وجود；Siddhānta-muktāvalī 与 Nyāyasiddhāntamañjarī 共用《宗义摩尼鬘》；Scott 未按人名表音译；site 直译“站点”；samudghāta 自拟“灭除投射”超出源文 extermination；polarity 三义（太极／极性项／两极性）单行不能覆盖；population thinking 宜“种群思维”；non-singular term“单数”误植（应“单称”）。
* **维持原判两例**：pakṣatā“宗未决性”经联网核证（Gangesa／Annambhaṭṭa 定义含“未确定所立”）成立；Pyrrhus et Cinéas 书名《皮瑞斯与辛尼阿斯》合中文维基既有形（Pyrrhus 通译“皮洛士”已注于行内）。
* **MERGE 族**：同键变体与单复数／拼式重复（scepticism／skepticism、singleton set、possible worlds、poverty of stimulus、QFT／Quantum Field Theory、relevant logic、true class→proper class、units of selection、sophismata 两件、place (topos) 等）均并入主行，留变体注。
* **连接号方向更正（自首）**：r02–r31 有 21 条 FIX 把“人名／概念复合短横线”判改一字线，方向判反——ADR-0041／rules/02 §连接号明定短横线＝复合名词与外来语内部分合（盎格鲁-撒克逊、让-雅克），一字线仅用于时间与地域起止，且 Tier 3 未批禁铺量；经复核 ADR 原文后 21 条全部撤回为 KEEP（Curry-Howard、Einstein-Podolsky-Rosen、Fischer-Ladner、Heine-Borel、historico-critical、honesty-humility、柏拉图-黑格尔、Kleene–Mostowski、知识-如何／那、科亨-施佩克尔×2、林登鲍姆–塔尔斯基、勒文海姆-斯科伦、手段-目的、米勒-莱尔、突变-选择平衡、正理-胜论、沃尔夫-鲍姆嘉通、波尔-罗亚尔、策梅洛-弗兰克尔），更正注已入台账。教训：连接号三形先按 ADR-0041 逐形核分工，不得以“统一方向”一句话概括全部连接号。
* **待收口**：FLAG 726 键走 termonline-batch 联网核证通道裁定；FIX 40／MERGE 34 写回 `shu-yu-biao.md`（修弱势方，须凭证）并联动 m 系撞形 620／键形 84 队列。
## 2026-11-21 术语表写回：FIX 19、MERGE 34（修弱势方）

* **写回口径**：按 r 系逐行研判台账（2026-11-20）修弱势方——登记册行为弱势方者定值，依据列留凭证（逐行研判 2026-11-21）；吸收行删除，主行依据记“旧键并入”并录旧键首现。凭证表 `specs/008-terminology-campaign/results/writeback-2026-11-21.tsv`（类型／键／原文旧新／译法旧新／理由）。
* **FIX 19 分型**：改译 8（后验必然性、现实论者、先天性、经典极限、坍缩模型、范畴的、能取所取、标记重捕法）、人名音译 1（斯科特同构定理）、删除跨行重复亦作 1（comprehension axiom）、原文列正列 8（Aufbau 补全、Bayes’／blob／Calvinism／causal closure／conceivability 归“—”、causa secundum esse 补录、acquired psychic nexus 去尾随空格）、译法列去释义 1（飞矢不动）。
* **MERGE 34**：同键变体／单复数／拼式／首字母重复各行并入主键（scepticism、singleton set、possible worlds、poverty of stimulus、QFT、relevant logic、place (topos)、sophismata 两件、states of affairs、units of selection、true class、wu xing、yì 等），主行译法按需补亦作（correspondence theory of truth、Symphilosophie）。
* **账**：登记册 7,109→7,075 数据行；`check_terms` 退出 0（无硬错误，余 924 条人名缺籍属／生卒告警为既有账）。台账文件系 2026-11-20 快照，写回后 34 键已离册——收集器已加缺键告警，后续勿盲目重生成以免丢 MERGE 记录。
## 2026-11-21 撞形队列处置三批（并键 62、豁免 227 键、改定 50）

* **复算入口**：`script/tmp/collision_live.py` 按登记册现况复算主译撞形——首批 44 并＋174 豁免后残余 99 组（217 键），队列落 `results/collision-live-2026-11-21.md`；口径补“保留原文／拉丁原文保留”为不译占位、非主译。
* **第一批（B1）**：结构重复并键 13（单复数、形容词形、同概念异形：Incommensurable、Intuitionistic、karma 两形、host 两形、ideal elements、normal functioning、right of nature、moral judgments、immediate perception、supposit for、perspectivalism、Computing、adharma 两形）＋跨语言／同形异义豁免 46 键（希腊—阿拉伯—梵—藏—德语同概念，及 same-reliance 等异源同形）；7,031→7,018。凭证 `collision-b1-2026-11-21.tsv`。
* **第二批（B2）**：改定 47（审定库凭证：soundness 可靠性／reliability 可靠度、separability 分离性、pramāṇa 量（认识手段）、pakṣa 宗（所立）、circumscription 限定（非单调推理）、prajñapti 假名（施设）、reify 物化、illusion 错觉、Validation 验证等）＋豁免 28；改定引入的新撞形再判：并键 4（ampliative、coherence theory、exceptive term、reify）、再改定 3（disputation 辩论（义务论辩）、finality 终极性、pakṣa 宗（所立））、补豁免 7（illusion╱Täuschung、non-determinism╱indeterminacy、pramāṇa、pudgala 两义等）；末段改定 3（separability 分离性、substantialization 实体性、restriction 限制）＋豁免 2；末组并键 1（substantialization→substantiality）。凭证 `collision-b2-2026-11-21.tsv`、术语在线 JWT 直连 147 词凭证（`queries/termonline-all/`，2026-11-21）。
* **终态**：残余 0 组（已豁免 114 组）；登记册 7,013 数据行；`check_terms` 退出 0；`check_all` 17 项全绿。
* **判据**：ADR-0048 要求的是“分行”——分行已成立且两概念确属同形异义者记豁免（如《中论》两书、historicism╱Historismus、entailment╱implication）；实为一概念者并键；一方译法失准者按审定库改定。禁以“主译必须互异”为唯一标准强行拆词。
* **直角引号违例（自首）**：写回与撞形脚本的注记模板用了直角引号（U+300E／U+300F），共 192 处落进登记册依据列；13a7c177a、0df7301de 两次提交未复跑门禁，故 check_quotes 一直是红的而我未报。已全量改弯引号（`check_quotes` 违例 0），`check_all` 复绿。防线：生成脚本的字符串模板同受 rules/02 §11 约束，提交前必跑 check_all 而非只跑 check_terms。
* **数字更正**：0df7301de 提交信息写“7,109→7,065”，实为写回后 7,075、撞形首批并键后 7,031；以本条与凭证表为准。
* **未决**：tashkīk 现译“调节（等级单义）”与阿维森纳—苏赫拉瓦迪“等级歧义”义不合，留待 ① 查证批裁定；撞形豁免 227 键的标记（marks）状态待与 FLAG 台账对齐。
## 2026-11-21 FLAG 查证首轮（①）：活队列 151 键，落定 113、未决 38

* **活队列口径**：2026-11-20 台账 FLAG 726 键扣除已离册（并键，141）、已随撞形处置（317）、已有 ok 凭证（261）后，撞形类以外待裁定 151 键（`results/flag-live-2026-11-21.tsv`、`flag-review-2026-11-21/vol-01..02`）。判据同撞形批：分行已成立者维持并登记凭证，实为同概念者合键，译法失准者改定，数据缺陷者正列。
* **取证通道**：术语在线 JWT 直连（`tools/tl_jwt_crawl.py`，恢复他队列断点后跑 147＋48 词，凭证入 `queries/termonline-all/`）、中国大百科条目标题探针（`script/tmp/zgbk_probe.py`，18 词，`results/zgbk-probe-2026-11-21.txt`）、`en/` 原文回读（`script/tmp/ctx_en.py`）。MCP 检索通道（exa／research search）本会话连接失败，必应直连结果噪声大，故以审定库＋大百科＋原文三源为主。
* **批 A／B／C 落定 113 键**：改定 90（如 anomalous monism→异常一元论、deterritorialization→解辖域化、continuum→连续统、anupalabdhi→不可得、Gentzen sequent→根岑矢列式、etiological→发生学的、vyatireka→异无 等，明细见 `flag-fix-a／b` TSV）、合键 12（future contingents、converso、ḥikma、insolubilia、lawlike／lawfulness、obligatio／obligationes、truthmakers、problem of universals／universals、parārtha、notiones secundae、scholastic quaestio、svārtha）、删行 1（abilities 普通词复数）、补登 3（corporation 公司、operational semantics (program theory) 操作语义、rabbāniyya 养育性）、另补豁免 1（Indalmoi）、维持 26（附审定库或语境凭证，`flag-keep` TSV）。
* **实质判例**：anupalabdhi 依大百科“不可得比量因”定“不可得”（原“未觉”）；continuum 依大百科“连续统假设”定“连续统”；deterritorialization 依审定“解辖域化和再辖域化”；sequent 依审定定“矢列式”（Gentzen sequent→根岑矢列式、hypersequent→超矢列式）；psychometric 族按审定“辨别效度”维持；epistemic 族 18/26 行作“认知”，三处例外（认识论责备／知识证成／认识状态）统一为“认知～”，ESR 保留“认识论结构实在论”并登记族内例外。
* **数据缺陷正列**：Needham problem 原文列中文→英文原词；wujūb 原文列 وجود→وجوب；correlative cosmology 原文列中文→英文；autexousion 原文列补同文异形 autoexousy；al-kabar 键形与出处更正（khabar，ibn-taymiyya 认识论四源，原误记 saadya）后并入既有 khabar 行；ḥikma→Ḥikmah 合键。
* **每次改定后复算撞形**（`collision_live.py`）：批 A 引出 2 组（khabar 重复、契约论），批 B 引出 6 组，均当轮合键／再改定／补豁免收净；终态残余 0 组，已豁免 114 组，登记册 7,013→7,002 数据行，`check_terms` 退出 0，`check_all` 17 项全绿。
* **未决 38 键**（`results/flag-open-2026-11-21.md`）分四类：译名查证 15（a fortiori argument、A New Elucidation、anyāpoha、aṣālat al-wujūd／māhiyyah、bhāvanā、das Umgreifende、significatio、naimittikī 等，需权威译本或研究文献）、用语重抓 12（expansion coefficient、Garden、general characteristic、Guelph、jing、kata、Leib、filtration、corporations、spiritualism 等，属证据列缺陷、不动译法）、回源核对 6（correct／incorrect conventional 键截断疑虑、aṣālat 两行等）、分域登记 5。

### 同轮续：批 D／E（用语归属回核与既有解决结案）

* **批 D 回核六项用语**：expansion coefficient（qm 三见）、filtration（logic-dynamic 六见）、general characteristic（abhidharma 原文 sāmānyalakṣaṇa 共相义确证）、kata（japanese-aesthetics “a form ( kata )”确证）、jing（zhu-xi 首译成立）、Garden（epicurus “the Garden”学派别称确证）——登记册用语列本无错，FLAG 所指系 dossier 证据行误选，六项维持结案。
* **批 D 正列两项**：Guelph 用语由 marsilius-padua 改 dante（SEP 全库无 Guelph 拼形，党派通作 Guelfs，dante 六见、humanism-civic 一见）；spiritualism 撤回“hartshorne 实抓误译”自注——原文“a scientific sort of spiritualism”确是唯灵论义，译法列去释义。
* **批 E**：既有解决的主行结案 17（binarium／ideal element／Kabbalah／moral judgment／normal function／place (Aristotelian topos)／Ḥikmah／qiyāsāt 按域分义／operational semantics 分行／geomancy 族／Sortals／content internalism／exceptive word／nirvikalpaka 族／corporations 分域／intension and remission 孤行）；改定 2（rubūbiyya 主性单列；correct／incorrect conventional 补藏语原文列，回读原文证键未截断）。
* **终态**：151 键落定 140，未决 11（a fortiori argument、A New Elucidation、anarchic hand、anyāpoha、aṣālat al-wujūd、aṣālat al-māhiyyah、bhāvanā、das Umgreifende、Leib、naimittikī、significatio），缺口一律为“需权威译本／研究文献”，而本会话检索通道不可用（exa／research MCP 连接失败，必应直连把多词中文查询退化为单字词条，仅能作单点验证），故按 rules/03 不猜、如实留白。
* **门禁**：`check_terms` 退出 0、撞形残余 0 组；`check_all` 17 项中 16 绿，唯一红项“转换保真”系 `yuanwen/b/bodin.md` 于 22:20 被并行会话改动（工作区 M，非本线文件），按并行纪律不修不提交。

### 同轮续二：联网恢复后未决 11 键清零（批 F）

* **通道恢复**：exa MCP 恢复后以英文／中文实词查询直取权威页，替代此前退化的必应直连；全部 12 条改定（含 tashkīk）逐条留联网凭证。
* **判例与凭证**：A New Elucidation→《形而上学认识各首要原则的新说明》（李秋零译《康德著作全集》《康德认识论文集》目录）；a fortiori argument→当然论证（法律论证文献 argumentum a fortiori 通行“当然论证／当然解释”）；anarchic hand→异己手（清华长庚医院、华艺《異己手徵候群》）；anyāpoha→遣他（法尊译《集量论》卷五《观遣他品》，华文哲学百科作遮诠）；aṣālat al-wujūd／al-māhiyyah→存在的优先性／本质的优先性（王希《伊斯兰哲学中的“是”、“存在”和“本质”》，SEP mulla-sadra 作 principality of existence／essence）；bhāvanā→修习（《佛光大辞典》【修习】：“梵语 bhāvanā……数数薰习之意”，撤回自拟“心习”）；das Umgreifende→大全（王玖兴译《生存哲学》“对于大全的体验”“大全的几种样式”）；naimittikī→缘发的（弥曼差 naimittika-karman＝occasional sacrifices，原“自然种类词”义反）；significatio→意谓（中文中世纪逻辑研究，与指代对举），signification 并入；Leib 用语删人名引用改取 existentialism／phenomenology 两处“活的身体”义。
* **tashkīk 更正**：原“调节（等级单义）”改“等级性（分级述谓）”——SEP mulla-sadra 述 tashkik 为存在按强度分级（graded），与 accommodation 行的撞形随之解除。
* **终态**：151／151 落定，未决 0；登记册 7,002→7,001 数据行；撞形残余 0 组；`check_terms` 退出 0；`check_all` 17 项全绿（并行会话 bodin 改动已完成，转换保真项回绿）。

### 同轮续三：批 G（corroboration 分形）＋ m 系 m1000／m1200 结案

* **四词分形**（科学哲学高频族，历轮各批留下互相撞形）：verification＝证实、confirmation＝确证（确证理论）、validation＝验证（仿真 V&V 校核／验证／确认三分）、corroboration＝确认（degree of corroboration＝确认度，亦作“验证”）。凭证：波普尔《实在论与科学的目标：科学发现的逻辑后记》中译“验证度”一节（作者自述弃“确证度”改“验证度”，并把“确证”让给证实主义者）；周煦良等译《科学：猜想和反驳》用“确证”。为避免与 validation 验证、confirmation 确证混同，corroboration 主译取“确认”。
* **确认同形异域豁免**：corroboration（波普尔）与 ascertainment（nges pa，藏传量论）同译“确认”，按条区分不合并。
* **m 系结案**：m1000（10 键）与 m1200（5 键）逐条对账，15 键全部已在前批落定（改定 8、写回 MERGE 2、批 E 维持／正列 3、并入 1、改定 Arrow 1），结案表 `results/m-batch-close-2026-11-21.tsv`；m-collision（538 FLAG）与 m-keyform（84 FLAG）已分别由撞形三批与键形归一覆盖。
* **终态**：登记册 7,001 数据行；撞形残余 0 组、已豁免 115 组；`check_terms` 退出 0；`check_all` 17 项全绿。
## 2026-11-21 EN 逆向装配第六批：C 侧转义改造与结构化强调（用户“1”批准 C 侧专项后落地，续作至 11-22）

* **路线反转**：接五批“star 三轮回退”结论，判据试错的终点是语义层——R 侧形态试探三轮不收敛，根因在 C 侧有损（md 里字面 `*`／`$` 与强调定界符、数学定界符不可区分；嵌套强调 strong 套 em 679 处/77 件、em 套 strong 81/38、em 套 em 255/82 在旧四条单层正则下整块丢失）。本批先改产生方再改判下方。
* **C 侧**（tools/yuanwen.py）：文本层全转义（`\`→`\\`、`*`→`\*`、`$`→`\$`，单射）；`_emph_tags_to_md` 栈式单趟取代四条正则（同类嵌套压平、异类照发、空白外移含 `&nbsp;`/U+2028、缺闭合回删、跨 `<br>` 引块行不发表、相邻同类合并）；数学体美元转义（行内全转、显示只转边缘）、空公式 `\(\)` 不产 `$$`、裸排环境先暂存后补 `$$`、希腊字母在斜体内出裸字符。
* **R 侧**（specs/053 bin/reassemble.py）：`_star_parse` 改 run 逐星消费（整 run 全作开星优先→按 slot 最内层先闭），撤 `_intra_word_open` 与全部形态试探；code 段占位；`\$`/`\*`/`\\`/`\#` 占位还原；数学改扫描式占位（显示体允许成对单美元）；记号星占位撤除（吞合法闭星）。
* **检查器配套**：fidelity `strip_math_ex` 增 `dollars=False`（html 侧裸 `$` 恒字面，全库 728 处/105 件皆币值）；作者行剔除限 count=1（berlin 图注整行 em 恢复后被误删判例）。
* **实测**：B3.1 **1,452→1,569/1,873（83.8%），集合级 0 退化**（转绿 117／转红 0）；B3.2 建池 **1,274→1,359（72.6%）／缺口 514／stale 0**，池占页 31.79%→34.70%（T7 如实同报）；I2/I3 门禁 1,873 全过 0 issue，深比对软信号 305（基线 322）。全量重转七轮（含 entries.json sha 登记同步），中间轮次 1,467→1,521→1,562→1,551（反斜杠转义引入 17 件转红，补 `\\` 还原后恢复）→1,569。
* **教训**：①“顺手修一处”必须全库复跑——第 4 轮反斜杠转义一次性引入 17 件转红，靠集合级对照当场定位；②嵌套强调的正确表示是栈不是更强的正则；md 扁平形态表达不了的结构宁可压平／不发表并交池补，也不产歧义星流；③检查器与转换器必须同批改，字段语义变化不同步对称面就整批假阳性。

## 2026-11-25 目录条目标题体例规范化建议书（SUMMARY＋mu-lu-s，评估类）

* **任务**：用户指令“对 mu-lu-s 和 summary zh en 条目本身给出符合国内、国际学术标准的规范化建议，不计成本代价，如人们之间的符号等。联网查询标准规范”；评估类交付（rules/08 §14：结论＋证据＋建议＋改判表），不实施。
* **产出**：`jian-yi-shu/mu-lu-tiaomu-ti-li-gui-fan-jian-yi-shu.md`——SUMMARY＋mu-lu-s 共 3,738 行条目全量量化；国标条款级比对（GB/T 15834-2011 §4.5/4.10/4.13/4.14/4.17、GB/T 15835-2011 §5.1.1、CY/T 154-2017 并列英文词组顿号条款、GB/T 22466-2023 见参照〔2023 新版代替 2008〕、ISO 999:1996、CMOS 17/18 §6.80、SEP contents.html 上游自证、世界人名翻译大辞典）。
* **核心发现**：①作者栏并列顿号 1,276 行 100% 统一且有 CY/T 154 直接支撑——登记判据即可，零改动；②唯一双轨并存大项＝标题内并列连词：en “and”→zh “与”129／“和”71、无判据，两案呈裁（案 A 全量归一“与”76 行／案 B 双轨白名单登记）；③微瑕 26 处全定位：U+2027 间隔号混码 1、`&ndash;` 实体泄漏 1、别名行 zh 连接三形态（——见 623／：见 4／缺连接 11）、——见 前带空格 3、见后全角冒号后空格 2、分组行 en 先行 2、mu-lu-s 标题 en dash（–）2 处违反 rules/02 ADR-0041 一字线裁定，并暴露 connector-scan 世纪区间模式缺口（现仅覆盖“年”与生卒年）。
* **待裁**：丙类“与／和”归一两案；实施须另立 specs（甲类机械 16 处＋乙类补译 10 行一批，丙类视裁定单列）。

### 补记（同日）：并行树提交收编事故与自愈

* **发案**：提交建议书时 `git commit` 未带 pathspec，把并行会话已暂存的 croce-aesthetics 四件删除一并收编并推送（c6a451fed，6 files）；推送后 origin 曾短暂处于“SUMMARY 仍列 croce 而 yuanwen 镜像已删”的不一致态。归因：提交纪律“只提交相关文件”违例——并行树收编族的提交面变体（specs/004 返工成因 R4 族）。
* **自愈**：并行会话随即提交 0ae9d83b6（specs/054 croce 换发＋gorampa 作者变更，五门全绿）续接其上，origin 恢复一致；未做还原提交以免与其在途状态碰撞。快照后复核：条目行 3,738 守恒，“与／和”计数不变（和 152＝142＋10）。
* **防线升级（rules/08 §12 二发升级）**：并行树上有他人已暂存内容时，提交一律 `git commit -- <pathspec>`，或提交前核对 `git diff --cached --stat` 应为空；判例已并入会话记忆“并行会话共树作业危害”。

## 2026-11-25 目录条目标题体例规范化实施（specs/059，甲 15＋乙 11，丙不归一）

* **裁定**：用户“与和不必强制归一化。甲乙丙全部批准，任何机械处理必须事后全量复核”。丙类（标题连词“与／和”）不归一、不设机检；甲类符号 15 处＋乙类别名补中文连接 11 行实施。
* **写回**：`specs/059/bin/apply.py` 整行精确匹配、前置门（每条 old 唯一命中，命中 0/>1 即中止）、逐行 old→new 追踪、幂等。`applied=26 abort=0`；复跑 `applied=0`。
* **事后全量复核**（独立复算器 `bin/recheck.py`，不复用替换表）：P1 U+2027、P2 HTML 实体、P3 见前空格、P4 “：见”、P5 冒号后空格、P6 分组行序、P7 mu-lu-s en dash、P8 别名缺连接，改前 1/1/3/4/2/2/2/11 → 改后全 0，`VERDICT: PASS`；行数守恒 2,787／5,274；diff 26 行逐行落白名单。
* **派生面**：`gen_en_summary.py` 重生成 SUMMARY-en 1 行（实体镜像）；`check_catalog_network --build-mulu` 重建 mulu-map 3 行，G1–G5 全绿。
* **判据落地**：ADR-0078＋`rules/01`“条目标题体例”节＋README 标准清单增 GB/T 22466-2023、ISO 999:1996、《世界人名翻译大辞典》。
* **研判结案**：L2378 左段 `Models in Science` 经 ADR-0024 判为合规存量（左侧写目标完整标题），同族 103 行维持不改；“建目录别名词条左侧英文”存量面（P11=484）不在本卡管辖。
* **外部红项**：`check_all` 唯一红为并行会话 vives 批（5700c2b82）的 H1 不一致（比韦斯／维夫斯），`journal/v/vives.ndjson` 在途 M，判其在途不抢修；本卡 26 处已随该提交收编入库（特征串核验 4/4、2/2）。

## 2026-11-25 六轴独立质量工序立项（ADR-0079，specs/060）

* **裁定**：用户认定标点、语法、语域、引文、计量、逻辑六类均未独立实现，要求全部独立；四项裁定＝工序层独立、全量回炉、结构化人工判据、只禁未定型日源词；补裁＝目标态 r2_reviewed、现代著作也逐条查原文、方括号承载、术语级全部首现括注。批准立项至 r2_reviewed。
* **状态机 v3**：`pipeline.json` 16 节点扩为 22，新增 q1_cite_check → q2_logic → q3_grammar → q4_register → q5_measure → q6_punct，接在 s2.5 与 S3 之间；`journal_lib` 加映射（ORDER 自动推导，零任务迁移）；`task_ops.advance` 挂 `_axis_gate`；首期 `gate_owner=false`（T1 升硬）。
* **判据与工具**：六器 `cite_audit`／`logic_audit`／`grammar_audit`／`register_audit`／`measure_audit`／`punct_audit`＋共享库 `axis_lib`＋编排器 `qchain`；数据表 `units.json`、`ja-loanwords.json`、`register-lexicon.json`、`punct-rules.json`。全部“机检为筛、人审为判”，逻辑骨架只登记可判项。
* **规则落地**：ADR-0079（四件套齐）；`rules/02` 标点判据归 q6；`rules/03` 和制汉语三分类；`rules/04` 六工序位次与五条顺序依赖；`rules/05/tools.md` 九行工具；`rules/07` 引文管理扩全语种；`rules/README` 标准清单增 ISO 5060:2024／690:2021／24229／80000-1:2022／SI 9／ISO 24617-8、-11、-12；`axioms.json` P29–P33；`journal-schema` 节点计数同步 22。
* **摸底**：全库 2417 个 yuanwen 文件，成句引文 34450 片段，确定非英文 314（0.91%，拉丁 161／德 79／希腊 34／法 20／汉 17）；术语级片段约 1.27 万。引文规范由“一律补原文”改为“判原著语种与原文可得性，verifiable 补、unavailable 不代造”。
* **公理化验证**：`specs/060/bin/verify_six_axis.py` 四组计算——A 结构公理（单链、q 位次、判据唯一、强制集、三处同步、回退合法，19 项违例 0）；B 覆盖完备（CY/T 266 29/29：机检 23、人审 4、豁免 2，缺口 0；MQM 7/7；判据 73 条）；C 一致性（多器同位置 100% 落入预登记分工对，待复核 0；幂等 7 指标全过）；D 假设登记（H-1…H-5 不可判项显式列出，不伪证）。定理 T1–T7 与五条顺序依赖反例见 `specs/060/verification.md`。
* **验证**：`unittest discover` 590 项全绿（新增 `test_six_axis.py` 12 项，`test_task_ops.py` 适配 q 链）；`check_stages` 13 项全绿；`check_doc_size`／`check_junk`／`spec_index` 绿。
* **试金石**（三件：adorno／abduction／aesthetics-existentialist）：清单 137/597/78/1/85/72、45/394/1/3/7/6、39/436/130/0/95/37（q1/q2/q3/q4/q5/q6）；门禁实拦 586／191／364 条。暴露 q2 逐句人审不可行（386 小时/件），已加“非逻辑句 trivial”通道（无强算子且分句 <4），待裁定降至 138/597、156/394、123/436；人工估算 149–253／47–78／88–163 小时。G4 anchor 自动对齐、G5/G6 误报排除列 T1 前置。
* **事故与自愈**：并行会话 1d85345ff（058 批 9）收编本批 trial.py／trial.md／verification.md／verify_six_axis.py，提交信息与内容不符（历史事实，禁 force 不追改）；8f9201a82 漏 add `journal_lib.py`／`task_ops.py`，已补提并推送，单测 591 绿。
* **S6 对象域双登记落地**（同日用户批准）：criteria_domain 24 条＋多判据节点 object_class；check_stages 增 S6 两谓词（16 项全绿）；归并探针由"13/13 全绿"转为"16 项失败 1"，归并从此可检。连带：R1/R2 判据由自然语言正名为 review-verity／review-coherence，承载体登记 kind=manual（S6 首轮即暴露）；P29 check.ref 改 [S2,S6]；单测 593 绿。
* **遗留**：T0 全库六轴摸底、试金石 3 件、A–Z 存量回炉（T1/T2）；语域样章与逻辑骨架金样本待用户裁定后入库。


## 2026-11-25/26 阶段 1.2 独立复核＋缺口族根因收口（specs/062 复核、specs/053 第四十五／四十六批）

* **独立复核（ADR-0039）**：阶段 1.2 实质数字全部复算成立；订正文档数字 2 处（text 66→65、资产口径）、修复图钉摘除 3 件（upsert_baseline 整体替换 files[] 的缺陷，改并集保留＋registered_orphans 补登）、旧池 judge 凭证补齐（1780/48/45 复现）、SVG 归图片资产（用户裁定：sha 变了随钉替换）。报告 `specs/062-phase12-recheck/results/phase12-review.md`。
* **B 族账本随 en/ 刷新（第四十四批）**：40 件假阳性 gap 根因是版面账/结构账冻结于抓取前（版权年滚动＋改名波纹）；`--rebuild-b3` 入 SOP。
* **缺口族根因收口（第四十五批）**：`gap_probe.py` 增 `fail_block()`（复演池吞并算法）逐件定真因；20 件缺口清至 2 件。真根因全是**上游 HTML 不规范写法**：空 `<li>`（账记 `e:1`，渲染禁兜底占位）、未闭合 `<dt>/<dd>`（`_close_dl_optional_end`）、末格省 `</td>`（按开标签切格）、大写 `<LI>`（li/ul 匹配一律 `re.I`）、URL 不平衡括号（RFC 3986 编码）；另修文字型注释链丢词（56 条保留 md 内链）、学术工具表 4 行上限（truth-correspondence 第 5 行）、引块表被 `<br>` 行标记撕行（`_split_br_lines` 容器配平）、supsub 样式 span 相邻星歧义（提前剥壳）、列表标记位挂链接（`mk` 保护含 `>` 前缀）、TOC 悬置首段（`toc_block` 尾携＋两侧去重）。**pool 1,853→1,871／gap 20→2／B3.1 1,663→1,665（0 转红）**。执行账超 100 KB，按 ADR-0004 拆分为 `execution-log/` 七卷日期文件＋index。
* **logic-intensional 收口（第四十六批，2026-11-26）**：裸排环境体内嵌 `\(…\)` 二次清扫改保持字面（占位序不变量成立，账驱动属冗余；全库对照证明真受影响面仅 1 件——pattern 计数会虚报 20 倍）。**终态 pool 1,872／gap 1（augustine＝勘误 §十二上游结构例外）／stale 0、池占页 52.08%；B3.1 1,665／208；I2 1873/0；check_all 21 门全绿**；两批均已提交推送、CI 门禁矩阵绿。
* **方法沉淀**：判 gap 必须复演池判据（首失配多是漂移噪声）；改 C 后标准陪跑＝旧模块全库对照→按改动清单重转→账增量刷→全量三步验收“pool 只增不减、B3.1 无新红”；放宽正则先做反例试金石（`\s*` 一字之差曾破 265 件 B3.1，靠 aristotle/nietzsche 抽样拦下）。
* **augustine 补丁出口收口（第四十七批，2026-11-26）**：末件结构错位（`<h4>Spanish</h4>` 误嵌空 `<li>`，四节同构破坏）经 **P-005**（格式层·结构错位，单行 find/replace，准入＝tag）正形化；`article_ledger` 接入补丁视图（账与 C 同一 en 视图，失配硬失败）；勘误 §十二该行改记补丁出口。**终态：B3.2 pool 1,873／gap 0／stale 0（页面级闭合 100%，池占页 52.16%）**；B3.1 1,665／208 集合零变；check_en_patches 5 条全绿；check_all 21 门全绿。四出口“例外”应是终态评审而非停车场——机制成熟后旧例外要重审。

## 2026-11-26 书目区再生标题收口（specs/053 第四十八批）

* **缺陷**：H0 有 `<h2>Bibliography</h2>` 内又嵌 `<h3>References</h3>` 的件，C 对每个命中 `references|bibliography` 的标题各再生“标题＋固定注”，md 因此有两个 `References（引用注释）` 与两条固定注；R 把嵌套标题当普通标题原样发，C 第二遍不再认，固定注行的 `[^key]` 字面被行内渲染吃掉——B3.1 破 8 件同族。
* **修法（纯 R）**：区内嵌套标题发可被 C 命中的原文标题 `<hN>References</hN>`；固定注一律不搬运；定义 ul 随即就地发（嵌套标题把 C 的 `bib_lvl` 提到同级，其后同级小节标题会终止书目区）。md 与 en/ 零翻动。
* **实测**：208 件残差闭合 20 件；全量三链 **B3.1 1,665→1,685（0 转红）／B3.2 pool 1,873／gap 0／stale 0、池占页 52.16%**；新增 `tools/tests/test_reassemble.py` 2 项；122 件子集先验 pool 122／gap 0。
* **否证记录（同批，不计入）**：A（求值视图建键不继承前条姓氏）修 adorno 型键名漂移但砍断 130 件赖以成立的同小节继承（消融 40 件 0/40）；A′（定义 ul 按小节分槽＋`<ul>` 边界计小节切换）原型键差 0、全量 1,763（+98）但 6 件旧绿转红（同姓多小节／author-less 小节指针误推进）；B（书目粗体键行发 `<dl>`）修 13 件但装配层按账 `bib_seq` 重排与 R 的 dl 撞车，5 件 `unaligned text units` 转 gap。**结论**：B3.1 与 B3.2 对同一结构可能偏好相反，R 侧单改必须两侧同验（子集 build 先行）；md 文末扁平定义列表不含小节条目数，键名复位点不可从 md 唯一反推，属信息损失而非规则缺陷。
## 2026-11-26 建键去小节依赖（specs/053 第五十批）

* **裁定前提**：用户指出“不存在任何译稿”——译稿清零（ADR-0081/0082）后 md 重转与键名重排零风险，故“账域”不必让判官吃账，应消解为规则域；先拿最大族书目键名。
* **修 A（section_free，默认开）**：年份起首且无姓可扫的文献条目不再向小节标题（`_section_author`）／前条姓氏（`prev_surnames`）推断作者，一律 slug 兜底；`–––` 续行仍继承。构建期与求值期同规则，键名可由 md 确定性复算。**B3.1 1,685→1,792（+107，0 转红）**；250 个 md 变更（3641+/3451−）；B3.2 pool 1,872／gap 1／stale 0（池占页 52.13%）。
* **修 B 否证（不计入）**：全量重转唤醒 HEAD 里的陈旧 md（HEAD 版转换器复现同件输出与新版一致），暴露书目区引导句被收编为伪键（`among-1982`）。普查 24 件 31 段全是 “…as follows:” 式导语。试修“以冒号收尾的段落落段”单件立即复原（pool 78,087 B 同 HEAD），但全量 **B3.2 gap 1→22**（22 件全为引导句件），B3.1 中性。定因：装配按账 `bib_seq` 定位书目单元，引导句段落身份不在账里，落段即与 H0 导语→列表次序脱钩（clauberg 判例）。整体回退，正确出口是**账/装配同改**（书目区 `<p>` 入账），与第四十九批 B 方案结论同源。
* **残差结构**：188→81 件；bib-keys 122→24、blank 26→14、text 33→36、note-forms 3、links 4；账域 68.6%→38.3%，最大族让位给 text 36（长尾微缺陷，每族 1–3 件）。
* **教训**：①全库重转前须预期“陈旧件被唤醒”——B3.2 复扫要逐件核 gap 名单，不能只看总数；②规则改对与页面装配可相反：B3.1 中性／单件 B3.2 转好，全量仍可大退，必须两侧同验；③22 件 gap 与 24 件命中件几乎重合，是因果链干净的强证据（否证比论证更省时）。
* **事故登记**：本批暂存被并行会话同树提交 `ae7b9f4a2`（信息为“064 rev16 待执行排程”）一并提交并推送，提交信息与内容不符；按禁 force 不改写历史，已核入库内容为本批最终版。教训：暂存与提交要连续完成，勿跨调用留窗口。
## 2026-11-26 书目导语落段＋账同步刷新（specs/053 第五十一批）

* **缺陷**：书目区引导句（“…can be found in Quine 1982 and in:”）是散文，含四位年份（句中引用），旧规则把书目区内含年份的 `<p>` 一律收进条目流，产出伪键 `[^among-1982]`（首词当姓）。普查 24 件 31 段，全部是 “…as follows:” 式导语，其后必跟列表。
* **修法**：C 侧以冒号收尾的段落落段不建键；**账侧同批刷新**（`article_ledger.py --slugs`）——`bib_seq` 该单元由 `pd`（定义项）切换为 `p`（散文段）。
* **首轮失败的教训（第五十批修 B）**：当时只重转 md、没刷账，旧账按 `pd` 定位导语，装配与 H0 的导语→列表次序脱钩 → 22 件 `unaligned text units`。据此误判为“账/装配同改”的大工程；实际 `extract_bib_seq` 的 else 分支早已支持 `<p>` 单元（按 `md_prose` 定序记 `["p", idx]`），只需账随 md 刷新。
* **实测**：25 件重转＋刷账后逐件 build **全部 pool／gap 0**，池值与 HEAD 逐值同量（augustine 192,309 B、burke 53,147 B、clauberg 69,607 B、cohen 46,066 B、logic-propositional 78,087 B），伪键消失而补集池不增（T7 验证力不降）。全库重转仅 23 件 md 变更（全部落在已刷账 25 件内；gangesa／ibn-rushd 导语无四位年份，C 不触发）。B3.1 **1,792→1,792（±0，转红 0）**；B3.2 **pool 1,873／gap 0／stale 0**。
* **纪律沉淀**：①凡改 C 使 md 的段落/定义归属变化，**必须同批刷账**（`--slugs` 增量合并，账冻结只改指定件）；②单件集群先验（25 件 3 分钟）再全量，比全量三轮省时；③“gap 全落在一个已知特征集”时先查“该特征对应的账字段是否随 md 刷新”，不要急着判成架构级改动。

## 2026-11-26 B3.1 残差 R 侧规则族第一波（specs/053 第五十二批）

* **治理前提**：用户 2026-11-26 裁定本轮豁免 ADR-0034，批准滚动至多 12 路**只读**子代理做残差分族与修法调研；写入、验证、提交仍由主代理完成，期间 git status 持续核对无越界写入。
* **分族**：12 路只读代理（text 36 全型／blank 14／bib-keys 24 两半／note-forms＋links 7／表格／引块／大写链接／强调／上下标／图片／blank 判据）＋主代理独立取证交叉验证；两侧在“件数、代码位置、责任侧”上一致（text 36：R 侧 35／C 侧 1）。
* **本波修 5 处 R 规则（md 零翻动）**：①`_link` 的 m3 段字符类补大写与下划线（`set-theory.ZF.md`／`frege-theorem.Gl-Hume.md`／`mohist-canons.B73.md`／`church.supplementB.md`／`spacetime-holearg.leibniz_equivalence.md` 此前丢链接）；②表格分隔行判据加“必须含 `-`”（纯空单元格行不再被当分隔行吞）；③资产路径 slug 补大写（`physics-Rpcc`／`statphys-Boltzmann` 图丢失）；④无分隔行＝字面段落（Related Entries 单行形 3 件）；⑤列表项多块（内嵌表＋续文本，4 件）。
* **实测**：**B3.1 1,792→1,815（+23，转红 0）**；B3.2 **pool 1,873／gap 0／stale 0**、池 **123,155,454 B**（较上批 −7,838 B，规则吸收更多、T7 验证力提升）、占页 52.16%；残差 58 件：bib-keys 24／text 17／blank 14／note-forms 3（links 4 全清）。
* **遗留**：引块空行游程 8 件（三种形态：前导/尾随 `<br>`、连续空行、行首空格；HTML 无法编码游程，需 C 侧归一或账承载）；上下标字形 4 件（R 需对 `_{}`/`^{}` 的 ASCII 内文写实体）；强调/三星/行首编号转义各 1；blank 14；bib-keys 24；note-forms 3。
* **教训**：①R 侧“丢结构”类缺陷可用单点正则批量收口（5 处改动收 23 件），但必须两侧同验（B3.1＋B3.2 抽样）；②代理与主代理并行取证互补：代理补出图片丢失、三星嵌套、无分隔行三型，主代理先验出空单元格行与列表内表；③12 路只读代理多处长时间停滞（无进展 15 分钟以上），产出未达预期，关键结论均由主代理自行复算。
