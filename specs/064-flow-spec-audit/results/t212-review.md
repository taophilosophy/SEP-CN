# T212 证据：imprecise-probabilities 校次链（tr-03／tr-04）

- 日期：2026-11-27
- 任务：T212（T154 拆站第 4 项）；状态推进 `tr-02_checked → tr-03_checked → tr-04_checked`
- 条目：`i/imprecise-probabilities`；译文 `zh/i/imprecise-probabilities.md`（764 行／18,403 汉字，二校后）
- 账本：`tasks/i/imprecise-probabilities.ledger.yaml`（169 段＝165 body＋4 oir）

## 一、tr-03 一校（对照 en 逐节核销）

| 项 | 结果 |
| ---- | ---- |
| 账本守恒 | 169 段；165 body 与 en 165 块逐块对应；4 oir 逐条对应 |
| 脚注 | 定义 189／引用 179 处／唯一键 137；无悬空（`[^key]` 为转换说明固定串，非正文引用） |
| 残留外文 | 0（正文英文仅限人名、术语括注、书名、引文出处与文献条目） |
| 图片 | 2 幅，路径 `../../assets/imprecise-probabilities/` 可解析，alt 已译 |
| 表格 | Table 1 结构完整（5 行×4 列） |
| 公式 | `check_math_zh` 硬错误 0；display 4 与行内公式逐式核销（差额 11 处已在 T211 归因） |
| 机检 | `check_pairs` 0、`check_style` 0、`check_quotes` 0、`check_terms` 硬 0、`check_academic --strict` 无硬错误 |

**逐节核销记录**：§1（引言／术语／区分）、§2.1–2.7、§3.1–3.6（含 3.4.1／3.4.2）、§4、尾节四件套均与 en 段落一一对应；两处图注、一处表注、15 处引块边界完整；未发现漏段、错位或未译段落。

## 二、tr-04 二校（语体、反欧化）

- 基线 `check_prose`：33 条（de-chain 22、long-sentence 6、passive-bei 3、weak-verb 2、as-one 1、conj-he-verb 1）。
- 本轮实改 26 处：拆长句、去“的”链、被动改主动、弱动词改实义动词（“作出下注” → “下注”、“被引出” → “经引出而表达”、“委员会作为一个整体” → “委员会整体”、“接受与拒绝” → “接受还是拒绝”等）。
- 剩余 7 条全部位于直接引文，逐条豁免：

| 行 | 规则 | 豁免理由 |
| ---- | ---- | ---- |
| 117 | long-sentence／de-chain | Joyce 引文（1999: 21），引文不可改写 |
| 123 | long-sentence | Kaplan 引文（1983: 571），引文不可改写 |
| 217 | long-sentence／de-chain | Levi 引文（1999: 510），引文不可改写 |
| 279 | long-sentence／weak-verb | Walley 引文（1991: 93），引文不可改写 |

- 语体：现代汉语学术书面语；术语按 `zh/shu-yu-biao.md`，人名按条目 D5 保留拉丁形（引注可溯）。
- 账本重建：169 段，`step2` 与正文 165/165 一致。

## 三、机检（两站复跑）

| 检查器 | 结果 |
| ---- | ---- |
| `check_pairs.py` | 0 issue |
| `check_style.py` | 0 issue |
| `check_quotes.py` | 0 处 |
| `check_math_zh.py` | 0 条 |
| `check_terms.py` | 硬错误 0 |
| `check_academic.py --strict` | 无硬错误 |
| `check_all.py` | 23/23 全绿 |

## 四、结论

- tr-03 一校：账本 169 段守恒、165/165 块对应、189 脚注闭合、残留外文 0。
- tr-04 二校：`check_prose` 33→7，26 处实改，7 条引文豁免逐条留痕；语体一致。
- 状态推进 `tr-02_checked → tr-03_checked → tr-04_checked`。下一步 T213：rv-01／rv-02／六轴／rv-09。
