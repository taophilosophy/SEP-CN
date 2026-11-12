# specs/015 破折号专项线交接卡

更新：2026-11-12（pc6）。本卡只记**破折号防滥用线**；语体线（verdicts.jsonl／置空重译）另有其记录，两线互不代管。

## 已完成

1. **枚举工具**：`bin/dash_scan.py`——全库 done 词条正文破折号用量枚举（排除引块／代码块／References 照录区），输出 `results/dash-scan.jsonl`，按密度排序；只作复核优先级，不作判定（spec.md 判定口径 7）。
2. **高密度段判定**：`per_1k ≥ 6/千字` 共 51 条全部语义复核，50 条结论入库 `results/dash-verdicts.jsonl`（james-ward 已在语体 verdicts 有 `dash=ok` 记录，不重复）；50 条均判 `abused`、`action=fix`。
3. **规则落地**：`rules/02`“破折号滥用的修复方式”——修复以含破折号的原句为单位、回英文源句（`yuanwen/`）**整句重新翻译**，禁止符号层机械替换（用户 2026-11-10 裁定）。
4. **样板修复**：`m/mathematics-inconsistent.md` 完成——22 段 58 处破折号句全部整句回源重译，残余 0；`check_prose` 回落 s2 豁免基线 8 条（无新增）；`check_style`／`check_academic --strict` 过。复核记录见 dash-verdicts 末条。
5. **机械替换回溯审计（2026-11-12，用户裁定「存在机械替换情况，禁止，必须重译」）**：新工具 `bin/mech_audit.py` 对全部已收口条目的修复 commit 逐行做 diff 分类（pure＝去标点逐字同＝纯符号替换；conn＝相似度≥0.95 且增删≤4 字＝连接词级补丁；susp＝0.85–0.95＝须人工判读），产出 `results/mech-spots.json`。首轮覆盖 17 条收口词条、438 处候选＋20 处 susp，**逐处回 `yuanwen/` 源句比对后实修 29 处、9 条词条判定零实修**（明细见 dash-verdicts 2026-11-12 各条）。查出的硬伤示例：kepler 诸行星「并不规则」↔源文 moved irregularly（语义翻转）、mathematics-inconsistent「特例微积分」连读（删对破折号）、al-farabi「哲学家—先知—统治者」被擅改为「兼……兼」（合规连接号误改，已回滚）。结论：符号层替换集中在 early 批次，且多数恰与源句结构对应（such as→括注、that is→即）；**「相似度高」不等于违规，必须回源定性**。

## 续做队列（按 dash-scan 密度降序）

lambert-auxerre→dai-zhen→…→kant-leibniz→kilvington **等 17 条已收口且通过机械替换回溯审计**（见 dash-verdicts `action=none`）。**下一条：leibniz-mind（81 对，7.92/千字）**，其后 lakatos（200）→ luxemburg（136）→ leibniz-evil（144）→ lorenzo-valla（116）→ karl-reinhold（98）→ ockham（156）→ duhem（98）→ 18thGerman-preKant（139）→ kochen-specker（118）→ …（余 34 条全清单见 dash-verdicts.jsonl `action=fix`，动手前以 dash_scan.py 最新复扫为准）。

**注意事项**：

* 语体线已置空重译的词条（classical／mixed，任务已出 done 队列）自动移出本线，重译时按新规则写即可——动手前以 `dash_scan.py` 最新复扫为准，判定记录以 dash-verdicts 为准。
* 修复一律整句回 `yuanwen/<letter>/<slug>.md` 英文源重译；成对插入语（真正插入、转折）可保留，引文内、书名内破折号豁免不动；单破折号作连接号（如「哲学家—先知—统治者」）合规，**不得改成「兼」「与」**（2026-11-12 al-farabi 回滚先例）。
* 重译后必跑：`check_prose <file>`（对照任务 s2 evidence 豁免基线，不许新增）、`check_style.py --docs <file>`、`check_academic.py --docs <file> --strict`，再 `dash_scan.py` 复扫该条归零确认。
* **收口前必跑** `python specs/015-style-register-review/bin/mech_audit.py <slug>`，对 pure/conn/susp 三类候选逐处回源定性；pure 必改，conn／susp 视源句结构判「保持」或「重译」，结论写进 verdicts 的 evidence。一次性本地草稿不得留在 `script/`。
* 完成后向 dash-verdicts.jsonl 追加 `{dash:"ok", action:"none"}` 记录（追加式流水，不改旧行）。
