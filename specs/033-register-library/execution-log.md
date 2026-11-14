# execution-log — specs/033 登记册共享解析/折叠库

## 2026-11-15

* 开工基点：main 领先 1（并行会话提交）、behind 0；工作区并行会话在途态（`baseline/catalog.json`＋`en/_catalog/` 快照未提交），全程 pathspec 提交规避。`check_all` 11 项 10 绿 1 红：`原始物分歧账` 红在 `en/kant-reason`（未登记漂移），与在途 catalog 同源，属并行会话 001 管线在途，本规格不处置。
* 盘点（§2 口径表）：`norm_key`/`fold` 6 处实现 3 种口径；外围 5 工具（check_academic/check_junk/check_tables_images/check_doc_size/rebuild_dir）只持路径常量与白名单，不在解析面内。
* spec v1.0 落地；卡钉脚本 `bin/pin.py` 落地，pin-before 采集后进入迁移。
