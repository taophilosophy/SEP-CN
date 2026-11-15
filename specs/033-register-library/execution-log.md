# execution-log — specs/033 登记册共享解析/折叠库

## 2026-11-15

* 开工基点：main 领先 1（并行会话提交）、behind 0；工作区并行会话在途态（`baseline/catalog.json`＋`en/_catalog/` 快照未提交），全程 pathspec 提交规避。`check_all` 11 项 10 绿 1 红：`原始物分歧账` 红在 `en/kant-reason`（未登记漂移），与在途 catalog 同源，属并行会话 001 管线在途，本规格不处置。
* 盘点（§2 口径表）：`norm_key`/`fold` 6 处实现 3 种口径；外围 5 工具（check_academic/check_junk/check_tables_images/check_doc_size/rebuild_dir）只持路径常量与白名单，不在解析面内。
* spec v1.0 落地；卡钉脚本 `bin/pin.py` 落地，pin-before 采集（术语 6269 行／人名 4622 行，五 B 副本当日同文，A≠B、B≠C 仅术语表——与 §2 口径表吻合）。
* 试金石 term_relations 迁移（592c39948）：pin 逐字段一致；顺带发现并修正 pin 脚本 REPO 少剥一层目录的首轮失误（作废条件未触发，属脚手架 bug 非迁移回归）。
* 批二 term_coverage/term_flow/term_harvest/cnki_query 迁移（9cd7a1612）：pin 一致；cnki_query 键口径 docstring 如实化（B≠A 为有意分歧，见 §2）。
* check_terms 迁移（682607739）：A 口径以 `norm_key_quote as norm_key` 别名保位，`parse_registry*`/`split_row`/`is_data_row`/`HEADER_WORDS` 再出口（term_audit/tl_browser_batch 零改动兼容）；门禁退出码 0，30 单测绿，pin 一致。
* registry_azsort 迁移（55ddf1ce5）：C 口径以 `fold_nfd as norm_key` 保位，azsort→check_terms 反向依赖解除；双表干跑守恒 0（6270/4578），24 单测绿，pin 一致。
* FR-4 单测 `test_register_lib.py` 17 例（三口径差异类／分节桶／双 schema 解析／消费方别名一致性）＋全库 320 例全绿。新增测试两处期望首稿写错（NFD 剥变音符、《中文书名》归 #），以库实行为准修正。
* FR-5 登记：rules/05 工具表、specs/001 contracts/cli.md 职责权属表各补一行。
* 收官复验：`check_all` 复跑见执行记录末行；pin 全程七次采集零漂移。
