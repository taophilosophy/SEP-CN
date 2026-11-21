# specs/055 执行日志

## 2026-11-21 全程（单会话）

### 预览阶段

* 开工：与 origin/main 同步（behind 0）；`check_all` 基线 17 项中 G3 红＝并行会话在途 inquiry 行未重建 mulu-map（first_diff_line 1718），登记不越权修复，后随本线重建消解。
* 联网核实（用户指令"绕过礼貌抓取"，无间隔）：SEP 官方无公开分类体系（词条页/搜索页实测）；PhilPapers 挂载点逐页核实 8 处——决策论与博弈论→行动哲学、道德心理学→行动哲学＞实践理性、技术→计算与信息、化学→物理科学、医学→科学哲学杂类（有类）、教育→社会科学哲学（有类）、环境→应用伦理、文化→社会政治。
* 两案骨架（`build_skeletons.py`，守恒 1883=1883）：案一 PP 骨架＋本地细分（六区）；案二 现行四区＋校准标记（16 疑位热点、4 小节）。产出 skeleton-scheme1-pp.md／skeleton-scheme2-calibrate.md／skeleton-stats.json。
* 用户选型（2026-11-21）：**案一**；史区人物簇也按重要性/影响力（016 生年序作废）；史区 H2 断代保留时间序。

### 执行阶段

* 映射模型（`build_mapping.py`）：区域优先＋确定性锚定表（S1_TONG2/S1_LANG3/S1_ETH3/S1_SCI2），规则号 R0–R9 逐行入 TSV 依据列；1883 行全量（1873 计划＋10 前言/关于原样）。
* 排序模型：四级档 S（28 个学科枢纽）→A（98 个经典专题）→B（其余）→C（154 嵌套簇成员随母条不排序）；档内 SEP 原题英段字母序平位；标题节点级序 NODE_ORDER 显式子序表（17 个父节按重要性重排，未列出者保持现行序稳定）。史区人物簇按档位重排（柏拉图/亚里士多德/苏格拉底居前等）。
* 节注迁移：26 行 `>` 节注全部随节迁移；悬注归属规则修正为"上方最近标题"（预览阶段曾误挂下一标题且文件尾 2 行丢失，已修）；3 处旧路径引用同步修订（哲学通论／女性主义哲学→价值理论／性别种族性；政治哲学／政治理论→政治与社会哲学／政治理论；伦理学／应用伦理学→价值理论／应用伦理学）。
* 试金石：`write_mulus.py --dry` 试写核读行动哲学区／古典希腊重排／前言原样／节注修订，四处全符。
* 写回：`--apply` 守恒自检（1883 进=出、零重复、missing/extra 双空）后覆写 `mu-lu-s.md`（2911 行）。
* 门禁：`check_mulu_s` 五项全绿；`--build-mulu` 重建 mulu-map（1883 行、fixed 1028）后 `catalog-net` G1–G4 全绿；`check_all` **17 项全绿**（一次 unittest 假红为本会话试写产物 results/mulus-new.md 触发 docsize＋临时目录竞态，删除产物后复跑全绿）。
* 提交（按批）：预览产物 7d092a8f4、行尾修复 7939a7fc6、写回主提交见 git log。

### 发现登记（不越权处置）

* **标题缺陷三处**（SUMMARY 域，非本 spec 范围）：`kochen-specker`（"ks 定理）"前缀残段）、`logic-provability`（作者括注截断"（Rineke"）、`feminism-objectification`（作者括注截断"（Evangelia"）——mu-lu-s 文字跟随 SUMMARY，属 017 授权的标题体例修复线，另轮处置。
* 环境：骨架/映射两脚本首轮 write_text 未指定 newline 产生 CRLF 工作副本（入库 blob 已被 eol=lf 归一），补 `newline="\n"` 重生成，工作区与库内均 LF。

### 产物清单

* `bin/build_skeletons.py`（两案骨架）、`bin/build_mapping.py`（映射＋排序模型）、`bin/write_mulus.py`（对账写回器）
* `results/`：skeleton-scheme1-pp.md、skeleton-scheme2-calibrate.md、skeleton-stats.json、mapping.tsv（1883 行×8 列含依据）、plan.json（写回计划正典）、write-preview.md、review-clusters.txt（125 簇复审清单）、execution-log.md（本文件）
* 试写产物 mulus-new.md 已按 docsize 门禁要求删除（可由 plan.json 重生成）

## 2026-11-22 遗留问题处置（用户指令“解决遗留问题”）

### 发现一改判：三处“标题缺陷”系审计误报（en_key 启发式假象）

* 取证：`kochen-specker`／`logic-provability`／`feminism-objectification` 三条在 SUMMARY.md、词条 H1、新旧 mu-lu-s 四处逐字一致且完整；SUMMARY 实为“科亨-施佩克尔定理（KS 定理） The Kochen-Specker Theorem (Carsten Held)”“…(Rineke (L.C.) Verbrugge)”“…(Evangelia (Lina) Papadaki)”，无残段、无截断；连接号短横线与全库同类标题（弗雷格-希尔伯特争论、爱因斯坦-波多尔斯基-罗森论证）惯例一致。
* 根因：mapping 生成器 en_key 启发式两缺陷——`rfind(" (")` 在作者名含内嵌括号（(L.C.)、(Lina)）时截断；英文段起算于首个 ASCII 字母，撞上全角注记段“（KS 定理）”内的字母。三者皆 review-clusters.txt 审查清单的显示假象，非库内数据缺陷。
* 处置：SUMMARY/词条/门禁零改动；en_key 重写为双规则（①跳中文字题与全角括号注记段；②作者段＝串尾最外层括号平衡组），回归测试 `bin/test_en_key.py` 九例全过（含沙夫茨伯里/皮科全角注记与方括号剥离既有行为对照）。
* 重放对账：对 00ee29e44^ 旧版 mu-lu-s 重放全管线，产物 diff 仅 4 行 en_key 归正（第四条 `social-procedures` 同属内嵌括号族），写回增量仅 kochen-specker 一行移位（新节内按真英文题字母序归位），其余三键排序位不变；mulu-map 重建，G3/G4 全绿。

### 发现二（事故登记）：共用工作树 checkout 误收事件

* 事件：重放周期用 `git checkout 00ee29e44^ -- mu-lu-s.md` 还原旧版输入，暂存区旧文件被并行会话 s25 提交（ca31f15d8，10:06:17）扫入库，分支上 mu-lu-s 被回退、G3 变红（mulu-map 新、文件旧）。
* 修复：重放完成后原子提交 6e701789b 恢复新结构＋mulu-map 同步重建，已推送，G1–G4 全绿；对 00ee29e44 的净增量＝kochen-specker 一行移位。
* 归因（rules/08 §10 四元组）：共树并行会话高频提交（s23/s24/s25 间隔约 6 分钟）＋本会话 checkout 带路径参数（暂存区污染面暴露给并行提交）。防线：共用工作树禁 `git checkout <commit> -- <path>`／任何按路径的版本还原——重放类操作一律走临时 worktree（`git worktree add`）或先把输入物复制到 spec bin/results 副本；与 [[sep-cn-parallel-session-hazards]] 现有危害族同源，已补录记忆。
* 门禁现状：本线两域（mulu_s 五项、catalog-net G1–G4）全绿；`check_all` 17 项中 `管线单元测试` 一项红，系并行会话 specs/053 线在途未提交的 `tools/yuanwen.py` 转换器改动所致（test_em_with_trailing_star_escaped），非本线领域，由其线收口。
