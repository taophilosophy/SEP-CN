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
