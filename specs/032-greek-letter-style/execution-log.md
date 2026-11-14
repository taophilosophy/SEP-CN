# specs/032 执行记录

## 2026-11-15 定性与分类

* 三件逐处提取＋上下文判读（`script/tmp/greek_classify.py`、`script/tmp/greek_edge_check.py`）：A 类 100、C 类 4、B 类 5，共 109 处；显示块（`$$`）内孤立项为零。
* 全库影响面扫描：32 件 606 处（试金石三件 109 处，试金石外 29 件 497 处）。
* C 类认定依据：belief-merging L72/L246 的 `$\Delta$` 为融合算子名；logic-dynamic L412 `$\Delta$` 为 RPDL 重复模态、L393 `$\mu$` 为「模态 μ-演算」专名成分——均非变量，按 GB 3102.11 算符正体转裸 Unicode 不加斜体。
* 边界登记：belief-merging L153/L167 存在 `$\omega$` 与 `$\omega'$` 同行混排（回改后呈文本斜体＋公式两种形态），属 ADR-0049 拍板项 ①③，本役按批准口径只转 A/C 类。
* 与源形态偏差记录（既有，非本役引入）：belief-merging zh L246 孤立 `$\Delta$` 在 en 源为复合式 `$\Delta_{\textit{IC}}$`——zh 侧 A+C=20 对 yuanwen 纯孤立 19，差 1 由对账容差吸收。

## 2026-11-15 回改执行

* `bin/rewrite_pilot.py`（五纪律内置）：dry-run 计划与定性底数一致（belief 20＝A18+C2、axiom 20 全 A、logic-dynamic 64＝A62+C2，共 104 处）→ 正式写回。
* 残余门：写回后 A/C 类残余 = 0；B 类 5 处（ω′）原样；裸 Unicode 希腊字母 107 处（104 新 + 3 既有）。
* 结构审计：行数守恒（numstat 增删相等：axiom 12/12、belief 8/8、logic-dynamic 31/31）；`$$` 行零触碰；范围限定三件。
* 台账：`results/ledger.json` 104 行（file/line/cls/old/new/cmd）。
* 幂等复跑被基线前置门正确拒绝（写回后树脏即拒，纪律 4 生效）；残余门即幂等证明。
* 目检抽查六点通过：复合式邻接（`$\neg \neg \varphi$ 与 *φ*`）、C 类正体（`Δ 是 *IC* 融合算子`、`模态 μ-演算`）、表格内散文（`（*α* 为任意语句）`）、A/公式混排（`程序 *α* 配一个模态词 $[\alpha]$`）。
* 风格告警 HEAD 版 129 对现版 129，零新增（比对 `script/tmp/s032/`）。

## 2026-11-15 工具协同

* `tools/check_math_zh.py`：新增 **C10（告警级）**——行内纯孤立希腊字母片段告警（ADR-0049 应转文字），撇号/下标/复合式不在列，不影响退出码；docstring 十类改口径。
* `tools/check_pairs.py`：count-vs-source 公式数两侧对称剔除纯孤立希腊字母片段（`GREEK_LONE_RE`），回改后三件公式数告警归零（余下 dangling-link、bracket-pair 两条为既有告警，非本役面）。
* 附带修复：check_math_zh 模块级 stdout 重包加 UTF-8 守卫——多检查器被单测进程导入时，重复 TextIOWrapper 包装因旧包装器 GC 关闭底层 buffer 而炸（本次实测）。
* 单测：`tools/tests/test_greek_style.py` 8 例（C10 六态 + 退出码语义 + check_pairs 归一两态 + 正则范围）；全套 301 例全绿（原 293）。
* 定点检查器：check_academic --strict 三件 OK；check_math_zh 三件 0 问题；check_style 三件零新增。

## 2026-11-15 渲染验收材料

* 阅读站 dev 服务（PID 2612，vitepress dev，端口 81，本仓工作树）三页可达：`/a/axiom-choice`、`/b/belief-merging`、`/l/logic-dynamic` 全 200；dev 模式为 SPA 注水，curl 只见壳，视觉判定在浏览器。
* 会话环境注记：npm script 在 Windows 不吃 env 前缀；用户裁定**使用 bun、禁止 npm**，`bun run dev` 生效（其自有 shell 支持 env 前缀）；首起撞本会话孤儿进程占 81，复用之。

## 2026-11-15 待办与移交

* [ ] 用户浏览器验收三件，拍板 ADR-0049 三边界项：①ω′ 撇号变体是否文字化；②α₁ 带下标孤立变量是否文字化；③同段 `*ω*` 与 `$\omega'$` 混排可接受度；兼拍板 φ 字形。
* [ ] 验收通过：ADR-0049 转 accepted＋rules/02 增补条款；铺开批次立项（试金石外 29 件 497 处）。
* [ ] check_all 现况：10/11，唯一红项「直角引号总检」全在他会在途日志文件（qian-yan/ri-zhi-yu-bian-ji-gui-hua.md），非本役面。
