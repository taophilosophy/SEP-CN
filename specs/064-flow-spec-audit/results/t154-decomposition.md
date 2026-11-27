# T154 拆解：imprecise-probabilities 全流程（方案）

- 日期：2026-11-27
- 依据：`tasks.md` T154（工作包）、`specs/060-six-axis-quality-gates/spec.md` §5.4（本件为“全构件”试金石）、`bin/entry_scale_scan.py`（构件口径）、`rules/04` 状态机、W1（T149–T153）执行模板
- 条目：`i/imprecise-probabilities`（`tasks/i/imprecise-probabilities.json` 状态 `cleared`；`zh/i/imprecise-probabilities.md` 仅存 H1 存根）
- 版本钉：`pubinfo_date: Feb 19, 2019`；`archive_edition: Spring 2019`；`sha256: ae9016a1…0767`
- 原则：T154 只作容器，**不得整体勾选**；拆为 6 个原子任务（T209–T214），从下一可用号顺序分配

## 一、源文实测（2026-11-27，`en/i/imprecise-probabilities.md`）

| 项 | 实测 |
| ---- | ---- |
| 规模 | 119,763 字节／759 行；正文＋尾节 87,082 字符；脚注定义区 29,215 字符 |
| 标题 | H1 1／H2 8／H3 16／H4 2（H1＋8 节＋Acknowledgments） |
| 脚注 | 定义 189 条；正文引用 179 处 |
| 表格 | 1 块（Table 1，Ellsberg 赌局，5 行） |
| 图片 | 2 幅（Figure 1 `two-by-two.png`、Figure 2 `joyces-diagram.png`） |
| 引块 | 15 块／19 行 |
| 列表 | 21 项，全部一级（无嵌套） |
| 公式 | display 4＋行内 366（`en_source_audit`；`check_math` 合计 370、missing 0、unbalanced 6 待人工定性） |
| LaTeX 环境 | 1（`\begin{…}`，在公式块内） |
| 加粗 | 1 处；代码块 0 |
| 尾节 | References（引用注释）／Academic Tools／Other Internet Resources／Related Entries／Acknowledgments |

## 二、14 类构件清单（T154 验收口径）

按 `entry_scale_scan.py` 的 13 个 WEIGHTS 键＋H2 共 14 类；本件命中 **12 类**，与 060 spec “14 类格式构件占 12 类”一致：

| # | 构件类 | 本件 | 计数 | 验收方式 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | H2 节标题 | 有 | 8 | 节集合与 en 一致 |
| 2 | H3+ 子标题 | 有 | 18 | 标题层级与文字一致 |
| 3 | 脚注定义 | 有 | 189 | 定义数／键闭合／无悬空 |
| 4 | 链接 | 有 | 21 | 链接目标与文字照录 |
| 5 | 图片 | 有 | 2 | 路径可解析、alt 与图注齐备 |
| 6 | 表格块 | 有 | 1 | 行列结构完整 |
| 7 | 引块 | 有 | 15 | 引文边界与出处完整 |
| 8 | 列表项 | 有 | 21 | 项数与层级一致 |
| 9 | 嵌套列表 | **无** | 0 | 源文全为一级，译文不得自行制造嵌套 |
| 10 | 行内公式 | 有 | 366 | 定界符配对、数学结构不丢失 |
| 11 | display 公式 | 有 | 4 | 块级定界符与换行照录 |
| 12 | LaTeX 环境 | 有 | 1 | 环境名与配对完整 |
| 13 | 代码块 | **无** | 0 | 不得新增 |
| 14 | 加粗 | 有 | 1 | 强调位置一致 |

> 口径说明：060 spec 的“12 类”沿用旧中文文件扫描值，未给类别定义；上表将其还原为可复算的 14 类清单，并逐类记录命中／未命中。T209 须复核本节计数并把 14 类清单写入证据；后续各站按本表验“构件无丢失”。

## 三、原子任务

| 任务 | 名称 | 范围与手段 | 验收 | 证据 |
| ---- | ---- | ---- | ---- | ---- |
| **T209** | ex-04 源审计 | `en_integrity`（clean 1/1）＋`en_source_audit`（hard 0／warn 10）＋`check_math`（370／missing 0／unbalanced 6）；10 条 warn 与 6 条 unbalanced 逐条回源定性；复核 14 类构件计数；189 脚注键闭合、2 图资产在位；G13 按需 | 候选总数／豁免类计数／逐条结论三段齐全；hard 0 或逐条登记；14 类计数与本文一致；无静默跳过 | `results/t209-review.md` |
| **T210** | tr-02 样章（§1–§1.2） | 导言＋术语表＋重要区分；14,244 源字符、76 行内公式＋1 display、35 脚注引用、1 引块、13 列表项；建账本样章 | 公式与构件按 14 类清单无损；术语先登记后用；账本块数守恒 | `results/t210-review.md` |
| **T211** | tr-02 全量 | §2–§4＋尾节四件套＋189 脚注定义；分 3 批 checkpoint（§2／§3／§4＋尾节）；全文账本 `tasks/i/imprecise-probabilities.ledger.yaml`；`project_spec`／`pe` 字段补齐 | 全文入库；189 脚注定义闭合；4 display＋366 行内公式不丢失；2 图 1 表结构完整；账本守恒；`advance --step tr-02` 通过 | `results/t211-review.md` |
| **T212** | tr-03／tr-04 校次链 | 一校逐节核销（对照 en）；二校语体与反欧化（`check_prose` 告警清零或逐条豁免） | 账本守恒；残留外文 0；两站 `check_all` 全绿 | `results/t212-tr03.md`、`results/t212-tr04.md` |
| **T213** | rv 链 | rv-01 三轴（术语／体例／勘误）→ rv-02 全局一致性 → rv-03–08 六轴（q1 引文→q2 逻辑→q3 语法→q4 语域→q5 计量→q6 标点）→ rv-09 体例终校 | 各轴凭据落 `state/axis/`；`--gate` 0 或逐条豁免；rv-09 `check_style` 0 | `results/t213-rv01.md`…`t213-rv09.md` |
| **T214** | sg 链 | sg-01 初审（Verity）、sg-02 复审（Coherence）、sg-03 终审 | sg-01／sg-02 问题单无 Critical／Major；sg-03 须用户 `--mandate`，未指定则止于 `sg-02_checked` | `results/t214-sg01.md`、`t214-sg02.md`、`t214-sg03.md` |

## 四、执行顺序与出口

```
T209（ex-04）→ T210（样章）→ T211（全量）→ T212（tr-03／tr-04）
→ T213（rv-01／rv-02／六轴／rv-09）→ T214（sg-01／sg-02；sg-03 用户 mandate）
```

- 状态机禁跳步：每站完成后 `task_ops.py advance`，证据写入对应 `results/` 文件。
- 构件验收以本文 §二 的 14 类清单为唯一口径，T209 复核后如有修订，须在证据中写明差异与理由。
- sg-03 不因试金石批准自动获得授权（060 spec E2E 口径注）；未获 mandate 时本件停 `sg-02_checked`。
- T154 容器保持未勾选，完成由 T209–T214 派生；6 项全部完成且本件 `done` 后，T154 仅在“完成由子项派生”的意义上关闭，不整体勾选。

**状态**：方案落地；下一步 T209（ex-04 源审计）。
