# 012 原文列 · 执行记录

计录原则：每批一段，写清**批次、条数、证据档位、剩余告警数**；证据不可得者单列「留队」。

## 2026-11-06 阶段 0：落表（完成）

**指令来源**：用户「术语表，人名表新增一列原文：如果术语非英语，必须同时增加原文。」；同日三项裁定（原生文字 / 键后第 2 列 / 先告警后分批）。

**结构变更**

* `yi-zhe-shuo-ming.md`：五列 → 六列，插入第 2 列「原文」，全行初始 `—`；数据行 1240 全部六列（`line.count('|')==7`）。
* `ren-ming-biao.md`：同上；数据行 1043 全部六列。
* 其余五列内容逐字节未改（迁移脚本按 `split('|')` 原位插列）。

**工具变更**（`tools/check_terms.py`）

* `parse_registry_full()`：六列标准解析（`term, orig, trans, first_seen, basis, date, lineno`），旧五/四列兼容（`orig=None`）；`>6 列` 记告警。
* `parse_registry()`：保留旧六元组签名，`term_audit.py` / `tl_browser_batch.py` 免改（复用解析）。
* 新增 `has_foreign_char` / `_key_variants` / `is_non_english` / `orig_missing` / `write_orig_missing`；`FOREIGN_WORDS` 小语种词表（拉丁惯用语/德/法/阿拉伯/梵巴/藏/日/朝/汉/俄）。
* 新告警「非英语术语缺原文」：**不计硬错误**；全库运行重写 `specs/008-terminology-campaign/results/orig-missing.txt`。

**回归**

| 检查 | 结果 |
| ---- | ---- |
| `check_terms.py`（全库） | 硬错误 0；告警 528（术语 354 + 人名 174） |
| `check_terms.py --docs l/logic-provability.md` | 通过，0 疑似缺译法 |
| `term_audit.py` | 正常出报告（2276 行：术语 1236 + 人名 1040） |
| `tl_browser_batch.py --emit` | 2357 项（2270 行）正常 |
| `check_all.py` | 7 项全绿 |

**队列分类**（528 条，按 `script/_fill_orig_stage1.py` 分类器）

| 类别 | 条数 | 阶段 |
| ---- | ---- | ---- |
| 罗马化待原生文字（拼音/罗马字/梵阿转写） | 198 | 1 选出可机械者，余 2/3 |
| 希腊语 | 37 | 2（语料 9260 字可证） |
| 印度-闪米特（梵/阿/波斯，含变音标记） | 70 | 3（语料仅 49+6 字，须外源） |
| 非拉丁人名 | 76 | 2（希腊/梵/谚文者）→3（阿/藏） |
| 其它非拉丁 | 2 | 2 |

**阶段 1 分类器已知误判（干跑发现，待修）**

* `dictum (Abelard)`：括注为人名消歧，原文应取主形 `dictum` → 已修为「括号首字母小写才取括注」。
* `Cheka / gulag / partinost`：西里尔源词，已内置映射（Чека / ГУЛАГ / партийность）。
* `yì`、`hadé`、`Lüshi chunqiu`：CJK 源词（义（義）/ 华丽 / 《吕氏春秋》），`FOREIGN_WORDS` 未覆盖 → 阶段 1 需 CJK 覆盖表排除或直接填。
* `naïve realism`、`Gödel’s theorem`、`Löwenheim-Skolem theorem`、`Müller-Lyer illusion`、`Łukasiewicz logic`、`Petőfi Circle`：含人名变音符的**英文术语/机构名**，填自身拼写即可消警（非原生文字问题）。

**语料可证性实测**（决定阶段 2/3 分流）

| 文字 | 字符数 | 文件数 |
| ---- | ---- | ---- |
| Greek | 9260 | 360 |
| Cyrillic | 998 | 20 |
| Hangul | 522 | 7 |
| Hebrew | 139 | 13 |
| Arabic | 49 | 3 |
| Devanagari | 6 | 1 |
| Tibetan | 0 | 0 |

**遗留**

1. `rules/03-terminology.md` 第 34 行「登记格式（两登记册统一，五列）」待改为六列并说明原文列（阶段 4 与条文开关同批落地，或提前单独改条文）。
2. 并行会话若按五列写表将致列错位——检查器有 `>6 列` 告警兜底，交接卡已列纪律。
