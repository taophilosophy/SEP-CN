# 上游更新派工单（2026-11-15 实际比较产出）

来源：drift_scan 真漂移 72 条 → compare.py 节级变更 39 条（含 compare.py 导言修复后新检出 29 条）→ 实际比较原始行级归类。
0045 分歧账勘误在账者处理时先用 `divergence.py carry` 随迁，再按变更段作业。

## A. 已译词条——9 件，分两类处置

| slug | 变更文件 | 勘误在账 | 原始 diff 概况 |
| ---- | ---- | ---- | ---- |
| academic-freedom | `compare/academic-freedom.json` | 是 | 属性/链接级（规范化文本等价）×8、正文/书名文字×5、结构增删×1 |
| behaviorism | `compare/behaviorism.json` | 否 | 正文/书名文字×2 |
| closure-epistemic | `compare/closure-epistemic.json` | 否 | 正文/书名文字×146、属性/链接级（规范化文本等价）×8、页框/站点套版（正文区外）×4、结构增删×2 |
| emotion-Christian-tradition | `compare/emotion-Christian-tradition.json` | 是 | 属性/链接级（规范化文本等价）×46、正文/书名文字×25、页框/站点套版（正文区外）×5、结构增删×3 |
| genetics | `compare/genetics.json` | 否 | 页框/站点套版（正文区外）×5、正文/书名文字×3 |
| it-moral-values | `compare/it-moral-values.json` | 否 | 文献与工具区文字×2、正文/书名文字×1、页框/站点套版（正文区外）×1 |
| kant-leibniz | `compare/kant-leibniz.json` | 否 | 属性/链接级（规范化文本等价）×42、正文/书名文字×23、页框/站点套版（正文区外）×10 |
| logic-provability | `compare/logic-provability.json` | 是 | 页框/站点套版（正文区外）×6、正文/书名文字×1 |
| saadya | `compare/saadya.json` | 否 | 正文/书名文字×66、页框/站点套版（正文区外）×12、属性/链接级（规范化文本等价）×12、结构增删×5、文献与工具区文字×2 |

### A1. state=done——5 件，已按 ADR-0050 置空重译（2026-11-15 用户裁定，取代本单原「变更段」建议）

academic-freedom、closure-epistemic、genetics、it-moral-values、saadya——已 reopen→clear（正文仅留 H1，state=cleared），按新源全量重译；`compare/<slug>.json` 降级为审读辅助。

academic-freedom、closure-epistemic、genetics、it-moral-values、saadya

### A2. state=s2.5_checked（ADR-0043 回退后在途）——4 件

behaviorism、emotion-Christian-tradition、kant-leibniz、logic-provability——
~~按管线契约挂现有流水~~ **2026-11-15 ADR-0051 已改道**：`reopen --upstream-sync --clear` 打回置空重译（R3 四闸），与 A1 同轨；正文已置空仅留 H1。

## B. 存根/未译词条（节级变更 30 件）

翻译铺到该词条时自动以最新 upstream 为底稿，无需 update 任务；清单与变更文件已在 `compare/`。

## C. 仅链接/页框/属性级（不建任务）

其余 32 件 sha 漂移但零节级文字变更（死链修整、页框年份、属性版式），登记备查不动译文。

## D. 实际比较归类总览（72 件全部 hunk）

| 归类 | hunk 数 |
| ---- | ---- |
| 正文/书名文字 | 1637 |
| 属性/链接级（规范化文本等价） | 847 |
| 页框/站点套版（正文区外） | 258 |
| 结构增删 | 82 |
| 文献与工具区文字 | 4 |

## E. 待裁定

1. A 表 9 件 done 词条采用 rework-open（保持 done、只走变更段）还是 reopen（重走）——先例与 005 派工规则支持前者，请裁定；
2. 9 件中 emotion-Christian-tradition、logic-provability、academic-freedom、incompatibilism-theories… 勘误在账者随迁次序。

> **⚠ 2026-11-15 同步后升级**：closure-epistemic 与 saadya 经全量回源核对发现被上游**同 slug 换血重发**（新作者 Alspector-Kelly／Hegedus，首发 2026-11-04／11-12）——中文译文对应旧文本已整体失效，属**重译级**（retranslate）而非 update；kant-leibniz 为正常实质修订（2026-11-14）。三件 zh 题注已机械对齐新 baseline；正文重译/更新由 reopen 后的任务承接。

