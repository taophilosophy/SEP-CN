# T159 拆解：japanese-aesthetics 全流程（方案）

- 日期：2026-11-28
- 依据：`tasks.md` T159（工作包）、T158 拆解模板、`specs/060` 六轴判据、`rules/04` 状态机
- 条目：`j/japanese-aesthetics`（`tasks/j/japanese-aesthetics.json` 状态 `cleared`；`zh/j/japanese-aesthetics.md` 仅存 H1）
- 版本钉：`pubinfo_date: Dec 6, 2023`；`archive_edition: Spring 2024`；`sha256: 022caca6…0904d`
- 原则：T159 只作容器，**不得整体勾选**；拆为 8 个原子任务（T244–T251）

## 一、源文实测（2026-11-28，`en/j/japanese-aesthetics.md`）

| 项 | 实测 |
| ---- | ---- |
| 规模 | 71,489 字节／339 行／70,131 字符 |
| 标题 | H1 1；H2 14（§1–§10＋References／Academic Tools／Other Internet Resources／Related Entries）；H3 1（Acknowledgments） |
| 章节字符量 | §1 2,146；§2 4,246；§3 5,285；§4 10,670；§5 6,557；§6 3,747；§7 9,173；§8 6,325；§9 6,722；§10 5,699；尾节 1,166；Acknowledgments 7,323 |
| 图片 | 33 幅缩略图（§3 3、§5 4、§7 1、§9 10、§10 15）；资产目录 72 件（含 thumb） |
| 补充子文档 | 6 件（`japanese-aesthetics.ginkakuji*.md`、`splashed-ink`、`ryoanji`、`late-spring`、`tokyo-story`），合计 3,638 字节 |
| 脚注 | 定义 44；正文引用 8；书目条目在定义区 |
| 公式 | 行内 0、display 0 |
| 表格／代码块 | 0／0 |
| 引块 | 21 行；列表 1 项；加粗 1 |
| 术语 | 登记册 `japanese-aesthetics` 行 63 条可复用 |

## 二、原子任务

| 任务 | 名称 | 范围与手段 | 验收 | 证据 |
| ---- | ---- | ---- | ---- | ---- |
| **T244** | ex-04＋tr-01＋tr-02 样章 | `en_integrity`＋`en_source_audit`＋`fetch_audit`；33 图与 72 资产闭包；44 脚注键口径；tr-01 术语摘录／勘误注入／结构清单／提示词；tr-02 样章 §1–§2（6,392 字符，0 图，0 公式） | 源审计 hard 0；33 图与 alt 清单在案；术语先登记后用；样章块数与 en 对应 | `results/t244-review.md` |
| **T245** | tr-02 批 1（§3–§4） | 15,955 字符；3 图；Wabi 与利休茶道 | 图注与 alt 中文齐备；账本守恒 | `results/t245-review.md` |
| **T246** | tr-02 批 2（§5–§7） | 19,477 字符；5 图；Sabi、Yūgen 与山水画 | 图注与 alt 中文齐备；账本守恒 | `results/t246-review.md` |
| **T247** | tr-02 批 3（§8–§10） | 18,746 字符；25 图；Iki、Kire、小津 | 25 图注与 alt 中文齐备；账本守恒 | `results/t247-review.md` |
| **T248** | tr-02 批 4（尾节＋Acknowledgments＋脚注＋补充子文档） | 8,489 字符＋44 定义；6 件补充子文档（3,638 字节） | 尾节合体例；44 脚注闭合；补充链接可解析 | `results/t248-review.md` |
| **T249** | tr-03／tr-04 | 一校逐节核销；二校语体与反欧化（`check_prose` 清零或逐条豁免） | 账本守恒；残留外文 0（书目与日文引文除外）；检查器全绿 | `results/t249-tr03.md`、`t249-tr04.md` |
| **T250** | rv 全链 | rv-01→rv-02→rv-03–08→rv-09 | 各轴凭据落 `state/axis/`；`--gate` 0 或逐条豁免 | `results/t250-review.md` |
| **T251** | sg 链 | sg-01／sg-02／sg-03（sg-03 须用户 `--mandate`） | sg-01／sg-02 无 Critical／Major；未授权则止于 `sg-02_checked` | `results/t251-sg01.md` 等 |

## 三、图表与体例要求

1. 33 幅缩略图按原段落位置照录；alt 一律中文；en 空 alt 者补描述性中文 alt（ADR-0037）。
2. 图片引用基座 `../../assets/japanese-aesthetics/`；不得引 `../en/assets/`。
3. 6 件补充子文档按带点补充材料处理：链接可解析，正文体例轴豁免。
4. 44 条脚注定义：书目条目照录英文，编号注照译；marker↔定义闭合。
5. 日文汉字（千利休、侘茶、名物等）与罗马字（*wabi*、*sabi*、*yūgen* 等）按术语表与原文处理；首现括注原文。
6. 每批完成后跑 `check_style`／`check_quotes`／`check_terms`／`check_pairs`；配对失败不得进入下一批。

## 四、执行顺序

```
T244 → T245 → T246 → T247 → T248 → T249 → T250 → T251
```

- 状态机禁跳步；T244 先 `cleared → ex-04_checked`，样章不推进 tr-02。
- T245–T248 属 tr-02 内部批次，T248 完成后统一 `advance --step tr-02`。
- T159 容器保持未勾选，完成由 T244–T251 派生。
