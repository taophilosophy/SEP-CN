# Tasks: 学术规范门禁（specs/003-academic-norms）

- [ ] T001 规范落文：`rules/07-academic-norms.md` 总纲 + `rules/adr/0006-学术规范流程.md`（证据：提交记录）
- [ ] T002 实现 `tools/check_academic.py`：硬错误/告警分级、`--docs`/`--strict`、`--root/--baseline/--tasks-dir` 注入（证据：全库首检输出）
- [ ] T003 单测 `tools/tests/test_check_academic.py` + fixtures，覆盖 US1–US4 与 Edge Cases（证据：unittest 输出）
- [ ] T004 接线登记：checks.yml 步骤 + rules/05 工具清单 + rules/README 索引与判例 + AGENTS.md 必读/预检 + tools/README 登记（证据：提交记录）
- [ ] T005 全库首检 + 证据归档（本清单勾选与首检摘要）；复跑全部门禁收尾
