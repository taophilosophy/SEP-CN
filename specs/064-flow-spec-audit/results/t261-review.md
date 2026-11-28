# T261 证据：digital-art ex-04＋tr-01＋tr-02 样章

- 日期：2026-11-28
- 任务：T261（T161 拆站首项）；状态 `cleared → ex-04_checked`
- 条目：`d/digital-art`；版本钉 `Dec 15, 2023`／`Summer 2024`／`25414cbb…fc01`
- 证据机检件：`t261-en-integrity.json`、`t261-en-source-audit.json`

## 一、ex-04 源审计

| 项 | 结果 |
| ---- | ---- |
| `en_integrity` | clean 1/1；hard 0 |
| `en_source_audit` | hard 0／warn 7（`t261-en-source-audit.json`） |
| `fetch_audit` | complete 1/1；资产 0、缺件 0 |
| 版本钉 | `html/digital-art/index.html` 106,249 字节，SHA-256 与任务账 `25414cbb…fc01` 逐字相符 |
| 规模 | 89,317 字节／343 行／13,318 英文词；160 块（正文 69、脚注定义 60、标题 17、引块 9、列表 4、代码块 1） |
| 结构 | H1 1；H2 9；H3 7；§1–§5＋四尾节 |
| 代码块 | 1（en L20–24，ASCII 兔子；三反引号成对闭合；第三行含弯引号与行尾空格，逐字保留） |
| 表格 | 0 内容表；Academic Tools 引块表 1（4 行） |
| 图片 | 0 幅；html 内 5 个 `<img>` 均为站徽／图标；`assets/digital-art/` 不存在 |
| 脚注 | 定义 60（60 键唯一）；正文 marker 66 处／50 键；说明性字面量 `[^key]` 1 |
| HTML 本体 | 注释配对 37/37；`<pre>` 闭合；括号与方括号逐段平衡（去链接与脚注键后 0 残余）；末段完整 |

### warn 候选定性（7 条）

| 告警 | 数量 | 定性 |
| ---- | ---- | ---- |
| `digit_for_letter` `1s`／`0s` | 6 | 假阳性：二进制数字串复数（“1s and 0s”），命中 B 类（年代与数字缩写）豁免，非字母误植 |
| `pp_no_space` `pp.7-23` | 1 | 真候选：书目条目缺空格且用连字符；纯排版空隙类，入勘误表、无需译注 |

### 人工核查与勘误

- 新发现 4 行文字缺陷，已入 `baseline/en-errata/en-errata.md` 第二十三节（均在冻结 html 内逐串核对）：
  1. 导论 en L8 `to to learn`（重复 `to`）；
  2. 书目 Ackermann 条 en L224 重复 `Andreas`；
  3. 同条 `pp.7-23`（缺空格、连接号）；
  4. 同条 `Medien-und Kulturwissenschaften`（德语并列复合缺空格）。
- 中文承载：第 2 条以译者注释①承载（书目按参考读法）；其余 3 条纯排版，无需译注。
- 无 Critical；无格式层补丁需求；无缺件、无静默跳过。

## 二、tr-01 译前准备

### 1. 术语摘录（样章，14 条新增，2026-11-28 登记）

| 原文 | 译名 | 登记状态 |
| ---- | ---- | ---- |
| digital art | 数字艺术 | 既有 |
| digital cinema | 数字电影 | 新增 |
| digital photography | 数字摄影 | 新增 |
| digital painting | 数字绘画 | 新增 |
| electronic music | 电子音乐 | 新增 |
| chatbot fiction | 聊天机器人小说 | 新增（`chatbot` 既有） |
| NFT art | NFT 艺术 | 新增 |
| net art | 网络艺术 | 既有 |
| video game | 电子游戏 | 新增 |
| digital media | 数字媒介 | 新增 |
| digital condition | 数字状况 | 新增 |
| ASCII art | ASCII 艺术 | 新增 |
| digital encoding | 数字编码 | 新增 |
| binary code | 二进制代码 | 新增 |
| computational process | 计算过程 | 新增 |
| computer art | 计算机艺术 | 新增 |

人名：Katherine Thomson-Jones、Shelby Moser（H1 作者括号）；Kittler、Rush、Paul、Tavinor、Gaut、Lopes、Robson、Atencia-Linares、Artiga、Millière、Moruzzi、Roberts、Krueger 均按原文照录；Gottfried Michael Koenig 首现括注原文。

### 2. 勘误注入

- 导论 `to to` 按参考读法作“可以期待学到更多”，无需译注。
- 书目重复 `Andreas` 按参考读法，译者注释①待 T267 尾节建立。
- `pp.7-23` 与 `Medien-und` 纯排版，按参考读法落文，无需译注。

### 3. 结构清单（样章）

- 导论 2 段；`## 1. 什么是数字艺术？`（H2）；`### 1.1 数字艺术界`（H3）＋5 段＋1 代码块。
- 10 个账本段：正文 7、标题 2、代码 1；0 图、0 表、0 公式。
- 正文 marker 11 处（定义待 T267 补齐）。

### 4. 提示词要点

底稿只用 `en/`；目标读者为中文哲学读者；现代汉语学术书面语；保留代码块原样、斜体术语与英文人名；年段用一字线；书名用通行汉译；不增删命题；`Dune` 作《沙丘》（*Dune*，2021）。

## 三、tr-02 样章

- 入库：`zh/d/digital-art.md`；28 行／2,134 字符／1,312 汉字；账本 `tasks/d/digital-art.ledger.yaml` 10 段。
- 结构：H2 1；H3 1；代码块 1（三反引号闭合）；图 0；表 0；公式 0。
- 账本守恒：`step2` 顺序拼接与 zh 正文逐字相等；10 段 `source` 均在 `en/` 内逐字命中。
- 机检：`check_style` 0；`check_quotes` 0；`check_terms --docs` 硬 0（2 条“正文缺登记译法”告警指向 §1.3／§3 尚未翻译的人名，留待后续批次）；`check_academic --strict` 无硬错误；`check_pairs` 4 条样章预期缺口（cite-authoryear 1、节标题／书目计数 2、尾节缺失 1），T267 收口时清零。
- 状态：样章不推进 tr-02；`tr-02_checked` 待 T267 全量完成后统一推进。

结论：T261 通过；状态至 `ex-04_checked`。
