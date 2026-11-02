# H 批恢复波子代理指令（compact inline，每代理一条词条）

> 恢复波专用：不读共享文件（共享文件读首次造成浅工），本文件即完整指令。工作目录 D:\SEP-CN。所有 `python` 命令在 `cd /d/SEP-CN` 后执行。

## 你的任务
完成词条 **SLUG** 的 retranslate：`clear → draft → s1 → s2 → s3`，最终 `s3_checked`。只做这一条，**不做** r1/r2/r3/done。

## 输入（只读）
- 英文源：`yuanwen/h/SLUG.md`（唯一底稿，零信任）
- 原始 HTML：`en/SLUG/index.html`（可疑回源）
- H1 文字：从 `SUMMARY.md` 找该词条行（`* [中文名 English-name (Authors)](h/SLUG.md)`），取 `中文名 English-name (Authors)`
- 版本钉：`baseline/entries.json` 该 slug 的 `pubinfo_date`/`archive_edition`
- 术语/人名：`yi-zhe-shuo-ming.md`、`ren-ming-biao.md`（登记册，先登记后使用）

## 第 1 步 clear
先跑 `python tools/task_ops.py show SLUG` 看当前状态：
- 若已是 `cleared`/`drafted`/更高：**跳过 clear**，从当前状态继续（已清过）。
- 若 `pending`：跑 `python tools/task_ops.py clear SLUG`。若报错（基线门禁/非 pending），读错误，不要强推，报告即可。

## 第 2 步 draft（最重要，逐段产出并**即时写回**）
从 `yuanwen/h/SLUG.md` 开头逐节翻译。**关键：边译边写**，不要最后一次性写——先建 `h/SLUG.md`，写 H1 + 版本行，然后每完成 3-5 段正文就**追加写入** `h/SLUG.md`，同时把该段 `source/step1/step2` 追加到 `tasks/h/SLUG.ledger.yaml`（增量保底，中断不丢）。

- 段落账本 `tasks/h/SLUG.ledger.yaml`：每段 `id/source/step1/step2`，step1=忠实初译，step2=语言优化（draft 成稿）。step1 留作 s1 对照底。
- 元素映射：`## 1 中文名`（去英文句点）；`### 1.1 中文名`；行内引用 `(Author year, p. X)` 原样；引块 `>`；图 `![图注](../yuanwen/assets/SLUG/<文件名>)`；表格 `:---:` 居中；数学 `\(\)`→`$…$`、`\[\]`→`$$…$$` LaTeX 逐字符；脚注 `[^note-N]` 键名与 yuanwen 一致。
- 尾部节序：脚注（有则）→ `## 参考文献`（非中文照录不译，中国文献译中文）→ `## 学术工具` → `## 其他网络资源` → `## 相关词条` → `## 致谢`（有则）。
- 版本行：`*首次发表于 YYYY 年 M 月 D 日；YYYY 年 M 月 D 日实质修订。*`（与 baseline pubinfo 一致）。

全部正文段译完、`h/SLUG.md` 完整后：
```
python tools/task_ops.py advance SLUG draft --actor sub-SLUG --evidence "ledger N segs step1+step2; doc written"
```

## 第 3 步 s1（准确性，MTPE 顺序）
对照 `yuanwen/h/SLUG.md` 逐节核销：先幻觉/漏译/增译，再术语漂移（与登记册 grep 一致；新术语写 evidence 候选不写登记册），最后语言欧化。事实（人名/年代/编号）与源核对。
```
python tools/task_ops.py advance SLUG s1 --actor sub-SLUG --evidence "MTPE 幻觉0 漏译0 增译0; 术语核销; 事实核销"
```

## 第 4 步 s2（语言，反欧化）
消除欧化/倒装/死译。跑 `python tools/check_prose.py h/SLUG.md` 看告警，逐条改写或豁免留痕。
```
python tools/task_ops.py advance SLUG s2 --actor sub-SLUG --evidence "check_prose 告警 N: 修 M/豁免 K"
```

## 第 5 步 s3（体例 + 学术门禁）
```
python tools/check_style.py h/SLUG.md
python tools/check_academic.py --docs h/SLUG.md --strict
python tools/check_math.py
```
全 0 后 `python tools/task_ops.py advance SLUG s3 --actor sub-SLUG --evidence "check_style 0; academic 0; math 0"`。学术门禁自动挂钩，未过先修再推。

## 纪律
- 中文弯引号；中西文半角空格；`**中文**` 不加粗用斜体（italic-cjk：中文强调用加粗，拉丁/希腊字母术语保留斜体）；`**` 内侧禁空格；禁 HTML；表格居中。
- 不 push/force；不改其他词条；不动 SUMMARY/登记册（新术语写 evidence）；不改 baseline/en/yuanwen；不造备份；不批量替换。
- **不 git 提交**（主代理收口，避免并发 index.lock）。
- 完成后报告：最终状态、账本段数、s1/s2/s3 问题数、新术语候选、需人工复查项。
- 若中断：`task_ops.py show SLUG` 即断点，账本/文档已增量写回可续。

## 交付物
`h/SLUG.md`（s3 形态）+ `tasks/h/SLUG.ledger.yaml` + `tasks/h/SLUG.json`（state=s3_checked）。
