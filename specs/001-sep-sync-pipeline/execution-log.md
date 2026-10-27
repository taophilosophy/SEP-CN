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

## 目录解析器修复连带清退与撤稿词条裁定 — 2026-10-28

* **嵌套吞没修复（50afaa94）**：parse_catalog 旧正则 `<li[^>]*>(.*?)</li>` 非贪婪匹配跨越嵌套边界，每个集群的第一个子词条被吞进父匹配，catalog.json 1808 条实际漏 64 条；HTMLParser 重写后 `--reparse` 离线重建为 1872 条（别名 654）。
* **find_zh_doc 收紧（46993453）**：二级废除子串/分词模糊匹配（trans→feminism-trans、srigupta→definitions 伪映射源），三级改整短语词边界且唯一命中、单词标题不参与（ideology→law-ideology 清零）。16 条 increment 词条此前被伪映射为"已消化"（74→58 假象），收紧后归零；存量 entries.json zh_doc 13 条由并行会话对齐（993d1c11）。
* **坏行五条裁定落地（ad4924df）**：SUMMARY/mu-lu-s 中文标题混英文残片、slug 被截断的 5 行，改写为实证真 slug——innateness-language / identity-ethics / religion-morality 见官方目录并已建基线；**pineal-gland 与 qm-action-distance 为 SEP 已撤稿词条**（Fall 2026 归档目录无、Web 检索确认归档 slug），按"保留旧译词条"裁定保留 SUMMARY 行，文件归位 p/pineal-gland.md 与 q/qm-action-distance.md。
* **软 404 垃圾注册清退**：对两个撤稿词条执行 fetch_entry，/entries/<slug>/ 返回 HTTP 200 + "Document Not Found" 正文（软 404），登记出 title 为空的垃圾基线两条——已从 entries.json 移除并删除 en/ 下 404 文件。**待建能力**：fetch_entry 需支持归档版 URL（/archives/<ed>/entries/<slug>/）方可为撤稿词条建基线，登记入 specs/005 技术债视野。
* **fetch_entry 补抓**：action / authority / artificial-intelligence（SUMMARY 有而漏抓，其中 action/artificial-intelligence 与并行会话 28e185bb 各自登记，幂等收敛）、identity-ethics / religion-morality（坏行修复归位）；fetch_audit 闭包完整（2 缺件自动补抓）。

## 英文镜像逐词条深度复核（en_integrity 定稿并接入 check_all）— 2026-10-28

* **任务**：用户指令「逐个复核网页、图片、数学公式等抓取的完整性，应在 en 文件夹，目录结构和 web 上游一致」。产出 `tools/en_integrity.py`（纯离线逐词条深度审计，18 项单元测试），全量 1731 词条跑三轮（语义收敛迭代），终态 **1731/1731 干净、硬发现 0**（首轮 3364 → 降噪 430 → 补抓后 1 → 入站引用语义后 0）。
* **四层检查**：① 页面真实性——index.html 存在、SEP 签名正向校验、错误/风控标记只在 title/h1 匹配（正文 "just a moment"/"generate limited" 等哲学文本误报已排除）、`</html>` 截断、零字节、charset；② 引用闭包按上游 URL 语义解析——HTML 注释剥离（注释掉的引用不构成加载义务）、实体反解（混淆邮箱 `m&#97;ilto:`）、双斜杠路径归一（上游 HTML 自带 `/entries//x/`）、大小写精确比对（Windows 不区分大小写会掩盖错名）、跨词条与词条内子目录资产（`../idiolects/appendix.html`、`BNfiles/x`）逐一核对本地存在；③ 目录结构一致性——在盘文件＝被引用（含跨词条入站引用表）∪ baseline 已登记，否则游离件（硬发现）；④ 数学形态盘点——MathJax 413 词条（全部站点级 `../../MathJax/`，TeX-MML-AM_CHTML / TeX-AMS-MML_HTMLorMML 两 config）、内联 MathML/TeX 784 页、公式图片资产 2 词条（frege-logic supp-begriff-formula SVG 等全部在包内），无缺件。
* **缺件补抓（礼貌 5 秒，全部 200）**：`local.js` ×419 词条（与并行会话协同完成；此前 fetch_audit 契约把 JS 排除在闭包外，b397a80e 已将裸 .js/.css 纳入词条自有资产）、`albo-joseph/vita.html`、`geometry-19th/vita.html`、`numenius/notes.html`、`formal-epistemology/ow-animate.mp4` + `zollman.mp4`（包内补充页引用）、`idiolects/appendix.html`（仅被 linguistics 跨词条路径引用，fetch_entry/fetch_audit 均不可见，手工补抓）。
* **边界发现（登记备查）**：fetch_audit 裸引用闭包对「路径形自引用」（`href="../<slug>/vita.html"`）与「同域绝对 URL」（`href="https://plato.stanford.edu/entries/<slug>/notes.html#…"`）存在盲区，由 en_integrity 的全命名空间解析覆盖；registered_orphans 4 词条（location-mereology figure06.png 等）均为上游页面注释掉的旧版引用，文件已登记保留不算缺件；en/ 顶层 `abduction.txt`/`alcmaeon.txt` 为 extract_text.py 契约产物（翻译工序输入），非上游镜像污染，保留。
* **门禁接入**：check_all.py `--all` 新增「英文镜像深度复核」（`en_integrity.py --all --quiet`，凭证 `specs/001-sep-sync-pipeline/en-integrity-full.json`；run() 支持带参脚本）；contracts/cli.md 职责权属表、rules/05 工具表同步登记（en_integrity 只读审计，不补抓不落盘 en/ 以外文件）。`python tools/check_all.py --all` 九项全绿（含 baseline_audit 全量哈希复算通过）。

## REMOVE 收尾裁定与撤稿词条归档基线 — 2026-10-28（续）

* **REMOVE 9 条全部定谳**：3 条错位别名文件由并行会话删除（eafb227d：health-well-being-personal-relationships、indian-philosophy、on-utopia）；其余 6 条经 SEP 在线探针实证为**撤稿词条**（/entries/<slug>/ 均返回软 404），裁定**保留**——旧译词条作为存档语料留存：pineal-gland、qm-action-distance、scientific-explanation、wisdom、continental-rationalism、time-experience。
* **归档版版本钉**（SEP 归档探针 + Web 检索交叉确认）：pineal-gland@spr2017、qm-action-distance@fall2019、scientific-explanation@sum2024、wisdom@fall2023、continental-rationalism@spr2026、time-experience@sum2024。
* **fetch_entry 能力扩展**：软 404 防护（SEP 错误页不再注册为基线，杜绝空 title 垃圾注册复发）+ `--archive-edition <ed>`（从 /archives/<ed>/entries/<slug>/ 抓取撤稿词条完整包）；单测 tools/tests/test_fetch_entry.py 4 项。
* **归档基线落地**：6 条撤稿词条经 --archive-edition 抓取入库（pineal-gland 7 文件、qm-action-distance 6 文件完整包）；5 条 ADD 词条基线补齐（arabic-islamic-liar、economic-democracy、moral-responsibility-empirical、nietzsche-aesthetics、realism-about-metaphysics）。并发竞态（与 apply-add intake 会话）三次重试收敛，11/11 在账。
* 注：ADD 队列 76 条中 economic-democracy 有 SUMMARY 行（find_zh_doc 命中），其余 4 条 zh_doc=None 待 intake 译名登记后接入。

## 第二轮全量镜像复核与缺件收敛（intake 并发窗口）— 2026-10-28

* **背景**：用户指令「再次全量复核」。此时并行会话正批量 intake 上游增量（baseline 1731→1877 持续增长），每轮扫描都会撞见新落地词条包的缺口。三轮扫描＋两轮礼貌补抓（`script/tmp/reconcile_missing.py` 收敛驱动器：读扫描凭证→fetch.get 5 秒节拍→重扫，至归零）后 **1877/1877 全部干净、硬发现 0、退出码 0**；`check_all --all` 九门禁全绿。
* **本轮补抓明细（全部 200）**：新 intake 词条包 local.js ×43 余（convention/evidence-legal/heritability/ecological-genetics/freewill/frege-hilbert/implicature-optimality-games/lewis-metaphysics/logical-consequence/paradox-zeno/peirce-logic/physics-Rpcc/properties/qm/realism-sem-challenge/selection-units/bolzano-logic 等）、figdesc.html ×3（aristotle-de-motu/ecological-genetics/physics-Rpcc——均为路径形自引用，fetch_audit 裸引用闭包盲区，en_integrity 捕获）、ibn-sina-logic/fig4.svg、mally-deontic/matrix3.png+matrix5.png、time-travel-phys 补充图 3 svg、epistemic-game/supplement.html、**russell 词条 legacy 媒体 6 件（desire/politics 的 .au/.qt/.wav）**。
* **fetch_audit 闭包语义定稿**：扩展名枚举（png/pdf/js/css…）曾漏掉 russell 的 .au/.qt/.wav 媒体引用——改为**文件名形状判定**（`[A-Za-z0-9][A-Za-z0-9._-]*\.[…]`）：一切形如文件名的裸引用皆词条包资产，锚点残留/实体残片/纯词不收。tools/tests/test_fetch_audit.py 三项（媒体收编、注释/实体/站点框架排除、垃圾形态排除）。
* **en_integrity 缺省件感知**：与 fetch-audit-full.json 凭证联动——fetch_audit 已探明上游 404 的缺省件（pineal-gland 撤稿页 6 图、scientific-explanation/local.js）由硬发现降为信息级 default_absent；本轮终态 default_absent=0（并行会话重抓撤稿页后引用已消失，两证据收敛一致）。
* **结论**：镜像复核门禁已在 intake 并发窗口下实测收敛；新词条包落库即被下一轮扫描捕获，补抓后归零——「扫描→补抓→重扫」闭环可持续例行化。

## wisdom 改判冲突复核与恢复 — 2026-10-28（复核三）

* **冲突**：c75cc794 依"软 404 检测"删除 wisdom（SUMMARY 行+mu-lu-s 行+w/wisdom.md+基线登记），与同批保留的 5 条撤稿词条（pineal-gland 等）同案异判，且与用户已批准的"6 条撤稿词条保留"裁定相悖。
* **事实更正**：6 条的 /entries/<slug>/ URL **全部**为软 404（HTTP 200+错误页正文）；"HTTP 200=词条在线"对六条均不成立。六条保留的真实共同依据是**归档版基线**（--archive-edition，见 entries.json archive_edition 字段）。
* **处置**：恢复 wisdom 全部四处登记（SUMMARY/mu-lu-s/w/wisdom.md/baseline，归档版 fall2023 重抓 upsert），裁定文档 wisdom 行改回保留并加事实更正块。六条同案同判；REMOVE 候选余 6 条（即六条撤稿保留项），逐条裁定见 contents-removal-adjudication.md，下一次 report 重生成时以裁定文档为准。

## 数学公式专项复核（用户指令「重点复核数学公式」）— 2026-10-28

* **en/ 侧（script/tmp/math_audit.py 一次性深扫，凭证 specs/001-sep-sync-pipeline/math-audit-en.json）**：全库 1878 词条——行内公式 142,357 个、显示公式 5,712 个、`$$` 2 对，MathML 标签 0（纯 TeX 定界）；MathJax 引用 887 处全部为站点级 `../../MathJax/`（TeX-MML-AM_CHTML ×782、TeX-AMS-MML_HTMLorMML ×105，lewis-metaphysics/reduction.html 为同域绝对 URL 同型），**零外部 CDN、零词条内 MathJax**；公式图片资产 7 件（frege-logic supp-begriff ×6、determinism-causal dome_with_eqn.gif）全部在包。
* **7 个定界符奇偶失衡词条逐一判定**：causation-probabilistic/connectives-logic/proof-theory 为公式内容内 TeX 行距序列 `\[..]`（排除后完全配平，非缺件）；common-knowledge `i\)`、discourse-representation-theory `[K']h\)`、nonexistent-objects 注 32 以裸 `)` 代 `\)`、phil-bio-latin-america `Kuhn (1962 [1970\)`——**四处均为上游内容笔误**，镜像逐字节忠实（baseline 哈希已验），MathJax 对未配对定界符忽略不渲染，零信任不改上游内容，仅登记。
* **yuanwen 侧 check_math 全量（1878 词条 / 130,333 公式）**：missing 2 → 逐条核实均为门禁口径误报——上游未闭合定界符使贪婪抽取跨块吞标签生成不可信期望串，而产物实际忠实（nonexistent-objects 注 32 连笔误都逐字保留；typelogical-grammar `*B* ⊗ *A*` 在产物 2 处）。
* **check_math 判定精度修补**（tools/check_math.py + test_check_math.py 11 项）：新增 `classify_formula`——内容逐字命中→ok；期望串以标记开头且跨块（前缀不可核对）→warning `[unclosed-delimiter]`（登记不拦截）；**标记前内容可核对且缺失仍判 missing 真失真**。修补后全量 missing=0、退出码 0；unbalanced 872 = 871 已知货币 `$` 启发式警告 + 1 unclosed-delimiter 登记。凭证 specs/001-sep-sync-pipeline/check-math-full.json。
* **结论**：数学公式在 en/ 抓取层零缺件、零损坏（4 处上游笔误如实镜像）；在 yuanwen 转换层 130,333 公式零丢失；离线渲染依赖站点级 MathJax（按契约有意不抓，联网即渲染）。check_all 九门禁全绿。

## 翻译规则补充（用户裁定两条，ADR-0011）— 2026-10-28

* **用户裁定（2026-10-28）**：① SEP 引用的原文若是中文或日语，译文优先使用中文或日语（不以英译回译；无法可靠还原时照录英译并译注）；② 参考文献若是中国文献（无论古代现代）一并译为中文。依 rules/06 程序先立 [ADR-0011](../../rules/adr/0011-引文原文语言与中文文献翻译.md)，再修订 rules/02:42（参考文献照录不译 → 非中文条目照录、中国条目翻译）与 rules/07（节首样文改为「非中文文献从原文照录，不作翻译；中国文献译为中文。」并新增「引文原文语言还原」条款）。
* **幻觉禁令照旧**：中文条目回译只能依据英文源所载信息与可核实文献，存疑处译注；标点体例仍按 rules/02 弯引号（不因日语原文引入直角引号）。
* **机检兼容**：check_academic 的 biblio-note 门禁只要求节首说明含「照录」，新样文兼容，无需改门禁。done=0 无存量改译负担，在途与后续词条自本 ADR 起执行。

## 参考文献优化建议全面落地（用户「复核后全面批准」）— 2026-10-28

* **biblio_analysis 报告十项建议全部实施**（结构盘点：1878 词条 232,608 条文献、文献节溶解为 References（引用注释）+ 文末脚注定义、中国文献三口径 33/173/283）。
* **tools/biblio_audit.py 转正**（原 script/tmp 分析脚本）：实体解码修复（上游汉字以 &#…; 实体编码，原始字节扫描曾漏检 confucius 等 33 词条）、典籍专名/作者位拼音双探针去噪、`probe_text()/likely_chinese()` 可导出；4 项单元测试。
* **check_academic 两条软告警**：biblio-note-outdated（节首样文为 ADR-0011 前旧措辞）、biblio-chinese-untranslated（疑似中国文献条目仍全罗马化，--strict 升硬）；BIBLIO_HEADINGS 收录 `References（引用注释）` 现制节名。
* **check_style 豁免细化**：BIB_HEADING_RE 扩展 References（引用注释）形态；文献节内**非中文行豁免、含汉字行（还原的中国文献）按正体例检查**。
* **ADR-0011 实施细则追加**（五条）：条目现制位置、著录格式标准（西文骨架+汉名/中文书名括注还原、通行简体、链接不动）、幻觉防线三来源（上游汉字/登记册通行名/条目英译括号）、古典学编号中文形态（(Analects 2.3)→《论语》2.3）、机检配套。
* **rules/07**（:17 现制形态与著录示例、:18 典籍编号中文形态、:22 结构完整性措辞、检查节 biblio_audit 指引）与 **rules/02**:43 对齐；**yi-zhe-shuo-ming.md** 新增「文献译名」区（典籍通行名 15 条种子 + confucius 上游汉字实证 3 条）并废止旧政策「参考文献条目一律不译」；**session-handoff.md** translate 行纳入 s1 文献还原作业与 chinese-* 簇工作量提示。
* 红灯归属说明：test_term_harvest 一项失败为并行会话 specs/008 未提交在途工作（term_harvest.py 未跟踪），与本次改动无关；本次新增/既有测试 139 项全绿，check_all 其余八门禁全绿。
