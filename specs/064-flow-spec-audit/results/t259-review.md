# T259 证据：kokugaku-school rv-02＋六轴＋rv-09

- 日期：2026-11-28
- 任务：T259（T160 拆站第八项）
- 条目：`k/kokugaku-school`；状态 `rv-01_checked → rv-09_checked`
- 依据：`rules/04`、ADR-0079 六轴、specs/060 `checklists/q1-cite.md`…`q6-punct.md`、ADR-0041 规范基线

## 一、rv-02 两轴审计

### 译文轴

- 账本 181 段与 en 181 块逐块对齐（79 正文、51 脚注定义、26 标题、19 引块、6 表）。
- 逐段回 en 核内容：无漏译、增译、错译；6 张和歌表逐行对应；51 条脚注定义键集相同。
- 引文 17 条与 en 引块一一对应；5 处正文 marker（`walthall-1998` 3、`fujiwara-2021` 2）闭合。

### 全局轴

| 项 | zh | en | 结论 |
| ---- | ---- | ---- | ---- |
| H2 | 11 | 10 | 差 1 为 `## 译者注释`（ADR-0065 允许） |
| H3 | 12 | 12 | 一致 |
| H4 | 4 | 4 | 一致 |
| 表格 | 6 | 6 | 一致；表号 1–6 |
| 脚注定义 | 51 | 51 | 键集相同 |
| 正文引用 | 5 | 5 | 一致 |
| 图片 | 0 | 0 | — |
| 公式 | 0 | 0 | — |

### 密度与语体

- 破折号 25 对；逐处复核均承担插入、转折或解释，未见以破折号代替句法结构。
- “一个”19 处，均对应不定冠词或数量义（一个自然乐园、一个全新的“黎明”、一个柔弱女子等），无冗赘。
- AI 腔抽查：无空洞拔高、模糊归因、公式化排比；“首先／其次／最后”只见于源文自身列举。
- 同源盲区：本轮由主会话完成，已以全局密度统计＋冷置回读（tr-03 后隔轮复读）补偿，记此。

## 二、rv-03 q1 引文轴

- `cite_audit --init`：17 条直引（全部 block，zh）；`--gate` 0 问题；`--check-hash` 0。
- 清单 `state/axis/kokugaku-school.cite.json`：17 条逐条 `verdict=pass`，`origin_lang=ja`、`original_status=unavailable`、`english_source=sep-inline`，anchor 指向 en L32…L271。
- 原著语种：17 条均为日文著作（《万叶集》《古事记》《古事记传》《葛花》《灵能真柱》《古道大意》《国益本论》《幽府新论》《岩木山三百首》《献芹詹语》《本学举要》等）的英译；日文原文不可得，译文据 SEP 英文引文转译，未代造原文。

## 三、rv-04 q2 逻辑轴

- `logic_audit --init`：303 散句；logic_bearing 37 条，逐条裁定 `equivalent`（reviewer=trae-main）。
- 算子候选 7 条（samples）：`all` 1、`no` 5、align 1；逐条复核：
  * §1 `all`：“all have their advocates”→“各有拥护者”，全称义保留；
  * §1 `no`：“no longer used”→“不再用来指称”，否定保留；
  * §2 `no` 2 条：“nothing came of it”→“请愿未果”；另一条为 not/no 词形误报；
  * §5 `no`、§6 `no`：均为 not/no 子串误报，语义未漂移；
  * `align`：2 个 H2 节因表格标签块与译者注释块数不一致被跳过（§3、§4），该两节已由 rv-02 逐段核与 tr-03 逐节核覆盖。
- `--gate` 0 问题；q1 hash 守恒。

## 四、rv-05 q3 语法轴

- `grammar_audit --init`：10 条告警；处置后 9 条（1 条已修）。
- 处置：
  * G-7@216 关联词假性错配：“无论如何……也”→删“无论如何”，`fixed`；
  * G-14@27 `conj-he-verb`：术语“和歌”首字误报，`false-positive`；
  * G-11@85 两处“有的……有的……”存在／列举结构，`false-positive`；
  * G-11@141、@167 两处、@226：和歌／引文内部，`waived`；
  * G-19@71、@75：“物哀”为已登记术语（首现 japanese-aesthetics），`waived`。
- G-1／G-5／G-7 机检命中：0／0／1（已修）；G-9、G-10、G-12–G-16 无未处置项；`--gate` 0。

## 五、rv-06 q4 语域轴

- 六个主节全部定为 R-1（导言与说明段可 R-2），无 R-4／R-5 越界；`--gate` 0。
- R-e 候选 2 条“蛮”：均为历史语境“蛮夷”（barbarian），非口语／网络语，`false-positive`。
- R-d 文言残留：0；R-f 称谓：统一用“你”以外的第三人称叙述，无敬称切换。
- 样章基准：`baseline/register-baseline.md` 尚未建立（全库缺口），按 rules/02 语体结论与既有 done 件同档；已登记 I1。

## 六、rv-07 q5 计量轴

- `measure_audit --init`：量值 2 条（10%、80%），均 `pass`；与源一致。
- 范围 37 条：36 条一字线；1 条 en dash 为引文页码 `SJTa: 401–402`（ADR-0041 豁免）。
- M-6“连接号混用”1 条：`false-positive`（正文年段统一一字线，en dash 仅见引文页码）；`--gate` 0。

## 七、rv-08 q6 标点轴

- `punct_audit --init`：1 条 P-13@45（`401–402`），`waived`（引文页码，ADR-0041）；`--gate` 0。
- P-1…P-12、P-14…P-20 无命中；`check_style` 0、`check_quotes` 0。

## 八、rv-09 体例终校

- 适用规范基线：GB/T 15834-2011（标点）、GB/T 15835-2011（数字）、CY/T 266-2023、GB 3100／3101（照录源豁免）、ADR-0041 偏离登记；未发现冲突。
- 结构：431 行／12,451 汉字；181 段账本；51 定义；5 引用；6 表；H2 11（含译者注释）、H3 12、H4 4。
- 尾序：参考文献 ＞ 原始文献 ＞ 二手文献 ＞ 学术工具 ＞ 其他网络资源 ＞ 相关词条 ＞ 脚注定义 ＞ 译者注释。
- `check_style` 0；`check_quotes` 0；`check_pairs --gate` hard 0／out_of_scope 0；`check_terms` 硬 0／告警 0；`check_academic --strict` 无硬错误；`check_math_zh` 0；`check_prose` 7 条已逐条豁免（见 T257 tr-04）。
- 六轴 gate：q1 0、q2 0、q3 0、q4 0、q5 0、q6 0。

结论：rv-02 与六轴、rv-09 全部通过；状态至 `rv-09_checked`，继续 T260（sg-01／sg-02）。
