# 064 组 A 执行证据（2026-11-27）

- 组：**a**（准入；T168／T169／T130）
- start tag：`batch/064-a-start` → `6b01e803e`（已推送）
- end tag：待打（T130 已完成，G0 条件满足；本文件提交后打 `batch/064-a-end`）
- 门禁：`python tools/check_all.py` **22/22 全绿**（2026-11-27，组 A 改动后）
- 口径：本文件只登记组 A 的实际执行与验证；不改写任务定义，不替代 `tasks.md` 的勾选与用户签字

## 1 T168 治理旧口径

**状态：完成**（2026-11-27；三处旧口径已消除）

| 文件 | 改前 | 改后 | 验证 |
| ---- | ---- | ---- | ---- |
| `AGENTS.md` L49 | `抓取礼貌`＋`相邻请求至少间隔 5 秒` | `抓取失败显式化`＋`4xx／5xx／超时退避重试并记录最终状态，禁止静默跳过；不设最小请求间隔（ADR-0069）` | `rg "5 秒|相邻请求"` 无命中；新行含 ADR-0069 |
| `AGENTS.md` L9 | 宪法原则列表含`礼貌抓取` | 改为`抓取失败显式化`（与宪法 V 现名一致，ADR-0069） | `rg "礼貌抓取" AGENTS.md` 无命中 |
| `rules/README.md` L39 | `P1–P28 公理` | `P1–P33 公理` | `rg "P1–P28"` 无命中；`P1–P33` 唯一命中 |
| `rules/naming.json` L11 | `ISO/IEC/IEEE 12207:2017 配置标识唯一且稳定` | `ISO/IEC/IEEE 12207:2026 配置标识唯一且稳定` | `json.load` 通过；`12207:2017` 无命中 |

**旁证**：`rules/standards.json` C45 为 12207:2026，status 记“现行（2026-04；2017 版 2026-04-29 废止）”；`rules/axioms.json` 实有 P1–P33。L49 修订同时覆盖了 ADR-0069 要求的“抓取失败显式化”语义。

## 2 T169 标准证据回写

**状态：完成**（2026-11-27；`verify_standards` 4/4 PASS）

| 对象 | 改动 | 验证 |
| ---- | ---- | ---- |
| `rules/standards.json` C45 | `checked` → `2026-11-27`；12207:2026／status／source 保持 | JSON 解析通过 |
| `rules/standards.json` C50 | 29148:2018：`status` 由“待核”→“现行（2018 版；2024 复审确认；DIS 在研）”；`source` 官方页；`checked` 2026-11-27 | 同上 |
| `rules/standards.json` C51 | 26514:2022：`status` 由“待核”→“现行（2022 版）”；`source` 官方页；`checked` 2026-11-27 | 同上 |
| `rules/standards.json` C52 | 15289:2019：`status` 由“待核”→“现行（2019 版；2025 确认；2026-06-11 转 90.92 修订）”；`source` 官方页；`checked` 2026-11-27 | 同上 |
| `rules/standards.json` `not_adopted` | 新增 ISO/IEC 25010:2023 条：九特性、ICT／软件产品质量、非译文质量模型；不直接适用、不纳登，仅工具质量／类比 | 字段形状仍为 `std`／`reason` 两键 |
| `rules/10-standards-clauses.md` §10.7 | 新增“工程过程标准备注（T169 回写，2026-11-27）”：29148／15289／26514／12207／25010 版本状态与本库处置 | 3 列表格；25010 明写不直接适用、不纳登 |
| `rules/README.md` 标准表 | `standards_table.py` 重生成（60 行），C50／C51／C52 状态同步 | `standards_table.py --check` → “README 标准表与 cited 同步” |

**验证输出摘要**：
```
[充分性] PASS  [一致性] PASS  [完备性] PASS
[V5] 规则正文标准号可解析到登记册 PASS
汇总：4 项，通过 4，失败 0；采纳项 23
json ok
```

## 3 T130 ex-04 人工定性

**状态：完成**（2026-11-27 用户全部批准；T130 已勾选）。

- 证据落点：`results/e2e-habermas.md` §“T130 人工定性（2026-11-27，待用户复核签字）”
- 候选总数：**5**（hard 0／warn 5／info 0，与 `e2e-habermas-source-audit.json` 一致）
- 豁免类计数：A 1／B 2／C 1／D 1（不豁免）／E 0
- 逐条结论：真候选 **1**（`,,`，D 类，HTML L4199–4201，系排印手误）；误报 **4**；待核 **0**
- 处置：`baseline/en-errata/en-errata.md` 第十三节已登记两条——`habermas` `des Ritus”,,`（①双逗号）与 `Theory on Empitical Research`（①拼写，用户批准另立）；`en/` 零改动，中文承载待重译时落地
- 附带观察：`Empitical` 已按用户批准入表；`en_source_audit` 拼写类未检出，工具改进仅作建议
- 缺口：无（T130 已完成；用户 2026-11-27 批准记录见 `results/e2e-habermas.md`）

## 4 组界与闸门

| 项 | 结果 |
| ---- | ---- |
| `batch/064-a-start` | 已创建并推送，指向 `6b01e803e` |
| `batch/064-a-end` | 待打；A 三任务已完成，G0 条件满足，本文件提交后打 |
| G0 | **条件满足**：T168／T169／T130 全部完成；b 组可并行启动 |
| 全量门禁 | 22/22 全绿（组 A 改动后） |
| 未改动 | `en/`、`yuanwen/`、译文、`tasks/*.json` 未改；`baseline/en-errata/` 按用户批准新增第十三节 |

## 5 残留与后续

1. 打 `batch/064-a-end`；随后打 `batch/064-b-start`，B 组（T020–T024）由主代理单干（本轮未授权子代理）。
2. `,,` 与 `Empitical` 已入勘误表；中文译注在该件重译时按 ADR-0065 落地，属后续 tr 链，不在本组。
3. `en_source_audit` 的“标题末词＝段落首词”抑制与拼写类缺口仅为建议，未改工具。
4. 组 A 改动与本证据文件应同批提交；提交后核对 `git log origin/main..main` 为空。
