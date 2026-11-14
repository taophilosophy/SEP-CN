# 执行记录：standards-tier3-rollout

## 开工卡（2026-11-14，M1 会话）

* **status**: 批 A1 执行完毕待收口；批 A2/B/C/D 排队
* **claim**: M1（用户本轮「复核后全面批准」；语料面按 ADR-0028 词条定岗）

## A2 转任务书交付（2026-11-14，pc6 主研读会；用户裁定「你仅出任务书」）

* **用户裁定**（本轮）：「你仅出任务书。具体任务交付给 s3_checked 之前的阶段，既有 s3_checked 完成的也撤销到该任务之前。」——pc6 会话撤销上列 A2 认领（未执行任何语料改动），A2 全部工作转为任务书 `ren-wu-shu-a2.md` 交付：具体任务由 s3_checked 之前的阶段会话随词条任务执行，现存 s3_checked（快照 24 件）撤销到 audited 后随新体例条款重走三校。
* **独立复算 A1（输入任务书基线）**：引注面完好（abraham-daud `I.3–5`、sharpe `pp. 129–30` 未动）、ISO 日期完好、en-dash 差值 1,394 精确守恒 ✓；本会话复扫残余 6 处/2 文件（他会复扫 5 处半角＋`1/` 目录 1 处 en-dash——其卡钉疑漏 `1/` 目录，195 vs 196 文件口径差实指）；**另有系统性漏网形态**：`（名字，1622–84）` 逗号前缀生卒年不在 connector-form 视括号前置 pattern 内，括注区间总形态（`数字[–―-]数字）`）letter 目录实扫 **3,072 处**（en-dash 3,000＋hyphen 72，含引注/照录豁免面待逐处裁定剔除）——任务书 W1 按此上界钉基线。
* **登记册面**：ren-ming-biao.md 数字邻接 en-dash 1,762 处（主体为生卒列区间，冒号页码式实测 0 处）、shu-yu-biao.md 5–6 处（牛顿 1665–1666、狄尔泰 1904–9、B 版演绎 §17–20、Rawls 2005: 23–28、Daniels 1996: 22–24、59–60——多为**依据列书证引注**，预计大多豁免保留，逐条裁定）——任务书 W2，交付维护任务通道。

## 步骤

| 步 | 内容 | 验收 |
| ---- | ---- | ---- |
| E1 | 卡钉：connector-scan 全库实扫入 `bin/connector-scan-baseline-20261114.json`（1,140 告警/195 文件；en-dash 面 1,135+） | 卡钉入库先于铺量 |
| E2 | 试金石（ADR-0039 §10）：3 文件 9 处（abner-burgos/al-farabi/abu-bakr-al-razi），人眼逐处对照裁定；幂等重跑 0 改动 | 试金石通过 |
| E3 | 铺量：`bin/normalize_en_dash.py` 全量，1,394 处/191 文件，manifest 逐行 before/after | manifest 入 results/ |
| E4 | 手改：阻断词年份起止 20 处（约/前/公元/?），逐处指定精确串并断言唯一命中，`results/manual-fixes.json` | 20/20 唯一命中 |
| E5 | 独立复算：复扫 connector-form 1,140→**5**（全为半角连字符存量，非本批面）；en-dash 总量 55,473→54,079，差值=1,394 精确守恒 | 守恒门通过 |
| E6 | 豁免面边界登记：照录/引注 en-dash 26,546 行不属归一面；待人工判定 12 处（罗马卷次、Bekker 59b–c、folio、笔记本 B–E、记号负号） | 边界与清单在案 |

## 待人工判定清单（禁机械，FR-002）

* 罗马卷次区间：boethius-dacia 25（IV–VI、VIII–IX、XIV）、bradley-moral 13（I–III）——GB/T 15834 §4.13 三形未明列罗马序数范围，待裁定时一并定。
* 书证/页码引注：diodorus-cronus 8（59b–c、142a–143b）、erasmus 181（Ei verso–Eii recto）、langer 45（87n–88n）、leibniz-evil 47（xv–xxiv、xxiii–xxiv）、nietzsche-aesthetics 37（1[85]–1[105]）——引注编号豁免面。
* 其他：origin-descent 23（笔记本 B–E 字母区间）、leibniz-logic-influence 43（莱布尼茨记号负号「以 – 表示」）。

## 收尾

* check_all 全绿后提交；语料提交按 manifest pathspec 精确加件，防卷他会件。

## 更正登记（2026-11-14）

* 前提交 36f246a82（results/）与其后语料提交 6945fcf8f 实际交付 **191 文件**，提交信息误写 194——差额为试金石 3 词条（abner-burgos/abu-bakr-al-razi/al-farabi），已随补交提交入库。
* **证据事故（归因 R4 写入路径脱核变体）**：幂等验证复跑用同一 `--out` 覆写了 pilot manifest，原始 9 处凭证丢失；交付凭证改由 git diff 与复扫残门承担。**防线升级**：验证性复跑必须 `--out` 指向独立文件，禁覆写原始 manifest。
* 总交付对账：机械 1,394＋手改 20＝1,414 处；letter 目录 en-dash 55,473→54,079（差 1,394 精确）；复扫 connector-form 5（全为半角存量，非本批面）。

## A2 移交登记（2026-11-14）

* **用户裁定**：「你仅出任务书。具体任务交付给 s3_checked 之前的阶段，既有 s3_checked 完成的也撤销到该任务之前。」——出单会话停止语料执行（G9② 161 处已判定未动笔），全部执行移交 s3_checked 之前阶段（audited 状态下校对管线）。
* **任务书**：`ren-wu-shu.md`（T0 回退原语工具任务归治理会话；T1 A1 的 185 条状态回退 done 170/r1 3/s3 12 → audited，文本保留；T2 顿号 147 删/14 豁免；T3 括号套用 335 候选先读条款原文；T4 多段引文 2 块；T5 收口）。
* **侦察凭证**：`results/g9-dunhao-candidates.json`（161）、`results/g9-paren-nesting.json`（335）、`results/a1-task-states.json`（185 条状态清单）；G9① 省略号 4 候选全豁免收口（dai-zhen ×2 与 yuanwen 同形照录）。
* **边界**：受影响 191 词条中 1 条无任务文件（korean-confucianism.supplement）单独裁定；5 条 cleared 本在 pre-s3 不动。

## 双任务书协同（2026-11-14）

* pc6 同轮签发 `ren-wu-shu-a2.md`（5b1d4b7ff）：路由=在途任务 audited/s3 随步落实＋s3_checked 快照件撤销（手工回写）＋done 归 specs/023 回炉＋r1 待用户明确；另扩 W1 括注区间上界 3,072、W2 登记册生卒列 1,762。
* 本会话 `ren-wu-shu.md` 补协同说明：T0/T1 执行路由降级备选（待用户扩大裁定才启用）；T2 判定清单（147/14）、T3/T4 候选与 G9① 结论作为 a2 输入凭证。
* **未决对表（待用户裁定）**：回退范围 185（含 done/r1）vs 24（现存 s3_checked）；r1_reviewed 是否同口径回退。
* pc6 补记（补面版重写后）：ren-wu-shu-a2.md 已重写——W1（括注生卒年/年代 3,072 上界，含 `（人名，1622–84）` 逗号前缀漏网形态）＋W2（登记册生卒列 1,762＋shu-yu-biao 5–6 逐条裁定）为补面，G9②③④/省略号/回退原语让渡 ren-wu-shu.md 及其判定清单（作 a2 输入凭证）；其初稿「手工 JSON 回写状态」指令**作废**（tasks/README §12 禁手改状态字段），回退一律以 T0 原语为准；W1 漏网根因=connector-form pattern 5 视括号仅认「（」前缀——治理面可选扩展（随 P14/P15 工具批一并考虑）。

## 用户裁定落定：185 条全口径回退（2026-11-14）

* 用户裁定：「done 也必须重来」——ren-wu-shu.md §0 二补、T1 激活：A1 受影响面内 state ∈ {s3_checked, r1_reviewed, r2_reviewed, r3_reviewed, done} 全部回退 audited（快照 185＝done 170/r1 3/s3 12，执行时按谓词实查）。
* a2 的 done→023 路由对 A1 受影响面被取代；023 回炉保留给 A1 未受影响 done 件；r1_reviewed 同口径（a2 §5 之问已答）。
* 执行方注意：回退脚本化（逐条 steps 追加＋state 回写，manifest、幂等、其余字段零触碰）；W1-W6 命中在回退后的 audited 步落实，s3 重走按 ADR-0041 条款核销。
