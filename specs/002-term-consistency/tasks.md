# Tasks: 术语一致性检查器

**Input**: [plan.md](./plan.md)

## 1. 实现

* [x] T001 实现 `tools/check_terms.py`：两表解析（FR-001）、键规范化（D1）、冲突检测（FR-002/D2）、登记册自洽性校验（User Story 2）、报告输出与退出码（FR-003）——凭证 `tools/check_terms.py`
* [x] T002 实现 `--docs <路径>...` 定点核销模式（User Story 3）：登记册“首现”驱动，仅报告不阻断

## 2. 测试

* [x] T003 unittest：fixtures 覆盖——无冲突、互斥冲突、子集滞后、合法多译法并存、废弃链断链、重复行、缺裁定日期告警、斜体键规范化（`tools/tests/test_check_terms.py`，9 用例全过）

## 3. 接线与登记

* [x] T004 接入 `.github/workflows/checks.yml`（冲突与违例为门禁）；登记 `tools/README.md` 与 `rules/05-ci-and-tools.md`
* [x] T005 对全库两表跑一轮基线：冲突 1 条（Theophrastus：登记册“特奥弗拉斯托斯” vs 词汇表“泰奥弗拉斯特”）已按 rules/03 方向裁决——词汇表向登记册对齐，备注保留旧译并注明日期；词汇表滞后告警 1 条（absolute idealism）与缺裁定日期告警 16 条（人名节 3 列行）留登记会话补齐
