# 阅读站构建与阅读体验（实现说明）

本目录是本地 VitePress 双语阅读站的实现。**本文是说明，不是规则**：与 `rules/` 冲突时以 `rules/` 为准；命令与门禁口径见 `rules/05-ci-and-tools.md`。构建配置变更请同步本文。

## 构建壳与分层（ADR-0055）

内容仓（本仓）与构建壳（`taophilosophy.github.io`）的分工是契约面，两侧改动都不得越线：

| 归属 | 位置 | 内容 |
| ---- | ---- | ---- |
| 构建壳 | `taophilosophy.github.io` 根 | `package.json`（唯一依赖声明；锁文件不入库、`.gitignore` 排除）、`node_modules/`（本地现装，不用缓存）、GitHub Pages 工作流 |
| 本仓 · 配置层 | `.vitepress/config.mts`、`math-plugin.mjs`、`config.build-check.mts` | 站点元数据、`srcExclude`、SUMMARY 解析、双语配对、侧栏、markdown 规则、`transformPageData` |
| 本仓 · 主题层 | `.vitepress/theme/` | 唯一引入字体、样式与终端组件的目录；只依赖 `vitepress`、`littlefoot` 与字体包 |
| 本仓 · 构建前置 | `.vitepress/prepare-*.mjs` | 生成 `public/mathjax/` 与 `.vitepress/git-stamps.json`，由壳脚本按序调用 |
| 本仓 · 静态资源 | `public/` | favicon、logo、mathjax（生成物，gitignore） |

* **主题层与配置层去耦合**：配置层不 import 主题层、不写视觉样式；主题层不 import 配置层、不读 `config.mts` 的内部变量。两者只通过 VitePress 约定接口交互（frontmatter、`themeConfig`、`lastUpdated`）。删掉 `theme/` 仍能构建（退回默认主题），删掉 `config.mts` 则站不成立——不对称是有意的。
* **依赖只在壳里声明**：本仓根不再有 `package.json` / `bun.lock`（`.gitignore` 已排除）。新增依赖改壳的 `package.json` 后 `bun install`；不在本仓跑包管理。

## 命令（包管理统一 bun，ADR-0014）

```sh
git clone https://github.com/taophilosophy/taophilosophy.github.io   # 构建壳
cd taophilosophy.github.io && git submodule update --init && bun install
bun run dev      # 开发服务器（root=docs）：http://<局域网 IP>:81
bun run build    # 静态构建 → docs/.vitepress/dist，含 pagefind 全文索引
bun run preview  # 预览构建产物（不跑 prepare-*）
```

* 要预览**本机工作树**（而非子模块的远端提交）：在壳里把 `docs/` 换成指向本仓的目录联接（Windows：`mklink /J docs C:\Users\ykla\Documents\SEP-CN`），再跑同三条命令；依赖仍由壳提供。
* `npm` 不是受支持路径：Windows 下 npm 用 cmd.exe 执行 script，不识别 `NODE_OPTIONS=` 前缀（ADR-0014）。
* 运行时基线（ADR-0032）：Node ≥ 26（本地验证 26.13.0；Vite 8 要求 `^20.19 || >=22.12`）、bun ≥ 1.4（本地 1.4.4）。`build` 需约 8 GB 空闲内存（壳脚本以 `NODE_OPTIONS=--max-old-space-size=12288` 起构建；内存不足时 V8 以 `FATAL ERROR: Reached heap limit` 退出 134），并行跑其它会话时先腾内存。
* CI（壳的 `push_deploy.yml` / `sync_deploy.yml`）构建前 `cp docs/README.md docs/index.md`：VitePress 把 `README.md` 编成 `README.html`，Pages 站点根需要 `index.html`。该文件只在 CI 生成，不入库。

## 构建期准备（prepare-*.mjs）

* `prepare-assets.mjs`：把 `mathjax/tex-svg.js` 复制到 `public/mathjax/`（specs/024：MathJax 4.1.3 起组件文件在包根，v3 的 `es5/` 目录已取消）。依赖可能被 hoist 到壳根，故脚本自 `.vitepress/` 起按 Node 解析顺序逐级向上找 `node_modules/mathjax`，写回固定为本仓 `public/`——与 cwd 无关。找不到即 exit 1，提示在壳根 `bun install`。
* `prepare-gitstamps.mjs`：一次全量 `git log` 生成 `.vitepress/git-stamps.json`（路径→最后提交时间 ms），`transformPageData` 据此注入 `lastUpdated`，免去内置逐页查询。派生物，gitignore。子模块浅克隆时历史只有一条提交，页脚时间统一为子模块提交时间，属已知限制。
* `preview` 不跑这两步，故 `preview` 前须至少 `build` 过一次。

## 分片构建（CI 并行，2026-11-16）

单次全量构建的固定成本结构：打包约 3.5 min、渲染 4326 页约 15 min、pagefind 索引约 5.3 min。CI 把渲染摊到四个分片并行：

* `SEP_SHARD=ad|ek|lp|qz` 时每片只渲染约 1/4 页面（按实测页数均衡：a–d 1165、e–k 1050、l–p 1196、q–z 915，中英两侧同片）。根级页面（README、`mu-lu-s`、两本登记册、SUMMARY）与 `1/`、`qian-yan`、`guan-yu`、`jian-yi-shu`、`fang-fa-lun` 只进 `ad` 片。产物写 `.vitepress/dist-<shard>`，pagefind 不在分片内跑。
* 分片模式**关闭死链检查**（`ignoreDeadLinks: true`）：跨片链接在本片必然"缺失"。链接完整性由不设 `SEP_SHARD` 的全量构建负责（本地收工前照旧 `bun run build`）。
* `.vitepress/merge-shards.mjs` 依次：叠加各片 dist → `hashmap.json` 取并集（客户端在本片哈希表缺项时会回退 fetch `/hashmap.json` 重试，并集后跨片跳转正常）→ 拼接各片 `sitemap.xml` 的 `<url>` 条目 → 对整份 dist 跑一次 pagefind（参数与插件一致：`--exclude-selectors "div.aside, a.header-anchor"`）。
* 实测（本机）：单分片打包＋渲染 3.3–4.2 min；四片并行＋合并（pagefind 5.3 min）约 13 min，对比全量 24 min。CI 侧 `push_deploy.yml` / `sync_deploy.yml` 均为 matrix → merge → deploy 三段。

## dev 服务器

* 固定 `host: '0.0.0.0'`、`port: 81`、`strictPort: true`——端口被占用即启动失败，不自动换端口。
* `watch.usePolling: true`（1500 ms）：本仓库所在盘的 `ReadDirectoryChangesW` 会报 UNKNOWN 错误；`en/`、`tools/`、`tasks/`、`baseline/`、`specs/` 等大目录不监听。
* dev 端 `index.md → README.md` 中间件：VitePress 2.0 alpha 的 dev 只按 `/index.md` 解析页面，本仓库沿用 GitBook 的 `README.md` 作首页与目录首页；中间件把请求改写为同路径的 `README.md`（存在时），使 dev 与 build 行为一致。

## 页面范围（srcExclude）

`en/`、`specs/`、`.specify/`、`tools/`、`tasks/`、`baseline/`、`script/`、`state/`、`rules/`、`.github/`、`.zcode/`、`.qoder/`、`AGENTS.md`、`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`yuanwen/SUMMARY.md`、`yuanwen/SUMMARY-en.md` 不参与构建。**新增治理/管线目录时必须同步补 `srcExclude`**，否则其中的 md 会成为站点页面并被全文搜索索引（ADR-0015）。

## Markdown 处理

* `markdown.attrs = false`（2026-10-28 裁定）：全库以 `^{…}`/`_{…}` 作上下标约定，正文含大量字面花括号（如 `^{−1}`）。attrs 插件会把尾随花括号吞成 HTML 属性——轻则上下标静默丢失（`u(a_{1})` 渲染成 `u(a`），重则非法属性名（`−½`）炸掉 Vue 模板编译，整页构建失败。**不要重新开启 attrs**。
* 行内代码统一注入 `v-pre`（vuejs/vitepress#3724）：代码里的 `{{ }}` 与标签不被 Vue 当模板处理。
* 数学：`math-plugin.mjs` 把 `$…$`、`$$…$$`、`\(…\)`、`\[…\]` 保护为哨兵 token，公式内容原样；MathJax 4.1.3 的 `tex-svg` 离线加载（`/mathjax/tex-svg.js`，specs/024 由 3.2.2 升级；v3 配置原样兼容），`startup.typeset: false`，由主题组件 `MathTypesetter`（挂载于 `doc-top`）在路由变化后手动排版，避免 SPA 切换漏排。

## 双语配对与侧边栏

* 中英两侧 SUMMARY（`SUMMARY.md`、`yuanwen/SUMMARY.md`）各自解析为扁平条目序列，**按序号对齐**；仅当清理转义后的标题完全相等、且英文侧路径匹配 `yuanwen/*.md` 时才配对。标题不一致即跳过（结构漂移保护），不会错配。
* 配对结果由 `transformPageData` 注入 frontmatter `enPath` / `zhPath`，供双语切换与对照 iframe 使用。
* 中文侧边栏由 SUMMARY 的 `##` 分组与缩进生成（组内折叠）；SUMMARY 目前无 `##` 分组时段落平铺。英文侧边栏按字母目录分组（`A–Z`，取自 `yuanwen/<letter>/`）。

## 搜索

* 构建（build）：`vitepress-plugin-pagefind` + `chineseSearchOptimize`，产出静态全文索引。
* 开发（dev）：无 pagefind 产物，退回 VitePress 内置 MiniSearch；站点自定义 `*_splitIntoSections`——剥离公式哨兵，单节上限 1500 字符、单页上限 3500 字符（原文库 2300+ 页、正文约 240 MB，整页索引会超出 V8 字符串上限）。

## 分块体积（2026-11-16 实测）

* 依赖块很小：framework 111 KB、theme 101 KB、littlefoot 7 KB（未压缩）。
* 超过 500 KB 警告线的全是「数据体积」块，且 2.0 无拆分手段：`chunks/metadata` 1.2 MB（`__VP_HASH_MAP__` 全站路由哈希表＋站点数据；metaChunk 自 2.0.0-alpha.19 起默认开启，页面元数据已按页拆出）、`chunks/assets` 1.0 MB（全站图片 URL 映射）、登记册与超长词条的单页模块（`shu-yu-biao` 1.3 MB 等）。
* 因此 `config.mts` 的 `vite.build.chunkSizeWarningLimit` 定为 1600（默认 500），并在配置里写明豁免依据；低于 1600 的块仍正常告警。`manualChunks` / `rolldownOptions.codeSplitting` 只能重排依赖，对上述块无效。

## 主题与字体

* 入口 `.vitepress/theme/index.ts`：`extends: DefaultTheme`，槽位注入 `BilingualToggle`（`nav-bar-content-after`）、`MathTypesetter` 与 `EntryMatter`（`doc-top`）、`SepFooter`（`doc-bottom`）、`FootnoteEnhance`（`layout-bottom`），并导入 `custom.css`、`sep-theme.css`、`vp-compat.css`。
* 层内分工：视觉令牌与换皮在 `custom.css` / `sep-theme.css`；唯一引用 VitePress 内部类名的桥接层是 `vp-compat.css`（升级 VitePress 只查这一层）；组件不读 `config.mts`，只消费 frontmatter 与 `useData()`。
* 字体全部离线自托管（`lxgw-wenkai-*-webfont` 依赖，不依赖外部 CDN）：正文与标题常规字重用 `LXGW WenKai Screen`（屏幕阅读版只有 400 一档）；标题粗体取自 `LXGW WenKai Bold`；代码用 `LXGW WenKai Mono`（内嵌英文等宽字形）。
* 品牌色在 `custom.css` 的 `--vp-c-brand-*` 变量：浅色 `#ff0072`、深色 `#a8e6cf`。改色只改变量，组件里不要硬编码色值。
