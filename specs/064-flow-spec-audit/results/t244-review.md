# T244 证据：japanese-aesthetics ex-04＋tr-01＋tr-02 样章

- 日期：2026-11-28
- 任务：T244（T159 拆站首项）；状态 `cleared → ex-04_checked`
- 条目：`j/japanese-aesthetics`；版本钉 `Dec 6, 2023`／`Spring 2024`／`022caca6…0904d`

## 一、ex-04 源审计

| 项 | 结果 |
| ---- | ---- |
| `en_integrity` | clean 1/1；hard 0 |
| `en_source_audit` | hard 0／warn 0；entry 链接 1、外部链接 11、标题 20 |
| `fetch_audit` | complete 1/1；72 资产；缺件 0 |
| 版本钉 | pubinfo Dec 6, 2023、archive Spring 2024 与 en 一致 |
| 结构 | H1 1；H2 14；H3 1（Acknowledgments）；正文 §1–§10 |
| 图片 | 33 幅缩略图（§3 3、§5 4、§7 1、§9 10、§10 15）；资产闭包齐备 |
| 脚注 | 定义 44（唯一键 44）；引用 8（7 真实引用＋[^key] 说明） |
| 公式／代码／表格 | 0／0／0（audit 的 tables 2 为链接行口径，正文无表行） |
| 补充子文档 | 6 件，均在 `en/j/` 就位 |
| 勘误 | 该件在全局勘误表无行 |

结论：源可信、资产闭包完整，无阻断项。

## 二、tr-01 译前准备

### 1. 术语摘录（样章 §1–§2）

| 原文 | 译名 | 登记状态 |
| ---- | ---- | ---- |
| Japanese aesthetics | 日本美学 | 既有 |
| mono no aware | 物哀（物の哀れ） | 既有 |
| pathos | 情致 | 既有 |
| wabi | 侘（侘び） | 既有 |
| sabi | 寂（さび） | 既有 |
| yūgen | 幽玄 | 既有 |
| iki | 意气（いき） | 既有 |
| kire | 切（きれ） | 既有 |
| mujō／impermanence | 无常 | 既有 |
| chadō | 茶道 | 既有 |
| shodō | 书道 | 既有 |
| self-cultivation | 修身 | 既有 |
| Six Arts | 六艺 | 新增（2026-11-28） |
| Genji monogatari | 《源氏物语》 | 新增（2026-11-28） |
| Heike monogatari | 《平家物语》 | 新增（2026-11-28） |
| Tsurezuregusa | 《徒然草》 | 新增（2026-11-28） |
| sōla | 沙罗 | 新增（2026-11-28） |
| Manyōshū | 《万叶集》 | 既有 |
| Dōgen／Yoshida Kenkō／Murasaki Shikibu／Motoori Norinaga／Ozu Yasujirō | 道元／吉田兼好／紫式部／本居宣长／小津安二郎 | 人名表 |
| Stanley Cavell | Stanley Cavell | 人名表（保留英文） |

### 2. 勘误注入

该件在 `baseline/en-errata/en-errata.md` 无行，无参考读法需注入。

### 3. 结构清单（样章）

- H1＋pubinfo 引块＋导论段；`## 1. 引言`（4 段＋1 引块）；`## 2. 物哀：事物的情致`（6 段＋2 引块＋1 脚注）。
- 16 个内容块；0 图、0 公式；1 条脚注定义（`mccullough-1988`，书目照录）。

### 4. 提示词要点

底稿只用 `en/`；目标读者为中文哲学读者；语体为现代汉语学术书面语；保留引块、脚注与斜体术语；日文术语首现括注原文；书名用登记译名；不增删命题；图与公式照录。

## 三、tr-02 样章

- 入库：`zh/j/japanese-aesthetics.md`；37 行／1,607 汉字；16 段账本（`tasks/j/japanese-aesthetics.ledger.yaml`）。
- 结构：H2 2；引块 2；脚注定义 1；图 0；公式 0。
- 机检：`check_style` 0；`check_quotes` 0；`check_math_zh` 硬错误 0；`check_terms` 硬错误 0；`check_academic --strict` 无硬错误；`check_pairs` hard 0／out_of_scope 1（样章预期）；`check_prose` 2 条 de-chain（术语读法列表与 Cavell 引文），留 tr-04 处理。
- 状态：样章不推进 tr-02；`tr-02_checked` 待 T248 全量完成后统一推进。

结论：T244 通过；状态至 `ex-04_checked`。
