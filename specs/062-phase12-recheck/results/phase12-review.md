# 阶段 1.2 独立复核（2026-11-25）

对象：阶段 1.2 收口提交（339c09dcf、2b369808f、23935892e）及其产物 `phase12-run.json`、`phase12-report.md`、`phase12-analysis.md`、`en-delta.json`、`b32-new-gap.md`。

方式：只读复算（不采信自报数字）＋定点门禁复跑；命令与结果如下。ADR-0039“自报完成须独立复算”。

## 一、逐项复算

| 项 | 报告值 | 独立复算 | 判定 |
| --- | --- | --- | --- |
| 抓取 | 1873／1873，失败 0 | `entries-before.json` 与 `baseline/entries.json` 各 1873 条，slug 集零差 | 一致 |
| 账变化 | 522（unchanged 1351） | 记录级差集 522 条：含 `local.js` 补登 430（仅补登 423、仅正文变化 92、兼有 7） | 一致 |
| 磁盘变化 | 126 文件／100 词条 | `en-delta.json` rows 126／slugs 100；账侧非 js 实变路径 122 html＋1 png＋2 svg，另 1 件 `local.js` | 一致（口径见 R-2） |
| 变化分类 | text 65／layout 42／rename-wave 17／binary 1／asset 1 | `en-delta.json` kinds 同值，合计 126 | 一致 |
| 建账清单 | 65 件 | 与 `kind=text` 集合 65 行同集，覆盖 54 词条 | 一致 |
| 正式修订件 | 10 件全在建账清单 | 逐名核对 10／10 在册 | 一致 |
| 元数据 | 29 件变化，10 件 `substantive_revision` | `entry-meta-delta.md` 29 行；10 件同上 | 一致 |
| 补丁 | 3 条有效，mismatch／admission／index／git_check／public 全 0 | 复跑 `check_en_patches.py --strict` 同值，exit 0 | 一致 |
| I2 | 1873 件，issue 0 | 复跑 `check_yuanwen_fidelity.py --gate`：checked 1873、issue_total 0 | 一致 |
| B3.1 | 1663／210，与旧基线集合零差 | 对比 1f23585f6：ok 集合对称差 0 | 一致 |
| B3.2 | 1851／22／0 → 1811／62／0；新增 gap 40、修复 0 | 复算 40／0；40 名与 `b32-new-gap.md` 同集；40 件全在本轮 100 词条变更集内 | 一致 |
| 池占比 | 118 MB，50.12% | 112.8 MiB／225.1 MiB＝50.12%（十进制 117.6 MB） | 一致 |
| yuanwen | 2421 | `yuanwen/**/*.md`＝2421 | 一致 |
| 门禁 | 应全绿 | 复跑 `check_all.py` 全绿（HEAD 为 19 项；复跑时工作区另含在途的 `en-patches` 门，共 20 项，失败 0） | 一致 |
| 旧池 judge | 1780／48／45 | 无落盘凭证；算术 1780＋48＋45＝1873 自洽 | 不可复算（R-5） |

## 二、复核发现与处置

### R-1 文档数字错（已改）

`spec.md` §5 两处写 `text 66`，实际 65；分类串漏 `asset 1`。原因：分类在 asset 类落地（voting-methods/local.js）前定稿。已改为 65／42／17／1／1（合计 126）与“65 件出建账清单”。

### R-2 图钉丢失（已修）

`logic-deontic` 重钉后，`files[]` 中 3 个旧图（`fig-box-b.svg`、`fig-square-b.svg`、`fig-vbox-a.svg`）被摘除，盘面文件仍在（en/ 冻结，ADR-0062）。后果：`en_integrity.py` 判为游离件（硬发现），而修复前 `en_integrity --all` 硬发现 4 项中 1 项即由此产生。

根因：`tools/fetch_entry.py:upsert_baseline` 以新抓包整体替换 `files[]`；上游新版不再引用的旧资产随之失登记。当日新增的护栏只拦“无 `files` 的记录”，不拦“`files` 变少”。

处置：按 `en_integrity` 既定的 `registered_orphans`（版本更替残件，非硬发现）口径恢复 3 条登记，sha 与原钉一致（`divergence verify` 复跑 4845/4845 pristine）。复检：`en_integrity logic-deontic` clean＝1、硬发现 0；全库硬发现由 4 降为 3（余 3 项均既存，见第三节）。

建议（未实施）：`upsert_baseline` 改为并集保留——旧有而新抓包无者保留原记录（标记残件），避免每次上游修订都摘钉；`check_all.py` 增 `en_integrity` 门（HEAD 的 19 项门禁清单不含它，故门禁全绿掩盖了该硬发现）。

### R-3 SVG 分类盲区（待裁）

`logic-deontic` 的 `fig-square-c.svg`、`fig-three-c.svg` 被上游重导出：画布 206.33×179.51pt → 216.28×175.15pt、357.27×87pt → 367.22×83.91pt，图元引用 26→30、42→47。`en_delta.py` 判 `layout`（“可见文本逐字等值”），未入建账。

成因：SVG 以 path 承载字形、无 text 节点，“可见文本”判据在 SVG 上恒为空，图形变化被一律吞作 layout。建议对 `.svg` 单列 `asset-visual` 类并人工过目；本次两图正文未变，不需重译，但应登记。

### R-4 上游新错链（待处置）

`aristotle-psychology/notes.html`（本轮 text 类，109 增删行）第 143 行：

```html
<a href="index..html#ref-1">1.</a>
```

双点错链，旧版（23935892e~1）无此串，系 2026-11-23 修订新引入；正确读法应为 `index.html#ref-1`（脚注回链）。全库同型 1 处。`en_integrity` 因之报 `missing_assets: ["index..html"]`（硬发现）。

建议出口：补丁 P-004（`find` 该 href、`replace` 单点、`expect 1`），转化后须重转该词条 yuanwen 并复跑 I2；或判格式例外并登记。属 053 四出口处置，本卡不改补丁池。

### R-5 旧池 judge 无凭证（待补）

pool 1780／gap 48／stale 45 只见于叙述，无落盘 JSON；算术自洽但不可复算。建议以 `page_assemble.py --all --dry`（旧池）留痕，或在报告中标注“叙述值，无凭证”。

### R-6 exit＝1 与补转凭证（建议补记）

`fetch-last.json` 记录 exit 1（2 件转换 `PermissionError`），SOP 以 exit 0 为全绿；补转动作无日志，仅结果可证（I2 复跑 1873／0）。建议 spec 记补转命令与时间，或 `phase12.py` 在补转后归一退出码。

### R-7 叙述口径（已改）

`phase12-analysis.md` §五“钉账资产 image 1477／script 28”是抓取前值，与同文 §三、`run.json` 的 1474／458 矛盾；`script 28` 恰是 `local.js` 补登前计数，与“已补登”自相矛盾。已改为抓取后口径，并注明修复后 image 回到 1477。

## 三、既存项（非本轮引入，未改动）

| 词条 | 现象 | 定性 |
| --- | --- | --- |
| aristotle-psychology | `suppl1.html` 未登记（游离件）；`suppl2–4` 在盘未登记（fetch_audit 契约不写 baseline，非硬） | 既存账务缺口 |
| saadya | `notes.html` 未登记（游离件） | 既存 |
| 全库 | `files[]` 内 113 条重复 image 路径（前后一致） | 既存账务冗余 |
| logic-deontic | `fig-graph-b/c.svg`、`supplement.html` 被引用且在盘，未登记 | fetch_audit 契约允许 |

修复后 `en_integrity --all`：audited 1873、clean 1871、with_hard_issues 2、hard_findings 3（aristotle-psychology 2、saadya 1）。

## 四、结论

阶段 1.2 的实质数字（抓取、分类、建账面、补丁、I2、B3.1／B3.2）全部经独立复算成立；两处文档数字错误已订正，一处账实脱节（3 个旧图摘钉）已修复。剩余三项待办：R-3 SVG 分类口径、R-4 上游新错链出口、R-5／R-6 凭证与退出码口径。
