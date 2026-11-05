# specs/011 全量翻译复核战役（复核既有所有翻译 + 术语表同步 + 人名表反向校对）

日期：2026-11-02。用户指令：「复核既有所有翻译，并且同步术语表，人名表再反向校对，不使用子代理。」（重复=催办，主会话直做。）

## 目标

对库内全部已有实质中文译文的词条（PROGRESS 口径外实测 152 条：A41/B14/C26/D14/E8/F1/G1/H16/I23/J6/K1/S1，含 48 条在途中间态的已译正文）做三层复核，并落发现清单与修复：

1. **机械层**：现成门禁逐条过——check_academic --strict、check_style、check_math、check_render_artifacts、check_terms 定点；在途词条尾节缺失（biblio/scholar-tools-missing）属预期态，豁免清单化，不修正文。
2. **术语同步层**：译文术语用法 ↔ yi-zhe-shuo-ming.md 双向对账。译文先行使用未登记术语 → 登记册补行（先登记后使用，宪法 III）；登记册译名与译文实际用词不一致 → 凭证优先裁定后修弱势方。
3. **人名反向校对层**：从译文反查 ren-ming-biao.md——①「中文人名（English Name）」括注模式抽取比对；②纯中文译名人名回查登记册有无登记；③登记册在册人名在译文中的实际用字一致；④括注体例（古典汉译+首现括注；现代学者保留英文）执行情况。

## 非目标

* 不重译全文（硬伤级误译定点修复除外，逐处留 evidence）。
* 不动英文源 en/、yuanwen/ 镜像（009 归一性复核已收官，移交项另行走镜像流程）。
* 不翻译新词条、不推进任务状态机（复核不改变词条翻译状态）。
* 不使用子代理（用户裁定 2026-11-02，主会话直做）。

## 既有基线（开工时）

* 门禁 7 项中 3 项红：学术规范 529 处（大头=在途词条尾节未拼）、术语硬错 3、分类目录 1 → **开工前已全部修复提交**（71e104ff：Williams 冲突修弱势方 39 处、登记册/人名表重复行去重、james-ward 穆勒目录瓦德→沃德）。
* 工作区 486 文件未提交 → 已收口：26 条 s3_checked/done 逐条提交 + 48 条在途快照 641faf13。
* 已知移交池（009）：T-math-macro-closure、T-supplement-drop、em-lang 挂起 69 术语、R3/R4 人名挂键家族——本战役人名反向校对吸收其发现清单，不重复移交流程。

## 流程与验收

1. 机械层全跑 → 差异清单 results/mechanical-scan.jsonl，逐条处置（修/豁免/移交）。
2. 术语同步 → results/term-sync.jsonl；check_terms 硬错误 0 且词汇表滞后清零为收口判据。
3. 人名反向 → results/person-audit.jsonl；登记缺口补登记、用字偏差修弱势方；gen_change_ledger 类批量改写走 rules/05 五纪律（前置门/幂等/逐行追踪/基线还原/探针）。
4. 人工深读 → results/manual-deepread.jsonl，按字母批滚动，每条落 verdict 与 evidence；本期做多少交接多少（session-handoff 补卡）。
5. 收口：check_all 7 项绿（豁免清单除外）+ 提交 + PROGRESS/execution-log 更新。

## 裁定记录

* 2026-11-02 用户指令即裁定：复核范围=全部既有译文（非抽样）；术语表同步与人名反向校对并列主线；不使用子代理。
* 修复方向裁定沿 ADR-0012 凭证优先 + 修弱势方：登记册（yi-zhe-shuo-ming.md / ren-ming-biao.md）为单一事实源，词汇表（qian-yan/ci-hui-biao.md）与存量译文为弱势方。
