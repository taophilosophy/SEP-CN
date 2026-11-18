# SEP 版式 VitePress 主题（specs/037）

**版本** v1.0 ｜ **状态** 已落地 ｜ **日期** 2026-11-15 ｜ **权威** 2026-11-15 用户指令“根据 SEP 官网页面做一套 VitePress 主题，包含本项目所需一切功能”

## 1. 目的与非目标

把阅读站从“默认主题＋缝补”升级为以 SEP 官网 2013 版模板为视觉基准的自研主题（`.vitepress/theme/`），现有功能零回退。

**非目标**：不动内容管线（词条 md、yuanwen、SUMMARY、登记册、baseline）；不改 config.mts 数据层逻辑（SUMMARY 解析、中英配对、搜索索引、git-stamps、死链守卫）；不换字体（正文霞鹜文楷维持）；不复刻 Bootstrap 2 私有产物（IE 条件注释层等历史包袱不入库）。

## 2. 裁定（Assumptions，2026-11-15 用户三问三答＋工程裁定）

1. **骨架**：词条页在仿 SEP 基础上保留左右 ToC——左侧站点侧栏与右侧页内 outline 都保留（不拆 VitePress 双轨导航）；SEP 风格落在页头品牌区、题区、pubinfo、页脚菜单块、配色。
2. **字体**：保留霞鹜文楷正文（离线字体资产不动），SEP 风格不通过换字体表达。
3. **深浅色**：保留双主题——浅色=SEP 原版式配色，深色=同布局暗色适配。
4. **架构**（工程裁定）：继续 `extends DefaultTheme` 槽位扩展＋CSS 设计令牌换皮，不自写 Layout——搜索弹窗、移动端菜单、深色切换、侧栏折叠等交互零回退，改动面收敛在 custom.css＋槽位组件。
5. **独立性**（2026-11-15 用户二次指令“主题与原有 vitepress 独立，尽量避免直接改 vitepress 非配置文件”）：VitePress 本体（node_modules/默认主题）零改动；引用 VitePress 内部类名的规则全部收敛在 `.vitepress/theme/vp-compat.css` 唯一桥接层（内部类名清单见该文件头注），升级 VitePress 只需复查该文件；主题本体（sep-theme.css、custom.css 组件段、主题组件 .vue）只用自有类名＋`--vp-*` 公开设计令牌。

## 3. 视觉基准（SEP 2013 模板取证）

- 页头：红 SEP 标志＋站名＋导航栏（搜索框）；本站对应 VitePress 顶栏换肤。
- 题区：entry 标题下作者行（逗号分列；`baseline/entries.json` 的 `authors` 字段已有）、`#article-banner` 信息横幅、`#pubinfo` 斜体行（First published …; substantive revision …）。
- 页脚：菜单块分栏（About/Community/Tools/Support 式）＋镜像选择器＋版权行；本站 VersionPin 信息迁入 SEP 式页脚块，信息不减。
- 设计令牌从 SEP `css/style.css`、`entry.css` 抓取取证（凭证存 specs/037/results/；无最小请求间隔，ADR-0069）。

## 4. 功能零回退清单（基线=2026-11-15 现状）

双语对照（side/stack、点击跳段、滚动同步、句选高亮、持久化）／littlefoot 脚注气泡／参考文献就地全量渲染／MathJax 4.1.3（含词条宏、sentinel）／版本钉（改 SEP 式页脚呈现，信息不减）／pagefind 构建搜索＋中文优化＋命中高亮／dev MiniSearch 分节限流／SUMMARY 分字母侧栏＋非词条页 slim／中英配对漂移保护／git-stamps lastUpdated／死链守卫（不新增豁免）／深浅色切换／移动端可用／cleanUrls、sitemap、编辑此页。

## 5. 验收判据

1. 浅色下首页、词条页、原文页三形态与 SEP 对应部位截图对照（页头、题区、pubinfo、页脚），凭证存 specs/037/results/。
2. 深色下词条页＋首页抽查无破相。
3. 第 4 节清单逐项人工走查通过，execution-log 记凭证。
4. `bun run build` 冒烟成功；`python tools/check_all.py` 全绿。
5. 词条页侧栏内联机制不回退：词条页构建产物体积不高于现基线＋10%。

## 6. 执行记录

见 [execution-log.md](execution-log.md)。
