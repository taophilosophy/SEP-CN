# 公理登记册 v2（specs/042；机读面）

约定：**锚**＝`路径::关键词`，须在现行文本命中；**载体**前缀 `gate:`／`tool:`／`impl:`／`hook:`／`spec:`（仅规格内定义，未落地）。判面＝机检／留痕／纪律。

## 一、公理（20 条）

| 公理 | 命题（浓缩） | 判面 | 权威锚 | 机器载体 |
| --- | --- | --- | --- | --- |
| B1 | `bytes(En(e)) = Pin(e)`；`en/` 冻结，偏离唯一出口是格式补丁池 | 机检 | `.specify/memory/constitution.md::零信任`、`rules/adr/0062::绝对冻结` | `gate:divergence`、`tool:check_en_patches` |
| B2 | 译文命题唯一裁决对象是 `En`；旧译／缓存／记忆不作底稿 | 留痕 | `rules/04::重译纪律`、`.specify/memory/constitution.md::既有中文译文` | `tool:mech_audit`、`discipline:s1 回源` |
| B3 | 成品可回溯 `(pubinfo, archive_edition, sha256)` | 机检 | `rules/06::每件成品可回溯`、`rules/07::版本事实` | `gate:academic`、`tool:baseline_audit` |
| B4 | 事件只追加；撤销以 `invalidate` 追加表达，不删事件 | 机检 | `rules/09::append-only`、`.specify/memory/constitution.md::只追加` | `spec:events-log`（待建）、`gate:divergence` |
| B5 | `Done`／`Head`／`stale`／进度均为派生量，禁回写日志 | 机检 | `rules/06::单一事实源登记表`、`rules/adr/0015` | `spec:derive-only`（待建） |
| B6 | 无方向声明不入质量门 | 留痕 | `rules/08::视为尚未立项`、`rules/06::方向声明缺失` | `gate:academic(task-evidence-missing)` |
| B7 | `Done(e)` 只增不减，除 `invalidate` 显式扣除 | 机检 | **待补**（新公理，尚无正文锚） | `spec:derive-only`（待建） |
| B8 | S 全序可插；插入不改既有阶段相对序与标识 | 机检 | `rules/04::禁止跳步`（改造后承接） | `impl:task_ops(expected_prev)`（改造） |
| B9 | 任何有效 attempt 必须完成 `{R1,R2,R3}`；S 不参与 R | 机检 | `rules/04::复核独立性`、`rules/09::P7` | `hook:r-chain`（待建） |
| B10 | R3 仅用户显式指定会话执行 | 机检 | `rules/adr/0054::mandate` | `hook:r3_mandate` |
| B11 | `saturate(e) ⟺ Done(e) ⊇ S_current ∪ R`；不设布尔毕业位 | 机检 | **待补**（新公理） | `spec:derive-only`（待建） |
| B12 | 并发以 `(entry, section)` 为写单元；同单元单写者 | 机检＋纪律 | `rules/06::并发会话纪律`、`rules/adr/0034::主代理单干` | `spec:claims`（待建） |
| B13 | 返工在独立 attempt；`merge` 前不影响主干派生 | 机检 | **待补**（新公理） | `spec:branch`（待建） |
| B14 | `merge` 只追加事件，不改写主干 | 机检 | **待补**（新公理） | `spec:merge`（待建） |
| B15 | 同一写单元认领全局唯一且有租期 | 机检 | `rules/06::按批次认领互斥` | `impl:campaign(claim/release)` |
| B16 | 返工分支只含需返工条目（写时复制） | 机检 | **待补**（新公理） | `spec:branch-scope`（待建） |
| B17 | 判官只读；升门须填谓词／命中数／幂等／回退 | 机检 | `rules/05::判官只读`、`rules/08::四件套` | `gate:*` 全体 |
| B18 | 禁静默跳过与兜底降级；失配即硬失败 | 机检 | `.specify/memory/constitution.md::礼貌抓取与失败显式化` | `impl:common(write_*_verified)` |
| B19 | 先登记后使用；语义层禁机械替换 | 机检＋留痕 | `rules/03::禁止机械替换`、`rules/adr/0048` | `gate:terms`、`tool:mech_audit` |
| B20 | 结构化落盘写后读回核验 | 机检 | `rules/09::信息项五属性` | `impl:common(write_json_verified)` |

## 二、效力悬空登记（S1 缺口）

以下五条目前**只有规格锚，无规则正文锚**，按 S1 判为效力悬空。它们的落地本身需要一个新 S 环节（暂名 `S-merge`），即"新公理也必须走一次自己定义的过程"：

| 公理 | 缺口 | 补锚位置（拟定） |
| --- | --- | --- |
| B7 阶段单调 | 无 | `rules/04` 新增「事件与派生」节 |
| B11 饱和相对性 | 无 | 同上 |
| B13 分支隔离 | 无 | `rules/04` 新增「返工即分支」节 |
| B14 合并单向 | 无 | 同上 |
| B16 分支最小化 | 无 | 同上 |

## 三、目的导出（Φ1–Φ8）

| 子目标 | B 子集 | witness |
| --- | --- | --- |
| Φ1 版本钉 | B1 B3 B4 | `gate:academic`、`baseline/entries.json` |
| Φ2 保真链 | B1 B4 B17 B18 | `gate:divergence`、`gate:fidelity` |
| Φ3 结构完整 | B3 B5 B17 | `gate:summary`、`gate:images` |
| Φ4 体例合规 | B17 B19 | `gate:quotes`、`gate:mathzh` |
| Φ5 术语一致 | B5 B19 | `gate:terms` |
| Φ6 语言质量 | B6 B9 | `spec:task-style-attest` |
| Φ7 内容正确 | B2 B19 | `tool:mech_audit`、`s1/r2` 人审 |
| Φ8 流程可审计 | B4 B5 B6 B8 B9 B10 B12 B20 | `spec:events-log`、`hook:r-chain` |

## 四、新模型的自我演示

本文档自身即一次演示：`specs/042` 是一份新的三位一体（spec ＋ 公理册 ＋ 后续 plan/tasks），按 §六 的判定它携带新判据（B7／B11／B13／B14／B16 无可复用载体），故应立新 S 环节；同时这五条公理尚无正文锚，S1 缺口 5 项——**新体系的第一件事就是给自己补一个 S**。这是"饱和相对性"最直接的体现：公理体系也不能毕业。
