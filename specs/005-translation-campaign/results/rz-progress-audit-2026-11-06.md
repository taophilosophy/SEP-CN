# R-Z 词条翻译进度对账（2026-11-06）

**会话**：RZ 进度对账（主会话直审，不用子代理） | **工具**：`script/rz_audit.py`（三源核对，只读）

## 方法

对 r–z 九个字母目录 385 个正式词条逐条核对四源：`SUMMARY.md` 正式条目（排除 —see 别名；R-Z 无 * 占位母词条）、`tasks/<L>/<slug>.json` 状态机（state/steps/version_pin）、`tasks/<L>/<slug>.ledger.yaml` 组稿账本、词条文件 `<L>/<slug>.md` + `yuanwen/` 镜像 + `baseline/entries.json`。

## 实测数字（与 `campaign.py status` 实时推导一致）

|字母|总词条|基线|镜像|已建任务|done|未建任务|状态分布|
|---|---|---|---|---|---|---|---|
|r|85|85|85|11|5|74|pending 5 / s1_checked 1 / done 5|
|s|161|161|161|6|1|155|pending 5 / done 1|
|t|71|71|71|2|0|69|pending 2|
|u|4|4|4|0|0|4|—|
|v|15|15|15|0|0|15|—|
|w|38|38|38|3|0|35|pending 3|
|x|3|3|3|0|0|3|—|
|y|2|2|2|1|0|1|pending 1|
|z|6|6|6|0|0|6|—|
|**合计**|**385**|**385**|**385**|**23**|**6**|**362**|pending 16 / s1_checked 1 / done 6|

**进度**：done 6/385（1.6%）；已建任务 23/385（6.0%）；在途 1 件（r/redistribution，s1_checked，RZ-main-20261104 于 2026-11-05）。

done 6 明细：r 批 reasoning-analogy / reid-memory-identity / reism / religious-experience / richard-sophister（r3 步骤齐全、账本齐备、正文 CJK 3695–22169）+ s 批 spacetime-holearg（10-28 旧存量，无组稿账本，账本注记已裁定不补造）。

## 偏差发现与纠正

1. **r 批账本对账补记失实三处**（原记"86 词条=done 5/pending 5/cleared 1+75 未建"）：总数实为 85（未建 74）；redistribution 实为 **s1_checked** 非 cleared（steps 至 s1，2026-11-05T19:07Z）。已 `campaign.py advance r translate --note` 追加更正条款（原补记保留留痕）。
2. **s–z 八批补记**：与实测逐项一致（含 spacetime-holearg 无账本裁定、t/w/y 未建计数），无需改动。
3. **PROGRESS.md**：重新生成与已提交版本零内容漂移（done 93 为全局数，含其他批次当日推进），纯时间戳差异已还原。
4. **状态机↔文件偏差**：零（无 done 缺 r3、无在途缺文件、无 cleared 缺 version_pin、无孤儿任务、无损坏 json）。

## 结论

R-Z 九批 phase=translate 与事实相符，账本计数经更正后零漂移；批次无收口条件（done≪total），继续由 RZ-main-20261104 按状态机推进。
