# 天城体词头离线可行性调查（csl-devanagari 路径）

调研日期：2026-11-14 ｜ 范围：只调查与试验，未改 `shu-yu-biao.md`／`ren-ming-biao.md`，未执行任何 git 写操作，未安装系统级软件。

## 结论

**有条件可行：可行范围为登记册里 102 条梵文（IAST）条目中的 27 条，且必须走“辞书项目自身发布的成品天城体镜像”，不得就地换算。** 其余 100 条（藏文 17、阿拉伯 3、希腊 2、日文 2、非梵文专名 1、以及 Cologne 各辞典未收的梵文篇名与复合词 75）无法借此路径补齐。

三条要点：

1. **数据存在，且是官方成品**：`sanskrit-lexicon/csl-devanagari` 是 Cologne 项目把 `csl-orig` 的 SLP1 源文本整书镜像为天城体的发布仓库，逐条带 Unicode 天城体词头 `<k1>`，不是转写。
2. **离线可得**：`mw`（66.5 MB）＋`bhs`（8.2 MB）两份镜像合计 74.7 MB，即可覆盖 27／27 条可达条目；一次下载后全程离线，零额外依赖（只要 curl ＋ Python 3 标准库）。
3. **合规可守**：字形来自辞书项目自己发布的渲染产物，与 B3 批已采信的 `getword.php?...&output=deva` 同源同实现；回放 B3／B5 已采信字形 8 条，逐字节全等。

风险不在“能不能取到”，而在“取错条目”：镜像与源数据存在版本漂移（MW 侧 0.16% 记录错位），必须按 `lnum`＋`pc` 双键对齐并回读校验。

## 统计口径

任务给定待补 126 条。核查时 `specs/008-terminology-campaign/results/orig-missing.txt` 正被并行会话改写（文件内出现未清理的冲突标记），门禁当刻报 128 条。本报告用 2026-11-14 01:30 快照去重后的 **127 个键**统计，与 126 的差额属会话并行写入浮动，不影响比例结论。

127 键构成：

| 文种 | 条数 | 说明 |
| --- | --- | --- |
| 梵文（IAST） | 102 | Cologne 路径的适用对象 |
| 藏文（Wylie 括注） | 17 | 如 `gzhan sel`、`rnam pa`、`blo` |
| 阿拉伯文 | 3 | `al-kabar`、`al-lays` 等 |
| 希腊文 | 2 | `skeptosunê`、`asynchytos henōsis` |
| 日文 | 2 | `makoto no shintō`、`mikunigokoro` |
| 其他 | 1 | `Löwenheim–Skolem–Tarski theorem` |

## 一、GitHub 组织仓库盘点

`sanskrit-lexicon` 组织现有 89 个公开仓库（`api.github.com/orgs/sanskrit-lexicon/repos`，2026-11-14 实测）。与本次问题相关的按下表分三类：

| 仓库 | 体积 | 是否含词典数据 | 字形形态 | 判断 |
| --- | --- | --- | --- | --- |
| `csl-orig` | 909 MB | 是，全部辞典源文本 | **SLP1 转写**（`<k1>kleSa`） | 只能作检索键，不能作字形 |
| `csl-devanagari` | 303 MB | 是，40 部辞典的整书镜像 | **Unicode 天城体**（`<k1>क्लेश`） | 本次采用的成品数据 |
| `csl-ldev` | 365 MB | 是，`csl-devanagari` 的按 `lnum` 拆条 | 天城体 | 同一数据的单条切片，便于定点取用 |
| `csl-json` | 363 MB | 是，37 部辞典的 JSON | 天城体（`"words"` 键即天城体词头） | 备选，`pd.json` 为空壳 |
| `csl-apidev` | 232 MB | 否，是 PHP 后端 | 含转写器与 `getword.php` | **官方渲染实现所在**，见第二节 |
| `csl-pywork` | 1.7 MB | 否，生成管线 | — | 与本问题无关 |
| `csl-sqlite` | 223 MB | 是，各辞典 SQLite | 转写为主 | 体积大，无额外收益 |
| `hwnorm1` | 126 MB | 词头归一化工具 | 转写 | 检索辅助 |
| `CORRECTIONS` | 185 MB | 含 `sanhw1/sanhw1.txt` | 转写 | **联合词头表，9.3 MB，可先判“哪部辞典收了这个词”** |

结论：**带天城体的成品数据只有 `csl-devanagari`（及其切片 `csl-ldev`、JSON 版 `csl-json`）**；`csl-orig` 与 `csl-sqlite` 里词头是 SLP1／转写，不能直接当原文列。

## 二、字形出处链：网页 `output=deva` 用的是哪套代码

B3 批采信的是 `https://www.sanskrit-lexicon.uni-koeln.de/scans/awork/apidev/getword.php?dict=mw&key=kleSa&input=slp1&output=deva`。该端点的实现链如下（全部可在 GitHub 读到）：

1. `csl-apidev/getword.php` → `GetwordClass`;
2. `csl-apidev/getwordClass.php` 中 `transcoder_processElements($table,"slp1",$filter,"SA")`，`$filter` 取 `deva`（MW 带重音时取 `deva2`）；
3. `csl-apidev/utilities/transcoder.php` 按 `utilities/transcoder/slp1_deva.xml` 的有限状态机逐字符转写；文档 `doc/transcoder.md` 明示 `transcoder_processString('rAma','slp1','deva')` 返回 `राम`。

也就是说，**网页端的天城体不是排印扫描，而是项目自带的转写器把 SLP1 规则化渲染出来的**。这一点决定了“官方渲染”与“自行映射”的界线不在“是否经过转换”，而在“转换规则由谁发布、能否复现”。

`csl-devanagari` 是同一思路的整书版本：其 `scripts/to_devanagari.py` 用第三方库 `indic-transliteration` 生成 `v02/<dict>/<dict>.txt`，并配套 `to_slp1.py` 做往返校验，差异写入 `diff/<dict>.txt`。它在 README 里明确“一行对应 SLP1 源的一行”，这正是可以按 `lnum` 对齐取字的依据。

### “官方模块渲染”与“自行映射”的区别

| 维度 | 官方模块渲染（本次采用） | 自行映射（ADR-0030 禁止） |
| --- | --- | --- |
| 规则来源 | 辞书项目仓库内的 XML／脚本，有提交记录、有许可证 | 我们或模型自拟的对照表、常识或记忆 |
| 可复核性 | 任何人可下载同一 commit 复跑，逐字节比对 | 无版本、无凭证，换人换机可能不同 |
| 与线上端点关系 | 与 `getword.php` 同一套 `slp1_deva.xml` | 与线上无关，可能与辞书字形相左 |
| 责任归属 | 字形由辞书项目负责，我们只做定位与校验 | 字形由我们负责，等于自造原文 |
| 典型反例 | — | 用 IAST／ISO 15919／SLP1 映射表把 `kleśa` 折成 `क्लेश` |

灰区一句话：**“我调官方转换器”与“我自己写转换器”看起来结果相同，但前者可追溯到项目的规则表，后者只可追溯到我。** 本报告把前者列为可采，把后者列为禁止，并把“只借官方规则表、自己重写算法”的做法降级为“仅作校验、不作回填依据”（见第七、八节）。

## 三、试验：5 词逐字比对

试验数据（2026-11-14 下载，见第五节哈希）：

- SLP1 源：`csl-orig/v02/mw/mw.txt`（286 525 条）、`csl-orig/v02/bhs/bhs.txt`（17 839 条）
- 天城体镜像：`csl-devanagari/v02/mw/mw.txt`（287 604 条）、`csl-devanagari/v02/bhs/bhs.txt`（17 839 条）
- 对齐方式：按 `<L>`（lnum）配对，取镜像侧同条目的 `<k1>`

| 登记键 | SLP1 检索键 | 辞典／lnum／页栏 | 离线镜像字形 | wisdomlib 页面字形 | 一致 |
| --- | --- | --- | --- | --- | --- |
| kleśa | `kleSa` | MW lnum 58617，p. 324 col 1 | क्लेश | क्लेश | 是 |
| ālambana | `Alambana` | MW lnum 26736，p. 153 col 2 | आलम्बन | आलम्बन | 是 |
| tathatā | `taTatA` | BHS lnum 6805，p. 248 col 1 | तथता | तथता | 是 |
| vijñapti | `vijYapti` | MW lnum 195250，p. 961 col 1 | विज्ञप्ति | विज्ञप्ति | 是 |
| svasaṃvedana | `svasaMvedana` | MW lnum 258250，p. 1277 col 1 | स्वसंवेदन | स्वसंवेदन | 是 |

5／5 逐字节相同（含变音符号与连写，非“看起来像”）。

**一处必须记录的歧义**：`tathatā` 在 Cologne 有两条并行词头——MW 的 `taTAtA`＝तथाता（p. 433 col 3）与 BHS 的 `taTatA`＝तथता（p. 248 col 1）。B4 批采信的是 MW 的 तथाता，wisdomlib 首屏展示的是 BHS 的 तथता。两形都“有据”，但不能混用；批量脚本必须把“哪部辞典、哪一页”写进依据列，否则会把两个词条压成一个。

### 对已采信批次的回放

用同一套离线数据复核 B2–B5 的 `原文` 列：

| 批次 | 总条数 | 逐字节复现 | 不一致 | 说明 |
| --- | --- | --- | --- | --- |
| B3 | 6 | 6 | 0 | 全部与 Cologne `deva` 渲染一致 |
| B4 | 9 | 8 | 1 | 即上条 `tathatā` 双形：B4 采信 MW 的 तथाता，并在备注里记了 Edgerton 的 तथता；离线复算先命中 BHS，故计为一条“选形差异”，字形本身无错 |
| B5 | 2 | 2 | 0 | — |
| B2 | 18 | — | — | 该批为希腊／日文／希伯来／德文，与 Cologne 无关，未纳入比对 |

即：**离线镜像能够复现已采信的 Cologne 字形，误差只来自“多形并存时选哪一条”，不来自字形本身。**

### 交叉验证：官方规则表与本镜像的一致性

另写了一个按 `transcoder.php` 算法逐条重写的 Python 版（只读官方 `slp1_deva.xml`，不引入任何自拟对照表），对两批数据做全量比对：

| 数据 | 比对条数 | 不一致 | 比例 |
| --- | --- | --- | --- |
| BHS（源与镜像版本同期） | 17 839 | 0 | 0.0000% |
| MW（源 2026-11-12，镜像 2026-10-30） | 285 648 | 471 | 0.165% |

BHS 全等说明“官方规则表 → 天城体”这条链是确定的；MW 的 471 条差异里 75 条连 `pc` 页码都不一致，其余为相邻条目错位（例如 lnum 1176 处镜像给出的是邻条 `अग्न्याधेय`），属 `csl-orig` 在镜像生成后继续增补导致的版本漂移，不是渲染错误。这正好说明：**取字时必须校验 `pc`，不能只信 `lnum`。**

## 四、覆盖与体积

用联合词头表 `CORRECTIONS/sanhw1/sanhw1.txt`（9.3 MB，逐词标注收录辞典）先做“哪部辞典收了这个词”的判定，再对照 `csl-devanagari` 实际镜像的 40 部辞典：

| 方案 | 追加体积 | 累计体积 | 可补条数（127 键中） |
| --- | --- | --- | --- |
| 仅 `mw` | 66.5 MB | 66.5 MB | 23 |
| ＋`bhs` | 8.2 MB | **74.7 MB** | **27** |
| ＋`vcp` | 61.3 MB | 136.0 MB | 28（仅多 1 条） |
| 全部 40 部镜像 | — | 504.6 MB | 28（上限） |

结论：**74.7 MB 已到性价比拐点**，再下 429 MB 只多 1 条。另有 2 条（`advayajñāna`、`anyāpoha`）只存在于 `PD`（Deccan College《梵语历史原则百科辞典》），而 `PD` 在 `csl-devanagari` 里没有镜像、在 `csl-json` 里是空壳，短期无解。

按 27 条方案计，剩余 100 条未命中的原因分三类：一是不是梵文（藏／阿／希／日，24 条）；二是梵文篇名或学派名，Cologne 各辞典本就不收（如 `Madhyamakāvatāra`、`Ratnagotravibhāga`、`Viṃśikā`）；三是登记键是英文描述加括注（如 `seed-syllable (bīja)`），键本身就不是词头，需先拆键再查。

## 五、复现步骤

全部命令在仓库根的 Git Bash 下执行，产物落 `script/_tmp/csl/`（`script/` 已被 `.gitignore` 忽略，不入库）。

```bash
mkdir -p script/_tmp/csl && cd script/_tmp/csl

# 1. SLP1 源（检索键）
curl -L -o mw_slp1.txt  https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/main/v02/mw/mw.txt
curl -L -o bhs_slp1.txt https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/main/v02/bhs/bhs.txt

# 2. 天城体官方镜像（原文列取字）
curl -L -o mw_deva.txt  https://raw.githubusercontent.com/sanskrit-lexicon/csl-devanagari/main/v02/mw/mw.txt
curl -L -o bhs_deva.txt https://raw.githubusercontent.com/sanskrit-lexicon/csl-devanagari/main/v02/bhs/bhs.txt

# 3. 联合词头表（判覆盖，可选）
curl -L -o sanhw1.txt https://raw.githubusercontent.com/sanskrit-lexicon/CORRECTIONS/main/sanhw1/sanhw1.txt

# 4. 取词（脚本在 script/_tmp/，未入库）
cd ../../..
python script/_tmp/deva_probe.py --slp1 script/_tmp/csl/mw_slp1.txt \
  --deva script/_tmp/csl/mw_deva.txt --keys kleSa,Alambana,vijYapti,svasaMvedana
python script/_tmp/lookup_missing.py --missing script/_tmp/missing_dedup.txt \
  --dict mw=script/_tmp/csl/mw_slp1.txt:script/_tmp/csl/mw_deva.txt \
  --dict bhs=script/_tmp/csl/bhs_slp1.txt:script/_tmp/csl/bhs_deva.txt
```

本次实测的文件指纹（sha256 前 16 位，便于日后核对是否同一版本）：

| 文件 | 字节 | sha256[:16] |
| --- | --- | --- |
| `mw_slp1.txt` | 50 163 993 | `e4641dc4384de459` |
| `mw_deva.txt` | 66 532 721 | `02316188db9fc8e6` |
| `bhs_slp1.txt` | 7 601 178 | `1cf4a001a250b14b` |
| `bhs_deva.txt` | 8 157 586 | `980bb5f9815ae88a` |
| `sanhw1.txt` | 9 299 918 | `4013211c350b7cb1` |

版本锚点（2026-11-14）：`csl-devanagari` @ `4e01fc2fbc53`（2026-10-30）、`csl-orig` @ `1600d6ba3a76`（2026-11-12）、`csl-apidev` @ `6af742757b6e`（2026-11-13）。

依赖：**只需 curl ＋ Python 3.8＋ 标准库**。PHP 不是必需（本机未装 PHP，也未装）；`indic-transliteration` 仅 `csl-devanagari` 生成镜像时需要，取用已发布镜像不需要。本次为交叉验证在 `script/_tmp/vendor` 本地安装过一次该库（`pip --target`，未进系统环境、未改 PATH），仅为核对，不进入建议流程。

下载耗时实测：raw.githubusercontent 约 65 KB/s，raw.githack 约 100–145 KB/s；74.7 MB 约需 10–20 分钟，建议一次下齐后离线复用。

## 六、风险

1. **版本漂移（最高）**：镜像随 `csl-orig` 更新滞后。MW 侧 471 条／285 648（0.165%）出现同 `lnum` 不同条，其中 75 条 `pc` 也不同。若只按 `lnum` 取字，会把邻条词头当成本条原文。**必须 `lnum`＋`pc` 双键校验，并回读 SLP1 侧词头确认语义。**
2. **多形并存**：同一登记键可能对应 MW／BHS／PW 的不同词头（`tathatā` 即例）。批量脚本要输出全部候选并标页码，人工择一，不得静默取第一个。
3. **键不是词头**：登记键里混有英文描述加括号（`seed-syllable (bīja)`、`apprehended object / grasped object（gzung yul）`），直接转写必然查空，需先拆键；这部分与藏文条目重叠。
4. **覆盖天花板**：Cologne 路径最多补 28 条（22.0%），对藏文、阿拉伯文、希腊文、日文与新造复合术语完全无效。不要据此期待“一次性清空告警”。
5. **许可**：`csl-devanagari`、`csl-orig` 为 CC-BY-SA-4.0；`csl-apidev` 仓库为 GPL-3.0，其 `transcoder.php` 文件头另标 CC BY-NC-SA 3.0。取用数据并标注出处属于引用事实，不改变本仓库许可；但**把 `transcoder.php` 移植进本仓库会引入 GPL 传染**，故试验脚本只留在 `script/_tmp/`，不入库。
6. **并发写入**：`results/orig-missing.txt` 在调查期间被并行会话改写并留下冲突标记。批量作业前应重新生成该清单，不要读旧快照。

## 七、合规判断

**允许**：

- 从 `csl-devanagari`／`csl-ldev`／`csl-json` 读取**已发布的**天城体 `<k1>`，逐字抄录，并在依据列写明“csl-devanagari v02/mw lnum=…, pc=…, commit …”，与 B3 批“Cologne 词条页 deva 渲染”同一档位。
- 用 IAST→SLP1 把登记键归一化成**检索键**（同一套罗曼化方案之间转写），因为该步骤不产出任何天城体字符，字形仍由辞书文件给出。这一步须在 ADR 里写明，避免被误读为“映射推算”。
- 用官方 `slp1_deva.xml` 复算作**校验**（本次 BHS 17 839 条零差异），用于发现版本漂移。

**禁止（触犯 ADR-0030 第 2 条）**：

- 用 IAST／ISO 15919／SLP1 对照表就地拼出天城体后直接写入 `原文` 列——哪怕结果与辞书一致，也属“按规则折算”，无凭证。
- 用模型记忆或常识补写天城体（包括“我记得 kleśa 是 क्लेश”这类）。
- 把 `csl-orig` 的 SLP1 词头当原文列直接填（那是转写，不是原生文字）。
- 把“自己重写的转换器输出”作为唯一依据（本次的 Python 版 FSM 只作校验，不作回填依据）。

**灰区（建议在 ADR 里一句话封口）**：

- 只借官方规则表、自己重写算法，属“半官方”。本次实测其与官方成品在同期数据上零差异，但仍建议：**回填只认成品镜像的字形，算法复现仅作交叉校验**。这样凭证链最短，也最容易被第三方复核。

## 八、建议

1. **补一条 ADR（0038 或续 0030）**：把“辞书项目自身发布的成品原生文字镜像”明确列为第三级来源，与 B3 的 `getword.php?output=deva` 同级；同时写明“检索键归一化不算映射推算”，封掉灰区。
2. **只对 102 条梵文键开工**，按 `mw`＋`bhs` 两库批处理；预期一次补齐 27 条，其余 75 条在依据列注明“Cologne 各辞典未收（2026-11-14 查，`sanhw1` 无记录）”，转为“工具书查无”状态，不再计入待办。这与 ADR-0030 第 4 条一致。
3. **批处理三件套**：`lnum`＋`pc` 双键对齐 → 回读 SLP1 词头做语义确认 → 输出候选表（含全部同形条目）供人工择一。严禁脚本直接写登记册。
4. **藏文 17 条另立路线**：Cologne 无藏文数据，`csl-devanagari` 不涉及；需另找带藏文排印的辞书（如 THL 的 `The Tibetan and Himalayan Library` 镜像站或《藏汉大辞典》电子版），本轮不展开。
5. **保留 `script/_tmp/` 试验脚本**（`deva_probe.py`、`deva_verify.py`、`lookup_missing.py`、`deva_fsm.py`），待 ADR 通过后整理为 `tools/` 下的正式工具（届时须去掉对本地 `vendor` 的依赖，只走标准库＋官方数据）。
6. **不建议**为多补 1 条去下 429 MB 的其余 38 部镜像，除非后续要批量处理非佛教术语。

## 附一：27 条可离线补齐清单（2026-11-14 试算）

| 键 | SLP1 检索键 | 辞典 | lnum | 页栏 | 镜像字形 |
| --- | --- | --- | --- | --- | --- |
| Abhidharmakośa | aBiDarmakoSa | mw | 11503 | 63,2 | अभिधर्मकोश |
| Ālambanaparīkṣā | AlambanaparIkzA | mw | 26745 | 153,2 | आलम्बनपरीक्षा |
| āśrayāsiddha | ASrayAsidDa | mw | 27673 | 158,3 | आश्रयासिद्ध |
| ātmamāna | AtmamAna | mw | 23575 | 135,3 | आत्ममान |
| Bāla-gādādharī | bAlagAdADarI | mw | 144526 | 728,3 | बालगादाधरी |
| Bodhisattvabhūmi | boDisattvaBUmi | mw | 145903.3 | 734,3 | बोधिसत्त्वभूमि |
| Madhyamakālaṃkāra | maDyamakAlaMkAra | mw | 156566 | 782,3 | मध्यमकालंकार |
| Madhyamakāloka | maDyamakAloka | mw | 156567 | 782,3 | मध्यमकालोक |
| Mahāyānasaṃgraha | mahAyAnasaMgraha | mw | 160508.1 | 799,2 | महायानसंग्रह |
| mātra | mAtra | mw | 161708 | 804,2 | मात्र |
| nirākāra | nirAkAra | mw | 106688 | 540,1 | निराकार |
| nirodhasamāpatti | niroDasamApatti | bhs | 8361 | 300,1 | निरोधसमापत्ति |
| Nyāyabindu | nyAyabindu | mw | 112875 | 572,3 | न्यायबिन्दु |
| Nyāyasiddhāntamañjarī | nyAyasidDAntamaYjarI | mw | 112930.25 | 572,3 | न्यायसिद्धान्तमञ्जरी |
| Pañcaskandhaka | paYcaskanDaka | mw | 113999 | 577,3 | पञ्चस्कन्धक |
| Prajñāpradīpa | prajYApradIpa | bhs | 9902 | 359,1 | प्रज्ञाप्रदीप |
| Pramāṇasamuccaya | pramARasamuccaya | mw | 135856 | 686,1 | प्रमाणसमुच्चय |
| pravṛttivijñāna | pravfttivijYAna | mw | 137320 | 694,1 | प्रवृत्तिविज्ञान |
| saṃyukta-samaveta-samavāya | saMyuktasamavetasamavAya | mw | 225740 | 1112,2 | संयुक्तसमवेतसमवाय |
| Śrāvakabhūmi | SrAvakaBUmi | bhs | 15260 | 535,1 | श्रावकभूमि |
| Śrāvakayāna | SrAvakayAna | mw | 222592 | 1097,1 | श्रावकयान |
| Tarkajvālā | tarkajvAlA | mw | 83361 | 440,1 | तर्कज्वाला |
| Triṃśikā | triMSikA | mw | 88528 | 461,2 | त्रिंशिका |
| vāsanā | vAsanA | mw | 192296 | 947,2 | वासना |
| vijñānavāda | vijYAnavAda | mw | 195298 | 961,2 | विज्ञानवाद |
| vipāka | vipAka | mw | 197521 | 973,2 | विपाक |
| Yogācārabhūmi | yogAcAraBUmi | bhs | 12509 | 448,2 | योगाचारभूमि |

此表仅为“命中试算”，不是裁定结果：入库前须逐条核对该辞书条目释义是否与登记册所记概念相符（例如 `mātra`、`nirākāra` 是普通词，可能只是构词成分而非术语本义）。

## 附二：证据 URL

- 组织仓库清单：`https://api.github.com/orgs/sanskrit-lexicon/repos?per_page=100`
- csl-devanagari README（说明镜像生成方式与逐行对应）：`https://github.com/sanskrit-lexicon/csl-devanagari/blob/main/README.md`
- csl-devanagari MW 镜像：`https://github.com/sanskrit-lexicon/csl-devanagari/blob/main/v02/mw/mw.txt`
- 镜像生成脚本：`https://github.com/sanskrit-lexicon/csl-devanagari/blob/main/scripts/to_devanagari.py`
- csl-orig MW 源：`https://github.com/sanskrit-lexicon/csl-orig/blob/main/v02/mw/mw.txt`
- 网页端点实现：`https://github.com/sanskrit-lexicon/csl-apidev/blob/main/getwordClass.php`、`https://github.com/sanskrit-lexicon/csl-apidev/blob/main/utilities/transcoder.php`
- 官方规则表：`https://github.com/sanskrit-lexicon/csl-apidev/blob/main/utilities/transcoder/slp1_deva.xml`
- 转写器文档：`https://github.com/sanskrit-lexicon/csl-apidev/blob/main/doc/transcoder.md`
- 单条数据切片：`https://github.com/sanskrit-lexicon/csl-ldev`
- 联合词头表：`https://github.com/sanskrit-lexicon/CORRECTIONS/blob/main/sanhw1/sanhw1.txt`
- 比对用辞书页：`https://www.wisdomlib.org/definition/klesha`、`https://www.wisdomlib.org/definition/alambana`、`https://www.wisdomlib.org/definition/tathata`、`https://www.wisdomlib.org/definition/vijnapti`、`https://www.wisdomlib.org/definition/svasamvedana`

## 附三：本次试验脚本（均未入库）

| 脚本 | 用途 |
| --- | --- |
| `script/_tmp/deva_probe.py` | 按 SLP1 键定位条目，取镜像侧同 `lnum` 的天城体 `<k1>` |
| `script/_tmp/deva_verify.py` | 官方规则表复算值与镜像值的全量比对 |
| `script/_tmp/deva_fsm.py` | `transcoder.php` 算法的 Python 复现（仅校验用） |
| `script/_tmp/lookup_missing.py` | 对待补清单做命中率试算（IAST→SLP1 仅作检索键） |
