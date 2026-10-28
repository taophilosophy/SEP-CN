# 0014. 包管理统一 bun，弃用 npm

状态：accepted | 日期：2026-10-28

## 背景

站点依赖一直以 `bun.lock` 为唯一锁文件（Bun 生态，镜像源 registry.npmmirror.com），但流程中仍残留 npm 用法：`package.json` 的 dev/build script 用 Unix env 前缀语法（`NODE_OPTIONS=… vitepress dev`）；`md-padding.yml` 用 `npm i -g` + `npx`；`rules/05` 与 `CONTRIBUTING.md` 让贡献者直接调用 `markdownlint-cli2`（隐含 npm 全局安装）。

2026-10-28 实测：Windows 下 npm 以 cmd.exe 执行 script，不识别 env 前缀语法，`npm run dev` 必败（报 `'NODE_OPTIONS' is not recognized`），局域网阅读站无法经 npm 启动；`bun run` 的内置 shell 跨平台支持该语法，`bun run dev` 即正常起站。用户裁定弃用 npm。

## 决策

1. **本仓库一切包管理与脚本执行只用 bun**：装依赖 `bun install`，跑脚本 `bun run <script>`，一次性调用 CLI 用 `bunx <pkg>`；不使用 npm / npx / yarn / pnpm，不生成它们的锁文件（`bun.lock` 唯一权威）。
2. `package.json` scripts 维持 Unix env 前缀写法（bun 跨平台可执行），不为 cmd.exe 兼容而改写。
3. `md-padding.yml` 改用 `oven-sh/setup-bun` + `bunx md-padding@latest`；本地 markdownlint 调用统一 `bunx markdownlint-cli2`（`rules/05-ci-and-tools.md`、`CONTRIBUTING.md` 同步改写）。
4. 历史文档（specs 执行记录、`qian-yan/` 日志等）中的 npm 记述按"当时事实"保留，不改写。

## 后果

* Windows 本机 `bun run dev` 即可启动局域网阅读站（`0.0.0.0:81`，见 `.vitepress/config.mts` server 段）；`npm run dev` 不再是受支持路径。
* `md-padding.yml` 移除 setup-node 与全局安装两步，改为单步 bunx，md-padding 改在 bun 运行时下执行（格式化行为不变）。
* 既有经 npm 全局安装的工具（如 markdownlint-cli2）不强制卸载，但受支持的调用方式只剩 bunx。
* `.gitignore` 中 npm 杂物忽略项保留（防误提交）。
