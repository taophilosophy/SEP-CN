# 任务书 A2：标准对齐语料收尾交付（连接号残余＋登记册生卒列＋G9 四项）与 s3_checked 回退

**签发**：pc6 主研读会 | **日期**：2026-11-14 | **依据**：用户本轮裁定「你仅出任务书。具体任务交付给 s3_checked 之前的阶段，既有 s3_checked 完成的也撤销到该任务之前。」
**性质**：本文件是唯一交付物；pc6 会话不再直接改语料/任务。执行归 s3_checked 之前的阶段会话（词条任务）与维护任务会话；现存 s3_checked 词条全部撤销到 audited（s3 之前）。

## 0. 意图复述与边界（rules/08 §1）

* **意图**：连接号/G9 等体例收尾不再作为独立战役由签发会话铺量，而是并入词条任务的正常阶段流（audited/s3），使每处修改都过既有质量门并留任务级凭证；已过 s3 的词条（s3_checked）因体例基准变更（ADR-0041）重走 s3。
* **目标**：connector-scan 与 G9 四项扫描余量清零（或豁免清单在案）；s3_checked 计数归零。
* **非目标**：治理面批 B/C/D（P1–P16、TBX 导出器）仍按 specs/026 §2 分派表归治理会话，不在本任务书；en/、yuanwen/、参考文献照录节零改动；done 词条不走 reopen（回炉由 specs/023 战役承担）。
* **约束**：rules/05 批量改写纪律、ADR-0039 试金石与独立复算、ADR-0028 认领即推与积压线、ADR-0033/0041 语义判定口径。

## 1. 任务分解与基线（执行时以实扫为准，以下为 2026-11-14 卡钉）

| 编号 | 任务 | 基线 | 形态与裁定规则 | 豁免面 |
| ---- | ---- | ---- | ---- | ---- |
| W1 | 正文括注生卒年/年代区间归一字线 | 括注区间形态 `数字[–―-]数字）` letter 目录实扫 **3,072 处**（en-dash 3,000＋半角 72；上界，含豁免面）；connector-form 残余告警 6 处/2 文件（d/demonstration-medieval.md 行 27/57/69/71×2、1/18thGerman-preKant.md 行 191） | 括注内生卒年/年代/时期区间 → 一字线「—」（U+2014）。判别：前缀为 〈人名〉，／约／公元、或孤括注 `（1269-72）` 式 → 修；前缀为 pp./p./vol./no./qq./行/页/题/卷/folio/数字.编号（古典学与书证引注，如 `I.3–5`、`pp. 129–30`、Bekker `59b–c`、folio `Ei verso`）→ 豁免保留并登记 | 参考文献节、脚注定义行（照录）、en/、yuanwen/、数学定界符、APA 作者重复符 –––、罗马卷次（IV–VI，他会 A1 待判定清单同列） |
| W2 | 登记册生卒列归一 | ren-ming-biao.md 数字邻接 en-dash **1,762 处**（主体生卒列，冒号页码式 0）；shu-yu-biao.md **5–6 处**（多为依据列书证引注） | 生卒列 `c. 953–1029` 式区间 → 一字线；依据列书证引注（Rawls 2005: 23–28、§17–20 式）→ 豁免保留逐条裁定登记 | 译法/依据/日期列内容零改动（ADR-0011 登记册防回归）；本任务只动连接号字符 |
| W3 | 并列书名号/引号间顿号（GB/T 15834-2011 §4.5.3.5） | `》、《` **47 处**；`”、“` **113 处**（letter 目录实扫） | 纯并列（直接邻接）→ 去顿号；括注/引语插入并列之间者 → 宜留顿号（条文原句）；长引语并列视可读性裁定并留痕。**逐处语义判定，禁机械全删** | 参考文献节、代码块、直接引文原文 |
| W4 | 省略号半角三点残留 | `...` 孤立三点 letter 目录实扫 **11 处** | 逐处回源定性：引文/中文语流省略 → 「……」（六连点）；西文书证、文件名、URL、代码 → 豁免登记 | 参考文献节照录、代码块 |
| W5 | 多段引文首尾引号（§4.8.3.5） | 待实扫（连续引块/引用注释型模板块组） | 多段引文：每段开头仅前引号，仅末段末尾后引号；语义判定逐处裁定，命中预计极少 | 单段引文（首尾全引号正确）不适用 |
| W6 | 括号套用（§4.9.3.6） | 待实扫（`（…（…）…）` 同形嵌套） | 非公式语境的同形嵌套 → 改异形配合（〔〕/［］）或重组句式，逐处裁定；数学/逻辑公式内豁免 | 数学定界符、公式、表格公式列 |

## 2. 交付路由（用户裁定落地）

1. **在途词条任务**（state ∈ pending/cleared/drafted/s1_checked/s2_checked/audited，快照 1,793 件量级以实查为准）：W1–W6 命中随其 **audited（审计已译）步骤**落实——定点扫描命令见 §4，命中逐处裁定修复，diff/锚点入任务 steps evidence；其 **s3（三校体例）步骤**以 `check_style.py 0 issue`＋`--connector-scan` warnings 0（或豁免清单在案）为新增凭证项（rules/02 ADR-0041 条款已生效，本条为其任务级执行口径）。
2. **done 词条**（395 件）命中面：随 **specs/023 回炉战役**核销（023 已含全员 audited 重走，禁止另开批量战役、禁止 reopen）。W1 两处残余文件（demonstration-medieval、18thGerman-preKant）均为 done，走此通道。
3. **登记册（W2）**：登记 glossary-maintenance 例行任务（tasks/ 根，不计状态机，S4 schema）；符号层机械替换允许（幂等＋守恒＋逐节抽查 ≥20＋转换前后非连接号字符 md5 一致），工具与 manifest 入 specs/026/bin|results/。
4. **s3_checked 现存 24 件全部撤销到 audited**（s3 之前）：
   * 认定口径：`tasks/**.json` `state=="s3_checked"`（2026-11-14 快照 24 件；执行时实查为准，含 r1 回退新增者）。
   * 操作：task JSON `state` 回写 `"audited"`；`steps` 追加 `{"step":"revert-s3","status":"ok","actor":<执行会话>,"at":<ISO 时间>,"evidence":"用户裁定 2026-11-14（specs/026/ren-wu-shu-a2.md）：体例基准变更（ADR-0041 连接号/G9 四项），s3 重走"}`；历史 steps 不删（可追溯）。task_ops 现无受控回退命令（仅 reopen=done→pending）：先手工 JSON 编辑＋`python tools/check_all.py` 全绿后提交；治理会话可选落地 task_ops 受控回退子命令（走 ADR，非本任务书前置）。
   * 重走范围：仅 s3 及其后（r1/r2/r3）；s1/s2/audited 凭证不重复劳动（不复查旧错原则，对照基准未变）。s3 重走时按新体例条款核销该词条 W1–W6 命中。
5. **边界注记**：r1_reviewed 4 件与 state=="checked" 1 件（非状态机标准态）不在回退面——r1_reviewed 是否同口径回退待用户明确；"checked" 件由其会话自查归位。

## 3. 执行纪律（全 W 通用）

* 认领即推（ADR-0028）：阶段会话认领后先推认领凭证；作业途中积压 ≤1、收工清零。
* 写前 `git status` 重查目标文件（并行会话活跃）；W3–W6 禁机械批量（语义裁定逐处）；W1/W2 符号层替换允许机械（幂等：重跑零改动；守恒：转换计数=总量差；逐行 before/after manifest）。
* 批量工具入 `specs/026/bin/`、manifest 入 `specs/026/results/`（ADR-0023 归置）；验证性复跑 `--out` 指向独立文件（他会 A1 防线沿用）。
* 每处修改可回溯：diff 或行锚点入对应任务 JSON evidence 或 023 战役记录。
* 收工：`python tools/check_all.py` 10 项全绿＋`check_quotes` 0 违例＋sync_guard 清零。

## 4. 定点扫描命令（执行会话直接可用）

```sh
# W1 括注区间（上界清单；引注豁免逐处裁定）
command grep -rnE "[0-9]{2,4}[–―-][0-9]{2,4}[）)]" --include="*.md" a/ b/ c/ d/ e/ f/ g/ h/ i/ j/ k/ l/ m/ n/ o/ p/ q/ r/ s/ t/ u/ v/ w/ x/ y/ z/ 1/
# W1 机检面（connector-form 告警，含豁免逻辑）
python tools/check_style.py <词条路径...> --connector-scan
# W2 登记册
command grep -nE "[0-9][–][0-9]" ren-ming-biao.md shu-yu-biao.md
# W3 并列顿号
command grep -rnE "》、《|”、“" --include="*.md" a/ b/ c/ d/ e/ f/ g/ h/ i/ j/ k/ l/ m/ n/ o/ p/ q/ r/ s/ t/ u/ v/ w/ x/ y/ z/ 1/
# W4 半角三点
command grep -rnE "[^.]\\.\\.\\.[^.]" --include="*.md" a/ b/ c/ d/ e/ f/ g/ h/ i/ j/ k/ l/ m/ n/ o/ p/ q/ r/ s/ t/ u/ v/ w/ x/ y/ z/ 1/
# W6 括号套用
command grep -rnE "（[^（）]{0,40}（" --include="*.md" a/ b/ c/ d/ e/ f/ g/ h/ i/ j/ k/ l/ m/ n/ o/ p/ q/ r/ s/ t/ u/ v/ w/ x/ y/ z/ 1/
```

## 5. 验收判据（总验收，由收口会话独立复算）

1. `check_style.py --connector-scan`（letter 目录＋登记册＋根叙事文档）warnings 0，或余量逐条对应豁免清单；
2. W3/W4/W6 实扫余量=裁定豁免清单在案；W5 扫描记录在案；
3. `tasks` 中 `state=="s3_checked"` 计数 **0**，24 件 `revert-s3` steps 凭证齐；
4. ren-ming-biao/shu-yu-biao 非 W2 豁免面 en-dash 0；
5. `check_all` 10 项全绿、`check_quotes` 0 违例、en/ 与 yuanwen/ 零改动（git diff 验证）；
6. 全部凭证入 specs/026/execution-log.md 与各任务 JSON。

## 6. 作废条件与基准钉

* 作废：一字线裁定被新裁定取代（回滚=git revert 语料批）；基线重转（specs/018/022 面）；与本任务书冲突的新裁定即停手上报。
* 基准钉：specs/026/bin/connector-scan-baseline-20261114.json（A1 卡钉）＋本文件 §1 基线数（W1 3,072/告警 6；W2 1,762/5–6；W3 47/113；W4 11）＋ §2-4 的 24 件快照。
* 口径差异在案：1,140（他会 A1 卡钉）/1,141（specs/025 C7b）/3,072（本任务书上界）为三种口径（告警行/窄模式/全形态），对表结论随 W1 执行记录一并登记。
