# T207 S16 收口

- 日期：2026-11-27。
- 本仓提交（分批推送，规避单次大包 408）：
  1. `622a1540d` 互换 `en`／`yuanwen` 目录名；
  2. `c59a37674` 根级中文目录与登记册归集 `zh/`、删除 `开源翻译.md`；
  3. `05bb27c34` 同步 `baseline` 与 `tasks` 的 `zh`／`en`／`yuanwen` 路径；
  4. `e67b12775` 更新 `.vitepress`、工具链、规则与 `specs` 路径；
  5. 本卡收口提交。
- 壳仓：`873cd1a` 更新 `README.md` 布局说明并推进 `docs` 子模块指针；已推送。
- 起始 tag：`batch/064-migrate-start`（`ae5ebdfe4`）；结束 tag：`batch/064-migrate-end`（本卡提交）。
- 门禁：`check_all` 23/23；`check_layout` L1–L4 全绿；`check_mulu_s` 坏链 0；单元测试全绿；VitePress ad 分片构建成功、无死链。
- 回退：按 T202 裁定使用 Git 历史；起始 commit `df3dce234b2fed79903eb304939ab7cda4674ab8`。
