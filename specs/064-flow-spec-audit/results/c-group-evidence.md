# 064 组 C 执行证据（2026-11-27）

- 组：**c**（W1 第一梯队；c1 habermas → c2 logic-preference → c3 environmental-aesthetics）
- start tag：`batch/064-c-start` → `14d1d7a55`（已推送）
- end tag：待打（C 组收口后）
- 本轮完成：**T132（habermas tr-02 样章）**；T133 全量未启动
- 门禁：`python tools/check_all.py` **23/23 全绿**
- 授权：C 组由主代理单干；本轮未调用子代理（ADR-0034）

## 0 清理

`python tools/clean.py --go` 删除 **90 项**未跟踪缓存与临时物（`.screenshots`、各 `__pycache__`、`specs/*/results/*.log`、`.vitepress/cache|dist` 等）；随后 `clean.py --check` 报“未发现本地垃圾”，退出 0；`git status` 无删除跟踪文件。

## 1 T132 执行内容

| 项 | 结果 |
| ---- | ---- |
| 前置 | T130 人工定性完成（hard=0／warn=5；5 候选 4 误报、1 真 typo，用户 2026-11-27 批准） |
| 任务状态 | `cleared` → `ex-04_checked` → `tr-02_checked`（`task_ops.py show habermas`） |
| 项目规格 | 补齐 `project_spec` 六项（ISO 11669:2024，ADR-0086） |
| 译后编辑 | `translation_mode: llm-pe`；`pe.level: full`；`pe.system: DeepSeek-V4.1-Flash`；evidence 明写“译后编辑／PE”（ADR-0084 D2=B） |
| 账本 | `tasks/h/habermas.ledger.yaml`：**16 段**，source 逐段回源 `yuanwen/h/habermas.md`（脚本逐段比对全等）；每段 step1／step2 双版且互不相同 |
| 样章 | `h/habermas.md`：§1–§2 选段，约 **2,350 汉字**（含引文/脚注总字符约 4,660） |
| 术语 | 使用登记形：于尔根·哈贝马斯、公共领域、法兰克福学派、社会研究所、交往行为、《交往行为理论》、商谈伦理、合理重构 |
| 标记 | 英文书名/报刊名保留斜体；中文强调按 `rules/02` 改加粗并补两侧空格；脚注键 6 处、定义 4 条（müller／specter／negt／landes） |
| 体例 | `check_style.py h/habermas.md` → 0 issue；`check_quotes.py` → 0 违例 |
| 术语机检 | `check_terms.py --docs h/habermas.md` → 硬错误 0（10 处首现告警属样章未覆盖人名，T133 全量后再核） |

## 2 H1／目录同步（术语一致性）

`ren-ming-biao.md` 登记形为 **于尔根·哈贝马斯**；原 `SUMMARY.md`、`mu-lu-s.md`、`baseline/mulu-map.json` 与 H1 仍作“尤尔根”。已统一为：

`于尔根·哈贝马斯 Jürgen Habermas (James Gordon Finlayson and Dafydd Huw Rees)`

同步文件：`SUMMARY.md`、`mu-lu-s.md`、`baseline/mulu-map.json`、`yuanwen/SUMMARY-en.md`（`gen_en_summary.py` 重生成）。`check_all` 的 SUMMARY H1、分类目录、目录四方重放三门均绿。

## 3 已知缺口（有意留到 T133／后续）

1. `check_pairs.py h/habermas.md` 报“尾节缺失：参考文献、学术工具、其他网络资源、相关词条”——样章只含 §1–§2，尾节随 T133 全量补齐。
2. `errata-apply` 报两条勘误未承载（`des Ritus”,,`、`Theory on Empitical Research`）——两条位于书目 chapter 3／chapter 9，不在 §1–§2 样章内；T133 译到相应书目后按 ADR-0065 落译注／译者注释。
3. `check_terms` 的 10 处“正文缺登记译法”告警，均为样章尚未出现的人名（Alexy、Apel、Benhabib 等），T133 全量后复跑。
4. 样章未含脚注以外的参考文献、图表、公式；这些构件的样章验证放在 T133 各批。

## 4 状态与下一步

| 项 | 结果 |
| ---- | ---- |
| T132 | **已完成**；样章待用户验收 |
| T133 | 未启动；建议按 4–6 批 checkpoint，先 §1 余节，再 §2–§9 |
| T134 起 | 未启动 |
| `batch/064-c-end` | 待打（C 组 22 步全部收口后） |
| 未改 | `en/`、`yuanwen/` 原文、译文其他词条、`baseline/en-errata`（本轮未新增） |
