# H 批继续翻译指令（Group B：账本部分，续译）

> 本指令用于**账本已有部分段落**（step1+step2）但未覆盖全部源的词条。从账本断点**续译**，不重译已完成的段落。工作目录 D:\SEP-CN。

## 你的任务

处理词条 **SLUG**，续译至 **s3_checked**。不执行 r1/r2/r3/done。

## 第 1 步：定位断点

1. 读 `tasks/h/SLUG.ledger.yaml`，取最后一段的 `id`（记为 N）。
2. 读 `yuanwen/h/SLUG.md`，按空行分块为段落列表。
3. 账本已有段落对应源的前 N 段（逐段 source 已记录）。**断点 = 第 N+1 段起**。

## 第 2 步：续译（边译边写，增量写回）

从第 N+1 段起逐段翻译，**每完成 3-5 段就追加**到 `tasks/h/SLUG.ledger.yaml`（保持 YAML 结构：`- id: M\n    source: |-\n    step1: |-\n    step2: |-`），并把 step2 拼合稿追加到 `h/SLUG.md`。
* 若账本结构与源段落**不逐段对位**（某段 source 与源第 k 段不符），先纠正——以源为准重排，缺段补译。
* 元素映射/体例：见 `rules/02-style.md`；脚注键名与 yuanwen 逐字符一致。
* 全部源段译完后：拼合 `h/SLUG.md` 完整稿（H1+版本行+正文+尾部节），确认 `h/SLUG.md` 有参考文献/相关词条等尾部节。

## 第 3 步：推进

```
python tools/task_ops.py advance SLUG draft --actor sub-SLUG --evidence "ledger N 段 step1+step2 全齐; doc 完整"
python tools/task_ops.py advance SLUG s1 --actor sub-SLUG --evidence "MTPE 幻觉0 漏译0 增译0; 术语核销"
python tools/task_ops.py advance SLUG s2 --actor sub-SLUG --evidence "check_prose 告警 N: 修 M/豁免 K"
python tools/task_ops.py advance SLUG s3 --actor sub-SLUG --evidence "check_style 0; academic 0; math 0"
```

s1/s2/s3 advance 前先跑对应检查（对照源核销 / check_prose / check_style+check_academic --strict+check_math）。s3 学术门禁自动挂钩。

## 纪律
* 不 git 提交、不 push；不改其他词条/SUMMARY/登记册/baseline/en/yuanwen；不造备份。
* 若源某段无法理解：回 `en/SLUG/index.html` 核对；仍不解记录并跳过，不要卡死。
* 完成后报告：最终状态、账本段数、s1/s2/s3 问题数、需人工复查项。
