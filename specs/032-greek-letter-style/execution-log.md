# specs/032 执行记录

## 2026-11-15 定性与分类

* 三件逐处提取＋上下文判读（`script/tmp/greek_classify.py`、`script/tmp/greek_edge_check.py`）：A 类 100、C 类 4、B 类 5，共 109 处；显示块（`$$`）内孤立项为零。
* 全库影响面扫描：32 件 606 处（试金石三件 109 处，试金石外 29 件 497 处）。
* C 类认定依据：belief-merging L72/L246 的 `$\Delta$` 为融合算子名；logic-dynamic L412 `$\Delta$` 为 RPDL 重复模态、L393 `$\mu$` 为「模态 μ-演算」专名成分——均非变量，按 GB 3102.11 算符正体转裸 Unicode 不加斜体。
* 边界登记：belief-merging L153/L167 存在 `$\omega$` 与 `$\omega'$` 同行混排（回改后呈文本斜体＋公式两种形态），属 ADR-0049 拍板项 ①③，本役按批准口径只转 A/C 类。
* 与源形态偏差记录（既有，非本役引入）：belief-merging zh L246 孤立 `$\Delta$` 在 en 源为复合式 `$\Delta_{\textit{IC}}$`——zh 侧 A+C=20 对 yuanwen 纯孤立 19，差 1 由对账容差吸收。

## 2026-11-15 回改执行

（回改脚本、台账、残余门、结构审计结果待填）

## 2026-11-15 工具协同

（check_pairs 归一、check_math_zh C10 的实现与验证结果待填）
