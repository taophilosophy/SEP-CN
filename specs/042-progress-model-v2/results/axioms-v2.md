# 公理登记册（specs/042 v3；机读面，C 系列 29 条）

约定：**锚**＝`路径::关键词`，须在现行文本命中；**载体**前缀 `gate:`／`tool:`／`impl:`／`hook:`／`spec:`（规格内定义，未落地）。判面＝机检／留痕／纪律。

## 一、公理（29 条，七组）

| 公理 | 命题（浓缩） | 判面 | 权威锚 | 机器载体 |
| --- | --- | --- | --- | --- |
| C1 | P1 完成即锁 `Pin(e)`；锁后不得改 `en/` 字节 | 机检 | `rules/adr/0062::绝对冻结` | `gate:divergence` |
| C2 | 译文命题唯一裁决对象是 `En`；旧译／缓存／记忆不作底稿 | 留痕 | `rules/04::重译纪律` | `tool:mech_audit` |
| C3 | `yuanwen` 只许格式层偏离，`substantive` 禁入 markdown | 机检 | **待补** | `spec:md-freeze`（待建） |
| C4 | 成品可回溯 `(pubinfo, archive_edition, sha256)` | 机检 | `rules/07::版本事实` | `gate:academic`、`tool:baseline_audit` |
| C5 | 事件只追加；撤销以 `invalidate` 追加 | 机检 | `rules/09::append-only` | `spec:events-log`（待建） |
| C6 | `Done`／`Head`／`stale`／进度比为派生量，禁回写 | 机检 | `rules/06::单一事实源登记表` | `spec:derive-only`（待建） |
| C7 | 三段全序固定（提取／翻译／审校），不得跳段换序；增段须改 ADR | 机检 | **待补** | `spec:stages.json`（待建） |
| C8 | 段内任意相邻节点之间可插；插入不改既有节点相对序与标识 | 机检 | **待补**（v3 修正） | `impl:task_ops(可插序)`（待建） |
| C9 | 节点类型（pipe／stage／review／format）唯一决定判据来源与降级策略，不决定能否插入 | 机检 | **待补**（v3 新增） | `spec:stages.json`（待建） |
| C10 | `{R1,R2,R3}` 为必选最小集，可增不可减、不可跳过 | 机检 | `rules/04::复核独立性` | `hook:r-chain`（待建） |
| C11 | `Seg(n+1)` 的输入必须等于 `Seg(n)` 的出口产物 | 机检 | **待补**（v3 新增） | `spec:segment-contract`（待建） |
| C12 | 每段以格式闭合节点 `F_i` 收口；格式问题不得跨段 | 机检 | **待补**（v3 新增） | `spec:format-close`（待建） |
| C13 | `Done(e)` 只增不减，除 `invalidate` 扣除 | 机检 | **待补** | `spec:derive-only`（待建） |
| C14 | `saturate(e) ⟺ Done(e) ⊇ 全部段的全部节点`；不设毕业位 | 机检 | **待补** | `spec:derive-only`（待建） |
| C15 | Seg1 之后的一切环节输入必须是 P1 锁定的同一 sha | 机检 | **待补** | `spec:pin-gate`（待建） |
| C16 | `yuanwen = convert(en ⊕ patches)` 可确定性重算 | 机检 | `rules/adr/0063::I2` | `gate:fidelity` |
| C17 | 正向验转换等值，反向验渲染结构同构 | 机检 | `rules/adr/0063::I2`、**待补**（反向） | `gate:fidelity`、`spec:render-check`（待建） |
| C18 | 差异必属 `format_only` 或 `substantive`；无法归类从宽判 3.2 | 机检 | **待补** | `spec:diff-binary`（待建） |
| C19 | 格式修正只以虚拟补丁表达，物理文件均不改 | 机检 | `rules/adr/0062::补丁池` | `tool:en_patch_lib`、`gate:check_en_patches` |
| C20 | 实质修正只入勘误表与中文译注 | 机检 | `rules/adr/0062::文字层`、`rules/adr/0065` | `gate:check_pairs(errata)` |
| C21 | 并发以 `(entry, section)` 为写单元；同单元单写者 | 机检＋纪律 | `rules/06::并发会话纪律` | `spec:claims`（待建） |
| C22 | 返工在独立 attempt；merge 前不影响主干派生 | 机检 | **待补** | `spec:branch`（待建） |
| C23 | merge 只追加事件，不改写主干 | 机检 | **待补** | `spec:merge`（待建） |
| C24 | 同一写单元认领全局唯一且有租期 | 机检 | `rules/06::按批次认领互斥` | `impl:campaign(claim)` |
| C25 | 返工分支只含需返工条目（写时复制） | 机检 | **待补** | `spec:branch-scope`（待建） |
| C26 | 判官只读；升门须填谓词／命中数／幂等／回退 | 机检 | `rules/05::判官只读`、`rules/08::四件套` | `gate:*` 全体 |
| C27 | 禁静默跳过与兜底降级；失配即硬失败 | 机检 | `.specify/memory/constitution.md::失败显式化` | `impl:common(write_*_verified)` |
| C28 | 先登记后使用＋禁机械替换 | 机检＋留痕 | `rules/03::禁止机械替换` | `gate:terms`、`tool:mech_audit` |
| C29 | 结构化落盘写后读回核验 | 机检 | `rules/09::信息项五属性` | `impl:common(write_json_verified)` |

## 二、效力悬空登记（S1 缺口，14 条）

以下仅规格锚、无规则正文锚。v3 的缺口比 v2 增加，因为新增了 C8／C9／C11／C12 四条结构公理：

| 公理 | 缺锚 | 拟补位置 |
| --- | --- | --- |
| C3 | markdown 冻结 | `rules/04` 新增「Seg1 提取」节 |
| C7 | 三段固定 | `rules/04` 新增「三段与节点」节 |
| C8 | 节点任意可插 | 同上 |
| C9 | 类型定判据 | 同上 |
| C11 | 段间契约 | 同上 |
| C12 | 格式段内闭合 | 同上 |
| C13 | 阶段单调 | `rules/04` 新增「事件与派生」节 |
| C14 | 饱和相对性 | 同上 |
| C15 | 单钉输入 | 同上 |
| C17（反向） | 渲染反校 | `rules/04` 新增「P3 反校」节 |
| C18 | 差异二分 | 同上 |
| C22 | 分支隔离 | `rules/04` 新增「返工即分支」节 |
| C23 | 合并单向 | 同上 |
| C25 | 分支最小化 | 同上 |

## 三、目的导出（Φ1–Φ8）

| 子目标 | C 子集 | witness |
| --- | --- | --- |
| Φ1 版本钉 | C1 C4 C15 | `gate:academic`、`baseline/entries.json` |
| Φ2 保真链 | C1 C16 C17 C19 C26 C27 | `gate:fidelity`、`gate:check_en_patches` |
| Φ3 结构完整 | C4 C6 C11 C12 C26 | `gate:summary`、`gate:images` |
| Φ4 体例合规 | C12 C26 C28 | `gate:quotes`、`gate:mathzh` |
| Φ5 术语一致 | C6 C28 | `gate:terms` |
| Φ6 语言质量 | C9 C10 | `spec:task-style-attest` |
| Φ7 内容正确 | C2 C20 C28 | `tool:mech_audit`、`s1/r2` 人审 |
| Φ8 流程可审计 | C5 C6 C7 C8 C9 C13 C21 C24 C28 | `spec:events-log`、`hook:r-chain` |

## 四、v3 对 v2 缺陷的登记

v2 的 C7 把"可插性"绑在"阶段类型"上，导致"插入发生在 Seg1"无法表达。v3 的 C8／C9 是对该缺陷的直接修正：

* 缺陷形态：类型即权限（pipe → 不可插）。
* 后果：1 段（全 pipe）成为不可扩展区，而它恰恰是最需要新增校验的地方（实体、表格、图注）。
* 修正：可插性上移到"段内位置"这一结构属性；类型只保留"判据来源"与"降级策略"两职。
* 可判据：T8「可插完备」——任意相邻节点对存在合法插入位，且插入后段间契约不变。

这条登记本身是规则体系的一次返工，按 rules/08 §12 应记成因：**R1 验收维度缺口**（v2 只验"是否有类型"，未验"任意段能否插入"）。
