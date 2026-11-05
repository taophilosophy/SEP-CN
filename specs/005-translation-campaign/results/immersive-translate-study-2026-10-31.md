# 沉浸式翻译插件专业翻译流程研究（2026-10-31）

**效力**：研究存档，不具约束力；采纳结论以 [ADR-0021](../../../rules/adr/0021-LLM辅助初译协议.md) 为准。
**方法**：官方文档四页实测（prompts／advanced／usage／features/webpage），对照本项目 rules/04（三审三校＋ADR-0020 MTPE 验收顺序）、rules/05（批量改写五纪律）、009 归一性深读实锤。

## 一、插件流程拆解（六环节）

| 环节 | 做法 |
| --- | --- |
| 1. 范围圈定 | `selectors`/`excludeSelectors` 只译正文；`stayOriginalTags` 保留不译；`blockMinTextCount/WordCount` 过短不译 |
| 2. 段落级批处理 | 翻译单位是**段落**；多段合并请求（约 25 段/次、1800 字符/次），限流 `limit`、超时 `requestTimeout` 显式参数 |
| 3. 上下文与术语注入 | 提示词注入 `{{title_prompt}}`（标题）、`{{summary_prompt}}`（全文摘要，Pro 服务端提取）、`{{terms_prompt}}`（"**必需术语：翻译时必须使用**；source==target 则保留原文"） |
| 4. 提示词协议（防幻觉） | 五条铁律：仅输出译文／**段落数与格式完全一致**／标签位置保持／专有名词代码保留原文／无额外文本；进阶用 **id-YAML 协议**（`- id: n`＋source 字段，译文按 id 回写）；分隔符选罕见的 `%%`；temperature 0.1–0.2 |
| 5. 质量守恒校验 | 对比响应与请求的 **token 数量比例**，异常判无效并切备用方案；非翻译任务才可 `strictPrompt` 跳过 |
| 6. 双语呈现 | 译文紧随原文、26 种弱化样式、对照/纯译文一键切换、悬停单段翻译、PDF Pro 逐段对齐 |

另有官方进阶示例**反思式翻译**：一次请求两步，`step1` 初译 → `step2` 优化，**双版保留输出**。

## 二、提取映射（已采纳，ADR-0021）

| 它的做法 | 本仓库对应 | 落点 |
| --- | --- | --- |
| id-YAML 段落账本 | rules/05 批量改写纪律（逐行身份追踪、残余≠0 禁止写回）同构 | rules/04 新节＋模板 §6：`tasks/<letter>/<slug>.ledger.yaml` |
| 反思式两步双版留档 | rules/04 MTPE 验收顺序（先忠实后流畅）的工业印证 | **强制**（用户 2026-10-31 裁定）：step2 为成稿对象，step1 为一校对照底 |
| 格式标记位置保持（html_only 条款） | 009 实锤：em 空格粘连、星号未转义、em-lang 超额包裹 | 标记守恒条款＋守恒校验清单 |
| 术语强制注入（terms_prompt） | 单一事实源 yi-zhe-shuo-ming.md／ren-ming-biao.md；先登记后使用 | 提示词注入登记册摘录；模型自提取术语只作候选 |
| 上下文注入（标题＋摘要） | SEP 词条有精确标题＋节结构 | 注入标题与节标题；**不采**全文摘要（长词条失真） |
| token 比例/长度守恒质检 | 现有门禁无此项 | 暂为人工判读标旗；机检脚本待裁定① |
| 批参数显式化 | 抓取礼貌（≥5s、退避）已有，翻译侧缺 | 批尺寸/限流/超时/温度登记进 evidence |
| 双语逐段对照 | 本地 VitePress 双语阅读站 | 待裁定②（审校视图排期） |
| 不译范围显式化 | 任务方向声明已含边界 | 模板 §3.5 不译区既有 |

## 三、不采纳清单（与宪法冲突）

1. **即译即用、无审校链**——插件面向即时阅读；三审三校不可省（流程先行、体例即契约）。
2. **第三方黑盒摘要/术语提取直接可用**（Pro 的 `imt_theme`/`imt_terms`）——违反零信任与可回溯；只借注入形态，内容来源必须本地可控。
3. **降级服务链自动切换**——翻译不走服务链，无对应需求。
4. **`strictPrompt` 跳过质检**——反面教材：质检不可设开关绕过；豁免必须逐条留痕。
5. **DOM 注入/译文样式主题**——产物形态不同（md 文件），仅双语站渲染可参考其弱化样式思想。

## 四、裁定记录

* 2026-10-31 用户裁定：「复核后批准合入流程和软件工程理论，立刻落地。反思必须强制」→ 合入执行（ADR-0021）；反思式两步确认为**强制**条款。
* 未决（待裁定）：①长度守恒 QA 脚本立项；②双语站逐段对照审校视图排期。

## 五、来源

* [AI Prompt 配置指南](https://immersivetranslate.com/zh-Hans/docs/prompts/)
* [高级自定义选项](https://immersivetranslate.com/zh-Hans/docs/advanced/)
* [快速开始](https://immersivetranslate.com/zh-Hans/docs/usage/)
* [网页翻译](https://immersivetranslate.com/zh-Hans/docs/features/webpage/)
* [官网](https://immersivetranslate.com/zh-Hans/home/)
