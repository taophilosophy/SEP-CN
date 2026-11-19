# 查无全量联网查证·试金石批裁定报告 2026-11-20

口径：ADR-0012 档②③（权威译本/学术出版通行译法/学界惯例/权威工具书）；禁维基；凭证只录实证（不造相符假象）；命中须语境正确（同形异义一律不采）。会话 TL-web-20261120，用户指令“联网逐个查证”。

## 通道与管线

* **通道探测**：Crossref（中文分词糊，弃）；OpenAlex（CJK 标题检索可用，投产为脚本道档③）；zgbk（mtoken 签名未破，待浏览器道）；ncpssd（机制在案，待浏览器道）。
* **管线**：`script/tmp/webcheck_build_queue.py`（查无 8,838−已有凭证 2＝队列 8,836，术语先行）→ `webcheck_fetch.py`（OpenAlex title.search＋精确包含过滤，≥5s 节奏，断点/幂等重跑/批刷盘）→ 逐词人工裁定（verdict JSON：KEEP/ADJUST/NOSOURCE/QUARANTINE/SKIP）→ `webcheck_merge.py`（落 `queries/web-authority/` 凭证＋挂起清单）→ term_audit 四态翻转。
* **试金石批执行**：抓 79 词 ok（60 词目标＋修补轮，429 前截止）；有命中 28；全量逐词裁定。

## 裁定结果

| 判定 | 件数 | 处置 |
| ---- | ---- | ---- |
| KEEP（凭证落库，cn=现译） | 16 | `queries/web-authority/`（140→156），audit 四态翻转 查无→一致 |
| ADJUST（改读） | 0 | — |
| NOSOURCE（本道无实证） | 24+51 无命中 | 仅记台账，他道（zgbk/ncpssd）仍可查 |
| SKIP（留待他道/定向核） | 8 | 含 4 例改读嫌疑（anarchic hand 异己手、ancilla 辅助比特、Anglican Catholic Church 安立甘公教会、a fortiori argument 译法存疑） |

KEEP 明细（16）：ancien régime 旧制度、a priori knowledge 先天知识、Abhidhamma 阿毗达磨、Abhidharmakośa 阿毗达磨俱舍论、abhūtaparikalpa 虚妄分别、Abstract Right 抽象法、abstraction theory 抽象理论、abilities 能力、acknowledgement (Anerkennung) 承认、advance directives 预先指示、aesthetic attitude 审美态度、aesthetic consciousness 审美意识、aesthetic emotion 审美情感、aesthetic idea 审美理念、aesthetic state of mind 审美心境、aestheticism 审美主义。

## 校准（吞吐与道口经济学）

* **四态翻转验证**：一致 1,984→2,000（+16）、查无 8,838→8,822（−16）、不一致不变——全链闭环。
* **OpenAlex 脚本道**：实测 ~6.5s/词（5s 节奏＋抓取）；KEEP 产出率 **20%**（28 命中中 16 证得实，79 抓词中 20%）；**硬顶＝当日免费配额（IP 共享，约数百请求即 429，本日已耗尽）**——升配需注册免费 API key（$1/日，邮箱注册，待用户授权）；不升配则本道日产能 ~200 词。
* **噪声画像**：假命中三族——泛义散文/教学期刊同形（回忆/注意/能力）、跨语言碰撞（日文浸透/平行角）、子串碰撞（所缘缘/现实论析）；真命中集中在：佛典古译（阿毗达磨系）、审美美学词族（审美X 全谱命中）、医卫/法学术语（预先指示）、黑格尔/康德主流术语（抽象法/先天知识）。
* **结构性结论**：OpenAlex 单道承不起 8,838 全量（按 20% KEEP 产率＋配额硬顶）；**主承道应为 zgbk（档②工具书条目直证）＋ ncpssd（档③期刊标题，机制在案）浏览器道**——待浏览器工具通道恢复后逐段建设；OpenAlex 作补充道（配额窗口内跑）。
* **节奏红线**：≥5s/请求（本战役自有参数）；429 即停日，不做夜间重试堆栈。

## 后续

1. zgbk/ncpssd 浏览器道建设（本日 DeferredToolCall 校验间歇故障未竟，下段续）；
2. OpenAlex API key 授权决策（升配 $1/日）提请用户；
3. 队列断点 script/tmp/webcheck-state.json（next=72，batch=6）；挂起清单 webcheck-nosource.json 本批未启用（NOSOURCE 不入挂起，等三道合查后定）；
4. SKIP 的 4 例改读嫌疑按 015 语体复核战役同型流程定向核。
