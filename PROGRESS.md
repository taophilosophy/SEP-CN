# 项目进度

<!-- 本文件由 `python tools/progress.py` 自动生成，不手改。数据源：SUMMARY.md（结构）、baseline/entries.json（基线）、journal/（进度事实）、tasks/（仅调度侧阻塞）。 -->

生成时间：2026-11-21 00:44（UTC）

## 总览

|指标|数值|
|---|---|
|SUMMARY 正式词条（重译对象）|1873|
|别名词条（— see，不建任务）|641|
|占位母词条（* 前缀，不建任务）|180|
|已建英文基线|1873|
|已建任务（journal 词条）|1199|
|例行/维护任务（不计状态机）|2|
|**账外词条（无 journal，未建任务）**|**674**|
|全库仅标题骨架（H1 之外无正文）|1443|
|其中：骨架且在账内（有任务未开工）|769|
|其中：骨架且在账外（无任务）|674|
|全库有正文（已译出内容）|430|
|**账实不符（cleared 有正文／有正文零过程记录）**|**0**|
|核心段完成（draft..R3 七节点）|394|
|强制集完成（s0/s2.4/global/R1/R2/R3）|394|
|其中：依赖回补重算（specs/052）|394|
|完整饱和（16 节点全过）|0|
|在途（已开工未走完核心段）|57|
|未开工（journal 内无 pass 事件）|748|
|阻塞（调度侧，journal 未迁移）|2|

> **分母口径**：完成／强制集／饱和／在途／未开工五项的分母是 **journal 词条 1199 件**，不是全库正式词条 1873 件。差额 674 件无 journal 记录（全部为仅标题骨架，`rules/01` 约定未翻译条目为仅含 H1 的骨架）；骨架合计 1443 件（账内 769 ＋ 账外 674），这些页已随 SUMMARY 上站但对读者为空。要把账外件计入进度，须先建任务（`task_ops.py create`）。

> **强制集口径**：强制集完成 394 件中，394 件的 s0/s2.4/global 是 2026-11-19 按现行判据重算所得（`specs/052` 回补批次，journal 事件 note 以 `backfill:` 标记，状态不迁移）。回补证明"内容过现行判据"，不证明"该件已完成 s2.5 人审"——读强制集完成数时须连同此行一起读。

## 节点通过数（journal 口径，共 16 节点）

|节点|通过数|
|---|---|
|F1|0|
|F2|0|
|P1|0|
|P2|0|
|P3|0|
|P4|0|
|R1|407|
|R2|402|
|R3|400|
|S3|431|
|draft|441|
|global|395|
|s0|420|
|s1|431|
|s2|431|
|s2.4|395|

## 按首字母（正式词条 / 基线 / 任务 / 核心段完成）

|字母|正式词条|已建基线|已建任务|核心段完成|
|---|---|---|---|---|
|A|160|160|160|60|
|B|63|63|62|20|
|C|171|171|171|29|
|D|92|92|92|27|
|E|99|99|99|29|
|F|96|96|96|5|
|G|49|49|49|18|
|H|61|61|61|17|
|I|76|76|75|35|
|J|38|38|38|14|
|K|36|36|36|22|
|L|144|144|30|30|
|M|139|139|15|13|
|N|50|50|11|10|
|O|21|21|13|12|
|P|164|164|12|8|
|Q|33|33|33|4|
|R|85|85|85|14|
|S|160|160|19|16|
|T|69|69|8|3|
|U|4|4|2|1|
|V|15|15|15|0|
|W|36|36|5|2|
|X|3|3|3|2|
|Y|2|2|2|0|
|Z|6|6|6|2|

## 在途词条（已开工未走完核心段）

|slug|已过节点数|已过节点|
|---|---|---|
|abelard|9|R1 R2 R3 S3 global s0 s1 s2 s2.4|
|abhidharma|9|R1 R2 R3 S3 global s0 s1 s2 s2.4|
|abner-burgos|9|R1 R2 R3 S3 global s0 s1 s2 s2.4|
|abortion|9|R1 R2 R3 S3 global s0 s1 s2 s2.4|
|advance-directives|9|R1 R2 R3 S3 global s0 s1 s2 s2.4|
|axiom-choice|2|draft s0|
|bradley|5|R1 S3 draft s1 s2|
|brentano|5|R1 S3 draft s1 s2|
|brentano-judgement|4|S3 draft s1 s2|
|buddha|4|S3 draft s1 s2|
|buddhism-chan|4|S3 draft s1 s2|
|buddhism-huayan|4|S3 draft s1 s2|
|butler-moral|4|S3 draft s1 s2|
|cancer|4|S3 draft s1 s2|
|cloning|4|S3 draft s1 s2|
|conceptual-art|4|S3 draft s1 s2|
|conscience|4|S3 draft s1 s2|
|cosmology-30s|4|S3 draft s1 s2|
|cosmopolitanism|4|S3 draft s1 s2|
|dance|2|draft s0|
|dynamic-semantics|2|draft s0|
|ehrenfels|4|S3 draft s1 s2|
|fitness|4|S3 draft s1 s2|
|grounding|2|draft s0|
|habermas|2|draft s0|
|haecceitism|1|s0|
|halevi|2|draft s0|
|hamann|1|s0|
|heritability|2|draft s0|
|heytesbury|2|draft s0|
|hume-moral|2|draft s0|
|iamblichus|4|S3 draft s1 s2|
|identity-ethics|9|R1 R2 R3 S3 global s0 s1 s2 s2.4|
|impossible-worlds|2|draft s0|
|intrinsic-extrinsic|2|draft s0|
|james-mill|4|S3 draft s1 s2|
|kant-development|4|S3 draft s1 s2|
|kant-judgment|4|S3 draft s1 s2|
|kant-religion|4|S3 draft s1 s2|
|kant-spacetime|4|S3 draft s1 s2|
|kant-transcendental|4|S3 draft s1 s2|
|knowledge-how|4|S3 draft s1 s2|
|kukai|4|S3 draft s1 s2|
|modality-varieties|1|s0|
|newton-stm|4|S3 draft s1 s2|
|philanthropy|2|draft s0|
|quantum-bayesian|5|R1 S3 draft s1 s2|
|repugnant-conclusion|4|S3 draft s1 s2|
|tarski-truth|2|draft s0|
|telesio|5|R1 S3 draft s1 s2|
|type-theory|1|s0|
|vaihinger|2|draft s0|
|xunzi|2|draft s0|
|yogacara|2|draft s0|
|yorck|6|R1 S3 draft s0 s1 s2|
|zhu-xi|9|R1 R2 S3 draft global s0 s1 s2 s2.4|
|zombies|7|R1 R2 S3 draft s0 s1 s2|

## 阻塞任务（调度侧，journal 未迁移 blockers）

|slug|阻塞原因|
|---|---|
|haecceitism|逐段对齐：EN 块 199/249 未配对（详情 specs/044 results）|
|hamann|逐段对齐：EN 块 195/263 未配对（详情 specs/044 results）|
