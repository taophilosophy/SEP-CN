# 044 — B0/B1 前置基线：HTML 模板一致性与 markdown 跨词条一致性的公理化充分性证明

**版本** v1.0 ｜ **状态** 方案（待批）｜ **日期** 2026-11-18 ｜ **权威** 用户指令“批准落地实施，先出方案书，进行公理化充分形式化证明，允许随机选取 5 个词条进行转换”

## 0. 方向声明（rules/08）

- **目标**：把 B0（HTML 模板一致性）与 B1（markdown 跨词条一致性）确立为翻译的**前置基线**，给出公理化的充分性形式证明，并以随机 5 词条试金石验证判据可执行、可证伪。
- **非目标**：本方案**不**实施全库遍历（那是 B0/B1 的**执行批次**，另立）；不改 `en/` 任何字节；不重译、不改译文措辞；不改 `yuanwen.py` 转换器；不动状态机。
- **验收判据**：①方案书成文且判据可执行；②判定器经 3 个负向样本证明可证伪；③定理 T1（充分性）、T2（可判定）、T4（证伪可用）陈述完整、T3（边界）明确；④5 词条试金石全跑、结论有据；⑤`check_all` 全绿、提交推送、`origin/main..main` 为空。

## 1. 判据形式化定义

### 1.1 B0 — HTML 模板一致性（单件谓词，10 项）

定义域：`en/<slug>/index.html` 的字节内容。B0 为**结构契约** 4 项与**可解析性** 6 项的合取：

| 谓词 | 判据 | 依据 |
| ---- | ---- | ---- |
| `marker` | `<!-- BEGIN ARTICLE HTML -->` 与 `<!-- END ARTICLE HTML -->` 均命中 | `parser.HEAD_RE`/`TAIL_RE` |
| `pubinfo` | `First published …` 出版信息可解析 | `parser.PUBINFO_RE` |
| `title` | `citation_title` 元数据命中 | `parser.META_RE` |
| `section` | 至少一个带节号（`N[.M[.K]]`）的 h2 分节 | `parser.parse_entry` blocks |
| `no_truncation` | 含 `</html>`（无截断） | `en_source_audit._check_page` |
| `no_error_page` | 页头无错误/风控页标记 | `en_source_audit.MARKERS` |
| `math_delim` | `\(`/`\)` 与 `\[`/`\]` 各自配对 | `en_source_audit._check_math` |
| `math_brace` | 公式内 TeX 花括号平衡 | 同上 |
| `table_row` | 每个 `<table>` 含 `<tr>` | `en_source_audit._check_tables` |
| `img_src` | 每个 `<img>` 有 `src` | `en_source_audit._check_images` |

**B0(s) ⟺ 上述 10 谓词全真。** 引用闭包（死链、资产缺失）属 `en_integrity` 包完整性面，**不并入 B0**（B0 只判“该 HTML 本身符不符合模板、可不可解析”，不判“它指向的东西在不在包内”）。

### 1.2 B1 — markdown 保真与跨词条一致（单件谓词，2 项）

定义域：`yuanwen/<letter>/<slug>.md` 与其对应 `en` 源。B1 为两个既有不变量（specs/039）：

| 谓词 | 判据 | 依据 |
| ---- | ---- | ---- |
| `pin`（I2 重放等值） | `md sha256 == 登记 yuanwen.sha256` 且 `en sha256 == 登记 source_sha256` | `check_yuanwen_fidelity.check_pins` |
| `token`（I3 词元流等值） | 两侧词元多重集 diff 为空（转换器白名单外） | `check_yuanwen_fidelity.multiset_diff` |

**B1(s) ⟺ I2(s) ∧ I3(s)。** “跨词条一致”不是逐件互比，而是**由 B0 与转换确定性推出**（见 T1）。

## 2. 公理化

### 2.1 符号

- `E`：全部词条集合（当前 `baseline/entries.json` 1,872 件）。
- `B0 : E → {真,假}`、`B1 : E → {真,假}`：上节定义的谓词。
- `convert : en → yuanwen`：`tools/yuanwen.py` 的确定性转换函数（含补丁池 `apply_en_patches`）。
- `S`：SEP 模板的结构元素集（BEGIN/END 标记、pubinfo、citation、节、图、脚注、补充材料——`parser.py` 契约）。

### 2.2 公理

- **A1（确定性）**：`convert` 是纯函数——同源 HTML（含同一补丁）必得同一 md；结构元素集 `S` 固定映射到统一 md 契约（脚注 `[^note-N]`、图片 `../assets/<slug>/`、节 `## N. 标题`、参考文献转脚注定义）。
- **A2（补丁守恒）**：补丁池只含格式层（准入谓词 C2），应用命中计数硬校验，失配即硬失败——不引入文字漂移。
- **A3（冻结）**：`en/` 字节 == 原始钉（ADR-0062/0045），是 B0 判定的稳定输入。

### 2.3 定理

**T1（充分性）**：若 ∀s∈E，B0(s)=真，且 A1、A2、A3 成立，则 ∀s∈E，B1(s)=真（即跨词条一致）。

> 证明：B0 保证每个 `en_s` 都含 `S` 的全部结构元素且可解析（无截断、公式配平、表格配平）；A3 保证输入稳定；A2 保证补丁不引入漂移；A1 保证 `convert` 对同一结构输入输出同一 md 形状。故所有 md 均来自同一契约 `S→md` 的确定性像，逐件 B1 成立，且形状同源 ⇒ 跨词条一致。∎

**T2（可判定）**：B0 与 B1 均为有限可判定谓词，全库遍历复杂度 `O(Σ_s |en_s| + |md_s|)`。

> 证明：B0 由 10 个正则/线性解析判定组成，每个 `O(|html|)`；B1 由哈希比对 + 词元多重集 `O(|md|)`。∎

**T3（边界，不可自证）**：`S` 是否穷尽 SEP 模板的**全部合法变异**不可自证——系统能证明“已登记的结构元素无一落空”，不能证明“没有第 11 种模板变异”。此为相对完备边界（同 specs/043 §6.4，Cook 1978；Zave & Jackson 1997）。

**T4（证伪可用）**：若 ∃s∈E，B0(s)=假，则 B1(s) 的一致性保证失效（该件 md 可能偏离契约）。

> 证明：B0=假 ⇒ 该 HTML 缺失某契约元素或含硬缺陷；A1 只保证“同一结构输入”的输出稳定，不保证“坏输入”的输出形状仍在契约内。∎

## 3. 试金石结果（5 词条，随机、可复现，已实跑）

- 抽样：固定种子 `random.Random(20261118)` 从 1,872 件可抓词条抽 5 件：`delmedigo`、`genotype-phenotype`、`phil-bio-latin-america`、`spinoza-modal`、`williams-bernard`。
- 结果：**B0 通过 4/5，B1 通过 5/5**（`results/trial-5.json` 机读在案）。
- **真实发现**：`phil-bio-latin-america` 的 B0 `math_delim` 失败，根因是**上游文字层误植**——正文 `Kuhn (1962 [1970\)` 的右方括号 `]` 被误写为 LaTeX 闭定界符 `\)`（该文件仅此 1 处、无对应 `\(`）。处置出口＝全局勘误表＋中文译注（非补丁池，非格式层）。
- **意义**：随机 5 词条即命中 1 处上游疏漏（20%），而当前 `s0` 仅覆盖 20/1,872、补丁池仅 3 条——**B0 全库遍历的必要性被试金石直接证实**，存量上游疏漏远未被发现。

## 4. 落点

- `specs/044-b0b1-baseline/spec.md`：本方案。
- `specs/044-b0b1-baseline/bin/verify_b0b1.py`：可执行判定器（B0 10 谓词 + B1 2 不变量，可注入路径，`--neg` 负向测试）。
- `specs/044-b0b1-baseline/results/trial-5.json`：5 词条试金石机读结果。
- 后续（不在本方案）：B0 全库遍历 = `specs/036` 存量补课的正式化；B1 全库遍历 = `check_yuanwen_fidelity --gate --deep` 的常态化。

## 5. 机检定位（ADR-0070，2026-11-18 补）

本判定器是**形式初筛**，不是语义裁判（试金石铁证：`phil-bio-latin-america` 的 `]→\)` 误植 B0 抓、B1 漏——B1 机检全绿却漏上游源本身的错）。如实标注覆盖度：

- B0 十谓词判“形式可解析”，不判“内容对”（盲区见 ADR-0070 附录 1–5）；
- B1 的 I2 是“md==convert(en)”的**自证**（转换器 bug 两边都错则不见），I3 多重集忽略顺序、320 件 math-asymmetric 判据不适用＝未验证（盲区 6–9）。

**“机检 0 问题”不得表述为“已验证”**；B0/B1 全库机检的价值是把 1,872 件筛到少数可疑件，缩小抽样人审（5% 深读）与全量人审的范围。
