# Q-R 批全流程翻译协议（2026-11-09，QR-main-20261109）

**上位依据**：`rules/04-translation-workflow.md`（状态机/六道）、`rules/02-style.md`（体例）、`rules/03-terminology.md`（术语）、`rules/07-academic-norms.md`（学术规范）、`specs/005-translation-campaign/fan-yi-mu-ban.md`（模板 v1.4，§2 元素映射/§4 骨架/§6 账本协议）、`specs/005-translation-campaign/k-batch-subagent-protocol.md`（母协议，本文件为其 Q-R 化变体）
**范围**：q 批 34 条 + r 批 85 条（其中 r 已 done 8 条、religion-epistemology 在途已 draft），剩余 111 条。任务 JSON 已由 Lead 全部建齐（pending）。
**队列**：`specs/005-translation-campaign/results/qr-queue-20261109.json`（按源文词数平衡切 6 块；块内按词数升序，先小后大验证管线）。

## 1. 角色与边界（ISO 17100 复核独立性）

| 角色 | 做什么 | 不做什么 |
| ---- | ---- | ---- |
| 译者（teammate） | 每词条 `clear → draft → s1 → s2 → s3`，状态推进到 `s3_checked` | 不做 r1/r2/r3/done；不提交共享登记册 |
| 复核员（teammate） | 每词条 `r1 → r2 → r3 → done`，独立于译者 | 不改初译底稿以外的他人词条；不做 draft/s1–s3 |
| Lead | 建任务、登记册收口提交、批次账本、全库门禁、抽查、纠偏 | 不代译者做初译 |

**复核独立性**：r1–r3 必须由**初译 actor 以外**的成员执行；r2 起至少要有一个跨成员复核记录。译者与复核员都不写 `r1/r2/r3` 中的对方步骤。

## 2. 每词条标准作业（严格按序）

```sh
# 0. 断点
python tools/task_ops.py show <slug>

# 1. 清空（pending→cleared；仅保留 H1，基线哈希门禁自动校）
python tools/task_ops.py clear <slug>

# 2. 账本骨架（source 逐字符取自 yuanwen，含 kind=body/oir/ack/note）
python script/lq.py init <letter> <slug>
python script/qr_merge.py <letter> <slug> --status    # 看未填段 id

# 3. 初译：读 yuanwen/<letter>/<slug>.md，按 20–40 段一批写片段文件
#    script/parts/<letter>-<slug>-p1.yaml（格式见 §3），然后合并：
python script/qr_merge.py <letter> <slug> script/parts/<letter>-<slug>-p1.yaml
#    重复 3 直到 --status 显示未填 0/112

# 4. 前置门（HARD 必须 0，否则禁止写回）
python script/lq.py check <letter> <slug>

# 5. 成稿（写回 <letter>/<slug>.md：H1+版本行+正文+脚注+文献+工具+其他+相关+致谢）
python script/lq.py compose <letter> <slug> --write

# 6. 中文强调斜体→加粗（仅中文；拉丁斜体保留）
python script/italic_to_bold_cjk.py <letter>/<slug>.md

# 7. 四检
python tools/check_style.py <letter>/<slug>.md                  # 0 issue
python tools/check_prose.py <letter>/<slug>.md                  # 告警逐条改或豁免
python tools/check_math.py <slug>                               # missing/unbalanced 空
python tools/check_academic.py --docs <letter>/<slug>.md --strict  # 0 硬错误

# 8. 八步推进（每步 evidence 写实：账本段数、HARD 数、门禁输出、修了什么）
python tools/task_ops.py advance <slug> --step draft --actor <你的名字> --evidence "…"
python tools/task_ops.py advance <slug> --step s1    --actor <你的名字> --evidence "…"
python tools/task_ops.py advance <slug> --step s2    --actor <你的名字> --evidence "…"
python tools/task_ops.py advance <slug> --step s3    --actor <你的名字> --evidence "…"   # 学术门禁自动挂钩

# 9. 提交（只用 pathspec；命中 index.lock 等 5 秒重试，最多 5 次）
git commit -m "Q-R：<slug> 落盘 r0 初校（<你>）：…" -- <letter>/<slug>.md tasks/<letter>/<slug>.json tasks/<letter>/<slug>.ledger.yaml
```

**draft 之后禁止再 `compose --write`**（会抹掉 s1–s3 的手工修正）；后续一律在 `<letter>/<slug>.md` 上逐处手改，账本保留 draft 时点状态（模板 §6.4）。若确需重建账本，须先把成稿 diff 全量回放。

## 3. 账本片段写法（step1/step2 双版，ADR-0021 强制）

`script/parts/<letter>-<slug>-pN.yaml`，与账本段同格式（勿写 `segments:` 头）：

```yaml
- id: 12
  step1: |-
    忠实初译：只译不改，不补不删，长句照原句法。
  step2: |-
    语言优化：在 step1 上消欧化、顺口吻、拆长句；不引入新信息。
```

要点：

* **逐段对位**：id 必须与 `qr_merge --status` 的未填 id 对齐；段数不得增删（增删点＝错位事故）。
* **双版必须不同**：step1 忠实、step2 润色；两者相同＝反思步缺失。
* **守恒**：`[^note-N]` 键、`$`、`**` 计数逐段与源一致（`lq.py check` HARD 门）；源文斜体词在 step2 里**不要**改加粗（`**` 计数漂移即 HARD）。
* **数学**：`$…$`/`$$…$$` 内 LaTeX **逐字符照录**，只把 `\(\)`/`\[\]` 定界符换成 `$`/`$$`；`<sub>/<sup>` → `_{x}`/`^{x}`。
* **不译区**：引用组 `(Author year, p. X)`、URL、代码、DK/Ak./AA 等编号、参考文献非中文条目。
* **长段可拆批**：同一 id 可在后续片段里重写（后者覆盖前者），但不要写空。

## 4. 体例硬点（rules/02，违规即返工）

* 中文弯引号 `“ ”` `‘ ’`；禁英文直引号、直角引号、全角直引号。
* 中英文/中文数字间半角空格；书名号内中英混排也加空格；`**` 内侧禁空格。
* 中文强调用 `**加粗**`，不用 `*中文斜体*`；拉丁/希腊术语保留斜体。
* 禁 HTML；表格居中 `:---:`、紧凑；段落不换行。
* 第二人称用“你”；不滥用“已”；不机械直译欧化句（rules/02 反欧化 12 条）。
* **H1 = SUMMARY 该行方括号内文字原样**（`# 中文名 English-name (Authors)`）。本库既有标题形可能是英文片段（如 `宗教认识论 epistemology of`），属既定约定，**不得“修正”**；发现确需改标题，报告 Lead 处理 SUMMARY/mu-lu-s。
* 版本事实行由 compose 从 baseline 生成，不改日期。
* 尾部节序固定：`## 脚注`（有则）→`## 参考文献`→`## 学术工具`→`## 其他网络资源`→`## 相关词条`→`## 致谢`（有则，源无则整节省略）。
* 参考文献：非中文条目照录；**中国文献条目译为中文**（ADR-0011），保留著录骨架与 `[^key]`。
* 相关词条行：compose 从 SUMMARY 映射；`NOTE 相关词条未匹配` 的项在 s1 逐条回 SUMMARY 核对并手改。

## 5. 术语与人名登记（先登记后使用）

* 查 `yi-zhe-shuo-ming.md`（术语，六列）/ `ren-ming-biao.md`（人名，八列）有无；有则照用，同词条内锁定主形。
* 无则先登记：写 `script/qr_rows_<slug>.py`：

  ```python
  SLUG = "<slug>"
  TERM = [("supervenience", "随附性", "学界通行译名；凭证 2026-11-09"), ...]
  PERSON = [("Williamson, Timothy", "蒂莫西·威廉姆森", "学界通行汉名；凭证 2026-11-09", "英国", "1955–"), ...]
  # PERSON 可 3/4/5 元组：3 元组籍属/年代留「—」（欠账），5 元组填全
  ```

  然后 `python -B -I script/reg_tool.py qr_rows_<slug>`（**不加 --stage**；登记册由 Lead 统一提交）。
* 依据档位：知网系权威源 → 权威译本通行译法 → 学界惯例；**禁维基**；查无则保留英文并登记。
* 禁自造译名；不确定时在报告里列“待裁定”，正文先用英文原名。

## 6. 报告格式（每完成一条词条，用 send_message 报 Lead）

```
<slug> s3_checked | 账本 N 段（body/oir/note）| HARD 0 | compose X 字符
四检：style 0 / prose 告警 a 修 b 豁免 c / math 0 / academic --strict 0
术语新增 n：…（已 reg_tool）| 人名新增 m：…
异常：…（无则写“无”）| commit <hash>
```

**每完成 1 条必须报一次**；Lead 据此记账、提交登记册、抽查。连续完成 4 条或上下文吃紧时，报告后**停下等指令**（Lead 会给下一批或换人）。

## 7. 不得为（违者返工+记档）

* 不 push、不 force、不改 `baseline/`、`en/`、`yuanwen/`、不造备份文件。
* 不动他人词条/批次文件；不改 SUMMARY.md、mu-lu-s.md、PROGRESS.md（报告 Lead）。
* 不跑 `check_all.py`（全库门禁由 Lead 跑；在途文件会让它红）。
* 不批量替换、不跑格式化工具代替判断；不静默跳过（抓取/核对失败必须记录）。
* 不伪造 evidence；不把“工具跑过”当完成证据，验收看六道与门禁输出。

## 8. 中断与续作

* 任何一步中断：`task_ops.py show <slug>` + `qr_merge --status` 即断点；账本片段文件可续写合并（幂等）。
* 已完成 draft 但未 s1 的词条：从 §2 第 7 步的对应门禁续作。
* 发现账本/成稿错位（段 id 不齐、markup 漂移）：回 `lq.py init` 重来，不硬修。

## 9. 分块与派发

| 块 | 条目数 | 源文词数 | 队列文件位置 |
| ---- | ---- | ---- | ---- |
| 1 | 18 | 300,526 | `qr-queue-20261109.json` chunks[0] |
| 2 | 19 | 304,130 | chunks[1]（含在途 religion-epistemology，见下） |
| 3 | 19 | 304,583 | chunks[2] |
| 4 | 18 | 297,263 | chunks[3] |
| 5 | 19 | 304,646 | chunks[4] |
| 6 | 18 | 297,223 | chunks[5] |

读取自己的队列：

```sh
python -c "import json;d=json.load(open('specs/005-translation-campaign/results/qr-queue-20261109.json',encoding='utf-8'));[print(e['letter'],e['slug'],e['words']) for e in d['chunks'][N-1]['entries']]"
```

**在途件 religion-epistemology（r 批，chunk 2）**：任务已 clear、账本 56 段双版已填、`r/religion-epistemology.md` 已成稿，但 state 仍 cleared。接手者：`qr_merge --status` 确认 0 未填 → `lq.py check` → `compose --write` → 四检 → advance draft/s1/s2/s3。
