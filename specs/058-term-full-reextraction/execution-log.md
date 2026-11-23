# specs/058 执行记录

> 一段一节，按时间倒序追加。行内只记事实与凭证，不记进度叙事。

## 2026-11-22 会话（specs/058 启动）

* 开工核对：`git log` 基点 1d4767584；`git fetch` 后 origin/main 与本地一致（0 落后 0 领先）。工作区含其他会话在途改动 121 件（baseline patches、specs/001/053、tasks/term-pool.json 等），本规格不触碰。
* 误触发说明：本会话早先以 `--help` 调 `tools/term_harvest.py`（该工具无 --help），实际执行了一次全库增量收割：池 +103 候选、来源/频次随新语料漂移，状态零变更（与 HEAD 逐条比对，published/held/rejected 全部保持）。该产物保留（与全库重提目标一致），未回滚。
* 联网调研：见 `results/research-evidence-2026-11-22.md`。通道事实：DDG/Brave/Mojeek/Bing/百度均被反爬拦截；维基 API 与 OpenAlex/Crossref API 经代理 192.168.5.4:7890 可用；SEP 官网 `/translations*` 均 404，未找到官方翻译项目页面，不作为依据引用。
* 立项：`spec.md`（方向、口径、方法、验收）＋调研凭证。
* 提取器：`bin/reextract.py`（新增规格内高精度分型提取器，复用 `tools/term_harvest` 守卫常量，不另造判定）。
* 首轮全量（约 13:40）：2,998,178 键，保留 224,813，短语低频尾 2,774,365 不入总表。抽查发现三类缺陷：斜体噪声（et al/Figure/priori 残片）、机构与题名误判人名（Oxford University Press/Vienna Circle/Anomalous Monism）、合并后展示形取错类型。
* 修正：① NOISE_TERM 黑名单 26 词；② 人名路线 ORG_WORDS／DEMONYM／NONPERSON_TAIL 三重过滤＋尾词修剪；③ 展示形按类型优先级更新（person>work>term>sentence>foreign>topic>script）；④ 句级引语路线独立清洗（clean_sentence，2–300 字符，拒收标记与编号残片）；⑤ 产物收缩：原始档落 `script/tmp/candidates-full.json`（本地），入库档 `results/candidates.json.gz`（gzip 压缩，防 64MB JSON 进库）。
* 二轮全量（后台）：修正后重跑，产出 `results/az/A–Z/#.tsv` ＋ `results/summary.md` ＋ gz 索引。最终计数：语料 2418 篇，原始键 3,011,396，保留 260,526，低频短语尾 2,774,918 不入总表；类型：phrase 97,935／term 69,824／sentence 45,970／person 21,986／foreign 15,239／work 4,701／topic 3,113／cjk 1,256／arabic 468／greek 99。
* 状态刷新后：已登记 5,340／池内 54,402（new）＋ 2,162（其余裁定）／本轮新增 198,622（主要是句级长词条与池外低频项）。
* 总表格式改 TSV：Markdown 单字母文件超过 ADR-0004 的 1000 行/100 KB 阈值，`check_doc_size` 判红；改为每字母一份 TSV（生成物，数据表语义）＋ `az/README.md` 索引，复跑门禁转绿。
* 首批落册（batch1）：从评审表人工圈定 140 条高置信术语，经审定库 JWT 直连查证（112 条实查，111 ok／1 empty／28 已有凭证跳过）；人工逐条定译后，剔除合写键重复 3 条，实登记 102 条（22 条依据为审定名词库命中，80 条为教科书级标准术语 A 档直裁并注明审定库未采原因）。`term_flow` 干跑 102／0 跳过，实写后 `registry_azsort --apply` 守恒（术语表 7,103 行），`check_terms` 硬错误 0，`check_all` 17 项全绿。
* 产物：`tasks/manifests/2026-11-22-058-batch1.json`（裁定清单）、`results/curated-translations.tsv`（人工译法）、`results/rowspec-batch1.json`（机器清单）、`results/register-queue-{terms,persons,works}.json`（后续批次队列）。
* 开放项：
  1. 人名 21,986 条、著作 4,701 条只入总表，未落册；`register-queue-persons.json`／`register-queue-works.json` 已生成，需逐条核籍属/生卒与中译本，works 队列当前混入术语（feminist ethics／informal logic 类），下批须先分型。
  2. 本轮新增 198,622 条中，句级长词条 45,970 条多为引文，不属登记对象；其余按 T1/T2 逐批裁定。
  3. `candidates.json.gz`（8 MB，机器索引）未入库，保留在 `results/` 本地；全量 TSV 已入库。

## 2026-11-22 续：术语在线优先（用户裁定）

* 口径变更：登记一律先查审定名词库（allSearch），命中学科对口即采审定译名；查无或仅他义命中才走 A 档直裁，并写明原因。`termonline-standard` 实测为模糊检索（多词查询返回电力标准等无关命中），降为参考，不作优先通道。
* 首批依据复核：对 102 条逐条按“英文形一致或单复数变体＋学科对口”重扫凭证，14 条译名一致的命中升级依据为审定名词库（decision theory、moral beliefs、mental representations、field theory、artificial intelligence、cognitive processes、modal operators、moral values、inductive logic、machine learning、social structures、scientific progress、political economy、evolutionary biology），译名与日期不动。
* 首批未改采的审定异形命中及理由：perceptual experience 审定作“感性经验”（马克思主义语境，与知觉现象学非同概念）、moral agents 审定作“道德行为者”（语料通行“道德行动者”20 篇 vs 1 篇）、legal rights 审定作“法权”（马克思政治经济学义）、empirical research 审定作“经验性研究”（语料“经验研究”27 篇）、religious experience 审定作“宗教体验”（语料“宗教经验”10 篇）。
* 第二批：人工圈定 61 条，与总表求交得 59 条；全部先查审定库（48 条实查 ok、10 条已有凭证跳过）。按术语在线优先生成清单：5 条采审定译名（moral theories、number theory、empirical content、moral principle、logically equivalent→逻辑等值），54 条审定无对口命中后 A 档直裁。两条审定异形命中判定他义未采：physical theories→身体理论（自然辩证法·理论方法，身体义）、moral concepts→道德观念（医学伦理学，观念≠概念）。
* 落册：`term_flow` 干跑 59/0，实写 59；`registry_azsort --apply` 术语表 7161 行守恒；`check_terms` 硬错误 0。
* 当日累计：术语表新增 161 行（首批 102＋第二批 59），其中审定名词库依据 19 行。
* 第三批：人工圈定 52 条，全部先查审定库（44 实查 ok、8 已有凭证）。7 条采审定译名（译名与人工一致，含 Newtonian mechanics、ontological dependence、formal semantics 等），45 条审定无对口命中后 A 档直裁；无改采冲突。
* 著作名批次：7 部（Philosophical Investigations、Theory of Justice、Treatise of Human Nature、Principles of Philosophy、Politics、Laws、Summa theologiae），先查审定库——全部命中他义（公正／礼貌／水法规／外轮山等），判无对口条目；按 rules/03 §154 转权威译本档位登记：《哲学研究》《正义论》《人性论》《哲学原理》《政治学》《法律篇》《神学大全》。
* 落册：第三批 52＋著作 7，`term_flow` 干跑零跳过、实写 59；`registry_azsort` 术语表 7221 行守恒；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 当日累计：术语表新增 220 行（102＋59＋52＋7），审定名词库依据 40 行。
* 著作名第二批：26 部经典（Phenomenology of Spirit、Groundwork、City of God、Science of Logic、Word and Object、Languages of Art 等）。先逐部查审定库（26 部全部有凭证，命中均为他义：正商品／白皮病／字／艺术学科／冥想／下降／感觉 等），判无对口条目；按权威译本档位登记 26 行（去向见 `curated-works2.tsv` 的中译说明）。
* 人名队列诊断：修复人名合写键别名（“姓, 名 / 名 姓”双向、J. S. 缩写、van/von/della/ibn 粒子尾名），此前队列中的 Descartes、Husserl、Heidegger、Nietzsche、Mill、Kripke、Lewis、Marx 等经典人物实为已登记变体，不再重复入队。剩余真缺项以现代学者为主（Van Cleve、Della Rocca、Dutilh Novaes、Van Parijs、Van Gulick 等），按 ADR-0022 需逐条核籍属/生卒与通行汉名，留作专批。
* 落册：著作第二批 26 行；`registry_azsort` 术语表 7246 行守恒；`check_terms` 硬错误 0。
* 当日累计：术语表新增 246 行（102＋59＋52＋7＋26），审定名词库依据 40 行。
* 人名专批：合写键别名修正后再筛，确认真缺项 13 人：Isaiah Berlin、Simon Blackburn、Christine Korsgaard、Galen Strawson、Jonathan Dancy、Miranda Fricker、Joel Feinberg、Philippe Van Parijs、James Van Cleve、Michael Della Rocca、Catarina Dutilh Novaes、Ruth Barcan Marcus、Patrick Suppes。
* 取证：逐一查 Wikidata（经代理，限流退避；凭证 `results/people-wikidata-2026-11-22.tsv`），取 QID／生卒／国籍；Van Cleve、Della Rocca 无生卒数据，按“生卒未详”留空；Miranda Fricker 与已登记的 Elizabeth Fricker 为异人，分行登记。
* 落册：`term_flow` 干跑 13/0，实写 13；人名表 4558 行守恒；`check_terms` 硬错误 0。总表的状态判定同步支持人名合写键别名（`isaiah berlin` 等已标“已登记（人名表）”）。
* 当日累计：术语表 246 行；人名表 13 行。
* 人名第二批：再筛得 15 人：Tim van Gelder、Michiel van Lambalgen、Gideon Rosen、Stephen Darwall、Huw Price、Tommie Shelby、Jon Elster、Mark Schroeder、Brian Barry、Michael Tye、María Lugones、Russ Shafer-Landau、Paul Boghossian、Susan Wolf、Cecilia Martini Bonadeo。
* Anne Conway 在别名检查中被识别为已登记（“Conway, Lady Anne / 安妮·康威”），剔除；据此给人名别名加敬称剥离（lady/sir/saint/pope 等），防同类重收。
* 取证：Wikidata 逐人查（限流退避；凭证 `results/people-wikidata-2026-11-22-b2.tsv`）。Tim van Gelder 无生卒数据，留“—”；Mark Schroeder 首检命中篮球运动员，改查 Q93387536（1977–）。
* 落册：`term_flow` 干跑 15/0，实写 15；人名表 4573 数据行守恒；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 当日累计：术语表 246 行；人名表 28 行（13＋15）。
* 人名第三批：10 人：Julia Kristeva、Ludwig von Mises、Ernst Haeckel、公孙龙（Gongsun Long）、Ramon Llull、Ernst Mally、Philipp Frank、Patricia Hill Collins、Douglas Den Uyl、Stephen Davies。
* 取证：Wikidata 逐人查（限流退避；凭证 `results/people-wikidata-2026-11-22-b3.tsv`）。Stephen Davies 首检命中英国法官，改查 Q7609025（新西兰美学家，1950–）；公孙龙生卒取 Wikidata 前325／前250 约数，记“约前325–前250”。
* 落册：`term_flow` 干跑 10/0，实写 10；人名表 4583 数据行守恒；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 当日累计：术语表 246 行；人名表 38 行（13＋15＋10）。
* 著作名第三批：7 部：Port Royal Logic、Outlines of Pyrrhonism、Considerations on Representative Government、Lectures on Ethics、Book of Changes、Enquiry concerning Human Understanding、Thoughts Concerning Education。先查审定库（命中“图书／讲师／理解／教育思想”等他义），转权威译本登记：《波尔·罗亚尔逻辑》《皮浪主义纲要》《代议制政府》《伦理学讲座》《易经》《人类理解研究》《教育漫话》。
* 落册：`term_flow` 干跑 7/0，实写 7；`registry_azsort` 术语表 7254 行守恒；`check_terms` 硬错误 0。
* 当日累计：术语表 253 行（246＋7）；人名表 38 行。
* 人名第四批：14 人：Jean van Heijenoort、Robert Van Gulick、Lewis Carroll、James Clerk Maxwell、Quentin Skinner、David Enoch、Patricia Churchland、Larry Laudan、Jonardon Ganeri、George Bealer、H. L. A. Hart、Robin Le Poidevin、Felipe De Brigard、Mark van Roojen。
* 取证：Wikidata 逐人查（限流退避；凭证 `results/people-wikidata-2026-11-22-b4.tsv`）。Felipe De Brigard 无生卒数据，留“—”；Lewis Carroll 为作家兼逻辑学家（与已登记的 Noël Carroll 异人）；Patricia Churchland 与已登记的 Paul Churchland 异人分行。
* 落册：`term_flow` 干跑 14/0，实写 14；人名表 4597 数据行守恒；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 当日累计：术语表 253 行；人名表 52 行（13＋15＋10＋14）。

## 2026-11-23：人名表存量缺口回填

* 背景：specs/013 缺籍属/生卒告警 781 条（`specs/013-person-attribution/results/person-missing.txt`）。逐条筛名家可确证项。
* 回填 5 行：Aëtius（古希腊，约1–2世纪活动期，Q794615）、A.R. Anderson（美国，1925–1973，Q3268033）、David Lewis（美国，1941–2001，Q384522）、R. P. Wolff（美国，1933–2025，Q739540）、Timothy Williamson（英国，1955–，Q984380）。依据列追加“籍属/生卒联网查证：Wikidata Qxxx（2026-11-23 查，凭证 …）”，裁定日期不动。
* 弃用并留痕：Jon Williamson 的 Wikidata 条目 Q61951951 生卒为占位值 1900、职业仅 researcher，不可信；Paul Hoffman、Emma von Hartmann 查无条目。
* 证据：`results/people-wikidata-2026-11-23-backfill.tsv`。`registry_azsort` 守恒 4597；`check_terms` 硬错误 0。
* 门禁环境说明：本轮 `check_all` 本地红两项（单体文件大小、管线单元测试），根因均为 specs/057 会话未跟踪的新文件 s3u-audit.md（3343 行超限），不在本规格提交范围；已提交树不受影响，CI 为最终裁判。
* 当日累计：人名表存量回填 5 行（含 4 行补齐籍属/生卒、全部 5 行补凭证）。

## 2026-11-23：存量缺口自动回填（首批 200 条）

* 工具：`bin/backfill_auto.py`——逐条查 Wikidata，唯一学术候选且国籍/生卒可得者回填；多候选/无候选/数据全缺留痕不写。国籍优先 P27 映射，缺则按描述民族形容词回退（限定两条）；生卒取 P569/P570。
* 干跑暴露三类噪声并加守卫：① Wikidata 占位年 1900（Batterman、Brock 类）不给日期；② 生卒倒序（Epiphanius 600–501）不给；③ 同年占位（Albalag 1300–1300）不写。
* 人工排除 7 条撞名/存疑：Charles Mills（命中 18 世纪英国史家）、Audrey、Batterman, Robert、Brock, Gillian、Epiphanius、della Valle, Paolo、Balog, Katalin（首检为 1935–2005 匈牙利作家，存疑）。
* 实写 22 行（Abizadeh、Aldrich、Apollonius Cronus、Aristides、Axiothea、Barnes、Başkent、Boxer、Brady、Bridgeman、Buddhaghosa、Carugo、Chaerephon、Cintula、Costelloe、Cratylus、Dal Lago、De Giacomo、Della Rocca、Epimenides、Falk、Finsen）；其中 Buddhaghosa、Cratylus 两行人工把世纪改写为“约5世纪／约前5世纪（活动期）”，防止把世纪区间当生卒。
* 证据：`results/backfill-auto-2026-11-23.tsv`（227＋201 行，含两次运行全记录与排除理由）。
* `registry_azsort` 守恒 4597；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 事后更正（2026-11-23）：22 行依据列原引用 `people-wikidata-2026-11-23-auto.tsv`（不存在的文件名），实际凭证为 `backfill-auto-2026-11-23.tsv`；已批量改名（仅凭证文件名，译法/日期不动），脚本常量同步修正。`check_terms` 复跑硬错误 0。

## 2026-11-23：存量缺口自动回填（第二批 200–400）

* 工具：`bin/backfill_auto.py --start 200 --limit 200` 干跑 200 条，得 19 条“OK”（代理用 `127.0.0.1:7890`，192.168.5.4:7890 TLS 握手失败已弃），逐条核对 SEP 语境后仅 5 条身份确证：Gale, George（科学哲学家，Q133521156，补 1943–）、Gopal Sreenivasan（Q108581195，加拿大）、Hippobotus（Q2614752，希腊）、Kolodny, Niko（Q16403824，美国）、Lorki, Joshua（Q462009，西班牙／犹太改宗者，活动期 1400–1419）。
* 排除 14 条撞名/身份不符：Gerbrandy（描述计算机科学家、籍属记意大利）、Grant, Robert（美国法学家）、Green, Adam（歌手）、Hanson, William（土木工程师）、Hill, Thomas（作家）、Hippo（法国文学批评家）、Homer（美国物理学家，1942–2018）、Howard（单名物理学家）、Hyland, Martin（数学家且无生卒）、Iris（法律数据库）、John Pollock（英国史家）、Jonah（作家）、Klein, Peter（德国作家）、Ladner, Richard E.（生年 2000 为占位）。全部写入 EXCLUDE 并在证据 TSV 记理由。
* 定点写入脚本 `bin/backfill_batch2_manual.py`（只写上述 5 行，依据列追加 Wikidata 凭证）。
* `registry_azsort` 守恒 4597 行；`check_terms` 硬错误 0（人名缺项告警 781→775）；`check_all` 17 项全绿。

## 2026-11-23：著作名第五批（12 部）

* 选目来自全量总表 work 型高频未登记项，先经包含式查重排除已登记书名与概念行误拦：把查重脚本的包含式命中限定为「译法以《 开头的书名行」，并禁止连字符内切词（修正 Political Treatise 误撞 Theological-Political Treatise）。
* 逐部查审定库 allSearch（JWT 直连，12 部全有凭证）：命中均为他义——冥想、实践理性（概念非书名）、博物学传统、礼貌/论著、逻辑程序设计语言、期望寿命、可检验性（概念）、螺旋CT、穹天说、几何[学]、概率逻辑，判无对口条目。
* 转权威译本档登记 12 部：《第一哲学沉思集》《实践理性批判》《宇宙发展史概论》（全增嘏译）《政治论》（斯宾诺莎文集第2卷）《语言的逻辑句法》《普罗提诺传》《可检验性与意义》《黑皮肤，白面具》（张香筠译）《逻辑哲学论》《谈谈方法》（王太庆译）《几何基础》（江泽涵、朱鼎勋译）《概率的逻辑基础》。
* 译名联网核证（微信公号检索，2026-11-23）：谈谈方法（商务，王太庆）、宇宙发展史概论（全增嘏）、斯宾诺莎文集第2卷政治论、语言的逻辑句法（商务分析哲学名著译丛）、黑皮肤白面具（三联，张香筠）、几何基础（北大社，江泽涵/朱鼎勋）、普罗提诺生平（波菲利）。
* 落册：`term_flow` 干跑 12/0，实写 12；`registry_azsort` 术语表 7254→7266 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch9-works.json`。

## 2026-11-23：存量缺口自动回填（第三批 400–600）

* 干跑 200 条得 21 条“OK”，复核后实写 11 条、排除 10 条。
* 实写：Melissus（约前5世纪活动期）、Menedemus of Pyrrha（约前350–）、Metrodorus of Chios（约前4世纪活动期）、Michael Smith（澳大利亚，1954–，Q6828096，换条目）、Moltmann, Friederike（德国／法国）、Omori, Hitoshi（日本）、Paroush, Jacob（以色列，生年 2000 占位不写）、Phaedo of Elis（约前4世纪活动期）、Retoré, Christian（1964–）、Robert Adams（美国，1937–2024，Q5254926，换条目）、Roush, Sherrilyn（美国）。
* 换条目两例：Michael Smith 首检命中英国记者 Q6834471，改查 Q6828096（道德哲学家 Michael A. Smith）；Robert Adams 首检命中科幻小说家 Q7341356，改查 Q5254926（Robert Merrihew Adams）。
* 排除 10 条：MacLeod, Colin（籍属与多伦多大学心理学家不符）、McKay, Thomas（生物工程师）、Meskin, Aaron（生年与已知美学家不符）、Moran, Thomas（作家）、Murphy, Peter（作家兼法官）、Nishimura（仅姓氏）、Pease, Adam（计算机科学家）、Perry, John（罗德学者）、Radcliff（军人）、Richmond, Marsha（生年 1901 与当代科学史家不符）。全部入 EXCLUDE 并记证据。
* 纪年口径：描述只给世纪者记“约前N世纪（活动期）”，不冒充生卒；Wikidata 占位生年（2000）不写。
* 证据：`results/backfill-auto-2026-11-23.tsv` 追加 21 行。`registry_azsort` 守恒 4597；`check_terms` 硬错误 0，缺项告警 781→769。

## 2026-11-23：术语第四批（45 条）

* 选料改法：队列前列被泛搭配占据（health care、qua、let alone 等），改按「type=term＋术语后缀词表（theory/paradox/logic/principle…）＋未登记」直筛，得 574 条技术性候选。
* 逐条查审定库（50 条入队，全部有凭证）；命中对口者 11 条采审定形：自然主义谬误、会话含义（审定“会话隐含”记亦作）、商谈伦理、混沌理论、中文屋论证、合作原则、不确定性原理、恶性循环原则、行为功利主义（审定“行动效用论”记亦作）、丘奇论题、马赫原理；语境原理一条按审定形直采（语料无通行译法）。
* 语料计数佐证（篇目数）：子结构逻辑 16 vs 亚结构逻辑 1、会话含义 3 vs 会话隐含 1、行为功利主义 11 vs 行动效用论 5；中文屋论证 16、不确定性原理 13、弗雷格定理 8、斯科伦悖论 12、辛普森悖论 12。
* 四条跳过：substructural logics（与已登记 substructural logic／子结构逻辑 同概念复数形）、analogical arguments（同 analogical argument）、intellectual property rights（与 intellectual property／知识产权 同概念）、backwards induction（同 backward induction）；审定形“亚结构逻辑”与登记形“子结构逻辑”的差异留作 open item，待 rules/03 定性与裁决。
* 其余 34 条 A 档直裁（审定库仅命中泛词或他义）。
* 落册：`term_flow` 干跑 45/0，实写 45；`registry_azsort` 术语表 7266→7311 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch10-terms.json`。

## 2026-11-23：自动回填的偏移缺陷与修法

* 现象：第三批落册后再跑 `--start 600`，输出的 20 条与第三批复核名单重合。根因：`person-missing.txt` 由 `check_terms` 每次重生成（781→769 条），已补项退出后行序整体前移，用行号 `--start` 定位不等于“未处理者”。
* 修法：`backfill_auto.py` 增 `done_keys()`——读证据 TSV 第一列去重，`todo` 只取证据未记键，再按 `--start/--limit` 切片；重复查询归零，偏移不再依赖行序。
* 该轮干跑仅产生记录未写库（无 `--apply`），已在证据 TSV 留痕；后续批次按新逻辑重跑。

## 2026-11-23：存量缺口自动回填（第五批·剩余未查项）

* 按新去重逻辑（证据键）重跑，处理 181 条，得 30 条“OK”，复核后实写 10 条、排除 18 条、体例误判撤回 2 条。
* 实写：Shakespeare（英国，1564–1616）、Stephen Schiffer（美国，1940–）、Swartz, Norman（1939–）、Tartaglia（意大利，1499–1557）、Theocritus（约前3世纪活动期）、von Fintel, Kai（德国）、Weber, Zach（新西兰）、Wetzel, Linda（美国，1951–）、Wheeler, Michael（英国，1960–）、Schubert, Lenhart（美国）。
* 同名异人两例关键拦截：Sextus 行指莱布尼茨《神义论》里的塞克斯图斯·塔克文（恩披里柯已另行登记）、Zosimus 行指炼金术作家佐西摩斯而非拜占庭史家，均排除。
* 排除 18 条：Selig（诗人）、Shanahan（占位生年）、Simmons（生物力学家）、Skow／Uniacke（无生卒）、Solomon／Ubaldo／Wagener／Yin Xian（单名或描述过弱）、Squatrito（非哲学家）、Stanhope（代际不符）、Stephens（馆员）、Tian Pian（占位生年，行内已有凭证）、Turner（作曲家）、Weckert（占位生年）、Weinrich（身份存疑）。
* 方法事故与撤回：把 Van Cleve「美国／哲学」、van Gelder「澳大利亚／认知科学」误判为籍属污染并改写，核对全表发现「国籍／领域」是通行体例（1,041 行如此），已恢复原值；教训＝改存量字段前先量体例基线。
* 证据：`results/backfill-auto-2026-11-23.tsv` 追加 30 行。`registry_azsort` 守恒 4597；`check_terms` 硬错误 0，缺项告警 769→763。

## 2026-11-23：术语第五批（43 条）

* 自后缀筛结果第 61–120 位取 43 条，全部先查审定库（31 条实查 ok、12 条已有凭证）。
* 审定对口者 10 条：普通语义学、数学直觉、临摹性原则（亦作“拷贝原则”）、无类理论、约束理论、良序原则、玻尔对应原理（审定作“对应原理”）、实体实在论、批判理性主义、有效场理论（亦作“有效场论”）。
* 其余 33 条 A 档直裁；佛教概念 storehouse consciousness 按传统译名取“阿赖耶识（藏识）”（语料两形各 5 篇）。
* 译文语料计数：伯特兰悖论 2 篇（贝特朗悖论 0）、可知性悖论 11 篇、良序定理 3 篇（良序原则 0，哲学数学两义分列取原则）。
* 落册：`term_flow` 干跑 43/0，实写 43；`registry_azsort` 术语表 7311→7354 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch11-terms.json`。

## 2026-11-23：人名第五批（新增 5 人）

* 从重生成的人名队列里别名感知核查后确认真缺项 5 人：Iris Marion Young、Saunders Mac Lane、Frans van Eemeren、Francisco Miró Quesada、Abraham ibn Daud（Albertus Magnus＝已登记 Albert the Great、C. S. Peirce／P. F. Strawson／Anne Conway／Fichte 等均为别名变体）。
* 取证：Wikidata 逐人查（凭证 `results/people-wikidata-2026-11-23-b5.tsv`）。汉名按通行音译：艾丽斯·马里恩·扬、桑德斯·麦克莱恩、弗兰斯·范·埃默伦、弗朗西斯科·米罗·克萨达、亚伯拉罕·伊本·达乌德；籍属/生卒随行登记（美国 1949–2006／美国 1909–2005／荷兰 1946–／秘鲁 1918–2019／西班牙（安达卢斯）约1110–约1180）。
* 落册：`term_flow` 干跑 5/0，实写 5；`registry_azsort` 人名表 4597→4602 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch12-people.json`。

## 2026-11-23：术语第六批（42 条）＋人名第六批（3 人）＋差异裁定留证

* 术语第六批自后缀筛第 121–190 位取 42 条（跳过 foundational metaphysics、brute necessity 等义项不清者，以及 repository consciousness——与已登阿赖耶识同概念）。全部查审定库（33 实查、9 已有凭证），仅 2 条对口：信号检测理论、范畴论；其余 A 档直裁（切消定理、苏什科论题、贝里悖论、下行因果、个例-个例还原、移动聚光灯理论等）。
* 落册：`term_flow` 干跑 42/0，实写 42；`registry_azsort` 术语表 7354→7396 守恒；`check_terms` 硬错误 0。
* 人名第六批 3 人（逐人 Wikidata 取证，凭证 `results/people-wikidata-2026-11-23-b6.tsv`）：Andrew von Hirsch（安德烈亚斯·冯·赫希，英国（生于瑞士苏黎世），1934–2026，Q4759036）、Evelyn Fox Keller（伊夫林·福克斯·凯勒，美国，1936–2023，Q239131）、Leon van der Torre（无通行汉名保留原文，荷兰，1968–，Q23038082）。冯·赫希汉名经公众号文章核证，两种汉形并记（亦作“安德鲁·冯·赫希”）。
* 落册：`term_flow` 干跑 3/0，实写 3；`registry_azsort` 人名表 4602→4605 守恒；`check_terms` 硬错误 0。
* 差异裁定：审定形与登记形不一致的 6 例（substructural logic、conversational implicature、act utilitarianism、Copy Principle、Bohr’s correspondence principle、effective field theory）逐条定性并留证 `results/adjudication-2026-11-23-termonline-divergences.md`——均不构成 D1–D5，属“审定形与学界通行形并存”，主形取语料通行者、另一形以“亦作”入译法列，不另起行。

## 2026-11-23：著作名第六批（29 部）

* 自著作队列按修正后查重筛出 30 部真书名，逐部查审定库（16 部已有凭证、14 部新查），命中全为他义（唯象学、无穷、历史与社会课、论著、乌托邦、元素周期律、德目、回忆说、哲学王、寿命、非相干性、上议院、曙暮光、防御者、预测、政治经济学、必然性、情感分析、教育民主、恐惧、经验、向导、算术、四月提纲、全员参与、外伤史 等），判无对口条目。
* 译名联网核证（公众号检索）：《哲学家的矛盾》（安萨里）、《和平的保卫者》（马西利乌斯，商务）、《唯物主义史》（朗格，郭大力与李石岑合译）、《论人》（笛卡尔）、《法律要义》（霍布斯）、《普罗克洛生平》（马里努斯）。
* 弃收 1 部：De Genesi ad litteram（奥古斯丁）无通行汉名，学界多保留拉丁原名，按“查无 → 不臆造”暂不入册。
* 转权威译本登记 29 部：《知觉现象学》《总体与无限》《历史与阶级意识》《论人》《无政府、国家与乌托邦》《过程与实在》《法律要义》《德性论》《法权论》《论人类不平等的起源和基础》《差异与重复》《名哲言行录》《普罗克洛生平》《哲学家的矛盾》《商君书》《偶像的黄昏》《和平的保卫者》《经验与预测》《政治经济学原理》《命名与必然性》《道德情操论》《民主主义与教育》《恐惧与颤栗》《经验与自然》《迷途指津》《算术基础》《关于费尔巴哈的提纲》《万民法》《唯物主义史》。
* 落册：`term_flow` 干跑 29/0，实写 29；`registry_azsort` 术语表 7396→7425 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch14-works.json`。

## 2026-11-23：门禁环境说明（著作第六批收尾）

* 本地 `check_all` 16/17 绿，唯一红项「管线单元测试」失败用例 `test_abbrev_bare_name_still_dropped`；根因是并行会话（specs/053）对 `tools/yuanwen.py` 的在途未提交改动（工作区 M），不在本规格提交范围。
* 用 `git show HEAD:tools/yuanwen.py` 载入已提交版本复算：`build_cite_keys(['Descartes, René','Leibniz, G. W.'])` 返回 `[]`，与用例期望一致——已提交树不受影响，本规格不触碰该文件，推送后以 CI 为最终裁判。

## 2026-11-23：术语第七批（55 条）

* 自后缀筛第 191–260 位取 55 条，全部查审定库（38 实查、17 已有凭证），对口者 7 条：内部效度、溯祖理论、粒子数算符、计算树逻辑、归纳问题、代入量词、物理丘奇-图灵论题（审定只收基形“丘奇-图灵论题”，专名作主形并注）。
* 其余 48 条 A 档直裁：先验还原、定域实在论、非经典逻辑、混合表达主义、轻易知识、分子命题、序数逻辑、双重继承理论、后门准则、实用真理等。
* 落册：`term_flow` 干跑 55/0，实写 55；`registry_azsort` 术语表 7425→7480 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch15-terms.json`。

## 2026-11-23：术语第八批（53 条）

* 自后缀筛第 261–340 位取 53 条（弃 scientific world conception——与已登记 scientific world view／科学世界观同概念）。全部查审定库（34 实查、19 已有凭证），无一条完全对口：仅有基形命中 3 例，按专名作主形并在译法列注审定基形（弱人择原理／一般对应原理）；蒯因-迪昂论题审定作全形“迪昂-诺伊拉特-蒯因命题”，英文形不同，判 A 档并注。
* A 档直裁 50 条：外量词、程序合理性、斯堪的纳维亚实在论、类型-类型还原、知觉之幕、词项逻辑、时间部分理论、规范性能动性、相关选项理论、说谎者悖论、蒯因悖论等。
* 人名用字从册：Quine 系一律作“蒯因”（依人名表既有行），不作“奎因”。
* 落册：`term_flow` 干跑 53/0，实写 53；`registry_azsort` 术语表 7480→7533 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch16-terms.json`。

## 2026-11-23：术语第九批（39 条）

* 后缀筛池已挖尽，改走「小写多词技术短语」路线：T2 未登记 term 型、2–4 词、freq≥6 且 spread≥3，得 2,032 条，人工圈定 45 条；6 条因单复数变体或译名撞行剔除（recursive functions、inner sense、mystical experiences、perfect information、primitive recursive functions、phenomenal concepts）。
* 全部查审定库（28 实查、11 已有凭证）；完全对口 7 条（神经网络、性欲、进化心理学、精神障碍、可废止推理、法律解释等），5 条审定形与通行形并存，按裁定表处置并记「亦作」（公民不服从／公民抗命、社会阶级／社会阶层、方法论个人主义／方法论个体主义、语义观／理论的语义观、集体责任／集体伦理责任）。
* conventional truth 取佛教传统译名「世俗谛」（语料 9 篇；约定真理 0 篇），依传统译名惯例。
* 落册：`term_flow` 干跑 39/0，实写 39；`registry_azsort` 术语表 7533→7572 守恒；`check_terms` 硬错误 0。裁定表同步扩写 `results/adjudication-2026-11-23-termonline-divergences.md`；清单 `tasks/manifests/2026-11-23-058-batch17-terms.json`。

## 2026-11-23：术语第十批（40 条）

* 小写多词池第 71–160 位取 50 条，10 条因单复数变体或译名撞行剔除；全部查审定库（24 实查、16 已有凭证）。
* 审定对口 10 条：对应规则、抽象结构、逻辑表达式、剩余价值、对称性破缺、有向图、深层生态学、惯性质量（直采），不完美信息（审定收“不完美信息博弈”）、句法观（审定作“理论的句法观”）、说明性还原（审定作“说明的还原论”）记短形＋注。
* 其余 30 条 A 档直裁：认知成功、意向立场、意义公设、名义本质、权宜之计、广延实体、增长块、命题形式、关系善、强涌现、内在理由、复制者动力学、完备性学说、承认性尊重等。
* 落册：`term_flow` 干跑 40/0，实写 40；`registry_azsort` 术语表 7572→7612 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch18-terms.json`。

## 2026-11-23：术语第十一批（45 条）

* 小写多词池第 161–260 位取 50 条，5 条因单复数变体／同概念异形剔除（occasional causes、world line、crucial experiments、moral personality、decisional capacity）；全部查审定库（26 实查、19 已有凭证）。
* 审定对口 4 条直采：信息通道、完美记忆、量子混沌、社会资本；关系从句审定只收“子句”基形，作 A 档并注。
* 其余 40 条 A 档直裁：无限理智、活力、语境价值、绝对构想、复数主体、构成性说明、使能条件、思维风格、深层自我、随机漂变、特殊启示、方便善巧、起源本质主义、可理解质料、第二实体、无源之见、真实选择、制度事实、非概念内容、重复危机等。
* 落册：`term_flow` 干跑 45/0，实写 45；`registry_azsort` 术语表 7612→7657 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch19-terms.json`。

## 2026-11-23：术语第十二批（56 条）

* 小写多词池第 261–370 位取 59 条，3 条因单复数变体／同概念异形剔除（stationary states、weak counterexamples、continual creation）；全部查审定库（35 实查、21 已有凭证）。
* 审定对口 14 条：知识源、内在实在论、个人知识、重复博弈、初等等价、态函数、分布式知识、循证医学、遍历假说、完全格、方法论整体主义、矢量势（直采）；子博弈完美均衡（审定作“子博弈完美纳什均衡”）、进化稳定策略（审定作“进化稳定对策”）、思想语言（审定收“思维语言假说”）记短形＋注。
* 其余 42 条 A 档直裁：他我、生命活动、负内省、集体意识、模态轮廓、完美集性质、协调博弈、存在性性质、函数变元、审慎关切、质的同一性、随附性物理主义、工作场所民主、还原语句、关系平等、信念归属、普遍字符、后期抢占、宪法爱国主义、基本善、人的科学、条件线等。
* 落册：`term_flow` 干跑 56/0，实写 56；`registry_azsort` 术语表 7657→7713 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch20-terms.json`。

## 2026-11-23：术语第十三批（47 条）

* 小写多词池第 371–480 位取 50 条，3 条因单复数变体剔除（non-normal worlds、reactive attitude、units of selection）；全部查审定库（38 实查、9 已有凭证）。
* 审定对口 7 条直采：语词条目、语言相对论、生成语法、事件演算、解析集、逆向工程、认知革命；自由游戏（审定“游戏活动”属幼教义）、光滑无穷小分析（审定收“无穷小分析”）、期望效用最大化（审定只收基形）作 A 档并注。
* 其余 37 条 A 档直裁：模写论、描述函数、历史资格、内模型、干预主义反事实、非规范事实、累积文化、实验数学、古典基础主义、语境完整性、认知相关性、根本理由、道德养成、预设触发语、分支层级、永恒现在、一般递归函数、科学唯物主义、裸复数、古代神学、正派民族、认知压迫、不当剥削、中心化世界、复合实体、无限属性、不存在对象、可判断内容、判断线、粒子诠释、集合变元、社会传递、因果过去、概念融贯、机器表、第三领域。
* 落册：`term_flow` 干跑 47/0，实写 47；`registry_azsort` 术语表 7713→7760 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch21-terms.json`。

## 2026-11-23：术语第十四批（48 条）

* 小写多词池第 481–590 位取 50 条，2 条因单复数变体剔除（abstract objects、moral community）；全部查审定库（38 实查、10 已有凭证）。
* 审定对口 9 条：决策性隐私、事件时间、相容条件、有向无环图、前束范式、惯性系统、技能知识（亦作“知道如何”）、完全问题（直采）；话语照应（审定只收回指／指代）作 A 档并注。
* 其余 39 条 A 档直裁：游戏形式主义、操作分析、替代推理、对照实验、力学崇高、宏大叙事、局部语境、这一个（tode ti）、缺失感质、人工行动者、协调定义、设计假说、四端、谓述函数、量子对象、严格条件句、监控资本主义、先验对象、未言明成分、约束最大化、认知资格、非消除性结构主义、丰饶柏拉图主义、抽象人造物、肤色界线、本质索引词、伦理共同体、信仰寻求理解、民间生物学、作为公平的正义、货币泵、现象对比、感性表象、单否定、第三教条、个例物理主义、延展简单物。
* 落册：`term_flow` 干跑 48/0，实写 48；`registry_azsort` 术语表 7760→7808 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch22-terms.json`。

## 2026-11-23：术语第十五批（47 条）

* 小写多词池第 591–700 位取 50 条，3 条因单复数变体或同概念剔除（general volitions、privation theory＝已登 absence theory of evil 缺失论、categorical judgment）；全部查审定库（43 实查、4 已有凭证）。
* 审定对口 11 条：基率谬误、信念度、岛宇宙、识别问题、读心术、分子钟、奇怪吸引子、泛代数、解析分层（直采）；领域特殊性（审定收“领域特殊理论”）、随机占优（审定收“随机优势决策”）作 A 档并注。
* 其余 34 条 A 档直裁：法律现象、记忆标准、先验幻相、类比扩展、二值语义学、因果充分条件、秘传道德、外延类型论、博弈形式、事实问题、缺失遗传率、原现象性质、公认意见、强客观性、外来的观念、评价性尊重、信念盒、推理演算、刻画定理、说明自主性、直觉泵、否定类比、复数投票、软家长主义、普遍权利、显象性质、倾向词项、两两多数投票、先验几率、纯粹完善性、抽象个人主义、表观遗传景观、叙事自我、规范立场、还原策略、安全信念。
* 落册：`term_flow` 干跑 47/0，实写 47；`registry_azsort` 术语表 7808→7855 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch23-terms.json`。

## 2026-11-23：术语第十六批（50 条）

* 小写多词池第 701–810 位取 50 条，全部查审定库（40 实查、10 已有凭证）。
* 审定对口 11 条：间接言语行为、裸奇异性、置换对称、抽样误差、性别角色、无意识推理、条件反应、科学社会主义、适者生存、不等交换（直采）；倾向性诠释（审定作“概率的倾向解释”）作 A 档并注。
* 其余 39 条 A 档直裁：消除性归纳、认知允准主义、存在诠释、奠基物理主义、非真部分、归纳原则、探询逻辑、似然原则、元逻辑性质、元语义理论、规范必然性、开放结构、序数表示系统、呈现现象学、心理现实主义、公共价值、分支分析、社会剩余、酸葡萄、严格服从、合作剩余、刻意练习、想象的共同体、认知摩擦、证据函数、延伸表现型、外在命名、物种分类单元、实质蕴涵悖论、经典赋值、构造性反推数学、直接表象、双重特征概念、充分公开性、后验必然、公共政治文化、报复问题、成功论、系统力。
* 落册：`term_flow` 干跑 50/0，实写 50；`registry_azsort` 术语表 7855→7905 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch24-terms.json`。

## 2026-11-23：术语第十七批（47 条）

* 小写多词池第 811–920 位取 50 条，3 条因单复数变体或同概念剔除（ideal observers、philosophia prima＝first philosophy 第一哲学、intellectus agens＝active intellect 主动理智）；全部查审定库（43 实查、4 已有凭证）。
* 审定对口 10 条：法律事实、自私基因、敏感性分析、结构方程模型、公地悲剧、祈使句、传递模型、疾病负担、天命（直采）；集体财产一条审定“集束性”实为 collection property，判非同概念，作 A 档并注。
* 其余 37 条 A 档直裁：集体心灵、话语构型、有穷主义数学、意向系统、物理坍缩、正名、二阶理由、超越自我、平凡性结果、无限制的部分-整体组合、等式演算、存在即被感知、伦理非自然主义、激发性理由、无错分歧、基因选择、不重合对应物、直觉归纳、语言学替代主义、唯物主义构想、零假设、外模型、相平均、音系形式、可信性关系、可能性空间、威胁优势、语境改变潜能、贡献性不正义、暗黑模式、具身心智、市场社会、原初质料、道德顺从、显明矛盾、正确理性、有说服力论证。
* 落册：`term_flow` 干跑 47/0，实写 47；`registry_azsort` 术语表 7905→7952 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch25-terms.json`。

## 2026-11-23：术语第十八批（48 条）

* 小写多词池第 921–1040 位取 50 条，2 条因同概念/单复数剔除（anima mundi＝world soul 世界灵魂、dialogue games）；全部查审定库（39 实查、9 已有凭证）。
* 审定对口仅 1 条：社会生态学。其余 47 条 A 档直裁（动态信念逻辑、形而上学析取论、计算架构、批判残障研究、正常系统等审定仅有他义或基形命中）。
* 本批落册后术语表数据行达 8,000。
* 落册：`term_flow` 干跑 48/0，实写 48；`registry_azsort` 术语表 7952→8000 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch26-terms.json`。

## 2026-11-23：术语第十九批（45 条）

* 小写多词池第 1,041–1,160 位取 50 条，5 条因同概念/同译名剔除（five relationships＝wu lun 五伦、intellectus possibilis＝possible intellect 可能理智、natura communis＝common nature 共同本性、state of mind＝psychological states 心理状态，及同组之一），实查审定库 37 条、已有凭证 9 条。
* 审定对口 3 条：话语表现结构、五行、情绪智力；硬决定论（审定“硬技术决定论”属技术决定论义）、经典质点力学、后继序数等作 A 档并注。
* 其余 40 条 A 档直裁：二阶意愿、奇异时空、多样中的齐一、无限制概括原则、人造人格、典范模型、因果必然化、集体承诺、计算学习理论、形式直观、不完全描述、推论票券、内在道德、限制性概念、潜在部分、时间贴现、毒素难题、真值集、适应性偏好形成、认知可能世界、等价演算、想象焦点、力量指示词、潜变量、立法意图、道德一致性推理、次级可理解物、超越的应当、转换成本、辩证规律、有意设计、证成难题、普遍利益、弯曲空间、秘传教义、大众人、完全复制、实物证据、忠诚反对。
* 落册：`term_flow` 干跑 45/0，实写 45；`registry_azsort` 术语表 8000→8045 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch27-terms.json`。

## 2026-11-23：人名第七批（新增 4 人）

* 由重生成的人名队列与常见哲学家清单双向核对，确认真缺项 4 人（其余如 Peter Singer、Parfit、Nussbaum、Dennett、Arendt、Beauvoir、Charles Taylor 等均为「姓, 名」倒序键已登记）：Thomas Hurka、Tim Crane、Allen W. Wood、Eric Voegelin。
* 汉名核证（通用检索通道；微信检索当日被反爬拦截）：蒂姆·克兰（商务《机械的心灵》2021）、艾伦·伍德（商务《费希特的伦理思想》2022，另注与 Ellen Meiksins Wood 异人）、埃里克·沃格林（译林《秩序与历史》五卷）；Hurka 著作有中译但汉名未通行，按既有判例保留英文原名。
* 取证：Wikidata 逐人查（凭证 `results/people-wikidata-2026-11-23-b7.tsv`）：Q7790919（加拿大 1952–）、Q7803365（英国 1962–）、Q14509268（美国 1942–）、Q704039（美国／德国 1901–1985）。
* 落册：`term_flow` 干跑 4/0，实写 4；`registry_azsort` 人名表 4605→4609 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch28-people.json`。

## 2026-11-23：著作名第七批（2 部）

* 队列余项经中译核证后仅 2 部成立：《另外于是，或在超过是其所是之处》（列维纳斯，伍晓明译注，北大社 2019；学界通称《别于存在》）与《英国史》（休谟，刘仲敬译本 2012 与石小竹译本商务 2023 两系）。
* 不可收：《语义学导论》（卡尔纳普）无中译；《时间与模态》《真正的理智体系》等亦无通行汉名，按“查无 → 不臆造”暂不入册。
* 落册：`term_flow` 2/0，实写 2；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch29-works.json`。

## 2026-11-23：术语第二十批（42 条）

* 小写多词池第 1,161–1,270 位取 45 条，3 条因同概念/异形剔除（commutative law＝交换律、contraction rule＝contraction、dialectical theology＝dialectic theology）；实查审定库 36 条、已有凭证 6 条。
* 审定对口 5 条：寒蝉效应、微小意识状态、递归集、封闭世界假设、条件刺激。
* 其余 37 条 A 档直裁：描述性名称、无为（wu-wei）、文件抽屉、法律拟制、数学崇高、道德语法、非确定性矩阵、非还原唯物主义、有机存在者、可能性证明、本体感受经验、自反传递闭包、看作、情境主义挑战、主观普遍性、实体共相、超自然启示、传递遗传学、裸指示词、赌商、盲目变异、因果异常、经典回收、俱乐部物品、集体挫败、会话记分、挫败条件、设计立场、民主讨论、二元思维、认知对应物、无形行动者、最简定义、社会摩擦、结构刻画。
* 落册：`term_flow` 干跑 42/0，实写 42；`registry_azsort` 术语表 8047→8089 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch30-terms.json`。

## 2026-11-23：质量复核（主形重复与落地率）

* 主形碰撞扫描：全表按「译法主形」（去括注、去书名号）归组，主形对应多英文键共 154 组；其中 22 组为当日新行与既有行同概念异拼写。20 组已合并（新行删去、旧行键追加合写别名、依据列留痕），2 组辨析后保留（可靠认知＝知识论义 vs 藏传量论义；统计相关性＝一般义 vs Salmon SR 模型）。合并后术语表 8,089→8,069，`check_terms` 硬错误 0。
* 落地率：当日 835 条术语中主形在 2,021 篇中文译文出现 364 条（43.6%），其余为前瞻性登记；抽查未落地项（丘奇论题、帕累托原则、良序原则、恶性循环原则、概率因果性）均为登记形与语料并行，非误登。
* 防线：`tools/term_flow.py` 增「中文主形已存在」告警（只告警不拦截），合成用例正确触发；全量单测 578 项通过。
* 报告：`results/quality-check-2026-11-23.md`。

## 2026-11-23：主形碰撞 135 组逐组定性（续前）

* 机器初筛（归一化后 case/punct、单复数、前缀三档）＋逐组人工核对：占位主形 2 组；裁定合并 6 组（excluded middle→law of excluded middle、Outlines→Outline of Pyrrhonism、ordinary objects→ordinary object、research program→research programme、Phenomenology of Spirit→phenomenology of mind、sadō→chadō）；同概念异语传统合法并存约 100 组；同形不同义合法分行约 12 组（含《数学原理》两书同名）；辨析保留 2 组。全部 135 组有归属，报告已更新。
* 合并动作同前轮：新行删去、旧行键追加合写别名、依据列留痕。术语表 8,069→8,063，`registry_azsort` 守恒，`check_terms` 硬错误 0。
* 《数学原理》两书同名（Principia Mathematica 与 Principles of Mathematics）为同形不同义双行，词条阶段需按上下文区分，已在报告标注。

## 2026-11-23：术语第二十一批（39 条）

* 小写多词池第 1,271–1,390 位取 39 条，实查审定库 36 条、已有凭证 3 条。本批起 dry-run 无一触发新加的中文主形告警，防线工作正常。
* 审定对口 8 条：名家、重写规则、纯粹曝光效应、颜色空间、成分分析法、生态系统健康、上下文无关文法、像似符号；其余 31 条 A 档直裁：坚白、兼爱（impartial care，墨家义）、五路、高贵的谎言、政治动物（zoon politikon）、法外国家、晦暗语境、模态基、循环效应、本体论转向、利他惩罚、认知装置、死隐喻、双极神论、经验子结构、危机倾向、纽结图、直接自我指涉等。
* 落册：`term_flow` 干跑 39/0，实写 39；`registry_azsort` 术语表 8063→8102 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch31-terms.json`。

## 2026-11-24：术语第二十二批（28 条）

* 小写多词池第 1,391–1,510 位取 32 条，4 条因单复数变体／同概念剔除（numerals 数词、perpetual motion 永动机、human nature 人性、tangent space 切空间）；实查审定库 23 条、已有凭证 5 条。
* 审定对口 1 条：无条件反应。其余 27 条 A 档直裁：多重现代性、中立类比、互不重叠的权威领域（NOMA）、似动现象、哲学原子论、位置性商品、原初本体论、理性人标准、根本颂、可感质料、强内在主义、主观动机集（Williams）、神学转向、未被知觉的对象、弱否定、卑劣的遁词（Kant）、迷箱、定量享乐主义、反射公理、反向传播算法、共同命运、比较相似性、默认假设、因果传递等。
* 落册：`term_flow` 干跑 28/0，实写 28；`registry_azsort` 术语表 8102→8130 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-24-058-batch32-terms.json`。

## 2026-11-24：术语第二十三批（35 条）

* 小写多词池第 1,511–1,630 位取 35 条，实查审定库 28 条、已有凭证 7 条。
* 审定对口 8 条：如何可能说明、叶节点、冗余参数、和平教育、投影确定性（直采）；随机游走（审定作“无规行走”）、读写头（审定作“读写磁头”）、裂脑（审定亦作“分裂脑”）记短形＋注。
* 其余 27 条 A 档直裁：享乐基调、高阶推理、隐含约定、归纳策略、不公平厌恶、内否定、不变性条件、法律问责、机制草图、心理词典、心理时间旅行、非坍缩诠释、多元世界主义、政治道德主义、私人政府、私人对象、多一问题、投影规则、心理利他主义者、公共目的、无目的的合目的性（Kant）、五谓（Porphyry）、物种问题、分类学不可通约性、世俗权威、沉思生活（vita contemplativa）、不当威胁。
* 落册：`term_flow` 干跑 35/0，实写 35；`registry_azsort` 术语表 8130→8165 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-24-058-batch33-terms.json`。

## 2026-11-24：specs/058 提取—登记线收官

* 池源耗尽确认：T1/T2 term 型（后缀筛 336 条）与小写多词池（1,590 条）全部处理完毕；T3 严阈值（freq≥10 且 spread≥4）剩余 0。机器可提取的高置信术语池已挖完，后续增量应来自新增词条语料的 `term_harvest` 常态收割，而非本规格的存量清理。
* 验收对照：①az/ A–Z 各节齐备、总数守恒（260,526）；②节头计数齐；③23 份 rowspec 干跑零锚点缺失、azsort 幂等；④`check_terms`/`check_all` 全绿（17 项）；⑤调研与审定库凭证落盘。
* 两日累计（11-23/24）：术语表 7,254→8,165（净＋911，含 43 部著作）；人名表 4,597→4,609；存量缺项回填 53 行（781→763）；主形碰撞 135 组全定性、合并 26 组；`term_flow` 加中文主形告警防线。
* 开放项移交：①person-missing 余 763 条需人工逐条确证（自动线已耗尽且 EXCLUDE 累计 50+ 条撞名）；②人名队列仍混提取噪声；③《数学原理》两书同名的词条级区分；④剩余 phrase/句级候选不属登记对象，维持现状。

## 2026-11-24：person-missing 历史人物专项回填（20 行）

* 策略转换：`person-missing` 余 763 条中当代学者（Wikidata 无生卒）与噪声名占多数，改按“单名古代人物＋中古教名”筛出 208 条单名候选，以限定词逐一检索 Wikidata，确证 20 人。
* 回填：章太炎（1869–1936）、汉武帝（前156–前87）、汉昭帝（前94–前74）、毛亨（约前3–前2世纪活动期）、朴齐家（1750–1815）、弥兰陀王＝米南德一世（前300–前130）、欧布里德（约前4世纪活动期）、麦加拉的菲洛（约前4世纪活动期）、忒奥格尼斯（约前570–前485）、埃庇米尼德斯（约前700–前600）、罗杰·斯温斯海德（？–约1365）、梅特涅（1773–1859）、迪斯雷利（1804–1881）、蒙特祖马二世（1466–1520）、拿撒勒人耶稣（约前7–30）、使徒保罗（约5–66）、琐罗亚斯德（约前628–前551 传统纪年）、姜静一堂（1772–1832）、李彦迪（1491–1553）、尼西亚的欧斯特拉提奥斯（约1050–约1120）。
* 纪年口径三条：Wikidata 生卒与学界通说不合时（欧布里德、菲洛），从通说记活动期并注；宗教人物生卒按 Wikidata 并注学界通说区间；传统纪年有争议者（琐罗亚斯德）标注“传统纪年”。
* 证据：`results/people-wikidata-2026-11-24-hist.tsv`。缺项告警 763→743；`registry_azsort` 守恒 4609；`check_terms` 硬错误 0。
* 未收：桓宽、襄楷、Moses 等检索无对应条目或生卒不传者，留白不臆造；Hamlet/Zeus 等文学神话人物非信史，不填。

## 2026-11-24：人名第八批（新增 6 人）＋Châtelet 别名并入

* person 型全量候选别名感知挖掘（756 条过一遍过滤），倒序核对后确认真缺项 6 人：Cook Wilson（英国 1849–1915，Q3817476）、Kristie Dotson（美国，在世，Q57756823）、John Finnis（澳大利亚／美国 1940–，Q3312283，通行汉名约翰·菲尼斯）、Shannon Sullivan（美国，在世，Q21062465）、Van Bendegem（1953–，Q2229166，P27 记荷兰王国与学界通说比利时不合，籍属留白不写）、Philip Quinn（美国 1940–2004，Q7183930，与已登记 Warren Quinn 异人）。
* 其余候选均为已登记倒序键（Hempel、Scanlon、Mackie、Stout、Anscombe、Del Medigo 等）或著作/机构名。
* Châtelet 别名并入：语料形 Du Châtelet（大写 D）未入键，旧行 `Châtelet, Émilie du` 键追加合写别名并留痕；别名漏检根因＝重音字形折叠未覆盖大小写差异，属已知的键形变体家族。
* 落册：`term_flow` 干跑 6/0，实写 6；`registry_azsort` 人名表 4609→4615 守恒；`check_terms` 硬错误 0。证据 `results/people-wikidata-2026-11-24-b8.tsv`；清单 `tasks/manifests/2026-11-24-058-batch34-people.json`。

## 2026-11-24：人名第九批（新增 53 人，另补 2 条别名）

* 候选源：person 型候选取频次≥8、分布≥3 的一批（含前半段遗漏者与后半段），先按“首/末名双 token 含于键”倒序核对既有 4,615 行，再逐人 Wikidata 检索并核 P31（人类）、P27（国籍）、P569/P570。
* 新增 53 人：哲学侧有 Sharon Street（1973–）、Susan Haack（1945–2026）、Jean-Luc Marion（1946–）、Terence Horgan、Nathan Salmon、E. J. Lowe（1950–2014）、Talcott Parsons、Judea Pearl、Cass Sunstein、Andrea Dworkin、Angela Davis、Richard Joyce、James Woodward（1946–）、Tim Maudlin、Robert Kane（1938–2024）、Charles Larmore、Alison Jaggar、Solomon Feferman、Rae Langton、Kent Bach、David Copp、Michael Huemer、Anna Stilz、Leslie Green、Naomi Zack、Jennifer Saul、Louise Antony、Berys Gaut、William Galston、Mathias Risse、Eva Kittay、Susan Bordo、Michael Ayers、Robert Sugden、Susanna Siegel、Amie Thomasson、Marilyn Friedman、David O. Brink、Frances Kamm、Neil Levy 等；科学史与社会科学侧有 Charles Lyell、Alexander von Humboldt、Alfred Russel Wallace、Ludwik Fleck、Paul Samuelson、Aníbal Quijano、Ernest Renan、Charlotte Perkins Gilman、Reinhold Niebuhr、Simón Bolívar；中国与日本侧有黄宗羲（1610–1695）、金岳霖（1895–1984）、上田闲照（1926–2019）。
* 体例：无通行汉名者按既有例记“（无通行汉名，保留英文原名）”（21 人）；籍属用「国别」／双籍并用「／」连接。
* 三处取证例外：①Leslie Green 的 Wikidata 生年记 1918，英文维基记 1956（苏格兰－加拿大法哲学家），从维基并在依据注明；②Aníbal Quijano 出生年 Wikidata 记 1930，另说 1928，取 Wikidata 并注；③Neil Levy／Anna Stilz／Mathias Risse 三人 Wikidata 无 P27，经网页补证（Levy 1967 年生于约翰内斯堡、澳大利亚籍；Risse 生于帕德博恩、德美双籍；Stilz 公开资料未载国籍，籍属留白不猜）。
* 别名补记 2 条：`Herschel, John F. W.` 补语料形 `John Herschel`，`Price, Henry Habberley` 补 `H. H. Price`（两行原别名列为“—”，键与译法不动）。
* 落册：`term_flow` 干跑 53/0，实写 53；`registry_azsort` 人名表 4,615→4,668 守恒；`check_terms` 硬错误 0，缺籍属/生卒告警 746→748（新增行中 Kamm 生年、Stilz 国籍确无公开数据）；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b9.tsv`、补充取证 `results/people-wikidata-2026-11-24-b9-supplement.md`；清单 `tasks/manifests/2026-11-24-058-batch35-people.json`。

## 2026-11-24：人名第十批（新增 20 人）＋15 条语料形别名补记

* 筛法升级：前几批用“首名＋姓氏双 token 含于键”倒序核对，本批改为三重过滤——①键全等；②倒序／合写形展开；③姓氏＋首字母包含；再人工剔除机构（World Bank、Bletchley Park）、书名（Twin Earth、Summulae de Dialectica）、头衔（Pope John、Minister General）、残名（Ibn Abī）与代词短语。
* 教训（列入开放项）：姓氏比对若不做 Unicode 折叠，`sadra` 永远匹配不到 `ṣadrā`——本批两条（Mullā Ṣadrā、Mīr Dāmād）干跑时被 term_flow 拦下“键已存在”，实为既有行带变音符。故扫描器应先用 NFKD 去变音符再比对，不得只小写化。
* 新增 20 人：伊斯兰与印度古典侧有法拉比（约872–950，Q160460）、Vācaspati Miśra（约10世纪活动期，Q1292812，无通行汉名保留原名）、寂天（约8世纪活动期，Q445460，取佛教传统译名）；中国侧齐宣王（？–前301，Q580333）；当代哲学侧 John Haugeland（1945–2010）、Uma Narayan、Paul Draper、Stephen Toulmin（1922–2009）、Michael Devitt、Rosalind Hursthouse、James Griffin（1933–2019）、Ruth Chang（生卒未记）、Andy Clark（1957–）、Mark Johnston、Hasok Chang、Delia Graff Fara（1969–2017）、Michael Martin（1932–2015，Wikidata 无人格项，取波士顿大学讣告与英文维基）、Salazar Bondy（1925–1974）；科学史与法政侧 John Nash（1928–2015）、Oliver Wendell Holmes（小霍姆斯，1841–1935）。
* 三处判定：①Andy Clark 的 Wikidata P27 记美国，据 LCNAF／Who’s Who「born 1957-11-20 in London」从英国并注；②Michael Martin 与已登记 M. G. F. Martin 异人，依据注明；③Adam Elga 无 Wikidata 人格项、普林斯顿官页与 PhilPapers 均抓取失败，本批未收，留待有凭证时补。
* 别名补记 15 条（键与译法不动）：Gassendi←Pierre Gassendi、Maimonides←Moses Maimonides、Fichte←Johann Gottlieb Fichte、Scanlon, T. M.←Thomas Scanlon、F.A. Hayek←Friedrich Hayek、Mackie, J. L.←John Mackie、Anscombe, Elizabeth←G. E. M. Anscombe、Twain, Mark←Samuel Clemens、Albert the Great←Albertus Magnus、Hempel, Carl G.←Carl Hempel、Wolff, R. P.←Robert Paul Wolff、Strawson, P.F.←Peter Strawson、Lewis, C.I.←C. I. Lewis、Laozi←Lao Dan、van Norden, B.W.←Bryan Van Norden。
* 落册：`term_flow` 干跑 20/2（两条变音符同名被拦），实写 20；`registry_azsort` 人名表 4,668→4,688 守恒；`check_terms` 硬错误 0，缺项告警 748→749（Ruth Chang 生卒确无公开数据）；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b10.tsv`、`results/people-alias-2026-11-24-b10.tsv`；清单 `tasks/manifests/2026-11-24-058-batch36-people.json`。

## 2026-11-24：人名第十一批（新增 14 人）＋11 条别名

* 扫描器修正：按上批教训改用 NFKD 去变音符，并把**别名列**一并纳入 token 集；只取 `status=本轮新增` 的 person 候选，避免对已登记项反复报缺。修正后 freq≥6、spread≥3 档余 197 条，其中绝大多数为误分型（书名、机构、战争、概念、头衔）。
* 新增 14 人：Richard von Mises（1883–1953，Q84292，与 Ludwig von Mises 异人）、David Ray Griffin（1939–2022，Q521358）、Ralph Barton Perry（1876–1957，Q32679）、斯塔尔夫人（1766–1817，Q123041）、Grace Lee Boggs（1915–2015）、Olympe de Gouges（1748–1793）、Johann Georg Sulzer（1720–1779）、Juan Bautista Alberdi（1810–1884）、Olivier Costa de Beauregard（1911–2007，Q3350939）、Roy Wood Sellars（1880–1973，与 Wilfrid Sellars 为父子异人）、Robert Gooding-Williams（1953–）、Lynn Hankinson Nelson（1948–2024，Wikidata 无国籍）、沃尔特·司各特（1771–1832）、Alice Chipman Dewey（1858–1927）。
* W. D. Ross 在册（键 `Ross, W. D.`），只在册补全名别名，不重复落册。
* 别名补记 11 条：Ross, W. D.←William David Ross、Hamilton←Sir William Hamilton、King←Martin Luther King Jr、Novalis←Friedrich von Hardenberg、Delmedigo←Elijah Del Medigo、Collingwood←Robin George Collingwood、Lotze←Rudolf Hermann Lotze、Eliot←Mary Ann Evans、Newton←Sir Isaac Newton、Moore, G. E.←George Edward Moore、Butler←Bishop Joseph Butler。
* 落册：`term_flow` 14/0；`registry_azsort` 4,688→4,702 守恒；`check_terms` 硬错误 0，缺项告警 749→750（Lynn Hankinson Nelson 无国籍数据）；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b11.tsv`、`results/people-alias-2026-11-24-b11.tsv`；清单 `tasks/manifests/2026-11-24-058-batch37-people.json`。
* 余量估算：别名感知后 freq≥6 档只剩误分型与零星低知名人物；下一批起以 freq 4–5、spread≥3 的少量真缺项为主，人名线接近收官。

## 2026-11-24：人名第十二批（欧陆与后殖民 18 人）

* 新发现通道：候选池的类型分类只把“名＋姓”形标成 person，姓氏单独出现或出现在脚注书目的名家被漏掉。改用双向筛——①在 `yuanwen/` 全库直接计数；②对登记册键＋别名＋译法三列做 NFKD 折叠反查。门槛“≥8 次且三列皆不含该姓”，命中一批欧陆与后殖民理论家。
* 新增 18 人：伊利加雷（1930–，Q28918）、皮埃尔·阿多（1922–2010，Q972152）、伊尔塞特劳特·阿多（1928–2026，Q29453535）、加塔利（1930–1992，Q352465）、拉图尔（1947–2022，Q355237）、钱德拉·莫汉蒂（1955–，Q1086920）、J. N. 莫汉蒂（1928–2023，Q6203267）、阿甘本（1942–，Q311687）、巴迪欧（1937–，Q311005）、齐泽克（1949–，Q184750）、朗西埃（1940–，Q467470）、巴利巴尔（1942–，Q289333）、西苏（1937–，Q234964）、马拉布（1959–，Q432690）、霍米·巴巴（1949–，Q325741）、米尼奥洛（1941–，Q497968）、姆本贝（1957–，Q340234）、斯蒂格勒（1952–2020，Q822727）。
* 未收：Maurizio Esposito（Wikidata 只有同名演员与无描述研究者项，身份不可确证）；Paolo Virno（语料仅 2 次 1 篇，量不足）。
* 落册：`term_flow` 18/0；`registry_azsort` 4,702→4,720 守恒；`check_all` 17 项全绿。证据 `results/people-wikidata-2026-11-24-b12.tsv`；清单 `tasks/manifests/2026-11-24-058-batch38-people.json`。

## 2026-11-24：人名第十三批（定向补捞 29 人）

* 定向名单来自古典学、康德／黑格尔研究、法哲学、现象学社会学、后殖民与生态女性主义诸领域，仍用“yuanwen 计数≥3＋登记册三列折叠反查”。
* 新增 29 人：艾利森（1937–2023）、舒茨（1899–1959）、巴什拉（1884–1962）、洛林·科德（1937–）、平卡德（1947–）、凯特·曼恩（1983–）、乔纳森·里尔（1948–2025）、罗伯特·派平（生卒留白）、隆古奈斯（1950–）、克劳特（1944–）、塔纳里（1843–1904）、拉希德（1971–）、马莫（1959–）、里普斯坦（1958–）、维拉莫维茨-默伦多夫（1848–1931）、基亚拉多纳（1970–）、安东尼·达夫（1945–）、洛维特（1897–1973）、阿尔格拉（1959–）、拜塞尔（1949–）、奥特劳（生卒缺）、博布齐恩（1960–）、梅亚苏（1967–）、卡普托（1940–）、陶伯斯（1923–1987）、诺克罗斯（生卒缺）、米斯（1931–2023）、德利吉奥尔吉（1965–）、布莱滕巴赫（生卒缺）。
* 生卒留白者经二次核查：Robert Pippin、Alastair Norcross、Katerina Deligiorgi、Lucius Outlaw、Angela Breitenbach 的英文维基条目与 Wikidata 项皆无生年记载（`action=parse&prop=wikitext` 已取，条目内无 `Birth date and age` 模板），故留白不臆造；Béatrice Longuenesse 生年 1950 由维基条目与 Wikidata 双证一致。
* 无 Wikidata 人格项者：Robert Pippin（经英文维基“Robert B. Pippin”确证为美国哲学家、芝加哥大学）；John Dillon（古典学，检索只有同名政客与无描述项，身份不可确证，本批未收）；Christoph Helmig、Corey Dyck、Andrea Falcon（项无描述、易与他人不辨，未收）。
* 落册：`term_flow` 29/0；`registry_azsort` 4,720→4,749 守恒；`check_terms` 硬错误 0，缺项告警 750→755（新增行生卒确无公开数据者 5 人）；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b13.tsv`；清单 `tasks/manifests/2026-11-24-058-batch39-people.json`。

## 2026-11-24：人名第十四批（非西方传统 21 人）

* 定向名单覆盖现代新儒家（Xiong Shili、Tang Junyi、Xu Fuguan、Liang Shuming、Li Zehou、Zhang Dongsun——登记册原只有 Feng Youlan 等少数）、京都学派（Tanabe Hajime、Nishitani Keiji〔已在册被拦〕、Abe Masao、Yuasa Yasuo、Keta Masako）、中国哲学英语学界（Chad Hansen、Justin Tiwald）、印度正理—语言哲学（Bimal Krishna Matilal）、伊斯兰照明学派（Hossein Ziai、Al-Maturidi）、非洲哲学（Senghor、Tempels）与拉美解放哲学（Francisco Romero、Arturo Roig、Horacio Cerutti Guldberg、José Carlos Mariátegui）。
* 生卒特殊处理：Al-Maturidi 只记卒年（生年有约 853／893 两说）；Xu Fuguan 取 Wikidata 1904–1982 并注通行传记作 1903；Tanabe 1885–1962 更正本会话早先误记。
* 取证例外：Chad Hansen（Wikidata 同名项为橄榄球员，本人无人格项）与 Arturo Roig（英文维基条目存在但未载生卒）留白待考；Justin Tiwald 籍属据香港大学哲学系页（exa 检索，2026-11-24）。
* 落册：`term_flow` 21/1；`registry_azsort` 4,749→4,770 守恒；`check_terms` 硬错误 0，缺项告警 755→757（Hansen、Roig 生卒留白）；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b14.tsv`；清单 `tasks/manifests/2026-11-24-058-batch40-people.json`。

## 2026-11-24：人名第十五批（分析哲学各分支 20 人）

* 名单按分支（数学哲学、物理学哲学、认知科学、语言哲学、宗教哲学、现象学）列权威人名，再用“yuanwen 计数≥3＋登记册三列折叠反查”取缺口，命中 21 条，剔除 Anne Bezuidenhout（无 Wikidata 人格项、无可靠在线传记）。
* 新增 20 人：扎哈维（1967–）、Cappelen（1967–）、Stoljar（1967–）、Lepore（1950–）、García-Carpintero（1957–）、Colyvan（生年缺）、Bergmann（1964–）、Magidor（1976–）、Dougherty（1971–）、Ratcliffe（1973–）、雷卡纳蒂（1952–）、默明（1935–）、纽厄尔（1927–1992）、Speaks（1975–）、维格纳（1902–1995）、Morriston（生卒缺）、Carston（1950–）、Heck（1963–）、Rayo（1973–）、Barsalou（1951–）。
* 籍属留白 5 人（García-Carpintero、Ratcliffe、Speaks、Morriston、Heck）：Wikidata 项无 P27，不以推测填充，缺项告警相应增至 763。
* 落册：`term_flow` 20/0；`registry_azsort` 4,770→4,790 守恒；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b15.tsv`；清单 `tasks/manifests/2026-11-24-058-batch41-people.json`。

## 2026-11-24：人名第十六批（教父、汉传／藏传佛教、环境与技术哲学 16 人）

* 新增 16 人：安布罗斯（约339–397）、爱任纽（约130–约202）、诺瓦天（约220–258）、塞维利亚的伊西多尔（约560–636）、凯撒利亚的巴西尔（约329–379）、卡西奥多鲁斯（约487–约583）、湛然（711–782）、成玄英（约7世纪活动期）、米滂（1846–1912 传统纪年）、阿底峡（982–1054）、阿恩·奈斯（1912–2009）、安德鲁·芬伯格（1943–）、唐·伊德（1934–2024）、特雷弗·平奇（1952–2021）、黛布拉·萨茨（1956–）、西尔维娅·温特（1928–）。
* 判定：成玄英 Wikidata 生卒为占位值（700–700），改记活动期；米滂 Wikidata 无生卒，取通行传统纪年；温特无 Wikidata 人格项，生年据英文维基条目 `birth_date` 模板；奈斯经英文维基“Arne Næss”反查得 Q335152（检索直查只出同名的政治家与登山家）。
* 未收：列子（语料作篇名）、义净（同名可能指《易经》文本，语境未清）。
* 落册：`term_flow` 16/0；`registry_azsort` 4,790→4,806 守恒；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b16.tsv`；清单 `tasks/manifests/2026-11-24-058-batch42-people.json`。

## 2026-11-24：人名第十七批（印度传统 8、日本古学 4、女性主义 6）

* 新增 18 人：伐致呵利（约5–7世纪诸说）、跋陀罗衍那（约前2世纪活动期）、清辨（约500–578）、欢增（约820–890）、阿毗那婆笈多（约950–约1016）、罗摩奴阇（1017–1137）、Prabhākara（约7世纪活动期，无汉名保留原名）、Viśvanātha Kavirāja（约1300–1384）、荻生徂徠（1666–1728）、伊藤仁斋（1627–1705）、山鹿素行（1622–1685）、贝原益轩（1630–1714）、克伦肖（1959–）、贝尔·胡克斯（1952–2021）、玛丽·戴利（1928–2010）、费尔斯通（1945–2012）、威蒂格（1935–2003）、鲁迪克（1935–2011）。
* 检索坑两处：①Wikidata 直查 `Ramanuja` 只出同名昆虫属与罗摩化身项，须经英文维基页反查得 Q1741798；②`Bhaviveka` 项标签作 Bhavyaviveka，须按英文维基页名检索。占位生卒（Bādarāyaṇa 前350–前350、成玄英 700–700 同类）一律不取。
* 落册：`term_flow` 18/0；`registry_azsort` 4,806→4,824 守恒；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b17.tsv`；清单 `tasks/manifests/2026-11-24-058-batch43-people.json`。

## 2026-11-24：人名第十八批（认识论、美学、社会理论、法哲学 12 人）

* 新增 12 人：格雷科（1961–）、梅迪纳（1968–）、Kornblith（1954–，无通行汉名）、卢克曼（1927–2016）、布尔迪厄（1930–2002）、埃米特（1904–2000）、Sartwell（1958–，无通行汉名）、莫斯（1872–1950）、莱考夫（1941–）、佩珀（1891–1972）、福利（1947–，Wikidata 无 P27）、麦考密克（1941–2009）。
* 未收：Gaile Pohlhaus、Wayne Riggs——英文维基无条目、Wikidata 无项，无可核身份记录，暂留缺口并记入本行。
* 落册：`term_flow` 12/0；`registry_azsort` 4,824→4,836 守恒；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b18.tsv`；清单 `tasks/manifests/2026-11-24-058-batch44-people.json`。

## 2026-11-24：人名第十九批（人工智能、道德心理学与公共选择 9 人）

* 新增 9 人：麦卡锡（1927–2011）、海特（1963–）、吉仁泽（1947–）、塔洛克（1922–2014）、梅西耶（1980–）、布伦南（1944–2022）、麦卡斯基尔（1987–）、格林（1974–）、维尔曼斯（1942–）。
* 检索：参数化查询（“John McCarthy computer scientist”）在 Wikidat 全文检索失效，改英文维基页名反查（`John McCarthy (computer scientist)`→Q92739、`Joshua Greene (psychologist)`→Q16224624）。
* 落册：`term_flow` 9/0；`registry_azsort` 4,836→4,845 守恒；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b19.tsv`；清单 `tasks/manifests/2026-11-24-058-batch45-people.json`。

## 2026-11-24：人名第二十批（古典柏拉图主义、京都学派、印度现代、当代中国 8 人）

* 新增 8 人：阿提库斯（约150–约200，Q758060）、三木清（1897–1945）、室利·阿罗频多（1872–1950）、辨喜（1863–1902）、拉达克里希南（1888–1975）、张岱年（1909–2004）、刘笑敢（1947–）、蒋庆（生卒留白，无 Wikidata 项与英文维基条目）。
* 别名补记 1 条：`Mengzi` 补 `Mencius`（语料 706 次全用拉丁化名，登记册原只有拼音键，属高危漏配）。
* 落册：`term_flow` 8/0；`registry_azsort` 4,845→4,853 守恒；`check_all` 17 项全绿。
* 证据：`results/people-wikidata-2026-11-24-b20.tsv`、`results/people-alias-2026-11-24-b20.tsv`；清单 `tasks/manifests/2026-11-24-058-batch46-people.json`。
