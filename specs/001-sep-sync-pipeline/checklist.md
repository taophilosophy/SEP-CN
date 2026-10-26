# Checklist: SEP 同步管线验收检查点

**Feature**: specs/001-sep-sync-pipeline | **Created**: 2026-10-26 | **依据**: spec.md FR-001…018 / SC-001…005、tasks.md T001…T046

> 勾选权归复核人：`[x]` 表示该判据经复核通过。全部为可观察事实判定。

## 一、实现完整性（管线四工具链 + 状态机可运行）

- [ ] Check 1: `python tools/fetch_entry.py set-theory` 的 stdout JSON 含 files[]（每件含 path/sha256/bytes/kind）、missing[]、pubinfo{first_published,substantive_revision}、archinfo.archive_edition 字段（来源：FR-001/002/003、T012）
- [ ] Check 2: 抓取 set-theory 后磁盘存在 `en/set-theory/index.html` 与 `en/set-theory/basic-set-theory.html`，两者 sha256 与 baseline/entries.json 登记一致（来源：FR-001/002、T012）
- [ ] Check 3: 抓取 bayes-theorem 后磁盘存在 `en/bayes-theorem/notes.html` 且 kind=notes（来源：FR-001、T012）
- [ ] Check 4: 抓取 bell-theorem 后磁盘存在 `en/bell-theorem/image1.jpg`（kind=image），且 `baseline/entries.json` 有其 sha256（来源：FR-005、T012）
- [ ] Check 5: 正文引用 notes.html 而其 404 时（如 quine），missing[] 含 {"expected": "notes.html", "http_status": 404} 且进程退出码非 2/3（来源：Edge cases、T012）
- [ ] Check 6: `python tools/fetch_catalog.py` 输出 entries 计数 ≥1800、aliases 计数 >0；`en/_catalog/` 出现带时间戳的 contents.html 快照；baseline/catalog.json 落盘（来源：FR-007、T013）
- [ ] Check 7: `python tools/extract_text.py set-theory` 连跑两次，输出文件 `en/set-theory.txt` 两份哈希逐字节一致（来源：FR-017、T009/T010）
- [ ] Check 8: `en/set-theory.txt` 内数学定界符 `\(`、`\[` 出现且 `&mdash;` 已解码为—且不残留 `&` 实体（来源：FR-016、T010）
- [ ] Check 9: `python tools/baseline_audit.py` 输出 hash_fail=[] 且 missing_files=[]（对已抓 5 样本）（来源：FR-002/017、T014）
- [ ] Check 10: `python tools/detect_updates.py --rss` 的 from_rss 含 slug=kant-transcendental、event=revised、date=2026-10-24、changes_to 含 Main text（来源：FR-006、SC-002、T022）
- [ ] Check 11: `python tools/detect_updates.py --archinfo --only set-theory` 输出 baseline_edition 与 latest_edition 且变更时 queue 含该 slug（来源：FR-008、T021）
- [ ] Check 12: `python tools/compare_versions.py anaxagoras --old archives/winter2019 --new live` 的 items[] 每条含 type∈{add,remove,replace,move}/section/excerpt_en，且 excerpt_en 在对应来源 HTML 中逐字符可检索（原文照录未改写；来源：FR-009、T024/T026）
- [ ] Check 13: Check 12 产出的变更清单落盘 `baseline/changes/anaxagoras-<日期>.json` 且每条 zh_doc 指向存在的 md 或字面量"待建任务"（来源：FR-010、T025）
- [ ] Check 14: `python tools/task_ops.py advance <slug> --step s2 --actor X --evidence Y` 在 s1 未完成时退出码 3 且任务 JSON state 不变（来源：FR-011/012、T028/T030）
- [ ] Check 15: `task_ops.py clear <slug>` 在 baseline_audit 未通过该词条时退出码 3 且不修改中文 md（来源：FR-013、宪法附加约束、T030）
- [ ] Check 16: `python tools/check_style.py <含直引号"测试">` 输出 rule=curly-quotes 的 issue，退出码 1（来源：FR-015、T029/T031）
- [ ] Check 17: `python tools/check_style.py` 对 `**加粗**紧贴汉字` 报 bold-spacing issue，对 `**加粗** 汉字` 不报（来源：FR-015、T031）
- [ ] Check 18: `python -m unittest discover -s tools/tests -t .` 0 failures（26 例：parser/common/extract/task_ops/check_style 全覆盖）（来源：T011/T030/T031）
- [ ] Check 19: tools/ 下 8 个管线脚本全部能无参或 --help 运行打印用法而非 traceback（退出码 2）（来源：contracts/cli.md、T001–T029）
- [ ] Check 20: 管线写 JSON 后读回哈希比对（write_json_verified），内容不符时抛错而非留坏文件（来源：plan.md 环境补充约束、T003/T008）

## 二、需求覆盖（spec 每条 FR/SC/US 有对应判据）

- [ ] Check 21: spec FR-001…FR-018 共 18 条在 checklist.md 可各自找到 ≥1 个 Check（映射表见文末"追溯矩阵"），无遗漏（来源：spec Requirements）
- [ ] Check 22: SC-001：5 样本抓取成功率=100%（5/5 词条包完整）且缺省件登记率=100%（来源：spec SC-001、T015）
- [ ] Check 23: SC-002：RSS 与 archinfo 双源对 2026-10 已知事件的命中结论一致（0 矛盾）（来源：spec SC-002）
- [ ] Check 24: SC-003：anaxagoras 比较清单人工抽查 ≥10 条，0 漏报 0 多余（来源：spec SC-003、T026）
- [ ] Check 25: SC-004：任一 slug 执行 `task_ops.py show` 单命令 ≤1 分钟返回当前 state、steps[]、actor、at（来源：spec SC-004、T028）
- [ ] Check 26: SC-005：演示轮 1 后 spec/plan/tasks/checklist 至少一份出现带"演示轮 1 修订"标记的改动，且 `script/tmp/demo-log.md` 记录对应问题（来源：spec SC-005、US5、T018）
- [ ] Check 27: User Story 4 验收：示范文档任务 JSON 的 steps[] 恰含 gate/clear/draft/s1/s2/s3/r1/r2/r3/done 十节且顺序无跳（来源：spec US4、tasks SOP、T032）
- [ ] Check 28: 战役批任务 T035–T042 共 8 批在 tasks.md 均有可勾选行且每批注明验收方式（批完成=该字母全部正文词条 done + audit.py 结构核对通过）（来源：tasks T035–T042）

## 三、边界与异常

- [ ] Check 29: 连续抓取任意两请求间隔 ≥5 秒（读 script/http-log.jsonl 相邻时间戳差值最小值验证）（来源：FR-004、宪法 V、T004）
- [ ] Check 30: 断网/超时模拟下 fetch_entry 对同一词条重试 ≤3 次后以退出码 1 结束且 failures[] 有原因，不产生空词条包（来源：FR-004、Edge cases）
- [ ] Check 31: 别名词条（如 akrasia）在 fetch_catalog 清单中 alias_of 非空，不建翻译任务（来源：Edge cases、T013）
- [ ] Check 32: 构造 contents.html 中存在而基线缺失的词条场景，fetch_catalog diff 的 added 列表含之（rename/removed 同理可测）（来源：FR-007、Edge cases）
- [ ] Check 33: update 类任务的 s1 证据可定位到变更清单条目（evidence 引用 baseline/changes/<slug>-*.json 的 item 序号），且未触碰变更段以外的已译内容（git diff 验证仅变更段落变动）（来源：SOP update 行、"不复查旧错"、T028）
- [ ] Check 34: 全部产出文件 UTF-8 无 BOM、LF（读头三字节验证；对 en/、baseline/、tasks/、specs/ 抽查 ≥10 文件）（来源：D8、Technical Context）
- [ ] Check 35: 图片引用名与磁盘文件名逐字符一致（引用 `image1.jpg` 时磁盘无 `Image1.JPG` 之类变体；对含图词条抽查）（来源：FR-005、D8、check-images.yml）

## 四、既有功能未回归（仓库 CI 与内容安全）

- [ ] Check 36: 提交后 `sync-headers.yml` 触发结果与 SUMMARY.md 一致，本流程未造成 H1 漂移（对比 push 前后 git diff 仅预期文件）（来源：Assumptions、T045）
- [ ] Check 37: markdownlint-cli2 对 specs/、tasks/、baseline/ 新增产物 0 error（配置 .github/.markdownlint.json）（来源：FR-015、T045）
- [ ] Check 38: 本流程未修改 en/、AGENTS.md、.gitignore、yi-zhe-shuo-ming.md（git status 验证，AGENTS.md/.gitignore 归其他会话）（来源：Assumptions、用户裁定）
- [ ] Check 39: 清空重译前的旧译文可从 git 历史恢复（任取一个 done 文档 `git log --follow` 能找到 clear 前的最后版本）（来源：FR-013、宪法附加约束、T032）
- [ ] Check 40: baseline/entries.json、tasks/*.json 均已入版本库（git ls-files 可见），en/ 下无任何文件被 git 跟踪（来源：FR-014、存储裁定、T016）

## 追溯矩阵（FR → Check）

| FR | Check | FR | Check |
|----|-------|----|-------|
| FR-001 | 1,2,3,4 | FR-010 | 13 |
| FR-002 | 2,4,9 | FR-011 | 14,25,27 |
| FR-003 | 1 | FR-012 | 14,27 |
| FR-004 | 29,30 | FR-013 | 15,39 |
| FR-005 | 4,35 | FR-014 | 40 |
| FR-006 | 10 | FR-015 | 16,17,37 |
| FR-007 | 6,32 | FR-016 | 8 |
| FR-008 | 11 | FR-017 | 7,9,12 |
| FR-009 | 12 | FR-018 | 7,20 |
