# 登记册共享解析/折叠库（specs/033）

**版本** v1.0 ｜ **状态** 已落地 ｜ **日期** 2026-11-15 ｜ **权威** 2026-11-15 用户裁定（统一工具不统一文件）｜ **工具** `tools/register_lib.py`（新）与七个消费工具

## 1. 目的

两登记册（`shu-yu-biao.md` 术语、`ren-ming-biao.md` 人名）的解析与键折叠在工具层重复实现：`norm_key`/`fold` 有 6 处实现、3 种语义口径，已两次发案静默漂移——cnki_query docstring 声称「与 check_terms 同规」实缺引号折叠；更早三处不同步致凭证文件名损坏＋42 行伪未查证（specs/008，项目记忆在案）。同一规范化函数多副本违反 specs/008 既有裁定（「凡多模块实现同一规范化函数必须抽单一模块共用」）。

本规格把解析/折叠/分节原语抽成单一叶子模块 `tools/register_lib.py`，各工具改为引用，消灭副本。**只收敛实现，不改任何语义**。

**非目标**：

* 不合并两登记册文件（2026-11-15 用户咨询裁定保留分立，ADR-0012 拆分维持）；
* 不改任何折叠口径的语义（三口径各自原样收敛为唯一实现）；
* 不动 `check_terms` 告警/硬错误口径（specs/002/031 权属不变）；
* 不动 `registry_azsort` 写回纪律与守恒门，登记册排序结果逐字节不变；
* 不迁移 `script/` 战役一次性脚本（历史存档，冻结）；
* 不改任何登记册数据行。

## 2. 口径事实（收敛前盘点，2026-11-15）

| 口径 | 现存实现 | 语义 | 用途 |
| ---- | ---- | ---- | ---- |
| A 引号折叠键 | `check_terms.norm_key` | ʾʿ’‘ʼ′\`→'＋剥 \*＋NFD 去组合符＋空白归一＋casefold | 登记册↔正文一致性比对（同形异符归一） |
| B 基础折叠键 | `term_flow.key_of`/`norm_key`（后者已委托 cnki_query）、`term_harvest.norm_key`、`cnki_query.norm_key`、`term_coverage.fold`、`term_relations.fold`（5 处同文副本） | 剥 \*＋NFD 去组合符＋空白归一＋casefold | 候选池键、凭证键、核销键 |
| C 排序内层键 | `registry_azsort.norm_key` | NFD 去组合符＋空白归一＋strip＋casefold（无剥 \*、无引号折叠） | A–Z 节内排序（改语义＝登记册重排，禁） |

已知有意分歧：cnki_query 用 B 而其 docstring 称「与 check_terms 同规」（A）——本规格更正 docstring 如实标注 B；引号形键会生成两份缓存凭证，属可接受冗余，升 A 会翻动既有凭证文件名，不纳入本规格（留待需要时单独立项）。

## 3. 交付物与功能需求

| ID | 交付 | 验收判据 |
| ---- | ---- | ---- |
| FR-1 | `tools/register_lib.py` 叶子模块（仅标准库，不 import tools 其他模块）：三折叠 `fold_nfd`（C）/`norm_key`（B）/`norm_key_quote`（A）为唯一实现；`split_row`/`is_data_row`/`HEADER_WORDS`；`parse_register2_full`/`parse_register_full`（6/8 列统一解析）；`bucket_of`＋`DECOR`/`FOLD`/`GREEK`；`TERM_FILE`/`PERSON_FILE` 常量 | 三口径逐行折叠指纹与 §2 盘点表语义一致；全部迁移工具引用之 |
| FR-2 | 消费工具迁移（试金石先行，每步一提交）：term_relations → term_coverage → term_flow → term_harvest → cnki_query → check_terms → registry_azsort；各工具删除本地副本改引库 | 每步卡钉指纹不变；`check_terms.parse_registry*`/`norm_key` 等旧名保留为再出口（term_audit、tl_browser_batch、registry_azsort 不改用法仍可用） |
| FR-3 | 卡钉基准 `specs/033/bin/pin.py`：读两登记册，输出文件 sha256、分节桶计数、A/B/C 三口径逐行折叠指纹（按各口径现存属主模块取函数）、解析行元组序列摘要＋告警数、azsort scan+render 干跑内容摘要；落 `specs/033/results/pin-<标签>.json` | 改造前 pin-before 与每步改造后 pin 逐字段相等（登记册 sha256 相同前提下）；不等即作废返工 |
| FR-4 | 单元测试 `tools/tests/test_register_lib.py`：三折叠差异类（引号形/斜体形/变音符）、bucket_of（装饰符剥离、ŁØæß 转写、希腊转写、非拉丁归 #）、两 schema 解析（列数与缺列告警）、库出口与 check_terms/azsort 旧名一致性 | `python -m unittest discover -s tools/tests` 全绿 |
| FR-5 | `rules/05` 工具表登记 `register_lib.py`；specs/001 契约职责权属表补一行（登记册解析/折叠原语唯一入口 → `register_lib.py`） | 两处指针可达、措辞与本法一致 |

## 4. 口径与约束

1. **三口径不得互相合并**：A 比 B 多引号折叠、C 无剥 \*——azsort 换排序口径＝登记册重排，破坏幂等基准与既有 A–Z 稳定序。
2. **卡钉与逐行身份**：FR-3 指纹按行计，任何一行键的折叠输出变化都会显影；登记册内容由 pin 内的文件 sha256 钉住，并行会话改动登记册时重采两侧基准再比。
3. **作废条件**：pin 不等且登记册 sha256 相同 → 整步 revert 归因登记再返工；azsort 干跑报守恒残余≠0 → 全线停工；同缺口二发升级防线（ADR-0039）。
4. **提交纪律**：每迁移一个工具即 pathspec 小步提交（并行会话共用工作树，禁 `git add -A`）；改代码后清 `tools/__pycache__` 再验。
5. **改口径门槛**：三口径若未来需要增删字符类，须在本规格追加裁定记录并同步全部消费方卡钉，禁止单点改库不验消费方。

## 5. 执行记录

见 [execution-log.md](execution-log.md)。
