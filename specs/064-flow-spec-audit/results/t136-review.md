# T136 rv-01 术语与勘误记录（2026-11-27）

- 对象：`h/habermas.md`（38,150 汉字）
- 三轴：术语轴（`check_terms`）→ 体例轴（`check_pairs`／`check_style`）→ 勘误轴（全局勘误表落地）
- 状态：**完成**（T136 勾选；状态推进 `rv-01_checked`）

## 1 术语轴

### 1.1 已处置

| 项 | 处置 | 证据 |
| ---- | ---- | ---- |
| `civil society` | 词条内 7 次“公民社会”、2 次“市民社会”混形。新增登记行 `civil society (Habermas)`＝**公民社会**，与黑格尔 `civil society`＝市民社会分列；正文 2 处统一为“公民社会” | 哈贝马斯 Zivilgesellschaft 与黑格尔 bürgerliche Gesellschaft 分列；中研院《後國族時代的民主與法律》用“公民社會”（2026-11-27 查） |
| `legitimacy` | 登记册通行行为“正当性”；本词条为哈贝马斯法哲学语境，新增 `legitimacy (Habermas)`＝**合法性**（Legitimität），与 `rightness`＝正当性分列；`legality` 在本语境对应“合法律性” | 童世骏译《在事实与规范之间》：Legitimität→合法性，Legalität→合法律性；澎湃新闻 8779384／8779386（2026-11-27 查） |
| `Benhabib` | 首现改“塞拉·本哈比（Seyla Benhabib）”，其余“本哈比”，统一登记形 | `ren-ming-biao.md` 登记形 |
| `Dussel` | 首现改“恩里克·杜塞尔（1993）”，其余“杜塞尔” | 同上 |
| `Joas` | 首现改“汉斯·约阿斯等人”，其余“约阿斯” | 同上 |

### 1.2 豁免

- `Müller-Doohm, Stephan` 的登记形“斯特凡·米勒-多姆”未见于正文：该学者仅出现在引用组（`Müller-Doohm 2016`）与脚注，按 rules/03 引用组人名照录拉丁，不强求汉译。`check_terms` 硬错误 0，仅此 1 条告警，已豁免留痕。

## 2 体例轴

| 检查 | 结果 |
| ---- | ---- |
| `check_pairs.py h/habermas.md` | 0 issue（尾节、编号、H1、pubinfo、勘误轴全过） |
| `check_style.py h/habermas.md` | 0 issue |
| `check_quotes.py` | 0 违例 |
| `check_academic --strict` | 无硬错误 |

## 3 勘误轴

- 全局勘误表 §十三 `habermas` 两条：
  - `des Ritus”,, translated as`（①双逗号）
  - `Theory on Empitical Research`（①拼写）
- 两条均位于**参考文献脚注**，中文正文不翻译书目条目，`中文承载` 已登记为“照录区，无需译注（参考文献条目照录；中文正文不复制）”。
- `check_pairs` 的 `errata-apply` 为 0；`en/` 零改动，`html/` 照录。

## 4 结论

T136 三轴完成：术语混形已按概念分列登记并统一正文；体例机检 0 issue；勘误承载与登记一致。证据见本文件、`shu-yu-biao.md` 新增两行与 `baseline/en-errata/en-errata.md` §十三。
