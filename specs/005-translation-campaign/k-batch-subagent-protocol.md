# K 批 2 路子代理滚动协议（长线任务）

**日期**：2026-11-02 | **效力**：本会话子代理滚动执行 K 组 36 词条 retranslate 任务
**上位依据**：`rules/04-translation-workflow.md`（状态机）、`rules/02-style.md`（体例）、`rules/03-terminology.md`（术语）、`rules/07-academic-norms.md`（学术规范）、`specs/005-translation-campaign/fan-yi-mu-ban.md`（模板 v1.2）、`j-batch-subagent-protocol.md`（母协议，本文件为其 K 化变体）
**规模裁定**：沿用用户 2026-11-02 裁定 **2 路并发**（J 批实测并发额度被并行会话共享挤占，38 路仅 13 路存活），2 路滚动（完成一补一，fresh 模式重派），直至批次收口。

## 1. 子代理任务边界

* 每个子代理负责 **一条词条** 的 retranslate 任务，状态机推进至 **s3_checked**。
* 子代理执行步骤：`clear → draft → s1 → s2 → s3`（初译 + 一校 + 二校 + 三校）。
* 主代理（本会话）统一执行 `r1 → r2 → r3 → done`（独立复核，满足 ISO 17100 复核独立性——r1–r3 由初译 actor 以外的会话执行）。
* 子代理**不得**执行 `r1/r2/r3/done`；主代理**不得**代做 `draft/s1/s2/s3`。

## 2. 任务范围（K 批特别注记：补充材料不在本任务内）

* 任务 JSON 的 `zh_doc` 只有主文件 `k/<slug>.md`；**本波范围 = 主文件**。
* K 批 4 词条带 15 个补充材料碎片（`kant-judgment` 5 件、`kochen-specker` 6 件、`kant-transcendental-idealism` 3 件、`korean-confucianism` 1 件），按模板 §2 条 19 为独立文件、另行建任务（先例：`s/spacetime-holearg` done，主文保留补充材料链接，碎片文件另行处理）。
* 子代理翻译主文时：正文引用补充材料的链接**保留**，写成 `（见[链接文字中译](<slug>.<x>.md)）`，链接目标文件名与 yuanwen 一致；**不要**去创建或翻译 `<slug>.<x>.md` 本身。
* K 批 6 词条含图（`yuanwen/assets/` 有资产目录：`kant-religion`、`kant-spacetime`、`kepler`、`knowledge-how`、`kochen-specker`、`korean-philosophy`），图片按模板 §2 条 9/10 映射：`![图注](../yuanwen/assets/<slug>/<文件名>)`，图注译出、reprinted with permission 标来源。

## 3. 子代理输入（只读）

| 输入 | 路径 | 用途 |
| ---- | ---- | ---- |
| 英文源 | `yuanwen/k/<slug>.md` | 翻译底稿（逐字符镜像） |
| 原始 HTML | `en/<slug>/index.html` | 可疑处回源核对（零信任） |
| 版本钉 | `baseline/entries.json` | pubinfo 日期/存档版/SHA-256 |
| SUMMARY 标题 | `SUMMARY.md` | H1 条目文字（中文名 English-name (Authors)） |
| 术语登记册 | `yi-zhe-shuo-ming.md` | 术语译法单一事实源 |
| 人名登记册 | `ren-ming-biao.md` | 人名译法单一事实源 |
| 翻译模板 | `specs/005-translation-campaign/fan-yi-mu-ban.md` | §2 元素映射、§4 骨架 |
| 体例规则 | `rules/02-style.md` | 引号/空格/斜体/加粗/表格 |
| 学术规范 | `rules/07-academic-norms.md` | 版本事实/引文/参考文献/结构 |

## 4. 子代理输出（可写）

| 输出 | 路径 | 说明 |
| ---- | ---- | ---- |
| 译文 | `k/<slug>.md` | 最终译文（s3 后形态） |
| 段落账本 | `tasks/k/<slug>.ledger.yaml` | step1+step2 双版（ADR-0021 反思式两步） |
| 任务状态 | `tasks/k/<slug>.json` | 用 `task_ops.py advance` 推进 |

## 5. 子代理操作序列（严格）

1. **读方向**：读 `yuanwen/k/<slug>.md`、`SUMMARY.md` 中该词条行、`baseline/entries.json` 中该 slug 条目。
2. **清空**：`python tools/task_ops.py clear <slug>`（基线哈希门禁自动检查；仅保留 H1）。本批任务已建齐并 cleared；若 clear 报错说明已在别处进行，读错误信息不强推，`show` 确认断点续作。
3. **初译（draft）**：按 `fan-yi-mu-ban.md` §2 元素映射 + §4 骨架，以英文源为唯一底稿，从头翻译。零信任——不参考任何既有中文译文。**每段产出 step1（忠实初译）与 step2（语言优化）双版入账本**（ADR-0021 强制）；每 3–5 段增量写回账本防中断丢失。
4. **一校（s1，准确性）**：对照 `yuanwen/k/<slug>.md` 逐节核销：漏译、错译、事实错误（人名、年代、编号）。**MTPE 顺序（ADR-0020）：先查幻觉/漏译/增译，再查术语漂移，最后处理语言欧化。**
5. **二校（s2，语言）**：消除欧化句/倒装/死译，打磨口吻（rules/02 反欧化条款）。跑 `python tools/check_prose.py k/<slug>.md` 查看告警，逐条改写或豁免留痕。
6. **三校（s3，体例）**：`python tools/check_style.py k/<slug>.md`、`python tools/check_academic.py --docs k/<slug>.md --strict`、`python tools/check_math.py`。**s3 advance 时学术门禁自动挂钩**（task_ops 内部执行 check_academic --strict，未过则拒绝 advance）。
7. **提交**：主代理统一收口提交。子代理**不 git 提交、不 push**（并发 git 会 index.lock 竞争；由主会话收口）。

## 6. 子代理必须遵守的体例要点（rules/02，违规即返工）

* 中文弯引号 `“ ”` `‘ ’`；禁止英文直引号、直角引号（U+300C–300F）、全角直引号。
* 中英文、中文与数字之间半角空格；**书名号内中英混排同样加空格**。
* `**中文强调**` 用加粗，不用斜体 `*中文*`（italic-cjk）；拉丁/希腊/希伯来字母术语保留斜体。
* `**` 星号内侧禁空格。
* 禁止任何 HTML 语法；禁止 AsciiDoc 残留；表格居中 `:---:`、紧凑风格。
* 数学定界符 `$…$`/`$$…$$` LaTeX 逐字符保留；`<sub>/<sup>` 转 `_{x}`/`^{x}`。
* 引用组 `(Author year, p. X)` 原样保留（作者姓、年份、页码不译）；Ak./AA 版本编号（康德）、DK 编号等古典编号照录。
* 参考文献非中文条目照录不译；**中国文献条目（古今）译为中文**（ADR-0011）；文首斜体说明行 `*非中文文献从原文照录，不作翻译；中国文献译为中文。*`。
* 参考文献节标题 `## 参考文献`；脚注 `[^note-N]` 键名与 yuanwen 逐字符一致。
* 尾部节序固定：脚注（有则）→ 参考文献 → 学术工具 → 其他网络资源 → 相关词条 → 致谢（有则）。
* 版本事实行：`*首次发表于 YYYY 年 M 月 D 日；YYYY 年 M 月 D 日实质修订。*`（日期与 baseline pubinfo 一致）。
* 学术工具三行链接原样（archinfo/InPhO/PhilPapers）。

## 7. 术语纪律（rules/03）

* 新术语**先登记 `yi-zhe-shuo-ming.md` 后使用**；登记格式五列（原文/译法/首现/依据/裁定日期）。
* 登记依据档位：知网系权威源 → 权威译本通行译法 → 学界惯例；**禁用维基百科译名**；查无可查保留英文并登记。
* 人名以 `ren-ming-biao.md` 为准：有通行汉名用汉译并首次括注原文；无通行汉名保留英文。
* 同一词条内锁定主形（ADR-0020），不混形。
* **滚动并发下术语登记由主代理统一收口**：子代理发现新术语写进 evidence（候选），主代理复核后统一登记，避免并发写登记册冲突。

## 8. 复核独立性（rules/04）

* 子代理做 draft→s3，主代理做 r1→r3→done。r1–r3 由初译 actor 以外的会话执行，满足 ISO 17100（c 批裁定的两波模式）。
* 主代理在子代理完成若干词条后统一复核，天然满足冷置。

## 9. 子代理验收判据（s3 达成条件）

* `task_ops.py show <slug>` 状态 = `s3_checked`。
* `k/<slug>.md` 完整（六节全译 + 脚注译出 + 文献照录 + 工具/其他/相关节）。
* `check_style` 0 问题；`check_academic --strict` 0 硬错误；`check_math` 0。
* 任务 JSON 的 steps 含 clear/draft/s1/s2/s3 各步 evidence（可复核）。
* 账本 `tasks/k/<slug>.ledger.yaml` 段落数与逐段身份与源一致，step1+step2 双版齐备。

## 10. 中断与续作

* 任何一步中断，重跑 `task_ops.py show <slug>` 即断点；工具全部幂等。
* 子代理完成 s3 后**不提交**，主代理收口时统一提交，避免并发 git 竞争。

## 11. 子代理不得为

* 不 push、不 force、不改其他词条、不动 SUMMARY/登记册（新术语候选写 evidence）。
* 不改 `baseline/`、`en/`、`yuanwen/`（只读）。
* 不造备份文件；不批量替换；不“跑格式化工具代替判断”。

## 12. 长线任务与监控（本会话强化）

* **滚动**：**2 路并发（用户 2026-11-02 裁定沿用）**，完成一路补一路；重派一律 fresh 模式（重译，产出率高于 resume，见 c 批实测）；派发顺序按 `yuanwen/k/<slug>.md` 字节升序（短词条先验证管线）。
* **长线**：子代理以 `run_in_background: true` 运行，主代理不阻塞等待（避免死等）。
* **监控**：主代理周期性运行 `python specs/005-translation-campaign/bin/k_batch_monitor.py`（聚合进度、断点凭证、停滞检测）；超时/浅工（只写 H1 存根）标记重试。
* **收口**：主代理统一执行 git add/commit（每词条一行中文信息），r1→r3→done 独立复核。
