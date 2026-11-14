# 023 战役执行台账 — 索引

协议见 `../spec.md`。每词条一行双轴台账在 `ledger-<letter>.md`；本文件只记阶段进度、基线钉与会话接力点。

## Phase 1 转换器先修（A4）

**状态（2026-11-14 08:50 会话 1）**：020 移交清单在现行转换器下**表格轴全部清零**——

* 会话 1 以内容级包含性对账（`bin/t023_containment.py`）复测 020 清单 26 词条：en 顶层表每行内容（含嵌套行）在 yw 全文归一化后全部在场，丢失 0。
* 过程中重转了 7 个滞后词条（logic-connexive、lukasiewicz、nonwellfounded-set-theory、pm-notation、proof-theory-development、zeno-elea、presupposition）验证现行代码。
* 单行折叠（嵌套表透传段压成单行，防外层 md 表撕裂）由并行会话 2026-11-14 上午实现并配单测（`tools/tests/test_yuanwen.py` TestNestedTables20261114）。
* 诊断过程中排除的假阳性模式（登记备查）：学术工具三行豁免、注释内弃用表（logic-deontic 表0）、引注标记行内插入、图片 alt 文本插行、`<=`/`<t` 字面与裸 `<[^>]+>` 剥标签的跨行吞吃、上下标 Unicode 未折半角。
* 图片轴 13 件待 Phase 1 收尾复跑 `script/t020_img.py`。

**全量重转收口（2026-11-14 会话 1）**：

* `--all-baselined --summary`：1872 转换 0 失败，summary 链接改写 0；他会已于当日晨以同代码全量重转入库（baseline converted_at 00:28–01:06 其时钟），本会话幂等复跑仅 17 文件差（他会 015 偿还轴定点重转），重转产物状态与 HEAD 一致。
* 归一化回归扫描（备份 vs 现行）：**2420 未变 / 1 OTHER / 增删 0**。OTHER 唯一例 `e/epistemology-evolutionary.md`：备份侧 `\frasl` 为手改漂移，重转后回归 en 源原形 `\frac{p_i \cdot w_i}{\overline{w}}`（已对 en 逐字核对，转换器输出正确，漂移纠正）。
* 图片轴 13 词条逐件定性（`bin/t023_img_qualify.py`）：25 处「镜像缺图」全部为 PDF 注释内专用图（转换器剥注释正确，镜像=Web 版语义）＋5 处 yw 在场（t020_img 只认 md 图语法，工具视野限制）。**020 图片轴真缺陷 0**。
* **开放阻塞**：specs/024 登记 `bun run build` 对重转内容为红（nonwellfounded-set-theory、typelogical-grammar 在 Vue 编译层报缺闭合/非法闭合标签）。023 复现排查进行中（protectMath 无嫌疑、透传 HTML 标签平衡已验证），待全量构建日志定位；修复归本战役（转换器内容或 math-plugin 白名单加固二选一）。

## 基线钉

| 钉 | 提交 | 说明 |
| ---- | ---- | ---- |
| 旧 | b20ab51b8 | 022 立卡时钉（ADR-0038 重转后） |
| 新 | 97563ee02 | 023 Phase 1 全量重转收口（嵌套表透传＋单行折叠＋li/dd 内表；幂等复跑 1872/0 失败验证与工作区一致） |

## 覆盖进度（Phase 2 逐条三向审校，随做随更）

范围：tasks state ∈ drafted 及其后（A2，≈422 条；cleared 不入列）。镜像轴沿用 018 已核 10 条（A5）。

| 字母 | 范围词条 | 已审 | 发现项 | 台账 |
| ---- | ---- | ---- | ---- | ---- |
| （未开始） | | | | |

## 会话接力点

- 2026-11-14 会话 1（本会话）：战役立案（spec + 用户四裁定 A1–A4）；018/022 冻结移交注记；020 清单复测清零；全量重转进行中。
- 接力规则：后继会话先读本索引，再读当前字母台账末尾「接力指针」，禁止跳条。
