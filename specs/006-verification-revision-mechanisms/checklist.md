# 验收检查点: 全流程一致性验证与修订机制（specs/006）

**生成**：2026-10-27 | **规则**：每条一行、二值判定、生成时不勾选（勾选权归复核人，[x] = 判据经复核通过）
**格式**：`- [ ] Check N: <可判定事实>（来源：spec FR-x／Task N）`

## 第一层：实现完整性

- [ ] Check 1: 批次核验组织层可运行——对任一批次（1 或 a–z）执行三类核验后，`specs/006-verification-revision-mechanisms/reports/<batch>.json` 存在且含 findings/coverage/verdict 字段（来源：Task T003 / 契约 1）
- [ ] Check 2: 差异项在批次报告中携带状态机字段 silent→ruled→fixed→closed，且收口批次内 silent 项计数为 0（来源：Task T004 / 契约 2 / SC-001）
- [ ] Check 3: 结构化复核记录含 subject/doubt/ruling/evidence_anchor/reviewer/recomputed 六字段，至少一批次有实例试运行（来源：Task T005+T018 / 契约 4）
- [ ] Check 4: 中英节序列批量对照可运行——批次内每词条输出节数量/顺序/标题对照结果（来源：Task T011+T012 / 契约 1）
- [ ] Check 5: 变更记录含 open→claimed→closed 状态与处理人/方式/验证证据字段（来源：Task T015 / 契约 3）

## 第二层：需求覆盖

- [ ] Check 6: SUMMARY↔官方快照↔mu-lu-s 三方核验差异清单按批次出具，静默差异 0（来源：spec FR-001 / SC-001 / Task T006–T008）
- [ ] Check 7: 全部别名条目链接指向存在的目标词条目录；递归条目不产生断链（来源：spec FR-001 / US-1 验收场景 2 / Task T007）
- [ ] Check 8: mu-lu-s 覆盖 SUMMARY 全部正式条目或登记为刻意不收录，链接文本与 SUMMARY 一致（来源：spec FR-001 / US-1 验收场景 3 / Task T006）
- [ ] Check 9: 全库抓取覆盖率报告出具——审计/完整/缺省件/可补抓四项计数，可补抓 = 0（来源：spec FR-002 / SC-002 / Task T009–T010）
- [ ] Check 10: 每个被引用资产在包内或登记为缺省件，缺省件 100% 显式登记（来源：spec FR-002 / US-2 验收场景 1 / Task T010）
- [ ] Check 11: 含脚注/图片/公式词条的核验——脚注文件与图片在包内、公式源码在转换产物中原样可见（定界符规范化除外）（来源：spec FR-003 / US-2/3 验收场景 / Task T013）
- [ ] Check 12: 中英节序列对照报告覆盖批次内全部词条，不一致项 100% 显式登记或修正（来源：spec FR-004 / SC-003 / Task T012+T014）
- [ ] Check 13: 模拟修订全链演练通过——变化被检测、变更记录含节级定位、update 任务建立并闭环、演练产物清理留痕（来源：spec FR-005 / SC-004 / Task T016）
- [ ] Check 14: 存档季例行调度已登记且零噪音验证通过（无变化时报告"无变化"，无空任务）（来源：spec FR-005 / Task T017）
- [ ] Check 15: 批次复核抽查通过——存疑留痕 100%、证据锚点 100%、独立重算 0 差异（来源：spec FR-006 / SC-005 / Task T018–T019）
- [ ] Check 16: 违规判定规则已登记——改写无英文源锚点且无译注说明 → 违规回炉（来源：spec FR-006 / Task T020）

## 第三层：边界与异常

- [ ] Check 17: 官方快照自身缺口（快照有而 SUMMARY 无的条目）全部按增量登记处理，无核验流程阻塞（来源：spec Assumptions 第 1 条 / upstream-increment.json）
- [ ] Check 18: 断网环境下词条包的翻译与复核材料可离线获取（正文/脚注/补充材料/图片/公式源码）（来源：spec US-2 验收场景 3）
- [ ] Check 19: 核验器只报告不修改——差异修正全部走既有显式裁定流程（summary_sync apply-add / rebuild check / 目录门禁），核验报告本身不改动目录（来源：data-model 不变式 1 / 契约 1）
- [ ] Check 20: 批次并行无耦合——多会话各自认领批次，核验报告无共享进行中状态，账本经版本库同步（来源：契约 5 / specs/005 会话协议）
- [ ] Check 21: 不建立任何备份文件（用户 2026-10-27 裁定；check_junk 根级 HTML 与 .bak 规则 0 命中）（来源：spec Assumptions 第 4 条）

## 第四层：既有功能未回归

- [ ] Check 22: `python tools/check_all.py` 全绿（七项门禁 + 单元测试）——既有门禁不被本 feature 增量工具绕过或破坏（来源：Task T002+T021 / plan Constitution Check）
- [ ] Check 23: 现有目录修正流程不受影响——check_summary / check_mulu_s / rebuild check / summary_sync 行为与 spec/005 批次账本兼容（来源：research.md 机制盘点 / Task T003）
- [ ] Check 24: 现有转换与比较工具行为不变——compare.py / yuanwen.py / check_math 的既有输出与测试保持通过（来源：research.md FR-003 行 / Task T011）
- [ ] Check 25: 学术规范挂钩不回归——task_ops s3/r3 的 check_academic 拦截行为保持（来源：rules/07 衔接表 / Task T020）
