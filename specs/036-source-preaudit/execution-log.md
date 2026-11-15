# specs/036 执行日志

## 2026-11-15 机制落地（本轮）

* ADR-0052 accepted；`task_ops.py` s0 状态三表＋`_source_gate`＋`source-audit` 补课子命令＋s3 历史门禁，单测 21/21 绿（新增 4 条：draft 要求 s0、s3 要求 s0 历史、补课边界×2）。
* 新工具 `tools/en_source_audit.py`（离线 HTML 本体审计，stdlib）：页面真实性/截断、typo 启发式（词内数字等号/重复词/标点串/数字替换字母/pp. 缺空格，DOI 与混淆邮箱掩蔽、全大写缩写豁免）、页内锚点（硬）、站内词条链接对 catalog（硬）、包内资产存在性（硬）、公式定界符与花括号（硬）、`\unicode` 族告警、表格无行/配平（硬）、嵌套表信息、note/fn 孤儿告警、空段落/标题跳档告警；`--net` 外链活检（缓存 state/link_cache.json、≥5s 间隔、退避）。单测 7/7 绿。
* 试金石 3 条（logic-provability／bauer／quine-nf）硬错 0；真候选 1 处（logic-provability 书目 `pp.61–70` 缺空格——en-errata #12 同类漏网，待裁定表处置）；bauer h2→h4 跳档告警属 SEP 原生结构，登记豁免。
* 文档同步：rules/04（状态机表＋源审计前置环节节＋s2.5 两轴收缩＋重译前置）、rules/09 P0.5 行、tasks/README、contracts/cli.md、fan-yi-mu-ban §6.5。
* 存量盘点：done 219／在途 s2.5_checked 194（补课集合 413）／pending 621／cleared 162（走管线自然入口）。
* 待办：批次启动待批；`--net` 全库活检待批；pending/cleared 件自 ADR-0052 起在 `advance s0` 强制过机检。

## 2026-11-15 首件补课（z 字头）与工具回修

* 首件 s0 补课启动（zabarella／回炉件）即拦：`en_source_audit` 硬错 2（entry_link_bad）——SEP 官方注释停用链接（`<!--<a href="../latin-averroism/">-->`）被链接抽取当作活链。工具缺陷归因：`_check_links` 跑在原始 HTML 上未剥注释，与 `_text_nodes`（typo 轴已剥）口径不一致；波及面 grep 实测 188 件 en/ 含注释锚点，s0 门对这类件不可通过，回炉池（413）整体受阻。
* 上游实证（礼貌抓取，间隔 6s，代理 7890）：`latin-averroism`、`neoplatonism-renaissance` 均 404——SEP 因目标词条未发布而注释停用，catalog 未过期（fetch_catalog 不解决）。旧 s1 凭证（2026-11-08）同判定："系 SEP 官方注释停用链接，无 SUMMARY 行"。
* 处置（specs/030 §4.7 同类回修先例）：`_check_links` 入口剥注释（与 _text_nodes 同用 COMMENT_RE），注释内锚点不作链接核对；单测新增 `test_commented_out_link_not_audited`（注释停用不报）＋既有 `test_entry_link_catalog`（活链仍拦）双向锁定，8/8 绿。
* 试金石：前 60 字头词条（60/60 含注释停用链接）修复后 entry_link_bad 对注释锚点零复发；活链核对能力不变。

## 2026-11-15 工具回修二（zombies 先例）

* zombies s0 补课即拦 2 硬错，均定性工具误报：①error_page——MARKERS 全页扫命中书目论文题 `'Access Denied to Zombies,'`（Piccinini 2017）；②entry_link_bad——源 href `../Russellian-monism/` 对目录键 `russellian-monism` 大小写敏感误缺。
* 回修：`_check_page` 错误/风控标记只识别页头区（前 4000 字符，title＋导航；真错误页体小且标记前置）；`_check_links` 目录比对小写归一（slug 语义不随 href 大小写漂移）。
* 单测 10/10 绿（新增 error_page 仅页头、大小写不敏感两用例，反向拦截均有断言）；zombies/zeno-elea/zabarella 复跑硬错 0。

* check_terms --docs 定点噪点回修：`s/scholem 首译` 型首现按斜杠拆分出的单字母碎片（s/z 等字头目录前缀）以 `endswith('s.md')` 误配任意 s 结尾文档（zombies 119 条噪点淹没真告警）；修法=单字母碎片不入匹配集，单测 17/17 绿（新增前缀不误配用例），zombies 定点 119→11（全为可定性真案）。
