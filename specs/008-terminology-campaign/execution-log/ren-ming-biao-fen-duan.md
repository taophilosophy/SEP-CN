# 人名表分段长跑（2026-11-13 起）

人称登记册（`ren-ming-biao.md`）全量未查证队列分段查证。队列由
`python tools/tl_browser_batch.py --emit --table person --unverified` 生成，规模随时间增长；
**分段接力，任何会话按 `state/tl-crawl-state.json` 续跑**，凭证落
`specs/008-terminology-campaign/results/queries/termonline-all/`。

## 一、首段 offset 0–200（TL-main-20261113，2026-11-13）

* 队列 `%TEMP%/az-person20.json` 实测 4424 项（键 4403，归并行已拆变体）；本段 200 项分 25 批跑完，
  爬虫自愈降级多次、批末补跑救回。
* 审计刷新：一致 1181 / 不一致 797 / 查无 4706 / 未查证 4219（含术语侧；人名侧未查证余约 4224）。
* **新增不一致 3 条，全部保留现译**：
  * Alexander the Great「亚历山大大帝」——审定命中为「亚历山大大帝征服中亚」全称短语（下位）；
  * Aspect, Alain「阿兰·阿斯佩」——审定命中为集体消费理论垃圾池（模糊匹配污染）；2022 年诺奖得主通行汉名；
  * Antiphon「安提丰」——审定命中「交替圣歌」（antiphon 礼仪词）同形异义，本行雅典演说家/智者。
* 门禁：`check_terms.py` 硬错误 0；凭证按检查点提交（0–48、48–80、80–128、128–168、168–200）。

## 二、第二段 offset 200–400（TL-main-20261113，2026-11-13）

* 200 项分 25 批跑完（`--start 200`，断点续跑口径实测可用）；审计刷新：一致 1158 / 不一致 789 / 查无 4807 / 未查证 3969
  （登记册行数因并行会话并网废弃行清理而变动，四态绝对值随之漂移，判定须用差集口径）。
* **新增不一致 6 条，全部保留现译**（审定命中皆为无关词或全称形）：
  Azarenka, Victoria（垃圾池）、Bateson, William（命中「半索动物门」为学科词）、Beethoven, Ludwig van（命中「贝多芬」短形）、
  Benedict XII / Benedict XVI（垃圾池）、Bieberbach, Ludwig（命中「空间群」为数学名词，与 Bieberbach 定理相关但非同词）。

## 三、后续段作业口径（复用勿重推）

* 起跑：`python -u tools/tl_crawler.py --crawl --queue "$TEMP/az-person20.json" --start <断点> --batches <N> --no-warm --interval 12 --batch-gap 20 --out-dir "$TEMP"`；
  守护 `python -u script/tl_ingest_watch.py`（mtime 记账版，见 `session-handoff.md`）。
* 限流：站点预算约 18 请求/5 分钟，2–3 词/分；人名查询模糊池噪声大（查无率高），属预期。
* 裁定口径同术语侧：只采审定库同词同学科命中做主译变更；人名音译差异一律保留现译，
  审定异形记「亦作」或仅在依据列留档。
