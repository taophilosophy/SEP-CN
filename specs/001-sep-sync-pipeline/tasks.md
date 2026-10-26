---

description: "Task list for SEP 同步管线 feature"
---

# Tasks: SEP 同步管线（抓取 · 更新 · 比较 · 翻译）

**Input**: Design documents from `/specs/001-sep-sync-pipeline/`

**Prerequisites**: plan.md（必需）、spec.md（必需）、research.md、data-model.md、contracts/cli.md、quickstart.md 均已就位

**Tests**: spec 的 SC-001…005 要求金样本验证，故保留测试任务（stdlib unittest，fixtures 复用抽样）。

**Organization**: 按用户故事分组；翻译战役（US4）以"每文档标准作业程序（SOP）"为最小单元，逐文档状态记入 `tasks/<首字母>/<slug>.json`。

## Format: `[ID] [P?] [Story] Description`

- **[P]**: 可并行（不同文件、无未完成依赖）
- **[Story]**: 所属用户故事（US1…US5）
- 所有路径以仓库根为基准

## 每文档标准作业程序（SOP）——US4 战役的最小执行单元

> 本节是"翻译任务细化到每个文档"的落地定义。**每个中文文档**（对应一个词条正文页）一律按下表执行；每步完成即在 `tasks/<首字母>/<slug>.json` 记 `{step, status, actor, at, evidence}`，禁止跳步（由 task_ops.py 强制）。两类任务共用此表：

**retranslate（清空重译，战役主体）**

| 步 | 名称 | 内容（可判定完成标准） |
| -- | ---- | ---------------------- |
| 0 | gate | `baseline_audit.py <slug>` 哈希复算全通过；任务记录已建（kind=retranslate，版本钉=pubinfo 日期+存档版名+index.html 哈希） |
| 1 | clear | `task_ops.py clear`：正文清空仅留 H1（H1 文字与 SUMMARY.md 一致）；git 工作区仅此文件变动 |
| 2 | draft | 以 `en/<slug>.txt` 为唯一底稿初译；新术语先登记 yi-zhe-shuo-ming.md 再使用；图片下载至 `.gitbook/assets/` 并逐字符一致引用；脚注并入文末 |
| 3 | s1 一校（准确性） | 对照英文源逐句：漏译/错译/事实/数字/人名/版本号逐条核销，留存对照记录为 evidence |
| 4 | s2 二校（语言） | 清除欧化句、被动滥用、口吻失真；全篇通读 |
| 5 | s3 三校（体例） | `check_style.py` 0 issue；markdownlint 0 error；图片引用存在且本地化 |
| 6 | r1 初审 | 对照原文自审并签字（evidence=复审对照记录） |
| 7 | r2 复审 | 第二遍逐句回核原文与逻辑一致性 |
| 8 | r3 终审 | CI 全绿（markdownlint/links/check-images）+ 版本钉核对 + 全文抽查 ≥20% |
| 9 | done | 单文档一次提交：`重译 <中文标题> (<slug>)`；任务 JSON 同批提交 |

**update（上游更新同步，常态）**：gate（读 `baseline/changes/<slug>-*.json`）→ s1 **仅变更段落**（不复查旧错）→ s2 变更段所在节 → s3 全文档 → r1 变更段 → r2 全文档回核 → r3 全文档 CI+钉 → 提交 `同步 <slug> 上游 <日期> 变更`。

---

## Phase 1: Setup

- [x] T001 建 `tools/`、`tools/tests/`、`en/`、`en/_catalog/`、`baseline/`、`baseline/changes/`、`tasks/` 目录骨架，并写 `tools/__init__.py`
- [x] T002 [P] 建 `en/.gitkeep` 确认 `.gitignore` 现行规则已覆盖 `en/`、`/script`（只核对不修改——AGENTS.md/.gitignore 归其他会话）
- [x] T003 [P] 写 `tools/common.py`：UTF-8 无 BOM 读写、LF 规范化、仓库根定位、写后读回自校验的 `write_json_verified()`（防假成功写入，见 plan.md 环境补充约束）
- [x] T004 [P] 写 `tools/fetch.py`：urllib 封装——UA 标识、相邻请求 ≥5 秒（宪法 V）、429/5xx/超时指数退避重试 ≤3 次、每次请求记录 `{url, status, bytes, sha256, at}` 日志至 `script/http-log.jsonl`（演示轮 1 修订：原命名 `http.py` 遮蔽标准库 `http` 包，已改名）
- [x] T005 [P] 从抽样复制 9 个金样本到 `tools/tests/fixtures/`（set-theory/logic-classical/bayes-theorem/bell-theorem/ibn-sina/consciousness/quine/aristotle-logic/arch-anaxagoras + archinfo 输出）

## Phase 2: Foundational（阻塞所有用户故事）

- [x] T006 写 `tools/parser.py`：按 spec"网站结构事实基础"标记契约解析词条 HTML——`<!-- BEGIN/END ARTICLE HTML -->` 边界、`pubinfo`、`h2/h3/h4+锚`、`div#toc`、`div.figure`+`figlabel`、`blockquote>table`、`sup>a[href^=notes.html]`、citation_author 元数据；输出块序列
- [x] T007 [P] unittest：`tools/tests/test_common.py`——set-theory 解析出 `basic-set-theory.html` 引用、bayes-theorem 解析出 notes 引用 ≥16、bell-theorem 图 figlabel 归并、anaxagoras pubinfo=2007-08-22/2026-08-09、logic-classical 行内公式 `\(...\)` 计数 >1000、archinfo 解析 Fall 2026 + Winter 2019 历史
- [x] T008 [P] unittest：`tools/tests/test_common.py`——write_json_verified 往返一致；UTF-8/LF 断言
- [x] T009 实现 `tools/extract_text.py`（契约见 contracts/cli.md）：HTML→带节号块序列文本，输出 `en/<slug>.txt`；同输入必得同输出（哈希可复算）
- [x] T010 [P] unittest：`tools/tests/test_common.py`——同一 fixture 跑两遍输出逐字节一致；实体解码（`&mdash;`→—）与数学定界符原样保留断言
- [x] T011 全部 unittest 通过：`python -m unittest discover -s tools/tests -t .`，0 failures（实测 26 例全绿）

**Checkpoint**: 基础设施就绪，可并行开工 US1/US2/US3 的独立部分

## Phase 3: User Story 1 — 词条快照基线 (Priority: P1) 🎯 MVP

**Goal**: 任意词条抓成完整词条包并形成可审计基线
**Independent Test**: quickstart 场景 1——5 样本抓取成功率 100%，缺省件显式登记，哈希复算通过

- [x] T012 [US1] 实现 `tools/fetch_entry.py`（契约见 contracts/cli.md）：正文+notes+补充材料+图片递归抓取、404 记 missing 缺省件、pubinfo 提取、archinfo 核对、登记 `baseline/entries.json`（data-model Snapshot 字段，slug 主键）
- [x] T013 [US1] 实现 `tools/fetch_catalog.py`：抓 contents.html 存 `en/_catalog/<时间戳>-contents.html`，解析全量清单（slug/标题/作者/alias_of/level），与上次快照 diff 输出 added/removed/renamed/alias_changed
- [x] T014 [US1] 实现 `tools/baseline_audit.py`：登记物逐件复算 SHA-256 + 存在性核对 + 缺省件核对；提供 `gate_passes(slug)` 供 clear 使用
- [x] T015 [US1] 抓取 5 样本词条（set-theory logic-classical bayes-theorem bell-theorem quine），stdout JSON 存 `script/tmp/demo-us1.json` 作凭证
- [x] T016 [US1] 运行 `baseline_audit.py` 全通过；提交基线（"建立词条基线：首批 5 样本"）与流程文档（"SEP 同步管线规格与产物"）——分开提交

- [x] T047 [P] [US1] 实现 `tools/yuanwen.py`：en/ 原始 HTML → yuanwen/<字母>/<slug>.md 确定性转换（块切分保原始片段、行内 HTML→Markdown、数学与 sub/sup 占位保护、TOC 跳过、图片相对引用 ../../en/、notes.html→[^note-n] 脚注、补充材料→<slug>.<x>.md 互链、yuanwen/SUMMARY.md 镜像、登记入 baseline）（演示轮 2，用户 2026-10-27 裁定）
- [x] [US1] T048 [US1] 引用注释转换：文献条目→[^key] 脚注定义（首作者姓-年份键，缩写首字母过滤、— see 排除、continuation 条目继承前条作者），文内引用组追加标记（演示轮 2 修订：token 正则须带尾点过滤，否则 KRS 类 acronym 被污染）
- [x] T049 [US1] zh_doc 三级匹配器入 common.find_zh_doc（路径后缀→首字母目录整路径子串+别名排除→英文标题全词+路径含最长词优先），fetch_entry 抓取即登记、task_ops/yuanwen 统一接入

**Checkpoint**: SC-001 达成——US1 独立可用

## Phase 4: User Story 5 — 演示轮 1 与流程纠偏 (Priority: P1)

**Goal**: 真实词条完整跑通一轮，暴露问题修订流程文档
**Independent Test**: 演示日志 + 四件产物修订记录可查

- [x] T017 [US5] 选一个小型真实词条，执行 SOP 步 0–3（gate/clear/draft 初译/s1 一校），全过命令与输出记 `script/tmp/demo-log.md`
- [x] T018 [US5] 演示中暴露的每个问题：或修订 specs/001-sep-sync-pipeline 四件（注明"演示轮 1 修订"），或记入"维持原设计"理由——逐条落档
- [x] T019 [US5] 向用户汇报演示结果与修订清单，确认是否进入下一循环（由本轮收尾报告履行）

**Checkpoint**: 流程经实跑验证一次（循环起点，后续按用户指令循环）

## Phase 5: User Story 2 — 上游更新检测 (Priority: P2)

**Goal**: 三源检测上游变化产出待处理清单
**Independent Test**: quickstart 场景 2——RSS 命中 2026-10 已知事件；archinfo 与基线差异报告正确

- [ ] T020 [US2] 实现 `tools/detect_updates.py` 的 RSS/new.html 解析（条目：slug/event/date/changes_to），输出 from_rss
- [ ] T021 [US2] 实现 archinfo 全量/子集核对（--only），对比 baseline 的 archive_edition，输出 from_archinfo 与合并 queue 写 `baseline/queue.json`
- [ ] T022 [US2] 验证：RSS 命中 kant-transcendental（2026-10-24 revised）与 academic-freedom（2026-10-17 new）；对 5 样本跑 archinfo 核对 0 误报
- [ ] T023 [US2] 提交（"管线：更新检测三源合并"）

**Checkpoint**: SC-002 达成

## Phase 6: User Story 3 — 英文版本比较 (Priority: P2)

**Goal**: 两快照段落级 diff 并映射中文文档
**Independent Test**: quickstart 场景 3——anaxagoras 存档旧版 vs 在线新版变更清单节号/摘录正确

- [ ] T024 [US3] 实现 `tools/compare_versions.py`：块切分+`difflib.SequenceMatcher` 对齐，输出 add/remove/replace/move 四类，每条含 section/excerpt_en
- [ ] T025 [US3] 实现 zh_doc 映射：基线 `zh_doc`（来自 SUMMARY.md）+ 无对应者标"待建任务"；变更清单写 `baseline/changes/<slug>-<日期>.json`
- [ ] T026 [US3] 验证：anaxagoras `--old archives/winter2019 --new live` 清单人工抽查 ≥10 条无误
- [ ] T027 [US3] 提交（"管线：版本比较与映射"）

**Checkpoint**: SC-003 达成

## Phase 7: User Story 4 — 每文档翻译任务与三审三校 (Priority: P3)

**Goal**: 六道状态机工具化 + 战役按字母批组织 + 一个文档完整走通 SOP
**Independent Test**: quickstart 场景 4——状态机拒跳步；场景 5 体例检查可判定

- [ ] T028 [US4] 实现 `tools/task_ops.py`（契约见 contracts/cli.md）：create/show/advance/clear/block；retranslate 与 update 两状态机（data-model 状态图），advance 校验前置步骤完成，evidence 必填；clear 的 gate 复用 baseline_audit.gate_passes
- [ ] T029 [US4] 实现 `tools/check_style.py` 六规则（curly-quotes/bold-spacing/cjk-spacing/no-html/no-text-fence/no-asciiart），代码块与行内代码豁免，英文词内撇号豁免
- [ ] T030 [P] [US4] unittest：`tools/tests/test_task_ops.py`——跳步被拒、update 类 s1 必须以 changes: 前缀引用变更清单、clear 的 gate 未过时拒绝、block/unblock 冻结语义
- [ ] T031 [P] [US4] unittest：`tools/tests/test_check_style.py`——各规则正反例（弯引号成对/方向、词内撇号豁免、加粗两侧空格、中西文空格、HTML 残留、text 围栏、xref 残留、代码块豁免）
- [ ] T032 [US4] **示范文档**：选 1 个小型词条按 SOP 步 0–9 完整走通六道并提交；任务 JSON 全程留痕——此即"每个文档怎么干"的标准样例
- [ ] T033 [US4] 战役批组织：`tasks/<字母>/` 按首字母建批（a…z 共 26 批），每批一个战役任务行（见下"翻译战役批任务"），批内逐文档走 SOP；批完成提交并跑 `script/audit.py` 结构核对
- [ ] T034 [US4] 提交（"管线：文档任务状态机与体例检查"）

### 翻译战役批任务（US4 展开——执行期逐批勾选）

> 每批 = 该字母下全部正文词条逐文档走完 SOP；别名词条（— see 型）只登记映射不建任务。批内顺序按词条长度升序（先短后长，快速积累完成样本）。**注**：并行会话已在执行"词条 H1 去除反斜杠转义"的批量清空（commit d4cf142b），本战役的 clear 步骤对其结果做幂等校验即可，无需重复清空。

- [ ] T035 [US4] 批 a–c：逐文档 SOP（数量见 baseline/entries.json 实测）
- [ ] T036 [US4] 批 d–f：逐文档 SOP
- [ ] T037 [US4] 批 g–i：逐文档 SOP
- [ ] T038 [US4] 批 j–l：逐文档 SOP
- [ ] T039 [US4] 批 m–o：逐文档 SOP
- [ ] T040 [US4] 批 p–r：逐文档 SOP
- [ ] T041 [US4] 批 s–u：逐文档 SOP
- [ ] T042 [US4] 批 v–z：逐文档 SOP

**Checkpoint**: SC-004 达成；战役批为长期执行项，按批推进按批验收

## Phase 8: Polish & Cross-Cutting

- [ ] T043 quickstart.md 五场景全量复跑一次留档（`script/tmp/demo-final.json`）
- [ ] T044 [P] `tools/README.md`：一页速查（契约指向 contracts/cli.md，不重复）
- [ ] T045 CI 共存性核对：push 后观察 sync-headers/markdownlint/links/check-images 是否全绿，异常记录并修订
- [ ] T046 宪法符合性终检：FR-001…018 逐条对照 checklist.md 结论归档

---

## Dependencies & Execution Order

### Phase Dependencies
- Setup(1) → Foundational(2) → US1(3) → US5 演示(4) → US2(5)/US3(6)（可并行）→ US4(7) → Polish(8)
- US2/US3 与 US5 演示轮无相互阻塞，但演示轮的纠偏结论可能修订它们的验收细节——建议先演示后并行

### 关键依赖
- T012 依赖 T006/T009（解析与提取）；T028 依赖 T014（clear 的 gate 调 baseline_audit）；T032 依赖 T028/T029 + US1 基线；T035–T042 依赖 T032（SOP 样例确立）与 US3（update 类输入）
- 战役批 T035–T042 内部无依赖，可多会话并行（每会话认领不同字母批，任务 JSON 文件不冲突）

## Parallel Example

```text
# Foundational 后可并行：
会话 A: T012 fetch_entry → T015/T016（US1 主线）
会话 B: T020 detect_updates RSS 部分（US2）
会话 C: T024 compare_versions 核心对齐（US3）

# 战役期并行（按字母批认领）：
会话 A: 批 a–c   会话 B: 批 d–f   会话 C: 批 g–i ……
```

## Implementation Strategy

- **MVP = US1（基线）+ US5（演示一轮）**：T001–T019 完成即可向用户证明管线可行并进入纠偏循环
- 战役批（T035–T042）是长期执行层：每批完成即交付一批成品文档，不必等全库
- 每任务完成即提交（宪法 IV）；SOP 步 9 的单文档提交是战役期的常态节奏
- 禁止：跳过 gate 清空正文、跳步推进状态机、以既有译文为底稿、批量改动词替换

## Notes

- [P] = 不同文件、无未完成依赖
- [Story] 对应 spec.md 用户故事
- 每步完成勾选并在提交信息注明任务号；遇阻塞记 blockers 转 blocked 状态，不得静默绕过
- 产物写盘后立即 git add（D11 防丢失纪律）
