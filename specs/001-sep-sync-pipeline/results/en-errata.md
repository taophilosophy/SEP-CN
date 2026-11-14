# en 源头勘误清单（ADR-0038）

范围：`en/<slug>/index.html` 就地改正的逐条凭证。只收“已核实”四类（排印/OCR 手误、同页自相矛盾、结构错位、占位符可自证）；可争议年份、命名选择、版本标记一律不改，另列“待考”。

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
| emotion-Christian-tradition | 正文 `*Grebethed*`（克尔凯郭尔引文中的词） | 疑为 `Gribethed`／`Gribenhed`，无可靠对照译本，不擅改 |

## 三、2026-11-14 续批（偿还途中新增）

| slug | 原串 | 改正 | 依据 |
| ---- | ---- | ---- | ---- |
| agrippa-nettesheim | `Fromman-Holzoobog` / `Memorie Doemicane` | `Frommann-Holzboog` / `Memorie Domenicane` | 出版社与期刊正名 |
| agrippa-nettesheim | `Princenton University\nPress` / `bilioth&egrave;que` / `Geschchte der Kristlicher` / `edited and and\ntranslated` / `Bell,\n1893&ndash;1890` | `Princeton…` / `bibliothèque` / `Geschichte der christlichen` / `edited and translated` / `1890–1893` | 拼写与降序年份区间 |
| marsilius-inghen | `Gr[special-character:uumlndungsrektors` | `Gr&uuml;ndungsrektors` | SEP 页自身坏实体 |
| marsilius-inghen | `[ISA]<em>, Quaestiones…` | `[ISA], <em>Quaestiones…` | 斜体不该含前导逗号 |
| marsilius-inghen | `J.-L- Sol&egrave;re` / `causasalit&eacute;` | `J.-L. Sol&egrave;re` / `causalit&eacute;` | 法语正字 |
| epistemology-evolutionary | `w_i \frasl \overline{w}` / `Kim, Jagwon., 1988` / `”blind-variation…“` / `“ Social learning` | `\frac{p_i\cdot w_i}{\overline{w}}` / `Kim, Jaegwon, 1988` / 引号方向改正 / 去空格 | MathJax 无 \frasl；Jaegwon Kim 通行拼写；引号体例 |
| albert-great | `“’Mathematics…` / `Super</em> <em>Ethica` | 去多余单引号 / 合为一段斜体 | 题名与书名 |
| envy | `Liverwright` / `No&uacute;s` / `Ben Ze'ev`（含 notes.html） | `Liveright` / `No&ucirc;s` / `Ben-Ze'ev` | 出版社、期刊、作者姓氏正名 |
| leibniz-modal | `Dordrect` / `the Freedom on Man` / `( ed.)` / `1978/9` | `Dordrecht` / `the Freedom of Man` / `(ed.)` / `1978/79` | 同页他条式样、书名介词 |
| leibniz-logic-influence | `1849&ndash;1963` / `Publicatons of the Heinri` / `Thomas Ballet` | `1849&ndash;1863` / `Publications of the Henri` / `Thomas Bassett` | Gerhardt 编数学文集实为 1849–1863；OCR 截断与人名手误 |
| leibniz-logic-influence | 正文 `(Erdmann 1840, p. 130)`，文献区无 1840 条（1840 条实为 Trendelenburg《Logische Untersuchungen》） | `(Leibniz 1839/40, p. 130)` | 埃尔德曼版著录作 Leibniz 1839/40，同页自相矛盾（②） |
| scholz | Neurath 1981 条被拆成两条（一条缺篇名与编者） | 合并为 `Gesammelte philosophische und methodologische Schriften, Vol. 2, ed. by R. Haller and H. Rutte` | 结构错位（③） |
| scholz | `Wissenschaften</em>d,; 106` | `Wissenschaften</em>, 106` | HTML 实体错位（①） |
| academic-freedom | `akedemische Freiheit` | `akademische Freiheit` | 德语正字（023 首条审校实证，类①） |
| academic-freedom | `David\nOwewn and Tracy Strong (eds.)` | `David\nOwen and Tracy Strong (eds.)` | David Owen 为韦伯《Vocation Lectures》Hackett 2004 版合编者，Owewn 非词（类①） |
| academic-freedom | `Enyidi Zsolt, 2018` | `Enyedi, Zsolt, 2018` | 已核实：Zsolt Enyedi, *Perspectives on Politics* 16(4) 2018, 1067–74, doi:10.1017/S1537592718002165（类①） |
| action | `Harman 198;1997`（§4.4 引证组） | `Harman 1986;1997` | 同页 §4.5 引 (Harman 1986; 1997)、书目唯一 1980s 条目为 1986，198 为缺位年手误（类①） |
| sophismata | `An Annoted Translation` / `&lsquo;Sophsimata&rsquo;` | `An Annotated Translation` / `&lsquo;Sophismata&rsquo;` | 拼写（①） |
| sophismata | `with E.J, Ashworth` / `Ingenium Publishers,.` / `1977 im Bonn` | `E.J.` / `Publishers.` / `in Bonn` | 标点与介词手误（①） |
| sophismata | `(Acta Philosophica Fennica, 48-2<em>)</em>` | `(Acta Philosophica Fennica, 48-2)` | 斜体标签错位（①） |
| leucippus | `Taylor, C.C.W, 1999a` / `Diels, H and W. Kranz` | `C.C.W.` / `H. and W.` | 缺句点（①） |
| leucippus | `<em>Apeiron</em>, 46 (4)`（同页 `47(3)`） | `46(4)` | 卷期空格体例不一（①） |
| logic-preference | 图 3 `(V_2) (p>q) ∧ (q>r) → q>r` | `→ p>r` | 标签作 transitivity，$A_2$ 同为传递式，同页自相矛盾（②） |
| logic-preference | `Berlin: Springerd.` / `Makinson David, 1993` | `Berlin: Springer.` / `Makinson, David, 1993` | 出版社拼写与姓名倒置（①） |
| logic-preference | `illustrated by \(V_4\) in the table above` | `in the figure above` | $V_4$ 实见于图 3，表图混称（②） |
| lorenzo-valla | `Studi di grammatica italiana</em>,w 19` | `italiana</em>, 19` | OCR 残字（①） |
| lorenzo-valla | 三条书目缺句末句点（`Rinascimento</em>, 31: 155&ndash;181`、`Vivarium</em>, 44: 375&ndash;395`、`Cambridge, Mass., Harvard University Press`） | 各补 `.` | 句读（①） |
| leibniz-mind | `Searle, J., 1990. &ldquo;Minds, Brains, and Programs,&rdquo; … 3: 417&ndash;457` | `1980` | BBS 第 3 卷（1980）与正文 Searle 1980 相合，同页自相矛盾（②） |
| leibniz-mind | `Toronto University Press..` | `Toronto University Press.` | 双句点（①） |
| leibniz-mind | `&rdquo;<em>Pacific` / `&rdquo;<em>Journal` / `&rdquo;<em>Causation` / `&ldquo; Leibniz` | 补空格、去引号内前导空格 | 排版（①） |
| publichealth-ethics | notes.html `(Omerand et al. 2009; …)` | `(Omer et al. 2009; …)` | OCR 拼合（①）；不修则 omer-2009 引注静默丢失 |
| schlegel | `Lacoue-Labarthe and J.-L. Nancy, 1978` | `Lacoue-Labarthe, P., and J.-L. Nancy` | 缺第一作者名首字母（①） |
| schlegel | `deMan, P., 1996` | `de Man, P., 1996` | 姓氏分写（①） |
| cockburn | `Eigtheenth Century` / `Eurpoean Philosophy`（×2） | `Eighteenth` / `European` | 拼写（①） |
| cockburn | notes.html `grown son.In response` | `son. In response` | 缺空格（①） |
| conway | `Principia philosophiae antiquissimae ac recentissimae`（首见） | `… et recentissimae` | 同书前后两写，同页自相矛盾（②） |
| conway | `<em>apocotastasis</em>` | `<em>apokatastasis</em>` | 拼写（①） |
| conway | `<em>History of Philosophy Quarterly, </em>39(1):21&ndash;44.` | `<em>History of Philosophy Quarterly</em>, 39(1): 21&ndash;44.` | 标点入斜体、缺空格（①） |
| conway | `(by Loptson, Conway1998)` / `Mercer 2012 and 2019 ,` | `Conway 1998` / `2019,` | 缺空格、逗号前空格（①） |
| leibniz-ethics | `<em>Philospohical Papers and Letters,</em>` | `<em>Philosophical Papers and Letters</em>,` | 拼写与逗号入斜体（①） |
| locke-on-medicine | `M.D. Ranslated from` / `&ldquo;Vaccuum&rdquo;` | `Translated` / `Vacuum` | 拼写（①） |
| locke-on-medicine | `&ldquo;Eloge de feu Mr. Locke.&rdquo;,` / `12: 243&ndash;284,` | 去引号内句点、末逗号改句点 | 标点（①） |
| montesquieu | `Montesquieu and Rouseau` / `University of Michign Press` | `Rousseau` / `Michigan` | 拼写（①） |
| montesquieu | `31 (3): 469-499` | `31(3): 469–499` | 卷期空格与半字线（①） |
| montesquieu | hulliung-1976 条末缺句点 | 补 `.` | 句读（①） |
| modesty-humility | 7 条书目期刊名前缺逗号 | 补 `,` | 书目标点（①） |
| modesty-humility | `&ldquo;Aidws in Epictetus&rdquo;` / `&ldquo;&rsquo;A Monkish Virtue?&rsquo;` | `Aid&#333;s` / `&lsquo;…&rsquo;` | 希腊转写与引号方向（①） |
| modesty-humility | kelly-2010 `Disagreement` 缺斜体；aquinas-1981 链接后缺句点 | 补斜体、补句点 | 书目体例（①） |
| obligationes | `Breen-Pedersen &amp; Pinborg 1976` / `Uckelman, Maat and Rybalko 2018` | `Green-Pedersen` / `2008` | 与书目条目不符（②） |
| obligationes | `J. Pinbord` / `Rober Swyneshed` | `Pinborg` / `Robert` | 拼写（①） |
| obligationes | keffer-2001／read-2020／yrjönsuuri-2015 条末缺句点 | 补 `.` | 句读（①） |
| origin-descent | `Preservaton` / `Darwin1869` / `Williams and Noegate` / `thirrd` / `Ethics an Contemporary` / `[M.J.S.}` | `Preservation` / `Darwin 1869` / `Norgate` / `third` / `and` / `[M.J.S.]` | 拼写与括号（①） |
| origin-descent | darwin-1872 条 `[<a …>…</a></li>` 缺闭合 `]` | 补 `]` | 截断（①） |
| oakeshott | `Nichomachean`（两处） | `Nicomachean` | 拼写（①） |
| oakeshott | grant-2012 条末缺句点 | 补 `.` | 句读（①） |
| object | notes `VII 15.1939b20&ndash;25` / `XI 9.1058b80&ndash;12` | `1039b20–25` / `1058b8–12` | OCR 掉位与衍 0（①） |
| object | `Wien: &Ouml;bvetHpt` / `<em>Oxford</em>: Oxford` / `<em>Words without Objects:</em> ,` | `ÖBV & HPT` / `Oxford:` / `Words without Objects` | 出版社、斜体与标点（①） |
| occasionalism | `(Weinburg 1964, 272)` / `Bouillier 1865` | `Weinberg` / `1854` | 拼写与年份（①②） |
| occasionalism | `Trunbout: Brepols` / `Constructionsn` | `Turnhout` / `Constructions` | 拼写（①） |
| erasmus | `quiddities and ecceities` / `Duncker &amp; Humbolt` / `Dodds, Gregory , 2009` | `haecceities` / `Humboldt` / `Gregory,` | 拼写与空格（①） |
| erasmus | `&Eacute;<em>rasme…` / `<em>. Desiderius Erasmus…` | 斜体含重音字母、去首点 | 斜体错位（①） |
| albo-joseph | `R. Josepf Albo` / `Miscel&aacute;neade` / `Dragestellt` / `W. Schlessinger` | `Josef` / `Miscelánea de` / `Dargestellt` / `Schlesinger` | 拼写（①） |
| albo-joseph | `Joseph Albo&rsquo;s, <em>Buch Ikkarim` | 去逗号 | 标点（①） |
| epictetus | `G&#333;ttingen` / `Vandenh&#333;ck` / `Dictionaire` / `Reallexicon` | `Göttingen` / `Vandenhoeck` / `Dictionnaire` / `Reallexikon` | 实体与拼写（①） |
| epictetus | graver-2003 书名与刊名同裹斜体 | 分列斜体 | 斜体（①） |
| epictetus | `Cambridge :` / `Beyond :` | 去空格 | 排版（①） |
| epictetus | 重复的 Stadter 1980 条 | 删一 | 重复登记（②） |
| ethics-deontological | `Similansky` / `Sauders` / `Wedgewood` / `MacMahan` | `Smilansky` / `Saunders` / `Wedgwood` / `McMahan` | 拼写（①②） |
| blame | `doi: doi:10.3998` / `Wieland. (eds.)` / `in H, LaFollette` / `<em>…Philosophy&nbsp;</em>32` | 去重复前缀、正句点、正逗号、卷号出斜体 | 标点与斜体（①） |
| egoism | `Korsgaard, C, 2005` / `&ldquo;The Myth of Egoism,&rdquo;, in` | `C.` / 去多余逗号 | 缩写与标点（①） |
| emotion-Christian-tradition | 正文 `see Bash 2019)`，文献条作 2020 | `see Bash 2020)` | 同页自相矛盾（②） |
| emotion-Christian-tradition | 正文 `Richard S. Lazarus (1993)` 与 `(see 1993 p. 122)`，文献区只有 lazarus 1991 | 均改 1991 | 同页自相矛盾（②）；出处即 *Emotion and Adaptation* |
| emotion-Christian-tradition | `Doubleday: Garden City, New York.` | `Garden City, New York: Doubleday.` | 同页其余条目皆“地名: 出版者”（②） |
| emotion-Christian-tradition | `&ldquo;Startle&rdquo; <em> The Journal of Philosophy</em>` | `&ldquo;Startle,&rdquo; <em>The Journal of Philosophy</em>` | 篇名后缺逗号、em 内多空格（①） |
| emotion-Christian-tradition | `schlechthinig` | `schlechthinnig` | 德语 schlechthin＋-ig（①） |
| epistemology-language-tibetan | `Universit&agrave; degli Sudie di Napoli` | `Studi` | 意大利机构正名 Università degli Studi di Napoli（①） |
| epistemology-language-tibetan | `Oxford: Wiley Balckwell` | `Wiley Blackwell` | 出版者正名（①） |
| epistemology-language-tibetan | `<em>Etudes Asiatiques</em>` | `<em>&Eacute;tudes Asiatiques</em>` | 法语刊名缺重音（①） |
| arabic-islamic-mysticism | 正文 `With Sabziwārī's death in 1797 CE..` | `in 1873 CE.` | 同页作（1797–1873），1797 为生年；另去双句点（②①） |
| arabic-islamic-mysticism | `(Nicholson, IV: 1519&ndash;1516)` | `1516&ndash;1519` | 页码区间倒置（①） |
| arabic-islamic-mysticism | `Fuṣūṣ al-ḥakam`（伊本·阿拉比条） | `Fuṣūṣ al-ḥikam` | 同页另处作 ḥikam，标题正音（②） |
| arabic-islamic-mysticism | `Chittick, W. C., 2007. Ibn Arabī, <i>Ibn Arabī's Metaphysics of Imagination</i>` | 去重复的“Ibn Arabī,” | 作者名窜入题名（①） |
| arabic-islamic-mysticism | `Nasir Khusraw:The Ruby of Badakhshan` | 冒号后补空格 | 排印（①） |
| arabic-islamic-mysticism | `<i>Classical</i> <i>Persian Sufism…</i>` | 合为一处斜体 | 书名被切断（①） |
| arabic-islamic-mysticism | `Hunsburger`（正文两处与书目） | `Hunsberger` | 作者正名 Alice C. Hunsberger（①） |
| equal-ed-opportunity | `39(4): 137&ndash;1176`（doi 10.1257/jel.39.4.1137） | `1137&ndash;1176` | doi 自证起页（②③） |
| equal-ed-opportunity | `Social Epigentics and Equality of Opportunity` | `Social Epigenetics` | 拼写（①） |
| equal-ed-opportunity | `<em>Finnish lessons</em>` | `<em>Finnish Lessons</em>` | 书题大小写（①） |
| equal-ed-opportunity | `Russel Sage Foundation`（reardon-2011 条） | `Russell Sage` | 出版者正名，同页另一条即作 Russell（②） |
| equal-ed-opportunity | `Erica Weather,` | `Erica Weathers,` | 同页正文两处作 Weathers（②） |
| equal-ed-opportunity | `Institute for Higher Education, 1998` | `Institute for Higher Education Policy` | 同页正文作全名，机构正名（②） |
| emilie-du-chatelet | `(Original publication date: 1742.]` | `1742.)` | 括号不配对（①） |
| emilie-du-chatelet | `Studia Leibnitiana, 2(2):: 114–27` | `2(2): 114–27` | 双冒号（①） |
| emilie-du-chatelet | `Cirey dans la vie intellectualle`（两条） | `intellectuelle` | 法语拼写（①） |
| emilie-du-chatelet | `&ldquo;&ldquo;Sancti…nobis&rdquo;. Emilie` | 单引号起、`&rdquo;: Emilie` | 引号重复且题名内应为冒号（①②） |
| emilie-du-chatelet | `18ᵗʰ Century Persepctives` | `Perspectives` | 拼写（①） |
| emilie-du-chatelet | `Institut et Musee Voltaire` | `Mus&eacute;e` | 法语重音（①） |
| emilie-du-chatelet | `Istitut des textes et manuscrit modernes` | `Institut des textes et manuscrits modernes` | 机构正名（①） |
| emilie-du-chatelet | 正文 `Institutions physique`（1742 年版书名） | `Institutions physiques` | 同页书目作 physiques（②） |
| emilie-du-chatelet | `Lindberg and Robert S. Westman (ed.)` | `(eds.)` | 两编者（①） |
| emilie-du-chatelet | `Ruth Hagengruber (eds.)`（hutton 条） | `(ed.)` | 单编者（①） |
| emilie-du-chatelet | `Eileen O'Neill and Marcy Lascano (ed.)` | `(eds.)` | 两编者（①） |
| emilie-du-chatelet | `La physique expérimentale ver 1740` | `vers 1740` | 法语拼写（①） |
| emilie-du-chatelet | `systèmes et hypotheses` | `hypothèses` | 法语重音（①） |
| emilie-du-chatelet | `Hagengruber, Ruth, 2011` | `2012` | 正文与注 6、9、16 均引 2012，文集为 Springer 2012（②） |
| emilie-du-chatelet | `–––, 2011, “Between Newton and Leibniz…` | `2012` | 同上，正文引 Hutton 2012, 77–95（②） |
| gelukpa | `<em>The Great Treatise on the States of the Path…</em>` | `Stages of the Path` | 通行英译书名（《菩提道次第广论》）（①） |
| gelukpa | `lam byi gtso bo rnam gsum` | `lam gtso rnam gsum` | 威利转写多一词（《三主要道》）（①） |
| gelukpa | `<em>Tsongkhapa&rsquo;s</em> <em>Collected Works</em>` | 合为一处斜体 | 同页另两条书目未断（②） |
| emerson | `the Confucian <em>junxi</em>` | `junzi` | 儒家“君子”通行拼音（①） |
| emerson | `(Wirzrbicki, 95…` | `Wirzbicki` | 同页另处作 Wirzbicki（②） |
| emerson | `<em>Emerson&rsquo;s Antislavery Writings, </em>31` | `</em>, 31` | 逗号误入斜体、缺空格（①） |
| emerson | `<em>…Racial Anglo-Saxonism, </em>Cambridge` | `</em>, Cambridge` | 同上（①） |
| emerson | `<em>Individuality and Beyond: Nietzsche Reads Emerson, trans. Alexander Reynolds</em>` | 译者移出斜体 | 译者名误入书名斜体（①） |
| emerson | `<em>Handbook of American Romanticism,</em>` | `</em>,` | 逗号误入斜体（①） |
| emerson | `Clemens Spahr, Jan Stievermann (ed.)` | `(eds.)` | 三编者（①） |
| emerson | `Boston: A. Williams and Co., 1882)` | `A. Williams and Co.` | 年份重复、括号不配对（①） |
| antonio-rosmini | `another ten are deduced`（其后只列九条） | `another nine` | 同页自相矛盾（②） |
| antonio-rosmini | `Theodicy (theou dike)` | `theou dik&#275;` | 希腊语转写缺长音符（①） |
| film | `the entire <em>ouvre</em> of a director` | `oeuvre` | 拼写（①） |
| film | `Francois Truffaut` | `Fran&ccedil;ois` | 变音符缺失（①） |
| film | `N&ouml;ell Carroll`（Bordwell 条） | `N&ouml;el Carroll` | 同页他处作 Nöel（②） |
| film | `<em>Filmospohy</em>` | `Filmosophy` | 拼写（①） |
| film | `Krakauer, Siegfried` | `Kracauer` | 作者正名（①） |
| film | `Ranciere, Jacques` | `Ranci&egrave;re` | 变音符缺失（①） |
| film | Badiou 2013 `<em>Film Fables</em>, Cambridge: Polity` | `<em>Cinema</em>` | 同名书已属 Rancière 2006，Polity 2013 版 Badiou 书名为 Cinema（②） |
| film | `Grey M. Smith (eds.)`（plantinga-1999） | `Murray Smith` | 编者正名（①） |
| film | `Hugh Grey (tr.)`（bazin-1967） | `Hugh Gray` | 译者正名（①） |
| film | 正文 `Carroll and Choi 2006` | `2005` | 书目作 Carroll & Choi 2005（②） |
