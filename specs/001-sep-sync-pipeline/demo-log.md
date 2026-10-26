# 演示轮 1 日志：SEP 同步管线实跑记录

**日期**: 2026-10-26 | **执行**: ZCode 会话（specs/001-sep-sync-pipeline） | **状态**: 完成，问题清单见文末

## 执行轨迹（命令 → 结果）

| 步 | 命令/动作 | 结果 |
| -- | --------- | ---- |
| 1 | 安装 Spec Kit（uv tool install specify-cli → specify init --here --integration zcode） | `.specify/` + `.zcode/skills/` 就绪 |
| 2 | SEP 网站完整抽样分析（9 词条 + contents/new/archives/archinfo/RSS/notes/补充材料/存档对比） | 结构事实固化进 spec.md |
| 3 | 四件产物 spec/plan/tasks/checklist + 上游自动件 | 全部落盘并 git 入库 |
| 4 | 用户裁定四项（全量重译/经典三审三校/元数据入库+原文本地/AGENTS.md 归他会话） | 写回 FR-012/013/014 |
| 5 | 管线工具 10 个文件（common/fetch/parser/extract_text/fetch_entry/fetch_catalog/baseline_audit/task_ops/check_style + tests） | 27 个单测全绿 |
| 6 | `python tools/fetch_catalog.py` | 1808 正常词条 + 621 别名引用（85 独立 + 536 并入） |
| 7 | `python tools/fetch_entry.py set-theory logic-classical bayes-theorem bell-theorem quine` | 5/5 成功，10 文件，0 失败；set-theory 抓到 2 个补充材料（basic-set-theory.html、ZF.html）、bayes 抓到 notes.html、bell 抓到 image1/2.jpg |
| 8 | `python tools/baseline_audit.py` | hash_ok=10，hash_fail=[]，missing_files=[] |
| 9 | `fetch_entry abduction / alcmaeon / arcesilaus`（战役批 a 预抓） | 3 词条入基线 |
| 10 | `task_ops create alcmaeon --kind retranslate` → `clear`（gate 过）→ 全文初译 → `advance draft` → `advance s1` | 状态机 pending→cleared→drafted→s1_checked，证据留痕 |
| 11 | `check_style.py` 对译文 | 首轮 11 issue（全部在照录文献内）→ 加参考文献豁免 → 0 issue |
| 12 | 提交 | 见 git log（演示轮 1 系列） |

## 发现与纠偏清单（每条已落实或登记）

1. **并发会话冲突（最严重）**: 用户安排的另一会话在同仓库并行工作（pull/reset/commit、批量清空词条正文、把 `/tools`、`/.specify`、`/.zcode` 写入 .gitignore、提交并"完善"了我的 spec.md）。本会话 6 份未跟踪产物曾被清除。**对策**: 产物写盘即 `git add`（research D11）、跨进程双视角复核、冲突不当场对抗只登记。**待用户裁定**: `/tools` 是否恢复入库（不入库则管线代码无版本控制，违背可复现原则）。
2. **SMB 假成功误诊**: 最初把产物丢失归因于网络映射盘写入假成功；真因是并发会话的 git 清理。plan.md 环境约束已按真因改写。跨进程复核习惯仍保留（对真 SMB 假成功也有防御价值）。
3. **`tools/http.py` 遮蔽标准库**: 模块名 http 与 stdlib 冲突 → 改名 `fetch.py`（tasks.md T004 已注明）。
4. **可执行工具缺 sys.path 引导**: `python tools/x.py` 报 ModuleNotFoundError → 六个工具加仓库根引导。
5. **parse_catalog 三连错**: (a) `<strong>` 包裹的链接没匹配（547 条全漏）；(b) 别名判定的 `\b` 被 heredoc 转义层写坏成 `\x08` 退格符（别名 0 条）；(c) 别名记录用目标 slug 作键，挤掉真词条。→ 重写为两遍归并模型（正常词条占键 + aliases 数组 + 无主别名独立），补目录单测（原测试盲区）。
6. **pubinfo 正则吃星期几**: `First published Wed Aug 22, 2007` 被整段捕获 → 星期设为可选非捕获组。
7. **archinfo fixture 用错**: 测试误用存档词条页而非 archinfo.cgi 输出 → 换正确 fixture。
8. **http 日志秒级时间戳**: 相邻请求间隔判定受取整假象干扰（最小显示 1.0s）→ 日志改毫秒精度，Check 29 从此可判定。
9. **extract_text 节号重复**: `[H2] 1 1. Abduction` → 渲染时剥离节号前缀。
10. **find_zh_doc 匹配过严**: 只认"路径以 slug.md 结尾"，实际文件名是 `…-alcmaeon-carl-huffman.md` → 加文件名子串回退。
11. **check_style 两个盲区**: (a) 照录英文文献里的引号被中文引号规则误伤 → 参考文献节豁免（含子标题层级处理）；(b) 围栏代码块内容行漏豁免 → 补 `fence_open` 守卫。
12. **heredoc 批量补丁不可靠**: 含转义序列的字符串替换曾静默失败（replace 未命中不报错）→ 教训：改用 Write 全量重写 + 单测护航。
13. **clear 幂等性**: 另一会话已把词条清成 H1 壳，clear 对其幂等（git diff 为空）——SOP 步 1 的定义（保留 H1）与他会话的批量清空兼容。
14. **体例冲突待裁定**: 古典人名音译（本仓库 SUMMARY.md 标题惯例，如"阿尔克迈翁"）vs《UNIX 生活》AGENTS.md"人名一律保留英文"。演示译文采用折中：有千年通行译名的古典人名用汉译+首次括注，现代学者保留英文，全部登记 yi-zhe-shuo-ming.md，最终以 AGENTS.md 修正会话裁定为准。
15. **术语表缺失**: 本仓库原无 yi-zhe-shuo-ming.md → 已创建（术语 10 条 + 人名 16 条 + DK/行号约定），SOP 步 2 的"先登记后使用"从此有载体。
16. **SEP 源头小不一致**: 目录页 1.1 节作 "Medical Writer or Philosopher?" 而正文 H3 作 "Physician Philosopher?"——译文按正文版本，登记备查。

## 待办（下一轮循环入口）

- [ ] 用户裁定：`/tools` 入库与否（影响可复现审计链）
- [ ] 用户裁定：古典人名音译体例（上文 14）
- [ ] `task_ops advance alcmaeon --step s2`（二校·语言）继续六道
- [ ] T020-T027：detect_updates.py 与 compare_versions.py 实现（US2/US3）
- [ ] 战役批 a（T035）正式开批
