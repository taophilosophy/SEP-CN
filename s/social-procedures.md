# 社会程序的形式化进路 Formal Approaches to Social Procedures (van Eijck, Jan, Verbrugge, Rineke (L.C.))
*首次发表于 2014 年 9 月 8 日；2019 年 11 月 7 日实质修订。*

具有算法面向的社会程序，往往能通过重新设计而得到改进。投票及其他和平的决策程序如此，婚配、拍卖、遗产的公平分配，以及分配正义的许多程序亦然。这些算法面向可用形式化方法分析。“社会软件”一词由罗希特·帕里克（2002）创制，用以指称那门新兴的跨学科事业：它致力于设计并分析规制社会过程的算法。这类分析与（重新）设计，所凭借的是逻辑、博弈论与理论计算机科学的方法。[^note-1] 社会程序形式化进路的研究目标有三：为社会情境建模、发展正确性理论、重新设计社会程序，理想情况下还引出新的社会行为。

对社会机制有所言说的，并不只有逻辑、博弈论与计算机科学。投票理论、拍卖理论、社会选择理论、社会认识论、机制设计理论、算法博弈论，也都把这类机制当作研究对象；更抽象层面的多智能体互动，则由人工智能与分布式计算来研究。因此，上述学科都对社会互动的形式分析各有一得。

## 1 作为算法的社会程序

社会软件算不上一个界线分明、自成格局的研究领域，它更像是计算机科学、逻辑与博弈论中某几类研究的统称。尽管如此，这一以算法与信息为重的视角——它同时照看社会程序与智能互动——已经催生出形形色色的重要洞见。本文要讨论若干实例，并为哲学中的相关讨论指路。

数学中 **算法** 的典型例子（另见“可计算性与复杂性”词条），是欧几里得求两个正整数 $A$ 与 $B$ 最大公约数（GCD）的方子。所谓最大公约数，就是能同时整除两数而无余的最大整数。

> 如果 $A$ 比 $B$ 大，就把 $A$ 换成 $A - B$；反过来，如果 $B$ 比 $A$ 大，就把 $B$ 换成 $B - A$。照这样下去，直到 $A$ 等于 $B$ 为止。

最终得到的 $A = B$，即你起始时那两个数 $A$ 与 $B$ 的最大公约数。例如取 $A = 20$、$B = 12$ 起算：第一步 $A$ 换成 $20 - 12 = 8$，$8$ 成为新的 $A$；第二步 $B$ 换成 $12 - 8 = 4$，$4$ 成为新的 $B$；第三步 $A$ 换成 $8 - 4 = 4$，$4$ 成为新的 $A$，两数 $A$ 与 $B$ 已相等。算法便给出 $4$，即 $20$ 与 $12$ 的最大公约数。

欧几里得的方子是 **形式的**，因而可以用形式手段来分析。其正确性源于一个洞见：设有两数 $A$ 与 $B$，$A$ 大于 $B$，若以 $A - B$ 替换 $A$，这双数的公约数集合并不改变。

算法的形态与路数很多，串行、并行皆有。若想要计算机科学中有趣的算法导论，可看 Harel & Feldman（2004）与 Miller & Boxer（2012）。社会程序亦可循同样的路数，用逻辑与理论计算机科学的形式工具来分析。[^note-2]

最适合形式化进路的，看来是那些人们希望求得保证的社会程序：给定某些起始条件，程序能保持或创造出特定的期望性质。公平分配（第 2 节）、匹配（第 3 节）、通信（第 4 节）即是其例。最后，形式视角对需要参与者作策略推理的情境（第 5 节）也有用。这些情境有一个共同点：智能体对他人心理状态知道什么、不知道什么，都举足轻重。作为本文诸例的对照，Van Benthem（2018）就社会视角如今在计算机科学内部所占的位置提供了一份引人入胜的概览，突出了社会能动性与信息。

## 2 公平

形式化方法本身解决不了哲学问题——Padma（2007）记下的这则故事便是明证。

> 两个农夫罗摩与希亚姆在吃恰帕提。罗摩有 3 块这种扁圆的面饼，希亚姆有 5 块。一位满面饥疲的旅人骑马来到二人面前。罗摩与希亚姆决定分些恰帕提给他。三人把 8 块恰帕提叠成一摞（像叠煎饼），再把这摞切成三等份，均分了吃，直到一点不剩。旅人原是贵族，感激之下，为自己那一份吃食给了两个农夫 8 枚金币。
>
> 旅人走后，罗摩与希亚姆为这 8 枚金币怎么分犯难。罗摩说，金币 8 枚、人只两个，一人 4 枚才公道。希亚姆说：“这不公平——我起先可是有 5 块恰帕提。”罗摩觉得他说得有理，却又实在舍不得把 5 枚给出去，便提议去请教足智多谋的毛尔维。希亚姆答应了。
>
> 两人把事情原原本本讲给毛尔维。他思忖良久，说最公道的分法是希亚姆得 7 枚，罗摩只得 1 枚。两人都吃了一惊。待请毛尔维讲明道理，他们便心服了：这确是对 8 枚金币的公平分配。

参与者本可以为上述每一种分配各自给出理由，说明它何以公平：

1. 罗摩：“旅人若不来，我们本会把恰帕提平分。那么现在把八枚金币照样平分，才算得上 **公平**。”
2. 希亚姆：“旅人若不来，你会按市价向我买一块恰帕提。如今旅人这般慷慨，市价一下子涨到一块恰帕提一枚金币。如此说来，你的恰帕提值三枚金币，我的值五枚。”
3. 毛尔维：“旅人吃掉了八块恰帕提的三分之一。罗摩起先只有三块，故他吃了罗摩处的 $1/3$ 块、希亚姆处的 $7/3$ 块。要公平，罗摩就得一枚，希亚姆得七枚。”

这里的一个教益或许是：在此事上，也在许多事情上，并不存在什么显然正确的公平概念。形式分析总是从直觉起步，帮着把直觉磨成更精确的定义；随后可以检验某个程序是否合乎该定义。不过，合乎定义并不证明定义本身正确。

### 2.1 公平分配

社会程序与世界一样古老。**分割—选择**（也叫“我切你选”）是一种两人公平分配程序，可用于合意或不合意的异质物品。一方按自己认定的均等份额把物品分开，另一方先挑。倘若两位参与者对各部分估值不同，就可能出现双方都觉得自己拿到了五成以上的情形。设 $X$ 是代表待分物品的集合；$X$ 上的估值函数 $V$，是从 ${{\cal P}}(X)$ 到 $[0,1]$ 的函数，满足 $V(\emptyset) = 0$、$V(X) = 1$，且对一切子集 $A$、$B$，由 $A \subseteq B \subseteq X$ 可推出 $V(A) \leq V(B)$（记号说明见基本集合论补充材料）。设 $V_m$ 与 $V_y$ 分别是我与你对 $X$ 内容的估值。若 $V_m$ 与 $V_y$ 不同，就说明你我给 $X$ 中某些项目定的值不一样。由此可以推出——施泰因豪斯早在 1948 年就指出了这一点——存在一种分法，使双方都拿到超过应得的部分；“这一事实驳倒了那种流行的看法：估值上的差异会让公平分配变得困难”（Steinhaus 1948）[^steinhaus-1948]。

估值是否为对方所知，结果大不相同。切的一方可以利用这种知识。先看双方互不知情：你的估值我不晓得，我的估值你也不晓得。此时若由我切，所能做的最好的事，就是取集合 $A, B \subseteq X$，使 $A \cap B = \emptyset$、$A \cup B = X$ 且 $V_m(A) = V_m(B)$。若由你选，你会依 $V_y$ 在 $\{ V_y(A), V_y(B) \}$ 中挑大者。于是立刻可见：切能保底得到公平的一份，但也仅止于此；选却可能带来更好的交易。所以，双方只知道自己估值时，若让你在切与选之间抉择，把切让给对方于你有利。

不过，若估值成了共同知识（见“共同知识”词条），局面便翻转过来：此时更有利的是充当切者。作为切者，你可以设法把物品分成集合 $A$ 与 $B$：按对方的估值，$A$ 比 $B$ 略值钱；而按你自己的估值，$B$ 比 $A$ 值钱得多。

这个例子表明，知与不知的问题，对公平分配协议的分析至关重要。认知逻辑（见“认知逻辑”词条）能照亮社会互动中知识与不知情的许多微妙之处，公平分配问题尤其如此；至于一项显示知与不知何其要紧的切蛋糕实验，见 Kyropoulou et al. 2019。然而在公平分配的传统研究里，知识的角色一向未受考虑——Robertson & Webb（1998）对“切蛋糕算法”的全面研究即是明证。

### 2.2 三人以上的分蛋糕

在社会选择文献里（Brams 2005; Brams & Taylor 1996）[^brams-2005][^brams-1996]，人们惯常拿切蛋糕来比喻 **单一异质物品的划分**，继承时分割一块土地便是其例。蛋糕上的浇头各异，不可能块块切得成分相同：也许顶上缀着糖渍樱桃，甲喜欢，乙却厌恶，如此等等。若 $n$ 位参与者各按自己的估值，都觉得自己至少拿到了蛋糕的 $1/n$，这次分蛋糕便是 **简单公平的**。一个程序可以做到简单公平，却仍不免有人心里不痛快。若每人都觉得别人没有拿到更大的一块，这次分蛋糕便称作 **无嫉妒的**。判断一次分配是否无嫉妒，确凿的标志是没有人想跟别人交换手中那块。事实证明，要设计出既公平又无嫉妒的切蛋糕程序极为困难。**我切你选** 是公平的，而且天然无嫉妒——蛋糕剩下的部分仍是整块，嫉妒无从生起。无嫉妒性的哲学讨论，见“经济学［规范性］与经济正义”词条。

R. 帕里克（2002）分析过所谓的巴拿赫—克纳斯特切蛋糕算法，适用于把蛋糕公平分给至少三人的场合。算法如下：

> 我先切下一块，是给自己留的。其余人都来看这一块。若无人反对，这块就归我。若有人提出异议，她有权切下一片，把那片放回蛋糕的其余部分，然后问自己能否拿这块削小了的。若无人反对，她拿走；否则由旁人接过刀，再削去一点，如此继续，直到有人拿走这块修整过的。接着进入下一轮，只剩 $n-1$ 位参与者。到最后两位时，改用 **分割—选择** 算法。

帕里克的讨论表明，理论计算机科学的方法可以用来论证该程序公平。程序的关键，在于一个循环操作：

> 一直修整下去，直到无人再对其大小有异议。

设 $r$ 表示按巴拿赫—克纳斯特算法切下一块蛋糕、再把它放回蛋糕主体的动作；设 $F(m,k)$ 是“蛋糕主体足够 $k$ 人分”这一命题。那么一开始 $F(m,n)$ 当然成立：整只蛋糕对整组人本已够大。再者，帕里克（1983, 2002）用其博弈逻辑证明：$F(m,k)$ 在动作 $r$ 下保持不变——若 $F(m,k)$ 在 $r$ 之前为真，则 $r$ 发生之后仍为真。显然，若能证明 $F(m,k)$ 在整个算法中一路成立，$k$ 依次取 $n, \ldots, 1$，分配之公平便由此确立。[^note-3]

### 2.3 所罗门的判决

**分割—选择** 有一个变体，所罗门王在著名的“所罗门的判决”里就用过，两个妇人都自称孩子生母，争执不下。事情原委见《列王纪上》3:16–28。两个同住一屋的妇人各有一个男婴。一人声称，对方夜里不慎闷死了自己的儿子，便偷走了她的孩子；对方否认，反以同样的罪名相控。所罗门王听完陈述，命人取剑，宣布唯一的公平办法：把活着的孩子劈作两半，两位妇人各取一半。真母亲闻言高呼，宁可放弃孩子，只求留他一命；假母亲却赞同这一判决。这一举动让所罗门看出谁是生母，孩子便交还给她。

这个程序不能重复使用。圣经故事是这样写的：

> 以色列众人听见王判断的这事，就都敬畏王；因为他们看见他心中有上帝的智慧，能以断案。

不难想见，若再有第二桩类似的争讼，两位妇人都会喊出：“给她吧，只求留他一命！”

所罗门处理此事的方式，可以改造为一个可重复使用的社会程序。办法是：所罗门不取剑，而是把下面的程序讲给两位妇人听。他先问第一位妇人是否愿意放弃孩子；答“愿意”即了结此案，不再追问。否则就问另一位是否愿意放弃；答“愿意”同样了结。若两人都拒绝，孩子便归他所有，然后准许其中一位赎回孩子，价格这样定：两人各在纸上写一个数目，不署姓名。设两个出价为 $A$ 与 $B$，孩子的价格即定作 $\frac{A + B}{2}$，由命运决定哪一位以此价得子，另一位须缴一小笔罚金。两位妇人若是理性的，其中一位在被问及时就会放弃（见 Moore 1992 与 Pauly 2005；理性的哲学讨论见“实践理性与博弈论”“伦理学”词条）[^moore-1992][^pauly-2005]。

摩尔（1992）与保利（2005）都谈到，在所罗门这类案子里，就共同知识与不知情作推理何其重要。比如：所罗门王并不知道谁是生母，而两位妇人对谁是真母亲却自始共同知晓，也因此知道真母亲出价必远高于对方。程序正因如此才安全。可见认知逻辑、尤其是共同知识，能照亮这样一个棘手的社会程序。若想读更传统的哲学导引，包括对公平、可操纵性与无嫉妒性的更详尽解释，见“经济学［规范性］与经济正义”词条。

下一节要表明，社会软件这一视角同样能照亮社会的匹配问题。此类问题从婚姻一路排到住院医师派往医院、大学录取程序、学生宿舍分配。

## 3 稳定婚姻问题

设有数目相等的男女两群，人人都想与异性结为夫妻；每位男子按严格次序列出自己对女子的偏好，每位女子亦然。**稳定婚姻匹配** 是男女之间的一一对应，其性质为：若某男子偏爱另一女子胜过自己的妻子，那么那位女子 **并不** 偏爱他胜过自己的丈夫；反之，若某女子偏爱另一男子胜过自己的丈夫，那么那位男子 **并不** 偏爱她胜过自己的妻子。

### 3.1 盖尔—沙普利算法

计算机科学家盖尔与沙普利证明：稳定匹配总是存在，并给出寻找这种匹配的算法，即所谓盖尔—沙普利算法（Gale & Shapley 1962）[^gale-1962]：

> 一开始，所有男子、所有女子都自由（未订婚）。
>
> 随后是若干轮：每位自由男子向他尚未求过婚、且最偏爱的女子求婚，并在名单上把她划去。女子若自由，便接受，两人订婚；女子若不自由，就把求婚者同现任未婚夫相比。她若更中意求婚者，便甩掉未婚夫——那人重又自由——并与求婚者订婚。
>
> 这样下去，直到男女两方全部订婚为止。

例如设有三名男子 $a, b, c$ 与三名女子 $d, e, f$，偏好名单如下（最偏爱的排在首位）：$a: edf$，$b: {\it fed}$，$c: {\it dfe}$，$d: {\it abc}$，$e: {\it cda}$，$g: {\it acb}$。于是 $a: {\it edf}$ 意为：$a$ 偏爱 $e$ 甚于 $d$，偏爱 $d$ 甚于 $f$。这里假定偏好是传递的，故 $a$ 也偏爱 $e$ 甚于 $f$。

这一情形的一个稳定匹配例子，可写作三对 $(a,e)$、$(b,f)$、$(c,d)$。注意女子 $d$ 最终跟了名单上排在最末的那位男子。可这个匹配依然稳定：$c$ 固然愿意拿丈夫去换另外两名男子中的任何一位，那两位却都不会答应——他们碰巧都娶了自己名单上排第一的女子。

要检验盖尔—沙普利算法是否总产出稳定匹配，可以这样做。显然，无人订婚的局面是稳定的。

对“订婚”映射 $E$ 来说，在女子集合 $W$ 与男子集合 $M$ 上稳定是什么意思？令 $m >_w m'$ 表示“$w$ 偏爱 $m$ 甚于 $m'$”（数值越大越好）。

**（1）**

对一切 $(m,w) \in E$：只要存在 $w'$ 使 $w' >_m w$，便不存在 $m'$ 使 $(m',w') \in E$ 且 $m >_{w'} m'$；

**（2）**

对一切 $(m,w) \in E$：只要存在 $m'$ 使 $m' >_w m$，便不存在 $w'$ 使 $(m',w') \in E$ 且 $w >_{m'} w'$。

说一位男子 **自由**，究竟何意？

**（3）**

自由男子的集合，应等于全体男子减去已订婚的男子。

其次来看算法单步中发生了什么。此步的前提是至少还剩一位自由男子 $m$；这位自由男子 $m$ 向他名单上尚未求过婚、排位最高的女子 $w$ 求婚。

分两种情形。若 $w$ 自由，$w$ 便接受求婚，两人订婚。新的订婚对集合是否稳定？只需检查新成的那一对 $(w,m)$。

- 假设存在某位自由的 $w'$，使 $w' >_m w$。这不可能，因为 $w$ 正排在 $m$ 名单之首。
- 假设存在 $m'$ 使 $m' >_w m$。那么 $m'$ 若已订婚，比如与 $w'$ 订婚，这必定意味着并非 $w >_{m'} w'$；否则 $m'$ 当初就会向 $w$ 求婚，而不是向 $w'$ 求婚。
- 新的自由男子名单等于旧名单去掉 $m$。这是对的，因为 $m$ 刚刚订婚。

再看另一种情形：设 $w$ 已经订婚。这又分两种子情形。若 $w$ 更中意现任未婚夫，便什么也不发生，所得的订婚对名单依旧稳定，自由男子名单也照旧——$m$ 求了婚，却被回绝。

若 $w$ 更中意 $m$ 而非现任未婚夫 $m'$，她便换人：订婚对集合中以 $(m,w)$ 取代 $(m',w)$。同样不难看出，所得的订婚对名单是稳定的；自由男子集合里，$m$ 换成 $m'$，这也妥当。

值得注意的是，盖尔—沙普利匹配算法极大地偏向求婚的一方。求婚方可以按偏好次序向任何候选人求婚；而受求婚的一方在程序开头，却必须对任何求婚都说“是”！若把算法中男女的角色对调，算出的仍是稳定匹配，只是这一个更有利于女子。

盖尔—沙普利程序的运行时间与男女数目的平方成正比（例如见 Cechlérová et al. 2005）[^cechlérová-2005]。皮尼等（2011）表明，参与者只要虚报真实偏好，就能轻易操纵程序的结果。所幸皮尼等也给出另一种程序，操纵它在计算上很难——要想出一种对个人有利的偏好虚报，本身就是一项计算复杂的任务。

盖尔—沙普利算法有许多重要应用，且不限于婚姻中介；盖尔与沙普利本人就讨论过大学录取程序（1962）。下一小节再介绍一项应用。

### 3.2 大学宿舍分配程序

帕里克与保利（2012）从社会软件的视角，考察盖尔—沙普利算法的一个变体——斯坦福宿舍抽签用它把学生分到房间。情形比婚姻设定复杂：学生并不给所有宿舍排完整次序，只给其中 8 所排序；而且他们还可以结组参加抽签。在宿舍情境里，学生反而有如实提交真实偏好的动机：抽签对他们而言 **不可操纵**。不过理论上，他们仍可在挑选提交偏好的那 8 所这一子集上作策略打算。

这一情形里，知识的问题颇有意思。算法虽挂在斯坦福的网页上，多数学生与管理者却并不真正懂得它怎么运作。因此不能假定斯坦福宿舍抽签是学生间的共同知识。这里似乎出现了一个有趣现象：多数学生即便承认不懂该算法，仍会说他们相信它公平（Parikh & Pauly 2012）[^parikh-2012]。

## 4 通信的逻辑

通信协议在分布式计算中不可或缺：所谓分布式计算，就是由分布式系统来算，而分布式系统是一组经通信网络彼此相连的计算机。通信协议从哲学上看也颇有意思，尤其在讨论隐私之价值的语境中（见“隐私”“计算与道德责任”词条）。形式化进路能帮着回答这类哲学问题：“安全性提高，隐私是否就必然减少？”

### 4.1 通信与分布式计算

下面的例子中，灵感不只从社会问题流向形式化解法，也反过来，从成功的社会实践流向形式化程序。分布式计算的许多算法，都与日常生活中的社会通信协议相通。一个例子是用“发言棒”规制同侪团体中的讨论与决策：棒子依次传递，只有持棒者才可发言（Nerburn 1999）[^nerburn-1999]。

由此社会程序而来的计算机通信协议，就是令牌环协议。分布式计算中的 **令牌环**，是一种网络：每台计算机恰好连到另外两台，网络内处处可达；一个“令牌”沿环形网络循环流转，通信只能由令牌当前的持有者发起。

有时计算机或网络故障会使令牌丢失。这时必须重新生成令牌，并保证只有一台计算机持有它。令牌环中重新生成令牌这一问题，称作 **首领选举问题**。下面给出它的一个算法：

> 设通信沿顺时针方向进行，且每台计算机都能分辨自己的顺时针邻居与逆时针邻居。设所有计算机的标识符互不相同（皆为正整数），且各机皆知自己的标识符。
>
> 每台计算机把自己的标识符沿环送出。计算机 $c$ 收到一个标识符时，$c$ 便与自己的相较：若大于自己的，$c$ 便转手送出；若小于自己的，$c$ 便弃之不问；若等于自己的，$c$ 即宣布自己为首领。

不难看出，这保证了标识符最大的计算机 $i_{\text{max}}$ 当选首领（见 Lynch 1996）[^lynch-1996]。至于环中有几台计算机，或哪台计算机是否知道环的大小、他机的标识符，都无需假定。协议的下一阶段，可由首领遍发一圈请求，令各机登记为非首领并停机。

再往上抽象一层，便是从分布式计算机或进程，转向互动的智能体，即多智能体系统。这些智能体可以是计算机、机器人、人、人的团队，或兼而有之。通常假定：智能体享有某种程度的自主；智能体对系统整体只有受限的局部视野；整个系统没有哪一个被指定的控制者（见 Wooldridge 2002 [2009]）[^wooldridge-2002]。

### 4.2 共同知识与社会程序

许多社会程序，其设计目的就在创造共同知识（Lewis 1969; van Ditmarsch et al. 2009; 并见“共同知识”词条）[^ditmarsch-2009][^lewis-1969]。你从银行账户取出大笔款项、由出纳点现金付给你时的那套老式仪式，便是一例。

共同知识能否达成、如何达成，取决于可用的通信设施。公开宣告，或可公开观察的仪式（即上述出纳仪式），能创造共同知识。但哈尔彭与摩西（1984）证明：在分布式环境中，若消息送达并无保证，单靠交换消息则创造不出共同知识。他们举了两位将军谋划合攻一城的例子。两位将军分驻城两侧的两座山头，各领一军；他们知道，唯有两军同时进攻，才能拿下此城。可隔开两山的山谷在敌手，从一处营地派往另一处的信使，随时有被擒的危险。将军们已约定合攻，只差定下时辰。于是他们互发消息，譬如“上午 9:00 进攻”。然而信使能否送到，他们无从确定；即便送到，确认的回信能否送到，也同样没有保证。如此循环不已。

共同知识虽在实践中有时难以达成，却是规制社会不可或缺的预设。罗马的立法者早已看出：若辖内公民能以不知法为由自辩无辜，则任何罪犯都无从定罪。于是他们立下 *Ignorantia legis neminem excusat*（不知法不免责）之类的原则。奉行法治的社会，其组织必须使公民 **原则上** 有能力知晓法律。法律须妥为公布、分发，例如刊印于人人可得而阅的政府公报。

Michael Suk-Young Chwe 在《理性的仪式》（2001）一书中指出，共同知识得以确立的群体 **规模** 甚为要紧。一个品牌若在大群体中成为共同知识，便价值不菲。Chwe 剖析了美式橄榄球超级碗期间播出广告的例子，把借这类广告使某事成为共同知识的巨额花费，同显而易见的收益两相对照。收益之一端，恰在于广告创造了共同知识：譬如决定买某一品牌的智能手机时，一项要紧的考量便是别人也会买同一型号。

当然，在许多社会情境里，你反倒想 **阻止** 共同知识生成，比如要对某些人保守秘密时。还有更耐人寻味的情形：某个人人皆知的事实——例如某国拥有核武器——若经公开宣告成为共同知识，却会招致政治麻烦。关于若干以维持隐私与不知情为要务的社会情境，见 van Eijck 与 Verbrugge（2009）。晚近一项有意思的进展，是基于动态认知逻辑的 **认知规划** 研究：它可以合成通信协议，在群体内造出高阶知识层级的特定精确配置（Bolander and Andersen 2011, Löwe, Pacuit, and Witzel 2011）[^bolander-2011]。

## 5 策略推理与合作

博弈论这一广阔领域，本百科全书的其它词条已有详尽论述（另见“博弈论”词条等）。自那部奠基之作（Von Neumann and Morgenstern 1944）[^von-1944]问世以来，该领域一直十分活跃。同样，社会选择理论、尤其是投票理论（见“社会选择理论”“投票方法”词条），早在“社会软件”一词出现之前许久，便已是兴旺的研究领域。

考察形式方法与算法视角能怎样帮着解决社会问题，颇有用处。例如在著名的囚徒困境（见“囚徒困境”词条）中，不妨试着设计政策，用惩罚叫欺骗对方变得无利可图。要注意，这种“社会软件工程”是在元层次上进行的，位于囚徒选择策略的那一层之上（van Eijck 2015）[^eijck-2015]。

博弈论中有一新近动向与社会软件相关：不再倚重纳什均衡这类解概念，转而着眼于理性慎思的过程，即“对局理论”（见 van Benthem, Pacuit and Roy, 2011，以及“分析博弈的逻辑”词条）。此类研究一面勾勒引导参与者作策略推理的规范原则，一面刻画用以解释博弈中预测行为与实际行为何以不同的心理现象（Camerer 2003; Ghosh and Verbrugge 2018; Pacuit 2015; Meijering et al. 2012, 2014; Top et al. 2018）[^camerer-2003][^ghosh-2018][^meijering-2012][^pacuit-2015][^top-2018]。

4.2 节简略谈到，分析社会程序时研究知识与信念有何作用。循此，认知博弈论关注的是：智能体对其他智能体策略持何种信念，那些智能体又对其他智能体的策略持何种信念，如此层层递进。理想化的情形是：一群智能体共同知道他们都是理性的（见“博弈论的认知基础”词条；Perea 2012; Brandenburger 2014）[^brandenburger-2014][^perea-2012]。

事实证明，尤其在投票理论里，设计一种逻辑来显式建模智能体投票时所依凭的知识，颇有用处。尤为有趣的是，建模群体中智能体虚报自身偏好、以操纵结果而作策略投票时发生的种种（van Eijck 2015; van Ditmarsch et al. 2012）[^ditmarsch-2012][^eijck-2015]。

近年以来，在多智能体系统这一研究领域，社会程序的形式化进路也被用来帮助设计实际软件，例如团队内的合作式问题求解、联盟形成、知识融合、拍卖，以及软件智能体之间的谈判（Bulling et al. 2015; Chalkiadakis et al. 2011; Dunin-Kęplicz and Verbrugge 2010; Pauly 2002; Shoham and Leyton-Brown 2009; Vazirani et al. 2007）[^bulling-2015][^chalkiadakis-2011][^dunin-kęplicz-2010][^pauly-2002][^shoham-2009][^vazirani-2007]。这类文献大体属于规范性研究。

与此相对，另一个引人入胜的研究领域是演化博弈论（见“演化博弈论”词条），它考察利他、社会规范、道德行为与合作这类特征究竟是如何演化出来的。该领域兼有规范性与描述性两项工作（Axelrod 1984; Bowles and Gintis 2011; Sigmund 2010）[^axelrod-1984][^bowles-2011][^sigmund-2010]。作为社会软件对该领域的一项独特贡献，加登福斯（2012）刻画了若干种合作各自所需的认知与通信多寡。范围从简单的群集行为，经互惠利他（“你替我搔背，我便替你搔背”），直至完全成熟的团队协作。

## 6 结论

总而言之，以算法与信息为重的这一形式视角——它同时观照社会程序与智能互动——已经带来形形色色的重要洞见，也引发了有意思的哲学讨论。未来的主要挑战，看来在于把目前相对零散的这一领域统合起来：许多研究者似乎并不了解其他子领域的相关工作。

## 脚注

[^note-1]: “社会软件”一词也被用作 MSN Messenger、Twitter、Skype 之类互联网通信应用的名称，本词条所论并不是这个。至于有时被称作“社会软件工程”的，又是另一回事：那是软件工程之下一个子学科的名称，该子学科专究软件工程的社会互动面向。

[^note-2]: 巴什肯特（2017）有一令人信服的论证：唯有在分析社会程序时，才值得越出经典逻辑之外。他表明，对帕里克社会软件研究中的若干例子来说，次协调逻辑提供了一个有用的视角（并见“次协调逻辑”词条）。

[^note-3]: 帕里克（2002）说：

> 另有一个成立的性质：若 $F(m, k + 1)$ 为真，则在切下一片蛋糕的动作 $c$ 之后，有可能剩下的主体仍够 $k$ 人分，切下的那片也够一人分。请看这一对比：动作 $r$ 无论怎样施行，都保持 $F(m, k)$——$r$ 怎么施行都不要紧；而切蛋糕的动作 $c$ 也许能达到想要的结果，却不必定如此。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### General References

### Fairness

### The Stable Marriage Problem

### The Logic of Communication

### Strategic Reasoning and Cooperation

[^başkent-2017]: Başkent, C., L.S. Moss, and R. Ramanujam, (eds.), 2017, *Rohit Parikh on Logic, Language and Society* (Outstanding Contributions to Logic: Volume 11), Berlin: Springer.
[^başkent-2017-2]: Başkent, C., 2017, “A Non-Classical Logical Approach to Social Software”, in Başkent, Moss, & Ramanujam 2017, pp. 91–110.
[^benthem-2018]: van Benthem, J., 2018, “Computation as Social Agency: What, How and Who”, *Information and Computation*, 261: 519–535.
[^eijck-2017]: Eijck, J. van, and Ph. Elsas, 2017, “What Is Money?”, in Başkent, Moss, & Ramanujam 2017, pp. 67–76.
[^eijck-2009]: Eijck, J. van, and R. Verbrugge (eds.), 2009, *Discourses on Social Software* (Texts in Logic and Games: Volume 5), Amsterdam: Amsterdam University Press.
[^eijck-2012]: ––– (eds.), 2012, *Games, Actions and Social Software: Multidisciplinary Aspects* (Lecture Notes in Computer Science: Volume 7010), Berlin: Springer.
[^harel-2004]: Harel, D., and Y.A. Feldman, 2004, *Algorithmics: The Spirit of Computing*, London: Pearson Education.
[^miller-2012]: Miller, R., and L. Boxer, 2012, *Algorithms Sequential & Parallel: A Unified Approach*, Boston, MA: Cengage Learning.
[^pacuit-2005]: Pacuit, E., 2005, *Topics in Social Software: Information in Strategic Situations*, Ph.D. thesis, New York: City University of New York.
[^parikh-2002]: Parikh, R., 2002, “Social Software”, *Synthese*, 132: 187–211.
[^parikh-2017]: –––, 2017, “Is There a Church-Turing Thesis for Social Algorithms?”, in A. Bokulich and J. Floyd (eds.), *Philosophical Explorations of the Legacy of Alan Turing*, (Boston Studies in the Philosophy of Science, Volume 324), Berlin: Springer, pp. 339–357.
[^pauly-2001]: Pauly, M., 2001, *Logic for Social Software*, Ph.D. thesis, Amsterdam: ILLC.
[^brams-2005]: Brams, S., 2005, “Fair Division”, in B.R. Weingast and D. Witteman (eds.), *Oxford Handbook of Political Economy*, Oxford: Oxford University Press, pp. 425–437.
[^brams-1996]: Brams, S., and A. Taylor, 1996, *Fair Division: From Cake-Cutting to Dispute-Resolution*, Cambridge: Cambridge University Press.
[^kyropoulou-2019]: Kyropoulou, M., J. Ortega, and E. Segal-Halevi, 2019, “Fair Cake-Cutting in Practice”, in *Proceedings of the 2019 ACM Conference on Economics and Computation*, ACM Press, pp. 547–548.
[^moore-1992]: Moore, J., 1992, “Implementation, Contracts, and Renegotiation in Environments with Complete Information”, in J.-J Laffont (ed.), *Advances in Economic Theory — 6ᵗʰ World Congress* (Volume 1), Cambridge: Cambridge University Press.
[^padma-2007]: Padma, T., 2007, *Mathematwist: Number Tales from Around the World*, Chennai: Tulika Publishers.
[^parikh-1983]: Parikh, R., 1983, “Propositional Game Logic”, in *24ᵗʰ Annual Symposium on Foundations of Computer Science*, Washington, DC: IEEE Computer Society, pp. 195–200.
[^pauly-2005]: Pauly, M., 2005, “Changing the Rules of Play”, *Topoi*, 24(2): 209–222.
[^robertson-1998]: Robertson, J., and W. Webb, 1998, *Cake-Cutting Algorithms: Be Fair If You Can*, Boca Raton, FL: A.K. Peters.
[^steinhaus-1948]: Steinhaus, H., 1948, “The Problem of Fair Division”, *Econometrica*, 16: 101–104.
[^gale-1962]: Gale, D., and L. Shapley, L., 1962, “College Admissions and the Stability of Marriage, *American Mathematical Monthly*, 69: 9–15.
[^cechlérová-2005]: Cechlérová, K., and D.F. Manlove, 2005, “The Exchange-Stable Marriage Problem”, *Discrete Applied Mathematics*, 152(1–3): 109–122.
[^parikh-2012]: Parikh, R., and M. Pauly, 2012, “What is Social Software?”, in van Eijck and Verbrugge 2012: 3–14.
[^pini-2011]: Pini, M. S., F. Rossi, K.B. Venable, and T. Walsh, 2011, “Manipulation complexity and gender neutrality in stable marriage procedures”. *Autonomous Agents and Multi-Agent Systems*, 22(1): 183–199.
[^bolander-2011]: Bolander, T., and M.B. Andersen, 2011, “Epistemic Planning for Single-and Multi-Agent Systems”, *Journal of Applied Non-Classical Logics*, 21(1): 9–34.
[^chwe-2001]: Chwe, M. S.-Y., 2001, *Rational Ritual*, Princeton and Oxford: Princeton University Press.
[^ditmarsch-2009]: van Ditmarsch, H., J. van Eijck, and R. Verbrugge, 2009, “Common Knowledge and Common Belief”, in J. van Eijck and R. Verbrugge (eds.), *Discourses on Social Software*, (Texts in Logic and Games), Amsterdam: Amsterdam University Press, pp. 99–122.
[^eijck-2009-2]: van Eijck, J., and R. Verbrugge, 2009, “Eating from the Tree of Ignorance”, in J. van Eijck and R. Verbrugge (eds.), *Discourses on Social Software* (Texts in Logic and Games), Amsterdam: Amsterdam University Press, pp. 184–198.
[^halpern-1984]: Halpern, J., and Y. Moses, 1984, “Knowledge and Common Knowledge in a Distributed Environment”, in *Proceedings of the 3rd ACM Symposium on Principles of Distributed Computing (PODS)*, pp. 50–61; revised, *Journal of the ACM*, 37/3 (1990): 549–587.
[^lewis-1969]: Lewis, D., 1969, *Convention: A Philosophical Study*, Cambridge, MA: Harvard University Press.
[^löwe-2011]: Löwe, B., E. Pacuit, and A. Witzel, 2011, “DEL Planning and Some Tractable Cases”, in Proceedings International Workshop on Logic, Rationality and Interaction (LORI), Berlin, Heidelberg: Springer, pp. 179–192.
[^lynch-1996]: Lynch, N., 1996, *Distributed Algorithms*, San Mateo, CA: Morgan Kaufmann.
[^nerburn-1999]: Nerburn, K., 1999, *The Wisdom of the Native Americans*, Novato, CA: New World Library.
[^wooldridge-2002]: Wooldridge, M., 2002 [2009], *An Introduction to Multi-Agent Systems*, first edition, Chichester: John Wiley and Sons; second edition 2009.
[^axelrod-1984]: Axelrod, R., 1984, *The Evolution of Cooperation*, New York: Basic Books.
[^benthem-2015]: Benthem, J. van, S. Ghosh, and R. Verbrugge (eds.), 2015, *Models of Strategic Reasoning: Logics, Games, and Communities* (FoLLI Publications on Logic, Language and Information, LNCS 8972), Berlin: Springer.
[^benthem-2011]: Benthem, J. van, E. Pacuit, and O. Roy, 2011, “Toward a Theory of Play: A Logical Perspective on Games and Interaction”, *Games*, 2(1): 52–86.
[^bowles-2011]: Bowles, S., and H. Gintis, 2011, *A Cooperative Species: Human Reciprocity and its Evolution*, Princeton and Oxford: Princeton University Press.
[^brandenburger-2014]: Brandenburger, A., 2014, *The Language of Game Theory: Putting Epistemics into the Mathematics of Games*, Singapore: World Scientific.
[^bulling-2015]: Bulling, N., and V. Goranko, 2015, “Logics for Reasoning About Strategic Abiliies in Multi-Player Games”, in van Benthem, Ghosh, & Verbrugge 2015: 93–136.
[^camerer-2003]: Camerer, C.F., 2003, *Behavioral Game Theory: Experiments on Strategic Interaction*, Princeton: Princeton University Press.
[^chalkiadakis-2011]: Chalkiadakis, G., E. Elkind, and M. Wooldridge, 2011, *Computational Aspects of Cooperative Game Theory* (Synthesis Lectures on Artificial Intelligence and Machine Learning: Volume 5), San Rafael, CA: Morgan and Claypool Publishers.
[^ciná-2016]: Ciná, G., and U. Endriss, 2016, “Proving Classical Theorems of Social Choice Theory in Modal Logic”, *Autonomous Agents and Multi-Agent Systems*, 30(5): 963–989.
[^ditmarsch-2012]: Ditmarsch, H. van, J. Lang, and A. Saffidine, 2012, “Strategic Voting and the Logic of Knowledge”, in *Proceedings of the 11th International Conference on Autonomous Agents and Multiagent Systems (AAMAS’12)*, vol. 3, pp. 1247–1248.
[^dunin-kęplicz-2010]: Dunin-Kęplicz, B., and R. Verbrugge, 2010, *Teamwork in Multi-Agent Systems: A Formal Approach*, Chichester: Wiley.
[^eijck-2015]: Eijck, J. van, 2015, “Strategies in Social Software”, in van Benthem, Ghosh, & Verbrugge 2015: 292–317.
[^gärdenfors-2012]: Gärdenfors, P., 2012, “The Cognitive and Communicative Demands of Cooperation”, in van Eijck and Verbrugge 2012: 164–183.
[^ghosh-2018]: Ghosh, S., and R. Verbrugge, 2018, “Studying Strategies and Types of Players: Experiments, Logics and Cognitive Models”, *Synthese*, 195(10): 4265–4307.
[^grädel-2002]: Grädel, E., W. Thomas, and T. Wilke (eds.), 2002, *Automata Logics, and Infinite Games*, (Lecture Notes in Computer Science 2500), Berlin, Heidelberg: Springer.
[^klein-2017]: Klein, D., and E. Pacuit, 2017, “Focusing on Campaigns”, in Başkent, Moss, & Ramanujam 2017, pp. 77–90.
[^meijering-2012]: Meijering, B., H. van Rijn, N. Taatgen, and R. Verbrugge, 2012,“What Eye Movements Can Tell about Theory of Mind in a Strategic Game”, *PLoS ONE*, 7(9), e45961, doi:10.1371/journal.pone.0045961
[^meijering-2014]: Meijering, B., N. Taatgen, H. van Rijn, and R. Verbrugge, 2014, “Modeling Inference of Mental States: As Simple as Possible, as Complex as Necessary“, *Interaction Studies*, 15(3): 455–477.
[^pacuit-2015]: Pacuit, E., 2015, “Strategic Reasoning in Games”, in van Benthem, Ghosh, & Verbrugge 2015: 3–33.
[^pauly-2002]: Pauly, M., 2002, “A Modal Logic for Coalitional Power in Games”, *Journal of Logic and Computation*, 12: 149–166.
[^perea-2012]: Perea, A., 2012, *Epistemic Game Theory: Reasoning and Choice*, Cambridge: Cambridge University Press.
[^shoham-2009]: Shoham, Y., and K. Leyton-Brown, 2009, *Multiagent Systems: Algorithmic, Game-Theoretic and Logical Foundations*, Cambridge: Cambridge University Press.
[^sigmund-2010]: Sigmund, K., 2010, *The Calculus of Selfishness*, (Princeton Series in Theoretical and Computational Biology), Princeton and Oxford: Princeton University Press.
[^top-2018]: Top, J., R. Verbrugge, and S. Ghosh, 2018, “An Automated Method for Building Cognitive Models for Turn-Based Games from a Strategy Logic”, *Games*, 9(3),44; doi:10.3390/g9030044
[^vazirani-2007]: Vazirani, V.V., N. Nisan, T. Roughgarden, and E. Tardos (eds.), 2007, *Algorithmic Game Theory*, Cambridge: Cambridge University Press.
[^von-1944]: Von Neumann, J., and O. Morgenstern, 1944, *Theory of Games and Economic Behavior*, Chichester: Wiley.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=social-procedures)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/social-procedures/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=social-procedures&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/social-procedures/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

### 会议系列

- [AAMAS：自治智能体与多智能体系统](http://www.ifaamas.org/)。
- [TARK：理性与知识的理论面向](http://www.tark.org/)。
- [LORI：逻辑、理性与互动工作坊](http://golori.org/)
- [LOFT：博弈与决策理论的逻辑与基础](http://www.econ.ucdavis.edu/faculty/bonanno/loft.html)。

### 其他站点

- [博弈、行动与社会软件：扬·范艾克与里内克·韦尔布鲁格 2009 年 ESSLLI 课程](https://rinekeverbrugge.nl/teaching/)
- [理性能动性的逻辑：埃里克·帕奎特 2010 年 NASSLLI 课程](http://ai.stanford.edu/~epacuit/lograt/nasslli2010.html)
- [一种离散且有界的无嫉妒切蛋糕协议：哈里斯·阿齐兹与西蒙·麦肯齐的报告](https://www.youtube.com/watch?v=jGiAckY00ik)
- [Kyropoulou 等 2019 年《实践中的公平切蛋糕》一文完整版预印本；2022 年修订](https://arxiv.org/abs/1810.08243)
- [稳定匹配盖尔—沙普利算法的交互式演示](http://mathsite.math.berkeley.edu/smp/smp.html)
- [令牌环协议视频](https://www.youtube.com/watch?v=rMWH21f7b2Q)

## 相关词条

生物利他主义 | 阿罗定理 | 信念合并与判断聚合 | 共同知识 | 可计算性与复杂度 | 计算机与道德责任 | 规范经济学与经济正义 | 社会认识论 | 博弈论 | 博弈论与伦理学 | 博弈论的认识论基础 | 演化博弈论 | 转型正义 | 行动的逻辑 | 认知逻辑 | 逻辑与游戏 | 次协调逻辑 | 实践理性 | 囚徒困境 | 隐私 | 再分配 | 社会选择理论 | 社会制度 | 社会规范 | 技术哲学 | 投票方法

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**

## 致谢

我要感谢扬·范艾克：与他合写本文 2014 年初版，是一段愉快的经历。也要感谢两位匿名审稿人，为这个更新版提出了若干改进与增补。因扬已于数年前退休，本文 2019 年的更新由我（里内克·韦尔布鲁格）独力完成，故一切遗留的不妥之处，责任全在我；若您有所发现，请告知。
