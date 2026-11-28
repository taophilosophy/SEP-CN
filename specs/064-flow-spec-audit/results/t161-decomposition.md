# T161 拆解：digital-art 全流程（方案）

- 日期：2026-11-28
- 依据：`tasks.md` T161（工作包）、`results/t160-decomposition.md` 模板、`specs/060` 六轴判据、`rules/04` 状态机
- 条目：`d/digital-art`（`tasks/d/digital-art.json` 状态 `cleared`；`zh/d/digital-art.md` 仅存 H1）
- 版本钉：`pubinfo_date: Dec 15, 2023`；`archive_edition: Summer 2024`；`sha256: 25414cbb…fc01`（实测 `html/digital-art/index.html` 106,249 字节，SHA-256 一致）
- 原则：T161 只作容器，**不得整体勾选**；拆为 11 个原子任务（T261–T271）

## 一、源文实测（2026-11-28，`en/d/digital-art.md`）

| 项 | 实测 |
| ---- | ---- |
| 规模 | 89,317 字节／343 行／88,474 字符／13,318 英文词 |
| 标题 | H1 1；H2 9（§1–§5＋References／Academic Tools／Other Internet Resources／Related Entries）；H3 7（1.1–1.4、4.1–4.3）；H4 0 |
| 章节字符量 | 导论 2,948；§1 25,167（1.1 2,631／1.2 5,209／1.3 10,030／1.4 7,158）；§2 11,789；§3 11,782；§4 17,143（4.1 3,012／4.2 8,024／4.3 5,556）；§5 8,839；尾节 References 56／Academic Tools 660／Other Internet Resources 1,069／Related Entries 1 行＋60 脚注定义 |
| 内容块 | 160：正文 69、脚注定义 60、标题 17、引块 9、列表 4、代码块 1 |
| 代码块 | 1（ASCII 兔子，en L20–24；三反引号成对闭合；第三行含弯引号与行尾空格，**逐字保留**） |
| 表格 | 0 内容表；Academic Tools 引块表 1（4 行） |
| 图片 | 0 幅；`assets/digital-art/` 不存在；`fetch_audit` 资产 0、缺件 0 |
| 脚注 | 定义 60（60 键唯一）；正文 marker 66 处／50 键（另有说明性字面量 `[^key]` 1）；10 条定义未被正文引用（书目项照源保留） |
| 公式 | 0 |
| 补充子文档 | 0 |
| 源审计 | `en_integrity` clean 1/1；`en_source_audit` hard 0／warn 7；`fetch_audit` complete 1/1 |

### warn 候选定性（T261 复核并落记录）

| 告警 | 数量 | 初判 |
| ---- | ---- | ---- |
| `digit_for_letter` `1s`／`0s` | 6 | 假阳性：二进制数字串的复数（“1s and 0s”），非字母误植 |
| `pp_no_space` `pp.7-23` | 1 | 真候选：书目条目缺空格且用连字符；纯排版空隙类，只入勘误表、不强求译注 |

### 人工核查发现（已在冻结 `html/` 内逐条确认）

| slug | 位置 | 上游原文 | 缺陷定性 | 参考读法 | 中文承载 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| digital-art | 导论（en L8） | `we can expect to to learn` | ①排印（重复 `to`） | `we can expect to learn` | 译文按“可以期待学到更多”，纯排版无需译注 |
| digital-art | 书目 Ackermann 条（en L224） | `Andreas Rauscher, Andreas and Daniel Stein` | ①排印（重复名 `Andreas`） | `Andreas Rauscher, and Daniel Stein` | 书目按参考读法呈现，译者注释承载 |
| digital-art | 书目 Ackermann 条（en L224） | `pp.7-23` | ①排印（空格与连接号） | `pp. 7–23` | 书目按参考读法，纯排版无需译注 |

- 三条均以 html 原串为准（2026-11-28 逐串核对）；按 ADR-0062 只入 `baseline/en-errata/en-errata.md`，不改 `en/`。
- 结论：本件无 Critical；无格式层补丁需求；无缺件。

## 二、原子任务

| 任务 | 名称 | 范围与手段 | 验收 | 证据 |
| ---- | ---- | ---- | ---- | ---- |
| **T261** | ex-04＋tr-01＋tr-02 样章 | `en_integrity`＋`en_source_audit`＋`fetch_audit`；7 条 warn 定性；html 本体与代码块闭合核查；tr-01 术语摘录／勘误注入／结构清单／提示词；样章导论＋§1.1（842 词，1 代码块，0 表）；任务账补 `project_spec`／`translation_mode`／`pe` | 源审计 hard 0；warn 逐条定性；术语先登记后用；样章块数与 en 对应；代码块闭合 | `results/t261-review.md` |
| **T262** | tr-02 批 1（§1.2–§1.3） | 2,324 词；Goodman 模拟-数字之分与生产关系；0 表 | 术语（differentiated／dense 等）按登记册；账本守恒 | `results/t262-review.md` |
| **T263** | tr-02 批 2（§1.4＋§2） | 3,010 词；展示层与数字图像；0 表 | 账本守恒；引块与列表结构完整 | `results/t263-review.md` |
| **T264** | tr-02 批 3（§3） | 1,868 词；数字媒介中的作品欣赏；0 表 | 账本守恒；人名与书名照源 | `results/t264-review.md` |
| **T265** | tr-02 批 4（§4.1–§4.2） | 1,689 词；互动作品定义与展示可变性；0 表 | 账本守恒；术语 interactivity 统一 | `results/t265-review.md` |
| **T266** | tr-02 批 5（§4.3＋§5） | 2,269 词；互动与创造、定位艺术；7 引块、3 列表 | 账本守恒；引块完整 | `results/t266-review.md` |
| **T267** | tr-02 批 6（尾节＋60 脚注定义） | 尾节四段＋60 条定义；`Primary`／`Secondary` 空节按源保留；书目骨架照录＋书名括注；推进 `tr-02` | 尾节合体例；60 定义键集与 en 相同；marker↔定义闭合；账本守恒 | `results/t267-review.md` |
| **T268** | tr-03／tr-04 | 一校逐节核销；二校语体与反欧化（`check_prose` 清零或逐条豁免） | 账本守恒；残留外文 0（书目与原文引文除外）；检查器全绿 | `results/t268-tr03.md`、`t268-tr04.md` |
| **T269** | rv-01 三轴 | 术语轴（D1–D5 定性、三出口）＋体例轴＋勘误轴 | `check_terms` 硬 0；体例 hard 0；勘误 3 行承载可验 | `results/t269-rv01.md` |
| **T270** | rv-02＋rv-03–08＋rv-09 | 两轴审计；q1 引文→q2 逻辑→q3 语法→q4 语域→q5 计量→q6 标点；体例终校 | 各轴凭据落 `state/axis/`；`--gate` 0 或逐条豁免；`check_all` 全绿 | `results/t270-review.md` |
| **T271** | sg 链 | sg-01 初审＋sg-02 复审；sg-03 须用户 `--mandate`，未授权则止于 `sg-02_checked` | sg-01／sg-02 无 Critical／Major | `results/t271-sg01.md` 等 |

## 三、体例与资产要求

1. 代码块：en L20–24 的 ASCII 兔子逐字保留（含弯引号与行尾空格），不译、不重排；rv-09 复查三反引号闭合。
2. 60 条脚注定义：书目骨架照录、书名按 ADR-0037 括注通行汉译（查证不到者留原样并登记）；`[^key]` 说明性字面量照录；marker↔定义闭合；未被引用的 10 条书目定义照源保留。
3. 尾节顺序：`## 参考文献 > ## 学术工具 > ## 其他网络资源 > ## 相关词条 > [脚注定义] > ## 译者注释`；本件无 `原始文献`／`二手文献` 子节，不凭空增设。
4. 勘误：3 行入全局勘误表新节；导论重复 `to` 与 `pp.7-23` 纯排版不设译注；书目重复 `Andreas` 以译者注释承载（正文与书目按参考读法）。
5. 术语：`digital art`＝数字艺术、`interactivity`＝交互性、`locative art`＝定位艺术、`locative media`＝定位媒介、`net art`＝网络艺术、`analog-digital distinction`＝模拟-数字之分、`finite differentiation`＝有限分立、`allographic`＝代笔的（`autographic` 亲笔的）、`bitmap`＝位图、`sampling`＝采样、`quantization`＝量化、`pixelation`＝像素化、`chatbot`＝聊天机器人、`display type`＝显示类型、`site-specificity`＝特定场域性、`serious play`＝严肃游戏；新术语先登记后用。
6. 人名与书名依 `zh/ren-ming-biao.md` 与学界通行译名；`Goodman`、`Lopes`、`Gaut` 等首现括注原文。
7. 每批完成后跑 `check_style`／`check_quotes`／`check_terms`／`check_pairs`／`check_academic --strict`；未绿不得进入下一批。

## 四、执行顺序

```
T261 → T262 → T263 → T264 → T265 → T266 → T267 → T268 → T269 → T270 → T271
```

- 状态机禁跳步；T261 先 `cleared → ex-04_checked`，样章不推进 tr-02。
- T262–T267 属 tr-02 内部批次，T267 完成后统一 `advance --step tr-02`。
- T271 的 sg-03 不在本方案内自动执行，须用户显式 mandate。
- T161 容器保持未勾选，完成由 T261–T271 派生。
