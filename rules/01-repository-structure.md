# 仓库结构与命名规范

本规则展开宪法第 III 条（单一事实源）与第 VI 条（体例即契约）中与仓库结构有关的部分。

结构改动属不可逆决策：动手前先写清目标结构、影响范围与验收（`check_summary.py`、`check_mulu_s.py`、`rebuild_dir.py check` 全绿），再选手段（脚本、命令）；不以“跑过某工具”代替判断（[08](08-intent-first.md)）。

## 目录职责

| 路径 | 职责 | 是否入库 |
| ---- | ---- | -------- |
| `zh/` | 中文内容根：词条正文、`zh/SUMMARY.md`、`zh/mu-lu-s.md`、两本登记册、`zh/PROGRESS.md`、`zh/RELEASE-NOTES.md` 与中文目录 | 是 |
| `html/` | 英文原始抓取 HTML（原始网页钉；ADR-0027 起入库，ADR-0062 绝对冻结）：`html/<slug>/index.html`，图片随包存 `html/<slug>/` | 是 |
| `zh/qian-yan/`、`zh/guan-yu/` | 项目说明页（版权、日志、编辑信息等） | 是 |
| `zh/SUMMARY.md` | **目录结构唯一数据源**，GitBook 侧边栏由它生成 | 是 |
| `.gitbook.yaml` | GitBook 空间内容配置（ADR-0056）：根层一份对应中文空间（`summary: zh/SUMMARY.md`）；`en/.gitbook.yaml` 对应英文空间，其 `structure.summary` 指向生成物 `en/SUMMARY-en.md`（`tools/gen_en_summary.py` 派生，不手改） | 是 |
| `zh/mu-lu-s.md` | 手工维护的 **分类目录** （独立于 SUMMARY 的学科分类视图） | 是 |
| `zh/shu-yu-biao.md` | 术语对照 **登记册** （术语决策的单一事实源；ADR-0036 改名，原 `yi-zhe-shuo-ming.md`） | 是 |
| `zh/ren-ming-biao.md` | 人名对照 **登记册** （ADR-0012 自术语表拆出） | 是 |
| `tasks/` | 文档任务状态记录（JSON，按 SEP slug 组织） | 是 |
| `journal/` | 条目事件日志（NDJSON，按 `journal/<letter>/<slug>.ndjson` 组织；三存储之一的事实源，`state` 为其派生视图，ADR-0068） | 是 |
| `baseline/` | 词条版本元数据清单（slug、版本日期、存档版名、SHA-256、抓取时间） | 是 |
| `specs/`、`.specify/` | 工程规格与项目宪法（spec-kit 体系） | 是 |
| `tools/` | 管线与治理脚本（Python，仅标准库） | 是 |
| `.github/` | CI 工作流与 lint 配置 | 是 |
| `.vitepress/` | 本地双语阅读站：配置、主题、构建期准备脚本；构建细节见其 `README.md`（实现说明，非规则） | 是 |
| `zh/fang-fa-lun/` | **已退役**（2026-11-15 归一化折叠：活条款入 rules/03/06/07，历史版本存 `rules/reference/`；仅存退役存根 README，ADR 历史链接保留） | 是 |
| `zh/jian-yi-shu/` | 分类目录核查建议书等一次性交付物（不入 SUMMARY） | 是 |
| `en/` | 英文原文**转换镜像**：`en/<letter>/<slug>.md`，与 `html/` 文字一致（ADR-0009/0062）；图片存 `en/assets/<slug>/` | 是 |
| `script/`、`state/` | 本地草稿脚本、管线本地运行态 | 否（gitignore） |
| `.git` | 版本库本体；不可变语义由版本历史承担 | 是 |
| `.autocorrectrc` | 拼写与格式自动修复配置（CI 修复侧） | 是 |
| `.gitattributes` | 换行与二进制属性（UTF-8/LF 契约的机读面） | 是 |
| `.gitignore` | 忽略规则；只管不入库，不管可堆放 | 是 |
| `.markdownlint-cli2.jsonc` | markdownlint 唯一配置（ADR-0061） | 是 |
| `.secrets`、`.workbuddy`、`.workbuddy-ai`、`.zcode` | 本地凭证、会话记忆与代理配置（ADR-0035 登记例外） | 否 |
| `AGENTS.md` | AI 代理入口指针；不复制数字、不新增义务（S6） | 是 |
| `CODE_OF_CONDUCT.md`、`CONTRIBUTING.md` | 行为准则与贡献指南 | 是 |
| `LICENSE` | 许可（BSD-2-Clause；SEP 文本另受 CC BY-NC-SA 约束） | 是 |
| `README.md` | 访客说明；不承载规则 | 是 |
| `zh/RELEASE-NOTES.md` | 发布说明；按版本追加 | 是 |
| `zh/PROGRESS.md` | 进度汇总（受控生成物，`tools/progress.py` 输出，不手改） | 是 |
| `assets/` | 词条图片；每件至少被引用一次，禁外链 | 是 |
| `public/` | 站点静态资产 | 是 |
| `rules/` | 全局规则与 ADR（宪法为上位；ADR 只追加） | 是 |
| `package.json`、`bun.lock` | 历史豁免：依赖与构建入口已迁构建壳（ADR-0055） | 否 |
| `node_modules/` | 本地依赖（可为指向构建壳的联接） | 否 |

> 上表与 `rules/layout.json` 同源：路径集合由 `tools/check_layout.py` 的 L2 谓词双向核对（缺一或多一即红，ADR-0067）。新增根级条目须先登记 layout.json 并走 ADR。

## 根目录白名单（ADR-0023）

根目录是**可枚举的契约面**：只允许登记在 `tools/check_junk.py` 的 `ROOT_ALLOW` 中的条目，四类——工具链配置（`.github/`、`.vitepress/`、`.specify/`、`.zcode/` 与点文件）、顶层叙事文档（`README.md` 等访客文档）、结构目录（`zh/`、`html/`、`en/`、`rules/`、`specs/`、`tools/`、`tasks/`、`baseline/`、`assets/` 等）与构建壳历史豁免。

* **新增根级条目须走 ADR**（`rules/adr/`），同时在 `ROOT_ALLOW` 登记说明；不登记即门禁红灯。
* **散件归置唯一路径**：本地会话草稿 → `script/`；运行态与临时文件（含 `*.tmp`）→ `state/`；批次工件与入库凭证 → `specs/<NNN>-*/bin|results/`。根目录不放中间产物、一次性脚本、抓取快照、提示词工作台。
* **门禁双向核对**（`python tools/check_junk.py`）：跟踪清单 ∩ 白名单 + 工作区 `os.listdir` ∩ 白名单。根级散件无论被 `git add -A` 扫入还是被忽略规则遮住，一律红灯；CI 侧只见跟踪清单，本地收工 `check_all` 同时覆盖未入库散件。
* 判定口径：根目录出现“不在白名单的任何文件或目录”即违规——包括被 `.gitignore` 忽略的 `_xxx/` 脚手架。忽略规则只管“不入库”，不管“可以堆在根目录”。客户端运行态 `.workbuddy/`、`.workbuddy-ai/` 为登记在案的例外（ADR-0035），前提是二者持续被 `.gitignore` 覆盖；同类目录须逐项走 ADR，不得援引本条自动放行。

## zh/SUMMARY.md 规则

* 第一行 `# Table of contents` 绝对不能变更，否则 GitBook 同步失效。
* 条目格式 `* [标题](路径)`，嵌套子条目缩进两格。
* **无链接行**两类，**都不指向任何文件**：①**分组行**（集群占位母行）写作 `* \*分类名`，必须带子条目（空分组行是硬错误，`check_summary.py` 实拦）；②**别名行**（标题含“——见 / — see”的 SEP 索引名）写作 `* \*X——见Y`，可无子条目。GitBook 要求一文件一页：分组行指向 `README.md`、别名行指向目标词条，都会让导入报 `multiple entries referencing`（ADR-0057、ADR-0060）。行首裸 `*` 须转义为 `\*`。
* **改标题只改 `zh/SUMMARY.md` 一处**；各文件 H1 必须与条目文字一致，本地门禁与 CI 用同一检查器 `tools/check_summary.py` 实拦；改后跑 `python tools/check_summary.py --sync-headers` 同步 H1（ADR-0024：CI 只校验，不再写回远端）。
* 同步/校验时会把标题中的转义还原：`\*`→`*`、`\[`→`[`、`\]`→`]`。SUMMARY 源码内的这些转义是 markdown 链接语法所需，**保留不删**。
* 首行是 `---`（YAML frontmatter）的文件（如 `zh/mu-lu-s.md`）不参与 H1 同步与校验。
* 别名词条行（含 `— see`）左侧英文必须写目标词条的**完整标题**（`baseline/entries.json` 的 `title`），不得留截断片段（`in biology`、`and informed consent`）或索引倒装残段（`clinical research, ethics of`）；右侧 `— see` 之后仍写 SEP 索引名。门禁 `python tools/check_summary.py` 的 `alias fragment` 项实拦（2026-11-07 裁定，ADR-0024）。

## zh/mu-lu-s.md（分类目录）规则

* 分类目录是 **手工维护的独立视图**，不由 SUMMARY 自动生成（旧的 `mulu.yml` 生成 `mu-lu.md` 的机制已删除）。
* 条目链接文本与 SUMMARY 条目文字保持一致（转义写法可以不同，还原后必须相同）。
* 链接文本内的内层方括号 **必须转义** （`[Abailard]` 写作 `\[Abailard\]`），否则 markdown 在第一个 `]` 处断链。
* 别名词条（标题含 `— see`）与 `*` 前缀占位母词条 **预期不收录**；递归自指的假条目（如“递归——见递归”）同样不收录。
* 改动后运行 `python tools/check_mulu_s.py` 检测与 SUMMARY 的对应性：坏链必须为 0，路径必须在 SUMMARY 中，共有路径标题必须一致。检测结果只报告，人工裁决后修改。

## 条目标题体例（ADR-0078，2026-11-25）

SUMMARY 与 mu-lu-s 的条目行、别名行、分组行与 mu-lu-s 标题层的文字与符号判据（结构规则见上两节；本节施于中文段，en 侧承 ADR-0062 不规范化）：

* **条目行（应）**：`中文题`＋半角空格＋`英文原题`＋半角括号作者栏；作者栏并列姓名之间用顿号，禁逗号／分号／`&`／and（GB/T 15834-2011 §4.5、CY/T 154-2017）。作者姓名缩写点从作者惯用式（宜，见 `zh/ren-ming-biao.md`），禁机械归一。
* **译注括注（宜）**：中文题内增补性括注用全角（），英文原题内括号与作者栏用半角，双轨不得互串。
* **别名行（应）**：`中文索引词——见中文目标题 英文段 — see 索引名`。“——见”为两字位破折号＋“见”（GB/T 15834 §4.10；GB/T 22466-2023 直接参照；ISO 999:1996 无盲引）；“：见”、缺中文连接、“——见”前空格均违例；“——见”后接西文或数字保留半角空格。
* **分组行（宜）**：`中文名`＋半角空格＋`英文索引名`；en 侧照录上游原样。
* **符号层（应）**：人名间隔号一律 U+00B7（禁 U+2027）；数字区间连接号遵本文件连接号节（rules/02、ADR-0041），标题层同受管辖；`&ndash;` 等 HTML 实体不得出现在目录文本中。
* **标题内并列连词（可，不设机检）**：en “and”／“vs.” 的中文连接词“与／和”自由择用，以语体自然为准，不强制归一、不建白名单（2026-11-25 用户裁定）。
* **机检**：`python -I specs/059-toc-title-normalize/bin/recheck.py`（P1–P8 谓词全 0 命中为 PASS；写回器与复算器分离）。

## 文件命名

* **目录命名域分区**（ADR-0067）：词条目录 `zh/<letter>/` 用 SEP slug；结构目录用英文固定词（`rules`、`specs`、`tools`、`tasks`、`baseline` 等）；`zh/qian-yan/`、`zh/guan-yu/`、`zh/jian-yi-shu/`、`zh/fang-fa-lun/` 为**已冻结的拼音命名域**——只减不增，新增目录一律英文 slug。布局登记以 `rules/layout.json` 为准，`frozen` 条目的增删须走 ADR。
* 词条文件名一律用 SEP slug（英文，`[a-z0-9.-]`，不得含空格、中文或英文冒号，必须兼容 Windows 文件名要求；集群前缀名如 `plato-cratylus` 原样保留）。2026-10-27 起**废除拼音 slug 命名**（ADR-0005），历史拼音命名文件已随上游同构重建（ADR-0007）删除或入史。
* 词条为**单文件形态**（ADR-0008/0009）：`zh/<letter>/<slug>.md` 承接正文（letter=slug 首字符，字母目录按 A–Z 排序），补充材料 `<slug>.<x>.md` 点号命名同目录平铺。
* 双库镜像（ADR-0009）：每个词条在中文侧 `zh/<letter>/<slug>.md` 与英文侧 `en/<letter>/<slug>.md` 一一对应，相对路径逐字符一致；`html/<slug>/` 存原始 HTML。
* 引用路径（图片、链接）必须与磁盘真实文件名 **逐字符大小写一致**——Windows 本地不敏感而 Linux CI 敏感，大小写错位会在 CI 构建时 404。

## 词条页内标题层级

* 词条页 H1 为 SUMMARY 条目文字；页内分节自 `##` 起，逐级递增，不得跳级（markdownlint MD001）。
* 词条页 H1 与 SUMMARY 不一致时以 SUMMARY 为准：门禁实拦，`--sync-headers` 同步；CI 只校验不写回（ADR-0024）。

## 图片

* 图片本地化：镜像侧存 `en/assets/<slug>/`（上游同名 `imageN.jpg`，ADR-0008），`en/<letter>/<slug>.md` 内写作 `../assets/<slug>/<文件名>`（相对解析到 `en/assets/`，ADR-0010）；中文词条 `zh/<letter>/<slug>.md` 用同一写法，解析到**根级 `assets/<slug>/`**，即词条图片就地入库（ADR-0023 澄清，2026-11-07 按词条补齐）。抓取原始 HTML 一律存 `html/<slug>/`（原始网页钉，ADR-0027 起入库；**html/ 绝对冻结**——文字缺陷入全局勘误表＋中文译注、格式问题入 `baseline/en-patches/` 补丁池，ADR-0062；分歧账只承载上游真变与审计面，ADR-0045）。
* 三条硬性要求：每个图片文件至少被一处引用（不得悬空）；引用必须能解析（不得指向缺失文件或外链）；必须本地化存放，禁止外部 URL。
* 门禁：`python tools/check_images.py`（悬空、大小写不符、外部地址、`assets/` 未引用资产；本地报告写 `state/image-report.md`）；CI 侧为 `checks.yml` 的 `images` 矩阵作业（`--gate` 硬拦，报告入运行工件——2026-11-16 起不再单独开 issue，ADR-0061）。
* “reprinted with permission” 图片必须在图注标明来源。

## 单体文件治理（ADR-0004）

* 叙事/规则/规格/指南类 markdown 单文件超过 **1000 行或 100KB** 任一，必须按文件夹拆分：`X.md` → `X/index.md` + 按节/附录归类的拼音命名子文件（注：拼音命名仅适用于叙事文档子文件，与词条 SEP slug 命名分属两个约定，见上文废除条款；拼音文件名属**标识符约定**，不受 GB/T 16159-2012 词式书写约束——词式书写仅约束拼音文本，豁免登记 ADR-0041）；`git mv` 保留历史；SUMMARY 收录状态不变。
* 豁免：登记册（`zh/SUMMARY.md`、`zh/mu-lu-s.md`、`zh/shu-yu-biao.md`（ADR-0036 改名）、`zh/ren-ming-biao.md`（ADR-0012））、生成物（`zh/PROGRESS.md`）；发布词汇表已并网删除（ADR-0036）；豁免文件超限须走 spec 改解析器后另行裁定。
* 门禁 `python tools/check_doc_size.py`（本地与 `checks.yml`）；SEP 词条本体不在管辖内。
* **规则文本专用阈值（2026-10-27）**：约束性规则 `rules/0X.md` 超过 **300 行或 30KB** 任一，必须按主题拆分为目录 `rules/0X/`，每文件一主题、分别存放具体规则，规则地图（`rules/README.md`）同步；`check_doc_size` 机检（当前最大 rules/03 174 行，全部达标）。
