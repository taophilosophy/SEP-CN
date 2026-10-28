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
