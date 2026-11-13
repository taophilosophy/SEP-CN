# en 源头勘误清单（ADR-0038）

范围：`en/<slug>/index.html` 就地改正的逐条凭证。只收「已核实」四类（排印/OCR 手误、同页自相矛盾、结构错位、占位符可自证）；可争议年份、命名选择、版本标记一律不改，另列「待考」。

改正后由 `python tools/yuanwen.py --all-baselined --summary` 全量重转，`baseline/entries.json` 的 `source_sha256` 与 `md` 哈希随重转重算；git 历史即勘误证据。

## 一、已改正（2026-11-14，18 处／16 文件）

| # | slug | 原串 | 改正 | 依据 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | incompatibilism-theories | `Buckareff, YEAR.` | `Buckareff, 2003.` | 同页正文引 “Feldman and Buckareff [2003]”，期刊卷 112 与 2003 相符 |
| 2 | religious-experience | `exists 3s a metaphysical assertion` | `exists is a metaphysical assertion` | 语境为 “That a transcendent god exists is …”，`3s` 系 `is` 误识 |
| 3 | mathematics-inconsistent | `O.Bueno and O. Limmbo (eds.)` | `O. Bueno and Ø. Linnebo (eds.)` | 该文集编者实为 Otávio Bueno 与 Øystein Linnebo |
| 4 | mathematics-inconsistent | `doi:10.1007/511229-014-0614-2` | `doi:10.1007/s11229-014-0614-2` | Synthese 的 Springer doi 前缀为 `s11229` |
| 5 | mathematics-inconsistent | 正文 `Paris and Sirokfskich (2008)` | `Sirokofskich` | 同页文献条作 “Paris, J., and Sirokofskich, A., 2008” |
| 6 | incommensurability | `(Einstein1949b, 683ff.)` | `(Einstein 1949b, 683ff.)` | 引称体例；同页键为 `einstein-1949b` |
| 7 | molyneux-problem | 正文 `Berchielli 2003` | `Berchielli 2002` | 同页文献条 “Berchielli, L., 2002” |
| 8 | molyneux-problem | 正文 `(Levin 2020)` | `(Levin 2019)` | 同页文献条 “–––, 2019, Locke on Molyneux’s question …” |
| 9 | ibn-ezra | `Crirical Edition` | `Critical Edition` | 拼写 |
| 10 | logic-provability | `Arithmetic Complexiy of Predicate Logics` | `Complexity` | 拼写 |
| 11 | logic-provability | `Cambridh=ge University Press` | `Cambridge University Press` | 排印手误 |
| 12 | logic-provability | `pp.109–130` | `pp. 109–130` | 体例（同页他条均作 `pp. `） |
| 13 | duhem | `Sijthooff and Noordhoff` | `Sijthoff` | 荷兰出版社通行拼写 |
| 14 | al-qudat | `Sufi Pyschology` | `Sufi Psychology` | 拼写 |
| 15 | aesthetics-18th-british | `Shelby-Bigge`（2 处） | `Selby-Bigge` | Hume 编者通行拼写（L. A. Selby-Bigge） |
| 16 | boolalg-math | `Birka&uuml;ser` | `Birkh&auml;user`（Birkhäuser） | 出版社通行拼写 |
| 17 | alcmaeon | `die Alcmeone` / `Accademia Nazionnale dei Lincei` / `Arabic tradtion` | `di Alcmeone` / `Nazionale` / `tradition` | 意大利语与拼写 |
| 18 | redistribution | `Mitchel Selgson` / `O&rsquo;Neil, Martin` | `Mitchell Seligson` / `O’Neill, Martin` | 编者与作者通行拼写（正文作 O’Neill） |
| 19 | lakatos | `Lakatos1978a` | `Lakatos 1978a` | 引称体例 |
| 20 | intellectual-property | 正文 `(Axelrod 198,` | `(Axelrod 1981,` | 文献条作 Axelrod 1981 |
| 21 | intellectual-property | Axelrod 1981 与 1984 同处一个 `<li>`，以 `<br />` 分隔 | 拆为两个 `<li>` | 一条文献一项；旧结构致转换后两条并录为一键 |

（表内 21 行对应 16 个文件、22 处替换，其中美学条两处同名、逻辑条三处。）

## 二、待考未改

| slug | 现象 | 处置理由 |
| ---- | ---- | ---- |
| alcmaeon | 正文引 `Mansfeld (2013, 78, n. 1)`，文献区只有 1975／2014a／2014b | 无法判定 2013 是 2014a 的笔误还是另一未列条目；不擅改 |
| redistribution | 正文 `Scanlon (1981, p. 199)`、`Nagel (1981, p. 201)`，文献条作 1982（Oxford: Blackwell, 206–231） | 1981 与 1982 可能分属原版与重印版，页码亦各自成立；保留正文年份 |
| redistribution | 正文 `Alesina et al. (1999)`，文献条作 2001（NBER WP 7387） | 工作论文与刊行版年份差属常态；保留正文 |
| redistribution | 脚注 [^note-6] 引 “Modigliani and Solow [1989]”，文献区无此条 | 源文引证悬空，无从补 |
| aesthetics-18th-british | 正文 `Hutcheson 1747, 12–13 and 1744, 48`，文献区只有 1742／1747 | 1744 或为该书另一印次，页码 48 与之相联；中文侧按原文保留 1744 |
| aesthetics-18th-british | 正文 `2005/389–391`，文献条作 `389–390 [2005]` | 页码区间互有小差，无可判据；中文侧照录 |
| langer | 文献键五套前缀与内容错位（`eugene-1951a` 实为 Langer 1951a 等） | 属命名体系而非手误，改动面大，另案处理 |
