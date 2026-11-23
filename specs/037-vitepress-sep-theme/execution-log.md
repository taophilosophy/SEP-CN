# 执行记录（specs/037）

## 2026-11-15 开工与裁定

- 开工检查：`sync_guard pull` 放行 0 件（HEAD=5c0b8d2e7）；`check_all.py` 全绿（exit 0）。
- 现状盘点：`.vitepress/theme/` 现有 4 槽位组件＋bili-paragraph 段落同步管线＋custom.css（436 行）＋config.mts 数据层（583 行）；功能基线见 spec 第 4 节。
- 用户三裁定（AskUserQuestion 三问三答，已入 spec §2）：①骨架=词条页仿 SEP 基础上保留左右 ToC；②字体=保留霞鹜文楷；③深浅色=保留双主题。
- 工程裁定（spec §2.4）：extends DefaultTheme 换皮架构，不自写 Layout。
- 取证：`baseline/entries.json` 含 `authors` 字段（题区作者行数据源已具备）；en/abduction 本地包含 `#article-banner`、`#pubinfo` 结构指纹；SEP css 令牌礼貌抓取待做（≥5s 间隔）。

## 2026-11-15 实现（当日完工）

**落地文件**：`.vitepress/theme/sep-theme.css`（新增，SEP chrome 层）、`custom.css`（令牌层换 SEP 配色＋bili/in-iframe 隐藏清单补 `sep-footer`/`entry-banner`/`entry-meta`）、`index.ts`（槽位重接＋修复 `lxgw-wenkai-webfont/lxgw-wenkai-bold.css`→`lxgwwenkai-bold.css` 坏导入——包内文件名无中间连字符，旧 dev 服务器因 node_modules 更新前启动而未暴露）、`components/EntryMatter.vue`（新增）、`components/SepFooter.vue`（新增）、`config.mts`（SrcMeta 增 `authors` 字段、移除 themeConfig.footer 由 SepFooter 接管）。sep 样式/entry css 原件在 results/。

**架构要点**：
- 令牌层：SEP 实测配色（cardinal #8c1515/羊皮纸 #f2ece8/横幅 #EDEBE9/页脚 #f9f5f3/发丝线 #D8D8D8），暗色为适配层（cardinal 提亮 #e08d8b 保 4.5:1+，对比度已验算）。
- body 固定红渐变 0→340px 渐入羊皮纸（SEP 同款 attachment:fixed）；顶栏双态：`.top` 类骑红带反白、滚动后羊皮纸实底（VitePress 2.0 `isTop`）。
- EntryMatter：`doc-content-before` 槽位在 2.0-alpha 不存在（VPDoc.vue 已核对），且 `doc-top` 是 aside 上方全宽位不合 SEP 版式——改 FootnoteEnhance 同款 DOM 手术，按 SEP 词条顺序“标题→作者行→斜体 pubinfo（SEP 原文措辞逐字）→EDEBE9 横幅”插到 h1 后；iframe 对照模式下 meta/横幅隐藏（镜像保持纯净）。
- SepFooter：挂 `doc-bottom`（VPContent 侧栏偏移＋VPDoc 水平内边距天然同容器缘；菜单块宽于正文列与 SEP 页脚版式语法一致）；版本钉整体迁入，信息不减；`themeConfig.footer` 移除，bili-mode/in-iframe 隐藏清单已补。
- 侧栏取羊皮纸实底＋右发丝线：透明骑渐变时顶部条目对深红带对比度不足，可读性优先（SEP 无侧栏，属本站适配层）。

**验证凭证**（浏览器实测截图 results/shot-*.png，dev:81 端口 1440×900 与 390×844）：
- 词条页浅色（题区/横幅/pubinfo/红色链接/侧栏激活态）、深色（暗红带＋暖深灰全站无破相）、页脚（菜单块＋版本钉 SHA 行＋版权）、首页浅色（slim 侧栏）；双语对照 side 模式（iframe=`/yuanwen/a/abduction?embed=1`、段落同步高亮工作正常）；bohr-correspondence 公式 111 处全排版＋littlefoot 脚注钮；搜索弹窗（Ctrl+K，羊皮纸面板红聚焦环）；移动端 390px 布局正常，贴边命中项均为 VitePress 既有隐形控件（跳转链接/汉堡钮/标题锚点），非本次引入。
- 已修：侧栏实底、导航双态、页脚 doc-bottom 迁移（layout-bottom 全宽会钻到固定侧栏下）、红带 460→340px。

**遗留观察项**（不阻断验收）：
- 词条 md 自带的“首次发表于…”译文引块与题区 pubinfo 并存（内容管线不动，信息重复但可回溯口径不同——题区为 SEP 原文措辞，引块为译者口径）。
- 404 页 / 触发 `doc-top` 数组槽位的 MathTypesetter 兼容已目验无异常。

**待 build 完成后**：页重护栏核对（词条页 dist 体积基线 +10% 内）、check_all 复跑、提交。

## 2026-11-15 独立性解耦（用户二次指令）

- 指令：“确保主题与原有 vitepress 独立，尽量避免直接改 vitepress 非配置文件”。
- 审计：VitePress 本体零改动（本会话全部提交落在 config.mts＋theme/ 自有文件；node_modules/vitepress 与默认主题未动）；换肤层有 13 处引用内部类名的选择器。
- 解耦：新建 `.vitepress/theme/vp-compat.css` 作**全站唯一桥接层**——顶栏双态（VPNavBar.top/VPLocalNav）、侧栏（VPSidebar）、页内目录（VPDocAsideOutline）、正文容器（vp-doc 链接/标题）、VPDoc padding 清零、bili-mode 与 in-iframe 两张沉浸隐藏清单全部迁入，文件头注列全依赖的内部类名清单；sep-theme.css 瘦身为纯自有类（body 渐变＋entry-*＋sep-footer）；custom.css 两张隐藏清单迁出后仅存 .vp-doc 性能块与 bili 布局改排（既有特性内聚，不动）；index.ts 桥接层最后加载。
- 验证：dev 重启后词条页计算样式逐项核对（nav 透明+top 类、footer #f9f5f3、sidebar #f2ece8、banner/meta/footer 在位）＋截图目验，与解耦前渲染一致。

## 2026-11-24 语言切换器（VitePress 原生 locales）

- 指令：“为vitepress 增加 en markdown 语言选择”；两项裁定：①走原生方案（联网读官方 i18n 文档＋按 2.0-alpha.21 node/client 源码逐层确认 useLangs→resolveLocaleLink→getLocaleForPath→resolveSiteDataByRoute 全链）②无中英配对的页面不显示切换器（与双语对照按钮 enPath 缺失不渲染一致）。
- 落地文件：`.vitepress/config.mts`（siteConfig.locales：root zh-CN＋yuanwen en，en locale themeConfig 文案英化；themeConfig.i18nRouting 接管切换目标；transformPageData 给无配对页注入 frontmatter.pageClass='no-langswitch-page'）、`.vitepress/theme/vp-compat.css`（.no-langswitch-page 藏 .VPNavTranslations 桌面 flyout 与 .VPNavScreenTranslations 手风琴两处＋头注补内部类名依赖）。主题组件与 index.ts 零改动（初版客户端 watch 打 body 类的 LangSwitchGuard.vue 方案被构建期 pageClass 方案取代后删除——SSR 即输出无首屏闪现、路由切换响应式更新）。
- 架构要点：
  - **locales 键必须是不带前导斜杠的目录名**（`yuanwen` 而非 `'/yuanwen/'`）：getLocaleForPath 用正则 `^/<键>/` 匹配 relativePath，带斜杠键拼成 `^//yuanwen/` 永不命中——首轮 ad 片构建 0 页 lang=en 后按 node 源码定位修正。
  - 切换目标 i18nRouting 函数（类型 I18nRouting）：配对页读 frontmatter.enPath/zhPath 直达（SSR href 已落静态 HTML），无配对回落 locale 首页兜底（该页切换器同时被 CSS 藏掉）。
  - en locale themeConfig 浅合并语义：对象键整体覆盖根级同名键，故 outline/editLink 须连子键一起重给（verify 脚本有断言）；search.options.locales.root 的搜索中文文案在 search 插件层级，en locale 无对应键自动回退主题默认英文。
  - 移动端事实（2.0-alpha.21 实测）：窄屏 VPNavBar 仍渲染（display:block，specs/038 时代“槽位被吞”结论已过时），hamburger 可见 → VPNavScreen 手风琴可达；VPLocalNav menu 钮打开的是 sidebar 抽屉（openSidebar）而非 nav screen。
- 验证凭证（specs/037-vitepress-sep-theme/results/）：
  - `verify-langswitch.mjs` 静态 18 项全绿（locales 结构、i18nRouting 五路映射、浅合并防丢、pageClass/css 挂钩）。
  - `SEP_SHARD=ad` 构建绿（208.7s，死链检查照常开）；产物 lang 统计 657 页 en（yuanwen）＋519 页 zh-CN；样例页 href：中文页 `/yuanwen/a/abduction`、英文页回程 `/a/abduction`、README 页 `/yuanwen/README`（首页与原文库首页配对成立）；CSS 规则 `.no-langswitch-page .VPNavTranslations,...{display:none}` 落 `assets/style.C4AAvTHc.css`；bili 双语类无回归。
  - `verify-langswitch-browser.mjs`（CDP，preview 实测）：桌面 9/9——配对页 flyout 可见（w=75）、点击 English SPA 导航到 /yuanwen/a/abduction（window 标记存活＝无整页刷新）、客户端 html lang=en、回程 SPA 导航、无配对页 /mu-lu-s 切换器 display:none 且 Layout 根含 no-langswitch-page；移动端 3/9→3/3——390px 下 nav screen 手风琴无配对页 display:none、配对页可见（h=21）。
- 踩坑记录：①`vitepress preview --outDir` 不生效（preview 按 config.outDir；不带 SEP_SHARD 时指向 dist/ 旧全量产物）——造成“hydration 失败”的半小时误判，产物 hash 对账后定位；②sirv（preview）启动时预载文件快照，构建收尾窗口启动会服务旧 HTML，改带 `SEP_SHARD=ad` 重启解决；③复合命令 `verify | tail && build` 中管道吞掉 verify 退出码，`&&` 未短路——两验证各自独立跑；④CDP 冷加载首页 hydration >1.5s，click 落在无监听阶段，等 `globalThis.__VITEPRESS__===true` 再点击（app chunk mount 前置标志）。
- 回归面：双语对照面板（BilingualCompare）零改动；body 类体系与 Layout 根 pageClass 互不干扰；页面集/死链面不变（locales 只加路径前缀语义，srcExclude/分片排除面未动）；check_all 复跑 17 项全绿。

## 2026-11-24 正文列加宽 75%＋封顶（用户裁定，覆盖 038 行长治理）

- 指令：“对主体界面加宽到屏幕的75%”；两项裁定：①全部态一起改（普通阅读态＋双语对照 side/stack/inter/仅英文各态）②75% 但封顶（cap＝1200px，≈75–80 汉字/行，specs/038 行长治理的阈度转为封顶语义——**本节登记对 specs/038“≥1280 压回 43rem”裁定的取代**，43rem 压制规则删除）。
- 落地文件：`.vitepress/theme/vp-compat.css` 单文件——:root 加 `--sep-doc-max-w: 1200px` 与 `--vp-layout-max-width: 100%`（覆盖 2.0-alpha 内置 90rem＝1440px）；≥960 段 .VPDoc（含/不含 has-aside）.content-container 与 bili-stack .vp-doc＝min(75vw, cap)；≥1280 对照段 side 双栏统一 37.5vw（两栏等宽保持对照语义，两侧容器 padding 不同按栏内 75% 会差 42px）、仅英文 75vw。
- 架构要点（三轮 CDP 实测定位）：
  - **宽度真正杠杆是 `--vp-layout-max-width`**（2.0-alpha 新令牌，内置 90rem）：VPContent 让位公式 calc((100% − layoutMax)/2 + sidebar-width) 把主体区压在 1440 内——1920 实测正文列只剩 784，content-container 的 75% 在其下物理不可达。放开为 100% 后正文列由 content-container 规则独立接管（侧栏 fixed 覆盖让位区，视觉不变）。
  - 688px 的出处是内部 scoped 规则 `.VPDoc.has-aside .content-container[data-v-…]{max-width:43rem}`（特异性 (0,4,0)）：body 元素前缀 (0,3,1) 压不住（类计数不足），`.VPDoc.VPDoc` 重复类提到 (0,4,0) 平级后靠桥接层源顺序取胜。
  - `--vp-content-max-width` 令牌在 2.0-alpha.21 **不存在**（全 dist 无定义），既有 bili-stack 规则的 fallback 688 恒生效——一并替换。
  - 旧认知修正：`.VPDoc .content-container` 自带 688px 的说法过时，实际是 has-aside scoped 43rem；`--vp-content-max-width` 同理并非现版本机制。
- 验证凭证（results/verify-width-full.mjs，单脚本 spawn preview→CDP 量测→kill 全链路，11 项全绿）：
  - 普通 1920→1200（75vw=1440 超封顶）、2560→1200（封顶生效）、1366→695（正文区物理宽 ≈742 < 75vw=1024，max-width 自然回退——CSS 注释预写行为）、390→327（窄屏满宽不压）；
  - 双语 side 1920 中文 680/英文 720（37.5vw 同基准两栏等宽；中文侧含 20px 内边距差 40px 属容器 padding 语义）；仅英文→1200；stack→1200；交错→1200；mu-lu-s 非词条页→1200；
  - 产物 CSS style.tbkfWn4U.css 落地；check_all 复跑 17 项全绿。
- 踩坑记录（本轮 preview 生命周期三连）：①sirv 启动时扫文件清单为快照——构建后新 hash 文件 404、同名 HTML 给新内容，造成“CSS 加载了但规则全旧”的错局（须构建进程退出后再起 preview，盯日志行判完成不可靠）；②shell `(... &)` 双重后台化吞 cwd（cssf 取值为空死循环）；③前台命令超时转后台会连坐清理 preview 子进程。终局：单 mjs 脚本内 spawn preview→量测→kill（verify-width-full.mjs）。
- 回归面：双语对照 body 类体系、语言切换器 no-langswitch-page、sep 版式令牌全部未动；aside（outline）固定 16rem 不受挤压；check_all 17 项全绿。
