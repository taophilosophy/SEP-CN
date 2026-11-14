# 0051. reopen 分类学与在途上游同步绕过（--upstream-sync，修订 ADR-0050 边界一）

accepted | 2026-11-15（用户裁定“将 reopen 进行分类讨论，该特殊情形列为可绕过”）

## 背景

ADR-0050 统一了上游更新引发的 done 件返工（reopen --clear 置空重译），但**边界一**把 s2.5_checked 在途件排除在外（ADR-0043 状态机 reopen 仅限 done），形成双轨：done 件置空重译、在途件挂流水吸收。实操问题：在途件的 s2.5 前产物（初译、一校二校、术语校）建立在对**旧上游**的中间态上，挂流水继续会与已同步的新 en/、新 yuanwen 脱节；同一批 9 件返工两种处置亦难维护。用户裁定：reopen 分类讨论成文，在途吸收上游同步这一特殊情形列为**可绕过**。

## 决策

1. **reopen 分类学（判据表）**：

| 类 | 触发 | 起始状态 | 处置 | 依据 |
| ---- | ---- | ---- | ---- | ---- |
| R1 质量返工 | 语体/学术硬伤 | done | `reopen`（--clear 同构 ADR-0050）→ pending | ADR-0033 |
| R2 上游修订（done） | 实质修订/换血重发 | done | `reopen --clear` → 置空全量重译 | ADR-0050 |
| **R3 上游修订（在途）** | 实质修订/换血重发 | **drafted…r3_reviewed** | **`reopen --upstream-sync [--clear]` → pending**（可绕过） | **本 ADR** |
| R4 不打回 | 存根/未译；仅链接/属性/页框级 | 任意 | 不建任务；翻译自带新底稿 / 登记备查 | 派工单 2026-11-15 |

2. **R3 绕过约束（四闸）**：①`--upstream-sync` 显式声明（不留痕迹的绕过不存在）；②`--reason` 必须引用凭证（`compare/<slug>.json` 变更文件或分歧账条目）；③blocked 任务不可绕（先 `--unblock`）；④pending/cleared/done 不适用（done 走 R2、cleared 无正文、pending 已在队首）。绕过后按 ADR-0050 同构置空重译；旧 steps append-only 留史，reopen step 记 `bypass: upstream-sync（ADR-0051 R3）` 标记。
3. **与 revert-state（ADR-0043）的分工**：revert-state 是 s3+/r 链 → s2.5_checked 的受控回退（**保正文**，只重走复核）；R3 是打回 pending **置空重译**（正文作废）。判据＝上游变更是否使正文失效：实质修订/换血 → R3；仅复核面缺陷 → revert-state。
4. **task_ops 实现**：`reopen` 增 `--upstream-sync`；无 flag 时维持“仅 done”不变（禁跳步对常态流不动）；单测四则锁死（在途无 flag 拒／带 flag 过并留标记／blocked 带 flag 拒／done 带 flag 拒）。
5. **应用**：本轮 4 件 s2.5_checked（behaviorism／emotion-Christian-tradition／kant-leibniz／logic-provability）即以 `--upstream-sync --clear` 打回置空重译；ADR-0050 边界一与派工单 A2 路径自此作废（注记）。

## 后果

**正面**

* 双轨归一：上游返工不论 done/在途，一律 reopen --clear 置空重译，处置不再按任务状态分叉。
* 在途中间产物不再建立于旧上游；术语校/审计成果由登记册与分歧账兜住，重走不丢制度记忆。

**负面 / 需跟进**

* 在途校对成果作废重走，纯时间成本（用户明示接受）。
* 绕过入口凭 flag+凭证双闸约束，滥用面（把非上游原因的打回伪装成 R3）靠 reason 凭证审计兜底；核对 reason 是否引用真实变更文件列入收工检查习惯。

## 参考

* [ADR-0050](0050-上游更新引发的置空返工.md)（置空返工，本 ADR 修订其边界一）、[ADR-0033](0033-译文语体门禁.md)（reopen 先例）、[ADR-0043](0043-s2.5-checked前置阶段合并与全量回退.md)（revert-state 与禁跳步）、[ADR-0045](0045-原始物双账语义与分歧账.md)（真漂移与 carry）。
* `tools/task_ops.py`（reopen --upstream-sync）、`tools/tests/test_task_ops.py`（四则单测）。
