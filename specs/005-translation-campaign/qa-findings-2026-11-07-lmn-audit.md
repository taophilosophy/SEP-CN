# L–N 批进度对账与纠正记录（2026-11-07）

**会话**：LMN-main-20261106　**范围**：`l/` `m/` `n/` 三批共 333 条正式词条（L 144 / M 139 / N 50）
**方法**：五方对账——SUMMARY 词条 × 成稿（行数/汉字/节/尾节）× 任务 JSON（状态机）× 段落账本（段数与 step2 填充）× git 最后改动。工具：`script/lmn_audit3.py`、`script/tmp/*`（`script/` 为草稿区，结论以本文件为准）。

## 1. 对账结论（2026-11-07 00:0x UTC 基线）

| 字母 | 正式词条 | 已成稿 | done | s3_checked（待复审） | 在途 | pending 任务 | 未建任务 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L | 144 | 18（12.5%） | 2 | 16 | 0 | 1 | 125 |
| M | 139 | 5（3.6%） | 3 | 2（原 cleared） | 0 | 9 | 125 |
| N | 50 | 0 | 0 | 0 | 0 | 2 | 48 |
| 合计 | 333 | 23（6.9%） | 5 | 18 | 0 | 12 | 298 |

* 结构零偏差：有稿 23 条与有稿任务 23 条一一对应，无“有稿无任务/任务超前于成稿”。
* M 计数：SUMMARY 中 m/ 有 190 行（139 正式 + 51 别名行），progress.py 口径为 139，正确。
* 批次注记污染已修：`ledger.json` 的 m/n 注记原混入“l 批任务 19 已建”句（复制粘贴），已按实核重写；l/m/n 认领转交 `LMN-main-20261106`。

## 2. 偏差与处置

1. **在途状态滞后（M 2 条）**：`modesty-humility`（账本 91/91）、`montesquieu`（57/57）已 compose 成稿但状态停在 `cleared`。处置：核验守恒门与 compose 一致性后推进 `draft → s1 → s2 → s3`，见 §3。
2. **`lq.py map_related` 子节名歧义（新发现）**：源文相关词条 `Chinese Philosophy: ethics` 走“父: 子”分支时，子节名 `ethics` 与 `a/african-ethics` 的英文名同为 `ethics`，候选消解失败后落回通用循环取首个同名命中，误映射为“非洲伦理学”。处置：本批手工改为“中国哲学中的伦理学”；**工具未改**，列债务 §4。
3. **标题/别名术语错位**：`modesty-humility` 原题“谦虚与谦逊”把 modesty/humility 混作同义词对，正文却严格区分（谦逊 59 处 / 谦卑 39 处），别名行又把 humility 标成“谦逊”。处置：H1+SUMMARY+mu-lu-s 统一为“谦逊与谦卑”，别名行改“谦卑——见谦逊与谦卑”，术语表登记 modesty/humility/intellectual humility 三行。
4. **OIR 链接全角右括号**：`montesquieu` 两条其他网络资源链接用 `）` 收尾，Markdown 链接不闭合。处置：改 ASCII `)`。
5. **老批次参考文献形态**：`lady-masham` 用 `## 参考文献` 且缺 `### Sources/### Studies`，与 done 标准（`## References（引用注释）`+注记+源子标题照录）不符。处置：归正。
6. **prose 实修**：`montesquieu` 第 80 行 de-chain 1 处拆句；其余条目待逐条复审。

## 3. 已完成（2026-11-07）

* `m/modesty-humility` → **done**（48fb6052 + 15984f4c）：91 段零数字差、defs 73=73、相关词条 10 项（修 1 项误映射）、标题与别名纠正、术语 3 行、人名 12 行；全九步四检全绿。
* `m/montesquieu` → **done**（a4af969d + 15984f4c）：57 段、defs 23=23、引文 9 封信 + SL 36 处逐句核销、OIR 链接修复、de-chain 实修 1 处、人名 8 行；全九步四检全绿。
* **L 批 16 条 s3_checked 全部 r1–r3 复审完成 → done**（575a72a9、76701b29、c5b96d78、69218e52、06b2c2bf、09459510、01215838、dcfdfbd5、e791efca、1cc3b3cf、865a72fd、82a9824d、1fe50ddf、2f18eb77、6e581b23、e322e918）：
  * 共性缺陷：参考文献节多为旧形态（`## 参考文献`、缺转换器注记、缺源文子标题），统一归正后 marker/defs/节数三齐。
  * 真缺陷：`lady-masham` 缺 Sources/Studies；`lawphil-theory` 缺三子节；`leucippus` 缺 Texts/Secondary；`leibniz-modal` 记号 `L*`/`L**`/`W*` 与斜体标记连写产生伪粗体（改行内代码，style 12→0）；`lambert-auxerre` 错字“兰伯持”+相关词条；`leibniz-ethics` 三处漏译残留（intense/embodied/confirm，已用 `script/tmp/scan_mix.py` 全库同型复扫）；`locke-on-medicine` 引注 `p150.52` 归一。
  * prose：叙事句一律实修（每条 1–14 处），引文/引块按 ADR-0020 豁免并逐条留痕（合计约 120 项，分布见各条 r2 evidence）。

**批次计数（2026-11-07）**：L done 18/144（余 126 未建任务），M done 5/139（余 9 pending + 125 未建），N done 0/50（2 pending + 48 未建）。

## 4. 债务登记

* **map_related 歧义未修**：凡是源文相关词条形如 `X: y` 且子节名 `y` 与其他词条英文名同形（如 `ethics`、`mind`、`language`），都可能误映射。建议修法：`父: 子` 候选消解失败时，先按父名 token 匹配 slug 片段（`chinese`→`ethics-chinese`），再回退；不得直接落回全局首个同名。修复前各批 s1 必须人工复核“相关词条”整行。
* **中英残留机检缺口**：`check_prose` 与既有混杂启发式（一行 ≥3 拉丁词）都漏掉“汉字 + 单个英文词 + 汉字”形态（leibniz-ethics 的 intense/embodied/confirm 三例）。已补 `script/tmp/scan_mix.py`（汉字-拉丁-汉字相邻扫描），建议并入 r1 标准检查清单。
* **记录纪律**：`task_ops advance --evidence` 文本中禁止出现反引号（Bash 会当作命令替换并吞掉内容，2026-11-07 leibniz-modal r1 事故已订正）。

## 5. 接管复账（2026-11-07 15:0x +08，LMN-main-20261107）

**起因**：用户指派本会话接手 L–N 三批翻译，先复算并同步进度、纠正账实。

**五方复算**（`script/lmn_audit4.py`：SUMMARY 正式词条 × 成稿行数/汉字 × 任务 JSON 状态 × 账本段数与 step2 × git 最后改动）：

| 字母 | 正式词条 | 已成稿 | done | 在途 | pending 任务 | 未建任务 |
| --- | --- | --- | --- | --- | --- | --- |
| L | 144 | 18 | 18 | 0 | 1（langer） | 125 |
| M | 139 | 5 | 5 | 0 | 9 | 125 |
| N | 50 | 0 | 0 | 1（neoplatonism） | 2 | 47 |
| 合计 | 333 | 23（6.9%） | 23 | 1 | 12 | 297 |

* **账实零偏差**：无「有稿无任务」「done 无稿」「成稿状态滞后」三类偏差；§1–§3 的对账结论在复算时点依然成立（L 18 / M 5 / N 0 done）。
* **新增在途（前会话中断遗留，未提交）**：`n/neoplatonism` 任务 `cleared`（2026-11-07T02:03Z 创建，baseline gate hash_ok），账本 43 段已填 24 段（step1/step2 双版齐，`lq.py check` 除 25–43 缺失外无 HARD 项）；成稿仍为占位单行。本会话收编为在途件，账本提交为检查点。
* **认领转交**：l/m/n 三批 `claimed_by` 由 `LMN-main-20261106` 改为 `LMN-main-20261107`（中断会话交接）。
* **PROGRESS 重生成**：done 165、在途 242（含他会话新增任务，与 L–N 计数无冲突）。
* **收编件收口（2026-11-07 同日）**：`n/neoplatonism` 续译 25–43 段 → compose（14110 字符，8 节与源同构，defs 33=33、marker 34=34）→ s1 逐段核销（人名归正 4 处、相关词条 21 项）→ s2（prose 35→0）→ s3（术语 8 行＋人名 13 行登记）→ r1–r3 → **done**。N 批 done 0→1。
* **并行收编留痕**：s3 检查点（账本 43 段双版、成稿、登记行）被并行会话提交 9e6f51d7 一并收编，内容核对无覆盖；r1–r3 与终态由 252cc89f 补记。
* **本批下一步**：①续译 neoplatonism 余 19 段（25–43）→ compose → 三审三校收口；②清 pending：langer、M 9 条、N 2 条；③对 297 条未建任务按字母序建任务并翻译。

## 6. 接手复账（2026-11-08，LMN-main-20261108）

**起因**：用户指派本会话接手 L–N 三批，先复算同步、再续译。

**五方复算**（`script/lmn_audit4.py`）：

| 字母 | 正式词条 | 已成稿 | done | 在途 | pending 任务 | 未建任务 |
| --- | --- | --- | --- | --- | --- | --- |
| L | 144 | 18 | 18 | 0 | 1（langer） | 125 |
| M | 139 | 6 | 6 | 1（moral-demands-permissions，cleared，账本 45/63） | 7 | 125 |
| N | 50 | 1 | 1（neoplatonism） | 0 | 2 | 47 |
| 合计 | 333 | 25（7.5%） | 25 | 1 | 10 | 297 |

* 对 §5 基线变化：M done 5→6（`moral-responsibility-empirical` 于 2026-11-07T14:38Z 收口）；N done 0→1 已在 §5 记载；新增在途 `moral-demands-permissions`（账本 p4 段 33–45 落盘后暂停，余 46–63 共 18 段）。
* **账实零偏差**：无「有稿无任务」「done 无稿」「成稿状态滞后」；pending 12→10（2 条已续作）。
* 同步动作：PROGRESS.md 重生成（done 177 / 在途 242）；l/m/n `claimed_by` 转交 `LMN-main-20261108`。
* 本批下一步：①续译 moral-demands-permissions 段 46–63 → compose → 三审三校收口；②清 pending 10 条（langer、M 7、N 2）；③297 条未建任务按字母序建任务并翻译。


