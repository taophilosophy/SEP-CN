# 词汇表孤儿键清单与处置口径（2026-11-10）

## 事实

| 指标 | 数值 |
| --- | --- |
| 词汇表行数/键数 | 1403 / 1385 |
| 与术语册交集 | 623 |
| 与人名表交集 | 341 |
| 孤儿键（两册皆无） | **421** |

启发式分解：作品 48、人名形 3、术语形 370。分类仅作分流依据，逐条裁定见下方清单。

## 处置口径（本轮裁定）

1. **词汇表定位为读者向精选表**，不扩为登记册镜像：登记册 4780 术语键 + 3673 人名键，若镜像则词汇表将达约 8.4k 行，
   既违反“单体文件 ≤1000 行”约束（ADR-0004），也背离前言词汇表的体例。
2. **作品类**：词汇表按表头已声明收录“书名译名对照”，此类不属术语/人名登记范围，机检豁免，不补登记。
3. **人名类**：按 ADR-0012 并入人名表（有通行汉名者登记主形，此形记亦作），或作为英文键别名。
4. **术语类**：按“先登记后使用”补登记进术语册，依据记“词汇表既定译名补登记（2026-11-10）”。
5. `check_terms` 新增孤儿键告警（不阻断），每轮收口时核对数量是否下降。

## 术语类（370 条）

| 词汇表行 | 英文键 | 现行译名 |
| --- | --- | --- |
| 600 | 3rd Earl of Shaftesbury | 第三代沙夫茨伯里伯爵 |
| 604 | Abd al-Latif | 阿卜杜勒·拉蒂夫 |
| 605 | Abduction | 溯因 |
| 607 | Abelard | 阿伯拉尔 |
| 612 | Academic Skepticism | 学园怀疑主义 |
| 613 | accommodation | 顺应；调节 |
| 614 | Account | 解释；说明；原理 |
| 617 | Adam Ferguson | 亚当·弗格森 |
| 622 | agent | 行动者 |
| 630 | Alan Turing | 艾伦·图灵 |
| 631 | Albalag | 阿尔巴拉格 |
| 632 | Albert | 阿尔伯特 |
| 633 | Albert Camus | 阿尔贝·加缪 |
| 638 | Alexander Gerard | 亚历山大·杰拉德 |
| 643 | Allan Ramsay | 艾伦·拉姆齐 |
| 647 | Ammonius | 赫尔米亚的阿莫尼俄斯 |
| 661 | Archytas | 阿尔库塔斯 |
| 662 | Argument | 论证 |
| 666 | Aspect | 体（体貌） |
| 668 | atomism | 原子论 |
| 669 | Attributes | 属性 |
| 671 | Auvergne | 奥弗涅 |
| 672 | Avempace | 伊本·巴哲 |
| 673 | Averroes | 阿威罗伊 |
| 674 | Averroism | 阿威罗伊主义 |
| 676 | awareness | 觉知；觉察 |
| 677 | axiomatic | 公理化 |
| 678 | Bacon | 培根 |
| 679 | bald | 秃头 |
| 681 | Basil Bessarion | 巴兹尔·贝萨里翁 |
| 682 | basing relation | 基础关系 |
| 683 | Baudrillard | 鲍德里亚 |
| 684 | Bauer | 鲍威尔 |
| 686 | Bayes’ Theorem | 贝叶斯定理 |
| 689 | beauty | 美 |
| 690 | Beauvoir | 波伏瓦 |
| 691 | behaviorism | 行为主义 |
| 696 | Bell’s Theorem | 贝尔定理 |
| 698 | Benjamin | 本雅明 |
| 699 | Benjamin Whichcote | 本杰明·惠科特 |
| 700 | Bentham | 边沁 |
| 701 | Bergson | 柏格森 |
| 702 | Berkeley | 贝克莱 |
| 703 | Bernard Bosanquet | 伯纳德·鲍桑葵 |
| 707 | Big Data | 大数据 |
| 708 | binarium famosissimum | 最著名的一对 |
| 709 | biological development | 生物发育 |
| 710 | biological individuals | 生物学个体 |
| 711 | biomedicine | 生物医学 |
| 712 | Black Holes | 黑洞 |
| 714 | Bloch | 布洛赫 |
| 716 | Bodin | 博丹 |
| 717 | body | 身体 |
| 718 | Boethius | 波爱修斯 |
| 720 | Bohmian | 玻姆 |
| 721 | Bohr | 玻尔 |
| 722 | Boltzmann | 玻尔兹曼 |
| 723 | Boole | 布尔 |
| 725 | Bosanquet | 鲍桑葵 |
| 726 | boundary | 边界 |
| 729 | Bradley | 布拉德雷 |
| 730 | Brentano | 布伦塔诺 |
| 731 | British Idealism | 英国观念论 |
| 732 | Brothers Karamazov | 卡拉马佐夫兄弟 |
| 733 | Brouwer | 布劳威尔 |
| 734 | Bruno | 布鲁诺 |
| 735 | Bruno Bauer | 布鲁诺·鲍威尔 |
| 738 | Burali-Forti | 布拉利-福尔蒂 |
| 739 | Buridan | 布里丹 |
| 740 | Burke | 伯克 |
| 741 | Burleigh | 伯利 |
| 742 | Burley | 伯利 |
| 743 | Butler | 巴特勒 |
| 744 | Byzantine | 拜占庭 |
| 746 | Callicles | 卡利克勒斯 |
| 747 | Cambridge Platonists | 剑桥柏拉图学派 |
| 748 | Campanella | 康帕内拉 |
| 749 | Camus | 加缪 |
| 750 | Cantor | 康托尔 |
| 754 | Cardano | 卡尔达诺 |
| 758 | Carnap | 卡尔纳普 |
| 760 | Cassirer | 卡西尔 |
| 761 | Causal Approaches | 因果方法 |
| 763 | Champeaux | 尚波 |
| 769 | City of the Sun | 太阳城 |
| 773 | Cohen | 科恩 |
| 774 | coherence theory | 融贯论 |
| 775 | Collapse | 坍缩 |
| 776 | Collapse Theories | 坍缩理论 |
| 779 | Commentators | 评注者 |
| 783 | Computing | 计算 |
| 792 | Consistent Histories | 一致性历史 |
| 795 | constructive | 构造性的 |
| 797 | Content Externalism | 内容外在主义 |
| 804 | Conventionality | 约定性；约定性的 |
| 808 | correspondence theory | 符合论 |
| 810 | Cudworth | 库德沃斯 |
| 816 | Dedekind | 戴德金 |
| 817 | deflationism | 紧缩论 |
| 820 | desert | 应得 |
| 821 | Determinacy | 决定性 |
| 823 | development | 发展；发育 |
| 827 | Diodorus | 狄奥多罗斯 |
| 831 | Discovery | 发现 |
| 832 | Djamila Boupacha | 贾米拉·布帕查 |
| 835 | doxographical tradition / doxography | 学说史传统；学说汇编 |
| 837 | Dugald Stewart | 杜格尔·斯图尔特 |
| 842 | Edmund Burke | 埃德蒙·伯克 |
| 844 | Einstein-Podolsky-Rosen | 爱因斯坦-波多尔斯基-罗森 |
| 848 | empirical | 实证 |
| 850 | empirical approaches | 经验主义研究 |
| 858 | Epistemology of Visual Thinking in Mathematics | 数学中的视觉思维认识论 |
| 859 | Ernst Bloch | 恩斯特·布洛赫 |
| 862 | Ethics | 伦理学 |
| 864 | ethics of belief | 信念伦理学 |
| 865 | Everettian | 埃弗雷特 |
| 867 | Experience | 经验；体验 |
| 871 | Extrinsic | 外在 |
| 872 | Faith in a Seed | 种子的信仰 |
| 873 | Fakhr al-Din | 法赫尔丁·拉齐 |
| 874 | Fall | 堕落 |
| 879 | Formal Approaches | 形式化方法 |
| 886 | Francis Hutcheson | 弗朗西斯·哈奇森 |
| 887 | Francisco Suárez | 弗朗西斯科·苏亚雷斯 |
| 889 | François-Marie d’Arouet | 弗朗索瓦-马里·阿鲁埃 |
| 895 | general idea | 一般观念 |
| 897 | Georg Cantor | 格奥尔格·康托尔 |
| 898 | George Berkeley | 乔治·贝克莱 |
| 900 | George Campbell | 乔治·坎贝尔 |
| 901 | George Turnbull | 乔治·特恩布尔 |
| 903 | Gershom Carmichael | 格肖姆·卡迈克尔 |
| 905 | Girolamo Cardano | 吉罗拉莫·卡尔达诺 |
| 906 | God’s Existence | 上帝存在 |
| 907 | Gravity | 引力 |
| 908 | Great Learning | 大学问 |
| 909 | Greek sources | 希腊文献 |
| 910 | Grouchy | 格鲁希 |
| 912 | Hans Vaihinger | 汉斯·费英格 |
| 914 | Henri Bergson | 亨利·柏格森 |
| 916 | Henry Home | 亨利·霍姆 |
| 919 | Herbert Simon | 司马贺 |
| 920 | Herbert Spencer | 赫伯特·斯宾塞 |
| 921 | Hermann Cohen | 赫尔曼·科恩 |
| 922 | Hermann Weyl | 赫尔曼·外尔 |
| 923 | Hermeias | 赫尔米亚 |
| 928 | Hugh Blair | 休·布莱尔 |
| 932 | Ibn Bâjja | 伊本·巴哲 |
| 934 | Ibn Rushd | 伊本·鲁世德 |
| 935 | Ibn Sina | 伊本·西那 |
| 936 | Ibn ‘Arabî | 伊本·阿拉比 |
| 938 | Identity | 同一性 |
| 939 | identity theory | 同一论 |
| 940 | Ikhwān al-Ṣafā’ | 精诚兄弟社 |
| 942 | implicit bias | 内隐偏见 |
| 944 | Incommensurable | 不可通约性 |
| 945 | independence | 独立性 |
| 949 | Individuals | 个体 |
| 952 | Inertial Frames | 惯性系 |
| 957 | inherence | 依存；寓存 |
| 958 | inner speech | 内部言语 |
| 965 | Intrinsic | 内在 |
| 967 | Intuitionistic | 直觉主义 |
| 970 | Isaac Albalag | 以撒·阿尔巴拉格 |
| 974 | James Beattie | 詹姆斯·比蒂 |
| 975 | James Burnett | 詹姆斯·伯内特 |
| 976 | James Dunbar | 詹姆斯·邓巴 |
| 977 | James Hutton | 詹姆斯·赫顿 |
| 978 | Jean Baudrillard | 让·鲍德里亚 |
| 979 | Jean Bodin | 让·博丹 |
| 981 | Jeremy Bentham | 杰里米·边沁 |
| 983 | Johann Sturm | 约翰内斯·施图尔姆 |
| 988 | Judah Abrabanel | 犹大·莱昂·阿布拉瓦内尔 |
| 991 | Just Assassins | 正义者 |
| 992 | Justification | 证成 |
| 998 | Khayyam | 海亚姆 |
| 999 | Kochen-Specker | 科亨-施佩克尔 |
| 1000 | KS Theorem | KS 定理 |
| 1001 | Lange | 朗格 |
| 1002 | Large Cardinals | 大基数 |
| 1003 | Latin America | 拉丁美洲 |
| 1004 | Latin West | 拉丁西方 |
| 1007 | Leo Strauss | 列奥·施特劳斯 |
| 1013 | logical atomism | 逻辑原子主义 |
| 1015 | Long March | 长征 |
| 1016 | Lord Keeper of the Seal | 掌玺大臣 |
| 1017 | Lord Monboddo | 蒙博多勋爵 |
| 1222 | Lord Shaftesbury | 沙夫茨伯里勋爵 |
| 1019 | Ludwig Boltzmann | 路德维希·玻尔兹曼 |
| 1020 | Ludwig Wittgenstein | 路德维希·维特根斯坦 |
| 1030 | mañana paradox | 明天悖论 |
| 1025 | Margarete Susman | 玛格丽特·苏斯曼 |
| 1031 | McTaggart | 麦克塔格特 |
| 1036 | Methods | 方法 |
| 1039 | Modal Interpretations | 模态解释 |
| 1041 | modal metaphysics | 模态形而上学 |
| 1045 | Montague | 蒙太古 |
| 1046 | moral desert | 道德应得 |
| 1052 | Moral Vegetarianism | 伦理素食主义 |
| 1053 | More | 莫尔 |
| 1054 | most famous pair | 最著名的一对 |
| 1058 | Myths | 神话 |
| 1060 | Natorp | 那托普 |
| 1069 | Naturalistic Approaches | 自然主义方法 |
| 1070 | neo-Kantianism | 新康德主义 |
| 1072 | Nicolaus Taurellus | 尼古拉斯·塔雷路斯 |
| 1074 | Niels Bohr | 尼尔斯·玻尔 |
| 1080 | non-wellfounded | 非良基 |
| 1081 | Nova Atlantis | 新大西岛 |
| 1083 | Nuptials | 婚礼集 |
| 1085 | Nyāya-Vaiśeṣika | 正理-胜论派 |
| 1087 | observation | 观察 |
| 1092 | ontic structural realism | 本体的结构实在论 |
| 1103 | Paul Natorp | 保罗·那托普 |
| 1107 | Peter Abelard | 彼得·阿伯拉尔 |
| 1111 | Phenomenological Approaches | 现象学方法 |
| 1112 | Philo | 斐洛 |
| 1114 | Philoponus | 菲洛波努斯 |
| 1122 | Plague | 鼠疫 |
| 1124 | Platonism | 柏拉图主义 |
| 1125 | Platonists | 柏拉图主义者 |
| 1127 | pluralism | 多元主义 |
| 1128 | pluralist theories | 多元论 |
| 1134 | possible world | 可能世界 |
| 1135 | possible worlds | 可能世界 |
| 1136 | Post-Newtonian | 后牛顿 |
| 1139 | pragmatic | 语用（的）；实用（的） |
| 1141 | Pragmatist | 实用主义者 |
| 1148 | problem of universals | 共相问题 |
| 1149 | Progress | 进步 |
| 1151 | Proof-Theoretic | 证明论 |
| 1153 | property | 属性；性质 |
| 1154 | Pseudo-Science | 伪科学 |
| 1161 | QFT | 量子场论 |
| 1162 | Quantum Approaches | 量子研究方法 |
| 1167 | Quantum-Bayesian | 量子贝叶斯模型 |
| 1173 | Razi | 拉齐 |
| 1175 | Realism | 实在论 |
| 1176 | Rebel | 反抗者 |
| 1178 | Regress | 倒退 |
| 1179 | Reinhold | 莱因霍尔德 |
| 1180 | Relational | 关系性 |
| 1184 | Representation | 表征 |
| 1186 | Research | 研究 |
| 1187 | Retrocausality | 逆因果关系 |
| 1188 | revision theory | 修正论 |
| 1189 | Revolutions | 革命 |
| 1190 | Rigor | 严谨性 |
| 1192 | Rudolf Carnap | 鲁道夫·卡尔纳普 |
| 1194 | Samuel | 塞缪尔 |
| 1195 | Samuel Alexander | 塞缪尔·亚历山大 |
| 1197 | Sartre | 萨特 |
| 1200 | Schelling | 谢林 |
| 1201 | Science | 科学 |
| 1202 | scientific knowledge | 科学知识 |
| 1203 | Scientific Method | 科学方法 |
| 1207 | Scientific Theory | 科学理论 |
| 1209 | Second Sex | 第二性 |
| 1211 | Self-Deception | 自我欺骗 |
| 1212 | Self-Defense | 自卫 |
| 1213 | Self-Doubt | 自我怀疑 |
| 1215 | Self-Locating | 自我定位 |
| 1216 | Self-Locating Beliefs | 自我定位信念 |
| 1217 | Self-Reference | 自我指涉 |
| 1218 | Semantics | 语义 |
| 1221 | Set Theory | 集合论 |
| 1224 | Sherwood | 舍伍德 |
| 1228 | Simone Weil | 西蒙娜·薇依 |
| 1231 | Singularities | 奇点 |
| 1233 | social construction | 社会建构 |
| 1235 | Social Dimensions | 社会维度 |
| 1236 | Social Institutions | 社会制度 |
| 1237 | social minimum | 社会最低保障 |
| 1238 | Social Networking | 网络社交 |
| 1239 | Social Norms | 社会规范 |
| 1242 | Socialism | 社会主义 |
| 1246 | Sortals | 种类词 |
| 1248 | Sounds | 声音 |
| 1253 | Spencer | 斯宾塞 |
| 1259 | St. Petersburg | 圣彼得堡 |
| 1262 | statistical physics | 统计物理学 |
| 1263 | Stevenson | 史蒂文森 |
| 1264 | Stirner | 施蒂纳 |
| 1265 | Stoicism | 斯多葛主义 |
| 1266 | Stranger | 局外人 |
| 1267 | Strauss | 施特劳斯 |
| 1268 | Strawson | 斯特劳森 |
| 1271 | Structure | 结构 |
| 1272 | Stumpf | 斯图姆夫 |
| 1273 | Sturm | 施图尔姆 |
| 1284 | Suárez | 苏亚雷斯 |
| 1280 | Supertasks | 超级任务 |
| 1283 | Susman | 苏斯曼 |
| 1286 | Syrianus | 西里阿努斯 |
| 1288 | Tarski | 塔尔斯基 |
| 1289 | Taurellus | 塔雷路斯 |
| 1291 | Teleological | 目的论 |
| 1292 | Teleological Arguments | 目的论论证 |
| 1293 | Teleological Notions | 目的论观念 |
| 1294 | Telesio | 特莱西奥 |
| 1295 | temporal consciousness | 时间意识 |
| 1296 | Temporal Parts | 时间部分 |
| 1297 | Tense | 时态 |
| 1298 | Territorial Justice | 领土正义 |
| 1299 | Territorial Rights | 领土权利 |
| 1300 | Terrorism | 恐怖主义 |
| 1301 | testimony | 证言 |
| 1302 | Tetsurō | 哲郎 |
| 1304 | Theological Voluntarism | 神学意志主义 |
| 1305 | Theological-Political Treatise | 神学政治论 |
| 1307 | Theoretical Terms | 理论术语 |
| 1309 | Theory | 理论 |
| 1310 | theory of judgement | 判断理论 |
| 1311 | thermodynamic time asymmetry | 热力学时间非对称性 |
| 1313 | thin | 薄（的） |
| 1316 | Thought Experiments | 思想实验 |
| 1319 | Time | 时间 |
| 1320 | Time Machines | 时间机器 |
| 1321 | Time Travel | 时间旅行 |
| 1322 | Timon | 第蒙 |
| 1324 | Token | 殊例 |
| 1325 | Tokens | 殊例 |
| 1326 | Tommaso Campanella | 托马斯·康帕内拉 |
| 1329 | Tractatus Politicus | 政治论 |
| 1330 | Transcendental Arguments | 先验论证 |
| 1332 | Transformative Experience | 变革性体验 |
| 1333 | Transmission | 传递 |
| 1334 | Trinity | 三位一体 |
| 1335 | triumph | 胜利 |
| 1336 | Trust | 信任 |
| 1337 | Truth | 真理 |
| 1338 | truth definitions | 真理定义 |
| 1339 | truth values | 真值 |
| 1340 | Truthlikeness | 似真性 |
| 1341 | truthmakers | 使真者 |
| 1344 | Turing | 图灵 |
| 1345 | Turing machines | 图灵机 |
| 1346 | Turing test | 图灵测试 |
| 1347 | Two-Dimensional | 二维 |
| 1348 | type | 类型 |
| 1350 | Types | 类型 |
| 1351 | Umar Khayyam | 欧玛尔·海亚姆 |
| 1360 | Vaihinger | 费英格 |
| 1362 | Valla | 瓦拉 |
| 1363 | value | 价值 |
| 1364 | value theory | 价值论 |
| 1365 | Vasubandhu | 世亲 |
| 1366 | Vegetarianism | 素食主义 |
| 1369 | visual thinking in mathematics | 数学中的视觉思维 |
| 1370 | Vives | 维夫斯 |
| 1373 | Voting | 投票 |
| 1374 | Walden | 瓦尔登湖 |
| 1378 | War | 战争 |
| 1380 | Watsuji | 和辻 |
| 1381 | Watsuji Tetsurō | 和辻哲郎 |
| 1383 | Weil | 薇依 |
| 1385 | Weyl | 外尔 |
| 1386 | Whewell | 惠威尔 |
| 1387 | Whichcote | 惠科特 |
| 1388 | Whitehead | 怀特海 |
| 1389 | Wild Fruits | 野果 |
| 1396 | William Whewell | 威廉·惠威尔 |
| 1397 | Williams | 威廉姆斯 |
| 1398 | Wilson | 威尔逊 |
| 1399 | Windelband | 文德尔班 |
| 1400 | Wisdom | 智慧 |
| 1401 | Wittgenstein | 维特根斯坦 |
| 1404 | Zeno | 芝诺 |
| 1405 | Zermelo | 策梅洛 |
| 1406 | Zermelo-Fraenkel | 策梅洛-弗兰克尔 |
| 572 | 英语 | 中文 |

## 人名类（3 条）

| 词汇表行 | 英文键 | 现行译名 |
| --- | --- | --- |
| 625 | al-Baghdadi | 巴格达迪 |
| 626 | al-Farabi | 法拉比 |
| 629 | al-Razi | 拉齐 |

## 作品类（48 条）

| 词汇表行 | 英文键 | 现行译名 |
| --- | --- | --- |
| 602 | A Very Easy Death | 安详辞世 |
| 603 | A Week on the Concord and Merrimack Rivers | 河上一周 |
| 619 | Adieux: A Farewell to Sartre | 告别的仪式 |
| 642 | All Men are Mortal | 人都是要死的 |
| 644 | Alternative Axiomatic Set Theories | 替代性公理集合论 |
| 646 | America Day by Day | 美国纪行 |
| 654 | Anicius Manlius Severinus Boethius | 阿尼修斯·曼利乌斯·塞维利努斯·波爱修斯 |
| 656 | Anthony Ashley Cooper | 安东尼·阿什利·库珀 |
| 692 | Being and Nothingness | 存在与虚无 |
| 728 | Bounds of Sense | 感觉的界限 |
| 756 | Carl Friedrich Stumpf | 卡尔·弗里德里希·斯图姆夫 |
| 764 | Charles Leslie Stevenson | 查尔斯·莱斯利·史蒂文森 |
| 778 | Coming of Age | 老年 |
| 793 | Consistent Histories Approach | 一致性历史方法 |
| 834 | Donald Cary Williams | 唐纳德·卡里·威廉姆斯 |
| 856 | Epistemic Structural Realism | 认识论的结构实在论 |
| 863 | Ethics of Ambiguity | 模糊性的道德 |
| 885 | Francis Herbert Bradley | 弗朗西斯·赫伯特·布拉德雷 |
| 892 | Friedrich Albert Lange | 弗里德里希·阿尔贝特·朗格 |
| 982 | Johann Christoph Sturm | 约翰内斯·克里斯托夫·施图尔姆 |
| 985 | John Cook Wilson | 约翰·库克·威尔逊 |
| 1021 | Luitzen Egbertus Jan Brouwer | 勒伊岑·艾赫贝特斯·扬·布劳威尔 |
| 1038 | Mirror of Production | 生产之镜 |
| 1055 | Must We Burn Sade | 要焚毁萨德吗 |
| 1057 | Myth of Sisyphus | 西西弗神话 |
| 1082 | Novum Organum Scientiarum | 新工具 |
| 1108 | Peter Frederick Strawson | 彼得·弗雷德里克·斯特劳森 |
| 1115 | Philosophy of Sport | 体育哲学 |
| 1116 | Philosophy of Statistical Mechanics | 统计力学哲学 |
| 1117 | Philosophy of Statistics | 统计学哲学 |
| 1118 | Philosophy of Technology | 技术哲学 |
| 1158 | Pyrrhus and Cinéas | 皮瑞斯与辛尼阿斯 |
| 1163 | Quantum Field Theory | 量子场论 |
| 1170 | Rasâ’il | 《论文集》 |
| 1223 | She Came to Stay | 女宾 |
| 1227 | Simone de Beauvoir | 西蒙娜·德·波伏瓦 |
| 1244 | Sophie de Grouchy | 索菲·德·格鲁希 |
| 1255 | Speusippus of Athens | 雅典的斯彪西波 |
| 1260 | St. Petersburg paradox | 圣彼得堡悖论 |
| 1282 | Supervenience in Ethics | 道德随附性 |
| 1287 | System of Objects | 物体系 |
| 1411 | Ṯābit ibn Qurra | 塔比·伊本·库拉 |
| 1391 | The Will to Believe | 信仰的意志 |
| 1312 | Thick Ethical Concepts | 厚伦理概念 |
| 1315 | Thomas of Erfurt | 埃尔福特的托马斯 |
| 1343 | Tsongkhapa Losang Drakpa | 宗喀巴·洛桑札巴 |
| 1355 | Unity of Science | 统一科学 |
| 1394 | William of Champeaux | 尚波的威廉 |

