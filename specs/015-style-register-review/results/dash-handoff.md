# specs/015 破折号专项线交接卡

更新：2026-11-12（pc6）。本卡只记**破折号防滥用线**；语体线（verdicts.jsonl／置空重译）另有其记录，两线互不代管。

## 已完成

1. **枚举工具**：`bin/dash_scan.py`——全库 done 词条正文破折号用量枚举（排除引块／代码块／References 照录区），输出 `results/dash-scan.jsonl`，按密度排序；只作复核优先级，不作判定（spec.md 判定口径 7）。
2. **高密度段判定**：`per_1k ≥ 6/千字` 共 51 条全部语义复核，50 条结论入库 `results/dash-verdicts.jsonl`（james-ward 已在语体 verdicts 有 `dash=ok` 记录，不重复）；50 条均判 `abused`、`action=fix`。
3. **规则落地**：`rules/02`“破折号滥用的修复方式”——修复以含破折号的原句为单位、回英文源句（`yuanwen/`）**整句重新翻译**，禁止符号层机械替换（用户 2026-11-10 裁定）。
4. **样板修复**：`m/mathematics-inconsistent.md` 完成——22 段 58 处破折号句全部整句回源重译，残余 0；`check_prose` 回落 s2 豁免基线 8 条（无新增）；`check_style`／`check_academic --strict` 过。复核记录见 dash-verdicts 末条。

## 续做队列（按 dash-scan 密度降序）

lambert-auxerre→dai-zhen→kepler→al-farabi→leibniz-ethics→peirce-benjamin→lady-masham 等 14 条已收口（见 dash-verdicts `action=none`）；kant-leibniz（147）由 pc6 并行会话在途修复（2026-11-12）；reid-memory-identity（93 处修 75 留 18 源文自带）2026-11-12 收口。**下一条：kilvington（98 对，8.16/千字）**，其后 leibniz-mind（81）→ lakatos（200）→ …（余 35 条全清单见 dash-verdicts.jsonl `action=fix`，动手前以 dash_scan.py 最新复扫为准）。

**注意事项**：

* 语体线已置空重译的词条（classical／mixed，任务已出 done 队列）自动移出本线，重译时按新规则写即可——动手前以 `dash_scan.py` 最新复扫为准，判定记录以 dash-verdicts 为准。
* 修复一律整句回 `yuanwen/<letter>/<slug>.md` 英文源重译；成对插入语（真正插入、转折）可保留，引文内、书名内破折号豁免不动；单破折号作连接号（如「哲学家—先知—统治者」）合规。
* 重译后必跑：`check_prose <file>`（对照任务 s2 evidence 豁免基线，不许新增）、`check_style.py --docs <file>`、`check_academic.py --docs <file> --strict`，再 `dash_scan.py` 复扫该条归零确认。
* 完成后向 dash-verdicts.jsonl 追加 `{dash:"ok", action:"none"}` 记录（追加式流水，不改旧行）。
