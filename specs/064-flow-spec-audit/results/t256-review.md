# T256 证据：kokugaku-school tr-02 §5–§6＋尾节＋脚注

- 日期：2026-11-28
- 任务：T256（T160 拆站第五项，tr-02 收口）
- 条目：`k/kokugaku-school`；状态 `ex-04_checked → tr-02_checked`
- 范围：`en/k/kokugaku-school.md` §5–§6、四尾节、51 条脚注定义

## 一、入库内容

| 项 | 结果 |
| ---- | ---- |
| 译文 | 全文 431 行／12,515 汉字（本轮新增约 2,430 汉字） |
| 账本 | 106 → 181 段；全篇块与 en 逐块对齐（181/181） |
| 结构 | `## 5. 明治时期（1868—1912）的国学`（5 段＋2 引块）；`## 6. 明治之后的国学`（3 段）；尾节 4 个 H2＋2 个空 H3 |
| 脚注 | 定义 51（50 书目＋1 导读注）；键集与 en 完全相同；正文 marker 5 处（`walthall-1998` 3、`fujiwara-2021` 2）闭合 |
| 表格／图／公式 | 6 表（均在前批）／0／0 |

## 二、尾节体例

顺序：`## 参考文献`（含转换说明引块＋书目导读段）→ `### 原始文献` → `### 二手文献` → `## 学术工具`（四条列表，ADR-0037）→ `## 其他网络资源`（四条）→ `## 相关词条`（七项，` | ` 分隔）→ 51 条脚注定义 → `## 译者注释`。

- `### 原始文献`／`### 二手文献` 照源保留空节。
- 学术工具由源引块表改为列表形态（ADR-0037 决策 7）。
- 相关词条中文名与 `zh/SUMMARY.md` 集群名一致：日本哲学、日本美学、日本儒学、空海、日本哲学：净土、日本禅宗哲学、和辻哲郎。
- `[^kokugaku-1690]` 为书目导读注，整段译中文；其余 50 条书目骨架照录英文，书名不妄加汉译。

## 三、术语与核证

新增 10 条术语：`Ame-no-Minakanushi`＝天之御中主神、`Dajōkan`＝太政官、`Engishiki`＝《延喜式》、`furukoto`＝古事、`Hongaku kyoyō`＝《本学举要》、`Imperial Rescript on Education`＝《教育敕语》、`Omoikane`＝思兼神、`Separation of Kami and Buddhas`＝神佛分离、`Tamakatsuma`＝《玉胜间》、`Yōrōkan`＝养老馆。

核证：`Honkyō`＝本教、`hongaku`＝本学沿用既有登记；`Tama no mihashira`＝《灵能真柱》、`Kishin shinron`＝《新鬼神论》、`Kenkin sengo`＝《献芹詹语》前批已核；`Tamakatsuma` 依源文括注 *Basket of Jewels* 作《玉胜间》。

## 四、机检

- `check_style` 0；`check_quotes` 0；`check_terms` 硬错误 0（0 条告警）；`check_pairs` **0 issue**（节标题、书目、尾序、errata-apply、note-anchor 全部通过）；`check_academic --strict` 无硬错误；`check_all` 23/23。
- 账本守恒：181 段；脚注定义键集与 en 逐键相同。
- 结构：H2 11（比 en 多 `## 译者注释`，ADR-0065 允许）、H3 12、H4 4。

结论：T256 通过；状态至 `tr-02_checked`，继续 T257（tr-03／tr-04）。
