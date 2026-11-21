# 日志与编辑规划


> 本日志按 ADR-0004 分卷：卷一（2026-11-15 及以前）见 [日志卷一](ri-zhi-yu-bian-ji-gui-hua-1.md)，卷二（2026-11-16 至 11-20）见 [日志卷二](ri-zhi-yu-bian-ji-gui-hua-2.md)；本页为卷三（2026-11-21 起）。

# 项目日志（卷三：2026-11-21 起）

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

## 2026-11-22 遗留问题处置（用户指令“解决遗留问题”，specs/055 收口）

* **误报改判与根因修复**：见上条改判注；`build_mapping.py` en_key 双规则（跳全角注记段＋作者段括号平衡截断）＋`bin/test_en_key.py` 九例回归全过；对 00ee29e44^ 重放全管线，mapping.tsv 仅 4 行 en_key 归正（kochen-specker/social-procedures/logic-provability/feminism-objectification），写回净增量 1 行移位，mulu-map 重建 G1–G4 全绿。
* **共用工作树 checkout 误收事故（登记）**：重放用 `git checkout 00ee29e44^ -- mu-lu-s.md` 污染暂存区，被并行会话 s25 提交（ca31f15d8）扫入，分支 mu-lu-s 一度回退、G3 变红；原子修复提交 6e701789b 恢复新结构＋mulu-map 同步，已推送复绿。防线登记：共用工作树禁按路径 checkout 旧版，重放一律临时 worktree；已补录并行危害记忆。
* **门禁分工**：本线 mulu_s 五项＋catalog-net G1–G4 全绿；`check_all` 仅 `管线单元测试` 一红——系并行会话 specs/053 线在途 `tools/yuanwen.py` 转换器改动（test_em_with_trailing_star_escaped），由其线收口，本线不越权。
* **PROGRESS 阻塞 2 件核实**（haecceitism/hamann 逐段对齐未配对）：属翻译战役待派工项（两件均为仅标题骨架、未开工），非清理类可解项，维持登记不动。

## 2026-11-21 人名表逐行研判全表收官（specs/013，用户指令“所有无法判断的和已经判断的术语，人名都必须逐个结合不同原文研判”）

* **终态**：4,594 行（26 张简报 s01–s26）逐行显式判定收官，判定台账零缺；凭证账 1,117 行；缺项告警 2,696 → 924（余量为合规留空，非漏判）。26 批每批覆盖核对＋写回＋对账＋推送，`origin/main..main` 恒零。
* **取证道**：简报（原典语境＋GND／WD 候选）→ marks 全行判定（KEEP/FILL/FIX/NOSOURCE，note 留痕）→ marks_to_ledger（--check＋再生）→ apply_person_meta 写回第 4/5/7/8 列 → check_terms 汇总对账。DEFER 定点补查五轮（wd_defer.py，130 键，约 40 键转 FILL）。
* **误配防线战果**：机采误配改判 13 件（林奈／Partee／Arthur Pap／Boyd／Price／Porzio／A. G. Walker／王莽／Eric Williams／左拉／扬雄／Searle／Hippolytus），拒绝误配 20 余件（建筑师／卡巴莱艺人／足球员／昆虫学家／贵族谱系库等）；日期错列族 15 件归正（权日身／白颐正／白文宝／朴世堂／愼後聃／李齐贤／李穑／朝鲜太祖／尹鑴／李kan／李震相／李恒老／李檗／李睟光／李承薰，凭韩国学典八条目＋WD）；混指键 13 族登记拆键队列（Leland／Cosimo／Crates／Nicholas V／Philip II／Pythodorus／Radcliff／Sotion／Vacca／Wimsatt／Sherman 伪人等）。明细见 specs/013 execution-log 2026-11-21 节。
* **管线修正**：marks_to_ledger 三处（defer 载序最后载入——修正五轮补查静默失效的关键 bug；nat/life 缺列回退现值防误抹；expand_src 进凭证行）；check_coverage.py 新增；fix_quotes.py 全库引号清洗 10,258 处。
* **门禁**：本线范围 16/17 绿；唯一红项“管线单元测试”系并行会话 specs/053 线在途 tools/yuanwen.py 改动（test_em_with_trailing_star_escaped），非本线产物，由其线收口。
* **事故对账（与 specs/055 线互相印证）**：s25 提交（ca31f15d8）扫入并行会话经 checkout 污染的暂存 mu-lu-s.md——我侧系 git commit 未带 pathspec 卷入整个暂存区；对方已于 6e701789b 原子修复并复绿。防线登记：共用工作树提交一律 `git commit -- <路径>`（只提交指定路径，无视暂存区残留），checkout 旧版一律临时 worktree。
* **下步**：术语表 r02–r31 逐行研判（约 6,100 行）＋待处置队列（拆键 13 族／键形全角 84／撞形 538）。

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

## 2026-11-21 术语线开工（specs/008 全表 6,109 行，继续“逐个结合不同原文研判”指令）

* **机制**：r 系简报（r01–r31，每张 200 条）→ marks（default＝KEEP，仅非 KEEP 键显式落记）→ term_marks_audit.py 汇总 per-line-adjudication 台账（含 s 系已判 1,054 行＋m 系专项件）→ 每批 pathspec 提交推送。已判 r01（KEEP 193／FLAG 7）、r02（KEEP 193／FLAG 6／FIX 1：Curry-Howard 连接号按 ADR-0041 改一字线）。
* **管线修正**：收集器载序改 s→m→r（r 系全量复判最后载入，显式判定权威胜出；修正前字母序 s 后载会压 r）。
* **竞态变体登记（自首）**：r03 批次我的收集器写盘撞并行会话文件锁报 OSError（Errno 22），但我未核实即 add+commit，把并行会话的台账再生＋note 改写（443/443）扫进我的提交（d7fb7e177），信息未提对方改动——内容零丢失（r03 七 FLAG 经对方再生入账），提交信息失实，以本条自首。防线：收集器/生成器跑完先验输出增量与行数再提交；写盘失败＝工作区可能已是对方再生版本，须 `git diff` 取证归属再动作。

## 2026-11-22 mu-lu-s 空壳骨架缺陷修复与大小类对照（用户指令“你变动了哪些大小类目录，列出来比较”）

* **缺陷披露**：用户索要大小类对照，对照脚本（compare_headings.py）反检出 00ee29e44 起 mu-lu-s.md 混入**旧四区空壳骨架 138 节**（世界哲学（欧洲以外）／科学哲学／哲学通论整树空标题＋西史内犹太哲学旧位等），与新六区 populated 树并存——build_mapping 旧标题路径整树播种缺陷所致；check_mulu_s（只验链接行）与 G3（自洽重放）均不拦，此前“结构正确”的汇报不成立，如实更正。
* **修复链**：①播种移除，纯父节改由条目路径祖先合成；②序键两连修——合成节点码点序乱序改“子树最小首现序”（文档序回归）、节注 setdefault 伪实节点改按“有无直接条目”判定；③根层显式 H1 序（前言/关于/西史/传统/形上认识论/价值理论/科学逻辑数学）；④check_mulu_s 增第 6 项**空节硬拦**（旧版基线 0 空节验证安全，rules/05/tools.md 同步）；⑤对照脚本补子树全枚举。
* **重放纪律**：旧版输入走 `git show > results/快照副本`＋build_mapping argv 传参（共用工作树 checkout 禁令执行）；write_mulus --apply 守恒 1883 进=出；check_mulu_s 六项全绿（空节 0）；mulu-map 重建 G1–G4 全绿；**保序审计**：26 个保留父节中 9 处子序差异恰为 NODE_ORDER 批准的重要性重排（古代希腊居首、康德黑格尔居前等），其余全数文档序保持。
* **对照结论**（heading-diff.txt 入库）：旧 250 节点 → 新 251 节点＝保留 112＋迁移 127＋撤销 11＋新设 12；撤销↔新设对应：世界哲学（欧洲以外）→哲学传统、科学哲学→科学、逻辑与数学、哲学通论→形而上学与认识论＋价值理论、伦理学解散四升三迁、语言哲学与逻辑学拆分、政治哲学→政治与社会哲学、女性主义哲学→性别种族性、物理/生物/认知/信息四学科改名。

## 2026-11-22 分类体系定案维持（用户指令“除了西方哲学史必须保留…先查询再问我”＋修订“西史允许内部分类修订”）

* **六源检索**：PhilPapers 七类（Arabic-Islamic 挂 Asian 内）／IEP 四轴（科学哲学挂 M&E、逻辑数学与伦理同域）／REP 主题·地区·时期·宗教四轴／LCC B 类（BC 逻辑·BH 美学·BJ 伦理·BL-BP 宗教独立）／人大复印 B1–B9（逻辑·美学·宗教·科技哲学独立）／大百科“史＋分支”二分。
* **四问裁定（全选推荐项）**：顶层维持六区（甲）；西史区名保留＋内部断代制维持；逻辑维持科学、逻辑与数学内；宗教哲学维持形上认识论内、传统区维持八区域平列；元哲学不增设（M&E Misc 13 条就近安放，PP 杂类两区本库不设）。
* **落点**：specs/055 spec §Assumptions 定案登记；mu-lu-s.md 零改动；现行体系经六源比对后维持原判。

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

## 2026-11-22 人名表 CJK 全量复核（用户指令“继续复核 summary 条目的中日韩人名，以及全量复核人名表整体”）

* **SUMMARY 条目侧**：SUMMARY 里以人名为条目名的中日韩条目共 12 个（孔子、老子、庄子、荀子、朱熹、王阳明、戴震、空海、西田几多郎、和辻哲郎、日常美学之斋藤百合子，及诸“见……”别名行），条目定名逐一与人名表译法对账一致；人名表→SUMMARY 无漂移。
* **CJK 行全量**：按籍属筛出中日韩台（含高丽）行 224 条逐行过目，并以既有凭证（韩国学典／Wikidata／GND／上游自带汉字）核底；源文回读确认 SEP 词条全文罗马化、不含汉字，汉字回译只能靠外部权威，无“原文对照”可走。
* **实体修复 8 行**（凭证 `specs/013-person-attribution/results/cjk-review-2026-11-22.tsv`）：Morrison, Robert 身份正列——首现实为 Isis 105（2014）论文作者 Robert G. Morrison（b. 1969，鲍登学院，伊斯兰天文学史；exa 凭证 uchicago doi／Bowdoin 官网页），原行误并 1782–1834 年来华传教士马礼逊（GND 119420953），改“保留英文＋美国／科学史＋1969–”（ADR-0022）；Ichikawa Kon 市川昆→市川崑（官方网页用字）；Huan Tan 生卒 fl. 2023→前43–28（SEP 原文 43 BCE–28 CE）；Liu Bei 0161–0223→161–223；Murasaki Shikibu 0978–1016→978–1016（零填充格式归一）；Bodhidharma 籍属 中国→印度（南天竺）／中国（来华僧）（SEP“an Indian monk”）；Paek Munbo 依据换源（撤不合格引用，改韩国学典 E0022117＋人物综合库）；Parreut, John 列位移正列并补首现。
* **机检复扫**：person_review_flags 全表 4,594 行——flagged 0（上一轮 2 项已修）、重复组 0、保留英文形 41；缺籍属／生卒 924 为既存欠账（668 缺两项／60 缺籍属／196 缺生卒）。
* **欠账清偿开线**：`person-missing.txt` 924 键的 GND（lobid）批量取证已在后台续跑（`gnd-raw-2026-11-20.jsonl` 逐键候选＋断点，礼貌间隔 5s）；判定器 `gnd_adjudicate.py` 已备（严谓词：Person 型＋同名严格＋生卒不矛盾，同名多候选一律降存疑；古人生卒纪元码不自动填），吸取 Huan Tan 误并教训，自动接受名单仍须人工过目后才写回。

## 2026-11-21 EN 逆向装配第六批：C 侧转义改造与结构化强调（用户“1”批准 C 侧专项后落地，续作至 11-22）

* **路线反转**：接五批“star 三轮回退”结论，判据试错的终点是语义层——R 侧形态试探三轮不收敛，根因在 C 侧有损（md 里字面 `*`／`$` 与强调定界符、数学定界符不可区分；嵌套强调 strong 套 em 679 处/77 件、em 套 strong 81/38、em 套 em 255/82 在旧四条单层正则下整块丢失）。本批先改产生方再改判下方。
* **C 侧**（tools/yuanwen.py）：文本层全转义（`\`→`\\`、`*`→`\*`、`$`→`\$`，单射）；`_emph_tags_to_md` 栈式单趟取代四条正则（同类嵌套压平、异类照发、空白外移含 `&nbsp;`/U+2028、缺闭合回删、跨 `<br>` 引块行不发表、相邻同类合并）；数学体美元转义（行内全转、显示只转边缘）、空公式 `\(\)` 不产 `$$`、裸排环境先暂存后补 `$$`、希腊字母在斜体内出裸字符。
* **R 侧**（specs/053 bin/reassemble.py）：`_star_parse` 改 run 逐星消费（整 run 全作开星优先→按 slot 最内层先闭），撤 `_intra_word_open` 与全部形态试探；code 段占位；`\$`/`\*`/`\\`/`\#` 占位还原；数学改扫描式占位（显示体允许成对单美元）；记号星占位撤除（吞合法闭星）。
* **检查器配套**：fidelity `strip_math_ex` 增 `dollars=False`（html 侧裸 `$` 恒字面，全库 728 处/105 件皆币值）；作者行剔除限 count=1（berlin 图注整行 em 恢复后被误删判例）。
* **实测**：B3.1 **1,452→1,569/1,873（83.8%），集合级 0 退化**（转绿 117／转红 0）；B3.2 建池 **1,274→1,359（72.6%）／缺口 514／stale 0**，池占页 31.79%→34.70%（T7 如实同报）；I2/I3 门禁 1,873 全过 0 issue，深比对软信号 305（基线 322）。全量重转七轮（含 entries.json sha 登记同步），中间轮次 1,467→1,521→1,562→1,551（反斜杠转义引入 17 件转红，补 `\\` 还原后恢复）→1,569。
* **教训**：①“顺手修一处”必须全库复跑——第 4 轮反斜杠转义一次性引入 17 件转红，靠集合级对照当场定位；②嵌套强调的正确表示是栈不是更强的正则；md 扁平形态表达不了的结构宁可压平／不发表并交池补，也不产歧义星流；③检查器与转换器必须同批改，字段语义变化不同步对称面就整批假阳性。

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

## 2026-11-22 人名缺项再清：回读原文括注 41 条＋GND→Wikidata P227 桥 6 条（缺项 922→881）

* **通道甲（原文括注，零信任回源）**：按“首现”逐条读 en/<slug>/index.html，抽 “Name (生卒)” 紧括号式；只认含间隔号或带 c./d./b./fl. 标记者（单裸年几乎都是出版年，“Name (2005) … 111–120” 一类书目页码串占首版假阳性绝大多数）。逐条过目后写 35 条、弃 4（David／Hippo／Moses／Shakespeare 命中皆同名异人：Hartley 之子、Augustine of Hippo、《提本》之子、Schlegel 译事年代）。
* **正则修正**：助词分支 `\s+of\s+` 未接本体，导致 “Dietrich of Freiberg (…)”“Alexander of Aphrodisias (…)” 整串失配、退化为只抓末词；补上助词后本体落位，另放行 “1240/1250–1318/1320” 式斜杠年。第二批新增 6 条（Alexander of Aphrodisias fl. 约200／Dietrich 约1250–1310／Electress Sophie 1630–1714／Nicholas of Otranto –1235／Siger of Courtrai 约1280–1341／Zeno (of Citium) 前335–前263），弃 1（Solomon 命中的是 Ibn Gabirol）。合计 41 条，缺生卒 855→814。
* **通道乙（P227 桥）**：GND 已按规范名等值锚定、惟规范档无年份的 121 键，以 haswbstatement:P227=<gndId> 反查 Wikidata，取同一实体生卒。准入四闸：恰一命中／精度不低于年／生卒不同值（剔除活跃期代理）／职业不涉可疑族。判定：接受 9／存疑 30／查无 82。
* **接受集逐条再核（本人履历与双向国别栏）**：Matthen（本人 CV“Born Bangalore, India on 2nd April, 1948… Citizen of Canada”）、Solère（IdRef 069192642：1960，法国，CNRS）、Melia（fr.wikipedia 1935／英国籍）、Forsythe（维基：美国实验经济学家）、Squatrito（1979，与其 LSE 履历 2001 年本科毕业相符）、Song Xing（宋钘 前370–前291）。拒 3：Batterman（Q89298775 记 1900，与本行所引当代物理哲学家不合，疑 GND 并档）、Meskin（ORCID 自动条目同挂 1950 与 1934）、Platek（描述 Canadian statistician，与递归论学者不符）。
* **写回**：生卒 6＋籍属 4（Matthen 加拿大（生于班加罗尔）／Solère 法国／Forsythe 美国／Melia 英国）。缺生卒 814→811，缺籍属 727→723，任一缺 922→881。门禁 check_all 17 项全绿。
* **负结果（判为不可自动化）**：①“<国别形容词> philosopher <人名>”同位语全库仅 1 处可得（hegel 的 Klaus Hartmann），通道作废；②GND 等值多候选细分筛 116 键只出 18 条，逐看 10 条是泛名单词、其余职业明显不合，机械收窄不可采；③剩余 811 条中 92 条依据已注明“现代学者”（在世或当代，生卒本无），其余多为当代学者与无规范档的古代小人物。
* **教训**：①正则助词分支必须自带本体，否则整串退化为只抓末词；②单裸年、斜杠年、fl. 三种式样须分别判；③规范库并档会把错年份带进 P227 桥，故身份闸之外还必须看人的描述，接受集一律逐条过目。
