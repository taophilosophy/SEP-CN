# 执行日志：009 目录与镜像归一性复核

## 2026-10-29 建档

* 用户指令："建立任务书复核 summary、mu-lu-s、yuanwen、en 文件夹内容，格式、结构的归一性"。任务书落 `spec.md`，状态 Created（待开工）。
* 开工底数实测（写入 spec 范围栏）：baseline 1878；SUMMARY 2649 链接；mu-lu-s 1888 链接；yuanwen 2427 md（gitignore，仅 6 个演示条目入库）；en/ 1880 目录（1878 词条包 + `_catalog`/`_manual`）。
* 集合预检：en/ 1878 词条包对 baseline **零缺包**；SUMMARY 与 yuanwen/SUMMARY 链接数相等（2649）。
* 已知发现基线自 007 承接（457 脚注悬空 / 46 未换行收尾 / 5 pm-notation 表格 / 232 math warn / spacetime-holearg 在途），复审维持原状不计新失败。
* 并行会话注意：mu-lu-s.md、yuanwen/SUMMARY.md、tools/yuanwen.py 等在途 staged 编辑；本战役纯本地复核，冲突处只登记归属不裁改。

## 2026-10-29 用户裁定：禁止机械复核

* 用户指令："禁止机械复核，必须确保格式的转译一致性"。已登记进 spec「约束与用户裁定」并新增「格式转译一致性」专节。
* 要点：检查器全绿（check_markdown/check_math/重转换字节一致）降级为必要非充分；重转换零漂移只证转换器确定性，不证转译正确性。
* 落地：转译规则目录 T-01…T-09（自 convert_entry 构件面归纳：区块/行内/数学/表格/列表/图/引文键/脚注补充材料/目录镜像），每条规则三级结论——形态唯一性（全库扫描）、语义保真（≥5 例人工抽样，记录词条名与比对结论）、zh 镜像兼容（结构锚点）。
* 产物新增：`bin/transpile_scan.py`（形态分布扫描器）、`results/transpile-rules.md`（规则目录与裁定）；验收标准插入为第 2 条（零未裁决项）。

## 2026-10-29 用户指令：1% 抽样逐段审阅

* 用户指令："随机抽取1%的html yuanwen en进行逐段审阅"。已登记进 spec（约束与用户裁定 / 工具 / 产物 / 验收第 6 条）。
* 方案：baseline 1878 × 1% = ceil → **19 条**；`bin/para_review.py` 复用 convert_entry 的切块路径（HEAD/TAIL_RE + extract_blocks_raw）对 `en/<slug>/index.html` 与 `yuanwen/<letter>/<slug>.md` 做全段对齐（文本骨架归一：公式→⟦M⟧、脚注引用键与文献标记剔除、md 语法剥离）；分歧段 100% 人工复核，无分歧段每条抽检 ≥3 段（最长段/含公式段/含表格或链接段）。种子 20261029 落 sampling.json，可复现。

## 2026-10-29 用户改令：全量逐段复核（长线战役）

* 用户指令："改为全量逐段复核，建立长线任务书"。1% 抽样方案作废；spec 增「全量逐段复核（长线战役）」节：A–Z 字母批、review-log.jsonl 断点、多会话字母批认领、零写入被审对象。
* 全量形状直方图即 T-01…T-09 形态唯一性扫描本体，独立 transpile_scan.py 取消并入。
* 验收第 6 条改写为全量口径：1878/1878 凭证、分歧段零未裁决、抽检 ≥3 段/条留痕。

## 2026-10-29 用户补充：确保 SUMMARY 正确

* 用户指令："新增：确保summary 正确"。登记为战役硬门槛四查：条目集=baseline、路径在盘、标题链三元组全量逐条核对（para_review 采集）、转义规则+既有门禁全绿。
* 落地：para_review.py 逐条读 SUMMARY 条目文字、zh H1、yuanwen H1，三元组比对结果入 review-log 与 <slug>.json；标题链不一致处走分歧段人工裁定。

## 2026-10-29 对齐器语义裁定（para_review.py 冒烟定标）

* 冒烟词条：abduction、pm-notation、quine（各含 dl/数学/表格/bib 小节等形态）。定标后 abduction、pm-notation 全清，quine 仅剩可归类项。
* 归一化裁定：比值阈值 **0.95**；公式定界内容双侧归一 ⟦M⟧；上下标双侧归一 ⟦S⟧/⟦P⟧（Unicode 原生字符经 SUB_MAP/SUP_MAP 反向识别，T-02 记号保真另由重转换字节复核覆盖）；pubinfo（First published…）双侧保留配对；作者行（全斜体行）双侧剔除；标题比较去强调标记（`*Principia Mathematica*` 斜体保真不算分歧）。
* 剔除对称：html `bib-container` ↔ md `References（引用注释）`节（标题+其后 h3 小节+体例说明，遇下一 h2 即止）双侧剔除——T-07 设计转换（文献全量转脚注），其保真由 baseline cite 计数与 007 重转换字节复核覆盖，不逐段比对。
* **整组合并判据**：连续非匹配区段整组比值 ≥0.95 → 记 merged 形态注记（preamble/列表/dl 的 1↔N 拆合块是转译形态，非内容分歧，T-01）；<0.95 才逐块 flag。
* 标题链判据修正：SUMMARY 条目文字 = zh H1（中文侧硬）；yuanwen H1（去强调）= html 标题（英文侧硬）；SUMMARY 用「姓, 名」引文格式系设计使然，与 html 原题词序差异不算错。
* 冒烟已知真发现：bib 段 h3 小节在 md 侧随 References 节渲染（quine 型）——已归入 References 段剔除范围，非正文泄漏。
