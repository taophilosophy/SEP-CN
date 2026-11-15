# 0057. SUMMARY 集群占位母行改为无链接分组行（GitBook 一文件一页）

accepted | 2026-11-16

## 背景

2026-11-16 用户报错：GitBook 导入时报 `The summary contains multiple entries referencing "README.md"`。

查证（gitbook.com/docs，2026-11 现值）：`SUMMARY.md` 是 GitBook 空间目录的镜像，**每个 Markdown 文件只能出现一次**（一个页面只能有一个 URL），否则同步/导入被拒。

本仓符合该报错的形态：

* `SUMMARY.md` 有 **183 行**指向 `README.md`：第 1 行是站首页（合法），其余 **182 行是集群占位母行**，形如 `* [\*美学 aesthetics](README.md)`，本身没有独立页面，只承担「字母分节 → 主题簇 → 词条」中的主题簇层级；
* 成因可追至目录重建（`tools/rebuild_dir.py` 的「纯导航节点（无作者、快照无对应条目页），链到 README」口径）——当时为满足 GitBook「每个条目都要有链接」的要求，把无页面的分组节点统一指向 `README.md`，与现行「一文件一页」约束正面冲突；
* 本地消费方早已为这批行开了口子：`tools/check_summary.py` 的 H1 比对跳过 `README.md`（「多行共指」）、`.vitepress/config.mts` 的首页行过滤按标题转义特征排除、`tools/progress.py` 因路径首段不是字母而不计——即这 182 行从未被当作真实页面统计；
* ADR-0056（GitBook 双语发布，同日 accepted）已把 GitBook Git Sync 定为发布路线，本缺陷是其导入可行性的前置障碍。

## 决策

1. **集群占位母行改为无链接分组行**：`* [\*美学 aesthetics](README.md)` → `* \*美学 aesthetics`。保留 `\*` 前缀（占位母行的身份标记，`mu-lu-s.md` 不收、`check_summary` 的空分组判定都靠它）与子条目缩进层级，只去掉链接。
   * 2026-11-16 追加：**别名词条行**（标题含「——见 / — see」）与目标词条真实行同指一文件，同类报错换文件复现（`i/ibn-rushd.md`），按同一手法去链接——641 行，见 [ADR-0060](0060-别名行去链接.md)。
2. **删除 2 个空标签**（无子条目的占位行，删前逐个核为冗余）：`\*动物 animal` 的重复行（同标题另有一行带 5 个子条目）、`\*斯宾诺莎 Spinoza`（挂在真实词条 `巴鲁赫·斯宾诺莎 Baruch Spinoza` 下的空子标签）。
3. **`yuanwen/SUMMARY.md` 镜像同步改写**：同一批行去链接（该文件是中文标题镜像、被 VitePress 用于中英按序配对，两侧必须逐位对齐）。
4. **`tools/check_summary.py` 认无链接分组行**：不再计入 `UNPARSED`；新增两项口径——`nav groups (linkless, ADR-0057)` 计数，以及**空分组行为硬错误**（GitBook 与侧栏都会留一个空组）。判定从严：残留链接语法碎片（`[`、`](`）仍按 `UNPARSED` 硬错误抓出，防止坏链被静默降级成分组行。
5. **站点侧栏行为保持不变**：`.vitepress/config.mts` 的 `parseSummary` 本就不为无链接行产出条目，改后侧栏无需改逻辑；顺手改掉「159 行按标题转义排除」的过期注释，并简化 `topRows` 过滤（`README.md` 现在只可能是首页一行）。
6. **英文空间 TOC 的接口约定**：ADR-0056 的 `tools/gen_en_summary.py` 已按本节实现——母词条占位行输出为**无链接分组行**（去 `\*` 标记、留英文标签与缩进），`--no-groups` 是「GitBook 拒收无链接项」时的回退形态；分组行不是页面，生成器不得改回指向文件的链接。2026-11-16 追加：别名行（ADR-0060）走同一分支输出英文标签。

## 后果

* **正面**：GitBook 导入的重复引用障碍消除；`SUMMARY.md` 重新满足「一文件一页」；结构审计新增空分组硬门，防止同类空标签再混入；本地 VitePress 侧栏渲染**逐字节不变**（见证据），阅读站零回归。
* **代价**：`SUMMARY.md` 不再是「每行都是 markdown 链接」的纯链接列表，所有解析方都须知分组行这一形态（已核清消费方：`check_summary`、`check_mulu_s`、`progress`、`campaign`、`common.find_zh_doc`、`create-pdf.yml` 的按字母过滤、`file-name-check.yml`、`sync-headers.yml`；除 `check_summary` 外均按路径解析，分组行天然不参与）。导出 PDF 的 `gitbook-pdf-export/mdconv.py` 只抓全文 markdown 链接目标（`re.findall(r'\[.*?\]\((.*?)\)')`），分组行不产出条目——改写前反而会把它抽成 182 个重复的 `README.md` 目标，改写后导出面只增不减。
* **待实测（GitBook 侧）**：现代 GitBook 对无链接列表项的渲染方式（按 GitBook 官方 skill 文档，列表项「应当是 markdown 链接」；旧版 gitbook-cli 明确支持无链接项渲染为非可点击标签）。首次同步后须核对主题簇标签是否保留、页面数是否恰为 2526。**回退方案**（若 GitBook 拒收无链接项或自行建空页）：删除这 180 行分组行，站点侧栏改由 `mu-lu-s.md`（手编分类单一事实源）在构建期派生分类树。
* **与 ADR-0056 的顺序**：本 ADR 不改英文空间配置面，只改两份 SUMMARY 的行形态；ADR-0056 的生成器与页面数核对按新形态复算（两侧条目数仍为 2526 / 2513，与其 ADR 记载一致）。

## 证据

* 改写账本（逐行新旧全文、行号、删除行）：`state/summary-nav-unlink-20261115.json`（运行态，不入库）；改写脚本 `script/_summary_unlink_nav.py`（本地草稿区，幂等、残余归零前置门）：
  * 前置门：两侧各 2708 列表行、README 引用 183（首页 1 + 占位 182）、空标签 2、中英标题序列逐一相等；
  * 写回：每侧去链接 180 行、删除 2 行；后置门：两侧各 2706 行、README 引用 1、空标签 0、标题序列仍逐一相等；二次运行识别「已应用」零改动（幂等）。
* 侧栏不变性：`bun` 导入真实 `.vitepress/config.mts` 导出 `themeConfig.sidebar` JSON 快照，改写前后 `cmp` **逐字节一致**（964 KB；含按字母分键侧栏、英文侧栏、瘦身索引侧栏与目录页侧栏）。
* 门禁：`tools/check_summary.py` → `total entries 2526 / nav groups 180 / empty nav groups 0 / HARD ERRORS 0`；`--headers` H1 mismatch 0；`tools/check_mulu_s.py` HARD 0；新增单测 `tools/tests/test_check_summary_nav.py` 4 例全绿（合法分组行、空分组行硬错误、坏链仍 UNPARSED、`--headers` 忽略分组行）。

## 落点

* `SUMMARY.md`、`yuanwen/SUMMARY.md`：各 180 行占位行去链接、各 2 行空标签删除（两侧镜像同步）。
* `tools/check_summary.py`：分组行解析、`nav groups` 计数、空分组硬错误（`hard` 求和增项）。
* `tools/tests/test_check_summary_nav.py`：新增。
* `.vitepress/config.mts`：`parseSummary` 与 `topRows` 注释改新口径，`topRows` 过滤简化（无行为变化）。
* `rules/01-repository-structure.md`：`SUMMARY.md` 规则增「无链接分组行」条款。
