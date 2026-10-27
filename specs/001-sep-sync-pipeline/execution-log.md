# ADR-0007 上游同构重建执行记录 — 2026-10-27

用户裁决：统一 SUMMARY 与磁盘结构为上游同构；先删全部词条内容目录；根 `<slug>/index.md`（中文）与 `yuanwen/<slug>/index.md`（英文，省 entries/ 层）；别名保留并链到目标；SUMMARY 由单一会话独自重写。规则登记：`rules/adr/0007-上游同构重建.md`、`rules/01`、spec Assumptions（commit 13cfca27）。

## 删除（commit 3c9747e8）

20+ 混杂目录（argument/、value-pluralism/、brentano/ 等 23 个）+ 根级字母目录（a-t、u/x/y、pending/）共 **2678 个文件** git rm 入史；悬空词条图片 10 张；保留治理与项目设施、README 引用的 wechat.png。

## SUMMARY.md 重写（2565 行）

工具 `tools/rebuild_dir.py rebuild`，以 HEAD（68be4fac）为文本源、官方快照（`.github/sep-baseline/official-snapshot.json`）为 slug 权威：

* **保留 2565 行**：条目 1799（快照精确/词集/短标题匹配）+ 别名 604（链到目标 `<target>/index.md`，不占目录）+ 导航节点 143（无作者且快照无对应条目页，链 README 保缩进结构）+ 前置页 12（README、mu-lu-s、qian-yan/ 3 页、guan-yu/ 7 页）+ 补回缺失条目 5（korean-philosophy、lawphil-naturalism、leibniz-causation、biodiversity、computational-linguistics——SUMMARY 历史上丢失、快照与 mu-lu-s 均有）。
* **丢弃 42 条重复导入行**（与其他行同 slug）+ 52 条开发文档链接（HEAD 版已无，历史轮次记录）。
* 过程修复的三个算法 bug：① 别名英文提取切分序错误（在"——见"上取第一段误伤别名文本）；② 模糊匹配对无作者行放行（"diversity" 模糊匹配到 "biodiversity"），改为必须有作者重合 ≥0.4；③ 注册优先级（导航/派生行先注册挤掉真实条目），改为两遍注册：真实条目先注册，派生行 finalize 二次裁决。
* 兜底链：官方快照精确标题 > 词集（忽略冠词 the，救回语序颠倒）> 模糊（须作者佐证）> 快照短标题后缀（SUMMARY 全称以短标题结尾）> 派生 slug（待人工核对）。

## mu-lu-s.md 同步

* 11 处链接文本同步为 SUMMARY 标题（规则：mu-lu-s 为派生视图，文本与 SUMMARY 一致）。
* naturalism slug 错配修正：`数学哲学中的自然主义 (Alexander Paseau)` → naturalism-mathematics/；自然主义（David Papineau）→ naturalism/ 并补回 SUMMARY。

## 检查器同步（ADR-0007 语义）

* `tools/check_summary.py`：重复路径统计豁免别名行（链目标路径属预期共享）与导航节点（链 README）；orphan 扫描排除 yuanwen/en（镜像库）。
* `tools/check_mulu_s.py`：别名行不覆盖条目行标题（setdefault）。

## 骨架与迁移

* **中文侧**：1815 个 `<slug>/index.md`（仅 H1=SUMMARY 条目文字；`stubs` 子命令，幂等）。
* **yuanwen 迁移**：2292 个扁平文件迁入 `<slug>/index.md`（点号补充材料 `slug.suffix.md` 拆入 `<slug>/<suffix>.md`；11 个已跟踪演示文件 `git mv` 保历史）；补缺 8 个英文标题桩。
* **镜像覆盖 1872/1872 = 100%**（快照 main 全部有 `yuanwen/<slug>/index.md`）；SUMMARY/mu-lu-s 断链 0。

## 门禁

`check_summary` / `check_mulu_s` / `check_doc_size` 全部 0 退出；orphan 40 个均为基建/开发文件（预期）。

## 待人工核对

1. **24 个派生 slug 条目**（明细 `rebuild-review.json` 搜"待人工核对"）：快照无此条或同名歧义，路径为标题推导，抓取 404 即可确认并改名。已知重点：on-utopia（疑 plato-on-utopia）、and-the-pineal-gland（疑 descartes-pineal-gland）、action-at-a-distance-in、health-well-being-personal-relationships、naturalism（数学自然主义已改 naturalism-mathematics，勿回退）、in-the-renaissance（疑 aristotelianism-renaissance）、continental-rationalism。
2. **137 个导航节点**链 README（无作者且快照无对应条目页，如"美学 aesthetics""类比 analogy"）；快照索引修好后可复核是否漏条目。
3. **42 条重复导入行**已从 SUMMARY 移除（明细在 rebuild-review.json "slug 与其他行重复"）。
4. 别名目标无法解析 2 条（recursion 自指、Routley）。
5. README 微信二维码图 wechat.png 已删除（README 引用行同步移除，.gitbook/assets 清空）；`yuanwen/SUMMARY.md` 已由 write_summary 重建为直拷贝镜像（ADR-0007 后两侧相对路径逐字符一致）；`yuanwen/assets/`（227 个提取文件，gitignored 本地原始物）待清理裁决。
6. `tools/summary_sync.py` 与 `tools/repair_loop.py` 仍按旧 a–z 字母方案定位文件，需按 ADR-0007 改造（yuanwen.py 输出路径已于 bbbf40ae 对齐）。

## 复现

```
python tools/rebuild_dir.py rebuild   # SUMMARY/mu-lu-s 链接重写（基于当前文本源）
python tools/rebuild_dir.py stubs     # 中文侧 <slug>/index.md 骨架（幂等）
python tools/rebuild_dir.py yuanwen   # yuanwen 迁移 + 英文侧补缺
python tools/rebuild_dir.py check     # 断链/镜像覆盖核验
```

## ADR-0008/0009 执行补充 — 2026-10-27

* **ADR-0008（词条文件化）**：`<slug>/index.md` → `<slug>.md` 平铺（flatten，git mv 1821+3，SUMMARY/mu-lu-s 链接改写）。
* **ADR-0009（A–Z 字母目录）**：根级平铺 → `<letter>/<slug>.md`（toletters，moved 4116、git mv 1821；SUMMARY 改写 2560 处、mu-lu-s 1805 处）；补充材料点号命名同目录平铺；图片归 `yuanwen/assets/<slug>/`；英文字母目录与中文侧逐字符镜像。
* 过程修复：① flatten 英文侧 index.md 目标路径算错（首笔落 yuanwen/index.md 后全部碰撞跳过）；② toletters 误迁 AGENTS.md/CODE_OF_CONDUCT.md/CONTRIBUTING.md（skip_roots 补齐）；③ "进步 progress" 条目被 narrative progress/ 目录占位致桩未建成，已建 `p/progress.md`；④ 同名子词条裁定：亚里士多德主义复兴 → `a/aristotelianism-renaissance.md`（原派生路径 i/in-the-renaissance.md 作废）；⑤ 历史缺载条目补回 6 条（arabic-islamic-essence、aristotle-de-motu、aristotle-text、korean-philosophy 等，中文标题按集群命名惯例拟定，待译名登记册复核）。
* **镜像覆盖**：快照 main 1872 条，中文/yuanwen 双侧 100%（缺口 74 条为上游增量，见 upstream-increment.json）。
* **工具对齐（ADR-0008/0009）**：yuanwen.py（`yuanwen/<letter>/<slug>.md` + 点号补充材料 + assets 图片）、common.py find_zh_doc、summary_sync.py（无字母节插入、`<letter>/<slug>.md` 路径）、progress.py（字母目录统计）、rebuild_dir.py（stubs/flatten/toletters/check）；migrate_exec.py 标记废弃。
* **待上游同步 intake**：74 条快照有而 SUMMARY 无的条目（upstream-increment.json），需按 rules/04 建任务后译名登记、建桩插入，不机器臆造中文标题。

## 全量复核与管线验证轮 — 2026-10-27

* **门禁套件**：check_summary / check_mulu_s / check_doc_size / check_junk / check_terms / check_academic 全部 0 退出（check_academic 修复：kind=glossary-maintenance 任务无 SEP 版本可钉，豁免 version_pin 要求）。
* **同步 SUMMARY→baseline**：zh_doc 旧拼音路径重同步 704 处（SUMMARY 字母目录路径为准）；72 条 baseline 独有条目属 upstream-increment intake，维持原状；yuanwen.md 记录路径已是正确字母目录形态。
* **mu-lu-s 分类更新**：补 5 条——亚里士多德子词条 2 条（嵌套）、arabic-islamic-essence（中世纪区）、academic-freedom（社会政治区）、naturalism-mathematics（数学哲学区）；断链 0、标题一致 0、重复 0。
* **干执行验证（3 轮，礼貌 5 秒）**：fetch_catalog（1808 条目录快照 + diff，无上游变化）→ fetch_entry capitalism（en/capitalism/ 原始 HTML + baseline 登记，Fall 2026 存档版）→ yuanwen.convert_entry（yuanwen/c/capitalism.md 镜像，cite_defs 254）。全链跑通；capitalism zh_doc=None 为正确行为（未入 SUMMARY，译名登记后按 summary_sync apply-add 接入）。
* **段级变更比较（US-3）**：目前仅有目录级 diff（fetch_catalog），段落级比较工具尚未实现，属 spec 001 后续工程。

## 学术规范落地与 US-3 段落比较 — 2026-10-27

* **tools/compare.py（spec 001 US-3 落地）**：抓取英文源最新快照（不覆盖 en/ 基线，礼貌 5 秒）与基线比较——节级拆分（h2 锚 id + 标题）、节级 added/removed/moved、modified 节内段落级 diff（difflib 附摘录）；每条变更映射 baseline.zh_doc 的 md 文档与 `## 节标题` 行号，无 zh_doc 标注待建任务；单元测试 tools/tests/test_compare.py（8 项）覆盖 added/removed/modified/映射/无变更。干执行：kant-transcendental 抓取比对报"无变更"（source_sha256 一致）。
* **学术规范落地三件套**：① checks.yml CI 接入 check_academic + check_all --quiet；② task_ops.py advance() 审校挂钩——s3/r3 校次自动跑 check_academic --docs --strict，0 硬错误方可过（词汇表维护任务与无 zh_doc 条目豁免）；③ tools/check_all.py 一键全量合规复核（六项门禁 + 单元测试，--all 加 baseline_audit）。
* **修复既有红灯**：test_check_academic 三个测试自 68be4fa 创建起即红（fixture gamma-doc.md 仅 7 非空行，按"存根=非空行≤10"规则被跳过，告警类断言永不触发）——fixture 增补占位段至 14 非空行后恢复；compare.py 模块导入的 stdout 重包在 unittest discover 下与同型操作相撞（旧 wrapper 回收关闭 buffer），加 UTF-8 守卫。
* **同步**：rules/05（工具表 + 快速命令 + CI 清单）、contracts/cli.md（compare.py 契约）、rules/07 衔接表由挂钩自动执行。

## CI 目录误报修复 — 2026-10-27

* 根因：file-name-check.yml（"检查 SUMMARY.md 目录"）在校验通过时只打日志、从不开闭历史 issue——目录重建前的真实失败创建了 "SUMMARY.md mismatch: Missing files" issue，此后每次触发都"始终报告目录有问题"。
* 修复：校验通过时自动评论并关闭历史 mismatch issue（actions/github-script）。本地已核验 SUMMARY 2563 链接 0 缺失、0 大小写错位（Linux CI 逐字符校验安全）。
* 推送：经用户授权 `git push -f`（49c4683c）。**被覆盖的远端提交 587ec741 仅存在于并行会话本地**（本仓库未 fetch 到），该会话需 `git fetch && git reset --hard origin/main` 重新同步后将其工作重新落地。

## 流程依赖审查与更新流程验证 — 2026-10-27

* **依赖权属契约**（contracts/cli.md）：新词条接入唯一入口 apply-add、批量骨架 rebuild stubs、baseline 唯一登记方 fetch_entry、fetch_audit 只补缺件不写 baseline（审计 JSON 即凭证）、compare 产出持久变更文件、H1 同步归 CI——八项职责一一对应，消除双路径矛盾。
* **并行化**：check_all 七门禁 ThreadPool 并行（5.8s，原串行约 12s 提速 2 倍）；compare 批量串行受 5 秒礼貌约束（并发抓取属 2026-10-27 并发裁定范围，按需启用 fetch_all 节拍）。
* **更新流程闭环干执行**：fetch_catalog（1808 条无上游变化）→ compare --html 模拟变更 → 持久变更文件 compare/<slug>.json → update 任务（--from 变更文件，change_file 记录）→ 状态机 s1/s2/s3：反例（无 changes: 前缀）被 PreconditionError 拦截，正例全通过且 s3 学术挂钩触发。演练任务与模拟变更文件已清理（可按 drill 复现），本记录为凭证。
