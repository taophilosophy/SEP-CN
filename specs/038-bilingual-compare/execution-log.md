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
6. **构建与门禁**：`SEP_SHARD=ek bun --bun x vitepress build docs`（壳仓入口，死链检查开启、无新增豁免）**通过**，`build complete in 166.52s`，唯一告警为既有的“块 >1600 kB”（specs/037 已定 `chunkSizeWarningLimit: 1600`，数据体积块无拆分手段）。`python tools/check_all.py` 11 项、失败 3，均为存量且与本次改动无关：①直角引号 124 处 / 10 文件（ADR-0059/0060、`shu-yu-biao.md`、`z/zhu-xi.md` 等；本次新增文档全改弯引号，计数由 126 降至 124）；②原始物分歧账 `en/zhu-xi`（登记后又改动，另有会话在办）；③单测 `test_check_summary_headers.AliasFragmentTest.test_dangling_fragment_is_hard_error`（ADR-0057/0060 别名片段门禁改 baseline 全集后测试未同步；本次未触 `tools/`）。

## 2026-11-16 补：英文原文页的回程入口

**起因**：收尾观察发现 `transformPageData` 注入的 `zhPath` 全站没有消费方——旧 `BilingualToggle` 与本组件都只认 `enPath`，从中文页“新窗口”打开的英文原文页没有任何回中文的入口（浏览器后退之外）。

**改动**：`BilingualCompare.vue` 增 `zhPath` 计算属性；模板分两路——`zhPath` 存在（英文页）时导航位只渲染“⇦ 中文译文”药丸（`.bili-btn` 的 `<a>` 形态，`withBase(zhPath)`），不渲染对照面板与“目录/对照原文”按钮；`enPath` 存在（中文页）时维持原样。`custom.css` 的 `.bili-btn` 补 `text-decoration: none`（`<a>` 形态防下划线）。

**验证**（dev，`--dump-dom`）：
- `/yuanwen/a/abduction` → `bili-toggle-wrap` 内仅 `<a class="bili-btn" href="/a/abduction" title="回到该词条的中文译文">⇦ 中文译文</a>`，`bili-panel` 不出现；同页带 `?bili=1` 也不开面板。
- `/yuanwen/z/zhu-xi` → 同上（长条目同样配对成功）。
- `/a/abduction` → 仍是“⇤ 目录 ⇔ 对照原文”两钮＋面板（无回归）。
- 无配对页 `/guan-yu`、`/yuanwen/README` → 两种入口都不出现（`bili-toggle-wrap` 缺席）。

## 2026-11-16 未做/另案

- 不复刻参考站设置面板（字号、行距、背景亮度、繁简切换）：spec §1 非目标。
- 交错态不做双侧滚动互驱与句级高亮（英文块已随中文流排布，互驱只会抖动）；`bili-active` 在交错态不标。

## 2026-11-16 移动端适配返工（用户：移动端适配有问题）

**量测方法**：Chrome headless 的 `--window-size` 有 526px 最小宽度，真机 390 量不出来；改用 CDP（`--remote-debugging-port` + `Emulation.setDeviceMetricsOverride`，Node 全局 WebSocket 直连，脚本见 `results/mob.mjs`）在 390×844 / 768×1024 / 1280×860 三档真视口量测＋截图。此前用“iframe 装 390px 页面”的土办法有两个陷阱：站点自带 `html.in-iframe` 会把导航/侧栏全隐藏（量不到导航位按钮），截图也拍不出内容。

**查出的六个问题**：

| # | 现象（390×844 实测） | 根因 | 修法 |
| - | ---- | ---- | ---- |
| 1 | 手机上根本没有对照入口：`.bili-toggle-wrap` 在 DOM 里但 rect 全 0 | ≤959px 时 VitePress 换 VPLocalNav，`nav-bar-content-after` 槽位被塞进 `display:none` 的 VPNavBar，祖先隐藏后 `position:fixed` 也不渲染 | 窄屏 `Teleport to="body"` 出导航栏，改右下浮窗（`.bili-toggle-wrap` 固定定位、胶囊底）；桌面 `:disabled` 保持原位 |
| 2 | 点开“对照”只见满屏英文，中文完全不可见，标签还写着“⇔ 左右” | 窄屏 `.bili-side .bili-panel{left:0}` 全屏覆盖，且左右两栏在 390px 宽下本就不成立 | 新增 `effLayout`：窄屏 `side` 等价 `stack`（上下分屏）；布局循环在窄屏只在 上下 ⇄ 交错；标签跟随 `effLayout` |
| 3 | 文档末尾被控制条盖住：`padding-bottom` 写死 52px，手机条实际 67–95px | 条内 8 个控件在 375px 下折 2–3 行 | `ResizeObserver` 量条高写 `--bili-bar-h`，CSS `calc(var(--bili-bar-h,40px) + 12px)`；注意必须取 `borderBoxSize`（`contentRect` 扣掉 padding/border，83px 的条只报 70px） |
| 4 | “仅英文”在窄屏只有下半屏有内容，上半屏空白 | `body.bili-show-en:not(.bili-bottombar) .bili-panel` 只写了 `left:0;width:auto`，没钉 `top`，被同特异性的 `.bili-stack .bili-panel{top:50%}` 后声明压过 | 四处定位全钉（top/right/bottom/left 0） |
| 5 | ≥1280px 桌面双栏中文列左移出界（.content-container x=-7、正文 x=13、锚点被裁） | VitePress 在 `min-width:80rem` 给 `.content` 设了 `min-width:40rem`（640px），而双栏中文列只有 ~561px | 侧栏让位规则里补 `min-width:0;width:auto`（此前用 1254px 视口量测，没触发这条） |
| 6 | 英文栏内标题锚点“¶”被顶出左缘 8–16px | 注入文档的 `.header-anchor` 带负外边距，而 `.bili-doc` 左内距只有 16–28px | 对照面板内的锚点直接隐藏（面板不是导航来源）；中文侧锚点保留 |

**返工后的实测**（`results/mobile-390-*.png`、`tablet-768-compare.png`、`desktop-1280-*.png`）：

- 390×844 关闭态：导航可见、右下浮窗 `[274,791,104,40]`；`hOverflow=0`；全页无溢出元素（offCount 0，此前 181 里都是抽屉侧栏的正常负偏移）。
- 390“对照”：body `bili-stack`，英文占下半 422px、控制条 83px、正文留白 422px，中文列 `[24,32,342]`，浮窗隐藏。
- 390 交错/仅中文：底栏 83px、body 留白 95px（= 条高 + 12）、交错 94 个英文块。
- 390 仅英文：面板 `[0,0,390,844]` 铺满、正文 760px。
- 768：`side` 同样降为上下（条 46px 单行）、中文 688 居中。
- 1280/1440：双栏恢复 `bili-side`，中文列 `[52,126,521]`/`[52,126,601]`，与英文栏 `[625,…]`/`[705,…]` 不重叠，`offCount=0`。
- 真机视口下所有状态 `hOverflow=0`（320/390/414/768/1280 全测）。

## 2026-11-16 公式尺寸（用户：移动端公式约为汉字 50% 高，改成一样大或 95%）

**根因**：MathJax 的 SVG 输出把宽高写成 `ex` 单位，`1ex` 取的是**元素字体**的 x-height。正文用的霞鹜文楷 Screen 在浏览器里报的 x-height 只有 0.2285em（实测 16px 字号：`1ex`=3.66px，对照 serif 8.22px、sans 8.69px、等宽体 7.48px），所以公式只画到 MathJax 设计尺寸的约 46%。同一 16px 下汉字墨迹高 15px、拉丁小写 9px，而公式 x-height 仅 8px ≈ 汉字的 53%——与用户观感一致。**桌面端同样偏小**（390 与 1280 两档量得的 `ex` 完全相同），只是手机上了紧挨汉字更显眼。

**处置**（`.vitepress/theme/custom.css` 数学段）：
1. 公式容器字体固定到自托管的 `--vp-font-family-mono`（x-height=0.4678em，各平台一致，不受系统字体与加载失败影响）——先把 `ex` 变成确定量；
2. 容器 `font-size: 1.8em`，于是 `1ex` = 0.4678×1.8×16 = 13.5px，即汉字墨迹（15px）的 **90–95%**。倍率是唯一的调参处。

**实测**（CDP 真机视口，`b/boolalg-math`、`b/bohr-correspondence`）：
- 行内公式 svg 高：修前 4–5px → 修后 14px；汉字墨迹 15px，比值 0.93（修前 0.53）。
- 行间公式容器计算字号 28.8px（=1.8×16），display 块仍居中（`text-align:center`），多行 `align*` 块高 149px。
- 页面级横向溢出仍为 0；宽公式在 `.math-tex mjx-container`（`overflow-x:auto`）内滚动——放大后手机上更易触发（实测 627px 宽式在 342px 容器内滚动），这是放大的必然代价，保留滚动而非缩字号。
- 行距：正文 `line-height:28px` 不变；含上下标的行内公式会把该行撑到约 33px（原本就比正文行高的上下标结构），纯文字行不受影响。
- 对照面板注入的英文文档共用同一 `.math-tex` 规则，两侧同步生效。
- 凭证：`results/math-mobile-390.png`、`results/math-desktop-1280.png`。

## 2026-11-17 主题全量矩阵测试（用户：全量测试找 bug＋功能建议；适配 720p/1080p/2K/4K、最新 iPhone/iPad、小米旗舰）

**覆盖面**：19 视口 × 6–8 态 × 亮/暗（`results/full-matrix-20261117.json`，跑批日志 `matrix-run4.log`，截图 `matrix-*.png`）。
视口：1280×720、1920×1080、1707×960（2K@150%）、2560×1440、3840×2160；iPad mini 744×1133、Air 820×1180、Pro 13 竖 1032×1376／横 1376×1024、Air 横 1180×820；iPhone SE 375×667、15/16 393×852、16 Pro 402×874、16 Pro Max 440×956；安卓 360×800、小米 15 393×873、小米 Ultra 412×915、430×932、手机横屏 852×393。页面：首页／`a/abstract-objects`（公式）／`a/axiom-choice`（公式＋30 行表格）／对照 side·inter·en-only／`yuanwen` 原文页回程。

**测量陷阱（先行记录，此前两轮结论被它污染）**：Chrome 157 的 CDP `Emulation.setDeviceMetricsOverride` 在带 `mobile:true` 时会被词条页（MathJax 隐藏 iframe）重置并钳制到 524px——前几轮手机实测全在 524 宽下进行，`<524` 的溢出根本看不见。解法：`mobile:false`（本主题响应式全走 CSS 媒体查询，与 mobile 旗标无关）＋导航后重发 override＋每视口独立标签页。前一轮（run2/run3）与本轮（run4）的差异即此。

### 发现并修复的 bug

| # | 症状（真机视口实测） | 根因 | 处置 |
| - | ---- | ---- | ---- |
| 1 | **所有 ≤440px 手机整页横溢 84–164px**（zh/对照/交错/原文页全态，axiom 达 303–340px） | 长公式 svg 按自然尺寸排（实测 37.1ex≈500px），而 `.math-tex` 是 inline 元素，其上的 `overflow-x:auto` **对 inline 不生效**——旧记录「宽公式在容器内滚动」实际从未生效，只因旧测量在 524px 钳制宽度下做，500px 公式恰好装得下 | `.math-tex` 改 `inline-block; max-width:100%; overflow-x:auto`（custom.css 数学段）：超宽公式在自身盒内滚动，页级溢出归零 |
| 2 | **2K/4K 对照双栏行长失控**：中文列 1841px（2560 下 1201、1920 下 881），英文面板 1919px——单行 100–190 字符不可读 | side 让位规则把 `.content-container` 的宽度限制全拆了，且无大屏上限；仅英文态英文文档撑满整窗（3840px） | `vp-compat.css` 增 `@media (min-width:1280px)`：side 中文列与 `body.bili-mode .bili-doc > .vp-doc`（面板＋仅英文共用）一律 `max-width:43rem; margin-inline:auto`，在各自栏内居中。≤1279 半屏本就不超 688px，维持原生满宽 |

### 复验（run4，修复后全量重跑）

- **19/19 视口全态 `hOverflow` 干净**（唯一非零值是桌面滚动条的 −15）；axiom 表格在手机上是容器内滚动（合法形态），页级不溢出。
- 4K：side 中文列 `[609,112,688]`（居中）、面板内英文 `.vp-doc` 688 居中、仅英文内文档 688 居中（宿主仍是整屏滚动容器）；1280 半屏布局不变（561px，帽不触发）。
- Esc 关闭 19/19 零残留（body 类清空、面板移除）；暗色 `html.dark`＋暖黑底正常；`--bili-bar-h` 与实测条高全视口一致（iPad Pro 竖屏折行 91px 也正确反馈）；触摸目标 ≥30.75px（平板/手机），桌面 19.5px 属鼠标常态。
- 交错块/复制按钮/回程入口（en 页右下浮窗 `[634,1080,98,40]` 等）各视口在位。
- 行内公式改 inline-block 后基线完好（`matrix-mathfix-393.png`）：svg 高 21–30px vs 行高 28px，与修前一致。

### 判定不是 bug 的两项（防重查）

- **VPSidebar 宽度随视口增长**（1920 下 505px、3840 下 1465px）：VitePress 2.0-alpha 在 `≥90rem` 用 `calc((100% - (var(--vp-layout-max-width) - 4rem)) / 2 + var(--vp-sidebar-width) - 2rem)` 把侧栏推宽以让正文居中——实测数值与公式精确吻合，上游设计。
- **iPad Pro 竖屏（1032px）控制条折两行（91px）**：条内 8 控件在半屏面板宽度下放不下；`--bili-bar-h` 已如实反馈，正文留白随之自适应，可用性无损。
