# specs/054 — 目录四方重放网络（catalog 网络转换完备性）

- 编号：specs/054；立项日期：2026-11-19；状态：approved（用户 2026-11-19 当轮批准全部路线）
- 承办：主会话（ADR-0034 主代理单干）
- 上位框架：specs/053 §9（公理 A4–A6、定理 T5–T8、收缩对 B3.1/B3.2）、specs/044 §1.3 B 系列、ADR-0076 三类目制、ADR-0045 双账语义

## 0. 方向声明（rules/08 §0）

用户裁定（2026-11-19 两轮指令＋"批准全部"）：把 zh SUMMARY、en SUMMARY（yuanwen/SUMMARY-en.md）、contents.html（上游目录钉存）、mu-lu-s.md 四方工件做成**转换完备网络**——

1. **变动跟随**：上游 contents.html 变动后，衍生文件按固定次序机械跟随（人工裁定点仅 ADD/REMOVE/RENAME/alias 四类事件）。
2. **逆向装配**：必须能从账＋规则＋残差池**逆向装配回 contents.html，与钉存快照 sha256 全等**（装配用于验证，oracle 只读不覆写）。
3. 转换完备性以固定门禁与固定目录存储的映射/残差账证明（specs/053 收缩对框架的目录域推广）。

**非目标**：不重抓上游（只用既有钉存快照，礼貌抓取另轮）；不改 `en/` 冻结件与 `yuanwen/`（I2/I3 管辖）；不做正文域 B3（specs/053 已立项，本 spec 只做目录域）；不实现 detect_updates/compare_versions（specs/001 T020-25 另线）；不改 mu-lu-s.md 的编辑内容本体（归类语义仍是人工裁定，本 spec 只外置其账）。

**验收判据**（可判定，见 §6；全部满足即验收）。

## 1. 试金石实证基线（2026-11-19，凭证 script/tmp/archive-q/probe1/2/3.py）

两时点钉存快照（`en/_catalog/20261027T171130Z-contents.html`、`en/_catalog/20261114T231750Z-contents.html`）分解实证：

| 层 | 实测 |
| ---- | ---- |
| L1 冻结模板 | 头 143 行＋尾 77 行＋中间骨架内容跨时点**逐字节恒等**（新独有 0＝旧独有 0） |
| L2 正典行 | 1872 行与账 1:1（集合差双 0）；规则渲染闭合 **1710/1872＝91.3%**；残差 162＝闭合标签缺失＋内联 `<em>` 题名 |
| L3 别名行 | 653 行（556 slug 键，97 双别名），形态规则 100% 可判定；标签文本账外 |
| L4 簇与序 | 母行 188（仅 33 可由题名推导）；ul 开 369／闭 343（差 26＝letter 大列表收口）；页序≠账序≠题名排序→账缺 doc_order |

实体编码策略实测闭合：HTML4 命名实体优先（é→`&eacute;`）＋无名码点十进制兜底（ū→`&#363;`），纯函数。

## 2. 工件与账设计（单一事实源落位）

| 账 | 路径 | 内容 | 写者 |
| ---- | ---- | ---- | ---- |
| 目录机器账（升级） | `baseline/catalog.json` | 现有 `items[]`（slug/title/authors/alias_of/level）新增三族：`doc_order`（页序位）、`alias_rows[]`（slug/label/level/doc_order）、`cluster_mothers[]`（label/level/doc_order） | `tools/fetch_catalog.py`（`--offline` 从钉存快照重建） |
| 页面模板账 | `baseline/catalog-skeleton.json` | 头模板＋尾模板＋letter 节标行文本（26 键）＋固定说明行（按锚点） | `tools/rebuild_catalog.py --build`（从最新钉存快照抽取） |
| 行级噪声池 | `baseline/catalog-residual.json` | 每条＝{slug, kind, detail}，准入谓词限定 kind ∈ {`no-close-li`（闭合标签缺失）, `inline-markup`（题名内联 `<em>` 等）}；正文文字层禁入（A5 准入谓词） | 同上，生成后冻结 |
| mu-lu 归类账 | `baseline/mulu-map.json` | slug→{section, order, line_text} 全目录行覆盖 | `tools/check_catalog_network.py --build-mulu`（从 mu-lu-s.md 抽取） |

结构标记行（`<ul>` 开闭、`</ul></li>` 收口、空行）**不入账**——由簇结构规则确定性生成（已实测配对规律）；规则无法覆盖的个别例外才入残差池。

## 3. 工具与 CLI 契约（详见 contracts/cli.md）

1. `tools/parser.py`：`_CatalogHTMLParser` 升级——解析别名行族、母行族与页序，输出字段不变名不改（只增）；消费方 `summary_sync.py`/`fetch_catalog.py` 兼容（只增字段，schema 向后兼容）。
2. `tools/rebuild_catalog.py`：目录域装配器。`--build` 从钉存快照生成模板账＋噪声池（冻结）；默认（重放）模式＝账⊕规则⊕池→逐字节装配 contents.html，`--check` 与指定钉存快照 sha256 对比，全等退出 0。装配件**只用于验证输出 sha，禁止写回** `en/_catalog/`（oracle 只读）。
3. `tools/check_catalog_network.py`：四向重放门。G1 装配等值门（rebuild_catalog --check 对最新快照＋旧快照）；G2 en-SUMMARY 重放门（`gen_en_summary.py --check`）；G3 mu-lu 重放门（mulu-map ⊕ SUMMARY → mu-lu-s.md 字节全等）；G4 目录↔SUMMARY 对账（`summary_sync.py report` mapped 全覆盖）。`--gate` 入 `check_all.py`。

## 4. 门禁登记（rules/05 判定权表）

新增 gate key：`catalog_net`（判官只读；只增不改既有 16 项）；`gen_en_summary --check` 并入 G2 不单独立 key。门禁登记行同步 `rules/05-ci-and-tools.md` 门禁清单。

## 5. 理论落位

- **变动跟随**＝公理 A4（装配确定性，网络无隐藏状态）＋T6（四类漂移覆盖完备）＋**残差正交引理**（本 spec 实测：池按 slug 键控且只含标签/形态信息，内容变动不改 slug→池命中关系不变→重放机械跟随；ADD/REMOVE/RENAME 为仅有人工裁定点）。
- **逆向装配**＝B3 目录域实例：B3.2 装配全等（sha256 对比钉存快照）、B3.1 往返不动点（装配件重解析≡账）；收缩对定位沿 053 §9.5（lens PutGet/GetPut，Foster–Greenwald–Moore–Pierce–Schmitt TOPLAS 2007）。
- **T7 量化**：规则闭合率＝装配证据力。账升级（序/别名/母行三族）优先于建池——池只收真噪声（实测 162 行级，占正典行 8.7%；账升级后池约 2–3%）。

## 6. 验收判据（全部满足）

- **A1 账升级**：`--offline` 重建后 catalog.json 三族字段与钉存快照逐位一致（doc_order 与快照词条序恒等；alias_rows＝653 行全解析；cluster_mothers＝188 母行全解析）。
- **A2 装配全等**：rebuild_catalog --check 对最新钉存快照（20261114T231750Z）sha256 全等。
- **A3 跨时点装配**：对旧快照（20261027T171130Z）以同时点账装配亦 sha256 全等（账由同一 `--offline` 从该快照重建）——变动跟随的实证闭环（账差＝上游变动，装配件各自与其快照全等）。
- **A4 池纪律**：残差池 ≤200 条且逐条过准入谓词；池冻结（建池后只读，改动须登记）。
- **A5 门禁**：check_all 含 `catalog_net` 后 17 项全绿；单测 `tools/tests` 全绿。
- **A6 mu-lu 账**：mulu-map.json 覆盖 mu-lu-s.md 全部目录行，重放字节全等；G3 绿。
- **A7 凭证**：装配 sha 对比记录入 `results/`；execution-log 留干执行记录。

## 7. 卡钉基准与作废条件（ADR-0039）

**卡钉**：`en/_catalog/20261114T231750Z-contents.html` 与 `20261027T171130Z-contents.html` 的 sha256（开工时登记入 results/pins.json；本工程不改快照）。**作废条件**：①池 >200 条或出现准入谓词外残差类（文字层差异）→ 停线归因登记（四元组）再议；②上游改版（模板指纹漂移、L1 层不再跨时点恒等）→ 本 spec 账升级部分重验；③快照集变更（新 fetch_catalog 落盘）→ A2/A3 换钉重跑，不影响已验收结论。

## 8. 标准筛查结论（rules/08 §13，ADR-0042）

命中已登记域：ISO/IEC/IEEE 29148:2018（FR 七特性自检，本 spec §0/§6 按其组织）；GB/T 26162-2021（账目分类/元数据关联，ADR-0076 已映射 baseline 落位）；ISO 15489-1（记录四特性，账冻结与只追加语义）。理论对照沿 053 §9.5 已登记三锚点（lens laws／Darcs patch inverse／translation validation），无新增外部标准需研读；筛查结论＝无未登记适用域。
