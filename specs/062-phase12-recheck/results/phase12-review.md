# 阶段 1.2 独立复核（2026-11-25）

对象：阶段 1.2 收口提交（339c09dcf、2b369808f、23935892e）及其产物 `phase12-run.json`、`phase12-report.md`、`phase12-analysis.md`、`en-delta.json`、`b32-new-gap.md`。

方式：只读复算（不采信自报数字）＋定点门禁复跑；命令与结果如下。ADR-0039“自报完成须独立复算”。

## 一、逐项复算

| 项 | 报告值 | 独立复算 | 判定 |
| --- | --- | --- | --- |
| 抓取 | 1873／1873，失败 0 | `entries-before.json` 与 `baseline/entries.json` 各 1873 条，slug 集零差 | 一致 |
| 账变化 | 522（unchanged 1351） | 记录级差集 522 条：含 `local.js` 补登 430（仅补登 423、仅正文变化 92、兼有 7） | 一致 |
| 磁盘变化 | 126 文件／100 词条 | `en-delta.json` rows 126／slugs 100；账侧非 js 实变路径 122 html＋1 png＋2 svg，另 1 件 `local.js` | 一致（口径见 R-2） |
| 变化分类 | text 65／layout 42／rename-wave 17／binary 1／asset 1 | 原分类 kinds 同值、合计 126；SVG 并入资产类复跑后为 text 65／layout 40／rename-wave 17／binary 3／asset 1 | 一致（R-3 结案后口径） |
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

`spec.md` §5 两处写 `text 66`，实际 65；分类串漏 `asset 1`。原因：分类在 asset 类落地（voting-methods/local.js）前定稿。SVG 归资产类后口径为 65／40／17／3／1（合计 126），与“65 件出建账清单”。

### R-2 图钉丢失（已修）

`logic-deontic` 重钉后，`files[]` 中 3 个旧图（`fig-box-b.svg`、`fig-square-b.svg`、`fig-vbox-a.svg`）被摘除，盘面文件仍在（en/ 冻结，ADR-0062）。后果：`en_integrity.py` 判为游离件（硬发现），而修复前 `en_integrity --all` 硬发现 4 项中 1 项即由此产生。

根因：`tools/fetch_entry.py:upsert_baseline` 以新抓包整体替换 `files[]`；上游新版不再引用的旧资产随之失登记。当日新增的护栏只拦“无 `files` 的记录”，不拦“`files` 变少”。

处置：按 `en_integrity` 既定的 `registered_orphans`（版本更替残件，非硬发现）口径恢复 3 条登记，sha 与原钉一致（`divergence verify` 复跑 4845/4845 pristine）。复检：`en_integrity logic-deontic` clean＝1、硬发现 0；全库硬发现由 4 降为 3（余 3 项均既存，见第三节）。

建议（未实施）：`upsert_baseline` 改为并集保留——旧有而新抓包无者保留原记录（标记残件），避免每次上游修订都摘钉；`check_all.py` 增 `en_integrity` 门（HEAD 的 19 项门禁清单不含它，故门禁全绿掩盖了该硬发现）。

### R-3 SVG 分类（已结案）

`logic-deontic` 的 `fig-square-c.svg`、`fig-three-c.svg` 被上游重导出：画布 206.33×179.51pt → 216.28×175.15pt、357.27×87pt → 367.22×83.91pt，图元引用 26→30、42→47。旧判据把它们判成 `layout`，因为 SVG 无 text 节点、可见文本判据恒为空。

用户 2026-11-25 裁定：图片资产 sha 变了就随钉替换入库，不建账、不过目。据此把 `.svg` 并入 `binary` 资产类（`en_delta.py` 已改，另增 `--base REV` 复跑参数）；复跑值：text 65／layout 40／rename-wave 17／binary 3／asset 1（合计 126）。残差：无。

### R-4 上游新错链（待处置）

`aristotle-psychology/notes.html`（本轮 text 类，109 增删行）第 143 行：

```html
<a href="index..html#ref-1">1.</a>
```

双点错链，旧版（23935892e~1）无此串，系 2026-11-23 修订新引入；正确读法应为 `index.html#ref-1`（脚注回链）。全库同型 1 处。`en_integrity` 因之报 `missing_assets: ["index..html"]`（硬发现）。

建议出口：补丁 P-004（`find` 该 href、`replace` 单点、`expect 1`），转化后须重转该词条 yuanwen 并复跑 I2；或判格式例外并登记。属 053 四出口处置，本卡不改补丁池。

### R-5 旧池 judge 无凭证（已补）

pool 1780／gap 48／stale 45 原先只见于叙述。已用 `bin/oldpool_judge.py` 复现：`git archive 802db20da` 导出第 43 批池，内存替换 `assembly_pool.load_pool` 后对当前 en/ 重判，凭证 `results/phase12-oldpool-judge.json`。结果 **pool 1780／gap 48／stale 45（1873）**，与叙述逐值吻合。

### R-6 exit＝1 与补转凭证（已修）

`fetch-last.json` 记录 exit 1（2 件转换 `PermissionError`），SOP 以 exit 0 为全绿；补转动作无日志。已在 `phase12.py` 加自动补转：抓取后对 `convert_failures` 逐件串行重转（间隔 1.5 秒释放 Windows 句柄），结果写入 `convert_retry`（slug／exit／recovered／at）；任一未补回则整体判失败。报告新增“补转”行。

### R-7 叙述口径（已改）

`phase12-analysis.md` §五“钉账资产 image 1477／script 28”是抓取前值，与同文 §三、`run.json` 的 1474／458 矛盾；`script 28` 恰是 `local.js` 补登前计数，与“已补登”自相矛盾。已改为抓取后口径，并注明修复后 image 回到 1477。

### R-8 新增 gap 的真正根因：B 族账本未随 en/ 刷新（已修）

追查 40 件新增 gap：`page-layout.json` 的 `copyright_year`／`site_year`／`era` 与 `article-ledger.json` 的 `rel_items`／`hids` 都是抓取前冻结值，与新 en/ 不符。逐件定位显示首因是页脚版权年（2025→2026 等）与目录改名波纹（8 件 rename-wave 的 `rel_items` 显示文本）——不是池规则缺陷，也不是上游文本问题。

处置：版面账全量重建（25 件变化：年份／修订日／作者／era／`croce-aesthetics`→`croce`）；结构账增量刷新 101 件（`--slugs` 合并、`--drop croce-aesthetics`，实际变化 51 件）。随后 B3.1 扫描 → 池重建 → 终判，落为 053 第四十四批：**pool 1811→1852、gap 62→21、stale 0、占比 50.12%→51.17%，转好 40、转差 0；B3.1 1663／210 集合零变**。追加书目容器修复后终态 **pool 1853／gap 20**（见 053 批记录）。SOP 已把“B 族账本刷新”列为 1.2 必做步，`phase12.py` 增 `--rebuild-b3`。

**教训**：B3.2 的“gap”是**账与 H0 不符**的合并信号，其中一大族是账本冻结造成的假阳性；判定 gap 前必须先确认账本与本轮 en/ 同时点。

## 三、既存项（非本轮引入）

| 词条 | 现象 | 定性 |
| --- | --- | --- |
| aristotle-psychology | `suppl1.html` 此前既无引用也无登记（游离件） | 已登记（`registered_orphans` 口径） |
| saadya | `notes.html` 同上 | 已登记 |
| 全库 | `files[]` 内 113 条重复 image 路径（前后一致） | 既存账务冗余 |
| logic-deontic | `fig-graph-b/c.svg`、`supplement.html` 被引用且在盘，未登记 | fetch_audit 契约允许 |

修复后 `en_integrity --all`：audited 1873、clean 1871、with_hard_issues 2、hard_findings 3（aristotle-psychology 2、saadya 1）。

## 四、结论

阶段 1.2 的实质数字（抓取、分类、建账面、补丁、I2、B3.1／B3.2）全部经独立复算成立；两处文档数字错误已订正，一处账实脱节（3 个旧图摘钉）已修复，SVG 分类按“随钉替换、不建账”结案。复核提出的其余各项均已落地：补丁 P-004、`upsert_baseline` 并集保留、`en_integrity` 入门禁、补转自动重试、旧池 judge 凭证、B 族账本刷新（R-8）。

## 五、后续收口（2026-11-25 第四十五批，补记）

§二 R-8 修完后的剩余 20 缺口已由 specs/053 第四十五、四十六批逐族清零至 **1 件**（augustine 上游结构错位＝勘误 §十二例外；logic-intensional 裸排环境内嵌行内公式已于 11-26 第四十六批收口）。终态：**B3.2 pool 1,872／gap 1／stale 0（池占页 52.08%）**、**B3.1 1,665／208（+2，0 转红）**、I2 1873/0、`check_all` 全绿。族账见 `specs/053-en-template-audit/execution-log/2026-11-25.md`、`2026-11-26.md` 与 `results/gap-probe-*`。
