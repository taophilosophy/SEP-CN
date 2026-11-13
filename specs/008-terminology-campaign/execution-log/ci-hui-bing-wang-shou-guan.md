# 词汇表并网收官（ADR-0036，2026-11-13）

发布词汇表 `qian-yan/ci-hui-biao.md` 并网删除：行分流术语登记册（改名 `shu-yu-biao.md`）与人名登记册，三表收敛为双表。本页记录执行口径、逐行决策与遗留送审项。

## 一、结构变更

| 项 | 变更前 | 变更后 |
| ---- | ---- | ---- |
| 术语登记册 | `yi-zhe-shuo-ming.md` | `shu-yu-biao.md`（`git mv` 保历史；H1 改「术语表」） |
| 人名登记册 | `ren-ming-biao.md` | 不变（H1 改「人名表」，与 SUMMARY 入口对齐） |
| 发布词汇表 | `qian-yan/ci-hui-biao.md`（1384 键） | **删除**（git 历史可溯） |
| 门禁 | `check_terms.py` 三表 | 两表（自洽 + 缺依据；词汇表比对腿移除） |
| 读者入口 | SUMMARY/mu-lu-s「词汇表」 | 「术语表」+「人名表」两条 |
| 宪法 | III「术语译法以 yi-zhe-shuo-ming.md 为准」 | 改 `shu-yu-biao.md`（v1.3.0 → **v1.3.1**） |
| 豁免/白名单 | `check_doc_size`、`check_junk`、`check_academic`、`rebuild_dir` | 文件名同步；词汇表条目移除 |

工具收口：`term_flow.py`（去掉词汇表插入回路）、`term_harvest.py`（已登记键去词汇表腿）、`term_relations.py`/`term_coverage.py`/`cnki_query.py`/`term_audit.py` 路径改指；`script/glossary_lint.py` 失去对象退役（本地脚本，不入库）；`specs/011/bin/vocab_sync.py` 同失去对象（历史留档）。

## 二、行分流（守恒）

词汇表 1384 键中，与两登记册精确同键 975 行（术语 632、人名 342）按登记册为准校对后废弃；**两册均无 410 行逐行审阅分流**：

| 去向 | 行数 | 说明 |
| ---- | ----: | ---- |
| 术语册新增（术语/书名/地名/学说名） | 229 | 书名行依据列记来源（如上海译文译本名），术语行记语境义 |
| 人名册新增 | 27 | 含苏格兰启蒙群（Beattie/Burnett/Dunbar/Turnbull/Carmichael/Ramsay/Blair）、古典注疏家、现代学者 |
| 归并入既有行（键列补别形） | 7 | Voltaire（补本名 François-Marie d’Arouet）、Shaftesbury 三形、Burley/Burleigh、Sturm 简形、al-Razi/Razi |
| 废弃留账 | 149 | 同人异形重复 97、泛指姓/简称（Bacon/Cohen/Williams/Wilson/Albert/Benjamin/More/Samuel/Sturm 等）、复数异形、碎片键、泛词 |
| **合计** | **412** | 守恒门：写入 263 + 废弃 149 = 412 |

决策账（逐行）：`specs/008-terminology-campaign/results/bing-wang-2026-11-13.json`；未命中原始清单：`bing-wang-unmatched.tsv`；执行器：`bin/bing_wang.py`（plan/apply 两段，apply 前置守恒断言）。

写回后 `tools/registry_azsort.py --apply` 归位：术语册 6215→6215 行、人名册 4657→4657 行，周界 0，复跑幂等。

## 三、冲突仲裁（同键异译，7 条）

变体集合口径下真冲突 7 条，按 ADR-0036 决策 3「以术语在线审定库为准」逐条裁决：

| 词 | 词汇表 | 登记册 | 审定库查证 | 裁定 |
| ---- | ---- | ---- | ---- | ---- |
| akrasia | 不能自制 | 意志薄弱 | termonline-all 查无 | 登记册为准，补亦作「不能自制」 |
| paradox of suspense | 悬疑悖论 | 悬念悖论 | 查无 | 补亦作「悬疑悖论」（SUMMARY 题名形） |
| square of opposition | 逻辑方阵 | 对当方阵 | 查无 | 补亦作「逻辑方阵」 |
| cardinal | 枢机主教 | 基数 | 命中「基数词/基本方位」均异学科 | 集合论义维持「基数」，另立多义行 `Cardinal（教会职衔）` = 枢机主教 |
| rationality | 理性 | 合理性 | 命中「理性」来自信息科学/马克思主义学科 | 跨学科同名不采，维持「合理性」（与 reason 理性 区分） |
| schêma | 图型 | 图式（行内已注「图型」） | — | 已含亦作，无需改 |
| Understanding | 理解 | 知性（行内已注日常义「理解」） | — | 已含语境分工，无需改 |

## 四、遗留送审（5 条人名译法冲突）

人名册为决策源，但词汇表注记主张全库改形，口径不一，交用户裁定后再回写：

| 人物 | 词汇表 | 人名册现行 | 备注 |
| ---- | ---- | ---- | ---- |
| Simone de Beauvoir | 波伏瓦（注记：全库取波伏瓦，亦作波伏娃） | 西蒙娜·德·波伏娃 | 册内另有 `de Beauvoir, Simone` 重复行 |
| McTaggart, J.M.E. | 麦克塔格特 | 麦克塔加特（依据列已注「亦作麦克塔格特」备查） | 可径直改主形 |
| Juan Luis Vives | 维夫斯 | 胡安·路易斯·比韦斯 | 两名均通行 |
| Thābit ibn Qurra | 塔比·伊本·库拉 | 萨比特·伊本·库拉 | 阿拉伯语 ثابت 通译两形 |
| Fakhr al-Dīn al-Rāzī | 法赫尔丁·拉齐 | 册内两行同译（`al-Rāzī, Fakhr al-Dīn` 与 `Fakhr al-Dīn al-Rāzī`） | 册内重复行待合并 |

## 五、门禁

`check_terms.py` 硬错误 0（自洽 0）；`check_all.py` 九项中「哲学学术规范」红 5 处为 M1 翻译线在途产物（`tasks/m/{mandeville,marsilius-padua,model-organisms,moral-learning,music}.json` 缺语体核验结论，来源提交 f7670c6a1），非本批引入，按规则留痕不越权修复。
