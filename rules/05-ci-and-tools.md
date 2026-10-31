# CI 约定与本地工具

本规则约定 CI 工作流的行为边界与本地工具的使用方式。**本地脚本只是 CI 的预演，结果以 CI 为准** （宪法 VI）。

工具与工作流都是手段：新增或修改检查器前，先确认要拦哪类错误、以哪条门禁验收；不以工具数量、运行时长或 CI 次数衡量治理成效（[08](08-intent-first.md)）。

## CI 工作流清单（`.github/workflows/`）

| 工作流 | 行为 | 触发 |
| ---- | ---- | ---- |
| `checks.yml` | 仓库一致性门禁：`check_summary.py` + `check_mulu_s.py` + `check_junk.py`（垃圾/产物入库）+ `check_doc_size.py`（单体文件大小，ADR-0004）+ `check_terms.py`（术语一致性）+ `check_academic.py`（哲学学术规范，rules/07）+ `check_all.py --quiet`（一键全量复核汇总）+ 管线单元测试，硬错误即红灯 | push / 手动 |
| `sync-headers.yml` | 把每个 SUMMARY 条目对应文件的 H1 改写为条目文字（含转义还原 `\* \[ \]`；跳过 frontmatter 文件；覆盖缩进子条目），自动提交 | push |
| `file-name-check.yml` | 校验 SUMMARY 条目文件存在，缺失自动开 issue | push |
| `markdown-lint2.yml`（手动）/ `Markdown-lint2-pr.yml`（PR 触发） | markdownlint 检查（统一配置 `.markdownlint-cli2.jsonc`；手动流可 `--fix` 开格式化 PR） | 手动 / pull_request |
| `check-images.yml` | 图片引用检查（悬空、可解析、本地化） | push |
| `links.yml` | 链接检查 | 定时（每月 15 日 18:00 UTC）+ 手动 + repository_dispatch |
| `md-padding.yml`、`AutoCorrect.yml` | 手动触发，自动补 CJK 空格并以 PR 提交，合并前人工核对 diff | 手动 |
| `Auto-Assign.yml`、`GC.yml`、`create-pdf.yml` | issue/PR 自动分配、垃圾回收、PDF 导出 | 各自约定 |

* 不要新增与上述约定冲突的本地规则；需要新检查时先改 `tools/` 并在此登记。
* CI 红灯定位：打开 `checks.yml` 的第一个失败 step，按上表同名工具在本地用相同命令复现（如 `python tools/check_summary.py`）；各工具退出码语义见其 docstring，不按文字推断。
* lint 配置统一在根目录 `.markdownlint-cli2.jsonc`（规则、纳入范围、按文件豁免），`.github/.markdownlint.json` 保留为等价规则副本；`yuanwen/`（原文照录）与 `.zcode/`（本地工具）不参与 lint。
* 修改工作流须同步更新本表（变更管理见 [06-governance.md](06-governance.md)）。

## 本地工具（`tools/`，Python 3 仅标准库）

| 工具 | 用途 |
| ---- | ---- |
| `fetch.py` / `fetch_catalog.py` / `fetch_entry.py` | SEP 抓取（正文、目录、词条包；串行默认 ≥5 秒间隔，失败显式化；并发模式间隔按 2026-10-27 用户裁定，见 specs/001 Assumptions） |
| `fetch_all.py` | 全量抓取+原文镜像驱动器（并发节拍 A=16 路×5s / B=64 路×10s，实测均无限流；`--resume` 断点续跑；逐条留痕 `script/fetch-all-log.jsonl`） |
| `extract_text.py` / `parser.py` / `yuanwen.py` | 原始 HTML → 提取文本（`en/`、`yuanwen/`，不入库）；数学保真（2026-10-27 裁定）：跨块公式保护、公式内部原样保留，仅定界符统一 `$`/`$$`、空白折叠、表格内 `|` 用 `&#124;` 保义 |
| `baseline_audit.py` | 基线清单审计（哈希、版本钉一致性） |
| `task_ops.py` | 文档任务状态机（show / create / advance / clear / block） |
| `check_style.py` | 体例检查（引号、空格、HTML/AsciiDoc 残留；输出 JSON） |
| `check_prose.py` | 语言质量预检（ADR-0020，**告警级**，不进 CI）：长句、被动、弱动词、“的”链、类名“们”、作为一个、存在着、当…的时候 八则反欧化模式；输出 JSON，默认退出码 0，`--strict` 升硬 |
| `check_render_artifacts.py` | 渲染产物残留物扫描（ADR-0019）：对构建产物 HTML 做文本级检查——裸 `**`（星内空格粗体永不渲染）、字面 `[^`（脚注配对失效）、`]( `链接残留、数学哨兵 `@@M`；代码块/预排块内字面量豁免。分期转硬门禁（`raw[^` 待镜像脚注修复后纳入） |
| `check_summary.py` | SUMMARY.md 结构审计（条目解析、缺失文件、孤儿文件、命名、重复）；硬错误退出码 1 |
| `check_mulu_s.py` | 分类目录 ↔ SUMMARY 对应性检测（坏链、覆盖缺口、标题不一致、重复收录）；坏链/路径错/标题不一致为硬错误，退出码 1 |
| `check_junk.py` | 垃圾/产物入库门禁（ADR-0003）：原始物、缓存、构建产物、系统杂物命中即退出码 1 |
| `check_terms.py` | 术语一致性门禁（specs/002）：登记册 ↔ 词汇表译法互斥冲突、登记册废弃链/重复为硬错误（退出码 1）；词汇表滞后、缺裁定日期、`--docs` 定点核销仅告警 |
| `check_math.py` | 数学保真门禁（2026-10-27 裁定）：原始 HTML 每条公式内容必须原样出现在 yuanwen 产物；占位符残留、行内 `$` 失衡为硬错误（退出码 1） |
| `check_doc_size.py` | 单体文件大小门禁（ADR-0004）：叙事/规则/规格类 md 超 1000 行或 100KB 即退出码 1；登记册与生成物豁免 |
| `check_academic.py` | 哲学学术规范门禁（rules/07、specs/003）：非存根词条的参考文献/学术工具/译注/脚注配对、任务版本钉；`--docs <路径>...` 定点、`--strict` 告警升硬 |
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

## 提交策略

* 高频小步提交：完成一个单元立即提交，不攒大批改动。
* 提交信息中文一行简述，如“重译 阿尔克迈翁：初译 + 一校”。
* 只提交与本次工作相关的文件；原始物（`en/`、`yuanwen/`、`script/`）不入库。
* 直接提交 main 分支；未经用户要求不 push、不做 force 操作。
* 本机 git 配置了 GPG 签名但无私钥时，用 `git commit --no-gpg-sign`。
