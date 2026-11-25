# 补丁三出口判据（ADR-0085）

补丁池（`baseline/en-patches/`）只收**个案外科修补**，不承担“公共缺陷”的兜底。任何修补先走三问，再定落点。

## 三问定出口

| 顺序 | 问题 | 若“否” | 若“是” |
| ---- | ---- | ---- | ---- |
| Q1 | 能否写成结构／编码规则，且不依赖逐句语义判定？ | **勘误表**（文字层，禁入转换层，必要时中文译注） | 进入 Q2 |
| Q2 | 同形是否跨件（≥2 件）？ | **补丁池**（个案，`origin: upstream-typo`） | 进入 Q3 |
| Q3 | 升档后全库影响是否可枚举？ | **暂留池**（`origin: converter-gap`＋升档计划） | **升档转换器**（改 `tools/yuanwen.py`，删补丁） |

“影响可枚举”＝等价类测试可写＋I2 全量重转零漂移＋B3.1 集合级对照转红 0。

## 出处字段

补丁头必填 `origin`：

* `upstream-typo`：上游自身瑕疵（漏空格、缺闭合标签），转换层无从推导；
* `converter-gap`：转换器规则缺失，须附升档计划，升档后退役。

缺失或值域外由 `tools/en_patch_lib.py` 解析时硬失败。INDEX 由 `specs/039 bin/migrate_en_patches.py --refresh` 再生（保留 `created` 与 `origin`）。

## 公共性探针

`python tools/check_en_patches.py` 对每条空白差补丁提取变更核心 token，统计它在其他词条中的命中：

* 他件命中 ≥1 → 输出 `PUBLIC …（候选升档）`，计入 `public_candidates`；
* 只告警不拦；标记差补丁不探（标签同形≠同一缺陷）；
* `--no-public` 关闭探针。

探针只回答“是否跨件”，升档与否仍按 Q1／Q3 人审。

## 升档与退役

1. 改 `tools/yuanwen.py`（禁只改产物）；
2. 全量重转，I2 零漂移、B3.1 集合级转红 0；
3. 删除对应 `*.patch`，`--refresh` 再生 INDEX；
4. `baseline/en-errata/en-errata.md` 对应行注“已升档退役”，保留追溯。

判据与判定权归属见 [judgment-rights.md](judgment-rights.md)；补丁准入谓词（C2）与三律见 ADR-0062／0063。
