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

## 四、净队列续跑首段裁定（TL-main-20261114，2026-11-14）

* 净队列 `%TEMP%/az-person-next.json`（3984 项，emit 跳过已查证 715 键，并网去重后存活行）自 offset 0 重跑；
  爬虫+守护后台长跑，本节裁定时爬至 offset ≈330（Collins/Collingwood，C 段）。
* 审计（audit-2026-11-14）：一致 1159 / 不一致 792 / 查无 4985 / 未查证 3847；
  维基排查 4 条均为**已撤维基引证的合规留痕**（Conventuals 2026-11-08、Herbrand/Nelson/Takeuti 2026-11-13
  撤维基措辞记录），非违例，无需动作。
* **A–C 段人名不一致 34 条，全数判读：保留现译，零主译变更**。其中 9 条为前三段已裁定存量
  （Alexander the Great、Aspect、Azarenka、Bateson、Beethoven、Benedict XII/XVI、Bieberbach、Antiphon）；
  25 条新增逐条归因：
  * 审定库模糊池垃圾命中（18）：Adam Mickiewicz→密卷云、Adam Wodeham→四德、Addams→斯、
    Adolf Grünbaum→宾格、Adolf von Harnack→纳克、Alison→阿利亚、Alois Riehl→德哈斯-范阿尔芬效应、
    Alter→波特、Ammonio→克烈、Ammonius Hermeiou/Saccas→同上、Anaxagoras→阿夫拉米方程、
    Andersen→比尔拉财团、Anderson→安南、André of Neufchâteau→沙芥、Andreas Rüdiger→克烈、
    Andronikos Doukas→同上、Carafa→RNA聚合酶III（编号 III 模糊）；
  * 同名异人（2）：Addison, Joseph→约瑟夫·斯蒂格利茨、Adolph Friedrich Hoffmann→弗里德里希·李斯特；
  * 同形异义（3）：Achilles→小行星588号（天文学）、Cao Cao→槽（建筑学 cao）、Antiphon→交替圣歌（存量）；
  * 短形/下位（2）：Bruckner→布鲁克纳（海峡两岸音乐名词短形，同 Beethoven 先例）、Alexander the Great→征服中亚全称（存量）；
  * 有道辅助档不作变更依据（1）：Anaximenes→阿那克西米尼（音译 n 差异，youdao-aux 仅辅助）。
* 门禁：check_terms 硬错误 0（凭证侧无登记变更，无涟漪）。
* **插曲（外部清理事故与恢复）**：批 0 的 6 份未跟踪凭证在 ingest 后、提交前被外部 `git clean` 类操作
  删除（GitHub Desktop discard 特征；%TEMP% 批次文件完好）；已按 `git restore` + 仅本轮批次幂等重入恢复，
  零数据损失。凭证提交节奏加密（每 2–3 批一次）以缩小未跟踪窗口。并行线大扫提交
  （4a9d8384d「工作区与 stash 一并提交」）已卷入约 40 份凭证入库。

## 五、净队列续跑二轮裁定（TL-main-20261114，2026-11-14）

* 爬至 offset ≈472（C 段尾/D 段口）复跑审计：一致 1162 / 不一致 801 / 查无 5282 / 未查证 3637。
  登记册被并行线重排，**行号漂移，本轮起裁定按词条键记录**。
* **新增不一致 14 条（真增量），全数保留现译，零主译变更**；另 28 条为已裁定存量因行号漂移重报
  （第四节 34 条的词条键全数复现，裁定不变）：
  * 音译/全称形差异（5）：Charles Fourier（审定经济学全称「弗朗斯瓦·马利·沙尔·傅立叶」，现行短形）、
    Theophrastus（审定「泰奥弗拉斯多」，现行「特奥弗拉斯托斯」）、Cournot（审定经济学界「古诺」，
    现行「库尔诺」，依据列已有留档）、Alban Berg（审定倒装形「贝尔格，阿班」）、Chopin/Collins, Anthony
    （审定音乐名词短姓形「肖邦/科林斯」，现行全形）；
  * 同名异人（1）：Coleridge→科勒里奇-泰勒（Samuel Coleridge-Taylor 作曲家）；
  * 同形异义（5）：Damon→守护程序（daimon 信息科学）、Galen→含锡石（地质）、Hao Wang→好太王碑（民族学）、
    Hui Shi→会试（古代史）、Porphyry→斑岩（岩石学）；
  * 下位/短语命中（2）：Yan Hui→孔颜之乐（全称短语）、Yang Zhu→杨朱学派（下位学派名）；
  * 模糊池垃圾（1）：Aḥmad ibn al-Muʿtaṣim→TA克隆。
* 口径确认：人名音译差异一律保留现行主形（ADR-0012 优先级 + 前三段先例），审定异形仅在依据列留档，
  不齐改正文。

## 六、三轮裁定（TL-main-20261114，2026-11-14）

* 爬至 offset ≈580（D 段）复跑审计：一致 1162 / 不一致 804 / 查无 5376 / 未查证 3540。
  未裁定仅 3 条，全数保留现译：Dred Scott（命中「斯科特判决案」为事件名下位）、
  Duncan-Jones, Austin（命中「费舍曼－琼斯－豪瑟假设」为 fuzzy 池 Jones 片段污染）、
  Durà-Vilà, Víctor（命中「集体消费理论」垃圾池）。零主译变更。

## 七、净队列滚动裁定台账（TL-main-20261114，自四轮起合并记录）

* **四轮**（offset ≈700，E 段；审计 一致 1162 / 不一致 807 / 查无 5491 / 未查证 3422）：新增 3 条全保留——
  Eduard Steuermann（海峡两岸音乐名词「施托伊厄曼」，音译用字「尔/厄」差异）、
  Emperor Wu (Han)（命中「光武中兴」为下位事件短语）、Epictetus（「集体消费理论」垃圾池）。零主译变更。
* **五轮**（offset ≈816，F 段；审计 一致 1162 / 不一致 808 / 查无 5602 / 未查证 3310）：新增 1 条保留——
  Feigl, Herbert（命中「维也纳学派」为其所属学派名，非人名命中）。零主译变更。
* **六轮**（offset ≈940，G 段；审计 一致 1164 / 不一致 810 / 查无 5715 / 未查证 3193）：新增 2 条保留——
  Hegel（命中「青年黑格尔派」为下位派名）、George III（命中「RNA聚合酶III」为编号模糊垃圾）。零主译变更。
* **七轮**（offset ≈1080，G/H 交界；审计 一致 1164 / 不一致 811 / 查无 5863 / 未查证 3044）：新增 1 条保留——
  Guo Xiang（命中「国相」为同音异义，中国古代史名词）。零主译变更。
* **八轮**（offset ≈1230，H 段；审计 一致 1166 / 不一致 813 / 查无 6004 / 未查证 2899）：新增 2 条保留——
  Helmholtz, Hermann von（审定「黑尔姆霍尔茲」音译差异，海峡两岸音乐名词）、
  Herbert Simon（审定「赫伯特·西蒙」通行音译；现行「司马贺」为本人自定中文名，依据更强，保留）。
  零主译变更。
* **守护 PermissionError 事故（2026-11-14）**：双守护实例并存，save_seen 写同名 .tmp 互踩（Windows 文件锁）
  致守护死亡约 30 分钟；爬虫不受影响。已修守护（tmp 名加 pid、写失败容忍跳过）并重启；
  死亡窗口 12 批按 mtime 手工幂等补入（85 ok / 3 empty / 5 error，error 由补跑或下轮 --unverified 收口）。
* **九轮**（offset ≈1380，H 段中；审计 一致 1167 / 不一致 816 / 查无 6135 / 未查证 2764）：新增 3 条保留——
  Hindemith, Paul（审定「兴德米特」音译差异）、Hipparchus（「上清派」垃圾命中；现行行带
  「（毕达哥拉斯派）」消歧括注）、Hu Shi（「有扈氏」同音异义，中国古代史名词）。零主译变更。
* **十轮**（offset ≈1500，I 段；审计 一致 1167 / 不一致 817 / 查无 6234 / 未查证 2664）：新增 1 条保留——
  Iris（命中「虹神星」为小行星 7 号天文学定名，同形异义）。零主译变更。
  另记：H 段凭证 129 份单提交（bfae61a99），`hipparchus_毕达哥拉斯派.json` 文件名含 CJK
  （safe_key 只音译希腊字母、不动 CJK），可正常审计命中，属已知形态。
* **十一轮**（offset ≈1600，J/K 口；审计 一致 1168 / 不一致 825 / 查无 6344 / 未查证 2545）：新增 8 条保留——
  Jevons（审定经济学「威廉·斯坦利·杰文斯」；登记册按 ADR-0012 体例保留英文，属体例差异非音译差异，
  改译须动 william-jevons 正文，超出人名查证批范围，留档不动）、Jia Yi（「仪驾」同音异义）、
  Johann Friedrich（「布格缪勒，约翰」同名异人 fuzzy）、John Donne（「圣十四行」全称短语下位）、
  John Hick（「约翰·希克斯」经济学家同姓异人）、Jones, Peter（「费舍曼－琼斯－豪瑟假设」fuzzy 片段）、
  Kahneman（「卡内曼」音译用字差异，经济学名词）、Kaṇāda（「坎纳达人」民族学同形异义）。零主译变更。
* **十二轮**（offset ≈1710，K 段；审计 一致 1168 / 不一致 826 / 查无 6443 / 未查证 2445）：新增 1 条保留——
  Koopmans, Tjalling（审定「加林·库普曼斯」为音译用字差异，经济学名词）。零主译变更。
* **十三轮**（offset ≈1830，K/L 交界；审计 一致 1168 / 不一致 831 / 查无 6554 / 未查证 2329）：新增 5 条保留——
  Kraft, Victor / Lactantius（「集体消费理论」垃圾池）、Kuhn（「库恩-托马斯-赖歇加和规则」
  为含人名的定理名，化学名词下位）、Kurzweil, Ray（「《奇点临近》」著作名下位）、
  Lao Tzu（「老子辩证思想」下位思想名）。零主译变更。
* **十四轮**（offset ≈1980，L 段；审计 一致 1169 / 不一致 833 / 查无 6685 / 未查证 2195）：新增 2 条保留——
  Lincoln, Abraham（「林肯旅」为下位事件名，世界历史名词）、Liu Bei（「刘裕北伐」同姓 fuzzy，
  中国古代史名词）。零主译变更。
* **十五轮**（offset ≈2110，L/M 交界；审计 一致 1168 / 不一致 836 / 查无 6666 / 未查证 2212）：新增 5 条保留——
  Luther, Martin（审定短姓形「路德」）、Lysis（「裂解」同形异义，兽医学）、Mach, Ernst（「马赫学会」
  含人名的机构名下位）、Malthus（审定全称形「托马斯·罗伯特·马尔萨斯」）、
  Marx, Karl（审定倒装形「马克思，卡尔」，海峡两岸音乐名词）。零主译变更。
* **十六轮**（offset ≈2215，M 段中；审计 一致 1170 / 不一致 837 / 查无 6764 / 未查证 2111）：新增 1 条保留——
  McTaggart, J.M.E.（「集体消费理论」垃圾池；该译法 2026-11-13 已专项裁定维持现行）。零主译变更。
* **十七轮**（offset ≈2330，M 段尾；审计 一致 1171 / 不一致 841 / 查无 6865 / 未查证 2005）：新增 4 条保留——
  Mersenne（审定短姓形「梅森」）、Michelangelo（「米开朗琪罗诗的组曲」含人名的作品名下位）、
  Mill, John Stuart（审定经济学「约翰·斯图亚特·穆勒」vs 现行「密尔」：哲学界通行密尔、
  经济学通行穆勒，属学界既有分流，按人名音译差异保留现行）、Milton, John（「米尔顿」音译差异）。
  零主译变更。
* **十八轮**（offset ≈2455，M/N 交界；审计 一致 1172 / 不一致 843 / 查无 6993 / 未查证 1874）：新增 2 条保留——
  Newton, Isaac（「牛顿望远镜」含人名的器物名，天文学）、Nicholas III（「RNA聚合酶III」编号模糊垃圾，
  同 George III 先例）。零主译变更。
* **十九～二十轮**（offset ≈2720→3100，N–S 段；2026-11-14 提速后双道并跑）：新增 8 条保留——
  十九轮：Octavia、Paz, Octavio（垃圾池）、Paul III、Pio di Carpi, Alberto III（编号模糊垃圾）、
  Philip II（「腓力二世改革」下位事件名）；二十轮：Poncelet, Jean-Victor（垃圾池）、
  Proudhon（审定全称形「皮埃尔·约瑟夫·蒲鲁东」）、Rāma（「拉马人」族称同形异义，民族学）。
  零主译变更。
* **提速改造留痕（2026-11-14）**：窗口失效定性为 TTL≈120s（非性能限流，「18 请求/5 分钟」作废）；
  激活器 listFront 重放（0.3s）实现为 `tl_crawler.activate()`，主动每 90s 续窗、降级立即激活
  （废 60s 误罚）；稳态 `--interval 10 --batch-gap 2 --warm-every 90` 实测 5.3 词/分（原 2.1），
  零降级零 error。**双道并跑**：标准库 standardSearch（匿名）尾段并行已证实互不干扰，
  凭证落 termonline-standard/（查无按「标准库未收录，不作否定证据」口径）。交接卡限流节已重写。
* **十九轮**（offset ≈2720，N/O 交界；审计 一致 1172 / 不一致 848 / 查无 7236 / 未查证 1626）：新增 5 条保留——
  Octavia、Paz, Octavio（「集体消费理论」垃圾池）、Paul III、Pio di Carpi, Alberto III（「RNA聚合酶III」
  编号模糊垃圾，同 George III 先例）、Philip II（「腓力二世改革」下位事件名，世界历史名词）。零主译变更。
