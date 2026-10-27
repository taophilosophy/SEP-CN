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
| D1 | 正文翻译 done=0——管线全就绪但三审三校零实跑（**偿还计划见 specs/005-translation-campaign**） | 项目主目标未开始 | 1791 词条待译 | P0 |
| D2 | en/ 原始物仅存本地 → 2026-10-27 **显式豁免**（用户裁定：不备份，禁止任何备份文件，项目由 git 管理；en/ 原始物为可再生抓取物，重抓即恢复） | 已接受的风险 | en/ 约 3998 文件 | ✅ 豁免 |
| D3 | 74 条上游增量未接入（**随 specs/005 各波 intake 偿还**） | SUMMARY 与官方目录缺口 | upstream-increment.json | P1 |
| D4 | 24 个派生 slug + 137 个导航节点待人工裁定 | 镜像路径不确定、目录导航节点无条目页 | rebuild-review.json | P1 |
| D5 | baseline zh_doc 对 72 条 baseline 独有条目仍是旧拼音路径 | 版本钉链断 | 72/1724 | P1 |
| D6 | yuanwen.py（660 行最复杂转换器）无直接单测 | 数学/表格/脚注保真仅靠 check_math 间接把关 | 0 专项测试 | P1 |
| D7 | mu-lu-s 手编分类单点维护、无自动分类辅助 | 每次新增条目累积分类缺口（当前 21 条） | 1810 行 | P2 |
| D8 | VitePress 双语站未在新结构下构建验证 | 发布链路未验证 | config.mts/theme 大改后未跑 | P2 |
| D9 | tasks 非标准状态（round1_augmented、演练复位）不在状态机枚举 | progress.py 报"非标准状态" | 2 个任务 | P2 |
| D10 | 无版本标签机制（G5 缺口）→ 2026-10-27 已补：里程碑 tag `v2026.10.27-目录重建定型` | 发布/回退有锚点 | tag 机制就位 | ✅ 已解除 |
| D11 | compare.py 移动节判定粗（仅"同标题异锚"） | 移动类变更可能误报为增删 | — | P3 |
| D12 | specs/001 网站结构事实基础（2026-10-26 抽样）已过时 | 规格领域事实与现结构漂移 | 部分 | P3 |
| D13 | package.json / node_modules 未在治理层登记（07-delivery 编码卫生） | 依赖无 lockfile 治理 | VitePress | P3 |
| D14 | yuanwen 脚注定义名错位：convert_notes 从 notes.html 回链目标（index.html#ref-N）取名 → md 定义为 `[^note-ref-N]`，正文引用按 `notes.html#note-N` 为 `[^note-N]`，引用-定义对不上 | 脚注跳转断裂（工作底稿层） | 646 文件 / 3931 引用悬空（2026-10-28 全量复核实测） | P1 |
| D15 | yuanwen 图片接线缺失：正文未生成 `![](…assets/<slug>/…)` 引用（en 源 10019 个 `<img>`/2154 文件未接线）；已接线文件路径混用 `assets/`（错）与 `../assets/`（对，md 位于 `<letter>/` 子目录）；227 条 baseline 记图但 `yuanwen/assets/<slug>/` 未复制 | 图片在镜像中不可见，与 ADR-0009"md 内相对引用"不符 | 10019 图 / 227 目录缺 | P1 |
| D16 | yuanwen.py 块游走器对 div 不配平的源 html，`toc` skip 区闭合搜索越界吞章（aquinas 丢 §2–13、set-theory 丢 §4 等 19 文件，丢 10–25% 正文）；另 22 文件 h2 含行内公式整行标题被丢；63 补充材料（figdesc 等）无 md；xymatrix/multline 少量公式丢失 | 正文完整性缺陷，含 git 跟踪演示件 set-theory | 19+22+63+11 文件 | P1 |
| D17 | 上游双重转义实体（`&amp;rsquo;` 等）随转带入 md | 上游编辑噪声，忠实带过 | 26 文件 | P3 |
| D18 | yuanwen 侧 136 个 9 字节占位（未抓取词条镜像占位，2026-10-27 06:31 批量生成，工具与规则均无此功能来源）；曾覆盖 18thGerman 实体件（已修复）；其中 2 个无 zh 对应（已删）；占位去留待裁定 | 镜像一致性口径未定 | 136 个 | P3 |

## 三、Doctrine 落地路线（不计成本建议）

1. **G5 补齐**：引入版本标签机制——每个稳定里程碑打 `v<YYYY.MM.DD>-<说明>` tag 并 push（tag 不可改写）；发布说明指向可复现提交哈希；已知限制清单入 README 或 RELEASE-NOTES。改动小、收益大（回退锚点 + G5 门禁闭环）。
2. **G4 强化（0 信任复核制度化）**：每批翻译 done 后，用"换命令/换环境"复算——`baseline_audit --all` + 随机抽 3 个词条用独立命令重算转换并 diff compare 结果；结论与证据不符即回炉。现有 evidence 字段已可承载，补一条规则（rules/06 质量门）即可。
3. **D2 解除（不计成本首推）**：en/ + baseline/ 建立私有备份——方案 A：私有 GitHub 仓库作原始物镜像（每日 push --mirror 或脚本增量推送，注意 SEP 内容许可 CC BY-NC-SA 的私有存档例外）；方案 B：S3/R2 对象存储版本化桶（成本极低、不可变版本化天然契合"不可变原始物"）；方案 C：异地冷备（rsync 至另一磁盘/NAS）。三者可叠加：本地 + 对象存储 + 异地。
4. **D6 解除**：为 yuanwen.py 建金样本单测（tools/tests/fixtures 已有 9 个词条 HTML）——断言转换产物包含全部公式定界符内容、脚注配对数、表格数、图片引用数；把 check_math 的全量门禁降为"金样本精确断言 + 全量抽样"双层。
5. **D1 主攻**：按 rules/04 三审三校实跑首批 5 个词条（含重数学/含图/含脚注各一），以 doctrine G3/G4 门禁记录格式（逐条判据 + 证据 + 未通过项）写入任务 JSON，作为翻译工作流的首次 G4 验收。
6. **迭代纪律**：每存档季（3/6/9/12 月 21 日）跑 fetch_catalog + compare 全量 → 变更进 update 队列 → 技术债务登记表复审（本文件更新复审日期）。

## 四、复审

* 复审日期：2027-01-21（下个存档季）。
* 未通过项：D1/D2/D10 为本登记表的主攻项；其余按批次消化。
* 2026-10-28 yuanwen 全量复核（1727 主文 + 427 补充材料，逐文件：结构/乱码/图片/数学/脚注/完整性）：乱码与 UTF-8 解码零缺陷；24 件哈希漂移已用现工具重转换归零、SUMMARY 镜像已同步；抽读 abduction/tarski/japanese-aesthetics/aquinas/aristotle/algebra 等定性；新增 D14–D18。
