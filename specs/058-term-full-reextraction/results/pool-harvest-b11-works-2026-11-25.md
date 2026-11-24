# 收割批 11：著作名与古典语词（斜体片段审计，2026-11-25）

池的 `italic` 抽取是「斜体边界切分」，切出来的是片段（`Principia`、`Essays`、`et al`），不适合当著作名审计源。改从**中文译文本身**取斜体：`\*…\*` 扫描 `a/`–`z/` 1880 文件，得 27,187 个不同片段、45,843 次；与登记册强归一比对，未登记且 ≥5 次者 690——其中绝大多数是期刊名（Synthese 261、Philosophical Studies 258、Philosophy and Phenomenological Research 174…）。

## 一、期刊不入册（口径记录）

登记册 0 条期刊行，此前各批也未登。本批确认：**期刊名作书目专名处理，保留原文，不进术语表**。理由：译名无统一通行形（《哲学研究》与《哲学与现象学研究》并存），且栏位（原名、卷期）属书目层，与术语层混登会污染检索。若日后要查重，另立书目层清单，不并入 `shu-yu-biao.md`。

## 二、著作名缺口（4 条）

| 英文 | 主形 | 语料 | 说明 |
| ---- | ---- | ---- | ---- |
| Isagoge | 《导论》（波菲利） | 133 | 波菲利《导论》；原文列补 Εἰσαγωγή |
| The Presocratic Philosophers | 《前苏格拉底哲学家》 | 13 | Kirk–Raven–Schofield 文集 |
| Essays on Actions and Events | 《行动与事件论文集》 | 12 | 戴维森 1980 文集 |
| The Philosophical Writings of Descartes | 《笛卡尔哲学著作集》 | 14 | Cottingham 等英译本 |

并键 4 条（同书异形）：`Tractatus Logico-Philosophicus / Tractatus`、`Treatise of Human Nature / A Treatise of Human Nature`、`Summa Theologiae / Summa Theologica`、`dharma / dharmas`。

## 三、古典语词（13 条）

斜体里的拉丁／希腊短语不是书名，而是术语，且不少是高频：locus classicus 89、tout court 151、par excellence 118、magnum opus 136、ad infinitum 103。这批全部补齐：

* doxa（δόξα）意见 ／ intentio 意向 ／ ens realissimum 最实在的存在者 ／ pietas 虔敬
* reductio ad absurdum 归谬法（**并入**既有 `reductio` 行）
* per se 就其自身 ／ ipso facto 凭其事实本身 ／ ad infinitum 至无穷 ／ mutatis mutandis 略作必要改动 ／ de facto 事实上 ／ locus classicus 经典出处 ／ magnum opus 代表作 ／ par excellence 典范（地） ／ tout court 全然

非英语键的原文列按既有惯例补源语形（希腊文用希腊字母，拉丁文重写拉丁形），故本批未新增「非英语术语缺原文」告警（仍 148 条）。

## 四、人名侧：结论是「不需要补登」

用 token 子集法（候选全名 token ⊆ 人名行键或别名 token）核 `person` 类候选 ≥10 次者 3,126 条，抽样反查发现绝大多数根本不是人名——池的 `person` 类型装的是大写短语（`Social Sciences` 413、`Common Cause` 408、`Health Care` 406、`Mental Imagery` 387…）。真姓名者经批 6 已逐条核对在册（`van Inwagen, Peter`、`Pico della Mirandola, Giovanni`、`Conway, Lady Anne`、`Ibn Daud, Abraham` 等，均姓先形，故按整串比对必假阳性）。

**人名侧真正的缺口是质量而非数量**：435 行译形仍为拉丁字母（ADR-0022「无通行汉名者保留英文」）、781 行缺籍属／生卒。两者都需要在线查证，当日通道全不通，故本批不动；`Dalen, Dirk van`（语料 47 次）等高频者最值得通道恢复后先查。

## 五、落册与门禁

* 清单：`tasks/manifests/2026-11-25-058-batch63-terms.json`（17 行）
* `term_flow` 17/0；池 published=14；`shu-yu-biao.md` diff +21／−4（17 新行＋5 键并入），数据行 8,796→8,813（+17），`registry_azsort` 守恒
* `check_terms` 硬错误 0（自洽 0）
* 本批无主形撞形告警（reductio 已于落册前并入）

## 六、遗留

1. 斜体审计脚本尚未入库（本轮为一次性内联脚本），下轮应固化为 `bin/audit_italic_titles.py`，并把「期刊词表」与「缩写残片」（`In Cat`、`In Isag.`、`Phys.`、`Sent.`、`Acad.`）作为过滤项。
2. 未登记 ≥5 次的 690 行里，除期刊与残片外还有 `Abstractiones`、`Repastinatio`、`Dialoghi`、`Antoniana Margarita` 等冷僻书名——缺权威汉译形，按「不猜」留待查证。
3. Sikh 词（gurmat 45、śabad 18、haumai 11）与 `positum`、`Schein` 等术语，义项需按条目语境定，留待有凭证时再立。
