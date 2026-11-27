# 064 组 C 执行证据（2026-11-27）

- 组：**c**（W1 第一梯队；c1 habermas → c2 logic-preference → c3 environmental-aesthetics）
- start tag：`batch/064-c-start` → `14d1d7a55`（已推送）
- end tag：待打（C 组 T135–T153 收口后）
- 本轮完成：**T132（样章）＋T133（全量）＋T134（一校首轮）＋T135（二校）＋T136（rv-01）＋T137（rv-02）**；T138 已拆为 T185–T190，六轴与 T139（rv-09）、T140 拆分项 T191／T192、T141（sg-03 用户签字）全部完成；**habermas 已 `done`**；T142 拆分项 T193–T195 完成；logic-preference T143 样章、T196–T201 全量翻译与收口完成，状态 `tr-02_checked`；T145–T148 未启动
- 门禁：`python tools/check_all.py` **23/23 全绿**
- 授权：T132 主代理单干；T133 用户批准至多 5 个子代理，按 5 个批次产出、主代理合并（ADR-0034 当轮例外）

## 1 T132 样章（已完成）

- 账本：`tasks/h/habermas.ledger.yaml` 起始 16 段，source 逐段回源、step1／step2 双版。
- 样章：`h/habermas.md` §1–§2，约 2,350 汉字。
- 任务状态：`cleared → ex-04_checked → tr-02_checked`；补 `project_spec` 六项与 `llm-pe/full` PE 字段。
- `check_style` 0 issue、`check_quotes` 0 违例、`check_terms` 硬错误 0。

## 2 T133 全量（已完成）

| 项 | 结果 |
| ---- | ---- |
| 批次 | 5 个子代理：b1 §1.2 尾–§2.1；b2 §2.2–§2.3；b3 §2.4–§3；b4 §4–§6；b5 §7＋尾节 |
| 合并 | 主代理合并样本＋b1–b5，补 §1.2 被跳过的 3 段（源行 34／36／38）与全部脚注定义 |
| 全文 | `h/habermas.md` **38,150 汉字**（总字符约 110,183；含 §1–§7、参考文献、学术工具、其他网络资源、相关词条、脚注） |
| 账本 | `tasks/h/habermas.ledger.yaml` **239 段**；source 逐段对应 yuanwen；step1／step2 双版；239／239 step2 均落文；T133 复核补漏 §1.1 P4 与 §1.2 交往权力段后由 237 增至 239 |
| 脚注 | 155 个文内标记；完整脚注定义块自 `yuanwen` 复制（254 条定义，参考文献照录） |
| 体例 | `check_style` 0 issue；`check_quotes` 0 违例；`check_pairs` 0 issue；`check_academic --strict` 无硬错误；`check_math_zh` 0 条 |
| 全量门禁 | `check_all` 23/23 全绿 |

### 2.1 勘误承载裁定（T133 执行时）

T130 批准的两条 `habermas` 勘误（`des Ritus”,,`、`Theory on Empitical Research`）位于**参考文献脚注**，中文正文不翻译书目条目（照录）。T133 将勘误表 §十三“中文承载”由“译注队列”改为 **“照录区，无需译注（参考文献条目照录；中文正文不复制）”**；`check_pairs` 的 errata-apply 因此按照录区豁免，全文 0 issue。该调整是对 T130 承载形态的执行级修正，缺陷登记与参考读法不变。

### 2.2 术语与已知告警

- 登记形使用：于尔根·哈贝马斯、公共领域、法兰克福学派、社会研究所、交往行为、《交往行为理论》、商谈伦理、合理重构。
- 子代理新增术语候选：生活世界、有效性主张、形式语用学、以言行事、交往权力、系统／生活世界、合法性危机、后世俗、宪法爱国主义、世界主义等；T136 已登记 `civil society (Habermas)`＝公民社会、`legitimacy (Habermas)`＝合法性两个语境分行，其余未登记词留 T136 后治理批次。
- `check_terms --docs h/habermas.md` 硬错误 0；仅 `Müller-Doohm` 引用组拉丁名 1 条告警，按引用照录豁免。

## 3 H1／目录同步

`ren-ming-biao.md` 登记形为 **于尔根·哈贝马斯**；已统一 `SUMMARY.md`、`mu-lu-s.md`、`baseline/mulu-map.json`、H1 与 `en/SUMMARY-en.md`。

## 4 状态与下一步

| 项 | 结果 |
| ---- | ---- |
| T132／T133／T134／T135／T136／T137 | **已完成**（T137 rv-02 完成，状态 `rv-02_checked`） |
| T138／T140／T141 | 六轴 T185–T190、sg-01／02（T191／T192）、sg-03（T141）全部完成；T141 用户签字后置 `done`；两个容器不勾选 |
| T142／T143／T144 | T142 拆为 T193–T195（完成）；T143 样章完成；T144 拆为 T196–T201，T196／T197 完成、T198 未启动；容器均不勾选 |
| T139–T141 | 未启动 |
| c2／c3 | 未启动 |
| `batch/064-c-end` | 待打（C 组 22 步全部收口后） |
| 未改 | `en/`、`html/` 原文、其他词条译文 |
