# 004 · rules/reference/engineering-doctrine 落地映射与技术债务登记

**状态**：Draft | **创建**：2026-10-27 | **来源**：用户指令"根据 rules/reference/engineering-doctrine 里面的软件工程理论学术要求规范治理整个项目，并根据实际不断迭代，分析目前的技术债务"

## 一、Doctrine 门禁映射（G0–G5 ↔ 现行机制）

| Doctrine 门禁 | 要求 | SEP-CN 现行对应 | 状态 |
|---|---|---|---|
| G0 立项与范围 | 范围声明、ADR、目录边界 | README + rules/01（目录职责表）+ ADR-0005..0009 | ✅ 对齐 |
| G1 需求基线 | FR 编号/优先级/可测判据/证伪条件/复审日期 | specs/001-003（FR 编号 + Acceptance Scenarios + Assumptions 带日期） | ✅ 对齐 |
| G2 设计基线 | 依赖方向、接口契约、状态/错误唯一出处、关键决策 ADR | tools/ 契约（contracts/cli.md）、rules/01 目录职责、ADR | ✅ 对齐 |
| G3 实现与单元验证 | 静态零告警、全量测试、正/失败路径测试、结构门禁 | check_all 七项 + 76 单测（compare 有失败路径测试；yuanwen 转换器仅 check_math 间接） | ⚠️ 部分缺口 |
| G4 集成与验收 | 证据目录、0 信任复核（换命令/环境/角色）、结论不超证据 | specs/*/demo-log + 执行记录；compare/抓取干执行留痕 | ⚠️ 部分缺口 |
| G5 发布与归档 | 版本标签、变更记录、已知限制公开、标签不可改写 | 无版本标签机制（仅 git 提交流） | ❌ 缺口 |

## 二、技术债务登记（按优先级，依据 2026-10-27 实测）

| # | 债务 | 影响 | 量化 | 优先级 |
|---|---|---|---|---|
| D1 | 正文翻译三审三校零实跑→**已破零（2026-10-28）**：done=1（spacetime-holearg 空穴论证演示件，六道审阅全过）；批量翻译待阶段 A checklist 验收解锁（**偿还计划见 specs/005-translation-campaign**） | 项目主目标开工、进度 0.1% | 1877 词条待译（done 1/1878） | P0 |
| D2 | en/ 原始物仅存本地 → 2026-10-27 **显式豁免**（用户裁定：不备份，禁止任何备份文件，项目由 git 管理；en/ 原始物为可再生抓取物，重抓即恢复） | 已接受的风险 | en/ 约 3998 文件 | ✅ 豁免 |
| D3 | ~~74 条上游增量未接入~~ **✅ 已解除（2026-10-28）**：71 条补遗 intake 接入（apply-add 闭环，提交 1691cd9e）+ 3 条并行会话处置，缺口 74→0；71 个 retranslate 任务建立（转入 D1 主攻） | SUMMARY 与官方目录缺口闭合 | 0/74 待接入 | ✅ 已解除 |
| D4 | 24 个派生 slug + 137 个导航节点待人工裁定 | 镜像路径不确定、目录导航节点无条目页 | rebuild-review.json；已个例裁定 aristotelianism-renaissance 等（specs/001 执行日志），整体待清 | P1 |
| D5 | ~~baseline zh_doc 对 72 条 baseline 独有条目仍是旧拼音路径~~ **✅ 已解除（2026-10-28）**：intake apply-add 闭环重写 zh_doc；实测 1878 条 zh_doc 全部为字母目录形态、异常 0（nominalism-metaphysics 存档版 zh_doc=None 属存档词条固有，非路径漂移） | 版本钉链恢复 | 异常 0/1878 | ✅ 已解除 |
| D6 | ~~yuanwen.py（660 行最复杂转换器）无直接单测~~ **✅ 已解除（2026-10-28）**：tools/tests/test_yuanwen.py 17 项直接单测（公式实体、脚注锚点、嵌套表格、跨块 display math、图题、PDF 注释剥离），随管线单元测试门禁全绿 | 保真判据双层化（金样本断言 + 全量 check_math） | 17 项专项测试 | ✅ 已解除 |
| D7 | mu-lu-s 手编分类单点维护、无自动分类辅助 | 每次新增条目累积分类缺口（2026-10-28 实测 73 条正式条目：原 21 + intake 新条目） | 1817 行 | P2 |
| D8 | VitePress 双语站未在新结构下构建验证 | 发布链路未验证 | config.mts/theme 大改后未跑 | P2 |
| D9 | tasks 非标准状态（round1_augmented、演练复位）不在状态机枚举 | progress.py 报"非标准状态" | 2 个任务 | P2 |
| D10 | 无版本标签机制（G5 缺口）→ 2026-10-27 已补：里程碑 tag `v2026.10.27-目录重建定型` | 发布/回退有锚点 | tag 机制就位 | ✅ 已解除 |
| D11 | compare.py 移动节判定粗（仅"同标题异锚"） | 移动类变更可能误报为增删 | — | P3 |
| D12 | specs/001 网站结构事实基础（2026-10-26 抽样）已过时 | 规格领域事实与现结构漂移 | 部分 | P3 |
| D13 | package.json / node_modules 未在治理层登记（07-delivery 编码卫生） | 依赖无 lockfile 治理 | VitePress | P3 |
| D14 | ~~yuanwen 脚注定义名错位~~ **✅ 已解除（2026-10-28）**：convert_notes 改按注段锚点 id（`<div id="note-N">` 或回链 `<a id="note-N">`）切段取名，1727 条全量重转换后引用-定义零悬空 | 脚注跳转恢复 | 原 646 文件 / 3931 引用 | ✅ 已解除 |
| D15 | ~~yuanwen 图片接线缺失~~ **✅ 已解除（2026-10-28）**：inline `<img>` 一律接线 `![](../assets/<slug>/…)`（含标签的伪公式护栏另见 D16）；路径统一 `../assets/`（ADR-0010）；资产复制过滤为图片类（local.js 历史误复制清除）；227 缺失目录随全量重转换补齐 | 图片全量可见、引用可解析 | 原 10019 图 / 227 目录缺 | ✅ 已解除 |
| D16 | ~~yuanwen.py 块游走器吞章~~ **✅ 已解除（2026-10-28）**：真因为上游漏写 `</p>` 时深度配对永不归零（非 toc div 配平问题），`_find_close` 对 p 采用隐式闭合语义（`</p>`/`</li>`/下一块级开标签即闭合）；公式保护加护栏（含 HTML 标签或超界的未配对定界符不暂存，typelogical 40KB 吞段根因）；63 补充材料缺件随重转换补齐 | 正文完整性恢复（aquinas §2–13 等回位） | 原 19+63 文件 | ✅ 已解除 |
| D17 | 上游双重转义实体（`&amp;rsquo;` 等）随转带入 md | 上游编辑噪声，忠实带过 | 26 文件 | P3 |
| D18 | yuanwen 侧镜像占位（未抓取词条）**裁定保留（2026-10-28）**：维持 yuanwen/SUMMARY.md 链接可解析；占位仅允许对无 baseline 实体的 slug 存在，覆盖实体件的事故（18thGerman）已修复并重转换；2 个无 zh 对应孤儿已删 | 口径已定：保留 + 禁覆盖实体件 | 134 个 | ✅ 已解除 |
| D19 | `AutoCorrect.yml` 仍用 yarn 全局安装（ADR-0014 已统一 bun：md-padding 已迁移，此流遗漏） | 工具链双轨、与 ADR-0014 冲突 | 1 个工作流 | P2 |
| D20 | `create-pdf.yml` 检出第三方仓库 `FreeBSD-Ask/gitbook-pdf-export` 并向其 push tag / 发 Release（手动触发即写外部仓库） | 误触即污染他人仓库 | 1 个工作流 | P1 |
| D21 | 根级 `sm.xml` 实为上游 404 页面快照（`<title>Document Not Found</title>`），已入库 | 仓库杂物、易被误认为站点地图 | 1 文件 | P3 |
| D22 | `tasks/` 根级非字母目录 JSON：`ci-hui-biao.json`（kind=glossary-maintenance）按路径规则（`tasks/<首字母>/<slug>.json`）不被 `task_ops` 读取；`term-candidates.json`、`term-pool.json` 为术语工作池，未登记归属 | 任务操作对根级记录不可见 | 3 文件 | P2 |
| D23 | 许可证二义：README/package.json/CONTRIBUTING 为 BSD-2-Clause，`qian-yan/ban-quan-shuo-ming.md` 写 BSD-3-Clause | 发布许可表述不一致 | 1 处 | P2 |

## 三、Doctrine 落地路线（不计成本建议）

1. **G5 补齐**：引入版本标签机制——每个稳定里程碑打 `v<YYYY.MM.DD>-<说明>` tag 并 push（tag 不可改写）；发布说明指向可复现提交哈希；已知限制清单入 README 或 RELEASE-NOTES。改动小、收益大（回退锚点 + G5 门禁闭环）。
2. **G4 强化（0 信任复核制度化）**：每批翻译 done 后，用"换命令/换环境"复算——`baseline_audit --all` + 随机抽 3 个词条用独立命令重算转换并 diff compare 结果；结论与证据不符即回炉。现有 evidence 字段已可承载，补一条规则（rules/06 质量门）即可。
3. **D2 解除（不计成本首推）**：en/ + baseline/ 建立私有备份——方案 A：私有 GitHub 仓库作原始物镜像（每日 push --mirror 或脚本增量推送，注意 SEP 内容许可 CC BY-NC-SA 的私有存档例外）；方案 B：S3/R2 对象存储版本化桶（成本极低、不可变版本化天然契合"不可变原始物"）；方案 C：异地冷备（rsync 至另一磁盘/NAS）。三者可叠加：本地 + 对象存储 + 异地。
4. **D6 解除**：为 yuanwen.py 建金样本单测（tools/tests/fixtures 已有 9 个词条 HTML）——断言转换产物包含全部公式定界符内容、脚注配对数、表格数、图片引用数；把 check_math 的全量门禁降为"金样本精确断言 + 全量抽样"双层。
5. **D1 主攻**：按 rules/04 三审三校实跑首批 5 个词条（含重数学/含图/含脚注各一），以 doctrine G3/G4 门禁记录格式（逐条判据 + 证据 + 未通过项）写入任务 JSON，作为翻译工作流的首次 G4 验收。
6. **迭代纪律**：每存档季（3/6/9/12 月 21 日）跑 fetch_catalog + compare 全量 → 变更进 update 队列 → 技术债务登记表复审（本文件更新复审日期）。

## 四、复审

* 复审日期：2027-01-21（下个存档季）。
* 未通过项：D1 为主攻项，D4/D7/D8 按批次消化；D2 豁免维持，其余已解除。
* 2026-10-28 yuanwen 全量复核（1727 主文 + 427 补充材料，逐文件：结构/乱码/图片/数学/脚注/完整性）：乱码与 UTF-8 解码零缺陷；24 件哈希漂移已用现工具重转换归零、SUMMARY 镜像已同步；抽读 abduction/tarski/japanese-aesthetics/aquinas/aristotle/algebra 等定性；新增 D14–D18。
* 2026-10-28 二次全量复核（1878 主文 + 546 补充材料，D14–D16 修复后全量重转换）：转换器级缺陷全部归零；新发现并修复补充材料站点导航渗漏（convert_supplement 缺切片，374 件含 Browse/About/Support SEP 导航）；三样本段落级抽读通过（alcmaeon 30 段 1:1、algebra 源公式 850 全在案、japanese-aesthetics 33 图 1:1）；余 60 项均为上游固有噪声（断锚 33/双转义实体 15/注释资产 8/小文件边界比率 2/未配对定界符字面量 2），已逐类定性登记。审计脚本与明细：%TEMP%\yuanwen_audit.py。
* 2026-10-28 三轮复核（登记表复审，批准执行）：check_all --all 9/9 全绿（含基线完整性审计与英文镜像深度复核）；D3 实测解除（上游增量 74→0：71 intake + 3 并行处置，71 个 retranslate 任务转入 D1）；D5 实测解除（1878 条 zh_doc 全字母目录形态、异常 0）；D6 实测解除（test_yuanwen.py 17 项直接单测）；D10 标签在位确认；D1 更新为 done=1/1878（spacetime-holearg 空穴论证演示件，战役进度 0.1%）；D7 缺口实测 73（check_mulu_s 第[3]节）；D4 补个例裁定记录。
* 2026-10-28 仓库 Wiki 折叠审计（ADR-0015）：`.qoder/repowiki` 63 个文件按 7 模块零信任比对（3 模块并行子代理、4 模块主线直接核验）；回灌站点构建知识至 `.vitepress/README.md`、运行/门禁口径至 rules/05 与 CONTRIBUTING、目录职责补齐至 rules/01；权威层随审计修正门禁计数（六项+单测）、任务路径、CI 触发、lint 命令、AGENTS 进度数字；新增 D19–D23。
