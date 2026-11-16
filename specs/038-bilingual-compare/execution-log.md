# 执行记录（specs/038）

## 2026-11-16 重做双语比较界面（用户指令）

**指令**：中英比较界面必须重新设计，学习文言文现代汉语比较 <https://zhuangzi.5000yan.com/1.html> 等多语言比较网站的 UI。
**两问两答**：主形态＝“C 混合：双栏＋可切交错”；进入词条默认状态＝“跟随上次选择”（`localStorage`）。

**落地文件**：

- `.vitepress/theme/components/BilingualCompare.vue`（重写，632 行）：同页注入（fetch → DOMParser → `.bili-doc`），三态＋三布局，段落级双向定位、句级高亮、`j/k`、`Esc`、进度、滚动记忆、`?bili=&layout=&show=` 链接参数。
- `.vitepress/theme/bili-paragraph.ts`：新增 `docSections` / `annotateBlocks` / `blockByKey` / `interleavePlan`（纯函数，交错计划可测）。
- `.vitepress/theme/custom.css`：面板骨架（side 右半 50vw / stack 下半 / bottombar 固定页底）、英文块浅底附注样式（`rgba(128,128,128,.07)`、8px 圆角、左 3px 强调条）、三态显隐、句级 `mark` 配色、移动端折行。
- `.vitepress/theme/vp-compat.css`：specs/038 布局段（中文让位、底栏留白、仅英文独享屏幕、悬停可供性）。
- `.vitepress/config.mts`：`transformPageData` 增加 dev 联接路径归一（见下）。

**去 iframe 的连带修复（工程裁定，spec §2.3）**：原方案 iframe + postMessage 有三套跨窗口缺陷（滚动、键盘、选区），且中文侧点击无法命中英文 DOM；改为同页注入后 `en-` 前缀隔 id、相对链接按原文页 URL 解析、`MathJax.typesetPromise` 复排。

## 2026-11-16 本次会话补完的修复

| # | 缺陷（实测证据） | 修法 |
| - | ---- | ---- |
| 1 | dev 下 `enPath`/`srcMeta` 全落空：壳仓 `docs` 是目录联接，Vite 按真实路径解析后 `relativePath` 变成 `../../SEP-CN/a/abduction.md`，查表必失配（探针曾读到 `open=true enPath=undefined`） | `transformPageData` 按文本剥前导 `../` 与仓目录名段；构建态（docs 为真实目录）走原值 |
| 2 | dev 全是 SPA 外壳，`fetch(enPath)` 取不到 `.vp-doc`，面板报“英文原文载入失败” | 加 `loadViaIframe()` 兜底：隐藏同源 iframe 让英文页自行渲染后 `importNode`；构建态 fetch 成功即不产生 iframe |
| 3 | 双栏模式中文没让位：中文块 x=296..944、英文栏起于 612，正文被压在面板下 | `.content-container` 自带 `max-width:688px;margin:auto`，仅放开 `.container` 无效；外层 `padding-right:50vw` ＋ 两层容器全取消宽度限制，并清零 `.content` 的 24px 左右内边距（否则中文列左 84 / 右 52 不均） |
| 4 | 上下堆叠：文档末尾半屏永远压在英文栏下面 | `body.bili-stack.bili-mode{padding-bottom:50vh}` |
| 5 | 移动端面板整体左移 15px 出屏：`width:100vw` 含纵向滚动条宽度、右锚定后左缘落在 -15 | 改 `left:0;width:auto`（两处 100vw 规则一并收敛） |
| 6 | `Esc` 关闭后中文永远缩在左半屏：`bili-side`↔`bili-show-*` 类无条件写 body，关闭面板后残留 | `refreshClasses()` 以“对照真的开着”为前提统一切换布局/三态类（`hide-sidebar` 独立不受限） |
| 7 | 交错 / 仅中文态仍报“英 x%”（英文栏此时不可见，数字无意义） | 进度在 `layout==='inter'` 或 `show==='zh'` 时只报中文 |

## 2026-11-16 验收

**凭证**：`results/*.png`（7 张，1280×860 与 900×760）、`results/probe-20261116.json`（组件内临时探针经 `--dump-dom` 取回的量化数据；探针已删，`grep bili_probe` 为空）。

1. **四态 × 浅色 ＋ 抽查深色**：`side-light` / `side-dark` / `inter-light` / `inter-dark` / `zh-light` / `en-light` / `mobile-side-light`。像素统计（`nonwhite`/`dark`）：浅色 97–99% 非白、5–7% 深色；深色 100% 非白、89–95% 深色 —— 均为真实渲染而非空白。英文块底色实测：浅色 `rgba(128,128,128,.07)`、深色 `rgba(255,255,255,.05)`，圆角 8px、左 3px 强调条。
2. **布局几何**（1280×860 → vw 1254）：双栏 VPDoc `[0,64,612,…]`／中文列 `[52,126,508,…]`／英文栏 `[612,64,627,696]` 互不重叠；堆叠中文 688 居中、英文占下半；交错底栏 `[0,719,1239,41]`；仅英文时 VPDoc 尺寸归零、英文栏满宽 1183。
3. **交错配对**：`a/abduction` 94 个英文块、2 个退化整段（参考文献类），标题严格 z↔e 交替（`1 溯因：基本观念` ↔ `1. Abduction: The General…`）；`z/zhu-xi` 129 块 / 5 个退化段、正文高 68796 无横向溢出。退化阈值（比值 <0.5 或差 >8）在两条目上均按预期触发。
4. **交互**：滚动跟随（side：中 45% / 英 51%，双语 `bili-active` 落在同一段；stack 同）；点击跳段（英文栏 scrollTop 1025→1153 且命中同段，双侧句级 `mark` 各 1 处）；`j` 前进（scrollY 158）、`k` 回首段（预期无位移）、`Esc` 关闭（body 类清空、面板移除、中文恢复 688 居中）；关闭再开启往返正常（508 左列 ↔ 688 居中）。
5. **移动端**：900 与 420 宽双栏降为整宽面板、控制条折两行（高 67px）、无横向滚动（`overflowX=-15` 即滚动条宽度）。
6. **构建与门禁**：`SEP_SHARD=ek bun --bun x vitepress build docs`（壳仓入口，死链检查开启、无新增豁免）**通过**，`build complete in 166.52s`，唯一告警为既有的「块 >1600 kB」（specs/037 已定 `chunkSizeWarningLimit: 1600`，数据体积块无拆分手段）。`python tools/check_all.py` 11 项、失败 3，均为存量且与本次改动无关：①直角引号 124 处 / 10 文件（ADR-0059/0060、`shu-yu-biao.md`、`z/zhu-xi.md` 等；本次新增文档全改弯引号，计数由 126 降至 124）；②原始物分歧账 `en/zhu-xi`（登记后又改动，另有会话在办）；③单测 `test_check_summary_headers.AliasFragmentTest.test_dangling_fragment_is_hard_error`（ADR-0057/0060 别名片段门禁改 baseline 全集后测试未同步；本次未触 `tools/`）。

## 2026-11-16 补：英文原文页的回程入口

**起因**：收尾观察发现 `transformPageData` 注入的 `zhPath` 全站没有消费方——旧 `BilingualToggle` 与本组件都只认 `enPath`，从中文页「新窗口」打开的英文原文页没有任何回中文的入口（浏览器后退之外）。

**改动**：`BilingualCompare.vue` 增 `zhPath` 计算属性；模板分两路——`zhPath` 存在（英文页）时导航位只渲染「⇦ 中文译文」药丸（`.bili-btn` 的 `<a>` 形态，`withBase(zhPath)`），不渲染对照面板与「目录/对照原文」按钮；`enPath` 存在（中文页）时维持原样。`custom.css` 的 `.bili-btn` 补 `text-decoration: none`（`<a>` 形态防下划线）。

**验证**（dev，`--dump-dom`）：
- `/yuanwen/a/abduction` → `bili-toggle-wrap` 内仅 `<a class="bili-btn" href="/a/abduction" title="回到该词条的中文译文">⇦ 中文译文</a>`，`bili-panel` 不出现；同页带 `?bili=1` 也不开面板。
- `/yuanwen/z/zhu-xi` → 同上（长条目同样配对成功）。
- `/a/abduction` → 仍是「⇤ 目录 ⇔ 对照原文」两钮＋面板（无回归）。
- 无配对页 `/guan-yu`、`/yuanwen/README` → 两种入口都不出现（`bili-toggle-wrap` 缺席）。

## 2026-11-16 未做/另案

- 不复刻参考站设置面板（字号、行距、背景亮度、繁简切换）：spec §1 非目标。
- 交错态不做双侧滚动互驱与句级高亮（英文块已随中文流排布，互驱只会抖动）；`bili-active` 在交错态不标。
