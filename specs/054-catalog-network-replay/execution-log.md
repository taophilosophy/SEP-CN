# specs/054 执行记录

## 2026-11-19 第一轮：立项＋账升级＋装配器＋四向门（A1–A6 达成，A7 凭证随本记录）

### 0. 试金石（动笔前小样本，ADR-0039）

试金石脚本在 `script/tmp/archive-q/`（gitignored 草稿区）：`probe_reconstruct.py`（P0–P4 分层测量）、
`probe2_closure.py`（行族分类）、`probe3_assemble.py`（四层闭合率）、`probe4_align.py`、`probe5_scan.py`
（推进对齐算法预演）。两时点钉存快照＝`20261027T171130Z` / `20261114T231750Z`。

关键实测：
- 正典 1872／别名 653 行／簇母行 188（窄正则）→ 修正后 225（含内联标记母行）；头部导航 li 42 条曾误记母行，已由 `saw_a` 排除。
- doc_order 必须取 **li 开始序**（关闭序在嵌套簇下与页序错位 31 位起分歧，实证修正）。
- 别名链接显示文本 ≠ 正典题名（200 局势），必须入账 `href_text`。
- 实体策略：HTML4 命名实体优先＋十进制兜底；上游另有字面 UTF-8 与实体并存（preferences 行实证），列 `entity-encoding` 类。
- 残差 kind 最终四类：`trailing-space` / `inline-markup` / `no-close-li` / `entity-encoding`（组合枚举判定）。

### 1. 交付

| 项 | 结果 |
| ---- | ---- |
| parser 账升级 | `parse_catalog_full`：items 增 `doc_order`（li 开始序）、`has_children`；顶层增 `alias_rows`（653 行，含 `href_text`）、`cluster_mothers`（225→按 saw_a 过滤后账内 188＋内联 37 计 225 解析、实际入库 225 条含导航修正前的口径见 §2 事故）；旧接口 `parse_catalog` 行为不变（slug 序、aliases 并合） |
| fetch_catalog | `--reparse`（离线重建）、`--reparse-snap <名>`（跨时点）；`items` 保持 slug 序，`alias_rows`/`cluster_mothers` 按 doc_order 序 |
| rebuild_catalog | `--build`（骨架账＋残差池）、重放、`--check`（sha256）、`--build-account`（跨时点账）；纯层 `compute()`/`align_events()`/`rebuild()` |
| 装配等值 A2 | 最新快照 sha256 `205a4fec…f495` **全等**（池 194、骨架 954 行＋尾 77 行） |
| 跨时点 A3 | 20261027 快照 sha256 `9a230fc0…1631` **全等**（独立账＋独立骨架/池于 `results/`） |
| 池纪律 A4 | 194 ≤ 200；逐条过 A5 准入谓词（四类组合枚举），无谓词外残差 |
| 四向门 A5 | `check_catalog_network.py --gate`：G1 两时点全等／G2 en-SUMMARY 重放／G3 mu-lu 逐行全等（账存原样文字＋转义归一「文字跟随」子断言）／G4 unmapped=0、extra=0（挂起集 7 条冻结自 catalog-verdict）——全绿；已入 `check_all.py` GATES（键 `catalog-net`） |
| mu-lu 账 A6 | `baseline/mulu-map.json`：1881 行（全链接行，组行 0——mu-lu-s 无 `\*` 组行）、fixed 751＋尾 1；重放逐行全等 |
| 单测 | `test_rebuild_catalog.py` 9 项＋`test_common.TestCatalog` 新增 2 项，全绿 |

### 2. 事故与修正（归因登记，四元组）

1. **sweep 收编**：首笔 commit 未带 pathspec，卷走并行会话 166 件 specs/008 凭证 → `reset --soft` 退回、`restore --staged` 归还、pathspec 重提（2 files）。教训复验 [[sep-cn-parallel-session-hazards]] 既有纪律。
2. **doc_order 口径错**：初版取 li 关闭序，与页序在第 31 位分歧（africana-contemporary/africana）→ 改 starttag 计数，正典页序 1872 恒等。
3. **导航 li 误入母行账**：42 条页眉导航（Browse/What's New…）被记簇母行 → `saw_a` 谓词排除（含任意 `<a>` 的 slug-less li 不入账），UNMATCHED 42→5→0。
4. **标签尾连字符被剥**：`self- &mdash; see self-knowledge` 的 `self-` 被旧 `.rstrip("— -")` 削成 `self` → 改为只剥「前接空白的独立破折号」。
5. **门禁键名下划线**：`catalog_net` 违反 `key.replace('-','').isalnum()` 夹具 → 改 `catalog-net`（check_all＋spec 三处同步）。
6. **rules/05 触顶**：该文件 30690/30720 字节（余 30），本门禁登记行无处安放（加两行即 31885>30720）→ 按 ADR-0004 应拆 `rules/05/` 目录＋同步 rules/README 地图、layout.json、rules/01 职责表；本轮**回退 rules/05 改动**保绿线，拆分留作独立治理项（门禁功能已在 `check_all.py` 生效，工具职责在 `contracts/cli.md` 与各工具 docstring 载明）。

### 3. 作废条件复核（spec §7）

- 池 194 ≤ 200 ✓；无准入谓词外残差 ✓。
- 快照 sha 已登记 `results/pins.json`；快照未改 ✓。
- 若上游模板漂移（L1 骨架跨时点不再恒等）→ A2/A3 重验；本轮两时点骨架均 954 行且尾 77 行恒等。

### 4. 下一步（未开工）

- rules/05 拆分（ADR-0004）＋门禁登记行补录。
- 每轮 `fetch_catalog` 后重跑 `rebuild_catalog --build`（池随快照重冻）与 `--gate`；漂移时按 A5 停线归因。
- specs/001 `detect_updates.py`/`compare_versions.py` 仍为未实现契约（本 spec 非目标）。

## 2026-11-19 第二轮：rules/05 触顶处置＋门禁登记补录（用户批准）

`rules/05-ci-and-tools.md` 原 30690 字节（限 30720，余 30），任何新增行都超限 → 按 ADR-0004 拆为目录：

| 子文件 | 内容（原节搬家，正文逐字保留） |
| ---- | ---- |
| `rules/05/index.md` | 引言＋子文件索引＋新增门禁/工具的登记路线 |
| `rules/05/ci-workflows.md` | CI 工作流清单（含本轮新增 `check_catalog_network.py --gate`）＋运行时基线 |
| `rules/05/tools.md` | 本地工具表（**新增 `rebuild_catalog.py` / `check_catalog_network.py` 两行登记**）＋快速命令＋lint 配置＋表格风格 |
| `rules/05/site.md` | 站点运行 |
| `rules/05/batch-rewrite.md` | 生成器与批量改写纪律 |
| `rules/05/judgment-rights.md` | 判定权与规则所有权（**新增一行：目录↔上游目录账重放 → `check_catalog_network.py`**）＋升门四件套＋测量效度 |
| `rules/05/commit-policy.md` | 提交策略 |
| `rules/05/shell-discipline.md` | 本机 shell 工具纪律 |

链接改写：rules/02、03（内部相对引用）、04、06、08、09 的 `[05](05-ci-and-tools.md)` → `[05](05/index.md)`；`rules/README.md` 规则索引与两处快速判例；`AGENTS.md` 必读表；`.vitepress/README.md`；`.github/workflows/checks.yml` 注释。子文件内相对链接整体上移一级（`../0X-*.md`、`../adr/`、`../../.vitepress/`）。旧文件 `git rm`。

验收：`check_doc_size` 达标（rules/ 全部回到限内）、`check_layout` L1–L4 全绿、`check_catalog_network --gate` 四门绿、全量 `check_all` 见下。

## 2026-11-19 第三轮：CI 实红两处（均为本会话缺陷）＋修复

1. **漏件提交（已推缺陷）**：`check_catalog_network.py` 调用 `R.compute()`，但 `compute()` 重构未随 `05fb857d0` 入提交（pathspec 漏 `tools/rebuild_catalog.py`），本地绿因工作区有新版 → CI 该门 AttributeError。修：补提交 `fa1c25d5e`。教训：提交后须以 `git show HEAD:<file>` 对照工作区核实关键调用面，不能只信本地门禁绿。
2. **路径可移植性（真实二红）**：`baseline/catalog.json` 的 `source` 写 Windows 绝对路径，CI（Linux）上 `os.path.basename` 不切反斜杠 → G1 判“账与快照不同时点”。修：写账改相对路径（`en/_catalog/<名>`）＋比对端 `_basename_any` 双分隔符归一；旧账向后兼容。回归单测 `test_basename_any_cross_platform`。
3. 另：`rules/05` 拆分批次被并行会话 `git add -A` 型 sweep 收编进其提交 `8fc52eb0d`；内容经 `git show HEAD:rules/05/*` 核实完整（8 份子文件＋旧文件已删），不重复提交。

两处修复后：两时点 `--check` 仍 sha256 全等（`205a4fec…` / `9a230fc0…`）；`check_catalog_network --gate` 退出 0；单测全绿。

## 2026-11-19 第四轮：遗留 2/3 运营化 ＋ 每日三次 CI（用户批准“不计成本”）

### 遗留 1（直角引号）收口
`term_flow.build_row` 增加 `_quote_norm`（「」→“”、『』→‘’，rules/02 第 11 条），写册即归一；登记册现存 740 处一次性归弯，键集合 7044 行逐行核验零丢失（`script/tmp/archive-q/verify_sq.py`：非引号差异行 0、丢键 0）。`check_quotes` 全库 0 违例。单测 `test_term_flow_quotes` 5 项。

### 遗留 2（每轮 fetch 后 build/gate）→ 自动化
- `fetch_catalog.py --snapshot-only`：CI 只落快照不写 baseline（只读检出）。
- `catalog_drift.py --assembly`：本次快照产临时骨架/残差池 → B3.2 sha256 装配核验；残差超 A5 四类即“格式层漂移”，与目录漂移分栏报出。
- 本地既有节奏不变：`--build` → `--check` → `--gate`。

### 遗留 3（detect_updates 未实现）→ 实现（只检测，正文更新属其它步骤）
`tools/detect_updates.py`：new.html NEW/REVISED（90 天窗）＋可选 archinfo.cgi 版次核对 → 队列（new→retranslate／revised→update）。实测两点：①`/sep.xml` 已 404，`sources.feed=unavailable:404`（new.html 为唯一源）；②冻结后修订在 archinfo 上表现为 “is not yet archived”，新增 `pending_change_type` 解析，版次记 `pending-archive`（避免误判“无版次”）。

### CI：`.github/workflows/catalog-drift.yml`（每日三次）
cron `0 1,9,17 * * *`（北京 09:00／17:00／次日 01:00）；抓 contents.html → 四方漂移＋装配核验 → new.html/archinfo 变更检测 → 有漂移或待办即开/更新 issue（`sep-upstream-sync`，失败另标 `sep-sync-broken`）；只读只报告，不写账、不改 SUMMARY/mu-lu-s。旧 `sep-sync-check.yml`＋`.github/scripts/sep_sync_check.py`（周频、仅对 official-snapshot）删除，避免双 owner；rules/05/ci-workflows.md 工作流表与网络抓取例外口径同步。

### 首跑实测（2026-11-19，本地同款链路）
- 上游快照 1873 条（账 1872）：新增 `inquiry`、`privacy-health`；`privacy-medicine` 消失（转别名）；`history` 改名（→ history and historiography, philosophy of）＋作者换；`argument`／`gadamer`／`hedonism`／`special-obligations` 作者增补。
- 装配核验：sha256 `39bbc60b…` **全等**，残差 194 条（仍全部落在 A5 四类）→ 模板/格式层零漂移。
- 覆盖：`inquiry`、`privacy-health` 在 SUMMARY 与 mu-lu-s 均缺；`privacy-medicine` 为待裁撤。
- 变更检测：90 天窗 91 条待办（NEW 14／REVISED 77）。
- 存量补录：`bioethics-moral-reasoning` 补入 mu-lu-s 应用伦理学节，`mulu-map` 重建（1882 行），G3/G4 复绿。

### 观察项（未处置，留待接续）
- 上游新增/改名/裁撤（inquiry、privacy-health、privacy-medicine、history）属 intake 落地，按“正文更新由其他步骤做”不在此轮处理；CI 首次运行会以 issue 形式挂出。
- `check_catalog_network` G1 取 `en/_catalog` 最新快照与 baseline 比时点；每轮正式 `fetch_catalog` 落地后需重跑 `--reparse`＋`--build`（CI 巡检抓的快照在 runner 上用完即弃，不入库）。

## 2026-11-19 第五轮：issue #47 结案（目录与条目落地，用户指示）

### 目录（catalog 层）
`fetch_catalog` 落快照 `20261119T041214Z`（1873 条）；`summary_sync report` → ADD 2／REMOVE 1：
- `privacy-medicine → privacy-health` 走 `apply-rename`（文件改名、全库链接改写；侧写误改 `specs/016` 历史预览件已还原），SUMMARY/mu-lu-s 标题改「健康照护与研究中的隐私 Privacy in Health Care and Research (Leslie Francis)」；
- `inquiry` 走 `apply-add --title-zh 探究`（H1 桩＋字母节插入＋baseline zh_doc＋yuanwen 转换）；
- `history` 改名（历史与史学史哲学 Philosophy of History and Historiography）＋作者换（Kuukkanen）；`argument`／`gadamer`／`hedonism`／`special-obligations` 作者增补，SUMMARY＋mu-lu-s 双向同步，`check_summary --sync-headers` 同步 6 处 H1；
- 复跑 `report`：add 0／remove 0／mapped 1873（与上游对齐）。

### 条目（en/ 与 yuanwen/）
按 89 条变更队列批量 `fetch_entry`（5 批、0 失败），实变 11 件：argument／berlin／emily-elizabeth-constance-jones／gadamer／hedonism／history／horkheimer／incompatibilism-theories／special-obligations＋新件 inquiry／privacy-health；`yuanwen.py` 重转对应镜像。旧 slug 包 `en/privacy-medicine/`、`yuanwen/p/privacy-medicine.md` 清除（上游换发，git 历史保留）。

### 任务（状态机）
- `gadamer`、`incompatibilism-theories`（原 s2.4_termchecked，译文均为 H1 桩）按 **ADR-0051 R3** `reopen --upstream-sync --clear`（reason 引快照 diff＋issue #47）→ cleared；
- `inquiry`、`privacy-health` `create --kind retranslate`（pending，version_pin＝Nov 17, 2026）。

### 验收
`check_all` 17 项中 16 绿；唯一红＝图片引用完整性，命中 `specs/008-terminology-campaign/results/audit-2026-11-19.md` 内嵌 `termonline` 数据带来的 `<img src='/root/syzx/...'>`（并行会话的生成报告，非本线产物，见其 term_audit 生成器需 sanitize）；目录四方门 G1–G4 全绿，装配 sha 全等（池 194）。

### 结案附带的三处工具缺口（本轮一并修）
1. **fetch_entry 假阴性**：索引 sha 相同即早退，脚注/补充材料/资产的上游改动不可见。改为全文件钉比对（`ledger_files`），`save()` 内容不同即写；仅当 files[] 全钉一致才报 unchanged。
2. **detect_updates 队列虚高**：90 天窗按日期列，已同步条目日日重报。加 `filter_synced`（`fetched_at` ≥ 事件日即剔）＋ `--verify-web`（抓 index.html 与钉比 sha，剔除「列表说改、实际逐字节一致」假阳性——emotion-Christian-tradition 实证）。
3. **check_images 假阳性**：`/root/...` 站点绝对路径被判悬空（源自抄录的上游 HTML）。单列 `absolute` 告警类，不计硬门；补单测。

结案后复跑：队列 0（synced_skipped 88、verified_same 1）；`check_all` 17 项全绿。

## 2026-11-22 巡检 issue 口径：只报目录漂移，目录干净即关闭（用户裁定）

- 起因：用户质疑 issue #52 在“目录无漂移”时仍发布。定位：旧触发条件是「目录漂移 或 正文队列非空」；#52 由 `culture-cogsci` 的 `new.html` 修订（2026-11-21）触发，其后 `delusion` 亦入队。16:40 班与 08:07 班队列同容仍追加评论——issue 是常驻追踪器、每班追加运行日志，且无指纹去重；本地未落地则 `baseline/entries.json` 不前移，队列逐班复现。
- 裁定落地（`catalog-drift.yml`）：
  1. issue 开关只看目录漂移——`changed == 'true'` 开/更新；`changed == 'false'` 显式成立时关闭打开中的 `sep-upstream-sync` issue（关闭附一行原因评论）。
  2. 正文变更检测保留（顺序门不变：仅目录干净时执行），但结果只落运行工件；issue 不再报告“上游变更待办 N 条”，队列也不参与 issue 开关。
  3. `sep-sync-broken` 不随目录干净自动关闭，留人工定性。
- 同步更新 `rules/05/ci-workflows.md` 工作流表。当前无打开中的同步 issue；关闭路径待下一个目录干净班次实测。

## 2026-11-22 官方基线快照同步与 G5 增补（用户指令“同步几方目录互转”）

- **现状核查**：四方门 G1–G4 全绿；`catalog_drift --latest` 报 `changed=false`（新增/删除/改名/作者/别名全 0，SUMMARY 与 mu-lu-s 差集 0）；`summary_sync report` add 0／remove 0／mapped 1873；`gen_en_summary --check` 最新。唯一失配方是 `rebuild_dir check` 依赖的 `.github/sep-baseline/official-snapshot.json`——该文件自 2026-11-15 后无生成器/门禁，停留在 11-14 快照，仍含上游已撤下的 `privacy-medicine`，故误报“缺 yuanwen 镜像 1 件”。
- **新增工具**：`tools/sync_official_snapshot.py`（`--check` 比对／`--write` 写回；解析规则沿用旧周检脚本，main/alias 与历史基线同构；护栏 main≥1800、alias≥600）。写回 `20261122T021217Z`：main 1872→1873（+`inquiry`、+`privacy-health`、−`privacy-medicine`）、alias 653（+`in health care and research`、−`and medicine`）、`history` 标题改为 “history and historiography, philosophy of”、6 处作者增补（argument／embodied-cognition／gadamer／hedonism／special-obligations 等）。
- **G5 增补**：`check_catalog_network.py` 由四子门扩为五子门，G5 断言 official-snapshot ≡ 最新 contents.html 解析 ≡ catalog 账（sku 集、title/authors、alias 文本集）。负向探针（改 `abduction` 一条 title）实测转红，`--write` 复原转绿。
- **依据**：这是“派生物无生成器/门禁”族缺口的第二次（首次为 `yuanwen/SUMMARY.md` 镜像 stale，2026-11-22 已登记），按 ADR-0039 升级防线而非只修数据。
- **复核**：`rebuild_dir check` 0 缺镜像／1873；五子门全绿；`check_all` 17 项全绿。
