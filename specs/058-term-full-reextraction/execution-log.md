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
