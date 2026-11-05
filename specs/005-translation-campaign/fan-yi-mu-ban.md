# SEP 词条统一翻译模板

**版本**：v1.0（2026-10-28）｜**效力**：specs/005 审阅战役的操作模板，对全部 retranslate/update 词条任务生效；体例细则以 `rules/02-style.md` 为准，任务流程以 `rules/04-translation-workflow.md` 为准，术语以 `fang-fa-lun/gong-cheng-fang-fa.md` S1–S2 为准。冲突时规则 > 本模板；本模板不得与规则冲突。

**依据**（零信任，可回溯）：① `baseline/entries.json` 全部 1878 条 SEP 真实页面的结构实测（2026-10-28，统计见 §1）；② 已过一校的演示词条 `a/alcmaeon.md`（任务 `tasks/a/alcmaeon.json`，state=s1_checked）；③ `yuanwen/` 逐字符镜像库的转换约定（`tools/yuanwen.py`，2026-10-28 全量复审计零缺陷）。SEP 官方作者手册在线路径不可达（/manual/ 404，礼貌抓取两试即止），页面结构以本地原始物实测为准——比手册更可靠，因为它就是 1878 条真实页面本身。

## 1. SEP 词条页结构总览（实测）

对 1878 条 `en/<slug>/index.html` 的统计：

| 元素 | 出现率 | 说明 |
| ---- | ---- | ---- |
| citation_title / citation_author 元数据 | 100% | 标题与作者的唯一权威来源；34% 为多作者（638 条） |
| pubinfo（首次发表/实质修订） | 100%（84% 含修订） | 版本钉来源（任务 JSON 的 version_pin） |
| 导语段（无标题引言） | 100% | 摘要式开篇，TOC 之前 |
| 编号章节（h2）+ 小节（h3） | 100% / 94% | `1. Title` / `1.1 Title` 形态 |
| Academic Tools | 100% | 固定三件：How to cite / InPhO / PhilPapers |
| Related Entries | 100% | 词条间导航列表 |
| 致谢（Acknowledgments） | 39% | 常在 Related Entries 之后 |
| notes.html（原文脚注） | 37%（690 条） | 正文 `<sup>[n]</sup>` 引到 notes 页 |
| 补充材料 `<slug>.<x>.html` | 29%（546 件） | figdesc（图片描述页）占 3% |
| 词条包内图片 | 13% 词条 / 约 1482 处引用 | 含点图放大的大图链 |
| 数学定界符 `\(\)` / `\[\]` | 24% | 含 prooftree、align、xymatrix 等环境 |
| 表格 | 100% 页面含 table 标签 | 正文数据表仅部分词条 |

zh 侧译文按**同样的章节序**逐节对位翻译（便于逐节核销），但不复制原页的 TOC 与站点框架。

## 2. 元素级映射总表（源 → zh 模板）

| # | SEP 源元素 | zh 模板 | 示例（已验证的 alcmaeon 实测） |
| ---- | ---- | ---- | ---- |
| 1 | 页面标题 + 作者 | H1 = SUMMARY 条目文字：`# 中文名 English-name (Author1 and Author2)` | `# 克罗顿的阿尔克迈翁 Alcmaeon (Carl Huffman)` |
| 2 | pubinfo | 正文首行斜体：`*首次发表于 YYYY 年 M 月 D 日；YYYY 年 M 月 D 日实质修订。*`（无修订则止于"首次发表"句） | `*首次发表于 2003 年 4 月 10 日；2025 年 7 月 18 日实质修订。*` |
| 3 | 导语段（preamble） | 无标题，直接正文段落；作为摘要整体译出 | alcmaeon 第 5 行（"克罗顿的阿尔克迈翁（Alcmaeon of Croton）是……"） |
| 4 | 编号章节 h2 | `## 1 中文名`——保留原编号、**去掉英文句点**、空格后接中文标题；`1.1` → `### 1.1 中文名`；层级不得跳级 | `## 1 生平与著作`；`### 1.1 医生还是哲学家？` |
| 5 | 章节标题中的斜体/书名 | 标题内 `*斜体*` 保留；《书名》用书名号 | （照 rules/02 引号与书名号规则） |
| 6 | 正文引用组 `(Author year, p. X)` | **原样保留**（作者姓、年份、页码不译）；文内编年引证照录 | `（Zhmud 2012a, 366; 2014, 100）` |
| 7 | 引块（残篇、原始文本引文） | `>` 引用块；DK 等文献编号保留；引文译出，编号括注照录 | `> 克罗顿的阿尔克迈翁……说了如下的话……（DK 12B1）` |
| 8 | 行内强调/书名 | `*斜体*`；著作名用《》，篇名用《》或引号按中文学术惯例 | 《形而上学》986a22 以下 |
| 9 | 图片 `<img>` | `![图注](../yuanwen/assets/<slug>/<文件名>)`；图注（figlabel/caption）译出后作为图下一行斜体；reprinted with permission 必须在图注标明来源（rules/01） | 见 §4 图注骨架 |
| 10 | 点图放大链 `<a href="X-large.gif">` | 大图与小图都按 #9 本地化引用；正文锚点 `图 N` 语义译出 | （yuanwen 侧已实现同款，键一致） |
| 11 | 表格 | markdown 表格，`:---:` 居中（rules/02），单元格紧凑风格；`<caption>` 表题译出为表格前斜体行 | （rules/02 表格条款） |
| 12 | 数学 `\(\)`/`\[\]`/环境 | 定界符转 `$…$` / `$$…$$`，LaTeX 内容**逐字符保留**（宪法 VI；含 prooftree、align、xymatrix）；`<sub>/<sup>` 转 `_{x}` / `^{x}` | （与 yuanwen 镜像逐字符一致，便于对照） |
| 13 | 原文脚注 `<sup>[n]</sup>` → notes.html | `[^note-N]` 引用；文末 `## 脚注` 节列出 `[^note-N]: 译文`——**键名与 yuanwen 逐字符一致**（note-N；补充材料专用键 note-\<x\>-N 同理） | 见 §4 脚注骨架 |
| 14 | Acknowledgments | `## 致谢`，整段译出 | （39% 词条适用） |
| 15 | Academic Tools | `## 学术工具`——固定四行，链接原样：如何引用本词条（archinfo）/ 预览本词条的 PDF 版本（SEP 学会之友）/ InPhO / PhilPapers；bullet 形态（v1.3 裁定，在先成例 36+）；存量表格形态四项齐备者合规不再改形 | alcmaeon 206–210 行 |
| 16 | Other Internet Resources | `## 其他网络资源`——条目译出（条目名+说明），URL 原样；无条目时写 `[欢迎向作者提出建议。]` | alcmaeon 212–214 行 |
| 17 | References / Bibliography | `## 参考文献` + 斜体说明行 `*以下文献从原文照录，不作翻译。*`；子标题（Texts and Commentaries 等）保留英文；条目逐字符照录——**中国文献条目（古今）一律译为中文**（ADR-0011） | alcmaeon 115–204 行 |
| 18 | Related Entries | `## 相关词条`——SEP slug 对应的 SUMMARY 中文名，` | ` 分隔一行排布；站内链接由管线在对应词条重译完成后统一挂接（先以译注占位） | alcmaeon 216–220 行 |
| 19 | 补充材料 `<slug>.<x>.html` | 独立文件 `<letter>/<slug>.<x>.md`；正文引用写 `（见[补充材料](<slug>.<x>.md)）`；文件首行 `# <英文标题中译>（<slug> 补充材料）`，第二行斜体版本行同 #2 | yuanwen 头为 `# <title> — <x>（supplement）`，zh 侧对位 |
| 20 | figdesc（图片描述页） | 随其所属词条译为 `<slug>.figdesc.md`，作为无障碍描述保留 | （47 条适用） |
| 21 | 正文交叉引用 `see X` | 语义译出（"见……"/"——见……"）；X 为词条时用 SUMMARY 中文名，未译词条按管线占位（同 #18） | SUMMARY 中 `\*…——见…` 行既有惯例 |
| 22 | 译注 | `（译注：……）`单独成句，谨慎克制，仅补现状说明（rules/02） | alcmaeon 220 行 |

## 3. 全局纪律（引用既有规则，不重复展开）

1. **零信任**：底稿只用 `en/<slug>/index.html`（原始物）；可疑处回源核对；版本钉入任务 JSON（version_pin：pubinfo 日期 + 存档版 + SHA-256）。
2. **术语先行**：新术语先登记 `yi-zhe-shuo-ming.md` 再进正文（fang-fa-lun S2）；正文用词与登记簿 grep 一致。
3. **体例**：中文弯引号、中西文半角空格、禁止 HTML、禁止直角引号——`tools/check_style.py` 0 问题（rules/02 全条款适用）。
4. **脚注键与文件名逐字符一致**：zh 侧 `[^note-N]`、`<slug>.<x>.md`、图片文件名与 yuanwen 完全一致——这是双库对照审校与管线挂链接的基础。
5. **不译区**：引用组人名年份、参考文献非中文条目、LaTeX、URL、代码、DK/古代作品编号。
6. **zh 图片路径裁定**：zh 词条位于 `<letter>/` 子目录，本地化资产在 `yuanwen/assets/<slug>/`，可解析的相对引用只有 `../yuanwen/assets/<slug>/<文件名>`——与 yuanwen 侧的 `../assets/<slug>/`（ADR-0010）**不同**；"双库镜像逐字符一致"指路径的对位结构（同资产、同文件名），不是 URL 字符串相同。**本条为 2026-10-28 新裁定，首个含图词条实跑时请用户确认。**

## 4. zh 词条骨架（可复制）

```markdown
# <SUMMARY 条目文字：中文名 English-name (Authors)>

*首次发表于 YYYY 年 M 月 D 日；YYYY 年 M 月 D 日实质修订。*

<导语段（无标题，摘要式开篇，整体译出）>

## 1 <章节名>

### 1.1 <小节名>

<正文段落。行内引用组原样保留（Author 2012, 366）。>

> 引块：原始文本/残篇译文……（DK 12B1）

![<图注译文>](../yuanwen/assets/<slug>/<imageN.jpg>)

*<图注：Figure N：……（reprinted with permission 时注明来源）。>*

$$<展示公式，LaTeX 逐字符保留>$$

正文脚注引出处[^note-1]。

## 2 <章节名>

## 参考文献

*以下文献从原文照录，不作翻译。*

### <原小节标题保留英文>

* <文献条目逐字符照录（中国文献条目译为中文，ADR-0011）。>

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=<slug>)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/<slug>/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=<slug>&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/<slug>/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

* <条目名译出，说明译出，URL 原样。>

## 相关词条

<中文词条名> | <中文词条名> | <中文词条名>

*（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）*

## 致谢

<致谢段译出；源页面无致谢则整节省略。>
```

**尾部节顺序固定为源的章节序**（实测：参考文献 → 学术工具 → 其他网络资源 → 相关词条 → 致谢，aquinas/alcmaeon 双验）：正文之后依次为 脚注（有则）→ 参考文献 → 学术工具 → 其他网络资源 → 相关词条 → 致谢（有则）；缺失的节整节省略，不造空节。

可选节按源页面实际有无决定——`## 脚注`（37% 词条）：

```markdown
## 脚注

[^note-1]: <脚注译文>（脚注内的公式与引用组按正文同规则处理。）
```

表格与表题的形态（表题译出为表格前的斜体行，表格居中紧凑风格）：

```markdown
*Table 3：<表题译文>*

| <表头> | <表头> |
| :---: | :---: |
| <数据> | <数据> |
```

## 5. 元素 → 门禁对照（每节译完自查）

| 模板元素 | 检查钩子 |
| ---- | ---- |
| 全文体例（引号/空格/禁 HTML） | `tools/check_style.py --docs <路径> --strict` |
| 术语一致性 | `tools/check_terms.py` + 登记簿 grep（fang-fa-lun S3 三校） |
| 学术规范挂钩 | `tools/check_academic.py --docs <路径> --strict` |
| 数学定界符 | `tools/check_math.py <slug>` |
| 图片引用可解析、无悬空 | `check-images.yml`（CI）+ yuanwen 审计脚本 |
| H1 与 SUMMARY 一致 | `tools/check_summary.py`（CI 改写为 SUMMARY 文字） |
| 脚注键与 yuanwen 一致 | 双库对照（键名 diff） |
| 词汇表发布 | `script/glossary_lint.py`（任务收尾） |

## 6. LLM 辅助初译操作规程（ADR-0021，2026-10-31）

规则层条款见 [rules/04](../../rules/04-translation-workflow.md)「LLM 辅助初译协议」；本节是操作细则。

### 6.1 账本文件

`tasks/<首字母>/<slug>.ledger.yaml`，与任务 JSON 同目录并存（存储约定见 `tasks/README.md`；`.json` 寻址的工具不读取账本）：

```yaml
version: 1
slug: abduction
params:            # 批参数显式化（rules/04 ADR-0021），同款数据登记进任务 evidence
  model: "<模型名>"
  temperature: 0.2
  batch_segments: 25
  rate_limit_s: 5
  timeout_s: 60
segments:
  - id: 1
    source: "<英文原文段，逐字符取自 en/ 原始物>"
    step1: "<忠实初译：只译不改，不补不删>"
    step2: "<语言优化：在 step1 基础上消欧化、顺口吻；不引入新信息>"
```

### 6.2 提示词骨架（送审 system prompt）

```text
你是一位专业的中文学术翻译者，为《斯坦福哲学百科全书》翻译词条片段。
## 铁律
1. 仅输出译文，不解释、不加"翻译如下"等额外文本。
2. 保持与输入完全相同的段落数：逐段翻译，不合并、不拆分、不遗漏。
3. markdown 标记（*斜体*、**粗体**、[^note-N]、$…$、> 引块、《》书名号）照原位保留，计数不变。
4. 引用组（Author year, p. X）、书目编号、LaTeX 内容、未经登记者的专有名词保留原文。
5. 必需术语：必须使用下列译名；登记册无译名者保留英文原词待登记。
{{terms}}
## 上下文
词条：《{{title}}》；当前节：{{section}}
```

### 6.3 守恒校验清单（写回前置门，残余≠0 禁止写回）

| 校验 | 判据 | 失败处置 |
| ---- | ---- | ---- |
| 段落数 | 账本 segments 数 = 英文源段落数 | 补段或删段后重校 |
| 逐段身份 | id 连续；source 与 `en/` 原始物逐字符一致 | 回源重取 |
| 标记计数 | `*`/`**`/`[^note-N]`/`$`/`《》` 计数译文与原文守恒（LaTeX 内容除外） | 该段废稿重做 |
| 双版存在 | 每段 step1、step2 均非空且互不相同 | 补反思步 |
| 长度比例 | step2/source 字符比显著偏离常态（如 <0.4 或 >2.0）标旗 | 人工判读漏译/增译/串段 |

长度比例暂为人工判读标旗，机检脚本另行立项（ADR-0021 待裁定①）。

### 6.4 交接

账本 step2 → draft 成稿落入词条 md（骨架与元素映射照本模板 §2–§4）→ 一校以账本为对照底逐节核销（rules/04 MTPE 顺序：先幻觉漏译增译，再术语漂移，后语言）。账本文件随任务入库，evidence 引用其路径与校验输出。

### 6.5 已知陷阱与工具要点（2026-11-04，F–K 批实践沉淀）

**直译流水线（主会话，无子代理）**：①`python script/lq.py init <L> <slug>`（骨架自动含标题段与 oir 段）②通读 yuanwen → 写 `script/build_<slug>.py` 双版翻译 dict（**分批落盘、每批即 commit 账本**，防会话中断丢失；注意 `json.dumps` 把元组转列表，取值须 `s1, s2 = v[0], v[1]`）③组装账本＋守恒自检 → `lq.py check`（HARD=0 方可写回）→ `lq.py compose --write` ④`script/italic_to_bold_cjk.py <md>`（中文强调斜体→粗体）⑤四检（style/math/summary/academic --strict）→ task_ops 八步推进 → pathspec commit。

**compose 陷阱**：

1. SUMMARY 行含转义括号 `\[...\]` 时 `summary_title` 截断 H1——s1 手工补全（kokugaku-school 实例）。
2. 关联词条 NOTE 项（未匹配者）留 s1 人工复核对齐 SUMMARY 登记形；无 SUMMARY 行者保留中文译名，待管线挂链。
3. 脚注键/`$`/`**` 计数守恒是硬门——勿在 step2 加粗源文斜体词（`**` 计数漂移即 HARD）。

**前批账本对齐手术**（hare 先例）：旧账本按“compose 补标题”约定制作会 check 失败——补标题段（kind=body、step1=step2 机械段，SOFT 可过）+OIR 样板段（kind=oir）+ack 段改 kind，id 按文档序重编号。

**斜体→粗体转换**：守卫锚定正则 `(?<!\*)\*([^*
]+?)\*(?!\*)`（`script/italic_to_bold_cjk.py` v3）；裸正则会跨对误配（011 v1-v3 事故重现），账本 compose 是零损失恢复的安全网。豁免行：标题/列表子弹/脚注定义/表格/pubinfo 斜体行；`**` 与相邻汉字间补半角空格。

**curly-quotes 转写撇号**：`Gevia‘` 类转写撇号右邻为空格时不豁免——改词内撇号形（`Gevi'at`，两侧拉丁）过门。

**补充材料**：无独立基线条目（task_ops create 拒），按模板 #19 随主任务走同周期：账本手建（source 程序化取自 yuanwen 保逐段身份）、手工装配。

**SUMMARY 全题化联动**：主行英文为 TOC 片段时回 en/ 查 citation_title 全题化；**必须联动 mu-lu-s.md 同路径行**（holbach 漏联动被 check_mulu_s 抓到）。

**审校实抓先例**（复审对照时优先排查）：Bob **Hale**≠R.M. Hare（均译“黑尔”，需〔Bob Hale〕消歧）；Nachlass 非书名（不用书名号）；源文 off-color 译“变味”非“变色”；no less problematic than convenient 病句型；contemporary=今天/当代（非“当时”）；partially free=部分自由的（非“一部分”）；spiritualism=唯灵论≠唯心论；mistranslation credit X with Y 的方向（把 Y 归于 X）。

**git 纪律**：并行会话活跃时提交一律带 pathspec；重置前先 `git log -2` 确认 HEAD 无他人新提交；共享登记册（ren-ming-biao 等）被他会占用时，用 `git apply --cached` 只暂存己方 hunk。

**现制 References（引用注释）要点（2026-11-05，18thGerman-preKant 首例）**：①2026 起新修订页为「节说明 + 文末 `[^key]:` 定义区」形态，lq.py `refs_kind=modern` 分支自动识别（保留源节标题、转换器契约注记、空子节标题；定义随 References 节照录，非中文条目不译，`[^unless-nd]`/`[^following-nd]` 伪脚注同照录）；②孤立定义（文献表推荐文献未被正文引用）与注记字面 `[^key]` 为源文同构，机检现制豁免覆盖，勿当事故修；③SUMMARY 标题疑衍字时对 `en/<slug>/index.html` citation_title 实证，修 SUMMARY 必联动 mu-lu-s 同路径行；④账本填充器严禁「`- id: N` 起非贪婪跨段匹配 TBD」的正则（会吞掉中间段骨架造成错位 14 段），须按 ` - id: ` 块级切分替换——错位会被写回门脚注键守恒 HARD 拦下，回滚重填即可。

## 7. 演示与修订

* 本模板 v1.0 由 alcmaeon（一校通过）验证主体骨架；**spacetime-holearg（空穴论证）为四要素演示件**（2026-10-28，任务 state=s3_checked）：图片（`../yuanwen/assets/` 路径裁定**首跑确认**）、脚注（note-1..8 含跨文件孤儿豁免）、数学（`$$…$$` 配对 0 缺失）、表格元素中图/脚注/数学三类已实跑验证，表格类元素仍待首个含表词条确认。演示发现的问题按 rules/04"演示与纠偏循环"回修本模板。
* 修订记录追加于此表（同 fang-fa-lun S10 纪律，git 历史为准）：

| 版本 | 日期 | 要点 |
| ---- | ---- | ---- |
| v1.0 | 2026-10-28 | 首版：结构总览（1878 条实测）+ 22 项元素映射 + 骨架 + 门禁对照；zh 图片路径等五项裁定待首跑确认 |
| v1.1 | 2026-10-28 | 四要素演示件 spacetime-holearg 实跑：zh 图片路径裁定获首跑确认；跨文件脚注（补充材料引用主文 notes）定例——主文保留定义，门禁 orphan-def 跨文件豁免（tools/check_academic.py） |
| v1.2 | 2026-10-31 | 增 §6 LLM 辅助初译操作规程（ADR-0021）：段落账本、反思两步强制（用户裁定）、守恒校验、术语与上下文注入；原 §6 演示与修订顺移为 §7 |
| v1.3 | 2026-11-04 | 学术工具三行改四行（用户裁定「不计成本解决待裁定事项」）：补「预览本词条的 PDF 版本」行——rules/07 完整性原则优先于 v1.0 三行省略；bullet 形态对齐 36 在先成例措辞；70 存量词条批量补齐（script/rz_acat_pdf.py 幂等插入器，URL 逐条 slug 校验），lq.py compose 同步改四行；表格形态存量（31+4）四项齐备合规不改形，形态归一另行立案 |
| v1.4 | 2026-11-05 | 现制 References（引用注释）首例落地（18thGerman-preKant，2026-07 新修订页）：lq.py 扩展 refs_kind=modern 分支（保留源节标题+转换器契约注记+空子节标题+文末 `[^key]:` 定义随 References 节照录），向后兼容旧制；伪脚注 `[^unless-nd]`/`[^following-nd]`（作者说明文字，转换器合成键）随文献定义区照录不译，s1 复核裁定留痕；§6.5 增补：SUMMARY 标题衍字须对 en/ citation_title 实证修复并联动 mu-lu-s（本例「18 18th」系 d765f061 批量修复引入，commit d16d6863 修正）；账本填充器禁用跨段非贪婪正则（批2 错位 14 段事故，写回门 HARD 拦截，块级重写修复） |
