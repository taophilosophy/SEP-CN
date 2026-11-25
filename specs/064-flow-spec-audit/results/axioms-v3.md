# 全要素公理化证明（扩展至 v3：AX21–AX30／CT13–CT17）

- 日期：2026-11-26；对象：specs/064 rev 5（含 §12 工具链、§14 清理、§15 登记表）
- 前身：AX1–AX20／CT1–CT12 见 `axioms-v2.md` 与 `specs/063-stage-naming/results/axiomatic-completeness.md`；本文件只写新增部分与总分层的自洽检验

## 1 论域扩展

在 v2 的论域（N／Σ／C／T／R／D／S／K／M）上增加：

| 符号 | 对象 | 基数 |
| ---- | ---- | ---- |
| L | 长期登记条目 | 首批 3（catalog／errata／patches INDEX），上限不定 |
| Tt | 临时登记条目 | 本机实测量 |
| Lang | 语言集 | 3（Rust／Python／Bun） |
| Lock | 版本锁文件 | 3（Cargo.lock／uv.lock／bun.lock） |
| G | 黄金测试用例集 | = A 级工具数 26（每工具 ≥1 用例） |
| P | 实施阶段 | 12（S0–S11） |

## 2 新增公理（AX21–AX30）

| ID | 分组 | 陈述 | check |
| ---- | ---- | ---- | ---- |
| AX21 | 登记完整 | ∀e∈L∪Tt：15 字段齐；`id` 在表内唯一且不复用；`status` 在枚举内 | `registry verify`（struct） |
| AX22 | 登记单源 | L∪Tt 的 `path` 不与既有事实源重叠：`en/*`、`tasks/*`、`en-patches/*.patch` 不得为条目 path（目录级指向除外） | `registry verify --source`（struct） |
| AX23 | 时序一致 | `created_at ≤ modified_at ≤ verified_at`（null 视为不参与）；`lifecycle=session` 的 `ttl_days` 必填且 > 0；`permanent` 的 `ttl_days` 必为 null | `registry verify`（struct） |
| AX24 | 清理安全 | 删除动作仅对 `kind=temp ∧ status=expired ∧ clean_policy=expire` 成立；`protect` 条目永不删除；`--go` 为显式开关 | `registry prune`（gate） |
| AX25 | 语言边界 | 门禁判据的硬拦实现 ∈ {Rust}；跨语言只经“子进程＋`--json`＋退出码”；禁 FFI／PyO3／共享内存 | `sep check --self-audit`（struct） |
| AX26 | 版本钉 | 每门语言恰一个锁文件＋一个版本钉；钉值与 CI 一致 | CI（struct） |
| AX27 | 黄金等价 | ∀t∈A 级：G 中存在 t 的用例，且新实现通过；未通过的实现不得替换既有实现 | `run_golden.py`（gate） |
| AX28 | 缓存卫生 | 工作区中不存在未登记的临时物（`clean --check` 退出 0）；已登记条目状态与实际一致 | `clean --check`＋`registry verify`（gate） |
| AX29 | 文档形态 | 含可执行判据的规格卡三件套齐（spec＋plan＋tasks）；评估／叙事卡 spec 单卡合法；**本卡自身受此约束** | `check_doc_shape`（struct，新增） |
| AX30 | 风险可退 | 每个 P0 变更在 plan §4 有回退路径与窗口 | 人审（audit） |

## 3 新增定理

### CT13 登记计数守恒

**陈述**：|L|＋|Tt| = 登记表条目总数，且每个条目恰对应一个 `path`（除非 `status=pruned`）。
**证明**：AX21 要求 `id` 唯一，AX22 要求 path 不与事实源重叠（故非目录级条目一一对应文件）；`pruned` 条目保留记录但不指向现存文件。∎
**机检**：`registry verify` 计数。

### CT14 清理幂等

**陈述**：`prune --go` 连续执行两次，第二次为空操作。
**证明**：第一次把 `expired→pruned` 并删除文件；第二次判定时不再存在 `status=expired ∧ kind=temp` 的条目（AX24 只对 expired 生效），故无动作。∎
**意义**：与项目“对账式生成器稳定性”原则同构（幂等是清理工具的硬要求）。

### CT15 语言边界闭合

**陈述**：任一语言的实现可被独立替换而不影响其他语言，前提是 AX25 成立。
**证明**：AX25 保证跨语言交互只有进程边界（stdout／exit code／文件），无共享内存与 FFI。进程边界是弱耦合：替换一侧只要协议不变，另一侧无感。∎
**推论**：三门方案可在任意时点回退任一语言（如 Rust 某工具迁回 Python），回退成本 = 一处替换。

### CT16 迁移等价不可自证（反定理）

**陈述**：无黄金测试的迁移**不可**证明行为等价。
**证明**：语言间存在语义差异（正则方言、Unicode 归一、浮点格式、排序稳定性），这些差异不产生编译错误，只产生静默差异。要证等价必须有可观测输出对照——即黄金测试。无对照则等价命题不可判定。∎
**意义**：这是 AX27 的**必要性证明**——它把“黄金测试”从最佳实践升级为公理前提。

### CT17 体系自指一致

**陈述**：064 自身满足它规定的三件套判据（AX29）。
**证明**：064 含可执行判据（registry schema、check_all 第 22 项、golden 框架），故属“工具型卡”；现已有 spec.md＋plan.md＋tasks.md 三件。∎
**意义**：消除“规则制定者不遵守规则”的自指矛盾；也验证 §6.4 判据可执行（本卡是第一例）。

## 4 一致性与独立性

**一致性**：构造模型 𝔐″（含两表、三语言、12 阶段），逐条核验：

1. AX24 与 AX28 相容——前者管删除权限，后者管存在状态；`clean --check` 只读，不改状态。
2. AX25 与 AX27 相容——语言边界是静态约束，黄金等价是动态验收，互不干涉。
3. AX29 与既有 56 张单卡相容——判据是“含可执行判据者必须三件套”，叙事卡单卡合法，56 张不需补。
4. AX30 与“暂不开工”相容——回退路径是设计属性，不要求立即实施。

**独立性**（各配反例）：

| 去掉 | 反例 | 失效点 |
| ---- | ---- | ---- |
| AX21 | 条目缺 `ttl_days` | 过期判定不可算 |
| AX22 | 也登记了 `en/plato/index.html` | 与 entries.json 双账，漂移 |
| AX23 | `verified_at` 早于 `created_at` | 时间戳不可信，审计失效 |
| AX24 | `protect` 条目被 prune | 长期物丢失（不可逆） |
| AX25 | 用 PyO3 让 Rust 调 Python 函数 | 语言边界消失，回退成本不可控 |
| AX26 | 无锁文件 | 双机构建漂移 |
| AX27 | 跳过黄金测试直接替换 | 静默行为漂移（CT16） |
| AX28 | 未登记 `*.tmp` 残留 | 缓存累积，门禁卫生失效 |
| AX29 | 本卡只有 spec | 自指矛盾（CT17 失败） |
| AX30 | P0 变更无回退 | 事故不可逆 |

## 5 可判定性

| 公理 | 承载工具 | 需人工？ |
| ---- | ---- | ---- |
| AX21–AX24 | `tools/registry.py`（verify／prune） | 否 |
| AX25 | `sep check --self-audit`（扫源码中的 FFI 关键字与进程调用） | 否 |
| AX26 | CI（比对锁文件与钉） | 否 |
| AX27 | `run_golden.py` | 否 |
| AX28 | `clean --check` | 否 |
| AX29 | `check_doc_shape`（新，按卡类型判三件套） | 否 |
| AX30 | 人审（plan §4 表） | **是**（audit 类） |

## 6 边界（不可自证）

| # | 项 | 说明 |
| ---- | ---- | ---- |
| B8 | 黄金测试的**覆盖充分性** | 通过 ≠ 正确；只证“在该输入上等价” |
| B9 | 登记表 `purpose` 的文字质量 | 机检只验非空 |
| B10 | 语言选择的长期合理性 | 公理只保证边界可退，不保证选型最优 |
| B11 | `check_doc_shape` 的卡类型判定 | “含可执行判据”的识别是启发式（有 tools/ 或 gate 字段），可能误判 |

## 7 三层公理的分工（避免将来误并）

| 层 | 文件 | 回答的问题 |
| ---- | ---- | ---- |
| 流程语义（P1–P33） | `rules/axioms.json` | 流程怎么算对 |
| 标识与文档结构（AX1–AX20） | `axioms-v2.md` | 编号与文档怎么算全 |
| 生命周期与语言（AX21–AX30） | 本文件 | 产物怎么算清、实现怎么算可替换 |

三层互不重叠，`summary` 关系：P 组管“对”、AX1–20 管“全”、AX21–30 管“净与可控”。
