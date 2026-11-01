# K 批子代理统一作业指令（每个子代理读本文件一次，再按 SLUG 执行）

> 本文件由主会话生成，供每个 K 批子代理读取。每个子代理只处理**一个**词条（SLUG 在启动参数中给定）。任务边界、验收判据、体例纪律详见 `specs/005-translation-campaign/k-batch-subagent-protocol.md`，本文件是其可执行的操作细化。

## 0. 你的任务

处理词条 **SLUG**（K 批）。完成 retranslate 状态机 `clear → draft → s1 → s2 → s3`，最终状态 `s3_checked`。**不得**执行 r1/r2/r3/done（那是主代理的独立复核）。

**范围**：只译主文件 `k/SLUG.md`。若正文引用补充材料（链接形如 `<slug>.<x>.md`），保留链接并中译链接文字，**不要**创建或翻译补充材料文件本身（另行建任务，先例 `s/spacetime-holearg`）。

## 1. 只读输入（路径已定）

| 用途 | 路径 |
| ---- | ---- |
| 英文源（翻译底稿） | `yuanwen/k/SLUG.md` |
| 原始 HTML（可疑回源） | `en/SLUG/index.html` |
| 术语登记册 | `yi-zhe-shuo-ming.md` |
| 人名登记册 | `ren-ming-biao.md` |
| 翻译模板（元素映射+骨架） | `specs/005-translation-campaign/fan-yi-mu-ban.md` |
| 体例规则 | `rules/02-style.md` |
| 学术规范 | `rules/07-academic-norms.md` |

从 `SUMMARY.md` 找该词条行取 H1 文字（形如 `* [中文名 English-name (Authors)](k/SLUG.md)`，去掉前导 `*` 与 `[`、尾部的 `](...)`）。从 `baseline/entries.json` 取 `pubinfo_date` / `archive_edition`（版本钉）。

## 2. 第一步：清空

```sh
cd /d/SEP-CN
python tools/task_ops.py clear SLUG
```

本批任务此前已建齐并 cleared；若 clear 报错（可能已在别处进行），读错误信息，不要强推——改用 `python tools/task_ops.py show SLUG` 确认断点后续作。

## 3. 第二步：初译 draft（最关键，占 80% 工作量）

以 `yuanwen/k/SLUG.md` 为**唯一底稿**，从头逐节翻译。零信任：**不参考** `k/SLUG.md` 现有内容（那是存根，清空后只剩 H1），不参考任何第三方译文。

**段落账本**：建 `tasks/k/SLUG.ledger.yaml`，格式与 C 批账本一致（见 `tasks/c/cockburn.ledger.yaml` 范例）：

```yaml
version: 1
slug: SLUG
segments:
  - id: 1
    source: |-      # 英文源段落（逐字符）
    step1: |-       # 第一步：忠实初译
    step2: |-       # 第二步：语言优化（draft 成稿对象）
  - id: 2
    ...
```

**反思式两步强制（ADR-0021）**：每段必须产出 step1（忠实初译）与 step2（语言优化）双版并都留档。step2 为 draft 成稿对象；step1 为一校对照底（润色引入的幻觉/增译/漂移以 step1 对照核销）。

**增量写回保底**：每完成 3–5 段就写一次账本文件（防止中断丢内容）。段 id 与源逐段对位（从 `yuanwen/k/SLUG.md` 按空行/段落结构切分，与 C 批账本同法）。

**标记守恒**：markdown 强调、链接、脚注键（`[^note-N]`）、数学定界符的计数与位置，回写前后守恒；不守恒该段废稿重做。

**元素映射（fan-yi-mu-ban.md §2）要点**：
- H1 = SUMMARY 条目文字（`# 中文名 English-name (Authors)`）。
- 版本行：`*首次发表于 YYYY 年 M 月 D 日；YYYY 年 M 月 D 日实质修订。*`（日期与 baseline pubinfo 一致；无修订则止于首次发表句）。
- 编号章节：`## 1 中文名`（保留编号、去掉英文句点）；`1.1` → `### 1.1 中文名`；不得跳级。
- 行内引用组 `(Author year, p. X)` 原样保留；Ak./AA（康德）、DK 等古典编号照录。
- 引块 `>` 引用块；图 `![图注](../yuanwen/assets/SLUG/<文件名>)`；表格 `:---:` 居中、紧凑风格。
- 数学 `\(\)`→`$…$`、`\[\]`→`$$…$$`，LaTeX 逐字符保留；`<sub>/<sup>`→`_{x}`/`^{x}`。
- 脚注 `[^note-N]` 键名与 yuanwen 逐字符一致；文末 `## 脚注` 节。
- 补充材料引用链接保留：`（见[补充材料标题中译](SLUG.<x>.md)）`，链接目标文件名不改、不建文件。
- 尾部节序：脚注（有则）→ `## 参考文献` → `## 学术工具` → `## 其他网络资源` → `## 相关词条` → `## 致谢`（有则）。

**draft 完成**：账本全部段落双版齐备、`k/SLUG.md` 已写入 step2 拼合稿、`task_ops.py advance SLUG draft --actor sub-SLUG --evidence "ledger: N segments step1+step2; H1=<title>"`。

## 4. 一校 s1（准确性，MTPE 顺序）

对照 `yuanwen/k/SLUG.md` 逐节核销，**顺序（ADR-0020）：先查幻觉/漏译/增译 → 再查术语漂移 → 最后处理语言欧化**。

- 幻觉/漏译/增译：每段与 step1 对照，确认译文忠实、无凭空添加、无漏句。
- 术语漂移：正文用词与 `yi-zhe-shuo-ming.md`、`ren-ming-biao.md` 一致（grep 核对）。新术语写进 evidence 候选（不直接写登记册，主代理收口）。
- 事实错误：人名、年代、版本号、编号逐一与源核对。

`task_ops.py advance SLUG s1 --actor sub-SLUG --evidence "MTPE 对照: 幻觉0 漏译0 增译0; 术语漂移 核销清单; 事实 核销清单"`

## 5. 二校 s2（语言，反欧化）

消除欧化句/倒装/死译，打磨口吻。跑 `python tools/check_prose.py k/SLUG.md` 看告警，逐条改写或豁免留痕（豁免写进 evidence）。参考 rules/02 反欧化条款（长句拆分、被动句、弱动词、定语链、“们”、冠词存在句、指代显化）。

`task_ops.py advance SLUG s2 --actor sub-SLUG --evidence "check_prose 告警 N 条: 修 M 条/豁免 K 条; 逐句回核"`

## 6. 三校 s3（体例 + 学术门禁）

```sh
python tools/check_style.py k/SLUG.md          # 0 问题
python tools/check_academic.py --docs k/SLUG.md --strict   # 0 硬错误
python tools/check_math.py                      # 全局数学平衡（确认本词条无 missing/unbalanced）
```

- 中文弯引号、中西文半角空格、`**` 星号内侧禁空格、禁止 HTML、表格居中、书名号内中英空格。
- 参考文献：非中文条目照录不译；**中国文献条目（古今）译为中文**（ADR-0011）；文首斜体说明行。
- `task_ops.py advance SLUG s3 --actor sub-SLUG --evidence "check_style 0; check_academic --strict 0; check_math 0"`（**学术门禁自动挂钩**，未过则 advance 被拒——先修再推）。

## 7. 完成与报告

- 最终状态必须 `s3_checked`（`python tools/task_ops.py show SLUG` 验证）。
- **不 git 提交、不 push**（主代理收口统一提交，并发 git 会 index.lock 竞争）。
- 向主代理报告：状态、账本段数、发现的问题、新术语候选、是否需人工复查。

## 8. 不得为

不 push/force；不改其他词条；不动 SUMMARY/登记册（新术语候选写 evidence）；不改 `baseline/`、`en/`、`yuanwen/`；不造备份；不批量替换；不“跑格式化工具代替判断”。

## 9. 若遇到困难

- 某段源文本无法理解：回 `en/SLUG/index.html` 核对原始，确认不是镜像缺陷；仍不解则记录进报告，跳到下一段，不要卡死。
- 中途中断：重跑 `task_ops.py show SLUG` 即断点；账本已增量写回，可续。
- 连续多段失败：如实报告，不要伪造完成。
