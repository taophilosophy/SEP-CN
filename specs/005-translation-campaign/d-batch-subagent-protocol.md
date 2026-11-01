# D 批 40 路子代理滚动协议

**日期**：2026-11-01 | **效力**：本会话 40 路子代理滚动执行 D 组 92 词条 retranslate 任务
**上位依据**：`rules/04-translation-workflow.md`（状态机）、`rules/02-style.md`（体例）、`rules/03-terminology.md`（术语）、`rules/07-academic-norms.md`（学术规范）、`specs/005-translation-campaign/fan-yi-mu-ban.md`（模板 v1.2）

## 1. 子代理任务边界

* 每个子代理负责 **一条词条** 的 retranslate 任务，状态机推进至 **s3_checked**。
* 子代理执行步骤：`clear → draft → s1 → s2 → s3`（初译 + 一校 + 二校 + 三校）。
* 主代理（本会话）统一执行 `r1 → r2 → r3 → done`（独立复核，满足 ISO 17100 复核独立性——r1–r3 由初译 actor 以外的会话执行）。
* 子代理**不得**执行 `r1/r2/r3/done`；主代理**不得**代做 `draft/s1/s2/s3`。

## 2. 子代理输入（只读）

| 输入 | 路径 | 用途 |
| ---- | ---- | ---- |
| 英文源 | `yuanwen/d/<slug>.md` | 翻译底稿（逐字符镜像） |
| 原始 HTML | `en/<slug>/index.html` | 可疑处回源核对（零信任） |
| 版本钉 | `baseline/entries.json` | pubinfo 日期/存档版/SHA-256 |
| SUMMARY 标题 | `SUMMARY.md` | H1 条目文字（中文名 English-name (Authors)） |
| 术语登记册 | `yi-zhe-shuo-ming.md` | 术语译法单一事实源 |
| 人名登记册 | `ren-ming-biao.md` | 人名译法单一事实源 |
| 翻译模板 | `specs/005-translation-campaign/fan-yi-mu-ban.md` | §2 元素映射、§4 骨架 |
| 体例规则 | `rules/02-style.md` | 引号/空格/斜体/加粗/表格 |
| 学术规范 | `rules/07-academic-norms.md` | 版本事实/引文/参考文献/结构 |

## 3. 子代理输出（可写）

| 输出 | 路径 | 说明 |
| ---- | ---- | ---- |
| 译文 | `d/<slug>.md` | 最终译文（s3 后形态） |
| 任务状态 | `tasks/d/<slug>.json` | 用 `task_ops.py advance` 推进 |

## 4. 子代理操作序列（严格）

1. **读方向**：读 `yuanwen/d/<slug>.md`、`SUMMARY.md` 中该词条行、`baseline/entries.json` 中该 slug 条目。
2. **清空**：`python tools/task_ops.py clear <slug>`（基线哈希门禁自动检查；仅保留 H1）。
3. **初译（draft）**：按 `fan-yi-mu-ban.md` §2 元素映射 + §4 骨架，以英文源为唯一底稿，从头翻译。零信任——不参考任何既有中文译文。
4. **一校（s1，准确性）**：对照 `yuanwen/d/<slug>.md` 逐节核销：漏译、错译、事实错误（人名、年代、编号）。**MTPE 顺序（ADR-0020）：先查幻觉/漏译/增译，再查术语漂移，最后处理语言欧化。**
5. **二校（s2，语言）**：消除欧化句/倒装/死译，打磨口吻（rules/02 反欧化条款）。跑 `python tools/check_prose.py <slug>` 查看告警，逐条改写。
6. **三校（s3，体例）**：`python tools/check_style.py <slug> --strict`、`python tools/check_academic.py --docs d/<slug>.md --strict`、`python tools/check_math.py <slug>`。**s3 advance 时学术门禁自动挂钩**（task_ops 内部执行 check_academic --strict，未过则拒绝 advance）。
7. **提交**：`git add` 只加 `d/<slug>.md` + `tasks/d/<slug>.json`，中文一行提交信息（如 `d 批 draft-s3 <slug> 初译三校`）。**不 push。**

## 5. 子代理必须遵守的体例要点（rules/02，违规即返工）

* 中文弯引号 `“ ”` `‘ ’`；禁止英文直引号、直角引号（U+300C–300F）、全角直引号。
* 中英文、中文与数字之间半角空格；**书名号内中英混排同样加空格**（《C 程序设计语言》）。
* `**中文强调**` 用加粗，不用斜体 `*中文*`（italic-cjk）；拉丁/希腊/希伯来字母术语保留斜体。
* `**` 星号内侧禁空格（`** 内容 **` 永不渲染）。
* 禁止任何 HTML 语法；禁止 AsciiDoc 残留；表格居中 `:---:`、紧凑风格。
* 数学定界符 `$…$`/`$$…$$` LaTeX 逐字符保留；`<sub>/<sup>` 转 `_{x}`/`^{x}`。
* 引用组 `(Author year, p. X)` 原样保留（作者姓、年份、页码不译）。
* 参考文献非中文条目照录不译；**中国文献条目（古今）译为中文**（ADR-0011）；文首斜体说明行 `*非中文文献从原文照录，不作翻译；中国文献译为中文。*`。
* 参考文献节标题 `## 参考文献`；脚注 `[^note-N]` 键名与 yuanwen 逐字符一致。
* 尾部节序固定：脚注（有则）→ 参考文献 → 学术工具 → 其他网络资源 → 相关词条 → 致谢（有则）。
* 版本事实行：`*首次发表于 YYYY 年 M 月 D 日；YYYY 年 M 月 D 日实质修订。*`（日期与 baseline pubinfo 一致）。
* 学术工具三行链接原样（archinfo/InPhO/PhilPapers）。

## 6. 术语纪律（rules/03）

* 新术语**先登记 `yi-zhe-shuo-ming.md` 后使用**；登记格式五列（原文/译法/首现/依据/裁定日期）。
* 登记依据档位：知网系权威源 → 权威译本通行译法 → 学界惯例；**禁用维基百科译名**；查无可查保留英文并登记。
* 人名以 `ren-ming-biao.md` 为准：有通行汉名用汉译并首次括注原文；无通行汉名保留英文。
* 同一词条内锁定主形（ADR-0020），不混形。

## 7. 复核独立性（rules/04）

* 子代理做 draft→s3，主代理做 r1→r3→done。r1–r3 由初译 actor 以外的会话执行，满足 ISO 17100。
* 单会话作业时终审前须冷置——主代理在子代理完成若干词条后统一复核，天然满足冷置。

## 8. 子代理验收判据（s3 达成条件）

* `task_ops.py show <slug>` 状态 = `s3_checked`。
* `d/<slug>.md` 完整（六节全译 + 脚注译出 + 文献照录 + 工具/其他/相关节）。
* `check_style --strict` 0 问题；`check_academic --strict` 0 硬错误；`check_math` 0。
* 任务 JSON 的 steps 含 clear/draft/s1/s2/s3 各步 evidence（可复核）。

## 9. 中断与续作

* 任何一步中断，重跑 `task_ops.py show <slug>` 即断点；工具全部幂等。
* 子代理完成 s3 后**必须提交**，避免主代理复核时读到未提交的半成品。

## 10. 子代理不得为

* 不 push、不 force、不改其他词条、不动 SUMMARY/登记册（除非登记自己词条的新术语，且只加行）。
* 不改 `baseline/`、`en/`、`yuanwen/`（只读）。
* 不造备份文件；不批量替换；不"跑格式化工具代替判断"。
