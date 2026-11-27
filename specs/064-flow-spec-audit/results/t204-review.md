# T204 根目录归集 zh/ 与关联者

- 日期：2026-11-27。
- 目录：27 个字母目录＋`1/`＋`fang-fa-lun/`、`guan-yu/`、`jian-yi-shu/`、`qian-yan/` 全部 `git mv` 到 `zh/`；`SUMMARY.md`、`mu-lu-s.md`、`shu-yu-biao.md`、`ren-ming-biao.md`、`PROGRESS.md`、`RELEASE-NOTES.md` 同迁 `zh/`；`开源翻译.md` 按用户指令 `git rm`。
- 链接：`zh/SUMMARY.md` 根级链接改 `../`；`zh/mu-lu-s.md` 词条链接去 `zh/` 前缀（相对 zh）；根 `README.md` 的目录/登记册/进度链接改 `zh/…`。
- 事实源：`rules/layout.json` 新增 `zh`、互换 `en`／`yuanwen` 语义、登记册与中文目录路径改 `zh/…`、删除 `开源翻译.md`；`rules/01` 目录职责表同步。
- 工具：`register_lib.term_path/person_path`、`progress.py` 输出 `zh/PROGRESS.md`、`check_mulu_s`、`check_terms`、`check_term_concepts`、`check_doc_size`、`check_junk`、`check_layout`、`summary_sync`、`check_catalog_network`（mu-lu 重放映射）全部改 zh 布局。
- 任务：`tasks/**/*.json` 的 `zh_doc` 全部改 `zh/<letter>/<slug>.md`；登记册维护任务改 `zh/shu-yu-biao.md` 等。
- 壳仓：`README.md` 增内容布局说明；`deploy.yml` 路径不变（`docs/README.md` 仍为首页）。
- 验收：`check_layout` L1–L4 全绿；`check_mulu_s` 坏链 0；`check_taskfile_invariant` 0 违例。
