# 验收检查点（specs/005 规划书 G4）

判定纪律：逐条二值（通过/不通过），不写"基本通过"；每条通过项附证据（命令+输出摘要+产物路径）；0 信任复核用换命令/换环境重算。

## 备份豁免（2026-10-27 用户裁定）

- [x] 不备份：禁止任何备份文件，项目由 git 管理（specs/004 D2 显式豁免）

## Wave 0 工作流验收（5 词条）

- [ ] 5 任务 done，全步骤 actor/at/evidence 齐全
- [ ] 学术挂钩：s3/r3 每次advance实触发记录（含至少 1 次拦截→修复→unblock 全过程）
- [ ] logic-classical：1545 处行内公式逐一可见（check_math 0 硬错误）
- [ ] bayes-theorem：25 表格齐、脚注 [^key] 配对 0 孤儿
- [ ] action-perception：3 图 + 图注齐，"reprinted with permission" 来源标注
- [ ] set-theory：补充材料入译文且互链有效
- [ ] FR-005 金样本单测落地（D6 解除）
- [ ] `vitepress build` 0 错误（D8 解除）
- [ ] 暴露问题回流规划书（修订 diff 可查）

## 每词条 done（逐词条通用）

- [ ] 状态机 r3_reviewed → done（禁止跳步）
- [ ] `check_academic --docs <路径> --strict` 0 硬错误
- [ ] `check_style` 0 issue + markdownlint 绿
- [ ] 版本事实行与 baseline pubinfo 一致
- [ ] 参考文献照录不译、引注/定义 0 孤儿
- [ ] 结论不超证据：随机复核 1 处译文与英文源对照

## 每波收口

- [ ] 该区词条 100% done 或 blockers 登记（数量与原因）
- [ ] `check_all` 全绿（并行 7 项 + 单测）
- [ ] intake 报告入 specs/001（summary_sync report 清空）
- [ ] G4 门禁记录入 execution-log（doctrine 最小字段）
- [ ] 0 信任抽查：随机 3 词条换命令重算 diff 一致

## 全程验收（2027-06-21 夏存档）

- [ ] 1791 词条 done（PROGRESS.md 佐证）
- [ ] 74 条 intake 全接入（镜像 1872/1872）
- [ ] specs/004 登记表 13 项全部"已解除（证据）"或"显式豁免（理由）"
- [ ] 4 次存档季比对报告齐备，漂移 100% 进 update 队列
- [ ] 全程 G4 门禁记录齐备（execution-log）
- [ ] 终版 tag + 已知限制清单发布
