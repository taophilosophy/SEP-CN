# 执行记录：standards-tier3-rollout

## 开工卡（2026-11-14，M1 会话）

* **status**: 批 A1 执行完毕待收口；批 A2/B/C/D 排队
* **claim**: M1（用户本轮「复核后全面批准」；语料面按 ADR-0028 词条定岗）

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
