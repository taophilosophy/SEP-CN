# T160 拆解：kokugaku-school 全流程（方案）

- 日期：2026-11-28
- 依据：`tasks.md` T160（工作包）、`results/t159-decomposition.md` 模板、`specs/060` 六轴判据、`rules/04` 状态机
- 条目：`k/kokugaku-school`（`tasks/k/kokugaku-school.json` 状态 `cleared`；`zh/k/kokugaku-school.md` 仅存 H1）
- 版本钉：`pubinfo_date: Jun 21, 2021`；`archive_edition: Fall 2021`；`sha256: 640fe38e…1d3`
- 原则：T160 只作容器，**不得整体勾选**；拆为 9 个原子任务（T252–T260）

## 一、源文实测（2026-11-28，`en/k/kokugaku-school.md`）

| 项 | 实测 |
| ---- | ---- |
| 规模 | 67,714 字节／415 行／66,724 字符／9,847 英文词 |
| 标题 | H1 1；H2 10（§1–§6＋References／Academic Tools／Other Internet Resources／Related Entries）；H3 12；H4 4 |
| 章节字符量 | §1 2,996；§2 5,795；§3 12,362；§4 23,625；§5 5,558；§6 2,378；尾节 2,597＋脚注定义 9,391 |
| 内容块 | 183 块：正文 79、脚注定义 51、标题 27、引块 19、表格 6、列表 1 |
| 表格 | 6 块／47 行：§3.2 两首和歌对译表、§4.3 两首、§4.4 一首、§4.5 一首（英文左列＋罗马字右列） |
| 图片 | 0 幅；`assets/kokugaku-school/` 不存在；`fetch_audit` 资产 0、缺件 0 |
| 脚注 | 定义 51（50 条书目＋1 条导读注）；正文引用 5 处（`walthall-1998` 3、`fujiwara-2021` 2）；`[^key]` 为说明性字面量 |
| 公式／代码块 | 0／0 |
| 引块 | 19 块（含 4 首和歌以引块起句） |
| 补充子文档 | 0 件 |
| 源审计 | `en_integrity` clean 1/1；`en_source_audit` hard 0／warn 2（`heading_skip` 为站尾导航 H4，`fall2018` 为 URL 段，均拟判误报） |
| 勘误 | 全局勘误表有 1 行：§4.3 `Matsudaira Yoshitatsu (1824–83)` 生卒误，中文须用参考读法 `1800–1862` 并加译注 |
| 术语 | 登记册已有 16 条术语＋24 条人名（含旧 s2.4 收口），本轮回炉复核后使用 |

## 二、原子任务

| 任务 | 名称 | 范围与手段 | 验收 | 证据 |
| ---- | ---- | ---- | ---- | ---- |
| **T252** | ex-04＋tr-01＋tr-02 样章 | `en_integrity`＋`en_source_audit`＋`fetch_audit`；2 条 warn 定性；51 脚注键口径；tr-01 术语摘录／勘误注入／结构清单／提示词；样章 §1–§2（8,791 字符／1,341 词，0 表） | 源审计 hard 0；warn 逐条定性；术语先登记后用；样章块数与 en 对应 | `results/t252-review.md` |
| **T253** | tr-02 批 1（§3） | 12,362 字符／1,982 词；2 张和歌对译表；契冲、荷田春满、贺茂真渊、本居宣长 | 两表结构完整、表号与单元格中文；账本守恒 | `results/t253-review.md` |
| **T254** | tr-02 批 2（§4.1–§4.2） | 12,079 字符；平田笃胤与宫贞雄；无表 | 人名生卒照源；账本守恒 | `results/t254-review.md` |
| **T255** | tr-02 批 3（§4.3–§4.5） | 11,179 字符；4 张和歌表；松尾多势子、平尾鲁仙／鹤屋有猷、矢野玄道；勘误行落地（松平义建生卒＋译注） | 4 表结构完整；勘误承载在位；账本守恒 | `results/t255-review.md` |
| **T256** | tr-02 批 4（§5–§6＋尾节＋51 脚注） | 7,936 字符正文＋2,597 字符尾节＋51 条定义；`Primary`／`Secondary` 空节；书目照录＋书名括注 | 尾节合体例；51 定义与 en 逐字一致；账本守恒；推进 `tr-02_checked` | `results/t256-review.md` |
| **T257** | tr-03／tr-04 | 一校逐节核销；二校语体与反欧化（`check_prose` 清零或逐条豁免） | 账本守恒；残留外文 0（书目与日文引文除外）；检查器全绿 | `results/t257-tr03.md`、`t257-tr04.md` |
| **T258** | rv-01 三轴 | 术语轴（D1–D5 定性、三出口）＋体例轴＋勘误轴 | `check_terms` 硬 0；体例 hard 0；勘误 1 行承载可验 | `results/t258-rv01.md` |
| **T259** | rv-02＋rv-03–08＋rv-09 | 两轴审计；q1 引文→q2 逻辑→q3 语法→q4 语域→q5 计量→q6 标点；体例终校 | 各轴凭据落 `state/axis/`；`--gate` 0 或逐条豁免；`check_all` 全绿 | `results/t259-review.md` |
| **T260** | sg 链 | sg-01 初审＋sg-02 复审；sg-03 须用户 `--mandate`，未授权则止于 `sg-02_checked` | sg-01／sg-02 无 Critical／Major | `results/t260-sg01.md` 等 |

## 三、体例与资产要求

1. 6 张和歌表：英文左列译中文，罗马字右列照录；表前加 `表 N` 标签行（N＝1–6），表内不增删诗行；归属行（如“（据 Muraoka 1964: 148）改译”）随左列译中文。
2. 51 条脚注定义：50 条书目条目骨架照录、书名按 ADR-0037 括注通行汉译（查证不到者留原样并登记）；导读注全文译中文；marker↔定义闭合。
3. 尾节顺序：`## 参考文献 > ### 原始文献 > ### 二手文献 > ## 学术工具 > ## 其他网络资源 > ## 相关词条 > [脚注定义]`；`### 原始文献`／`### 二手文献` 照源保留空节。
4. 勘误：§4.3 松平义昭句按参考读法作 `松平义建（1800–1862）`，文末 `## 译者注释` 节加圈号①条目；正文禁含上游错形 `1824–83`。
5. 术语：`kokugaku`＝国学、`Kokugakusha`＝国学者、`Nihonjinron`＝日本人论、`kakuriyo/yūmeikai`＝隐世/幽冥界、`magokoro`＝真心、`karagokoro`＝汉意、`kannagara`＝随神而行、`shinkoku`＝神国、`kokutai`＝国体、`hongaku/honkyō`＝本学/本教、`mikunigokoro`＝御国心、`makoto no shintō`＝真神道、`kishin`＝鬼神、`saisei itchi`＝祭政一致、`Taikyō senpu undō`＝大教宣布运动、`Yamato gokoro/damashii`＝大和心/大和魂；人名依 `zh/ren-ming-biao.md`。
6. 日文书名与术语首现括注原文；`waka`、`Man’yōshū`、`Kojiki` 等依登记册或学界通行译名。
7. 每批完成后跑 `check_style`／`check_quotes`／`check_terms`／`check_pairs`／`check_tables_images`；未绿不得进入下一批。

## 四、执行顺序

```
T252 → T253 → T254 → T255 → T256 → T257 → T258 → T259 → T260
```

- 状态机禁跳步；T252 先 `cleared → ex-04_checked`，样章不推进 tr-02。
- T253–T256 属 tr-02 内部批次，T256 完成后统一 `advance --step tr-02`。
- T260 的 sg-03 不在本方案内自动执行，须用户显式 mandate。
- T160 容器保持未勾选，完成由 T252–T260 派生。
