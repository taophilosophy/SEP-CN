# 022 执行日志（重转后基准偿还校对）

对照源钉：b20ab51b88250ad80afa79eb56012f681c6a9f06（spec.md A2）。工具在 `bin/`（scan/attach/copy_defs），结果在 `results/`。

## 2026-11-14 主会话（开卡日）

### 开工前清障（非 022 正文，但同会话完成）

* 收口上一会话遗留：UU 冲突×7（stage2==HEAD 已择优，按 HEAD 收口）、autostash 残余（45 文件逐项仲裁后吸收删库）。
* 修复数学门禁违规四处（上会话「1/！/？」提交引入）：axiom-choice C1 宏反展开回改（\sH/\inn/\amp→\mathcal{H}/\in/\mathbin{\&}，塔斯基归一人名表「塔尔斯基」×4）；risk 真公式误转义回改＋货币转义保留；logic-dynamic 分裂公式并回单式（源文 SEP 排版伪迹，551 条 C2/C5 清零）；philanthropy 货币 $100 转义。
* CI 自拦修复：checks.yml 图片报告改写 `state/`（886351ed6 起工作流自生成根目录散件被自家垃圾门禁拦，每推必红）。
* 门禁基线：check_all 9/9 绿；check_math_zh 全库 0。

### 机检 triage（scan_zh_vs_yuanwen.py，439 非存根）

* 早基线（scan-latest.jsonl）：flagged 202，marker 债 only_yw=2263/only_zh=163，sec_diff 102，defs_diff 18，tail 6。
* 收工快照（scan-20261114-b.jsonl）：CLEAN 287（+50），only_yw=534（约 400 在在途件——按范围不直改，见移交③），sec_diff 18（致谢节识别修正后塌缩），defs 15。

### 标记偿还（attach_markers.py，位点级整链替换保序）

* 第一批：151 条 done 纯机械，679 处（四检全绿）。
* 第二批：79 条混合词条机械部分，473 处；余 244 处转人工清单。
* defs 补齐＋改形后追加：9 条 139 defs 照录入位＋挂键 31 处。
* 大改形 2 条（条目式文献节→引用注释 defs，zh 零 defs 且无中国文献条目，整节替换）：immutability 37、incompatibilism-theories 129，改后挂键 19 处。
* 提交：be2393e9f（误卷他会 2 文件，见事故④）、a30f2b8fd、bcc4d28b0（10 文件 510 行，含验证）。

### 已知残留（移交清单）

1. **人工挂键 ~130 处/40 条**（done 词条）：`results/manual-worklist.json`。类：no-zh-group 46（转引自等措辞变体）、no-group 24（叙事式引注）、unplanned 8、其余零星。样例先例：environmental-aesthetics 4 键逐一定位核对后手工挂（welchman-2020 于 L125 链尾追加）。
2. **键改名类（only_zh 227 的一部分）**：重转改键，zh 须随改（marker+def 键同名改）。已实证：redistribution `o-neil-2012`→`o'neill-2012`（撇号归一）；abhidharma `cox-nd*`→`cox-2004a/b`；brouwer 12 键（018 缺陷⑤年份后缀归位）；mathematics-inconsistent `shapiro-2014`→`shapiro-nd`（ADR-0038 勘误联动）；dai-zhen `*yang*-2009` 键含星号。逐键 1:1 数目核对后改。
3. **在途件债务（约 400 处）**：cleared/s3_checked 词条 zh 由账本 compose 重生成，禁直改；债务已在 scan-20261114-b.jsonl 按 slug 列明，归各翻译/评审会话在 compose 后或账本内消化。
4. **大改形余量**：immutability/incompatibilism-theories 已完成；后续若 scan 再报 zh-no-defs 类，同法（script/022_convert_refs.py，先验无中国文献条目）。
5. **其他信号类**：ratio 极值 122 条（漏译句 hint，需回源深读）、para_mismatch 49、tail_missing 6（多为在途件尾节未组）、defs_diff 15（改键类见②）。

### 事故与对策登记

1. **并行 sweep 收编（≥5 次）**：本会话产物（022 骨架、批次 1/2 挂键）多次被并行会话「！」提交整批收编——验证入 HEAD 即可，勿重复提交；对策已录 [[sep-cn-018-yuanwen-audit]] 并行会话回滚实证。
2. **git add -u 事故（be2393e9f）**：本会话用 `git add -u` 卷入他会 2 个在途文件（09-rework-lessons.md、t023-containment.txt）且提交信息失实。史不可改（他会已在顶上），登记备查；**此后一律 pathspec add+commit**。
3. **并行 clean 扫走未跟踪件**：copy_defs.py 初稿被 git clean 删除——022 全树随即入库受跟踪保护（a30f2b8fd）。
4. **024 spec 空文件双增冲突（AA）**：两会话同建 specs/024-mathjax-v4-upgrade/spec.md；stage2/3 均 0 字节，按空收口后他会新稿（3357 字节草稿）随 a30f2b8fd 入库防丢。
5. **工具坑**：照录说明行字面 `[^key]` 被计真键（两侧措辞不一致时产生伪债）——scan/attach 已滤 `key`；`--out` 值被 args 过滤器误作 slug——已修；al-farabi-psych 属 a/ 目录，pathspec 写错 f/ 致 add 断链（逐 slug 以实际目录为准）。
