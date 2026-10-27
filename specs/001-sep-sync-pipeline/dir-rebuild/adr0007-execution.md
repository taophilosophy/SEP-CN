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
5. `yuanwen/assets/`（227 个提取文件，gitignored 本地原始物）与 `yuanwen/SUMMARY.md`（已跟踪遗留）待清理裁决。

## 复现

```
python tools/rebuild_dir.py rebuild   # SUMMARY/mu-lu-s 链接重写（基于当前文本源）
python tools/rebuild_dir.py stubs     # 中文侧 <slug>/index.md 骨架（幂等）
python tools/rebuild_dir.py yuanwen   # yuanwen 迁移 + 英文侧补缺
python tools/rebuild_dir.py check     # 断链/镜像覆盖核验
```
