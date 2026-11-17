# 公理登记册（specs/042 v2；机读面，C 系列）

约定：**锚**＝`路径::关键词`，须在现行文本命中；**载体**前缀 `gate:`／`tool:`／`impl:`／`hook:`／`spec:`（规格内定义，未落地）。判面＝机检／留痕／纪律。

## 一、公理（26 条）

| 公理 | 命题（浓缩） | 判面 | 权威锚 | 机器载体 |
| --- | --- | --- | --- | --- |
| C1 | P1 完成即锁 `Pin(e)`；锁后不得改 `en/` 字节 | 机检 | `rules/adr/0062::绝对冻结`、`specs/041::A1` | `gate:divergence` |
| C2 | 译文命题唯一裁决对象是 `En`；旧译／缓存／记忆不作底稿 | 留痕 | `rules/04::重译纪律` | `tool:mech_audit`、`s1 回源` |
| C3 | `yuanwen` 只许格式层偏离，`substantive` 禁入 markdown | 机检 | **待补**（新公理） | `spec:md-freeze`（待建） |
| C4 | 成品可回溯 `(pubinfo, archive_edition, sha256)` | 机检 | `rules/07::版本事实`、`rules/06::每件成品可回溯` | `gate:academic`、`tool:baseline_audit` |
| C5 | 事件只追加；撤销以 `invalidate` 追加 | 机检 | `rules/09::append-only` | `spec:events-log`（待建） |
| C6 | `Done`／`Head`／`stale`／进度比为派生量，禁回写 | 机检 | `rules/06::单一事实源登记表` | `spec:derive-only`（待建） |
| C7 | 阶段分 P／S／R 三类；P、R 顺序不可变，S 可插 | 机检 | **待补**（新公理，用户六阶段划分） | `spec:stages.json`（待建） |
| C8 | S 在可插域内全序；插入不改既有 S 的相对序与标识 | 机检 | `rules/04::禁止跳步`（改造承接） | `impl:task_ops(expected_prev)`（改造） |
| C9 | 任何有效 attempt 必含 `{R1,R2,R3}`；P、S 不影响 R | 机检 | `rules/04::复核独立性`、`rules/09::P7` | `hook:r-chain`（待建） |
| C10 | `Done(e)` 只增不减，除 `invalidate` 扣除 | 机检 | **待补**（新公理） | `spec:derive-only`（待建） |
| C11 | `saturate(e) ⟺ Done(e) ⊇ P ∪ S_current ∪ R`；不设毕业位 | 机检 | **待补**（新公理） | `spec:derive-only`（待建） |
| C12 | P2–R 的全部输入必须是 P1 锁定的同一 sha | 机检 | **待补**（新公理） | `spec:pin-gate`（待建） |
| C13 | `yuanwen = convert(en ⊕ patches)` 可确定性重算 | 机检 | `rules/adr/0063::I2` | `gate:fidelity` |
| C14 | 正向验转换等值，反向验渲染结构同构；两者皆过方为保真 | 机检 | `rules/adr/0063::I2`、**待补**（反向） | `gate:fidelity`、`spec:render-check`（待建） |
| C15 | `en` 与 `yuanwen` 的差异必属 `format_only` 或 `substantive`；无法归类从宽判 3.2 | 机检 | **待补**（新公理） | `spec:diff-binary`（待建） |
| C16 | 格式修正只以虚拟补丁表达，物理文件均不改 | 机检 | `rules/adr/0062::补丁池` | `tool:en_patch_lib`、`gate:check_en_patches` |
| C17 | 实质修正只入勘误表与中文译注，不写入 markdown | 机检 | `rules/adr/0062::文字层`、`rules/adr/0065::译者注释` | `gate:check_pairs(errata)` |
| C18 | 并发以 `(entry, section)` 为写单元；同单元单写者 | 机检＋纪律 | `rules/06::并发会话纪律`、`rules/adr/0034` | `spec:claims`（待建） |
| C19 | 返工在独立 attempt；merge 前不影响主干派生 | 机检 | **待补**（新公理） | `spec:branch`（待建） |
| C20 | merge 只追加事件，不改写主干 | 机检 | **待补**（新公理） | `spec:merge`（待建） |
| C21 | 同一写单元认领全局唯一且有租期 | 机检 | `rules/06::按批次认领互斥` | `impl:campaign(claim/release)` |
| C22 | 返工分支只含需返工条目（写时复制） | 机检 | **待补**（新公理） | `spec:branch-scope`（待建） |
| C23 | 判官只读；升门须填谓词／命中数／幂等／回退 | 机检 | `rules/05::判官只读`、`rules/08::四件套` | `gate:*` 全体 |
| C24 | 禁静默跳过与兜底降级；失配即硬失败 | 机检 | `.specify/memory/constitution.md::失败显式化` | `impl:common(write_*_verified)` |
| C25 | 先登记后使用；语义层禁机械替换 | 机检＋留痕 | `rules/03::禁止机械替换`、`rules/adr/0048` | `gate:terms`、`tool:mech_audit` |
| C26 | 结构化落盘写后读回核验 | 机检 | `rules/09::信息项五属性` | `impl:common(write_json_verified)` |

## 二、效力悬空登记（S1 缺口）

以下 **11 条**只有规格锚、无规则正文锚，按 S1 判为效力悬空。它们的落地需要一个新 S（暂名 `S-merge`）——新体系的第一件事是给自己补一个工位：

| 公理 | 缺锚 | 拟补位置 |
| --- | --- | --- |
| C3 | markdown 冻结 | `rules/04` 新增「P2 转换」节 |
| C7 | 三类阶段 | `rules/04` 新增「P／S／R 三类」节 |
| C10 | 阶段单调 | 同上 |
| C11 | 饱和相对性 | 同上 |
| C12 | 单钉输入 | 同上 |
| C14（反向） | 渲染反校 | `rules/04` 新增「P3 反校」节 |
| C15 | 差异二分 | 同上 |
| C19 | 分支隔离 | `rules/04` 新增「返工即分支」节 |
| C20 | 合并单向 | 同上 |
| C22 | 分支最小化 | 同上 |
| C3 的 `spec:md-freeze` | 载体未建 | `tools/check_md_freeze.py`（待立卡） |

## 三、目的导出（Φ1–Φ8）

| 子目标 | C 子集 | witness |
| --- | --- | --- |
| Φ1 版本钉 | C1 C4 C12 | `gate:academic`、`baseline/entries.json` |
| Φ2 保真链 | C1 C13 C14 C16 C23 C24 | `gate:fidelity`、`gate:check_en_patches` |
| Φ3 结构完整 | C4 C6 C23 | `gate:summary`、`gate:images` |
| Φ4 体例合规 | C23 C25 | `gate:quotes`、`gate:mathzh` |
| Φ5 术语一致 | C6 C25 | `gate:terms` |
| Φ6 语言质量 | C7 C9 | `spec:task-style-attest` |
| Φ7 内容正确 | C2 C17 C25 | `tool:mech_audit`、`s1/r2` 人审 |
| Φ8 流程可审计 | C5 C6 C9 C10 C18 C21 C26 | `spec:events-log`、`hook:r-chain` |

## 四、二分完备性的自检要求

C15 的判据若只靠人眼，等于没有判据。实施时须满足三条：

1. `norm` 唯一实现（放 `en_patch_lib`），P3 与补丁池共用，禁第二套。
2. 白名单（中文全半角、数学定界符、实体、代码块）显式登记；白名单缺项即判 3.2，判据为"未覆盖即从严"。
3. S9 审计：每批抽 ≥30 条差异，人工复核归类正确率；低于 100% 即回炉标定 `norm`，不放宽判据换取全绿。
