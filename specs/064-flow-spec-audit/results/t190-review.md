# T190 评审记录：rv-08 q6 标点（habermas）

- 任务：T190（T138 六轴第六轴，最后一轴）；日期：2026-11-27；actor：trae-main
- 依据：`rules/04` §六轴（ADR-0079）、`specs/060-six-axis-quality-gates/checklists/q6-punct.md`（P-1…P-20）
- 写域：`h/habermas.md`（12 处引文定位符＋1 处双冒号）；报告：`state/axis/habermas.punct.json`（运行态）

## 1 规模与处置

| rule | 命中 | 处置 |
| ---- | ---- | ---- |
| P-13 连接号 | 164 | waived：全部为引文页码区间（SEP 房屋样式 en-dash，如 285–6），按 q6 豁免清单与 rules/02 照录；不属正文数值范围（与 q5 M-6 同口径） |
| P-7 冒号套用 | 4 | false-positive：第二冒号位于引文 locator 内（章节／页码分隔），正文仅一个提示冒号 |
| P-8 引号 | 1→0 | 工具误报（法语 `d’appui` 的撇号被当单引号对），修工具后消除 |
| P-18 引号邻接空格 | 1→0 | 工具误报（段间换行被 `\s+` 当行内空格），修工具后消除 |
| P-20 半角标点 | 12→0 | 正文修改：引文定位符“第 N 章, / :”统一为全角“，／：”，并去掉 12 处多余空格 |
| P-1–P-6、P-9–P-12、P-14–P-17 | 0 | 机检与 `check_style`／`check_pairs` 均 0；人读未见异常 |

## 2 正文修改

| 位置 | 原 | 改 | 依据 |
| ---- | ---- | ---- | ---- |
| 12 处引文定位符（L325、L327×4、L329、L524×3、L540、L548、L552） | 第 6 章, 202／第 7 章: 181–200 等 | 第 6 章，202／第 7 章：181–200 等 | P-20 正文中文旁半角标点 |
| 同 12 处 | 章： 160／章， 101–105（全角标点后多一空格） | 章：160／章，101–105 | 标点后不留多余空格 |
| L397 | 如何使以下主张彼此相容：(a)… | 如何使以下主张彼此相容——(a)… | P-7 单句不套用两个冒号；改一字线提示列举 |

L397 对应 q2 骨架行 `p-habermas-0621` 的 `zh` 已同步更新；q1 引文 hash 未变（修改均在引号外）。

## 3 工具修正

- **P-8**：`’` 若前后均为拉丁字母（`d’appui` 式撇号）不参与单引号配对。
- **P-18**：引号邻接空格只认行内空格 `[ \t]+`，不再把段间换行当空格。
- 新增 `tools/tests/test_punct_audit.py` 4 项（撇号、段间换行、行内空格、汉字后半角标点），4/4 通过。
- 修正后 issue：181→168（P-8／P-18／P-20 清零，剩余 P-13 164＋P-7 4）。

## 4 机检凭证

| 检查 | 命令 | 结果 |
| ---- | ---- | ---- |
| q6 门禁 | `python tools/punct_audit.py h/habermas.md --gate --json` | problems 0，退出码 0 |
| 报告 | `state/axis/habermas.punct.json` | 168 条：164 waived＋4 false-positive，0 pending |
| 新增单测 | `python -m unittest tools.tests.test_punct_audit -v` | 4/4 OK |
| q1 hash | `cite_audit --check-hash` | 0 |
| q2／q3／q4／q5 门禁 | `logic_audit`／`grammar_audit`／`register_audit`／`measure_audit --gate` | 均 0 |
| 全量门禁 | `python tools/check_all.py` | 23/23 全绿 |

## 5 发现与限制（不静默）

- **K1 P-19 渲染层未验**：`check_render_artifacts` 扫描到 0 个已构建页面（本会话未构建站点），行首行末禁则无法在渲染产物上核对；源级标点检查已通过，P-19 留待站点构建／CI 渲染扫描。
- **K2 页码区间豁免**：164 处 en-dash 为引文页码，按照录豁免；若未来统一引文体例，应走引文规则而非 q6。
- **K3 复核独立性**：reviewer 与 tr-02 draft actor 同为 `trae-main`，属既定单会话偏离（同 T185–T189）。

## 6 结论

q6 标点完成：168 条 issue 全部处置（164 waived＋4 false-positive），0 pending，硬项 P-8／P-9／P-11／P-13／P-15／P-18／P-20 均无未处置命中；正文修正 12 处引文定位符标点与 1 处双冒号；工具消除两类误报并加单测 4/4。K1 渲染层缺口显式登记。T138 六轴（T185–T190）全部完成，下一步 T139（rv-09 体例终校）。
