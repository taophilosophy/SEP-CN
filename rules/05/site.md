# 站点运行（本地预演）

阅读站的构建机制是实现细节，见 [`.vitepress/README.md`](../../.vitepress/README.md)（**说明而非规则**）；本节只记命令与硬约束。

* 依赖与构建入口在壳仓 `taophilosophy.github.io`（docs/ 为指向本仓的子模块，[ADR-0055](../adr/0055-构建壳与内容仓分权.md)）：clone 壳 → `git submodule update --init` → 在壳根 `bun install` → `bun run dev` / `build` / `preview`（VitePress root = `docs`）。本仓不持有 `package.json` / `bun.lock`，不在本仓跑包管理；包管理统一 bun，不使用 npm / npx（[ADR-0014](../adr/0014-包管理统一bun弃用npm.md)）。
* dev 固定 `0.0.0.0:81` 且 `strictPort`：端口被占即启动失败，不换端口、不静默降级。
* `dev` 与 `build` 由壳脚本先跑 `.vitepress/prepare-assets.mjs`（MathJax 离线资源）与 `prepare-gitstamps.mjs`（页脚时间戳）；依赖被 hoist 到壳根时脚本自 `.vitepress/` 逐级向上解析 `node_modules`，产物固定写回本仓。`preview` 不跑这两步，故须先 `build`。
* 页面范围由 `.vitepress/config.mts` 的 `srcExclude` 控制：治理/管线目录（`rules/`、`specs/`、`tools/`、`tasks/`、`.qoder/` 等）一律不进站点；**新增此类目录须同步补 `srcExclude`**，否则会被构建为页面并进入全文搜索索引。
