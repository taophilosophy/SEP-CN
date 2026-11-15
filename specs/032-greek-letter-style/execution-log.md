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

## 2026-11-15 验收发现：公式渲染缺陷三族（用户浏览 axiom-choice 页报障）

**定性：三族全为既有缺陷，非 ADR-0049 试金石回归**（涉事行不在 104 处台账；yuanwen 归因明确）。

* **F1 裸 align 无 $$ 包裹**（6 处/2 文件：axiom-choice L17/93/97/212/270、belief-merging L185）：转换层遗留。机制＝markdown 把 `\\` 吃成 `\`（CommonMark 转义）→ MathJax findTeX processEnvironments 抓裸环境 → 排版已损伤＋宏未展开 → 红 raw TeX。用户粘贴中的 `\ V_{\alpha+1}` 即 markdown 损伤后形态，源文件完好。
* **F2 zh 侧 `\\` 退化**（impossible-worlds L212）：yuanwen `\\` → zh `\ `，翻译期损伤；修回即向基线收敛，零分歧登记。
* **F3 `\bfrac` 展开 artifact**（axiom-choice L68 ×2）：`${^{1}\unicode{x2044}_{2}}$` 系翻译期展开 SEP 宏 `\bfrac{1}{2}` 的产物，MathJax 排版失败裸显。en 原文用宏（yuanwen 保真保留 `\bfrac{1}{2}`）。
* 同族顺带：axiom-choice L270 `\mbox{by (**)}`/`\mbox{using (*)}` 英文连接语 → `\mbox{由（**）}`/`\mbox{用（*）}`（C8 家法）。
* 宏展开取各词条译者行内先例：`\sP`→`\mathcal{P}`（L91 先例）、`\Def`→`\mathrm{Def}`（L95 先例）、`\mymod`→`\textit{mod}`（belief-merging L66 先例）。

**修复**：`bin/fix_render.py`（22 笔，行级预检＋台账 `results/render-ledger.json`＋残余门＋行数守恒审计）全过；`bin/fix_render.py` 残差门与 `script/tmp/s032/bare_env_scan.py` 首版 DD_RE 无转义感知，曾把 impossible-worlds L180 相邻行内公式（`令 $\$$ 是…$\$w$`）假配对成块——已加 `(?<!\\)` 修正，impossible-worlds 裸环境系误报撤案。

**验证**：修复行经 protectMath 全部变哨兵（bun 实测）；check_math_zh 三件 0 问题；check_style HEAD 136 vs 现 136 零新增；check_pairs 与 HEAD 同集。

**F1 排查方法论注记**：check_math_zh math_spans 只认 `$` 定界，裸环境内容完全不进扫描——这是 C1 在 axiom-choice 静默的根因（`\sP` 明明在 needs_expansion）。

**\unicode 家族全量修复（续，用户 logic-linear 页二次报障实证 x214b 同败）**：`bin/fix_unicode_family.py` 27 笔/5 文件——logic-linear `\unicode{x214b}`→`⅋`（U+214B，18 处，en 原形 SEP 宏 `\lpar`，`\mathrel` 包装原样保留；孤立提法与兄弟 `$\otimes$`/`$\oplus$` 公式形态一致不入裸文本）、logic-relevance `\unicode{x22b0}`→`⊰`（en 原形 `\prurel`）、diodorus `\unicode{x2B26}`→`⬦`、heritability/justep 的 bfrac 分数 artifact→通行 slash 记法（`$V_{G}/V_{P}$`、`$1/P(A)^{n-1}$`）。宏语义由码点保真，C1 家法展开由劣形转优质形。字体事实：⁄ 在 MathJax TeX 字体内；⅋/⬦ 不在，走 MathJax 未知字符回退（系统字体 SVG text 渲染）。台账 `results/unicode-ledger.json`。**渲染确认待用户刷新 logic-linear/logic-relevance/diodorus-cronus/heritability/justep-coherence 五页。**

## 2026-11-15 验收通过与体例固化

* 用户浏览器验收（axiom-choice/belief-merging/logic-dynamic/logic-linear/logic-relevance 等），**批准通过**。
* ADR-0049 proposed → accepted（状态行与跟进项更新，只追加纪律）；[rules/02](../../rules/02-style.md) 增补「孤立希腊字母」条款（变量斜体、算子正体、派生形保持公式、`\phi`/`\varphi` 归一 φ）；三个边界拍板项按原口径固化（B 类保持公式）。
* C10 升硬门裁定挂起：待 C 类人工判读清单清零（升门前残余项会顶红门禁）。

## 2026-11-15 铺开批次（ADR-0049 accepted 后同日执行）

* `bin/rollout_batch.py`（全库扫描→分桶→逐文件树净检查→反引号行守卫→分组计数替换）：A 类 **425 处/28 文件**写回，台账 `results/rollout-ledger.json`；C 类嫌疑 27 处（孤立 `$\Delta$`/`$\mu$`/`$\Omega$`/`$\Sigma$`/`$\Lambda$`）不动出清单。
* `bin/fix_c_deferred.py`（C 嫌疑逐处人工判读，判据 GB 3102.11）：**24 处斜体**（字母表/签名 Σ、可能世界集与状态集 Ω、二阶测度 μ、LU 语境 Δ——均为变量或具名集）＋**3 处正体**（computability 无界极小化算子 μ ×2、ramsey 增量 Δ ×1，算符）。台账 `results/c-deferred-ledger.json` 含逐笔 why 字段。
* 守卫与豁免：`$$` 行、反引号行（行内代码与 Quine 式引名冲突，quine-nf L13 实测——该行 5 个 `$\Phi$` 豁免待手工）整行不动；脏树文件跳过（本轮无一命中）。
* 工具坑修复：rollout 首版同行多同类片段计数核验未分组（pilot 同坑复踩，已按（行，片段）分组）；rollout 台账路径含 Windows 反斜杠，阶段 2 归属核对须归一。
* 终检：28 文件残余孤立片段仅 5 处 `$\psi'$`（B 类撇号派生形，合法留存）；check_style HEAD 7 vs 现 7 零新增；**check_all 11 项全绿**（含他会面的直角引号红项已由他会收口）。
* 铺开合计 452 处＋试金石 104 处＋\bfrac/\unicode artifact 族 31 处＝ADR-0049 全库落日均告完成；存量仅余 quine-nf L13 反引号行 5 处（人工）与 B 类保持项。

## 2026-11-15 转换层并入（用户指令：把转换并入 HTML 转 en .md 流程）

* `tools/yuanwen.py` 新增两条转换规则（模块常量区＋inline_to_md 恢复循环）：
  * **R1**：行内孤立希腊字母（非 C 嫌疑 Δ/μ/Ω/Σ/Λ）转换时即转斜体文字——与 rollout_batch 同映射表、同 C 嫌疑口径，未译条目开卷即合规；
  * **R2**：SEP 原文裸排显示环境（\[…\] 之外的 \begin{align} 等，MathJax processEnvironments 语义）转换时补 `$$…$$` 包裹——F1 缺陷（markdown 吃 `\\` 行分隔）根因修复。宏（\lpar/\bfrac）仍保真保留，C1 家法展开留在翻译期。
* 验证：新增单测 7 例（孤立/嫌疑/复合/撇号/显示式/已包裹/散文混合）；全套 327 例全绿；**axiom-choice 全流程 scratch 重转对照**（monkeypatch 写盘临时目录，引注/脚注/表格全管线）：diff 56 行，规则效应 17 对（5 环境包裹＋12 希腊转文字），其余 25 行逐一对账为配对删除行与空行平移，零意外变更；\bfrac/\sP 保真 ✓。
* 存量不回改：已转词条维持现态（check_pairs 归一口径兼容两代形态）；未译条目随下次 fetch/重转自动获得新体例；契约 `specs/001.../cli.md` yuanwen.py 节注记同步。

## 2026-11-15 待办与移交（渲染缺陷补遗）

* [ ] 用户浏览器验收三件，拍板 ADR-0049 三边界项：①ω′ 撇号变体是否文字化；②α₁ 带下标孤立变量是否文字化；③同段 `*ω*` 与 `$\omega'$` 混排可接受度；兼拍板 φ 字形。
* [ ] 验收通过：ADR-0049 转 accepted＋rules/02 增补条款；铺开批次立项（试金石外 29 件 497 处）。
* [ ] check_all 现况：10/11，唯一红项「直角引号总检」全在他会在途日志文件（qian-yan/ri-zhi-yu-bian-ji-gui-hua.md），非本役面。
* [ ] **\unicode 构件族**（29 处/6 文件）：axiom-choice 2＋家族五件 27 处已全量修复（见上节），渲染确认待用户浏览器验收；若 ⅋/⬦ 回退渲染不理想，备选方案为 MathJax config 加 configmacros 宏表映射。
* [ ] **check_math_zh C11（裸数学环境检测）**：告警级，检测 `$$` 外 `\begin{align}` 等——防 F1 类复发（本轮未实现，登记待做）。
