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
