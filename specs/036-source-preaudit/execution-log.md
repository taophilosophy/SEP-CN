# specs/036 执行日志

## 2026-11-15 机制落地（本轮）

* ADR-0052 accepted；`task_ops.py` s0 状态三表＋`_source_gate`＋`source-audit` 补课子命令＋s3 历史门禁，单测 21/21 绿（新增 4 条：draft 要求 s0、s3 要求 s0 历史、补课边界×2）。
* 新工具 `tools/en_source_audit.py`（离线 HTML 本体审计，stdlib）：页面真实性/截断、typo 启发式（词内数字等号/重复词/标点串/数字替换字母/pp. 缺空格，DOI 与混淆邮箱掩蔽、全大写缩写豁免）、页内锚点（硬）、站内词条链接对 catalog（硬）、包内资产存在性（硬）、公式定界符与花括号（硬）、`\unicode` 族告警、表格无行/配平（硬）、嵌套表信息、note/fn 孤儿告警、空段落/标题跳档告警；`--net` 外链活检（缓存 state/link_cache.json、≥5s 间隔、退避）。单测 7/7 绿。
* 试金石 3 条（logic-provability／bauer／quine-nf）硬错 0；真候选 1 处（logic-provability 书目 `pp.61–70` 缺空格——en-errata #12 同类漏网，待裁定表处置）；bauer h2→h4 跳档告警属 SEP 原生结构，登记豁免。
* 文档同步：rules/04（状态机表＋源审计前置环节节＋s2.5 两轴收缩＋重译前置）、rules/09 P0.5 行、tasks/README、contracts/cli.md、fan-yi-mu-ban §6.5。
* 存量盘点：done 219／在途 s2.5_checked 194（补课集合 413）／pending 621／cleared 162（走管线自然入口）。
* 待办：批次启动待批；`--net` 全库活检待批；pending/cleared 件自 ADR-0052 起在 `advance s0` 强制过机检。
