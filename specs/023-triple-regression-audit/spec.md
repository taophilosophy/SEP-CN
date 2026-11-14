# 023 三向回归审校战役（en ↔ yuanwen ↔ 译文，逐行人审）

> **[销案 2026-11-14]** 本任务书已并入 **specs/028-s25-termchecked-rollout**（ADR-0043），未执行项由其承接；本文件留作凭证与输入清单，不再作为执行依据。（战役并入 specs/028：非 A1 done 存量按增项补课口径执行，台账沿用；185 回退件的 r 链全重走吸收其三向审计。ADR-0043。）


状态：进行中 | 立卡：2026-11-14 | 发起：用户指令“对已经完整翻译的条目（指所有段落均译出，无论是哪个阶段），依次回归 en、yuanwen 对应的条目，逐行审阅其内容、格式。不计成本代价。同时修订 tools/yuanwen.py，避免回归，特批准修复三者。”

## 方向声明（rules/08）

**目标**：对“所有段落均已译出”的词条（tasks 状态 drafted 及其后，含 done；现查约 422 条），逐条依次回归 `en/<slug>/` 与 `yuanwen/<letter>/<slug>.md`，**逐行人工审阅**三条轴：

1. **译文轴（zh）**：内容保真（回 en 零信任核对）＋ 格式（rules/02/03/07、脚注标记、书目、结构对账）。
2. **镜像轴（en↔yuanwen）**：转换保真逐段人审（specs/018 协议原样沿用；018 已核 a 字母 10 条的镜像轴台账**沿用不重做**）。
3. **转换器轴**：审出的系统性转换缺陷修进 `tools/yuanwen.py` + 单测锁定 + 全量重转，避免回归（specs/018 spec A4 裁定延续）。

**非目标**：

* 不整条重译（重译走 005 状态机）；不做语体复核（specs/015）与术语查证（specs/008）。
* 未译段落不审（不在范围的词条整体不动）。
* 不重抓上游：en/ 为快照，勘误仅限 ADR-0038 四类且逐条登记 `specs/001-sep-sync-pipeline/results/en-errata.md`。

**验收判据**：

1. 每词条一行双轴台账（`execution-log/index.md` 字母级覆盖表 + `execution-log/ledger-<letter>.md` 逐词条行），可接力、无跳条。
2. 发现项逐处定性（禁止机械批量替换，015 教训）；修复分三层落位并留痕。
3. 转换器改动后全量重转，归一化回归扫描（018 `bin/regression_scan.py`）非预期差异 OTHER=0 才收口；基线随重转重钉并记录新旧钉。
4. 处置后定点 `check_academic.py --docs <路径> --strict`、`check_math_zh.py`；收工 `check_all.py` 全绿。

## 用户裁定（2026-11-14，AskUserQuestion 四答）

* **A1**：“特批准修复三者”= **en、yuanwen、中文译文三层皆可修**。en 限 ADR-0038 四类并登记 errata；yuanwen 系统性缺陷只走转换器修正＋全量重转，不手改产物；译文走证据链修复（qa-rework 凭证步，禁经 clear）。
* **A2**：范围口径 = drafted 及其后（≈422 条）；**cleared（待重译）旧译文不入列**——校了也会被重译覆盖。无译文 1450 条不入列。
* **A3**：战役组织 = **新立本 spec（023）统一战役**；specs/018、specs/022 冻结并在其 spec 注明移交；018 已核 10 条镜像轴台账沿用。
* **A4**：**先修再审**——specs/020 已登记的镜像缺陷（嵌套表降级 16 件 128 处、整表丢失 8 件、findlay 缩写表断尾、图片未引用 13 件、mereology 单表拆散）先修进转换器＋单测，全量重转、重钉基线，然后才开始逐条审校，避免已校词条被重转打回。

## 背景与依据

* specs/018（en↔yuanwen 逐段人审）已修转换器 7 类缺陷并全量重转（见其 spec A4 与 execution-log）；剩余 412 条镜像轴审计移交本战役。
* specs/022（zh↔yuanwen@b20ab51b8 偿还校对）已建只读扫描器 `bin/scan_zh_vs_yuanwen.py` 并跑完全库 triage（`results/scan-latest.jsonl`，1879 行）；其人工判读尚未开条。本战役接手：机检只作拦截网与回归防线，**每条全文逐行人审是裁判**（018 先例：禁止编程比对替代人审）。
* specs/020 镜像缺陷清单：`specs/020-table-image-audit/results/mirror-defects.md`（移交 018 转换器战役，现随 A4 移交本战役 Phase 1）。
* ADR-0038：en 就地改正限四类；转换器引称匹配式已修（逗号式容许），`cite_markers=0` 不等于缺陷。
* ADR-0028 定岗：本机（M1）遇管线/工具问题不自行修复，**除非用户当场指示**——本战役即用户当场指示，获授权修 `tools/yuanwen.py` 与本 spec。

## 方法

### Phase 1：转换器先修（A4，先于一切审校）

1. 逐件复现 020 清单缺陷于最小样例；修 `tools/yuanwen.py`（嵌套表真结构化、整表丢失根因、findlay 断尾、`<img>` 保留、mereology 拆表），每类配单测入 `tools/tests/`。
2. 备份 `yuanwen/` → `--all-baselined` 全量重转 → 归一化回归扫描 OTHER=0（018 法）；重钉基线并在此登记新旧钉值。
3. `script/t020_cmp.py` / `t020_img.py` 复核受影响词条；020 清单逐件销账。

### Phase 2：逐条三向审校（字母序，A2 范围）

每词条协议（接力-friendly）：

1. `python -I tools/task_ops.py show <slug>` 定位任务态；Read `en/<slug>/index.html`（`<h1>` 至页脚）与 notes.html（若有）。
2. Read `yuanwen/<letter>/<slug>.md` 全文——镜像轴逐段走查（018 协议：完整性①、格式一致性②、无凭空多出③；书目逐条计数比对）。
3. Read `<letter>/<slug>.md` 译文全文——译文轴逐行走查：内容回 en 核对、格式按 rules/02/03/07、标记/defs/节数对账（022 扫描器 flags 作拦截网辅助，不作裁判）。
4. 发现项定性 → 修复按 A1 三层落位：en（ADR-0038 四类＋errata 登记）、yuanwen（系统性→转换器＋重转；孤立性→登记待重转）、译文（证据链）。
5. 台账双轴一行入 `ledger-<letter>.md`；接力指针写在台账末尾注释行；进度数字只进 index 覆盖表。

## Assumptions（追加裁定登记处）

* A5 [2026-11-14]：018 已核 10 条（abduction…academic-freedom 之前的 a 批）镜像轴结论沿用；其译文轴在本战役照常审。
* A6 [2026-11-14]：基线钉初始值为 b20ab51b8（承 022）；Phase 1 重转后由本 spec 记录新钉。
* A7 [2026-11-14]：别名词条（— see）与占位母词条不建审校行；digit 词条 `1/18thGerman-preKant`（done）入列不按字母桶汇总。
* A8 [2026-11-14]：用户裁定将本战役协议固化为状态机“审计已译”环节（`audited`，二校后独立环节）——本战役即“已完成条目回炉”的执行载体（ADR-0040）；范围口径 A2 不变，每条目作业＝审计已译环节＋一次独立校对（独立于初译 actor，ADR-0020），语体增项（破折号、“一个”、AI 腔，rules/02）并入逐条审阅；修复三层落位 A1 不变。
