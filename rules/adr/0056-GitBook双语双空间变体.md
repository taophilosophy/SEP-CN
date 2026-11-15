# 0056. GitBook 双语发布：双空间变体与空间内容配置

accepted | 2026-11-15（2026-11-16 补英文空间 TOC 与导入面核实）

## 背景

用户 2026-11-15 指令：按 GitBook 最新文档实现多语言，英语在 `yuanwen/` 目录。查证结论（gitbook.com/docs，2026-11 现值）：

* **Agent 自动翻译（Translations）**：组织首页建翻译，生成"翻译副本 section"，源变动只重译变动页；译文**不可手工编辑**，须先固定 slug；按词计费（$25/月含 5 万词，超出 $0.20/千词），改词表触发全量重译。**不采用**：本项目中文是人译产物、受零信任与体例门禁约束，不可编辑的机器译文直接违约。
* **内容变体（Content variants）+ Git Sync**：每语言一个 space，Site structure → Add variant → 设 `lang`，站点头部自动出语言切换器；Git Sync 的 Content mapping 可把**同一仓库的不同目录分别映射到不同 space**（`./` 相对 project directory）。**采用**。
* **`.gitbook.yaml` 按 space 一份**，路径相对该 space 的映射目录，键为 `root` / `structure.readme` / `structure.summary` / `redirects`；`structure.summary` 可改名，故不同 space 可用不同 TOC 文件。站点级映射由 `gitbook-docs.yaml` 承担，`gitbook-docs.yaml` 先于 `.gitbook.yaml` 生效。
* **导入面**：GitBook 文档明确"Markdown files not listed there won't appear as pages"——存在 `SUMMARY.md` 时，未列入的 md 不成页面；无 SUMMARY 时才按目录推断导航。故根空间映射 `./` 不会把 `tools/`、`specs/`、`tasks/` 等 7000+ 文件做成页面。文档未提供忽略清单，反向处理只能靠 SUMMARY 白名单。
* 旧版 gitbook-cli 的 `LANGS.md` 机制已随工具链归档，现行文档中不存在，不采用。

仓库侧现状与约束：

* 本仓没有 `.gitbook.yaml`，此前未接 GitBook 托管；对外阅读站是本地 VitePress（ADR-0055、specs/037）。
* `yuanwen/<letter>/<slug>.md` 与中文侧路径平行，但 `yuanwen/SUMMARY.md` 是**中文标题镜像**（条目 `../` 指回仓库根），并被 VitePress 用于中英配对（`.vitepress/config.mts`，标题相等才配对）——**不能改成英文标题**，否则触发配对漂移保护。
* 用户当轮约束：**不动公式、不改正文**。
* 并行会话当日落 [ADR-0057](0057-SUMMARY占位母行去链接.md)：GitBook 报 `The summary contains multiple entries referencing "README.md"`，182 行集群占位母行改为无链接分组行；该 ADR §6 对英文空间 TOC 定了接口——分组行须按无链接形态输出、去 `\*` 标记，不得改回指向文件的链接。

## 决策

1. **发布路线采用 GitBook 双 space 变体**：中文 space 映射仓库根，英文 space 映射 `yuanwen/`，两者在 Site structure 加成 variant 并分别设语言，语言切换器由 GitBook 头部提供。站点呈现仍以本地 VitePress 为准，GitBook 侧只承担多语言托管。
2. **根 `.gitbook.yaml`** 声明中文空间：`root: ./`、`structure.readme: README.md`、`structure.summary: SUMMARY.md`（中文侧目录单一事实源不变）。
3. **`yuanwen/.gitbook.yaml`** 声明英文空间：`structure.readme: README.md`、`structure.summary: SUMMARY-en.md`。英文空间用独立 TOC，**不碰中文镜像** `yuanwen/SUMMARY.md`。
4. **英文 TOC 由 `tools/gen_en_summary.py` 确定性生成** `yuanwen/SUMMARY-en.md`：
   * 只保留目标文件在 `yuanwen/` 内存在的条目（中文侧导航行如 `qian-yan/*` 自然剔除）；
   * 标题取“最后一个汉字之后的英文部分”，剥掉夹在中间的汉字/全角标点（书名号、括号、破折号），保留别名行首的 `*` / `\*` 标记；英文部分内的顿号 `、`（SEP 作者并列）统一为半角逗号；
   * 路径改为相对 `yuanwen/` 根（去掉 `../`），保留 `## A` 字母分节与子条目缩进；
   * 母词条占位行按 [ADR-0057](0057-SUMMARY占位母行去链接.md) §6 输出为**无链接分组行**（去 `\*` 标记、留英文标签与缩进）；中文侧两形态（`* [\*美学 aesthetics](README.md)` 与 `* \*美学 aesthetics`）产出同一结果，且绝不指向文件——GitBook 一文件一页，重复引用 `README.md` 会被拒收；
   * 生成即校验：目标存在、零汉字残留、零全角标点残留、分组行不含链接语法、条数与序号与中文侧对齐；`--check` 只校验不写回，`--no-groups` 为 ADR-0057 回退形态；
   * 结果：**2513 词条 ＋ 180 分组行 ＝ 2693 行**，与中文侧内容行 `(类型, 缩进[, 路径])` 序列逐位一致（中文侧 2706 内容行减 13 条中文专有导航行）。
5. **`.gitbook.yaml` 与生成物入治理面**：`tools/check_junk.py` 的 `ROOT_ALLOW` 登记 `.gitbook.yaml`（ADR-0023“新增根级条目须走 ADR”）；`rules/01-repository-structure.md` 目录职责表登记 `.gitbook.yaml`；`yuanwen/SUMMARY-en.md` 不入 VitePress 构建（`srcExclude`）。
6. **新增 `yuanwen/README.md` 作英文空间首页**（英文撰写）。理由：GitBook 默认 `structure.readme: README.md`，缺失时首次同步会**自动创建并写回**该文件；先手工落一个受控英文首页，避免同步端改写仓库。
7. **不动公式、不改正文**：本轮只涉及配置、目录生成与英文首页；词条正文（含 TeX）零改动。

## 后果

* **正面**：中文侧结构仍以 `SUMMARY.md` 为唯一事实源，英文 TOC 是确定性派生，改中文目录后跑一次生成器即同步；`yuanwen/SUMMARY.md` 镜像与 VitePress 中英配对不受影响；仓库侧多语言配置收敛为两份六行 YAML 加一个生成器。
* **代价**：英文标题从中文标题里切分出来，切分规则靠单测锁住（`tools/tests/test_gen_en_summary.py` 11 例：常规条目、别名保留 `\*`、书名号/括号剥离、英文在前、顿号归一、纯中文返回空、两形态同输出、无链接分组行、`--no-groups` 回退）；生成器须与 `SUMMARY.md` 改动同批运行。
* **已知边界**：英文空间侧栏顺序沿用中文侧顺序，非 SEP 上游字母序；中文专有导航页（版权、术语表、人名表等）不出现在英文空间；分组行标签是英文母词条名，无独立页面。
* **待实测（GitBook 侧）**：①文档口径为“未列入 SUMMARY 的 md 不成页面”，首次同步后核对根空间页面数是否恰为 2526；②ADR-0057 的无链接分组行在英文空间是否渲染为标签（若被拒收，改用 `--no-groups` 重生成，英文空间退为纯词条目录）。
* **免费版能力**：Git Sync 与 site variants 含在免费版；自定义域名需 Essential 起。Agent 自动翻译属付费且不可编辑，明确不用。
* **版权边界**：英文空间发布的是上游 HTML 快照文本，SEP 条目版权属 SEP 与各作者；对外发布前需按站点政策确认可公开范围。

## 落点

* 新增 `.gitbook.yaml`（中文空间）、`yuanwen/.gitbook.yaml`（英文空间）、`yuanwen/README.md`（英文首页）、`yuanwen/SUMMARY-en.md`（生成物）。
* 新增 `tools/gen_en_summary.py`（生成器，`--check` 可入校验、`--no-groups` 回退）；`tools/tests/test_gen_en_summary.py`（11 例单测）；`tools/README.md` 登记。
* `tools/check_junk.py`：`ROOT_ALLOW` 增 `.gitbook.yaml`。
* `rules/01-repository-structure.md`：目录职责表增 `.gitbook.yaml` 行（该行首次随 ADR-0057 提交时误标 0057，已更正为 0056）。
* `.vitepress/config.mts`：`srcExclude` 增 `yuanwen/SUMMARY-en.md`；`.vitepress/README.md` 同步一句。
* `rules/adr/README.md`：ADR 索引增 0056。
* 验收：`python tools/check_all.py` 全绿；GitBook 侧建 space、映射目录、加 variant 三步属人工操作，不入仓库。
