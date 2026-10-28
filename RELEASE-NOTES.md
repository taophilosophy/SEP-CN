# Release Notes

本文件是发布与归档（engineering-doctrine G5 门禁，ADR-0016）的发布说明登记处：每个稳定里程碑打**不可改写** tag（`v<YYYY.MM.DD>-<说明>`），并在本文件登记增量覆盖、验证凭证与已知限制。已知限制的权威清单以 `specs/004-engineering-doctrine/spec.md` 技术债务登记表为准，本文件只做发布视图摘要，不复制细节。

## v2026.10.27-目录重建定型

**tag**: `v2026.10.27-目录重建定型` ｜ **日期**: 2026-10-27 ｜ **状态**: 已发布

### 本增量覆盖

* 词条目录结构定型：A–Z 字母目录 + SEP slug 单文件（ADR-0005 → 0007 → 0008 → 0009 演进链，取代关系见各 ADR 状态行）。
* 双库镜像：`yuanwen/<letter>/<slug>.md` 与中文侧逐字符一致；英文镜像深度复核通过（`en_integrity.py`）。
* 抓取完整性收敛：`fetch_audit.py` 引用闭包迭代至不动点。
* 管线职责权属契约化：specs/001 `contracts/cli.md` 八项唯一入口。
* 基础设施：宪法 v1.0.0、rules/01–07、门禁六项 + 单元测试全绿、学术规范挂钩实拦（ADR-0006）。

### 验证凭证

* `python tools/check_all.py` 全绿（六项门禁 + 管线单元测试）。
* 英文镜像复核：`specs/001-sep-sync-pipeline/en-integrity-full.json`。
* 抓取完整性：`specs/001-sep-sync-pipeline/fetch-audit-full.json`。

### 已知限制（以 specs/004 登记表为准，2026-10-28 快照）

* 开放债务：D1（首轮翻译主攻进行中）、D4（派生 slug 与导航节点裁定）、D7（mu-lu-s 手编分类缺口）、D8（双站构建验证）、D9（任务非标准状态）、D11–D13、D17（上游双转义实体带过）、D19–D23（工具链与许可一致性）。
* 已解除或显式豁免：D2（原始物备份豁免）、D3、D5、D6、D10、D14–D16、D18。

## 发布流程（新里程碑登记模板）

1. 收工全绿：`python tools/check_all.py --all`（九项）。
2. 打 tag：`git tag v<YYYY.MM.DD>-<说明>`，随分支与 tag 一起 push（tag 不可改写）。
3. 在本文件顶部新增一节：tag、日期、本增量覆盖（ADR/规格链接）、验证凭证（命令与产物路径）、已知限制（指向 specs/004 开放项）。
4. 发布说明逐句对照证据，无超出证据的能力声明（G5 退出判据）。
