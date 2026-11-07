# 仓库结构与命名规范

本规则展开宪法第 III 条（单一事实源）与第 VI 条（体例即契约）中与仓库结构有关的部分。

结构改动属不可逆决策：动手前先写清目标结构、影响范围与验收（`check_summary.py`、`check_mulu_s.py`、`rebuild_dir.py check` 全绿），再选手段（脚本、命令）；不以“跑过某工具”代替判断（[08](08-intent-first.md)）。

## 目录职责

| 路径 | 职责 | 是否入库 |
| ---- | ---- | -------- |
| `<letter>/`（a…z 及个别非字母目录如 `1/`） | 中文词条正文：`<letter>/<slug>.md` + 补充材料 `<slug>.<x>.md`（ADR-0009 A–Z 字母目录 + SEP slug 单文件）；未翻译条目为仅含 H1 的骨架 | 是 |
| `yuanwen/` | 英文原文**本地库**：`yuanwen/<letter>/<slug>.md` 与中文侧逐字符镜像（ADR-0009）；图片存 `yuanwen/assets/<slug>/` | 否（gitignore，已跟踪演示条目除外） |
| `qian-yan/`、`guan-yu/` | 项目说明页（版权、日志、词汇表、编辑信息等） | 是 |
| `SUMMARY.md` | **目录结构唯一数据源**，GitBook 侧边栏由它生成 | 是 |
| `mu-lu-s.md` | 手工维护的 **分类目录** （独立于 SUMMARY 的学科分类视图） | 是 |
| `yi-zhe-shuo-ming.md` | 术语与人名对照 **登记册** （术语决策的单一事实源） | 是 |
| `qian-yan/ci-hui-biao.md` | 面向读者的 **发布词汇表** （发布视图，非决策源） | 是 |
| `tasks/` | 文档任务状态记录（JSON，按 SEP slug 组织） | 是 |
| `baseline/` | 词条版本元数据清单（slug、版本日期、存档版名、SHA-256、抓取时间） | 是 |
| `specs/`、`.specify/` | 工程规格与项目宪法（spec-kit 体系） | 是 |
| `tools/` | 管线与治理脚本（Python，仅标准库） | 是 |
| `.github/` | CI 工作流与 lint 配置 | 是 |
| `.vitepress/` | 本地双语阅读站：配置、主题、构建期准备脚本；构建细节见其 `README.md`（实现说明，非规则） | 是 |
| `fang-fa-lun/` | 翻译工程方法论与标准散页（**待逐步折叠进 rules/**，折叠前以规则地图登记为准） | 是 |
| `jian-yi-shu/` | 分类目录核查建议书等一次性交付物（不入 SUMMARY） | 是 |
| `en/`、`script/`、`state/` | 英文原始抓取 HTML、本地草稿脚本、管线本地运行态 | 否（gitignore） |

## 根目录白名单（ADR-0023）

根目录是**可枚举的契约面**：只允许登记在 `tools/check_junk.py` 的 `ROOT_ALLOW` 中的条目，五类——工具链配置（`.github/`、`.vitepress/`、`.specify/`、`.zcode/` 与点文件）、顶层叙事文档（`SUMMARY.md`、`PROGRESS.md`、登记册、访客文档）、A–Z 词条字母目录与数字目录 `1/`（ADR-0009）、结构目录（`rules/`、`specs/`、`tools/`、`tasks/`、`baseline/`、`assets/` 等）、包管理文件（`package.json`、`bun.lock`）。

* **新增根级条目须走 ADR**（`rules/adr/`），同时在 `ROOT_ALLOW` 登记说明；不登记即门禁红灯。
* **散件归置唯一路径**：本地会话草稿 → `script/`；运行态与临时文件（含 `*.tmp`）→ `state/`；批次工件与入库凭证 → `specs/<NNN>-*/bin|results/`。根目录不放中间产物、一次性脚本、抓取快照、提示词工作台。
* **门禁双向核对**（`python tools/check_junk.py`）：跟踪清单 ∩ 白名单 + 工作区 `os.listdir` ∩ 白名单。根级散件无论被 `git add -A` 扫入还是被忽略规则遮住，一律红灯；CI 侧只见跟踪清单，本地收工 `check_all` 同时覆盖未入库散件。
* 判定口径：根目录出现「不在白名单的任何文件或目录」即违规——包括被 `.gitignore` 忽略的 `_xxx/` 脚手架。忽略规则只管「不入库」，不管「可以堆在根目录」。

## SUMMARY.md 规则

* 第一行 `# Table of contents` 绝对不能变更，否则 GitBook 同步失效。
* 条目格式 `* [标题](路径)`，嵌套子条目缩进两格。
* **改标题只改 SUMMARY.md 一处**；各文件 H1 必须与条目文字一致，本地门禁与 CI 用同一检查器 `tools/check_summary.py` 实拦；改后跑 `python tools/check_summary.py --sync-headers` 同步 H1（ADR-0024：CI 只校验，不再写回远端）。
* 同步/校验时会把标题中的转义还原：`\*`→`*`、`\[`→`[`、`\]`→`]`。SUMMARY 源码内的这些转义是 markdown 链接语法所需，**保留不删**。
* 首行是 `---`（YAML frontmatter）的文件（如 `mu-lu-s.md`）不参与 H1 同步与校验。

## mu-lu-s.md（分类目录）规则

* 分类目录是 **手工维护的独立视图**，不由 SUMMARY 自动生成（旧的 `mulu.yml` 生成 `mu-lu.md` 的机制已删除）。
* 条目链接文本与 SUMMARY 条目文字保持一致（转义写法可以不同，还原后必须相同）。
* 链接文本内的内层方括号 **必须转义** （`[Abailard]` 写作 `\[Abailard\]`），否则 markdown 在第一个 `]` 处断链。
* 别名词条（标题含 `— see`）与 `*` 前缀占位母词条 **预期不收录**；递归自指的假条目（如“递归——见递归”）同样不收录。
* 改动后运行 `python tools/check_mulu_s.py` 检测与 SUMMARY 的对应性：坏链必须为 0，路径必须在 SUMMARY 中，共有路径标题必须一致。检测结果只报告，人工裁决后修改。

## 文件命名

* 词条文件名一律用 SEP slug（英文，`[a-z0-9.-]`，不得含空格、中文或英文冒号，必须兼容 Windows 文件名要求；集群前缀名如 `plato-cratylus` 原样保留）。2026-10-27 起**废除拼音 slug 命名**（ADR-0005），历史拼音命名文件已随上游同构重建（ADR-0007）删除或入史。
* 词条为**单文件形态**（ADR-0008/0009）：`<letter>/<slug>.md` 承接正文（letter=slug 首字符，字母目录按 A–Z 排序），补充材料 `<slug>.<x>.md` 点号命名同目录平铺。
* 双库镜像（ADR-0009）：每个词条在中文侧 `<letter>/<slug>.md` 与英文侧 `yuanwen/<letter>/<slug>.md` 一一对应，相对路径逐字符一致。
* 引用路径（图片、链接）必须与磁盘真实文件名 **逐字符大小写一致**——Windows 本地不敏感而 Linux CI 敏感，大小写错位会在 CI 构建时 404。

## 词条页内标题层级

* 词条页 H1 为 SUMMARY 条目文字；页内分节自 `##` 起，逐级递增，不得跳级（markdownlint MD001）。
* 词条页 H1 与 SUMMARY 不一致时以 SUMMARY 为准：门禁实拦，`--sync-headers` 同步；CI 只校验不写回（ADR-0024）。

## 图片

* 词条图片本地化于 `yuanwen/assets/<slug>/`（上游同名 `imageN.jpg`，ADR-0008），md 内 `../assets/<slug>/<文件名>` 相对引用（词条位于 `<letter>/` 子目录，须跨一级；ADR-0010 修订根级时代的 `assets/` 写法）；抓取原始 HTML 一律存 `en/<slug>/`（不可变原始物，不入库）。
* 三条硬性要求：每个图片文件至少被一处引用（不得悬空）；引用必须能解析（不得指向缺失文件或外链）；必须本地化存放，禁止外部 URL。
* “reprinted with permission” 图片必须在图注标明来源。

## 单体文件治理（ADR-0004）

* 叙事/规则/规格/指南类 markdown 单文件超过 **1000 行或 100KB** 任一，必须按文件夹拆分：`X.md` → `X/index.md` + 按节/附录归类的拼音命名子文件（注：拼音命名仅适用于叙事文档子文件，与词条 SEP slug 命名分属两个约定，见上文废除条款）；`git mv` 保留历史；SUMMARY 收录状态不变。
* 豁免：登记册（`SUMMARY.md`、`mu-lu-s.md`、`yi-zhe-shuo-ming.md`、`ren-ming-biao.md`（ADR-0012））、生成物（`PROGRESS.md`）、发布词汇表（`qian-yan/ci-hui-biao.md`）；豁免文件超限须走 spec 改解析器后另行裁定。
* 门禁 `python tools/check_doc_size.py`（本地与 `checks.yml`）；SEP 词条本体不在管辖内。
* **规则文本专用阈值（2026-10-27）**：约束性规则 `rules/0X.md` 超过 **300 行或 30KB** 任一，必须按主题拆分为目录 `rules/0X/`，每文件一主题、分别存放具体规则，规则地图（`rules/README.md`）同步；`check_doc_size` 机检（当前最大 rules/05 74 行，全部达标）。
