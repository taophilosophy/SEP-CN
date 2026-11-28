# T001 候选池复算（2026-11-28）

## 方法

- 遍历 `en/` 全部 `*.md`，取行首以 `#` 起始且标题文本以 `Proof` 或 `证明` 开头的首条命中（每文件一条）；结果落 `proof-candidates.tsv`（列：file／entry／line／heading／kind／verdict）。
- 展示公式口径：文件全文含 `$$` 即计入。
- 归属：补充页文件名首段即父词条 slug（如 `common-knowledge.proof2-04.md` → `common-knowledge`）。

## 结果

| 指标 | 数值 |
| ---- | ---- |
| `en/` 显式 Proof 节命中文件 | 30 |
| 其中：补充证明页（候选） | 28 |
| 其中：题名误命中（正条目 H1） | 2（`proof-theory`、`proof-theoretic-semantics`） |
| 父词条（候选归属） | 5：bayes-theorem、common-knowledge、frege-theorem、infinity、kochen-specker |
| 含展示公式（`$$`）文件 | 416 |

## 与 spec §2.6 口径对照

- 2026-11-28 评估口径为“显式 Proof 节 30 件／含展示公式 416 件”；本次复算数值一致（30／416）。
- 差异说明：30 件中含 2 件题名误命中（正条目标题以 Proof 开头），**真实形式证明候选为 28 件**，集中于 5 个词条的补充页；评估口径的 30 作为“命中上限”仍成立，编目对接按 28 件候选执行。
- 分布：bayes-theorem 1 件（单文件 2 个 Proof Sketch 节）、common-knowledge 13 件、frege-theorem 10 件、infinity 1 件（单文件多定理）、kochen-specker 3 件。

## 复算方式

本文件方法与 `proof-candidates.tsv` 可由任意会话以同一规则重放；不依赖 git 快照与外部网络。
