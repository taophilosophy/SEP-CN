# 后续布局调整：yuanwen/ → html/（2026-11-27）

- 用户指令：把 `yuanwen` 目录改名为 `html`，同步更新周边；至多批准 5 个滚动子代理。
- 执行：主代理 `git mv yuanwen html`；3 个子代理分别更新 `rules/`＋`AGENTS`／`README`／`.vitepress/README.md`、`specs/001/005/064`＋壳仓 `README.md`、`tools/tests/**`；主代理更新 `tools/`、`baseline/`、`.vitepress/config.mts`、`prepare-gitstamps.mjs`、`rules/layout.json`、补丁池。
- 语义：`html/` = 原始抓取 HTML（ADR-0062 冻结）；`en/` = Markdown 转换镜像；`zh/` = 中文正文与登记册。`tools/yuanwen.py` 模块名与 baseline `yuanwen` 字段保留，仅目录路径改 `html/`。
- 数据：`baseline/entries.json` 4960 条 `files[].path` 改 `html/...`；5 个补丁的 `file`/diff 头改 `html/...` 并再生 INDEX；`baseline/mulu-map.json` 不受影响。
- 站点：`srcExclude` 与 `watch.ignored` 改 `html/**`；`prepare-gitstamps` 排除 `html/`；页面 URL 不变（`/zh/…`、`/en/…`）。
- 验证：`check_all` 23/23 全绿；单元测试全绿；`SEP_SHARD=ad bun run docs:build` 成功（111.69s，无死链）；`/zh/a/abduction.html`、`/en/a/abduction.html` 均在。
- 历史文本：`rules/adr/**` 按只追加不改；`specs/064/results/t202/t206` 与旧→新映射表保留旧名以供追溯。
