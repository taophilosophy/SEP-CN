# 本地工具与配置

## 本地工具（`tools/`，Python 3 仅标准库）

| 工具 | 用途 |
| ---- | ---- |
| `fetch.py` / `fetch_catalog.py` / `fetch_entry.py` | SEP 抓取（正文、目录、词条包；退避重试与失败显式化；2026-11-18 起无最小请求间隔，ADR-0069）。`fetch_catalog.py --snapshot-only`＝只落 `en/_catalog` 快照不写账（CI 巡检用）；`--reparse`／`--reparse-snap`＝离线重解析建账 |
| `fetch_all.py` | 全量抓取+原文镜像驱动器（并发路数 A=16 / B=64（默认），不设节拍；`--resume` 断点续跑；逐条留痕 `script/fetch-all-log.jsonl`） |
| `extract_text.py` / `parser.py` / `yuanwen.py` | 原始 HTML → 提取文本（`en/`、`yuanwen/`，ADR-0027 起入库，随抓取批提交）；数学保真（2026-10-27 裁定）：跨块公式保护、公式内部原样保留，仅定界符统一 `$`/`$$`、空白折叠、表格内竖线一律以 `&#124;` 保义 |
| `baseline_audit.py` | 基线清单审计（哈希、版本钉一致性）；双账感知（ADR-0046）：已登记分歧且账目相符者计入 `divergent_registered` 不作 `hash_fail` |
| `divergence.py` | 原始物分歧账门禁（ADR-0045）：`verify` 三账一致（台账原始钉 ↔ 现文件 ↔ 登记；未登记的静默改 `en/` 即退出码 1，CI 经 check_all 覆盖）；`--deep` 加核 `base_commit` 的 git blob（本地，需完整历史）；`register`/`carry`（三方合并逆向补丁随迁，冲突退出码 3 转人工，`--merged` 复跑，随迁即归档新上游快照并前移钉）/`unregister`/`patch`/`list` |
| `drift_scan.py` | 全量回源 sha 核对（ADR-0045 跟进项，一次性豁免令 2026-11-15）：1872 词条 live index.html 对原始钉只读审计；64路×10s 已验证并发配置，逐请求留痕、429/5xx 退避不变；报告落盘 specs/001 results/drift-scan-<ts>.json；不进 CI（批量任务按需跑） |
| `task_ops.py` | 文档任务状态机（show / create / advance / clear / block） |
| `check_style.py` | 体例检查（引号、quote-spacing、空格、HTML/AsciiDoc 残留、italic-cjk；输出 JSON）；`--connector-scan` 连接号形态告警（connector-form，GB/T 15834 §4.13，ADR-0041，告警级不进 CI） |
| `check_prose.py` | 语言质量预检（ADR-0020，**告警级**，不进 CI）：长句、被动、弱动词、“的”链、类名“们”、作为一个、存在着、当…的时候 八则＋时态词冗余、并列连词接动词、“成功地” 三则（2026-11-14 扩项，specs/027）反欧化模式；输出 JSON，默认退出码 0，`--strict` 升硬 |
| `check_render_artifacts.py` | 渲染产物残留物扫描（ADR-0019）：对构建产物 HTML 做文本级检查——裸 `**`（星内空格粗体永不渲染）、字面 `[^`（脚注配对失效）、`](`链接残留、数学哨兵 `@@M`；代码块/预排块内字面量豁免。分期转硬门禁（`raw[^` 待镜像脚注修复后纳入） |
| `check_images.py` | 图片引用检查（rules/01 图片三条硬性要求）：悬空引用、大小写不符（Windows 不敏感/CI 404）、外部地址、`assets/` 未引用资产；`/...` 站点绝对路径单列**告警**（非本仓相对引用，多来自抄录的上游 HTML，不入硬门）；跳过代码块与行内代码，`yuanwen/` 缺位（CI）时跳过镜像引用；报告写 `state/image-report.md`（本地）或 `image-report.md`（CI 开 issue 用），无问题即清除旧报告，默认退出码 0；`--gate` 时悬空/大小写/外链任一 >0 退出 1（check_all 与 CI 门禁用） |
| `check_summary.py` | SUMMARY.md 结构审计（条目解析、缺失文件、孤儿文件、命名、重复）＋ H1 一致性硬门禁（SUMMARY 条目文字 ↔ 文件 H1，ADR-0024）＋ 别名行英文完整标题硬门禁（`alias fragment`，ADR-0024）；硬错误退出码 1；`--headers` 只查标题（CI 用），`--sync-headers` 按 SUMMARY 同步 H1（本地用，写回后跑残差门） |
| `check_mulu_s.py` | 分类目录 ↔ SUMMARY 对应性检测（坏链、覆盖缺口、标题不一致、重复收录）；坏链/路径错/标题不一致为硬错误，退出码 1 |
| `rebuild_catalog.py` / `check_catalog_network.py` | 目录域装配器＋四向重放门（specs/054）：`--build` 产骨架账＋噪声池（A5 四类准入，建池冻结）；重放＝账⊕规则⊕池，`--check` sha256 对钉存快照（B3.2 全等）；`--gate`＝G1 装配等值（两时点）/G2 en-SUMMARY 重放/G3 mu-lu 重放（＋文字跟随）/G4 目录↔SUMMARY 对账；禁写回 `en/_catalog/`（oracle 只读） |
| `check_junk.py` | 垃圾/产物入库门禁（ADR-0003 + ADR-0023 + ADR-0027）：缓存、构建产物、系统杂物命中即退出码 1（`en/`、`yuanwen/` 已入库，不再判违规）；根目录白名单对跟踪清单与工作区双向核对，根级散件无论是否入库一律红灯 |
| `catalog_drift.py` | 上游目录四方漂移巡检（specs/054 运营化，`catalog-drift.yml` 调用）：上游 contents.html ↔ catalog 账／SUMMARY／mu-lu-s，报增删、改名、作者变、别名变与两向覆盖缺口；`--assembly` 加做 B3.2 装配核验（残差超 A5 四类即格式层漂移）；`--latest` 取最新快照；只报告，退出码 1＝有漂移 |
| `detect_updates.py` | 上游变更检测（specs/001 T020-21 契约）：`new.html` 的 NEW/REVISED（默认 90 天窗；`sep.xml` 已失效记 `feed=unavailable`）＋ `archinfo.cgi` 版次核对 → 队列（new→retranslate／revised→update）；`--verify-web` 抓 index.html 核内容钉剔除假阳性（列表标改、实际与钉一致）；`synced_skipped`（`fetched_at` ≥ 事件日）与 `verified_same` 两栏解释被剔原因；`--no-write` 仅抑制默认 `baseline/queue.json` |
| `check_tables_images.py` | 表格与图片预检（ADR-0037，**告警级**，不进 CI）：表块结构（缺分隔行、列数不一致）、单元格全角空格与多空格填充、表内未译英文散文候选、学术工具节表形态、图片 alt 非中文、引用基座违规与解析失败；`--yuanwen` 扫镜像结构项、`--corpus` 出并集清单；默认退出码 0，`--gate` 时基座违规/解析失败升硬（图片项与 `check_images.py --gate` 重叠处以后者入闸为准） |
| `check_terms.py` | 术语一致性门禁（specs/002、specs/031）：两登记册自洽（废弃链断裂、同键同译法重复为硬错误，退出码 1）；缺依据/裁定日期、非英语术语缺原文、人名缺籍属生卒为告警；`--docs` 定点核销告警级；`--ledger <路径>` 写判读台账骨架、`--check-ledger <路径>` 校验台账闭合（D 类/三出口/证据/凭证/复核人，ADR-0048） |
| `register_lib.py` | 登记册共享解析/折叠库（specs/033）：键折叠三口径唯一实现——A `norm_key_quote`（引号折叠，登记册↔正文比对）、B `norm_key`（基础折叠，候选/凭证/核销）、C `fold_nfd`（azsort 节内排序内层，禁改）；行解析 `split_row`/`is_data_row`/`parse_registry*` 与 A–Z 分节 `bucket_of`；消费方（check_terms/registry_azsort/term_*）一律引用，禁再复制函数体 |
| `mech_audit.py` | 机械替换回溯审计（specs/031，ADR-0048 决策 4/7）：对指定词条历次修复 commit 逐行 diff 分类 `pure`（仅标点变动）/`conn`（≤4 字小块）/`susp`（相似 0.85–0.95），**只产候选不作定性**；`--since`、`--marker`、`--out`（默认 `state/mech-audit-latest.json`） |
| `check_math.py` | 数学保真门禁（2026-10-27 裁定）：原始 HTML 每条公式内容必须原样出现在 yuanwen 产物；占位符残留、行内 `$` 失衡为硬错误（退出码 1） |
| `check_doc_size.py` | 单体文件大小门禁（ADR-0004）：叙事/规则/规格类 md 超 1000 行或 100KB 即退出码 1；约束性规则 `rules/0X.md` 超 300 行或 30KB 须拆 `rules/0X/` 目录（`rules/05` 为本规则 2026-11-19 拆分实例）；登记册与生成物豁免 |
| `check_academic.py` | 哲学学术规范门禁（rules/07、specs/003）：非存根词条的参考文献/学术工具/译注/脚注配对、任务版本钉；`--docs <路径>...` 定点、`--strict` 告警升硬；CI 无 `en/` 原始包时注号定义（`note-*`）的补充材料跨文件引用无从核对，降级 `orphan-def-unverified` 告警（本地 `check_all` 有 en/ 时照常硬拦） |
| `compare.py` | 段落级变更比较（spec 001 US-3）：抓取英文源最新快照（不覆盖 en/ 基线）与基线比较，节级 added/removed/moved + 段落级 diff，映射中文文档与节行号；无 zh_doc 标注待建任务 |
| `fetch_audit.py` | 抓取完整性主动闭环：校验每词条包内全部被引用资产在包内，缺件自动补抓（404=缺省件登记）；引用闭包迭代至不动点（一切形如文件名的裸引用皆词条资产——页面/图片/词条自有 js/css/媒体；注释剥离＋实体反解后统计，与浏览器语义一致） |
| `en_integrity.py` | 英文镜像逐词条深度复核（纯离线）：页面真实性（SEP 签名/截断/零字节）、引用闭包按上游 URL 语义解析（大小写精确、跨词条与子目录资产）、目录结构一致性（在盘文件＝被引用（含跨词条入站）∪已登记，否则游离）、数学形态盘点；全量凭证 `specs/001-sep-sync-pipeline/en-integrity-full.json` |
| `biblio_audit.py` | 参考文献结构盘点与中文文献定位（ADR-0011）：条目量/链接域统计；三探针（实体解码汉字/典籍专名/作者位拼音）标出需按 ADR-0011 还原的词条与条目，供 s1 一校与质检定位 |
| `cnki_query.py` | 术语依据查询（ADR-0012 译名依据源）：知网系权威源（CNKI 翻译助手、术语在线）在线查询与缓存；2026-11-14 起为存量凭证通道，不再新增查询（rules/03） |
| `term_audit.py` / `term_harvest.py` | 术语战役工具（specs/008）：登记册审计与候选收割（008 池裁定流水线） |
| `campaign.py` | 全局统计表与批次调度（specs/005 并行设计）：a–z 批次账本（认领/阶段/断点续上），计数实时推导零漂移，多会话独立无耦合 |
| `check_math_zh.py` | 译文侧公式体例门禁（021 战役，D26 接线）：C1 宏残留/C2 内侧空白/C3 不可见字符/C4 未转义 %#/C5 中文入公式/C6 裸 $/C7 未转义货币/C8 英连接语/C9 散文 `\\(` 九类；默认 C1–C6+C8 硬错误，`--strict` 加 C7/C9（check_all 与 s3/r3 任务门用 strict） |
| `check_pairs.py` | 格式配对与一致性预检（ADR-0046，**告警级**，不进 CI）：全角括号/书名号配对与方向（序次语 N）豁免）、文内作者-年份引注与书目一致（en 书目交叉、破折号承接链）、书目键重复、节/书目/公式数量对照（zh vs en/yuanwen）、相对链接悬空、出版信息行形态、省略号六连点；输出 JSON，默认退出码 0，`--strict` 升硬 |
| `check_all.py` | 一键全量合规复核（门禁项数以 `--list-gates` 为准，ADR-0061/0067；`--all` 另加 baseline_audit、en_integrity 与 divergence --deep；`--quiet` 只报失败）；`--list-gates` 输出 CI 门禁矩阵 JSON（`checks.yml` 的唯一数据源，改门禁只改 `GATES`）；收工前/推审前跑一次 |
| `check_layout.py` | 目录布局一致性门禁（ADR-0067）：`rules/layout.json` 为唯一事实源，L1 根⊆声明／L2 `rules/01` 表≡源（双向）／L3 容器有索引或写明理由的 `index_exempt`／L4 specs 容器 schema（必需 `spec.md`、禁 `tmp/`、规格根禁 JSON、`execution-log` 两形态不并存）；只读，`--json` 出机读 |
| `spec_index.py` | 生成 `specs/README.md` 索引（ADR-0067，生成物不手改）；`--check` 只校验一致性（CI 可用） |
| `indep_review.py` | 形态横向清账扫描器（ADR-0047，s3 前置独立步骤，**告警级**，不进 CI）：六类判据 `bib-heading-form`（参考文献节名正典，W7）、`pubinfo-form`（出版信息行形态＋与 en 源有无一致，W8）、`bib-subsection`（文献分类子标题丢失）、`style`（check_style 全则，O1）、`quote-adjacent`（引号↔西文邻接，O2，脚注键/链接/转写撇号已遮蔽）、`pairs`（ADR-0046 七则）；默认只扫已译集合，`--letter` 分字头、`--class` 单类、`--all-files` 含存根、`--classes` 列判据 |
| `clean.py` | 本地垃圾清理器：默认试运行，`--go` 删除未跟踪缓存与临时文件（不触碰跟踪文件与 en/ 原始物） |
| `progress.py` | 生成 `PROGRESS.md` 进度汇总（自动生成，不手改）；含二维账与“账实不符”行（引用 `check_taskfile_invariant`） |
| `check_taskfile_invariant.py` | 任务账本↔译文一致性（specs/051，2026-11-19 起**严格档入 CI**）：I1 `cleared` ⟹ 译文仅 H1；I2 有正文 ⟹ journal 至少一个 `pass`；另列 `zh-doc-missing`／`maintenance-doc-missing` |
| `mandatory_backfill.py` | 强制集回补（specs/052/ADR-0075）：按现行判据重算 s0/s2.4/global，记 pass/fail；状态不迁移，fail 即停 |
| `summary_sync.py` | SUMMARY/mu-lu-s 目录同步与 intake（`apply-add` 为新词条接入唯一入口，职责权属见 specs/001 cli.md；report/apply-add/remove） |
| `sync_guard.py` | 双机同步护栏：`pull`（fetch＋rebase＋判弃自检实拦，ADR-0028）与 `status`（未推送自查；收工核对 `git log origin/main..main` 为空，ADR-0059） |
| `rebuild_dir.py` | 上游同构重建（ADR-0007 立项）：现役面＝`check` 镜像覆盖核验（rules/06 结构改动 done 判据）；`toletters` 为 ADR-0009 一次性迁移；rebuild/stubs/yuanwen 遗留废弃（specs/040 F-26） |
| `repair_loop.py` | 断链递归修复（2026-10-27 一次性工具，留档） |
| `term_coverage.py` / `term_relations.py` | 术语落地全覆盖核验与三表关系审计（specs/008 常态流程；只报告不修改，告警走 rules/03 三出口） |
| `term_flow.py` | 术语落册统一流水线（rowspec 驱动幂等落册，specs/008） |
| `registry_azsort.py` | 登记册 A–Z 分节重排（行序守恒门＋幂等，specs/033 消费方） |
| `gen_en_summary.py` | 生成 GitBook 英文空间 TOC `yuanwen/SUMMARY-en.md`（ADR-0056，生成物不手改）；`--check` 只校验（已并入 `check_catalog_network.py` 的 G2 门） |
| `en_patch_lib.py` | 补丁池唯一解析实现（目录正本三律＋C2 准入谓词，ADR-0062/0063；消费方＝yuanwen.py/check_en_patches.py） |
| `common.py` | 管线共享库（UTF-8 读写＋写后读回核验、SHA-256、SUMMARY 三级 zh_doc 匹配；非 CLI） |
| `compose_from_ledger.py` | 【已废弃留档】旧布局（tasks/h/）账本拼装器（specs/040 F-25） |
| `migrate_exec.py` | 【已废弃留档】拼音 slug 迁移执行器（ADR-0007/0008 后布局已不存在） |
| `termonline_token.py` / `tl_browser_batch.py` / `tl_crawler.py` | 术语在线通道三件（token 解密／浏览器批次／编程爬虫，specs/008；2026-11-14 起不再新增查询，存量凭证） |
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

* markdownlint（配置驱动，仓库根目录执行；包管理统一 bun，不使用 npm，见 [ADR-0014](../adr/0014-包管理统一bun弃用npm.md)）：

  ```sh
  bunx markdownlint-cli2            # 按 .markdownlint-cli2.jsonc 的 globs 与规则检查
  bunx markdownlint-cli2 --fix      # 自动修复可修复项
  ```

* 纳入/豁免写在 `.markdownlint-cli2.jsonc` 的 `globs` / **`ignores`** 两键——`ignoreGlobs` 与 `overrides` 是死键（官方 README 无此键；2026-11-06 README 考据＋A/B 实测复现“静默无效”，v0.24.0 验证，排除生效时 finding 以 `!` 前缀可见）；按文件豁免用行内 `<!-- markdownlint-disable -->`。
* 表格风格统一 **compact**（每个单元格两侧恰一个空格，空单元格恰一个空格；MD060 `aligned` 按显示宽度计量、CJK/emoji 记 2——官方 doc/md060.md，2026-11-06 全仓整改裁定口径；表格内竖线一律转义）。
