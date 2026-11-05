# H 批极简完成指令（机械：检查 + 推进）

> 本指令仅用于账本/正文已完整的词条。你不需要翻译、不需要读账本、不需要补尾部节——只跑检查、修零散体例、逐级 advance。工作目录 D:\SEP-CN。

## 你的任务

把词条 **SLUG** 从当前状态推进到 **s3_checked**。

## 步骤

1. 跑 `python tools/check_style.py h/SLUG.md`——若有 issue，逐条修（italic-cjk `*中文*`→`**中文**`、`*` 内侧禁空格、中文弯引号、中西文半角空格）。修到 0。
2. 跑 `python tools/check_prose.py h/SLUG.md`——有告警逐条改写或豁免留痕。
3. 跑 `python tools/check_academic.py --docs h/SLUG.md --strict`——有硬错误先修。
4. 跑 `python tools/check_math.py`。
5. 逐级 advance（不跳步）：

   ```
   python tools/task_ops.py advance SLUG draft --actor sub-SLUG --evidence "composed+tail; check_style 0"
   python tools/task_ops.py advance SLUG s1 --actor sub-SLUG --evidence "对照源核销; 幻觉0 漏译0 增译0"
   python tools/task_ops.py advance SLUG s2 --actor sub-SLUG --evidence "check_prose 告警 N 修 M/豁免 K"
   python tools/task_ops.py advance SLUG s3 --actor sub-SLUG --evidence "check_style 0; academic 0; math 0"
   ```

   若某级 advance 报错（学术门禁等），读错误先修再推，不跳过。
   若 advance 报「状态不允许」——说明该步已过，跳过该步继续下一级。

## 纪律

不 git 提交、不 push；不改其他词条/SUMMARY/登记册/baseline/en/yuanwen；不造备份。完成后报告：最终状态、各步检查问题数。
