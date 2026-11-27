# T187 评审记录：rv-05 q3 语法（habermas）

- 任务：T187（T138 六轴第三轴）；日期：2026-11-27；actor：trae-main
- 依据：`rules/04` §六轴（ADR-0079）、`specs/060-six-axis-quality-gates/checklists/q3-grammar.md`（G-1…G-19）
- 写域：`h/habermas.md`（本轮无改文）；报告：`state/axis/habermas.grammar.json`（运行态）

## 1 规模与分布

| 项 | 数 |
| ---- | ---- |
| 机检 issue 总数 | 140 |
| G-11 定语链／长句 | 105（de-chain 72＋long-sentence 33） |
| G-10 弱动词 | 32 |
| G-9 “被”字句 | 2 |
| G-7 关联词错配候选 | 1 |
| G-1 成分残缺 | 0 |
| G-5 句式杂糅 | 0 |
| G-17–G-19 和制汉语命中 | 0 |
| 待处置（pending） | 0 |

## 2 逐条处置

| 处置 | 数 | 说明 |
| ---- | ---- | ---- |
| waived | 139 | 139 条反欧化告警逐条豁免：137 条与 T135 处置表精确匹配，2 条因 T136 人名规范化致 detail 变化，按 T135 同口径补录（L349 de-chain、L351 long-sentence） |
| false-positive | 1 | G-7 L506“无论如何，全球政府也不可能完全合法”：“无论如何”为固定习语，非“无论……也”关联词错配 |
| fixed | 0 | 本轮无需改文 |

豁免口径与 T135 一致：学术长定语链不拆（拆分破坏论证层次或指称关系）；引证密集长句保留；`进行／作出／加以`为必要动词化搭配，非欧化弱动词；“被”字句 2 例为必要被动。

## 3 第一层补充检查（人审辅助）

对 G-2／G-6／G-7 的常见模式做定点扫描，命中均为 0：

- G-2：`原因是因为`、`原因是……造成的`、`大约……左右`、`首先……第一`、`目的是为了`、`再次重申`、`付诸于／诉诸于／来自于／截止到`。
- G-6：`进行地`、`地进行`。
- G-7：`不但……反而`、`只有……就`、`虽然……但是……但是`。

G-1／G-5 机检 0；G-3 搭配、G-4 语序、G-8 指代三项无专用机检，本轮以定点扫描＋前序 T134／T135 通读为基础，未逐句全量重审（见 §5）。

## 4 机检凭证

| 检查 | 命令 | 结果 |
| ---- | ---- | ---- |
| q3 门禁 | `python tools/grammar_audit.py h/habermas.md --gate --json` | problems 0，退出码 0 |
| 报告 pending | 读取 `state/axis/habermas.grammar.json` | 0 |
| q1 hash 守恒 | `python tools/cite_audit.py h/habermas.md --check-hash --json` | problems 0 |
| q2 门禁 | `python tools/logic_audit.py h/habermas.md --gate --json` | problems 0 |
| 全量门禁 | `python tools/check_all.py` | 23/23 全绿 |

## 5 发现与限制（不静默）

- **H1 第一层未全量重审**：G-3 搭配、G-4 语序、G-8 指代无可靠机检，本轮只做定点模式扫描与前序通读复用；未逐句建立语法审查记录。若要求 q3 全文覆盖，应另立逐句语法批。
- **H2 依赖前序处置**：139 条反欧化告警沿用 T135 的逐条豁免，未在 q3 重新改写；q3 只核对豁免理由与当前文本仍相符（T136 人名规范化造成的 2 条 detail 漂移已补录）。
- **H3 复核独立性**：reviewer 与 tr-02 draft actor 同为 `trae-main`，属既定单会话偏离（同 T185／T186）；已记录。

## 6 结论

q3 语法筛查完成：140 条机检 issue 全部处置（139 waived＋1 false-positive），0 pending；G-1／G-5 为 0，G-7 唯一命中为习语误报；G-17–G-19 无命中；`grammar_audit --gate`、q1 `--check-hash`、q2 `--gate` 均 0。H1 的全文逐句缺口显式登记。下一步 T188（rv-06 q4 语域）。
