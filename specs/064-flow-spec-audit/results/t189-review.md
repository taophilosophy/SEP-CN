# T189 评审记录：rv-07 q5 计量（habermas）

- 任务：T189（T138 六轴第五轴）；日期：2026-11-27；actor：trae-main
- 依据：`rules/04` §六轴（ADR-0079）、`specs/060-six-axis-quality-gates/checklists/q5-measure.md`（M-1…M-10）
- 写域：`h/habermas.md`（本轮无改文）；清单：`state/axis/habermas.measure.json`（运行态）

## 1 规模

| 项 | 数 | 说明 |
| ---- | ---- | ---- |
| 量值-单位条目 | 0 | 全文无 km／kg／°C／%／货币等物理量值 |
| 数值范围 | 170 | 164 为引文页码区间（短横线），6 为正文范围（一字线） |
| 机检 issue | 1 | M-6“连接号混用”聚合告警 |
| M-1／M-2／M-4 单位形态告警 | 0 | 无量值条目 |
| M-5 同量多单位 | 0 | 无量值条目 |
| M-6 真混用 | 0 | 见 §2 |

## 2 数值范围与连接号（M-6）

- **正文范围 6 处**，全部用一字线“—”：1929—2026（生卒）、1964—71、1971—1982、1983—1990、1991—1996、1—4（权利编号）。同形，合规。
- **引文页码区间 164 处**，用短横线“–”（如 1985–6、285–6、359–87）。按 `rules/02` 参考文献照录段“含 SEP 房屋样式的 en-dash 页码区间”豁免，不属 q5 正文数值范围。
- 机检把两类不同域合并统计，报“–／—”混用；逐条核对后判 **false-positive**，不统一改写（改写页码会破坏引文定位，且违反照录豁免）。

## 3 日期、数字与货币（M-7／M-10）

| 检查 | 结果 |
| ---- | ---- |
| 世纪／年代形态 | “20 世纪”“80 年代”“90 年代”全用阿拉伯数字；无“二十世纪”“八十年代”混形 |
| 日期空格 | 无“1929年”“6月”“18日”式缺空格；统一“1929 年 6 月 18 日” |
| ISO／全角 | 无 `YYYY-MM-DD` 日期、无全角数字 |
| 英文月份 | 仅参考文献条目内出现（照录，豁免） |
| 货币 | 无 US$／USD／欧元等；检索“马克”命中均为“马克斯·普朗克”，非货币 |
| 百分比 | 无 %／％ 量值 |

## 4 工具修正

原 `measure_audit` 把任意“数字＋字母”当量值，引用键 `1992a`／`1971c` 被解析成“数值 1992＋单位 a”，产生 394 个假条目、395 条假告警。本轮：

- 只识别白名单单位（`UNITS`／`BAD_FORM`）与复数形（`miles`→`mile`，M-1）；
- 跳过引用键 `\d{4}[a-z]` 与未登记符号（`5G`／`3D`／`COVID` 等）；
- 条目补 `canonical`／`reviewer` 字段；
- 新增 `tools/tests/test_measure_audit.py` 4 项（引用键跳过、单位与空格、复数、非量值 token），4/4 通过。

修正后：条目 394→0，issue 395→1（仅 M-6 聚合）。

## 5 机检凭证

| 检查 | 命令 | 结果 |
| ---- | ---- | ---- |
| q5 门禁 | `python tools/measure_audit.py h/habermas.md --gate --json` | problems 0，退出码 0 |
| 清单 | 读取 `state/axis/habermas.measure.json` | 0 条目；1 条 M-6 false-positive；0 pending |
| 新增单测 | `python -m unittest tools.tests.test_measure_audit -v` | 4/4 OK |
| q1 hash | `python tools/cite_audit.py h/habermas.md --check-hash --json` | problems 0 |
| q2／q3／q4 门禁 | `logic_audit`／`grammar_audit`／`register_audit --gate` | problems 0 |
| 全量门禁 | `python tools/check_all.py` | 23/23 全绿 |

## 6 发现与限制（不静默）

- **J1 本件量值面为空**：habermas 为哲学传记/论证文本，无物理单位与货币；q5 的实际对象退化为日期、年代、页码区间与编号。结论只对当前文本成立，不外推为“q5 全库已验”。
- **J2 页码区间豁免**：164 处 en-dash 为引文页码，按 rules/02 豁免；若未来统一引文体例，应走引文规则而非 q5。
- **J3 复核独立性**：reviewer 与 tr-02 draft actor 同为 `trae-main`，属既定单会话偏离（同 T185–T188）。

## 7 结论

q5 计量完成：0 个量值-单位条目、0 条 M-1／M-2／M-4／M-5 硬错误；6 处正文范围统一用一字线，164 处页码短横线按引文豁免；唯一 M-6 聚合告警定性为跨域误报；日期与数字形态全文一致。`measure_audit --gate` 0。下一步 T190（rv-08 q6 标点）。
