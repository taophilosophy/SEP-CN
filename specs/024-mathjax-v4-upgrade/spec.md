# 024 MathJax v4 升级（阅读站数学渲染 3.2.2 → 4.1.3）

## 背景

- SEP 原文页自带 MathJax 2.7.2（`en/` 不可变抓取物，管线不执行其 JS，不涉本升级）。
- 阅读站渲染链：`mathjax@3.2.2`（npm）→ `prepare-assets.mjs` 复制 `node_modules/mathjax/es5/tex-svg.js` 到 `public/mathjax/`（gitignore，构建期重建）→ `theme/mathjax-loader.ts` 按需注入 + `startup.typeset:false` + SPA 路由后手动 typeset → `theme/math-jax-config.ts` 配置（`\( \)`/`$ $` 双定界符、`svg.fontCache:'global'`、`enableMenu:true`）。
- `math-plugin.mjs` 哨兵管线只依赖 `$`/`$$` 定界符约定，与 MathJax 版本解耦。
- v4.0.0 于 2025-08-05 发布（现 4.1.3）；npm 包名不变（`mathjax`，4.1.3 在列，2026-11-14 实查）。官方口径：v3 配置大多原样可用；组件文件同名。**v4 npm 包内组件文件移至包根，`es5/` 目录取消**（2026-11-14 安装实证）。

## 目标

1. `mathjax` 依赖 3.2.2 → 4.1.3（bun.lock 唯一锁文件，bun add）。
2. `tex-svg.js` 本地组件资产换到 v4.1.3；同步修 `prepare-assets.mjs`（v4 包根路径）与 `.vitepress/README.md`。
3. `math-jax-config.ts` 按 v4 复核（实测 `typesetPromise`/`fontCache`/`enableMenu` 均在 v4 组件中，config 无需改动）。
4. 公式页浏览器冒烟渲染正确。

## 非目标

- 不动 `en/`、`yuanwen/`、译文、`math-plugin.mjs` 哨兵管线、公式定界符约定（$/$$）。
- 不引入公式构建期预排版（仍是客户端按需 typeset）。

## 验收判据

1. `bun.lock`/`package.json` 锁 4.1.3。
2. `public/mathjax/tex-svg.js` 资产为 4.1.3。
3. dev/preview 下公式最重页面（试金石：frege-theorem 711 行内公式、type-theory 243+52）浏览器渲染正常、console 无 MathJax 报错。
4. `python tools/check_all.py` 全绿。
5. pathspec 提交（只收本 spec 相关文件）。

## 外部阻塞登记（2026-11-14）

`bun run build`（全量）当前对 HEAD 为红，**与本升级无关**：他会话（specs/018 重转战役，提交 3518793f3「？」、3f2712d54「！」，2026-11-14 07:14/07:43）重转的 `yuanwen/n/nonwellfounded-set-theory.md` 与 `yuanwen/t/typelogical-grammar.md` 打破 `math-plugin.mjs` HTML 白名单的 Vue 编译假设（Element is missing end tag / Invalid end tag）。证据链：两页 dist 产物 2026-11-13 22:30（v3 + 旧内容 build 成功）→ 11-14 重转内容提交 → build 失败在 Vue 编译层；MathJax 资产是 public 静态文件运行时加载，不参与 Vue 编译，机制上与本升级无关。处置：yuanwen 产物归 018 战役管（018 裁定不得只改产物），修复点在其重转内容或 math-plugin 白名单加固，待他会话收口后复跑 `bun run build` 验证。

## 并行会话事件（复用勿重推）

本 spec 初稿与升级改动曾于 2026-11-14 被并行会话整卷（package.json/bun.lock 还原、specs/024 目录被扫、prepare-assets.mjs 回滚）——按既定对策原地重做并立即 pathspec 提交压最短窗口。specs/024 相关文件一律以 pathspec 提交，绝不 `git add -A`。

## 复核与修复闭环（2026-11-14 第二轮）

**复核**（用户指令「复核后落地修复」）：

- 全库影响面钉死：自研扫描器遍历 yuanwen 2421 个 md，protectMath 漏保护且含 TeX 命令形态共 **29 行 / 21 文件**，两种形态——`$ (A \to B) $`（首字符空白+非反斜杠开头，B 支首字符限制）与 `$1 = \#[…] $`（数字开头+尾部空格，A 支尾字符限制）。L503 仍原样在盘（022 校对未触及）。
- 报告 §6 其余项复核通过不动：dl 定义列表 yuanwen.py 已有专项（含 020 移交缺陷修复）；未知标签兜底为既有设计。

**修复**（`math-plugin.mjs` 单 `$` 定界符正则，最小改动）：

- A 支尾字符放宽：`(?:[^\s$][ \t]*)` 允许闭合 `$` 前空白，`\$(?!\d)` 保留（货币防不回归——`$150,000 and $200,000` 实测仍不配对）。
- B 支首字符放宽：`(?:[ \t]+\\)?(?:\\\$|[^\s$])` → `(?:[ \t]*[^\s$])`，涵盖原子译稿（首空白+命令）与原文圆括号两形态。

**复验三道全过**：

1. 新建 `.vitepress/math-plugin.test.mjs`（node:test 12 例）：两类缺口形态、货币守卫双例、display 块、围栏/行内代码豁免、尖括号白名单、哨兵无损还原——**12/12 过**。
2. 全库重扫 **suspect 29 → 0**（2421 文件）。
3. dev 冒烟 frege-theorem：`[data-mjx-error]` 与 `merror` **2 → 0**，受保护公式 span **1157 → 1180**（修复多护住 23 处），全部排版（mjx=1180），MathJax 4.1.3。

提交：`40c58dff0`（修复+测试，pathspec）。build 红线销账确认：023 Phase 1 收口提交 `aa1caa8b6`（全量构建绿，12G 堆）。

## 冒烟结果（2026-11-14，dev :81）

- 试金石 frege-theorem（原文侧）：MathJax **4.1.3** 加载成功（`window.MathJax.version`），1157 个 `.math-tex` span 全部排版为 1171 个 `mjx-container`，`typesetPromise` 就绪，SPA 手动排版模式工作正常，`svg.fontCache:'global'` 与 `enableMenu:true` 配置项在 v4 组件中实测存在。
- 页面 2 个 merror 归因（**既有缺口，非 v4 引入**）：L503 公式 `$1 = \#[\lambda z \, Azp \amp z\neqclose r] $`（数字开头 + 尾部 `$` 前空格）掉出 `protectMath` 货币守卫正则 A 支（要求尾字符紧随 `[^\s$]`）→ 公式裸给 markdown，`\#` 被 markdown 标点转义吃掉反斜杠 → MathJax 报 macro parameter character 错；正文 + 脚注区两份渲染各出 1 个 merror。v3 对同页同样报错（TeX 语义）。修复点：`math-plugin.mjs` A 支允许尾部空白（数字开头分支 `[^\s$]` 前容 `[ \t]*`）——留待数学/站点会话修复并回归（protectMath 单测 + 本页 merror=0 复验）。同型的 L502（数字开头 + 尾紧随）已受保护，不受影响。

## Assumptions（裁定登记）

- 2026-11-14 用户裁定「立刻升级」：阅读站 MathJax 升到最新稳定 4.1.3。
- `en/` 抓取物内 MathJax 2.7.2 保持原样（镜像语义 + 不可变口径）。
