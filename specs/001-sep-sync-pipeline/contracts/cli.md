# Contracts: 管线工具 CLI 接口契约

**Feature**: specs/001-sep-sync-pipeline | **Date**: 2026-10-26

全部工具为 `python tools/<name>.py` 形式的命令行程序，遵守统一约定：

- **输入**：命令行参数（词表、路径、开关）；不读 stdin 交互。
- **输出**：人读进度信息走 stderr；机器可读结果一律 JSON 走 stdout（零信任审计：每次运行的输出可存档为凭证）。
- **退出码**：`0` 成功；`1` 部分失败（详情在 stdout JSON 的 `failures[]`）；`2` 用法错误；`3` 前置条件不满足（如基线缺失、跳步）。
- **礼貌**：凡发 HTTP 请求的工具，请求间隔默认 5 秒（`--delay` 只能调大不能调小；robots 目录禁区已获用户授权绕过，但间隔约束保留）。
- **编码**：文件读写一律 UTF-8 无 BOM；stdout JSON `ensure_ascii=False`。
- **路径**：以仓库根为基准解析相对路径；Windows/Unix 兼容；可执行工具自带 sys.path 引导。
- **防丢**：JSON 落盘一律经 `common.write_json_verified()`（写后读回哈希复核）。

## fetch_entry.py — 抓取词条包

```text
用法: python tools/fetch_entry.py <slug>... [--force] [--delay N]
输出: {"fetched": [{slug, files: N, missing: [...], archive_edition}], "failures": [...]}
行为: 逐词条抓取 /entries/<slug>/index.html；解析正文内对 *.html 与图片的
      相对引用，续抓 notes.html、补充材料、图片；404 记入 missing（缺省件）；
      archinfo.cgi 查询最新存档版；全部登记进 baseline/entries.json。
```

## fetch_catalog.py — 目录快照

```text
用法: python tools/fetch_catalog.py
输出: {"fetched_at", "entries", "aliases", "raw", "new_vs_baseline": {added, removed, renamed, alias_changed}}
行为: 抓取 contents.html 存 en/_catalog/<时间戳>-contents.html；解析出
      {slug, title, authors, alias_of, level} 全量清单存 baseline/catalog.json；
      与上次快照 diff。
```

## detect_updates.py — 更新检测（未实现，T020-21）

```text
用法: python tools/detect_updates.py [--rss] [--archinfo] [--only <slug>...]
输出: {"from_rss": [{slug, event: new|revised, date, changes_to: [...]}],
       "from_archinfo": [{slug, baseline_edition, latest_edition, change_type}],
       "queue": [{slug, action: retranslate|update, reason}]}
行为: --rss 解析 sep.xml 与 new.html（三个月窗）；--archinfo 对基线全量或
      指定子集核对存档版名；queue 为两源合并后的待处理清单（写 baseline/queue.json）。
```

## compare_versions.py — 快照比较（未实现，T024-25）

```text
用法: python tools/compare_versions.py <slug> [--old <快照标识>] [--new <快照标识>]
输出: {"slug", "old_ref", "new_ref",
       "items": [{type: add|remove|replace|move, section, excerpt_en, zh_doc, anchor}]}
行为: 默认比较最近两轮快照；块切分+SequenceMatcher 对齐；变更清单写入
      baseline/changes/<slug>-<日期>.json；zh_doc 按 SUMMARY.md 映射。
```

## extract_text.py — 正文提取

```text
用法: python tools/extract_text.py <slug>... [--to <输出路径>]
输出: {"results": [{slug, source, sha256_in, sha256_out, blocks, out, at}]}
行为: 从原始 HTML 提取带节号结构的纯文本（块序列），写入 en/<slug>.txt；
      提取结果可由原始物重算复核（同哈希输入必得同哈希输出）。
```

## task_ops.py — 文档任务状态机

```text
用法: python tools/task_ops.py <命令> <slug> [参数]
命令: show <slug>                          查任务状态
      create <slug> --kind retranslate|update [--zh-doc <路径>] [--from <change 文件>]
      advance <slug> --step draft|s1|s2|s3|r1|r2|r3|done --actor <名> --evidence <引用> [--unblock]
      clear <slug>                         清空正文置 cleared（gate: 基线哈希复算）
      block <slug> --reason <文>
输出: 操作后的任务 JSON 全文
行为: 任务文件 tasks/<首字母>/<slug>.json；状态迁移合法性由本工具校验，
      禁止跳步（update 类 s1/s2 证据必须以 changes: 开头引用变更清单）；
      blocked 任务冻结一切转移，仅 --unblock 可解。
```

## check_style.py — 体例检查

```text
用法: python tools/check_style.py <路径>...
输出: {"files": N, "issues": [{path, line, rule, detail}]}
规则: curly-quotes（弯引号成对/方向/禁直引号直角引号日式半角引号，词内撇号豁免）、
      bold-spacing（**两侧空格，段首块首与中文标点例外）、cjk-spacing（中西文间空格）、
      no-html（HTML 标签残留）、no-text-fence（text 语言标注）、no-asciiart（xref:/link: 残留）。
行为: 只读检查；围栏代码块与行内代码豁免；退出码 1 = 有 issue。
```

## baseline_audit.py — 基线审计

```text
用法: python tools/baseline_audit.py [slug...]
输出: {"audited": N, "hash_ok": N, "hash_fail": [...], "missing_files": [...]}
行为: 对 baseline/entries.json 登记的每件抓取物复算 SHA-256 并核对文件存在；
      宪法门 I 的机器实现——task_ops clear 的强制 gate 依赖本工具。
```

## yuanwen.py — 原文 Markdown 镜像（演示轮 2 新增）

```text
用法: python tools/yuanwen.py <slug>... | --all-baselined [--summary]
输出: {"converted": [{slug, md, cite_markers, cite_defs, supplements, notes}],
       "failures": [...], "summary_links_rewritten": N}
行为: en/<slug>/index.html（不可变快照）→ yuanwen/<字母>/<slug>.md 确定性转换；
      脚注/补充材料/图片镜像；参考文献转引用注释（[^key]）；
      --summary 重建 yuanwen/SUMMARY.md（已转换条目改链 yuanwen 路径）；
      转换登记（md 哈希+源哈希）写入 baseline/entries.json。
```
