# T211 证据：imprecise-probabilities tr-02 全量

- 日期：2026-11-27
- 任务：T211（T154 拆站第 3 项）；状态推进目标 `tr-02_checked`
- 条目：`i/imprecise-probabilities`；源文 `en/i/imprecise-probabilities.md`（119,763 字节／759 行）
- 译文：`zh/i/imprecise-probabilities.md`（764 行／106,987 字节／18,478 汉字）
- 账本：`tasks/i/imprecise-probabilities.ledger.yaml`（169 段＝165 body＋4 oir）
- 方案：`results/t154-decomposition.md` §三

## 一、范围与规模

| 项 | 源文 | 译文 |
| ---- | ---- | ---- |
| 正文块（按空行切分，§1–§4） | 165 | 165（逐块对应） |
| 汉字 | — | 18,478 |
| H2 | 8 | 8（另加尾节四件套＋脚注＋译者注释） |
| 脚注定义 | 189 | 189（逐条照录，键集合相等） |
| 脚注引用 | 179 处／137 键 | 179 处／137 键 |
| 图片 | 2（Figure 1／2） | 2（alt 已译，路径 `../../assets/imprecise-probabilities/`） |
| 表格 | 1 块（Table 1，5 行×4 列） | 1 块（结构完整） |
| display 公式 | 4 | 4（逐字符照录） |
| 行内公式 | 366（`en_source_audit`） | 见 §二 守恒说明 |
| 尾节 | References／Academic Tools／OIR／Related Entries／Acknowledgments | 参考文献／学术工具／其他网络资源／相关词条／致谢（canonical 序） |

## 二、公式守恒说明

以 `$…$`／`$$…$$` 抽取正文公式标记比对：源 360、译 350，差额 10 处已逐项归因：

| 差额 | 处数 | 处置 |
| ---- | ---- | ---- |
| 孤立 `$\Omega$` | 8 | 按 ADR-0049 A 类转 `*Ω*`（正文文字） |
| 孤立 `$\mu$` | 2 | 按 ADR-0049 A 类转 `*μ*`（正文文字） |
| `$1- \alpha $` 内侧空格 | 1 | 按 C2 规范化为 `$1-\alpha$`（数学结构不变） |

除上述 11 处外，其余公式逐式对应；`check_math.py` 对源文报 370（display 4＋行内 366），译文 `check_math_zh` 硬错误 0、C10 0。

## 三、账本

- 169 段：165 body（含 H2／H3／H4、引块、表、图、列表）＋4 oir。
- `step1` 与 `step2` 逐段相同（暂无二校改动），无空段、无错位。
- 与 `zh` 正文 165/165 块对应；OIR 4 项与 en 逐条对应。

## 四、源缺陷与译者注释

本轮翻译发现上游文字缺陷 2 处，已登记 `baseline/en-errata/en-errata.md` 第十五节，`en/` 与 `html/` 不变：

| 位置 | 上游原文 | 参考读法 | 承载 |
| ---- | ---- | ---- | ---- |
| §2.3 首段 | `C.S. Pierce` | `C.S. Peirce`（皮尔士） | 译者注释①（§2.3 首段句末锚点） |
| §2.3 Keynes 引块 | `saying than an accession` | `saying that an accession` | 译者注释②（引块前导句冒号后锚点） |

另有源文脚注键 `[^seidenfeld-1994]`（图 1 图注）与译文初稿误写 `[^seidel-1994]` 的差异，已在译文中按 en 键修正，不属上游缺陷。

## 五、机检

| 检查器 | 结果 |
| ---- | ---- |
| `check_pairs.py` | 0 issue（尾序、pubinfo、编号、脚注、译者注释锚点均通过） |
| `check_style.py` | 0 issue |
| `check_quotes.py` | 0 处 |
| `check_math_zh.py` | 0 条（硬错误 0） |
| `check_terms.py` | 硬错误 0 |
| `check_academic.py --strict` | 无硬错误 |
| `check_all.py` | 23/23 全绿 |

## 六、结论

- 全文入库，165/165 块对应；189 脚注、2 图、1 表、4 display 公式完整；账本 169 段守恒。
- 两处上游文字缺陷已按 ADR-0076 入勘误并以译者注释承载；标签与链接完整。
- 状态推进 `ex-04_checked → tr-02_checked`。下一步 T212：tr-03 一校逐节核销＋tr-04 二校语体。
