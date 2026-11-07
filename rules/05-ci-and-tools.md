# CI 约定与本地工具

本规则约定 CI 工作流的行为边界与本地工具的使用方式。**本地脚本只是 CI 的预演，结果以 CI 为准** （宪法 VI）。

工具与工作流都是手段：新增或修改检查器前，先确认要拦哪类错误、以哪条门禁验收；不以工具数量、运行时长或 CI 次数衡量治理成效（[08](08-intent-first.md)）。

## CI 工作流清单（`.github/workflows/`）

| 工作流 | 行为 | 触发 |
| ---- | ---- | ---- |
| `checks.yml` | 仓库一致性门禁：`check_summary.py` + `check_mulu_s.py` + `check_junk.py`（垃圾/产物入库 + 根目录白名单，ADR-0023）+ `check_doc_size.py`（单体文件大小，ADR-0004）+ `check_terms.py`（术语一致性）+ `check_academic.py`（哲学学术规范，rules/07）+ `check_all.py --quiet`（一键全量复核汇总）+ 管线单元测试，硬错误即红灯 | push / 手动 |
| `sync-headers.yml` | 只读校验每个 SUMMARY 条目对应文件的 H1 是否与条目文字一致（转义还原后比较；跳过 frontmatter、README、别名行），不一致即红灯；**不提交、不推送**（ADR-0024：远端永不写回 main，避免造出本地没有的提交而与并行会话分叉） | push |
| `file-name-check.yml` | 校验 SUMMARY 条目文件存在，缺失自动开 issue | push |
| `markdown-lint2.yml`（手动）/ `Markdown-lint2-pr.yml`（PR 触发） | markdownlint 检查（统一配置 `.markdownlint-cli2.jsonc`；手动流可 `--fix` 开格式化 PR） | 手动 / pull_request |
| `check-images.yml` | 图片引用检查（悬空、可解析、大小写、本地化、未引用资产），逻辑在 `tools/check_images.py`（`.github/scripts/check_images.py` 为 CI 入口）；只报告，发现问题经报告开 issue，不设红灯（2026-11-07 补齐缺失脚本） | push（`.gitbook/assets/**`）/ 手动 |
| `links.yml` | 链接检查 | 定时（每月 15 日 18:00 UTC）+ 手动 + repository_dispatch |
| `md-padding.yml`、`AutoCorrect.yml` | 手动触发，自动补 CJK 空格并以 PR 提交，合并前人工核对 diff | 手动 |
| `Auto-Assign.yml`、`GC.yml` | issue/PR 自动分配、垃圾回收 | 各自约定 |
| `create-pdf.yml` | 手动导出本项目中文 PDF/EPUB（gitbook-pdf-export 工具只读使用；可按首字母分批，全量约 2600 词条）；产物仅上传运行工件，**不写 tag/Release/外部仓库**（2026-11-04 重写，D20） | workflow_dispatch |
| `render-artifact-audit.yml` | 手动构建全站后跑 `check_render_artifacts.py` 扫渲染残留（裸 `**`、字面 `[^`、链接残留、`@@M` 哨兵），有残留即红；报告入运行工件（2026-11-05 接线，ADR-0019 分期转硬的审计通道） | workflow_dispatch |

* 不要新增与上述约定冲突的本地规则；需要新检查时先改 `tools/` 并在此登记。
* CI 红灯定位：打开 `checks.yml` 的第一个失败 step，按上表同名工具在本地用相同命令复现（如 `python tools/check_summary.py`）；各工具退出码语义见其 docstring，不按文字推断。
* lint 配置统一在根目录 `.markdownlint-cli2.jsonc`（规则、纳入范围、按文件豁免），`.github/.markdownlint.json` 保留为等价规则副本；`yuanwen/`（原文照录）与 `.zcode/`（本地工具）不参与 lint。
* 修改工作流须同步更新本表（变更管理见 [06-governance.md](06-governance.md)）。

## 本地工具（`tools/`，Python 3 仅标准库）

| 工具 | 用途 |
| ---- | ---- |
| `fetch.py` / `fetch_catalog.py` / `fetch_entry.py` | SEP 抓取（正文、目录、词条包；串行默认 ≥5 秒间隔，失败显式化；并发模式间隔按 2026-10-27 用户裁定，见 specs/001 Assumptions） |
| `fetch_all.py` | 全量抓取+原文镜像驱动器（并发节拍 A=16 路×5s / B=64 路×10s，实测均无限流；`--resume` 断点续跑；逐条留痕 `script/fetch-all-log.jsonl`） |
| `extract_text.py` / `parser.py` / `yuanwen.py` | 原始 HTML → 提取文本（`en/`、`yuanwen/`，不入库）；数学保真（2026-10-27 裁定）：跨块公式保护、公式内部原样保留，仅定界符统一 `$`/`$$`、空白折叠、表格内竖线一律以 `&#124;` 保义 |
| `baseline_audit.py` | 基线清单审计（哈希、版本钉一致性） |
| `task_ops.py` | 文档任务状态机（show / create / advance / clear / block） |
| `check_style.py` | 体例检查（引号、空格、HTML/AsciiDoc 残留；输出 JSON） |
| `check_prose.py` | 语言质量预检（ADR-0020，**告警级**，不进 CI）：长句、被动、弱动词、“的”链、类名“们”、作为一个、存在着、当…的时候 八则反欧化模式；输出 JSON，默认退出码 0，`--strict` 升硬 |
| `check_render_artifacts.py` | 渲染产物残留物扫描（ADR-0019）：对构建产物 HTML 做文本级检查——裸 `**`（星内空格粗体永不渲染）、字面 `[^`（脚注配对失效）、`](`链接残留、数学哨兵 `@@M`；代码块/预排块内字面量豁免。分期转硬门禁（`raw[^` 待镜像脚注修复后纳入） |
| `check_images.py` | 图片引用检查（rules/01 图片三条硬性要求）：悬空引用、大小写不符（Windows 不敏感/CI 404）、外部地址、`assets/` 未引用资产；跳过代码块与行内代码，`yuanwen/` 缺位（CI）时跳过镜像引用；报告写 `state/image-report.md`（本地）或 `image-report.md`（CI 开 issue 用），无问题即清除旧报告，退出码 0 |
| `check_summary.py` | SUMMARY.md 结构审计（条目解析、缺失文件、孤儿文件、命名、重复）＋ H1 一致性硬门禁（SUMMARY 条目文字 ↔ 文件 H1，ADR-0024）＋ 别名行英文完整标题硬门禁（`alias fragment`，ADR-0024）；硬错误退出码 1；`--headers` 只查标题（CI 用），`--sync-headers` 按 SUMMARY 同步 H1（本地用，写回后跑残差门） |
| `check_mulu_s.py` | 分类目录 ↔ SUMMARY 对应性检测（坏链、覆盖缺口、标题不一致、重复收录）；坏链/路径错/标题不一致为硬错误，退出码 1 |
| `check_junk.py` | 垃圾/产物入库门禁（ADR-0003 + ADR-0023）：原始物、缓存、构建产物、系统杂物命中即退出码 1；根目录白名单对跟踪清单与工作区双向核对，根级散件无论是否入库一律红灯 |
| `check_terms.py` | 术语一致性门禁（specs/002）：登记册 ↔ 词汇表译法互斥冲突、登记册废弃链/重复为硬错误（退出码 1）；词汇表滞后、缺裁定日期、`--docs` 定点核销仅告警 |
| `check_math.py` | 数学保真门禁（2026-10-27 裁定）：原始 HTML 每条公式内容必须原样出现在 yuanwen 产物；占位符残留、行内 `$` 失衡为硬错误（退出码 1） |
| `check_doc_size.py` | 单体文件大小门禁（ADR-0004）：叙事/规则/规格类 md 超 1000 行或 100KB 即退出码 1；登记册与生成物豁免 |
| `check_academic.py` | 哲学学术规范门禁（rules/07、specs/003）：非存根词条的参考文献/学术工具/译注/脚注配对、任务版本钉；`--docs <路径>...` 定点、`--strict` 告警升硬；CI 无 `en/` 原始包时注号定义（`note-*`）的补充材料跨文件引用无从核对，降级 `orphan-def-unverified` 告警（本地 `check_all` 有 en/ 时照常硬拦） |
| `compare.py` | 段落级变更比较（spec 001 US-3）：抓取英文源最新快照（不覆盖 en/ 基线）与基线比较，节级 added/removed/moved + 段落级 diff，映射中文文档与节行号；无 zh_doc 标注待建任务 |
| `fetch_audit.py` | 抓取完整性主动闭环：校验每词条包内全部被引用资产在包内，缺件自动补抓（404=缺省件登记）；引用闭包迭代至不动点（一切形如文件名的裸引用皆词条资产——页面/图片/词条自有 js/css/媒体；注释剥离＋实体反解后统计，与浏览器语义一致） |
| `en_integrity.py` | 英文镜像逐词条深度复核（纯离线）：页面真实性（SEP 签名/截断/零字节）、引用闭包按上游 URL 语义解析（大小写精确、跨词条与子目录资产）、目录结构一致性（在盘文件＝被引用（含跨词条入站）∪已登记，否则游离）、数学形态盘点；全量凭证 `specs/001-sep-sync-pipeline/en-integrity-full.json` |
| `biblio_audit.py` | 参考文献结构盘点与中文文献定位（ADR-0011）：条目量/链接域统计；三探针（实体解码汉字/典籍专名/作者位拼音）标出需按 ADR-0011 还原的词条与条目，供 s1 一校与质检定位 |
| `cnki_query.py` | 术语依据查询（ADR-0012 译名依据源）：知网系权威源（CNKI 翻译助手、术语在线）在线查询与缓存 |
| `term_audit.py` / `term_harvest.py` | 术语战役工具（specs/008）：登记册审计与候选收割（008 池裁定流水线） |
| `campaign.py` | 全局统计表与批次调度（specs/005 并行设计）：a–z 批次账本（认领/阶段/断点续上），计数实时推导零漂移，多会话独立无耦合 |
| `check_all.py` | 一键全量合规复核（六项门禁 + 单元测试；`--all` 加 baseline_audit 与 en_integrity；`--quiet` 只报失败）；收工前/推审前跑一次 |
| `clean.py` | 本地垃圾清理器：默认试运行，`--go` 删除未跟踪缓存与临时文件（不触碰跟踪文件与 en/ 原始物） |
| `progress.py` | 生成 `PROGRESS.md` 进度汇总（自动生成，不手改） |
| `tests/` | 管线单元测试（unittest，金样本 fixtures） |

* 快速命令：

  ```sh
  python tools/check_style.py a/某词条.md      # 译文体例预检
  python tools/check_prose.py a/某词条.md      # 语言质量（欧化）预检（告警级，ADR-0020）
  python tools/check_all.py                    # 一键全量合规复核（收工前/推审前）
  python tools/check_summary.py                # 目录结构审计（门禁）
  python tools/check_mulu_s.py                 # 分类目录对应性（门禁）
  python tools/check_doc_size.py             # 单体文件大小（门禁）
  python tools/check_academic.py --docs a/某词条.md --strict   # 学术规范定点（s3/r3 校次）
  python tools/compare.py <slug>               # 段落级变更比较（更新任务输入，spec 001 US-3）
  python tools/baseline_audit.py [slug...]     # 基线完整性（需本地 en/ 原始物，不进 CI）
  python tools/progress.py                     # 重新生成 PROGRESS.md
  python tools/task_ops.py show <slug>         # 查任务状态
  ```

* markdownlint（配置驱动，仓库根目录执行；包管理统一 bun，不使用 npm，见 [ADR-0014](adr/0014-包管理统一bun弃用npm.md)）：

  ```sh
  bunx markdownlint-cli2            # 按 .markdownlint-cli2.jsonc 的 globs 与规则检查
  bunx markdownlint-cli2 --fix      # 自动修复可修复项
  ```

* 纳入/豁免写在 `.markdownlint-cli2.jsonc` 的 `globs` / **`ignores`** 两键——`ignoreGlobs` 与 `overrides` 是死键（官方 README 无此键；2026-11-06 README 考据＋A/B 实测复现「静默无效」，v0.24.0 验证，排除生效时 finding 以 `!` 前缀可见）；按文件豁免用行内 `<!-- markdownlint-disable -->`。
* 表格风格统一 **compact**（每个单元格两侧恰一个空格，空单元格恰一个空格；MD060 `aligned` 按显示宽度计量、CJK/emoji 记 2——官方 doc/md060.md，2026-11-06 全仓整改裁定口径；表格内竖线一律转义）。

## 站点运行（本地预演）

阅读站的构建机制是实现细节，见 [`.vitepress/README.md`](../.vitepress/README.md)（**说明而非规则**）；本节只记命令与硬约束。

* 顺序：`bun install` → `bun run dev` → `bun run build` → `bun run preview`；包管理统一 bun，不使用 npm / npx（[ADR-0014](adr/0014-包管理统一bun弃用npm.md)）。
* dev 固定 `0.0.0.0:81` 且 `strictPort`：端口被占即启动失败，不换端口、不静默降级。
* `dev` 与 `build` 先跑 `.vitepress/prepare-assets.mjs` 复制 MathJax 离线资源，缺 `node_modules` 时 exit 1；`preview` 不跑该步骤，故须先 `build`。
* 页面范围由 `.vitepress/config.mts` 的 `srcExclude` 控制：治理/管线目录（`rules/`、`specs/`、`tools/`、`tasks/`、`.qoder/` 等）一律不进站点；**新增此类目录须同步补 `srcExclude`**，否则会被构建为页面并进入全文搜索索引。

## 生成器与批量改写脚本（2026-10-30，SUMMARY 字母分节重排教训规则化）

凡对登记册/目录/正文做**程序化批量改写**（生成器、重排器、批量注入），一律遵守：

* **写回前置门**：改写结果存在任何未落位/未消费条目时**禁止写回**，dry-run 中止并列出明细（exit 非零）。残余计数以 **0** 为唯一通过标准；「行数守恒」「总量一致」只是必要条件，不构成通过证据。
* **禁止静默兜底降级**：fallback（节尾追加、缺省件补位）必须显式登记清单并计入失败面；同一输入重复运行**不得追加重复行**（幂等：同 raw 已存在即跳过）。
* **逐行身份追踪验收**：批量改写的验收=每条输入行的身份与落位坐标全量核对；只看总数（行数/字节数）不构成验收。抽查不少于 5 条且必须覆盖移动距离最大的行。
* **基线还原强制**：改写前 `git checkout -- <目标文件>` 并以 `git diff` 校验基线干净；**多会话并行下，任何 checkout 后必须重新 `git status` 确认**（并行会话可能已再次写入）。禁止在上一轮改写输出上迭代运行。
* **观察驱动调试**：失败定位先在**实际执行路径**加探针（消费点、写回点），禁止只凭对脚本逻辑的心智模型反复修补；单测复现的输入必须与批处理运行的输入逐字节一致。
* 失败实例存档：2026-10-30 SUMMARY 重排，占位行残余连续四轮被兜底掩盖（每轮 +1 行累积），根因=写回无前置门+基线混淆（checkout 回到的是上轮改写后的提交而非改写前）+仅凭行数守恒验收。

## 本机 shell 工具纪律（2026-11-06 考据）

ZCode Bash 工具在本机（Windows + Git Bash）的三条实测判据，均为静默失真类；细则与回归探针见项目记忆「本机工具坑」。

* **grep 实为 ZCode 注入函数（ugrep 7.8.4）**：函数预置 `-G --ignore-files --hidden -I`（定义在会话启动脚本，晚于用户 profile），**`--ignore-files` 按 .gitignore 语义过滤**——查 `en/`、`yuanwen/`、`script/` 等被忽略路径或做全量计数会**静默假 0**。判据：用 `command grep`／`/usr/bin/grep`，或追加 `--no-ignore-files`（ugrep 后旗标优先，实测可反转）；可疑时 `type -a grep` 验身份。
* **Bash 参数反斜杠连串减半**：MSYS argv 层把不在 `"` 前的 `\` 连串按 ceil(n/2) 减半（`\\`→`\`、`\\\\`→`\\`），quoted heredoc 不保护；单反斜杠（`\d`、sed `\t`、Windows 路径）与 `\` 紧邻 `"` 场景无损。判据：要 N 连串写 2N 个；正则块、多表达式 sed、含 `\\` 的 python 一律 Write 落盘再执行、sed 用 `-f`。
* **中文内联编码复测无损**（2026-11-06，python 3.14 UTF-8 默认）；中文落盘仍优先 Write 脚本文件（防御性，成本为零）。

## 提交策略

* 高频小步提交：完成一个单元立即提交，不攒大批改动。
* 提交信息中文一行简述，如“重译 阿尔克迈翁：初译 + 一校”。
* 只提交与本次工作相关的文件；原始物（`en/`、`yuanwen/`、`script/`）不入库。
* 直接提交 main 分支；未经用户要求不 push、不做 force 操作。
* 本机 GPG 已根治（2026-11-06 用户裁定）：私钥在 gpg4win（`C:/Program Files/GnuPG/bin/gpg.exe`）而全局曾配 `commit.gpgsign=true` 是「签名失败/挂死」根源；现已全局 `gpg.program` 指向 gpg4win 并关闭自动签名——提交默认免签、无需 `--no-gpg-sign`，需要签名时显式 `git commit -S`（交互输口令）。
