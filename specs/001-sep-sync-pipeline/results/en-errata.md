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
| sovereignty | `<strong>(</strong>124&ndash;125)` | `(124&ndash;125)` | 加粗残件（①） |
| sovereignty | `bombing of Iraq in December 1999` | `December 1998` | 同句并列科索沃 1999；“沙漠之狐”为 1998 年 12 月（②①） |
| sovereignty | `Thomas Pogge (1992, and 2008, 174&ndash;201)` | `(1992, 2008, …)` | 引证组多余逗号与 and（①） |
| sovereignty | `(Keohane &amp; Hoffman 1991)` | `Hoffmann` | 同页书目作 Hoffmann（②） |
| sovereignty | `Zone Books, 2010`（brown-2010 条目已标 2010） | 去尾年份 | 年份重复（①） |
| sovereignty | `Luther, Martin.,` | `Martin,` | 双标点（①） |
| sovereignty | `Machiavelli, Niccolo,` | `Niccol&ograve;` | 变音符缺失（①） |
| sovereignty | wilks-1964 缺句末句点 | 补句点 | 排印（①） |
| sovereignty | `2nd. edition`（pogge-2008） | `2nd edition` | 句点错位（①） |
| bohr-correspondence | hassoun-1989 `correspondence principle,”,` | 去多余逗号 | 双标点（①） |
| bohr-correspondence | `quantentheorische Umdeutung` | `quantentheoretische` | 德语正字（①） |
| auriol | friedman-1999 `C.A. Rietzel` | `C.A. Reitzel` | 出版者正名（①） |
| auriol | goris-2002 `Peter of Oriel` | `Peter of Auriol` | 人名正名（①） |
| auriol | `doi.org:10.1007/…`（martin-2026） | `doi:10.1007/…` | doi 前缀格式（①） |
| auriol | `The Stanford Encyclopedia Philosophy`（两条） | `…of Philosophy` | 缺 of（②） |
| auriol | pasnau-2008 `P. Kärkkäin` | `Kärkkäinen` | 编者正名（①） |
| moral-responsibility-empirical | 两个 `<h3>` 均编号 3.1（另一为 3.2） | 依次改 3.1／3.2／3.3 | 同页章节编号自相矛盾（②） |
| moral-responsibility-empirical | hofmann-2012 `102(6): 1318&ndash;133OB5` | `1318&ndash;1335` | OCR 混入大写字母，起止页自证（①） |
| moral-responsibility-empirical | sinnott-armstrong-2013 `<em>…Psychiatry</em>. pp. 851` | `</em>, pp. 851` | 句点误作逗号（①） |

## 四、2026-11-15 补登（分歧账建账时发现未登记件）

| slug | 原串 | 改正 | 依据 |
| ---- | ---- | ---- | ---- |
| bohr-correspondence | `&Uuml;ber quantentheorische Umdeutung` | `&Uuml;ber quantentheoretische Umdeutung` | 玻尔 1925 论文通行德语题名 quantentheoretische（①） |
| bohr-correspondence | `principle,&rdquo;,` 换行后 `<em>American Journal of Physics</em>` | `principle,&rdquo; <em>American Journal of Physics</em>` | 引号后重逗号删除并并行；同页他条均作 `,&rdquo; <em>`（①） |
| bodily-awareness | schwitzgebel-2007 `Schwitzgebel, Erica` | `Eric` | 作者正名（①） |
| bodily-awareness | alsmith-2015 `Sense ofOwnership` | `Sense of Ownership` | 缺空格（①） |
| bodily-awareness | barlassina-2019 `Luca.,` | `Luca,` | 双标点（①） |
| bodily-awareness | ehrsson-2022 题名缺收引号、`Nature Communication` | 补 `&rdquo;`；`Nature Communications` | 引号不配对、刊名误（①②） |
| bodily-awareness | gallagher-1986 `Aconceptual Clarification` | `A Conceptual Clarification` | 分词误合（①） |
| bodily-awareness | goldenberg-2003 `Goldsten and Gel&rsquo;s case` | `Goldstein and Gelb&rsquo;s case` | 人名正名（①） |
| bodily-awareness | kinsbourne-1995 `Attentionnal` | `Attentional` | 拼写（①） |
| bodily-awareness | lycan-2023 `Mroczko-WaSowicz` | `Mroczko-W&#261;sowicz` | 姓氏缺变音符（①） |
| bodily-awareness | martin-1993 `Naoimi Eilan, Rosaleen McCarty` | `Naomi Eilan, Rosaleen McCarthy` | 编者正名（①） |
| bodily-awareness | turvey-1995 `Carello, , 1995` | `Carello, 1995` | 多余逗号（①） |
| bodily-awareness | vignemont-2007 `One&lsquo;s Own Body` | `One&rsquo;s` | 左单引号误（①） |
| bodily-awareness | henri-1965 `Presses Universitaire de France` | `Universitaires` | 机构正名（①） |
| bodily-awareness | block-2005 `by Alva No&euml;&rdquo;:,` | `&rdquo;,` | 标点错乱（①） |
| bodily-awareness | o&rsquo;callaghan-2020 `University Press. 92&ndash;117` | `University Press, 92&ndash;117.` | 标点与句末（①） |
| bodily-awareness | clark-1997／melzack-1983／thelen-1994／gibson-1979 条末缺句点 | 补句点 | 排印（①） |
| bodily-awareness | shoemaker-1994 `Object Perception Model&rdquo;, 54(2)` | 去多余收引号 | 引号不配对（①） |
| bodily-awareness | matthen-2021 `The Dual Structure ofc touch` | `of Touch` | OCR 混入（①） |
| bodily-awareness | vignemont 条 `forthcoming` 而正文引 2021 | `2021` | 同页自相矛盾；文集 2021 年出版（②） |
| social-procedures | gale-1962 题名引号缺收尾、`L. Shapley, L.` 重复缩写 | 补 `&rdquo;`、去重 | 引号不配对（①） |
| social-procedures | meijering-2012 `2012,&ldquo;What` | 逗号后补空格 | 排印（①） |
| social-procedures | meijering-2014 题名收尾作 `&ldquo;` | `&rdquo;` | 引号方向误（①） |
| social-procedures | top-2018 `9(3),44;` | `9(3): 44.` | 卷期页码标点（①） |
| social-procedures | bulling-2015 `Strategic Abiliies` | `Abilities` | 拼写（①） |
| social-procedures | cechlérová-2005 `Cechl&eacute;rov&aacute;` | `Cechl&aacute;rov&aacute;` | 姓氏正拼（①） |
| bradley-moral | hegel-1807 `Bamberg und W&uuml;rzburg: Goebbardt` | `Goebhardt` | 出版者正名 J. A. Goebhardt（①） |
| bradley-moral | krook-1959 `Cambridge::` | `Cambridge:` | 双冒号（①） |
| bradley-moral | santayana-1933 `Santayana George, 1933` | `Santayana, George, 1933` | 姓与名未分隔（①） |
| bradley-moral | wollheim-1969 `fFirst published, 1959` | `First published, 1959` | 衍字（①） |
| bradley-moral | ethical-1951 `(Note: This volume omits Essays I, VI, VII.]` | `…VII.)` | 括号不配对（①） |
| bradley-moral | collected-1999 `Appearance ana Reality` / `Volume11:` | `and` / `Volume 11:` | 拼写与缺空格（①） |
| bradley-moral | ce-1901 `CE II.387&ndash;407 doi:` | 补句点 | 排印（①） |
| arabic-islamic-phil-math | `Avicenna (d. 937)` | `(d. 1037)` | 阿维森纳卒年（②①） |
| arabic-islamic-phil-math | `mutikallim&#363;n` | `mutakallim&#363;n` | 拼写（①） |
| arabic-islamic-phil-math | `Printing House of the Egyption Library` | `Egyptian` | 拼写（①） |
| arabic-islamic-phil-math | bertolacci-2006 `al-&Scaron;if&#257;&#417;` | `&#702;`（al-Šifāʾ） | 组合字符 OCR（①） |
| arabic-islamic-phil-math | gutas-2001 `in Wisnovsky 2001:, 1–38` | `2001: 1–38` | 冒号错位（①） |
| arabic-islamic-phil-math | kiankhah-2015 `Sophia Prennis` | `Sophia Perennis` | 刊名拼写（①） |
| arabic-islamic-phil-math | rashed-2015 `Al-Khwar&#299;zm&#299;` | `al-Khw&#257;rizm&#299;` | 转写正字（①） |
| arabic-islamic-phil-math | samaw’al-1972 `Université de Damascus` | `Université de Damas` | 机构正名（①） |
| arabic-islamic-phil-math | suhrawardī-1999 `(eds/)` | `(eds.)` | 残缺标点（①） |
| arabic-islamic-phil-math | berggren-2016 `Berggren, 2016` | `Berggren, J. L., 2016` | 缺名首字母（①） |
| arabic-islamic-phil-math | goodman-1992 条末缺句点 | 补句点 | 排印（①） |
| arabic-islamic-phil-math | `[Mph]`（两处）与 `[MPh]` | 统一 `[MPh]` | 同页缩写两体（②） |
| hutcheson | inquiry-1725 `[A] 1725 ,` | `[A] 1725,` | 逗号前空格（①） |
| hutcheson | adams-1976 `Motive Utilitarianism”:,` | `Motive Utilitarianism”,` | 题名后错标点（①） |
| hutcheson | arneson-2004 `Interpretated` | `Interpreted` | 拼写（①） |
| hutcheson | arneson-2004 `Defended”:,` | `Defended”,` | 题名后错标点（①） |
| hutcheson | kail-2001 `History of Philosophy Quarterly 18(1)` | 期刊名后补逗号 | 缺标点（①） |
| hutcheson | kivy-1976 `Burt Franklin and Co..` | `Co.` | 双句点（①） |
| hutcheson | clarke-1706 `excerpted as “ A Discourse` | `“A Discourse` | 引号内前导空格（①） |
| hutcheson | schmitter-2016 URL 末缺句点 | 补句点 | 缺标点（①） |
| hutcheson | 正文 `John Balguy… writes` ＋引块 | `writes:` | 引块前缺冒号（①） |
| hutcheson | 正文 `consists in ‘having … Affections.`（单引号且未收束） | 改双引号 `“…”` 并补收束 | 引号体例与未闭合（①） |
| hutcheson | smart-nd `19743`；正文 `Smart & Williams 1974` | `1973`（两处） | 年份误录、正文与书目矛盾（①②） |
| hutcheson | 正文 `not published until after Hutcheson’s death in 1755` | `not published until 1755, nine years after Hutcheson’s death` | 卒年与出版年相混（②；首段 1694–1746 自证） |
| ockham | guillelmi-1967 条 `Opera Theologica, 18 volumes` | `10 volumes` | 与列目自相矛盾（②；OTh 10 卷＋OPh 7 卷） |
| ockham | vol-nd-8 `Reportio` | `Reportatio` | 拼写（①） |
| ockham | epistola 条 `Friars Minor]);` | `Friars Minor];` | 多余反括号（①） |
| ockham | de-nd-2 `De election Caroli Quarti` | `De electione Caroli Quarti` | 拼写（①） |
| ockham | keele-2002 `Razor,</em>` | `Razor</em>,` | 逗号入斜体（①） |
| ockham | maurer-1978 `Nominalism:”` | `Nominalism”` | 题名内多余冒号（①） |
| ockham | spade-1999c `Ockhams’` | `Ockham’s` | 撇号错位（①） |
| kant-hume-morality | 两处 `doi:0.1093…` | `doi:10.1093…` | doi 缺前导 10（①） |
| kant-hume-morality | bricke-1996 题名末 `… Psychology John Bricke` | 删去窜入的作者名 | 作者名窜入题名（①） |
| kant-hume-morality | crisp-2019 `Benthem` | `Bentham` | 拼写（①） |
| kant-hume-morality | `F&ouml;ster` | `F&ouml;rster` | 拼写（①） |
| kant-hume-morality | radcliffe-2019 `Perspectives<em>,&rdquo; …Supplement</em>` | `Perspectives&rdquo;, <em>…Supplement</em>` | 斜体跨引号错位（①） |
| kant-hume-morality | robinson-2017 `2017 (eds.), 2017` | `(eds.), 2017` | 年份重复（①） |
| kant-hume-morality | `Suprenant`（5 处） | `Surprenant` | 拼写（①） |
| kant-hume-morality | [H]/[C]/[M]/[V] 说明段起 `(` 未闭 | 补 `)` | 括号未闭合（①） |
| kant-reason | møller-2020 `…in the</em> Critique of Pure Reason.` | `…in the Critique of Pure Reason</em>,` | 斜体提前收束（①） |
| kant-reason | rescher-2000 `Reach of Reason:</em> <em>Studies in…` | 合为一处斜体 | 题名被拆成两段斜体（①） |
| kant-reason | notes 注 35 `simply (?) as considerations` | `simply as considerations` | 作者遗留问号占位（①） |
| kant-social-political | o’neill-2016 `O’Neill, Onora 2016` | `Onora, 2016` | 缺逗号（①） |
| kant-social-political | waldron-1996 `Waldron, Jeremy 1996` | `Jeremy, 1996` | 缺逗号（①） |
| kant-social-political | yovel-1980 `Yovel, Yirmiyahu Yovel` | `Yirmiyahu` | 姓氏重复（①） |
| kant-social-political | stone-2018 `Kant: Constitutional Justice, and European Convention` | `Kant, Constitutional Justice, and the European Convention` | 双冒号且脱 the（①） |
| kant-social-political | willaschek-1997 `Jahrbuch für Recht und Ethik 5, 205–227` | 期刊名斜体、`5: 205–227` | 期刊名未斜体（①） |
| kant-social-political | fleischacker-1999 条末缺句点 | 补句点 | 缺标点（①） |
| kant-social-political | korsgaard-1997／wilson-1998 `, In …` | `, in …` | 句首 In 大写（①） |
| kant-social-political | doyle-1983 `205–235 and 323–353` | `205–235, 323–353` | 页码间英文 and（①） |
| knowledge-analysis | antognazza-2020 `120(3): 2020:277–308` | `120(3): 277–308` | 年份重复（①） |
| knowledge-analysis | hirvelä-2025 `59(2) :335–348` | `59(2): 335–348` | 冒号前空格（①） |
| knowledge-analysis | hirvelä-2025 `doi:10.111/nous.12516` | `10.1111/nous.12516` | doi 缺一位（①） |
| knowledge-analysis | cohen-1988 `1988 “How…` | `1988, “How…` | 年份后缺逗号（①） |
| knowledge-analysis | ichikawa 2017 条引号未闭合 `‘First’, in` | `‘First’”, in` | 引号未闭合（①） |
| knowledge-analysis | Jenkins 条 `2017,` | `2017-a,` | 正文引 2017-a 而条目无 a（②） |
| knowledge-analysis | gibbons-2013／ichikawa-2024 缺出版地 | 补 `Oxford:` | 缺出版地（①） |
| knowledge-analysis | pappas-2023 缺年份 | 补 `2023,` | 缺年份（①） |
| knowledge-analysis | worsnip-2017 `pp. 177-189` | `pp. 177&ndash;189` | 连字符应为连接号（①） |
| knowledge-value | carter-2020 `&ldquo; Epistemic Value…` | `&ldquo;Epistemic…` | 引号内前导空格（①） |
| knowledge-value | carter-2014 `Gordon, 2014 &ldquo;Objectual` | `2014, &ldquo;…` | 年份后缺逗号（①） |
| knowledge-value | jarczewski-2025 期刊名 `Episteme` 未斜体 | `<em>Episteme</em>` | 期刊名未斜体（①） |
| knowledge-value | goldman-1979 `*Justification and Knowledge* Boston: D. Reidel: 1–25` | `, Boston: D. Reidel, 1–25` | 标点错乱（①） |
| knowledge-value | derose-1992 `Research</em> , 52` | `</em>, 52` | 逗号前空格（①） |
| knowledge-value | pritchard-2010a `1-90` | `1&ndash;90` | 连字符应为连接号（①） |
| knowledge-value | pritchard-2011 条末缺句点 | 补句点 | 缺标点（①） |
| knowledge-value | turri-2016b 条末缺句点 | 补句点 | 缺标点（①） |
| knowledge-value | turri-2011a `URL = <[url](url)>` | `URL = <url>` | 嵌套方括号（①） |
| aristotle-causality | code-2015 `Theory and PRactice`／`Cambrdige` | `Practice`／`Cambridge` | 拼写（①） |
| aristotle-causality | witt-2015 `Phyiscs` | `Physics` | 拼写（①） |
| aristotle-causality | leunissen-2010-2 `Good Houskeeper.` | `Good Housekeeper.` | 拼写与句读（①） |
| aristotle-causality | bradie-1984 `Bradie, M., Miller, 1984, F. D.,` | `Bradie, M. and F. D. Miller, 1984,` | 姓名年份错位（①） |
| aristotle-causality | gaiser-1969 `4ᵗʰ Simposium` | `4th Symposium` | 上标字符与拼写（①） |
| aristotle-causality | sauvé-1992 `101, 791–825` | `101: 791–825` | 卷页缺冒号（①） |
| aristotle-causality | balme-1987／cooper-1987 `Issues in Aristotle Biology` | `Issues in Aristotle’s Biology` | 缺 ’s（①） |
| aristotle-causality | la-1976／gotthelf-1976 `1976/1977,“` | `1976/1977, “` | 逗号后缺空格（①） |
| aristotle-causality | wardy-1993 `1993,“` | `1993, “` | 逗号后缺空格（①） |
| aristotle-causality | boeri-1995 `Aristotle Physics` | `Aristotle’s Physics` | 缺 ’s（①） |
| aristotle-causality | henning-2009／stein-2011 `,”<em>` | `,” <em>` | 引号后缺空格（①） |
| aristotle-causality | stein-2021 条末缺句点 | 补句点 | 缺标点（①） |
| aristotle-causality | judson-2005 `Teleology,”,` | `Teleology,”` | 双标点（①） |
| aristotle-causality | furley-1999 `Aristotle’ Final Cause` | `Aristotle’s Final Cause` | 缺 s（①） |
| binarium | notes 引 Baur 拉丁文 `proporitionem` | `proportionem` | 拼写（①） |
| binarium | gilson-1955 `Institut supérieure de philosophie` | `supérieur` | 法语性数配误（①） |
| timon-phlius | decleva 2020 条 `Declava Caizzi` | `Decleva Caizzi` | 姓氏拼写（①） |
| truth-coherence | 正文 `(Candlish 2006)` | `(Candlish 2021)` | 正文年份与书目 2021 矛盾（②） |
| bergson | 正文 `Soulez & Worms 2002` | `Soulez et Worms 2002` | 同书两种写法（②） |
| bergson | 引文 `Avertissement … septième edition` | `édition` | 法文重音缺失（①） |
| olympiodorus | 正文 `Opsomer 2011`（书目为 2010） | `Opsomer 2010` | 年份与书目矛盾（②） |
| olympiodorus | opsomer-2010 `“Olymiodorus”` | `“Olympiodorus”` | 拼写（①） |
| olympiodorus | joosse-2021c `Twi New Translations` | `Two New Translations` | 拼写（①） |
| peirce-benjamin | 正文 `James Mills (1834–1906)`／`Benjamin Mills (1844–1870)`／`Herbert Henry Davis (1849–1916)` | 各补姓氏 `Peirce` | 三人为皮尔斯之子，脱姓（①②） |
| scholem | `Wohlfahrt, Irving`（正文与书目，2 处） | `Wohlfarth, Irving` | 学者姓氏拼写，Deutsche Biographie 作 Irving Wohlfarth（①） |
| scholem | ms 条 `New York: Schocken Books. Page numbers from the 1991 translation.` | 补出版年 `Schocken Books, 1991.` | 英译条缺出版年（①） |
| scholem | zadoff-2014 书名逗号误入斜体：`Das Leben des Werner Scholem,</em>`；译名条 `(trans.) Philadelphia: … Press 2018.` | 逗号移出斜体、补 `(trans.)` 后逗号与出版年逗号 | 体例（①） |
| environmental-aesthetics | lorenz-1950 `Studium Generale: Eitschrift` | `Zeitschrift` | 拼写（①） |
| environmental-aesthetics | erzen-2013 `Sassari: Edzione Edes` | `Sassari: Edizione EDES` | 出版者名拼写（①；官方版权页作 EDIZIONE EDES） |
| environmental-aesthetics | hepburn-1966 丛书括注置于篇名后 | 移至 *British Analytical Philosophy* 后 | 丛书信息位置（①） |
| environmental-aesthetics | hargrove-1979 篇名后缺逗号 | 补逗号 | 标点（①） |
| environmental-aesthetics | hettinger-2005 篇名末 `Environment:”`；loftis-2003 `Ethics”:` | 删多余冒号 | 标点（①） |
| environmental-aesthetics | orians-1986 空章号 `(ch. )` | 删除 | 占位残留（④） |
| environmental-aesthetics | ruskin-1846 `Smith, Elder&Co.` | `Smith, Elder & Co.` | 缺空格（①） |
| environmental-aesthetics | stecker-1999 `Amsterdam ; Atlanta`（窄空格＋分号） | `Amsterdam; Atlanta` | 标点（①） |
| environmental-aesthetics | gladden-obidzińska-2021 `special issue of … special volume 9` | `special volume 9 of *Contemporary Aesthetics*` | 语义重复（①） |
| environmental-aesthetics | zangwill-2005b `Revista di Estetica,</em>` | 逗号移出斜体 | 体例（①） |
| environmental-aesthetics | hill-2007 书目作 2007，正文引 Hill & Daniel 2008（21(1): 34–49 即 2008 年卷） | 书目改 2008 | 正文书目矛盾（②） |
| environmental-aesthetics | 正文 Hanich 2023，书目 hanich-2024（28(2), 2024） | 正文改 2024 | 正文书目矛盾（②） |
| bayes-theorem | 正文 `(Brinbaum 1962, 272)` | `(Birnbaum 1962, 272)` | 姓氏拼写（①） |
| bayes-theorem | 书目 `Sphon, W.`、注 1 `(Sphon, 1986)` | `Spohn` | 姓氏拼写（①） |
| bayes-theorem | 注 11 `(Halina 1988)` 以名代姓 | `(Mortimer 1988)` | 作者为 Halina Mortimer（②） |
| bayes-theorem | renyi-1955 `Scientiarium` | `Scientiarum` | 拼写（①） |
| bayes-theorem | bayes-1764 链接文字 `Fascimile` | `Facsimile` | 拼写（①） |
| bayes-theorem | hammond-1994 `Representations for of Probability` | `Representations of Probability` | 衍字（①） |
| bayes-theorem | 注 1 `probabilty` | `probability` | 拼写（①） |
| imprecise-probabilities | 正文 `要思想家` | `重要思想家`（缺字） | 缺字（①） |
| imprecise-probabilities | 11 条卷期页 `192:5 1527–1542` 式 | `192(5): 1527–1542` | 卷期与页码间缺冒号（①） |
| imprecise-probabilities | carr-2015 `2015 “Chancy…”`、`Topics 29 67–81` | 补逗号、`29: 67–81` | 标点（①） |
| imprecise-probabilities | ferson-1996 `Ginzburg,1996`、`54 133–144`；ferson-2004 `85 135–152` | 补空格与冒号 | 标点（①） |
| imprecise-probabilities | finetti-1964 书名重复、`Wiley. New York.` | 删重复、`New York: Wiley.` | 衍文与出版地倒置（①） |
| imprecise-probabilities | good-1983 书名重复、`University of Minnesota Press. Minnesota.` | 删重复、`Minneapolis: University of Minnesota Press.` | 衍文与出版地倒置（①） |
| imprecise-probabilities | hart-2015 `Hart. Casey`、`4 252–262` | `Hart, Casey`、`4: 252–262` | 标点（①） |
| imprecise-probabilities | miranda-2008 `Approcimate` | `Approximate` | 拼写（①） |
| imprecise-probabilities | williams-1976 `Przelęcki` | `Przełęcki` | 拼写（①） |
| imprecise-probabilities | wheeler-2011 `Malcom Forster`、`North-Holland. Amsterdam.` | `Malcolm`、`Amsterdam: North-Holland.` | 拼写与出版地倒置（①） |
| imprecise-probabilities | trautmann-2016 `Guijs van der Kuilen`、`2016 “Ambiguity…` | `Gijs van de Kuilen, 2016, “` | 拼写与标点（①） |
| imprecise-probabilities | ruggeri-2005 `25 623–667, Elsevier. Amsterdam` | `25: 623–667, Amsterdam: Elsevier.` | 标点与出版地倒置（①） |
| imprecise-probabilities | konek-nd `forthcoming “`、条末无句点 | 补逗号与句点 | 标点（①） |
| imprecise-probabilities | bradley-2016 `3:20`、bradley-2019／2016-2 条末无句点；voorhoeve-2016 `Stewart,2016` | 补冒号／句点／空格 | 标点（①） |
| buridan | `Dutihl Novaes, C.`（2 处） | `Dutilh Novaes` | 姓氏拼写（①） |
| buridan | normore-1985 `“Buridan’s Ontology,” ed. James Bogen, and James E. McGuire, <em>How Things Are…` | `in <em>How Things Are: …</em>, James Bogen and James E. McGuire (eds.),` | 编者结构与 in 缺失（②） |
| buridan | klima-2009 `Oxford-New York: Oxford.` | `Oxford-New York: Oxford University Press.` | 出版者残缺（①） |
| buridan | lines-2005 `Ethics</em>,”in` | `,” in` | 缺空格（①） |
| buridan | flüeler-1999 条末 `497–521` 无句点 | 补句点 | 标点（①） |
| buridan | thijssen-2001 两位编者作 `(ed.)` | `(eds.)` | 体例（①） |
| buridan | streijger-2010 `Aristotelis</em>,”,` 引号与斜体次序错乱 | `Aristotelis”</em>,` | 标点（①） |
| buridan | Klima/Sobol/Hartman/Zupko 2023 在 Modern 与 Translations 两区重复登记 | 删 Modern 区一条 | 重复条目（①） |
| xenocrates | Horky 2013 同文重复登记（一条引号错乱 `”Pythagorean“`） | 删畸形条，保留规范条 | 重复条目（①） |
| xenocrates | dörrie-1998 `philosophisce` | `philosophische` | 拼写（①） |
| xenocrates | garcía-2024 `<em>Themistius. Paraphrase of Aristotle</em>, De anima.` | 全题名入斜体 | 斜体断裂（①） |
| xenocrates | gutas-2010 `<em>Theophrastus</em> On First Principles (<em>known as his</em> Metaphysics)` | 全题名入斜体 | 斜体断裂（①） |
| xenocrates | raffa-2016 `<em>Claudio Tolemeo.</em> Armonica<em>. Con il…</em>` | 全题名入斜体 | 斜体断裂（①） |
| xenocrates | petrucci-2022 `“Platone. <em>Timeo</em>”. Introduzione` | `<em>Platone. Timeo</em>. Introduzione` | 斜体断裂（①） |
| xenocrates | calchi-2023 `Calchi, V,.`、`<em>The Theology of the</em> Epinomis` | `V.,`、整题名斜体 | 标点与斜体（①） |
| xenocrates | heinze-1892 `Stuttgart: Teubner, 1892` | `Stuttgart: Teubner` | 年份重复（①） |
| xenocrates | rashed-2004 `<em>&Alpha;rabic Sciences…` | `Arabic` | 希腊字母混入（①） |
| xenocrates | timotin-2012 `Brill: Leiden-Boston` | `Leiden-Boston: Brill` | 出版地倒置（①） |
| xenocrates | mansfeld-2020 `Runia, D, 2020` | `and D. Runia, 2020` | 标点（①） |
| xenocrates | 五条重复作者标记 `&ndash;&ndash; 20xx` | `&ndash;&ndash;&ndash;, 20xx` | 破折号缺一（①） |
| xenocrates | 正文 `Calchi 2020`（书目作 2023） | `Calchi 2023` | 正文书目矛盾（②） |
| holkot | 正文 `*Quod.*`／`*Quodl*.`／`*Quod*.` 三种缩写混用 | `*Quodl.*` | 同书缩写不一（①） |
| holkot | 正文 `f. f2ra` | `f. 2ra` | 衍字（①） |
| holkot | courtenay-1972 `Courtenay<em>, Covenant…` 逗号入斜体 | 逗号移出 | 体例（①） |
| holkot | hoffmann-1963 `Iher Ursprung` | `Ihr Ursprung` | 拼写（①） |
| holkot | keele-2007 `<em>Theological </em>quodlibeta<em> in the Middle Ages…` 斜体断裂、条末无句点 | 整题名斜体、补句点 | ① |
| holkot | kirjavainen-1990 `Congresss` | `Congress` | 拼写（①） |
| holkot | o’mara-1963（Part II，Chaucer Review 27(1)） | 1992（Part I 为 1992，卷次属 1992） | 年份倒置（②） |
| holkot | tachau-1987-2 `de Riijk` | `de Rijk` | 拼写（①） |
| holkot | grassi-1979 `71: 49-79` | `49&ndash;79` | 连接号（①） |
| holkot | tachau-1988 `geistesgeschichte` | `Geistesgeschichte` | 专名大小写（①） |
| representation-medieval | brower-2008 `117 (2): 1937&ndash;243` | `193&ndash;243` | 页码衍字（①） |
| representation-medieval | toivanen-2009 `Jyvaskyla`（2 处） | `Jyväskylä` | 变音符缺失（①） |
| representation-medieval | klima-2015 `New York: Fordham University.` | `Fordham University Press.` | 出版者残缺（①） |
| representation-medieval | panaccio-2017 `G.Klima (ed.)` | `G. Klima (ed.),` | 缺空格与逗号（①） |
| representation-medieval | tweedale-1990 `(ed.) <em>Historical` | `(ed.), <em>` | 缺逗号（①） |
| necessary-sufficient | 正文 `Downing1959` | `Downing 1959` | 缺空格（①） |
| necessary-sufficient | nebel-2019 `Nebel, Jacob 2019`、moore-2009 `Parker, Richard 2009` | 补逗号 | 体例（①） |
| necessary-sufficient | crupi-2020 `<em>Erkenntnis</em> 2020.` 年份重复 | `Erkenntnis.` | 衍字（①） |
| necessary-sufficient | gomes-2020 条 `<li>` 闭合写成 `-1/li>` | `</li>` | 标签破损（①） |
| necessary-sufficient | rothman-1976 `104:587&ndash;92 ` | `104: 587&ndash;92.` | 标点与空格（①） |
| necessary-sufficient | vanderweele-2017 `185, 11: 1041&ndash;1043` | `185(11): 1041&ndash;1043` | 卷期体例（①） |
| necessary-sufficient | 正文 `Nebel 2018`（书目 2019）、`von Fintel 1998`（书目 1997） | 改 2019／1997 | 正文书目矛盾（②） |
| cordemoy | `l’áction des corps`（正文与书目 2 处） | `l’action` | 重音误（①） |
| cordemoy | `l’Academie Français` | `l’Académie française` | 重音与性数（①） |
| cordemoy | `l’eclaircissement`、`lettre ecrite`（2 处）、`un cartesien` | 补 é | 重音缺失（①） |
| cordemoy | guerrini-1994 `Occasinalismo`、`filosophia` | `Occasionalismo`、`filosofia` | 拼写（①） |
| cordemoy | rosenfeld-1968 `Descartes to Le Mettre` | `La Mettrie` | 人名拼写（①） |
| cordemoy | nadler-2005 `“ Cordemoy…` | `“Cordemoy…` | 引号内多空格（①） |
| cordemoy | scheib-1997 `New York, Frankfurt am Main: P. Lang.` | `New York: P. Lang.` | 双出版地（①） |
| cordemoy | manning-2012 `12 (16); <a…` | `12(16). <a…` | 缺句点（①） |
| simon-faversham | donati-2003 `Aertsen zum 65</em>, Berlin/NY: Geburtstag` | `zum 65. Geburtstag</em>, Berlin/NY` | 书名与出版地拆散（①） |
| simon-faversham | ottaviano-1930 `Nazionale die Lincei` | `Nazionale dei Lincei` | 拼写（①） |
| simon-faversham | marmo-1995 `Sprachteorien in Spätantiken un Mittelalter`、`Geschichte der Sprachteorie` | `Sprachtheorien in Spätantike und Mittelalter`、`Sprachtheorie` | 拼写（①） |
| simon-faversham | pattin-1955 斜体断裂与 `België;` 分号 | 合并斜体、删分号 | 体例（①） |
| simon-faversham | vennebusch-1963 `des xiii.</em> <em>Jahrhunderts` 斜体断裂 | 合并 | 体例（①） |
| simon-faversham | tiné-1996 `…Middle Ages</em>. <em>Proceedings…` 斜体断裂 | 合并 | 体例（①） |
| simon-faversham | pinborg-1967 `Münster, Aschendorff.` | `Münster: Aschendorff.` | 体例（①） |
| simon-faversham | ebbesen-1986 `13<sup>th</sup>` 上标字符 | `13th` | 体例（①） |
| paradox-suspense | `more suspenseful on repeated to encounters` | `repeated encounters` | 衍字（①） |
| paradox-suspense | `<i>Touching the Void</i> (2004)` | `(2003)` | 上映年份误（②；影片 2003 年上映） |
| paradox-suspense | `<i>Michael Clayton</i> (2008)` | `(2007)` | 上映年份误（②；影片 2007 年上映） |
| paradox-suspense | gerrig-1997／smuts-2004 条末缺句点 | 补句点 | 标点（①） |
| paradox-suspense | mag-2011a／mag-2011b／smuts-2008 题名后缺逗号 | 补逗号 | 标点（①） |
| gersonides | perush-nd `Perush ‘al Sefer lyob` | `Iyob` | 拼写（①） |
| gersonides | sefer-1909 括号未闭合 `…Gerson Lange (Frankfurt am Main: Golde, 1909).` | 改 `…Gerson Lange. Frankfurt am Main: Golde, 1909).` | 括注错乱（①） |
| gersonides | goldstein-1992 篇名未加引号 `1992, Levi Ben Gerson’s Contributions…` | `1992, “Levi Ben Gerson’s Contributions to Astronomy”, in …` | 体例（①） |
| gersonides | green-2016 `Palgrave: MacMillan` | `Palgrave Macmillan` | 出版者体例（①） |
| gersonides | kellner-2010 `Boston, Academic Studies Press.` | `Boston: Academic Studies Press.` | 体例（①） |
| gersonides | klein-braslavy-1989 `<em>Da’ at</em>` | `Da’at` | 缺空格（①） |
| gersonides | husik-1916 `1916–1918,“Studies` | 补空格 | 标点（①） |
| gersonides | sirat-2003 `Les methodes`、touati-1973 `Les Editions` | 补 é／É | 重音缺失（①） |
| gersonides | glasner-2015 `Glasner, Ruth. 2015` | `Glasner, Ruth, 2015` | 标点（①） |
| gersonides | 正文 `(See North 1986, p. 25)`（书目仅 north-1989） | `North 1989` | 正文书目矛盾（②） |
| logic-fuzzy | běhounek-2014 编者名 `&#321;ukasiewicz, Thomas` | `Lukasiewicz, Thomas`（带 Ł 误置，编者为奥地利学者 Thomas Lukasiewicz） | 拼写（①） |
| logic-fuzzy | flaminio-2011 `Petr Hájek(eds.)`、hájek-2011 `Carles Noguera(eds.)` | 补空格 | 体例（①） |
| logic-fuzzy | hájek-2011 作者列 `Hájek, Petr, Franco Montagna, Carles Noguera` | 末作者前补 and | 体例（①） |
| logic-fuzzy | takeuti-1984 `Satako Titani` | `Satoko` | 拼写（①） |
| logic-fuzzy | nguyen-2005 缺出版地 | 补 `Boca Raton:` | 缺出版地（①） |
| logic-fuzzy | gödel-1932 `Anzeiger Akademie Der Wissenschaften Wien` | `Anzeiger der Akademie der Wissenschaften in Wien` | 期刊名体例（①） |
| logic-fuzzy | paris-2000 `(Studies in Fuzziness and Soft Computing. Volume 57)` | 逗号 | 标点（①） |
| logic-fuzzy | fermüller-2015 缺 `in` | 补 | 体例（①） |
| logic-fuzzy | zh 端 `[^supplementary-nd]`／`[^bibliography-nd]` 英文残句 | 改节首说明行「**补充文献：**」 | ①④ |

## 五、2026-11-15 续批（zombies 回炉 s2.5 增项发现）

| slug | 原串 | 改正 | 依据 |
| ---- | ---- | ---- | ---- |
| zombies | 正文 `; compare Latham 2000, 72f.).` | `; compare Latham 2000, 72f.` | 段内括号计票 5 开 6 闭，句末 `)` 无对应开括号（编辑残迹）；Yablo／Chalmers 两括号各自闭合在案 |

## 六、2026-11-15 续批（xenophanes 回炉 s0 补课发现）

| slug | 原串 | 改正 | 依据 |
| ---- | ---- | ---- | ---- |
| xenophanes | 正文 B16 `Thracians that theirs are are blue-eyed and red-haired.` | `Thracians that theirs are blue-eyed and red-haired.` | 衍字（①）：引文句法只需一个 are（Ethiopians 分句同构），双写为编辑残迹；drift_scan unchanged 证明上游原文如此 |
| xenophanes | 正文 B14 `wear their own clothers and have a voice and body` | `wear their own clothes and have a voice and body` | 拼写（①）：clothers 非英语词，B14 通行译文为 clothes；drift_scan unchanged 证明上游原文如此 |

## 六、2026-11-15 续批二（zhu-xi s0 前置发现）

| slug | 原串 | 改正 | 依据 |
| ---- | ---- | ---- | ---- |
| zhu-xi | 正文 `and the *Mean* of the the nature endowed in humans by heaven` | 删一 `the` | 冠词重复（①）；句式为 Confucius…Mencius…and the *Mean* of the nature…平行结构，双 `the` 非法 |
| xenocrates | 研究文献节重复著录 `<li>Isnardi Parente, Margherita, 2012, <em>Senocrate-Ermodoro: Frammenti</em>, Naples: Bibliopolis, 1982 (includes an Italian translation of the fragments); new, revised edition, by T. Dorandi, Pisa: Edizioni della Normale.</li>` | 删除该 `<li>` | 结构错位（③）：同一文献（Frammenti 1982 初版＋2012 Dorandi 修订版）已在原始文献节两条分立著录，研究文献节再整条重复，上游编辑残迹；drift_scan unchanged 证明上游原文如此 |
| xenocrates | 正文 `see Aronadio-Tulli-Petrucci 2018 and Calchi 2020` | `…Calchi 2023` | 同页自相矛盾（②）：正文 2020 与书目唯一条目 Calchi, V., 2023（*The Theology of the Epinomis*, Routledge）冲突，引称无歧义指该书；015 轮已修书目行 punct/斜体，本轮补正文侧 |
| xenocrates | 正文 `Fleisher 2018, 175–176 = T 1 IP` | `Fleischer 2018` | 同页自相矛盾（②）：正文引称与书目唯一 2018 条目作者 Fleischer, K. J.（Philodem, Geschichte der Akademie, Brill 2018）拼写冲突；zh 照录侧同步改 |
| yorck | 书目 `Press, pp.23–69.` | `Press, pp. 23–69.` | 缺空格（①）：pp. 后缺半角空格，同页 15 处 pp. N 惯例形对照可核；drift_scan unchanged 证明上游原文如此 |

## 七、2026-11-16 续批三（zhu-xi r1 数字对账发现）

| slug | 原串 | 改正 | 依据 |
| ---- | ---- | ---- | ---- |
| zhu-xi | 正文 `Lü Zuqian (1134–1181)`（两处） | `Lü Zuqian (1137–1181)` | 生年排印手误（①）；吕祖谦学界通行生卒 1137–1181（钱穆《朱子新学案》、束景南《朱子年谱长编》通行年表），译文已按通行形 |
