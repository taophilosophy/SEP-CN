# CI 约定与本地工具

本规则约定 CI 工作流的行为边界与本地工具的使用方式。**本地脚本只是 CI 的预演，结果以 CI 为准** （宪法 VI）。

工具与工作流都是手段：新增或修改检查器前，先确认要拦哪类错误、以哪条门禁验收；不以工具数量、运行时长或 CI 次数衡量治理成效（[08](08-intent-first.md)）。

## CI 工作流清单（`.github/workflows/`）

| 工作流 | 行为 | 触发 |
| ---- | ---- | ---- |
| `checks.yml` | 仓库一致性门禁**矩阵**（ADR-0061）：`plan` 作业跑 `tools/check_all.py --list-gates`（`GATES` 是唯一事实源），展开成每门禁一作业——`check_summary.py`（结构审计＋H1 一致性硬门禁，ADR-0024）＋`check_mulu_s.py`＋`check_doc_size.py`（ADR-0004）＋`check_junk.py`（垃圾/产物入库＋根目录白名单，ADR-0023）＋`check_images.py --gate`（图片引用完整性，rules/01）＋`check_terms.py`＋`check_quotes.py`＋`check_academic.py`（rules/07）＋`check_math_zh.py --strict`＋`divergence.py verify`（原始物分歧账，ADR-0045）＋管线单元测试；`fail-fast: false`，红灯作业名即门禁名，失败日志与图片报告入运行工件 | push / 手动 |
| `format.yml` | markdownlint／autocorrect／md-padding 三工具**矩阵**（ADR-0061）：手动触发各自 `--fix` 并各开一条 PR（合并前人工核 diff；禁机械替换译文，rules/05 生成器条）；PR 触发只读 markdownlint（告警级，权威配置根 `.markdownlint-cli2.jsonc`）。禁改区排除 `en/`、`yuanwen/`、两本登记册、`SUMMARY.md`、测试夹具、站点产物 | pull_request / 手动 |
| `links.yml` | lychee 链接检查；范围单点由 `.github/lychee.toml` 的 `exclude_path` 决定（原文 `en/`、镜像 `yuanwen/`、草稿/运行态/构建产物/夹具不查）。**报告口径（2026-11-16）**：检出死链开 issue，作业本身不硬拦（`fail: true` + `continue-on-error`，以保留真实退出码供 issue 步骤消费；`fail: false` 会加 `--no-fail` 使退出码恒 0、永不开 issue）。日志 `verbose` 保持 `warn`——`trace` 会把每条已检链接写进 job summary，实测 1.7 MB 超 GitHub 1 MB 上限 | 定时（每月 15 日 18:00 UTC）+ 手动 + repository_dispatch |
| `sep-sync-check.yml` | 每周抓取官方目录与 `.github/sep-baseline/official-snapshot.json` 比对，只报告、不改任何内容文件；报告入运行工件，非 `clean` 时开/更新 issue（`sep-upstream-sync`，抓取/解析失败另标 `sep-sync-broken`） | 定时（周一 18:30 UTC）+ 手动 |
| `Auto-Assign.yml` | issue/PR 自动分配 | issues / pull_request / 手动 |
| `create-pdf.yml` | 手动导出本项目中文 PDF/EPUB（gitbook-pdf-export 工具只读使用；可按首字母分批，全量约 2500 词条页；首字母过滤按 `## <字母>` 小节走，无链接的占位母行/别名行随节去留）；Python 3.15；产物仅上传运行工件，**不写 tag/Release/外部仓库**（2026-11-04 重写 D20；2026-11-16 适配，ADR-0061） | workflow_dispatch |
| `render-artifact-audit.yml` | 手动按 `SEP_SHARD` **四片矩阵**构建（`bun --bun x`，ADR-0014/0055）后逐片跑 `check_render_artifacts.py` 扫渲染残留（裸 `**`、字面 `[^`、链接残留、`@@M` 哨兵），有残留即红；报告入运行工件（2026-11-05 接线，ADR-0019；2026-11-16 矩阵化，ADR-0061） | workflow_dispatch |

* 不要新增与上述约定冲突的本地规则；需要新检查时先改 `tools/check_all.py` 的 `GATES`（CI 矩阵自动跟随）并在此登记。
* CI 红灯定位：打开 `checks.yml` 里红色的矩阵作业（作业名即门禁名），按其 `run` 命令在本地复现（如 `python tools/check_summary.py`）；各工具退出码语义见其 docstring，不按文字推断。门禁清单与本地 `check_all.py` 同源，不存在“CI 多查一项”。
* lint 配置统一在根目录 `.markdownlint-cli2.jsonc`（规则、纳入范围、按文件豁免），这是唯一一份（`.github/.markdownlint.json` 等价副本与 `.github/.autocorrectrc` 已于 2026-11-16 退役，ADR-0061）；autocorrect 配置为根 `.autocorrectrc`；`yuanwen/`（原文照录）与 `.zcode/`（本地工具）不参与 lint。
* 各工作流在文件顶部声明**最小 `permissions:`**（2026-11-15 按 CodeQL `actions/missing-workflow-permissions` 全量补齐）：只读校验类 `contents: read`；以 issue 反馈结果的加 `issues: write`；自动修复后开 PR 的加 `contents: write` + `pull-requests: write`。新增工作流照此就地声明，不依赖仓库默认权限。
* 修改工作流须同步更新本表（变更管理见 [06-governance.md](06-governance.md)）。

## 运行时基线（2026-11-10 起，ADR-0032）

* **Python ≥ 3.15**（本地验证 3.15.2；`tools/` 仅标准库，`check_all` 10 项与单元测试全绿）。
* **Node ≥ 26**（本地验证 26.13.0；Vite 8 要求 `^20.19 || >=22.12`，Node 26 满足；站点命令仍走 bun，见 ADR-0014）。
* **bun ≥ 1.4**（本地 1.4.4；`engines`/`packageManager` 钉在构建壳 `taophilosophy.github.io/package.json`，ADR-0055）。
* PDF 导出线（`create-pdf.yml`）用 Python 3.15（2026-11-16 用户裁定：随仓基线统一；原“暂留 3.13、待 weasyprint 上游支持”注记作废，ADR-0061）。

## 本地工具（`tools/`，Python 3 仅标准库）

| 工具 | 用途 |
| ---- | ---- |
| `fetch.py` / `fetch_catalog.py` / `fetch_entry.py` | SEP 抓取（正文、目录、词条包；串行默认 ≥5 秒间隔，失败显式化；并发模式间隔按 2026-10-27 用户裁定，见 specs/001 Assumptions） |
| `fetch_all.py` | 全量抓取+原文镜像驱动器（并发节拍 A=16 路×5s / B=64 路×10s，实测均无限流；`--resume` 断点续跑；逐条留痕 `script/fetch-all-log.jsonl`） |
| `extract_text.py` / `parser.py` / `yuanwen.py` | 原始 HTML → 提取文本（`en/`、`yuanwen/`，ADR-0027 起入库，随抓取批提交）；数学保真（2026-10-27 裁定）：跨块公式保护、公式内部原样保留，仅定界符统一 `$`/`$$`、空白折叠、表格内竖线一律以 `&#124;` 保义 |
| `baseline_audit.py` | 基线清单审计（哈希、版本钉一致性）；双账感知（ADR-0046）：已登记分歧且账目相符者计入 `divergent_registered` 不作 `hash_fail` |
| `divergence.py` | 原始物分歧账门禁（ADR-0045）：`verify` 三账一致（台账原始钉 ↔ 现文件 ↔ 登记；未登记的静默改 `en/` 即退出码 1，CI 经 check_all 覆盖）；`--deep` 加核 `base_commit` 的 git blob（本地，需完整历史）；`register`/`carry`（三方合并逆向补丁随迁，冲突退出码 3 转人工，`--merged` 复跑，随迁即归档新上游快照并前移钉）/`unregister`/`patch`/`list` |
| `drift_scan.py` | 全量回源 sha 核对（ADR-0045 跟进项，一次性豁免令 2026-11-15）：1872 词条 live index.html 对原始钉只读审计；64路×10s 已验证并发配置，逐请求留痕、429/5xx 退避不变；报告落盘 specs/001 results/drift-scan-<ts>.json；不进 CI（批量任务按需跑） |
| `task_ops.py` | 文档任务状态机（show / create / advance / clear / block） |
| `check_style.py` | 体例检查（引号、空格、HTML/AsciiDoc 残留、italic-cjk；输出 JSON）；`--connector-scan` 连接号形态告警（connector-form，GB/T 15834 §4.13，ADR-0041，告警级不进 CI） |
| `check_prose.py` | 语言质量预检（ADR-0020，**告警级**，不进 CI）：长句、被动、弱动词、“的”链、类名“们”、作为一个、存在着、当…的时候 八则＋时态词冗余、并列连词接动词、“成功地” 三则（2026-11-14 扩项，specs/027）反欧化模式；输出 JSON，默认退出码 0，`--strict` 升硬 |
| `check_render_artifacts.py` | 渲染产物残留物扫描（ADR-0019）：对构建产物 HTML 做文本级检查——裸 `**`（星内空格粗体永不渲染）、字面 `[^`（脚注配对失效）、`](`链接残留、数学哨兵 `@@M`；代码块/预排块内字面量豁免。分期转硬门禁（`raw[^` 待镜像脚注修复后纳入） |
| `check_images.py` | 图片引用检查（rules/01 图片三条硬性要求）：悬空引用、大小写不符（Windows 不敏感/CI 404）、外部地址、`assets/` 未引用资产；跳过代码块与行内代码，`yuanwen/` 缺位（CI）时跳过镜像引用；报告写 `state/image-report.md`（本地）或 `image-report.md`（CI 开 issue 用），无问题即清除旧报告，默认退出码 0；`--gate` 时悬空/大小写/外链任一 >0 退出 1（check_all 与 CI 门禁用） |
| `check_summary.py` | SUMMARY.md 结构审计（条目解析、缺失文件、孤儿文件、命名、重复）＋ H1 一致性硬门禁（SUMMARY 条目文字 ↔ 文件 H1，ADR-0024）＋ 别名行英文完整标题硬门禁（`alias fragment`，ADR-0024）；硬错误退出码 1；`--headers` 只查标题（CI 用），`--sync-headers` 按 SUMMARY 同步 H1（本地用，写回后跑残差门） |
| `check_mulu_s.py` | 分类目录 ↔ SUMMARY 对应性检测（坏链、覆盖缺口、标题不一致、重复收录）；坏链/路径错/标题不一致为硬错误，退出码 1 |
| `check_junk.py` | 垃圾/产物入库门禁（ADR-0003 + ADR-0023 + ADR-0027）：缓存、构建产物、系统杂物命中即退出码 1（`en/`、`yuanwen/` 已入库，不再判违规）；根目录白名单对跟踪清单与工作区双向核对，根级散件无论是否入库一律红灯 |
| `check_tables_images.py` | 表格与图片预检（ADR-0037，**告警级**，不进 CI）：表块结构（缺分隔行、列数不一致）、单元格全角空格与多空格填充、表内未译英文散文候选、学术工具节表形态、图片 alt 非中文、引用基座违规与解析失败；`--yuanwen` 扫镜像结构项、`--corpus` 出并集清单；默认退出码 0，`--gate` 时基座违规/解析失败升硬（图片项与 `check_images.py --gate` 重叠处以后者入闸为准） |
| `check_terms.py` | 术语一致性门禁（specs/002、specs/031）：两登记册自洽（废弃链断裂、同键同译法重复为硬错误，退出码 1）；缺依据/裁定日期、非英语术语缺原文、人名缺籍属生卒为告警；`--docs` 定点核销告警级；`--ledger <路径>` 写判读台账骨架、`--check-ledger <路径>` 校验台账闭合（D 类/三出口/证据/凭证/复核人，ADR-0048） |
| `register_lib.py` | 登记册共享解析/折叠库（specs/033）：键折叠三口径唯一实现——A `norm_key_quote`（引号折叠，登记册↔正文比对）、B `norm_key`（基础折叠，候选/凭证/核销）、C `fold_nfd`（azsort 节内排序内层，禁改）；行解析 `split_row`/`is_data_row`/`parse_registry*` 与 A–Z 分节 `bucket_of`；消费方（check_terms/registry_azsort/term_*）一律引用，禁再复制函数体 |
| `mech_audit.py` | 机械替换回溯审计（specs/031，ADR-0048 决策 4/7）：对指定词条历次修复 commit 逐行 diff 分类 `pure`（仅标点变动）/`conn`（≤4 字小块）/`susp`（相似 0.85–0.95），**只产候选不作定性**；`--since`、`--marker`、`--out`（默认 `state/mech-audit-latest.json`） |
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
| `check_math_zh.py` | 译文侧公式体例门禁（021 战役，D26 接线）：C1 宏残留/C2 内侧空白/C3 不可见字符/C4 未转义 %#/C5 中文入公式/C6 裸 $/C7 未转义货币/C8 英连接语/C9 散文 `\\(` 九类；默认 C1–C6+C8 硬错误，`--strict` 加 C7/C9（check_all 与 s3/r3 任务门用 strict） |
| `check_pairs.py` | 格式配对与一致性预检（ADR-0046，**告警级**，不进 CI）：全角括号/书名号配对与方向（序次语 N）豁免）、文内作者-年份引注与书目一致（en 书目交叉、破折号承接链）、书目键重复、节/书目/公式数量对照（zh vs en/yuanwen）、相对链接悬空、出版信息行形态、省略号六连点；输出 JSON，默认退出码 0，`--strict` 升硬 |
| `check_all.py` | 一键全量合规复核（十项门禁 + 单元测试；`--all` 加 baseline_audit、en_integrity 与 divergence --deep；`--quiet` 只报失败）；`--list-gates` 输出 CI 门禁矩阵 JSON（`checks.yml` 的唯一数据源，ADR-0061，改门禁只改 `GATES`）；收工前/推审前跑一次 |
| `indep_review.py` | 形态横向清账扫描器（ADR-0047，s3 前置独立步骤，**告警级**，不进 CI）：六类判据 `bib-heading-form`（参考文献节名正典，W7）、`pubinfo-form`（出版信息行形态＋与 en 源有无一致，W8）、`bib-subsection`（文献分类子标题丢失）、`style`（check_style 全则，O1）、`quote-adjacent`（引号↔西文邻接，O2，脚注键/链接/转写撇号已遮蔽）、`pairs`（ADR-0046 七则）；默认只扫已译集合，`--letter` 分字头、`--class` 单类、`--all-files` 含存根、`--classes` 列判据 |
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

* 纳入/豁免写在 `.markdownlint-cli2.jsonc` 的 `globs` / **`ignores`** 两键——`ignoreGlobs` 与 `overrides` 是死键（官方 README 无此键；2026-11-06 README 考据＋A/B 实测复现“静默无效”，v0.24.0 验证，排除生效时 finding 以 `!` 前缀可见）；按文件豁免用行内 `<!-- markdownlint-disable -->`。
* 表格风格统一 **compact**（每个单元格两侧恰一个空格，空单元格恰一个空格；MD060 `aligned` 按显示宽度计量、CJK/emoji 记 2——官方 doc/md060.md，2026-11-06 全仓整改裁定口径；表格内竖线一律转义）。

## 站点运行（本地预演）

阅读站的构建机制是实现细节，见 [`.vitepress/README.md`](../.vitepress/README.md)（**说明而非规则**）；本节只记命令与硬约束。

* 依赖与构建入口在壳仓 `taophilosophy.github.io`（docs/ 为指向本仓的子模块，[ADR-0055](adr/0055-构建壳与内容仓分权.md)）：clone 壳 → `git submodule update --init` → 在壳根 `bun install` → `bun run dev` / `build` / `preview`（VitePress root = `docs`）。本仓不持有 `package.json` / `bun.lock`，不在本仓跑包管理；包管理统一 bun，不使用 npm / npx（[ADR-0014](adr/0014-包管理统一bun弃用npm.md)）。
* dev 固定 `0.0.0.0:81` 且 `strictPort`：端口被占即启动失败，不换端口、不静默降级。
* `dev` 与 `build` 由壳脚本先跑 `.vitepress/prepare-assets.mjs`（MathJax 离线资源）与 `prepare-gitstamps.mjs`（页脚时间戳）；依赖被 hoist 到壳根时脚本自 `.vitepress/` 逐级向上解析 `node_modules`，产物固定写回本仓。`preview` 不跑这两步，故须先 `build`。
* 页面范围由 `.vitepress/config.mts` 的 `srcExclude` 控制：治理/管线目录（`rules/`、`specs/`、`tools/`、`tasks/`、`.qoder/` 等）一律不进站点；**新增此类目录须同步补 `srcExclude`**，否则会被构建为页面并进入全文搜索索引。

## 生成器与批量改写脚本（2026-10-30，SUMMARY 字母分节重排教训规则化）

凡对登记册/目录/正文做**程序化批量改写**（生成器、重排器、批量注入），一律遵守：

* **写回前置门**：改写结果存在任何未落位/未消费条目时**禁止写回**，dry-run 中止并列出明细（exit 非零）。残余计数以 **0** 为唯一通过标准；“行数守恒”“总量一致”只是必要条件，不构成通过证据。
* **禁止静默兜底降级**：fallback（节尾追加、缺省件补位）必须显式登记清单并计入失败面；同一输入重复运行**不得追加重复行**（幂等：同 raw 已存在即跳过）。
* **逐行身份追踪验收**：批量改写的验收=每条输入行的身份与落位坐标全量核对；只看总数（行数/字节数）不构成验收。抽查不少于 5 条且必须覆盖移动距离最大的行。
* **基线还原强制**：改写前 `git checkout -- <目标文件>` 并以 `git diff` 校验基线干净；**多会话并行下，任何 checkout 后必须重新 `git status` 确认**（并行会话可能已再次写入）。禁止在上一轮改写输出上迭代运行。
* **观察驱动调试**：失败定位先在**实际执行路径**加探针（消费点、写回点），禁止只凭对脚本逻辑的心智模型反复修补；单测复现的输入必须与批处理运行的输入逐字节一致。
* **适用范围排除**：把登记译法或体例措辞**套进译文正文**不属于本条授权的批量改写——术语按 [03](03-terminology.md) 差异处置（禁机械替换、逐处回源、差异联网查证，[ADR-0048](adr/0048-术语落地差异处置标准.md)），措辞按 [02](02-style.md) 逐句改。本条只适用于结构层与登记层（目录、登记册行、生成物），且产物须可复算。
* 失败实例存档：2026-10-30 SUMMARY 重排，占位行残余连续四轮被兜底掩盖（每轮 +1 行累积），根因=写回无前置门+基线混淆（checkout 回到的是上轮改写后的提交而非改写前）+仅凭行数守恒验收。

## 本机 shell 工具纪律（2026-11-06 考据）

ZCode Bash 工具在本机（Windows + Git Bash）的三条实测判据，均为静默失真类；细则与回归探针见项目记忆“本机工具坑”。

* **grep 实为 ZCode 注入函数（ugrep 7.8.4）**：函数预置 `-G --ignore-files --hidden -I`（定义在会话启动脚本，晚于用户 profile），**`--ignore-files` 按 .gitignore 语义过滤**——查 `en/`、`yuanwen/`、`script/` 等被忽略路径或做全量计数会**静默假 0**。判据：用 `command grep`／`/usr/bin/grep`，或追加 `--no-ignore-files`（ugrep 后旗标优先，实测可反转）；可疑时 `type -a grep` 验身份。
* **Bash 参数反斜杠连串减半**：MSYS argv 层把不在 `"` 前的 `\` 连串按 ceil(n/2) 减半（`\\`→`\`、`\\\\`→`\\`），quoted heredoc 不保护；单反斜杠（`\d`、sed `\t`、Windows 路径）与 `\` 紧邻 `"` 场景无损。判据：要 N 连串写 2N 个；正则块、多表达式 sed、含 `\\` 的 python 一律 Write 落盘再执行、sed 用 `-f`。
* **中文内联编码复测无损**（2026-11-06，python 3.14 UTF-8 默认）；中文落盘仍优先 Write 脚本文件（防御性，成本为零）。

## 提交策略

* 高频小步提交：完成一个单元立即提交，不攒大批改动。
* 提交信息中文一行简述，如“重译 阿尔克迈翁：初译 + 一校”。
* 只提交与本次工作相关的文件；原始物（`en/`、`yuanwen/`、`script/`）不入库。
* 直接提交 main 分支；**提交即推**（ADR-0059，2026-11-16 用户裁定）：`git commit` 成功后立即 `git push`，推前 `git fetch`、落后先 `python tools/sync_guard.py pull`，被拒重跑 pull 再推；`--force` 仍禁。
* 本机 GPG 已根治（2026-11-06 用户裁定）：私钥在 gpg4win（`C:/Program Files/GnuPG/bin/gpg.exe`）而全局曾配 `commit.gpgsign=true` 是“签名失败/挂死”根源；现已全局 `gpg.program` 指向 gpg4win 并关闭自动签名——提交默认免签、无需 `--no-gpg-sign`，需要签名时显式 `git commit -S`（交互输口令）。
