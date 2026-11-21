# 上游修订处置线的形式化完备性证明（issue #51 类，2026-11-21）

**性质**：续 specs/044 §2 与 specs/053 §9 记号（A 系公理、T 系定理编号顺延），不自造理论。
**对象**：目录巡检 CI 开出的上游修订 issue（#49/#51 先例）经处置线落地时，以下四问的
完备回答与保证机制——①是否触发 B1/B2/B3 转换保真流程；②已译条目是否做变动标记、
标记什么、由谁存储、谁判断；③哪个流程、谁触发；④怎么保证（无静默漏账面）。
**判据**：每个定理附构造性论证＋代码/数据可溯锚点；结论可由独立会话复算（可判定性四件套）。

## 1. 符号与域

- 词条空间 `E`（现役 1,873 件）；`en(s)`＝词条包字节（index.html 等全套文件钉）；`md_zh(s)`＝中文文档。
- 账本六件（各有唯一写入者）：
  - `L`＝baseline/entries.json（原始网页钉 `files[].sha256`、pubinfo、archinfo、转换登记 `yuanwen{md,sha256,source_sha256}`；写入者 fetch_entry/yuanwen/summary_sync）；
  - `D`＝baseline/en-errata/divergences.json（批准分歧，ADR-0045/0062）；
  - `C`＝specs/001-sep-sync-pipeline/compare/&lt;slug&gt;.json（段落级变更清单；写入者 compare.py）；
  - `T`＝tasks/&lt;letter&gt;/&lt;slug&gt;.json（任务账，append-only steps；写入者 task_ops）；
  - `J`＝journal/&lt;letter&gt;/&lt;slug&gt;.ndjson（事件日志，事实层；写入者 journal_lib，ADR-0068 三存储一视图）；
  - `M`＝baseline/mulu-map.json（mu-lu-s 归类账；重放生成 mu-lu-s.md）。
- 判据族（specs/044 §1.3）：`B0` 形式可解析、`B1` 词元等值、`B2` 结构等值、`B3.1` 往返不动点 `C(R(md))==md`、`B3.2` 装配全等 `sha(H0')==sha(H0)`；`B3 = B3.1 ∧ B3.2`。
- 账面保真谓词 `I2(s)`：`sha(md_zh(s)) == L.yuanwen.sha256(s) ∧ sha(en(s)) == L.yuanwen.source_sha256(s)`
  （check_yuanwen_fidelity 双查：md-hand-edited／source-drift）。
- 门禁面 `check_all` 17 项（--list-gates 现查）：其中 `G_div`＝原始物分歧账（divergence verify）、
  `G_fid`＝转换保真（fidelity --gate）、`G_net`＝目录四方重放（G1 装配/G2 en-SUMMARY/G3 mu-lu 重放/G4 对账）、
  `G_ledger`＝账实一致性、`G_unit`＝管线单元测试。
- 任务机挂载函数 `mount: step → 判据集`（task_ops advance 硬挂，ADR-0052/0040/0043/0054）：
  `mount(s0)={en_integrity, en_source_audit}`、`mount(s24)={check_terms, check_pairs, check_style}`、
  `mount(s25)={check_math, check_style}`、`mount(s3)=mount(r3)={check_academic, check_math_strict}`。
- 处置流程算子（issue #51 实测序列，ADR-0050/0051/0068 收编后）：
  - `u1` 检测（catalog-drift CI：detect_updates＋catalog_drift，只读）；
  - `u2` 比较（compare.py：抓最新快照，与钉字节比较 → 写 `C`）；
  - `u3` 钉前移（fetch_entry.py：`en(s)` 替换为新上游字节，`L` upsert，`J` 落 `lock` 事件）；
  - `u4` 镜像重转（yuanwen.py：`md_zh` 镜像重生成，`L.yuanwen` 重写）；
  - `u5` 建账（task_ops：done 件 `reopen --clear`／在途件 `reopen --upstream-sync`／无账件 `create --from C` → `clear`；写 `T`、`J`）；
  - `u6` 全量重译＋校次（draft → … → done，本线实例停于 s0）；
  - `u7` 门禁收敛（check_all 17 项 ＋ push 触发 CI）。

## 2. 引用公理（不新立）

A2（账写确定性：写后读回自校验）、A3（原始网页钉 sha256 永不改写，前移须随新上游快照归档）、
A4（装配确定性：R 纯函数）、A5（池冻结与准入；specs/053 §9.2）、单向波纹（specs/054 §3：
巡检 CI 只读只报告，落地由本地会话承担）、append-only（T steps 与 J 事件不删除）。

## 3. 定理 T9（B 系列触发判定）——回答问题①

**断言**：(a) `U = u1..u7` 各步的硬挂判据集与 `{B0, B1, B2, B3.1, B3.2}` 交集为空；
(b) `u3–u4` 的产物变换使词条落入 B0–B3.2 全量机检的定义域（覆盖保持）；
(c) 变动显形由三道独立面承载，其并集对"重转不一致"类漂移封闭。

**证明**：
(a) 代码级事实：task_ops.py 无 B0/B3/reassemble 引用（grep 核验，2026-11-21）；挂载集即 §1 mount 表，
    五判据均不在其并集中。任务层对 EN 侧保真的唯一硬性前置是 s0 的 en_integrity（包完整性）与
    en_source_audit（源审计，ADR-0052），它们约束"源可信"而非"转换保真"。∎
(b) `G_fid` 的遍历域＝`dom(L.yuanwen)`（entries.json 全件登记）；`u3` 保持 slug 在域内（upsert）、
    `u4` 重写登记，故 `s ∈ dom(G_fid)` 恒成立——处置不产生机检盲区。B3.1/B3.2 同理：每日三次
    en-roundtrip 巡检（reassemble --all／page_assemble --all）遍历全库，无白名单剔除。∎
(c) 显形面分解（roundtrip_drift.py:120 现查）：
    `changed = div_failures ∨ i2_failed ∨ newly_failing ∨ newly_passing ∨ added ∨ removed ∨ page_*`。
    - 面 1（en 钉账）：`u3` 后 `sha(en) == L.files[].sha256` 构成性成立（同一次写入）；
      若 en 变而账未动 → `G_div` 红（verify 三账核验）。
    - 面 2（I2 账面双查）：en 换而未重转 → `source-drift` 红；md 手改 → `md-hand-edited` 红；
      即"钉前移与重转不配对"必显形于 `G_fid`，且该项直接进 `changed`（i2_failed 项）。
    - 面 3（B3.1/B3.2 差集）：md 或重放结果的成败集合相对基线变化 → newly_failing/newly_passing/
      added/removed/page_* 显形。
    **边界（如实登记，T8 同构）**：词条本为 B3.1 已知残差且重转后失败模式不变时，面 3 不显形——
    此时该词条的转换质量证据由 B3.1 逐条求值本身承载（每轮全量重算、非缓存），残差处置归
    specs/053 W7–W12 四出口管辖；不构成"漏账"，因为该情形下无未记账变动（重转已入 `L`、`J`）。∎

**回答**：作为任务挂载判据——不触发；作为全量机检定义域——重转后必然覆盖，其中 B3.1
承载转换器对该词条"不丢文本"的主证据（specs/053 §7：B3.2 sha 全等不构成"最初无损"的
独立证据——池即答案，oracle 不可写；两层互证互不冒充）。

## 4. 定理 T10（变动标记完备性）——回答问题②

**断言**：处置过程中每类变动均有唯一存储账与判官，且"变动而未记账"落在某门禁红灯面内
（无静默漏账）。逐类构造（存储 S：变动 → 账；判官 V：账 → 退出码）：

| 变动类 | 变动了何者 | 存储账 S | 判官 V（红灯条件） |
| ---- | ---- | ---- | ---- |
| EN 源字节 | `en(s)` 套件 → 新上游字节 | `L.files[].sha256`（前移）＋ specs/001 results/upstream-snapshots 归档（A3）＋ `J` lock 事件 | `G_div`：sha ≠ 钉而未登记 → 红 |
| 批准分歧 | 勘误/搬运事实 | `D` | `G_div`：已登记而三账不符 → 红 |
| 变更清单 | 节级/段级 diff＋行号映射 | `C` | 非门禁（审读辅助，ADR-0050 降级；消费由任务证据约定承载） |
| 镜像产物 | `md_zh` 镜像重生成 | `L.yuanwen{md,sha256,source_sha256}` | `G_fid`：sha ≠ 登记 → 红 |
| 任务状态 | create/reopen/clear/advance | `T`（append-only steps）＋ `J`（pass/rework/lock 事件，双写） | `G_ledger`＋单测（journal 双写一致性钉死） |
| 中文正文 | 置空仅留 H1 → 全量重译 | zh md 本体 | clear 前置 gate（基线哈希复算）；`G_ledger` 账实一致 |
| 版次/作者/题名 | pubinfo、archinfo、title | `L`（upsert） | `G_net` G4 对账＋check_summary 标题锚 |
| 目录归类 | mu-lu-s 行 | `M`（抽账收编） | `G_net` G3 逐行重放全等（手改文件＝改弱势方，实证红灯先例） |
| 进度读数 | 在途/骨架计数 | PROGRESS.md（journal 派生） | 派生量可再生，`G_unit` 覆盖读面函数 |

**证明**：表中每行"红灯条件"列即构造性论证——删除 S 中任一账本（或跳过写入）后，该行 V 的
输入失配，门禁退出码非 0，check_all 收敛失败、push 被自身纪律拦截（提交即推前跑门禁）。
互异性由层位划分保证（原始字节/登记/事件/派生四层各有专属账，T6 同构）。∎

**回答**：会标记。标记不是给 zh md 加注记，而是**账本体系的写入**：变动何者→入哪本账→
哪个判官核验，上表即完备映射；"已译条目"被标记的最小事实集＝{`L` 钉与转换登记、
`J` lock/pass/rework 事件、`T` steps 历史、`C` 变更清单}，PROGRESS 读数是派生视图（ADR-0068：
日志为事实、状态为视图）。

## 5. 定理 T11（检测完备性与漏报面）——回答问题③前半

**断言**：上游修订事件的机器检测面由四路组成，任一路独立即可发现 #51 类事件；漏报边界
如实列出并有人工兜底。

| 检测路 | 触发者 | 覆盖 | 边界（漏报面） |
| ---- | ---- | ---- | ---- |
| catalog-drift CI（cron 每日三次） | 机器 | 目录级（fetch_catalog diff）＋ new.html NEW/REVISED ＋ archinfo 版次 | 上游改而未标注、窗口外（>3 月）修订、undated 项被剔 |
| compare.py 字节比较 | 人工（会话） | 正文逐字节，钉级准确 | 需人启动（消费 issue 或 drift_scan 清单） |
| drift_scan 全量回源 | 人工（季度/战役开工前） | 1,873 件 live 对钉，全量 | 并发豁免令一次性，需再批（specs/001 Assumptions） |
| en-roundtrip CI 差集 | 机器 | 相对基线变动 | 见 T9(c) 边界（残差件失败模式不变时不显形） |

**证明**：#51 实例即第 1 路捕获（run 44833333086 → issue → 会话处置）。四路检测者互不依赖
（cron／人工／人工／cron），第 1 路的"只读＋必开 issue"保证事件进入人工视野（单向波纹：
CI 不落地，落地必经会话）。∎

## 6. 定理 T12（流程保证）——回答问题③后半

**断言**：处置正确性由四层机制保证，任一层失守均被后层拦截：

1. **前置校验层**：状态机禁跳步（ORDER 唯一直接前驱，specs/040 F-01/F-02）、r3 须
   `--mandate`（ADR-0054，缺失即拒）、clear 须基线哈希复算、`blocked` 冻结一切转移。
2. **机检门禁层**：check_all 17 项（T10 的 V 全集）＋定点 `check_academic --strict`；
   每项有唯一硬拦点（pipeline.json criteria_owner，check_stages S2 验证）。
3. **CI 终审层**：push 触发 checks 矩阵重跑全部门禁；巡检类 CI 只读不落地（单向波纹），
   报告与事实分离。
4. **审计层**：append-only（`T` steps、`J` 事件、`D` 登记、upstream-snapshots 归档）——
   事后任一步可复核"何者、何时、何凭"；事件 schema 不变量（lock：同一 attempt 内
   sha256 变更须开新 attempt）由 schema 与单测承载。

**证明**：层 1 是过程拦截（advance 即校验）；层 2 是结果拦截（任何账实失配退出码非 0）；
层 3 在不同机器不同时点复算层 2（translation validation 家法：验证每次运行而非翻译器整体）；
层 4 使层 1–3 的历史不可篡改。四层依赖关系为串联，无单点。∎

## 7. 可判定性四件套（结论＋证据＋复算）

- **结论**：四问答案及依据为 T9–T12；处置机制对 #51 类事件类级完备（同族未来修订走同一
  流程，无流程外旁路——create 拒非 retranslate（test_create_rejects_update）、巡检只读、
  落地唯一入口）。
- **证据**（本会话实测，可复算）：
  - 检测：run 44833333086 → issue #51（新格式正文）；
  - 处置：C 两份（compare/modality-varieties.json 7 节 8 处／type-theory.json 1 节）、
    钉前移 557ef0da／f289038b（entries.json + upstream-snapshots）、重转登记重写、
    T/J 建账（state=cleared→s0 pass，version_pin 双钉）；
  - 门禁：check_all 17 项全绿（三轮）；CI run 44846073201/44846067302 均 success。
- **改判表**：无（本轮无判据改判）。
- **证明期发现与处置**（形式化的直接收益）：journal lock 事件在 schema 中已定义
  （"源钉变更"，不变量"同一 attempt 内 sha256 变更须开新 attempt"）但 fetch_entry 钉前移
  未落事件——T10 表第 1 行的 `J` 列原为缺口。处置＝补实现（upsert_baseline 尾部
  `_journal_lock`，sha 相同幂等不落）＋单测 2 项（tools/tests/test_fetch_entry.py，
  6/6 绿）。该缺口不影响 `G_div`/`G_fid` 红灯面（登记账已双查），仅审计事件流不全；
  补齐后 T10 第 1 行三账（L/snapshots/J）齐备。
