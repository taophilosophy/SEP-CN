# T134 tr-03 一校记录（2026-11-27，进行中）

- 对象：`h/habermas.md`（38,150 汉字）／`tasks/h/habermas.ledger.yaml`（239 段）
- 方法：账本 source 与 `yuanwen/h/habermas.md` 逐段对应；全文机检；残留外文扫描；高风险段落抽核
- 状态：**结构对照与机检完成；逐段语义复核待续——T134 不勾选**

## 1 段落守恒

- 账本 **239 段**；source **163,748 字符**；正文与尾节中文 **38,150 汉字**（ledger step2 合计 37,719，差额为标题/尾节标签）。
- 239/239 step2 均落文；逐段身份对应 yuanwen；未发现整段漏译或合并。
- 纯标签行 `**(1)**`／`**(2)**`／`**b.**`／`**c.**`／`**(3)**`／`**(D)**`／`**(U)**` 作为格式行保留在正文，不单独入账（非翻译段落）。
- **补漏记录**：初版合并漏掉 §1.1 P4（源 L20）与 §1.2 交往权力段（源 L30）；T133 复核时已补译并重排账本（237→239），随后重跑全部机检。

## 2 机检

| 检查 | 结果 |
| ---- | ---- |
| `check_pairs h/habermas.md` | 0 issue（尾节、编号、H1、勘误轴均过） |
| `check_academic --docs h/habermas.md --strict` | 无硬错误 |
| `check_terms --docs h/habermas.md` | 硬错误 0；未登记人名/术语告警留 T136 |
| `check_style`／`check_quotes`／`check_math_zh` | 0 issue／0 违例／0 条 |
| `check_all` | 23/23 全绿 |

## 3 残留外文

全文扫描（排除标题、引块、脚注定义、参考文献、URL、书名与引用组）后，长英文串仅 3 处，均为允许形态：

1. `*The Structural Transformation of the Public Sphere*`（英文原题括注）
2. `plebian public spheres`（源术语括注；源文拼写如此，待勘误）
3. `das Gute im Gerechten`（德文原语）

未发现未译英文句子或段落。**残留外文碎片＝0**（按“允许原题/术语/引文”口径）。

## 4 发现与挂账

### 4.1 术语不一致（转 T136 rv-01 裁定）

- `civil society`：全文 `公民社会` 7 次、`市民社会` 2 次（§7.2）。登记册主形为“市民社会”，但 §1.2 与 §4 语境用“公民社会”。属 D1/D5 词条内混形，T136 按概念与语境定主形，不机械替换。
- `legitimacy`／`rightness`：`合法性` 41 次、`正当性` 11 次。初步看“legitimacy→合法性、rightness→正当性”是语境分工，但需 T136 逐条核验，防止把 validity claim 的 rightness 误作 legitimacy。

### 4.2 源缺陷候选（未改源；待逐条回源确认后入勘误表或待考）

子代理在翻译中发现、尚未逐条入表的候选（节选）：
- §1.2：`plebian`（应 plebeian）；§1.4：`Zur Rekonstruction`（应 Rekonstruktion）。
- §2.2：L107 引号未闭合；L169 `kind` 单复数；L155 衍 `he`；L201 `on the on the`；L177 `underling`（应 underlying）。
- §3.3：L296（U）定义缺右括号；L320 多 `it`；L334 `all other`；L348 `leads Benhabib claims`；L280 `Cristoph`。
- §4：L370 `408 187` 缺分号；L392 语句残缺；L412 冒号误用；L432 `dividend`；L436 `478–1`；L448 缺右方括号；L457 `essay 3` 年份疑。
- §6：L475 引号错位；L477 `who` 应为 whom；L458 `(*sic*)` 保留。
- §7：L551 `[2008a 130–2]` 缺冒号；L539 `462, l` 疑 `n.`；L549 脱 `to`；L559 `post-metaphysical` 拼写不一。

处置建议：T134 只登记候选；确证者按 ADR-0062 入 `baseline/en-errata/en-errata.md`（文字层）或待考，格式层入补丁池；不在本记录改 `en/`。

### 4.3 结构性注意

- §2.2 类型学表：yuanwen 转换丢失 rowspan/colspan 语义；step2 已回 `en/` HTML 还原为四列逻辑表，需在 T136 前人工复核表头语义。
- 书目条目与脚注定义照录；两条已批准勘误按“照录区，无需译注”登记（见 c-group-evidence）。

## 5 结论

T134 的**结构面已过**：段落守恒、机检全绿、残留外文 0。**语义逐段复核尚未完成**，故不勾选、不推进 `tr-03_checked`；下一步需按节逐段回源核对（重点：§3 商谈伦理、§4 法哲学、§7 后世俗），并处理 4.1／4.2 的术语与源缺陷挂账。
