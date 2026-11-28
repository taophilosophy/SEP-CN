# T170 验收证据：目标态与标准 crosswalk（CP-S14-01–05）

- 日期：2026-11-28
- 范围：T282–T286；T170 为容器，不整体勾选
- 主文件：`results/target-workflow.md` §1、§1.1、§2、§4、§17

## 1 逐项验收

| 任务 | 检查点 | 落点 | 验收结果 | 结论 |
| ---- | ---- | ---- | ---- | ---- |
| T282 | CP-S14-01 | `target-workflow.md` §1 | 13 项规范均有版本／日期、状态、官方来源；现行／在研／草案分列；表后有状态口径与登记缺口说明 | 通过 |
| T283 | CP-S14-02 | `target-workflow.md` §1.1 | 31 行条款锚点；17100 5.3（5.3.1–5.3.6）、18587 4／6、5060 5.4–5.8／6.3、11669 4.3／5.2／5.3、CY/T 123 4–6、CY/T 266 5–6 均有落点与证据 | 通过 |
| T284 | CP-S14-03 | `target-workflow.md` §2 | 13 行差距；每行有“现状证据（可复核）”与“目标判据（可验收）”；无空泛“加强”；末尾补标准登记缺口与标准锚点漂移 | 通过 |
| T285 | CP-S14-04 | `target-workflow.md` §4 | P0–P7 八阶段；每阶段有角色、产物、G-* 闸门；22 节点全部映射且不重编号 | 通过 |
| T286 | CP-S14-05 | `target-workflow.md` §17 | 7.1 权利线、AI 披露、不另立 065 三项均只记录裁定与禁止边界，不设计 | 通过 |

## 2 外部核证（检索日 2026-11-28）

| 标准 | 核证内容 | 来源 |
| ---- | ---- | ---- |
| ISO 17100:2015 | 目录：5.3 Translation process；5.3.1 Translation、5.3.2 Check、5.3.3 Revision、5.3.4 Review、5.3.5 Proofreading、5.3.6 Final verification and release；3.1.3–3.1.7 能力条款；6.1–6.2 反馈与结项 | ISO OBP；AFNOR 全文 PDF（`password-europe.com/.../ISO-17100-2015.pdf`） |
| ISO 17100:2015 5.3.3 | “The reviser, who shall be a person other than the translator…” | 上表 PDF 与公开论文引文互证 |
| ISO 18587:2017 | 目录：4 Post-editing process（4.1–4.4）；5 Competences；6 Requirements of full post-editing | iTeh 预览 PDF（`cdn.standards.iteh.ai/samples/62970/...`） |
| ISO 5060:2024 | 目录：5.4 Error typology、5.5 Error type weights、5.6 Severity levels、5.7 Critical errors、5.8 Counting repeated errors；6.3 Sampling、6.4 Scorecard、6.5 Quality rating；7.1–7.2 | iTeh 预览 PDF（`cdn.standards.iteh.ai/samples/80701/...`）；BSI 预览 PDF |
| ISO 11669:2024 | 目录：4.3 Translation project parameters；5.2 Initial needs analysis；5.3 Risk assessment | ANSI／ISO 预览 PDF（`webstore.ansi.org/preview-pages/ISO/preview_ISO+11669-2024.pdf`） |
| CY/T 123-2015 | 条款落点沿用 `rules/10` §10.1（4.1.1–4.1.2、4.4.3、4.4.5、5.2.4–5.2.5、5.5.3–5.5.4、5.6–5.8、5.9.2、5.10、5.14、6.1–6.2） | `rules/10-standards-clauses.md` |
| CY/T 266-2023 | 目录与正文：5.1 文字、图片差错；5.2 符号差错；5.3 格式差错；6.1 公式；6.2 万分比；2023-06-16 发布、2023-08-01 实施 | 标准全文 PDF（`qxb-img-osscache.qixin.com/standards/df60e48b...pdf`） |

## 3 复算与边界

- 22 节点标识未改；本任务未执行翻译、未改 `en/`／`html/`／译文、未改工具与任务状态。
- 任务书新增 5 个原子编号（T282–T286），编号总数 198→203；T170 容器保持未勾。
- 未入 `rules/standards.json` 的 ISO/IEC 42001／23894 与 ACLS 已在 §2 末行登记为缺口，回写归 T175；本任务不代行登记。
- 发现既有锚点漂移：`specs/041` 引“ISO 17100 §5.5.4”，`specs/063` §1.3 把 §5.3 当“源文本接受性检查”；`rules/09` 一处已由 T171 改为 5.3.3，其余两处归 T175。
- 未实现 `project_spec`、TBX、评分卡、归档包与 AI 风险登记；分别归 T171–T174。

## 4 结论

CP-S14-01–05 全部通过，T282–T286 可勾选；T170 容器不勾，完成由子项派生。
