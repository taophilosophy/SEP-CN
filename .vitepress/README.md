# 阅读站构建与阅读体验（实现说明）

本目录是本地 VitePress 双语阅读站的实现。**本文是说明，不是规则**：与 `rules/` 冲突时以 `rules/` 为准；命令与门禁口径见 `rules/05-ci-and-tools.md`。构建配置变更请同步本文。

## 命令（包管理统一 bun，ADR-0014）

```sh
bun install      # 依赖（bun.lock 唯一锁文件）
bun run dev      # 开发服务器：http://<局域网 IP>:81
bun run build    # 静态构建（.vitepress/dist），含 pagefind 全文索引
bun run preview  # 预览构建产物（不跑 prepare-assets）
```

`npm run dev` 不是受支持路径：Windows 下 npm 用 cmd.exe 执行 script，不识别 `NODE_OPTIONS=` 前缀（ADR-0014）。

## 构建期准备（prepare-assets.mjs）

`dev` 与 `build` 先运行 `.vitepress/prepare-assets.mjs`：把 `node_modules/mathjax/es5/tex-svg.js` 复制到 `public/mathjax/tex-svg.js`（该目录 gitignore，克隆后首次运行自动重建）。缺 `node_modules` 时脚本直接 exit 1 并提示 `bun install`。`preview` 不跑此步骤，故 `preview` 前须至少 `build` 过一次。

## dev 服务器

* 固定 `host: '0.0.0.0'`、`port: 81`、`strictPort: true`——端口被占用即启动失败，不自动换端口。
* `watch.usePolling: true`（600 ms）：本仓库所在盘的 `ReadDirectoryChangesW` 会报 UNKNOWN 错误；`en/`、`tools/`、`tasks/`、`baseline/`、`specs/` 等大目录不监听。
* dev 端 `index.md → README.md` 中间件：VitePress 2.0 alpha 的 dev 只按 `/index.md` 解析页面，本仓库沿用 GitBook 的 `README.md` 作首页与目录首页；中间件把请求改写为同路径的 `README.md`（存在时），使 dev 与 build 行为一致。

## 页面范围（srcExclude）

`en/`、`specs/`、`.specify/`、`tools/`、`tasks/`、`baseline/`、`script/`、`state/`、`rules/`、`.github/`、`.zcode/`、`.qoder/`、`AGENTS.md`、`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`yuanwen/SUMMARY.md` 不参与构建。**新增治理/管线目录时必须同步补 `srcExclude`**，否则其中的 md 会成为站点页面并被全文搜索索引（ADR-0015）。

## Markdown 处理

* `markdown.attrs = false`（2026-10-28 裁定）：全库以 `^{…}`/`_{…}` 作上下标约定，正文含大量字面花括号（如 `^{−1}`）。attrs 插件会把尾随花括号吞成 HTML 属性——轻则上下标静默丢失（`u(a_{1})` 渲染成 `u(a`），重则非法属性名（`−½`）炸掉 Vue 模板编译，整页构建失败。**不要重新开启 attrs**。
* 行内代码统一注入 `v-pre`（vuejs/vitepress#3724）：代码里的 `{{ }}` 与标签不被 Vue 当模板处理。
* 数学：`math-plugin.mjs` 把 `$…$`、`$$…$$`、`\(…\)`、`\[…\]` 保护为哨兵 token，公式内容原样；MathJax 3 的 `tex-svg` 离线加载（`/mathjax/tex-svg.js`），`startup.typeset: false`，由主题组件 `MathTypesetter`（挂载于 `doc-top`）在路由变化后手动排版，避免 SPA 切换漏排。

## 双语配对与侧边栏

* 中英两侧 SUMMARY（`SUMMARY.md`、`yuanwen/SUMMARY.md`）各自解析为扁平条目序列，**按序号对齐**；仅当清理转义后的标题完全相等、且英文侧路径匹配 `yuanwen/*.md` 时才配对。标题不一致即跳过（结构漂移保护），不会错配。
* 配对结果由 `transformPageData` 注入 frontmatter `enPath` / `zhPath`，供双语切换与对照 iframe 使用。
* 中文侧边栏由 SUMMARY 的 `##` 分组与缩进生成（组内折叠）；SUMMARY 目前无 `##` 分组时段落平铺。英文侧边栏按字母目录分组（`A–Z`，取自 `yuanwen/<letter>/`）。

## 搜索

* 构建（build）：`vitepress-plugin-pagefind` + `chineseSearchOptimize`，产出静态全文索引。
* 开发（dev）：无 pagefind 产物，退回 VitePress 内置 MiniSearch；站点自定义 `*_splitIntoSections`——剥离公式哨兵，单节上限 1500 字符、单页上限 3500 字符（原文库 2300+ 页、正文约 240 MB，整页索引会超出 V8 字符串上限）。

## 主题与字体

* 入口 `.vitepress/theme/index.ts`：`extends: DefaultTheme`，在 `nav-bar-content-after` 注入 `BilingualToggle`、`doc-top` 注入 `MathTypesetter`，导入 `custom.css`。
* 字体全部离线自托管（`lxgw-wenkai-*-webfont` 依赖，不依赖外部 CDN）：正文与标题常规字重用 `LXGW WenKai Screen`（屏幕阅读版只有 400 一档）；标题粗体取自 `LXGW WenKai Bold`；代码用 `LXGW WenKai Mono`（内嵌英文等宽字形）。
* 品牌色在 `custom.css` 的 `--vp-c-brand-*` 变量：浅色 `#ff0072`、深色 `#a8e6cf`。改色只改变量，组件里不要硬编码色值。
