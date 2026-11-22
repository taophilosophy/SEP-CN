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
