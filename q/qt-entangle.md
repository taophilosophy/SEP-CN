# 量子纠缠与信息 quantum entanglement and information (Jeffrey Bub)

*首次发表于 2001 年 8 月 13 日；2023 年 5 月 2 日实质修订。*

量子纠缠是一种物理资源，与能量相似，它对应着分离的量子系统之间可能出现的那种奇特非经典关联。纠缠可以被测量、变换、纯化。一对处于纠缠态的量子系统，可以用作量子信息信道，去完成经典系统无法完成的计算任务与密码学任务。量子信息论所研究的，正是量子系统信息处理能力的一般问题。

## 1 量子纠缠

1935 与 1936 年，薛定谔在 *Proceedings of the Cambridge Philosophical Society* 上发表了一篇两部分的文章，讨论并扩展了爱因斯坦、波多尔斯基与罗森的一个论证。爱因斯坦-波多尔斯基-罗森（EPR）论证在许多方面堪称爱因斯坦批判量子力学正统哥本哈根诠释的顶点，意在表明这一理论并不完备。（关于量子理论中的 EPR 论证与量子力学的哥本哈根诠释，见相应词条。）经典力学中，系统的状态本质上就是一份属性清单。更确切地说，是给定一组参数，由这些参数可以重构出属性清单：组成系统的所有粒子的位置与动量（若是场，则为类似参数）。理论的动力学通过状态的演化律来规定属性如何变化。在给马克斯·玻恩的一封信里，沃尔夫冈·泡利把这种描述物理系统的方式称作“超然观察者”式的理想化（见 *The Born-Einstein Letters*，Born，1992；第 218 页）。按哥本哈根诠释，对量子系统作这样的描述是不可能的。量子态毋宁应被理解为一份目录，记下观察者对系统做了什么、又观察到了什么；状态的意义则在于：依据该理论，可以推断出对该系统未来可能观测之结果的概率。爱因斯坦不接受这一观点，提出了一系列论证，表明量子态只是对量子系统的不完备刻画。那些缺失的参数，有时被叫作“隐参数”或“隐变量”。

不要以为，爱因斯坦的“完备理论”概念里含有“理论必须是决定论的”这一要求。他要的是：复合系统若由相互分离的组分系统构成，就须满足可分离性与定域性条件。每个组分系统都要各自由其自身属性来刻画（按爱因斯坦的说法，即它自己的“如此存在”，德语作 “So-sein”）；同时，人们不可能作用于某个定域系统，就瞬时改变远处系统的属性（或这些属性的概率）。后来的分析——尤其是贝尔对量子关联非定域性的论证——表明：把这些条件恰当地表述为概率约束，它们就等价于这样一个要求。分离系统之间的统计关联，应可归约为一种概率分布，其分布落在赖欣巴哈意义上的共因之上（无论决定论还是随机论）。（关于贝尔定理与赖欣巴哈的共因原理，见相应词条。）

在最初的 EPR 文章里，两个粒子由某个源制备出来，处于复合系统的一个“纯”量子态。这个态既不能表示成其他纯量子态的混合或概率分布，也不能归约为两个粒子各自的纯量子态。两粒子分开之后，位置之间与动量之间都有“匹配的”关联：对某个粒子作位置测量或动量测量，就能确定无疑地预测对另一个粒子作同类测量的结果。这两类测量互不相容：要么作位置测量，要么作动量测量，不能同时作。比如在确立了位置关联之后再测动量，两粒子的动量之间就不再有任何关联。倒像是位置测量扰乱了动量值之间的关联，反过来也一样。量子粒子的这种位置关联与动量关联，除了一个奇特之处——同一对量子粒子只能观察到其中一种关联，不能两者兼得——与碰撞之后两个台球之间的经典关联一模一样。经典关联可以用共因来解释，也可以用彼此关联的“实在要素”来解释。EPR 论证由此断定：量子力学不完备，因为这些共因或实在要素没有写进量子态的描述里。

薛定谔在他那篇两部分文章的第一部分里，把这个难题摆了出来（Schrödinger, 1935; p. 559）：

> 不过，1 号系统我可以不作任何干扰就预测出 **要么** $x_1$、要么 $p_1$。而 1 号系统就像考场里的学生，不可能知道我要先问这两个问题中的哪一个。如此看来，这位学生 **无论如何** 都准备着对他被问到的 **第一个** 问题给出正确答案。那么他必定两个答案都知道；这是一种惊人的知识；全然不顾这样一个事实：给出第一个答案之后，这位学生总是心慌意乱或疲惫不堪，以致后面的答案全是“错的”。

薛定谔表明：若把两个粒子制备在某个 EPR 量子态中，两个“正则共轭”动力学量（即位置、动量这类取值足以确定经典系统全部属性的量）之间存在匹配的关联。这时，这两个粒子上就有无穷多个动力学量存在同样的匹配关联。取第一个粒子的正则共轭对，其上任一函数都与第二个粒子的正则共轭对上的同一函数相匹配。因此（Schrödinger, p. 559）1 号系统“不仅知道这两个答案，还知道大量别的答案，而且全不借助任何记忆术，至少不借助我们所知的任何一种。”

为描述量子系统之间的这种奇特联系，薛定谔造了“纠缠”一词（Schrödinger, 1935; p. 555）：

> 两个系统，我们通过各自的代表来了解其状态。当它们由于彼此之间已知的力而发生暂时的物理相互作用，经过一段相互影响的时间又重新分开之后，就不能再按原先的方式描述了。原先的方式，就是给每个系统各自安上一个代表。这一点，我不会称作量子力学的 **一个** 特征，而要说它是量子力学的 **那个** 特征：正是它逼着量子力学彻底离开经典的思想轨道。经过这番相互作用，两个代表［即量子态］已经纠缠在一起了。

他又补充说（Schrödinger, 1935; p. 555）：

> 这种奇特处境还可以换一种说法：对 **整体** 的最佳可能认识，未必包含对其所有 **部分** 的最佳可能认识。哪怕这些部分彼此完全分离、因而实际上能够“被最佳可能地认识”，也就是说，每个部分都能拥有一个自己的代表。这里之所以缺乏知识，绝不是因为相互作用了解得不够充分——至少不是那种本来可以了解得更完备的情形——而是因为相互作用本身。
>
> 近来人们注意到一个明显却非常令人不安的事实：即便把解纠缠的测量只限于 **一个** 系统，为 **另一个** 系统得到的代表，也绝不独立于我们为此目的选定的特定观测。而这些观测，顺带说，是 **完全** 任意的。理论竟容许实验者随意把一个系统操控、引导成这一类或那一类状态，而他自己根本无法接触它——这实在令人不安。

在文章第二部分，薛定谔表明：实验者只要对纠缠对中的一个成员实施适当选择的操作，就能把第二个系统“操控”进某个选定的量子态混合。操作中可能还要动用额外的“辅助”粒子或帮手粒子。这个混合的概率分布取决于该纠缠态。第二个系统不会被实验者随心所欲地操控进某个 **特定的** 量子态；不过，对于纠缠对的许多个副本，实验者可以约束第二个系统的量子态，使它落在某个选定的量子态集合里。这些态与对纠缠着的配对系统（或配对系统加辅助系统）所作测量的可能结果相关联。这个结论让他颇感不安。于是他提出：两个分离中的系统之间的纠缠，只在距离足够小时才持续存在。这里“足够小”是指：光从一个系统走到另一个系统所需的时间，与复合系统中其他变化所对应的特征时间相比可以忽略不计。他猜测，距离更长时，这两个系统实际上可能处于由该纠缠态所决定的一种相互关联的量子态混合之中。

纠缠量子态那些令人费解的特征，多数物理学家都归咎于爱因斯坦的“超然观察者”观点不合时宜，认为那是他对物理理论的误解。他们还把玻尔对 EPR 论证的回应（Bohr, 1935）看作对哥本哈根诠释的维护。这实在不幸：此后三十年，纠缠的研究无人问津，直到约翰·贝尔重新审视 EPR 论证（Bell, 1964）。贝尔考察的纠缠系统比 EPR 的例子简单：两个分离系统处于纠缠态，其间二值动力学量——例如沿某一特定方向的偏振或自旋——存在匹配关联。贝尔表明：在两个系统上适当选择 **不同** 的量并作测量，所得结果之间的统计关联，与一条不等式无法调和；这条不等式可由爱因斯坦的可分离性与定域性假定推出——实际上是由“这些关联有共同原因”这一假定推出。这条不等式今天称作贝尔不等式；作为经典关联或共因关联的必要条件，还可以推出若干相关的不等式。

贝尔的探究引发了一场围绕量子力学基础的持久争论。这场争论的一个重要收获，是确认纠缠能在远距离上维持，这就推翻了薛定谔的猜想——两个纠缠粒子一经分离，纠缠便会自发衰变。（光子的自由空间纠缠已在 143 公里距离上演示成功；借助卫星分发纠缠，也已在地球上相距 1200 多公里的两地之间实现。见 Herbst *et al* 2014 与 Yin *et al* 2017。）[^yin-2017] 不过，直到 1980 年代，物理学家、计算机科学家与密码学家才转变看法：纠缠量子态的非定域关联是一种可以利用的新型非经典物理资源，不再是量子力学需要解释掉的尴尬。纠缠究竟是什么、为何在概念上令人困惑、又能拿它来做什么，包括贝尔定理的一个简单证明，可参看图像小说 *Totally Random: Why Nobody Understands Quantum Mechanics (A Serious Comic on Entanglement)*（Bub and Bub 2018）。至于把纠缠当作物理资源的进一步讨论——如何测量纠缠，如何通过局部操作操控与纯化纠缠——可参看 Popescu 与 Rohrlich 的“The Joy of Entanglement”，收于 Lo, Popescu, and Spiller 1998，以及 Bub 2016 和经典教材 Nielsen and Chuang 2011。阿兰·阿斯佩、约翰·F. 克劳泽与安东·蔡林格因在纠缠光子上的开创性实验而获得 2022 年诺贝尔物理学奖：这些实验验证了贝尔的洞见，并开启了量子信息这一领域。

## 2 利用纠缠：量子隐形传态

再回头看看薛定谔的那个洞见：纠缠态可以用以某个概率把远处的粒子操控进一组状态中的某一个。其实，这种“远程操控”的可能性比薛定谔演示的还要惊人。设爱丽丝与鲍勃共享一个贝尔所考虑的那种纠缠纯态，例如两个光子处于偏振的纠缠态，爱丽丝手中持有其中一个纠缠光子，鲍勃持有与之成对的第二个光子。再设爱丽丝收到一个额外的光子，它处于未知的偏振态 $\ket{u}$，其中记号“$\ket{\ }$”表示一个量子态。爱丽丝可以对自己手中的两个光子实施某种操作，把鲍勃的光子变成四个态之一。究竟是哪一个，取决于她这次操作的四种可能（随机）结果：或者是态 $\ket{u}$，或者是某个与 $\ket{u}$ 有确定关系的态。爱丽丝的操作使她手中两个光子纠缠起来，同时使鲍勃的光子解纠缠，把它操控进态 $\ket{u^*}$。爱丽丝把操作结果告知鲍勃之后，鲍勃便知道要么 $\ket{u^*}$ = $\ket{u}$，要么知道如何借助局部操作把 $\ket{u^*}$ 变换成 $\ket{u}$。这种现象叫作“量子隐形传态”。经过隐形传态程序，态 $\ket{u}$ 对爱丽丝与鲍勃仍然是未知的。

这个现象的惊人之处在于：爱丽丝与鲍勃竟然把共享的纠缠态当作量子通信信道，在宇宙中爱丽丝这一侧毁掉一个光子的态 $\ket{u}$，又在宇宙中鲍勃那一侧把它重新造出来。光子的线偏振态要求指定空间中的一个方向（一个可以连续变化的角），因此，没有共享的纠缠态，爱丽丝就非得向鲍勃传送无穷多的经典信息，鲍勃才能精确重构态 $\ket{u}$。一个二值选项（记作 0 或 1，两种可能概率相等）所对应的经典信息量，是一个二进制位，即“比特”。要用十进制写出一个任意的角，需要 0 到 9 之间的无穷数字串；换成二进制，则需要 0 与 1 的无穷序列。爱丽丝操作的结果有四种可能，概率各为 1/4，只需两个比特的经典信息即可指明。耐人寻味的是，鲍勃仅凭爱丽丝传给他的两个比特经典信息，就能重构出态 $\ket{u}$，靠的显然是把纠缠态当作量子通信信道来传送其余的信息。这一想法最早由 Bennett *et al* 于 1993 年提出。量子隐形传态的进一步讨论，见 Nielsen and Chuang 2011，或 Richard Josza 的“Quantum Information and its Properties”，收于 Lo, Popescu, and Spiller 1998。量子隐形传态已在地球上约 100 公里的距离上实现，并在地球与卫星之间 1400 公里的距离上实现（Zeilinger, 2018）。用卫星传输纠缠光子来建设量子互联网，要依赖量子隐形传态。

## 3 量子信息

形式上，我们获知某个随机变量的取值时平均获得的经典信息量（等价地说，是获知其取值之前该取值的不确定性），由一个叫作香农熵的量来刻画，以比特计量（Shannon and Weaver, 1949）。随机变量由一组取值上的概率分布来定义。二值随机变量若两种可能等概率，香农熵就是 1 比特，代表最大的不确定性。其余各种概率——直观上代表“哪个选项更可能”的某些信息——香农熵都小于 1。到了知识最大、即对各选项毫无不确定性的情形，概率为 0 与 1，香农熵为零。（注意：“比特”一词既指按香农熵计的经典信息基本单位，也指一个基本的二态经典系统，该系统被看作代表某个基本经典信息源的可能输出。）

信息总要体现在物理系统的状态中，所以我们也可以把香农熵理解为对存储经典信息所需物理资源的度量。假定爱丽丝想经由一条经典通信信道（例如电话线）把一些经典信息传给鲍勃。这时一个相关的问题是：在不丢信息的前提下，消息能压缩到什么程度，好让鲍勃从压缩版本准确重构出原消息。按香农的信源编码定理（无噪编码定理，假定电话线无噪声、不丢信息），表示该消息所需的最小物理资源（实际上就是压缩可能性的下界）由信源的香农熵给出。

若改用物理系统的量子态、而不是经典态来存储信息，情况会怎样？原来，量子信息与经典信息截然不同。量子信息的单位是“量子比特”，它代表最简单量子系统（例如一个光子的偏振态）的状态能存下多少量子信息。这个术语出自 Schumacher（1995），他证明了香农无噪编码定理的量子对应版本。（仿照“比特”一词的用法，“量子比特”既指按冯·诺依曼熵计的量子信息基本单位，也指一个基本的二态量子系统，该系统被看作代表某个基本量子信息源的可能输出。）任意大的经典信息量都能编码进一个量子比特。这些信息能处理、能传送，但受量子测量种种特性的限制，最多只能取出一个比特。按 Holevo 的一条定理，一组备选量子比特态上的概率分布中，可获取信息受冯·诺依曼熵限制；只有当这些态在量子态空间中彼此正交时，冯·诺依曼熵才等于香农熵，否则就小于香农熵。

经典信息可以复制、可以克隆，量子“不可克隆”定理（Dieks, 1982; Wootters and Zurek, 1982）却断言：未知的量子态无法克隆。原因何在？不妨想想怎么造一台经典复制装置。非门取一个比特作输入，输入 0 则输出 1，输入 1 则输出 0——也就是说，非门是一个翻转输入比特的 1 比特门。受控非门（CNOT 门）以两个比特为输入，一个控制比特、一个目标比特；当且仅当控制比特为 1 时翻转目标比特，同时照抄控制比特。于是它有两个输入——控制与目标——和两个输出：控制比特，以及目标比特或翻转后的目标比特，取决于控制比特的取值。若把目标比特置为 0，CNOT 门就成了控制比特的复制装置，因为此时目标比特的输出正是控制比特的副本：输入 00 得输出 00，输入 10 得输出 11（这里第一个比特是控制，第二个是目标）。只要把测量径直看作一种复制操作，CNOT 门就是经典测量装置的典范。设想爱丽丝有这样一台装置，带输入、输出的控制线与目标线，用它去测量一个未知经典世界的属性。输入控制线是探针，探测某属性之有无，以 1 或 0 表示；目标线则相当于指针，初始置为 0。输出是 1 还是 0，取决于该属性有无。

假定我们想用 CNOT 门去复制一个未知的量子比特态。既然这里把 CNOT 门当作处理量子态的工具，那么输入态到输出态的演化，就必须由某种物理量子变换来实现。量子变换在量子比特的线性状态空间上是线性的。**状态空间** 的线性是说：状态空间中两个量子比特态以系数 $c_0, c_1$ 构成的任意和或叠加，仍是该状态空间中的量子比特态。**变换** 的线性则要求：变换应把一个由两个量子比特态之和表示的量子比特态，变成一个新的量子比特态，即这两个量子比特态各自变换之后的和。倘若 CNOT 门能成功复制两个正交量子比特态 $\ket{0},\ket{1}$，它就无法成功复制这两个量子比特的一般线性叠加。门的作用是线性的，因此它只能产生这样一个态：对两个正交量子比特态分别所得的输出再做线性叠加。也就是说，门的输出将是一个由两项之和表示的量子态，第一项是第一个量子比特态下控制与目标的输出，第二项是第二个正交量子比特态下控制与目标的输出。这可写作 $c_0 \ket{0} \ket{0}$ + $c_1 \ket{1} \ket{1}$——一个纠缠态（除非 $c_0$ 或 $ c_1$ 为零），而不是成功复制操作所要求的输出（此时控制与目标各自输出叠加量子比特态 $c_0 \ket{0}$ + $c_1 \ket{1}$）。

## 4 量子密码学

设爱丽丝与鲍勃分处两地，想传递一条秘密消息，又不向窃听者伊芙泄露任何信息。在经典世界里，只要他们共享一个“一次性密码本”就能办到：那是一把密码学密钥，由随机比特序列表示，长度至少等于传递该消息所需的比特数。事实上，这也是经典世界中达到完美安全的唯一办法。要把消息发给鲍勃，爱丽丝只需说明密钥中哪些比特该由鲍勃翻转，由此得到的比特序列就是消息。此外，他们还得有办法把消息编码成比特序列，即把字母、空格与标点符号表示成二进制数；这可以借助某种标准的公开方案来完成。

问题在于，这样传递的消息只有在爱丽丝与鲍勃为每条消息各换一个一次性密码本时才是秘密的。倘若几条消息共用同一个一次性密码本，伊芙就能把消息的统计特征同“词由字母拼成”的方式对照起来。由此她还能获得一些信息：字母与密钥中的比特子序列是如何对应的。要共享新密钥，他们只能靠可信的信使或类似办法来分发。而在经典世界里，密钥分发程序的安全性无从保证。

爱丽丝与鲍勃各自以某种据称安全的方式存储共享密钥，这里还横着另一个问题：把密钥复制走而不留痕迹。然而经典世界的物理定律既不能保证某种存储程序绝对安全，也不能保证安全一旦遭到破坏、密钥一旦被复制，就必定为人所察觉。所以除密钥分发问题之外，还有密钥存储问题。

量子纠缠为解决这些问题提供了一条途径，靠的是纠缠态关联的“单配性”：爱丽丝与鲍勃之间的纠缠关联，任何第三方都分享不到。而且，伊芙只要试图测量爱丽丝与鲍勃共享的纠缠态中的量子系统，就会毁掉这个纠缠态。爱丽丝与鲍勃检验一条贝尔不等式，便能察觉此事。

办法之一是阿图尔·埃克特最初提出的一个协议。设爱丽丝持有一批光子，每个光子对应一个处于态 $\ket{0}\ket{0} + \ket{1}\ket{1}$ 的纠缠对（为简化起见忽略相等的系数），鲍勃则持有与之配对的那批光子。爱丽丝相对于双方事先约定的某个方向 $z$，随机沿 $0, \pi/8, 2\pi/8$ 三个方向测量自己光子的偏振；鲍勃随机沿 $\pi/8, 2\pi/8, 3\pi/8$ 三个方向测量自己光子的偏振。两人公开告知各自的测量方向，但不告知测量结果，并把测量分成两组：一组是两人都沿 $\pi/8$ 方向测量、或都沿 $2\pi/8$ 方向测量的情形；另一组是爱丽丝沿 $0$ 或 $2\pi/8$ 方向测量、鲍勃沿 $\pi/8$ 或 $3\pi/8$ 方向测量的情形。第一组里，两人沿同一方向测量偏振，结果虽随机，却在该纠缠态中完全关联，于是他们把共享的这些随机比特当作密码学密钥。第二组则用来检验一条贝尔不等式，由此可以看出纠缠态是否已被窃听者的测量动过手脚。（见 Ekert, 1991。）

经典信息与量子信息的差异可以用来实现成功的密钥分发，但另有一些密码学协议恰恰被量子纠缠挡住了去路。比特承诺就是这样一个关键协议，它可作为子程序用于多种重要的密码学任务。在比特承诺协议里，爱丽丝交给鲍勃一个编码过的比特。该编码所含的信息应当不足以让鲍勃确定这个比特的取值。但若再加上进一步的信息（由爱丽丝在后续阶段、即她该揭示比特取值之时提供），就足以让鲍勃确信一点：这个协议不让爱丽丝有作弊的余地。她没法把比特编码成自己想揭示 0 就揭示 0、想揭示 1 就揭示 1 的样子。

为说明这个想法，设爱丽丝声称自己能逐日预测股市的涨跌。为了在不泄露有价值信息的情况下证实这一说法（也许是向潜在的雇主鲍勃），她提议做一个演示。在市场开盘之前，她先把预测写在一张纸上——0 表示“下跌”，1 表示“上涨”——然后锁进保险箱。保险箱交给鲍勃，钥匙由爱丽丝自己留着。当天交易结束，她宣布自己选的是哪个比特，并把钥匙交给鲍勃，以此证明她确实早在开盘前就立下了承诺。当然，这套“保险箱加钥匙”的办法无法证明能防住鲍勃作弊，因为经典物理学中没有任何原理能阻止鲍勃打开保险箱再关上而不留痕迹。问题在于：这一程序有没有一种无条件安全的量子对应物——依物理定律可证明，爱丽丝与鲍勃谁都作不了弊。鲍勃若能在爱丽丝揭示之前得到关于她承诺的 **某些** 信息，他就能作弊（这会让他与爱丽丝重复该协议时占便宜）。爱丽丝若能把真正立下承诺一事拖到她必须揭示承诺的最后阶段，或者能在最后阶段改变承诺而几乎不会被发现，她就能作弊。

结果表明：仅仅依据量子力学或经典力学的原理（既不借狭义相对论的信号传递约束，也不借广义相对论或热力学原理），无条件安全的两方比特承诺是不可能的。进一步讨论见 Mayers 1997、Lo and Chau 1997，以及 Lo 的“Quantum Cryptology”，收于 Lo, Popescu, and Spiller 1998。（Kent 1999 表明：在对爱丽丝与鲍勃双方都可验证地分离的站点之间安排定时通信序列，利用相对论性的信号传递约束，就能实施一个安全的经典比特承诺协议。）[^kent-1999] 大略说来，不可能性出在这里。协议中凡是要爱丽丝或鲍勃拿定主意的步骤，这个选择都可以通过恰当地让一个或多个辅助粒子与信道粒子纠缠起来而推迟。这类步骤包括：对量子信道中的某个粒子作测量，随机地、也许还是有条件地在若干要施加于该粒子的备选行动之间作选择，等等。再对辅助粒子作适当操作，信道粒子就能“操控”自如，使这种作弊策略无法识破。实际上，只要鲍勃得不到关于所承诺比特的任何信息，纠缠便能让爱丽丝随心所欲地把该比特“操控”成 0 或 1。

2022 年，美国国家标准与技术研究院（NIST）公布了一组加密协议，设计目标是抵御量子计算机的攻击：[NIST 公布首批四种抗量子密码算法](https://www.nist.gov/news-events/news/2022/07/nist-announces-first-four-quantum-resistant-cryptographic-algorithms)。

## 5 量子计算

量子信息可以被处理，但这种信息的可获取性受 Holevo 界的限制（第 3 节提到过）。戴维·多伊奇（1985）最先表明，如何借量子纠缠完成一项经典计算机不可能完成的计算任务。设我们有一个黑箱或预言机，用来求布尔函数 $f$ 的值，$f$ 的自变量或输入取 0 或 1，$f$ 的值或输出也取 0 或 1。输出或对两个输入相同（这时称 $f$ 是常量函数），或对两个输入不同（这时称 $f$ 是平衡函数）。设我们想确定 $f$ 究竟是常量还是平衡的。经典办法只有一种：把黑箱运行两次、或向预言机查询两次，0 与 1 两个自变量各一次，再把得到的值（$f$ 的输出）送进一个电路，由它判定两者相同（“常量”）还是不同（“平衡”）。多伊奇表明：若用量子态与量子门来存储、处理信息，那么只需对函数 $f$ 求值一次，就能确定 $f$ 是常量还是平衡的。诀窍在于设计电路（门的序列），让关于该函数某个 **全局** 问题的答案落在一个输出量子比特寄存器里，然后把它读出或测量出来。

再看量子 CNOT 门：控制比特的可能输入是两个正交量子比特 $\ket{0}$ 与 $\ket{1}$，目标比特的输入是 $\ket{0}$。不妨把输入的控制量子比特和输出的目标量子比特，分别看作某函数的自变量与相应的值。这个 CNOT 函数把值 0 配给自变量 0，把值 1 配给自变量 1。若控制比特输入的是两个正交量子比特以相等系数构成的线性叠加，目标比特输入量子比特 $\ket{0}$，输出便是纠缠态 $\ket{0} \ket{0}$ + $\ket{1} \ket{1}$（为简化起见忽略系数）。这是一个线性叠加，第一项代表 CNOT 函数的自变量 0 与相应值 0，第二项代表自变量 1 与相应值 1。纠缠态以线性叠加的形式表示出该函数全部可能的自变量与对应值，可这些信息是取不到的。能够表明可取到的，只是通过适当选择量子门而得到的、关于该函数是否具有某些全局性质的信息。这类信息不必读出任何个别自变量与值的求值结果即可获得。（实际上，要从纠缠态中获取关于函数某个全局性质的信息，通常就得放弃关于个别自变量与值的全部信息。）

多伊奇的函数 $f$ 与此类似。$f$ 的输出，在“常量”情形下或为 $\ket{0} \ket{0} + \ket{1} \ket{0}$，或为 $\ket{0} \ket{1} + \ket{1} \ket{1}$；在“平衡”情形下或为 $\ket{0} \ket{0} + \ket{1} \ket{1}$，或为 $\ket{0} \ket{1} + \ket{1} \ket{0}$。“常量”情形的两个纠缠态在四维双量子比特状态空间中正交，张成一个平面，不妨称之为“常量”平面；“平衡”情形的两个纠缠态同样张成一个平面，即“平衡”平面。这两个平面代表两个备选的量子析取，彼此正交，只交叠于一条线，这条线代表一个积态（非纠缠态），其中每个量子比特各自处于态 $\ket{0} + \ket{1}$。因此可以设计一种测量，用来区分 $f$ 的两个备选析取性质或全局性质——“常量”还是“平衡”——但有一定概率（其实为 1/2）失败，即测量结果落在两种情形所共有的重叠态上。不过，只要测量成功辨认出该全局性质，就只需对函数查询一次。若量子门选得巧妙，甚至可以设计出一次运行便能成功区分两种情形的量子电路。

多伊奇的例子说明，量子信息与量子纠缠可以怎样在一步之内算出一个函数的析取性质或全局性质，而经典办法需要两步。多伊奇的问题本身相当平凡，但如今已有若干有实用价值的量子算法。其中最著名的是 Shor 的因式分解算法与 Grover 的数据库搜索算法。Shor 算法能在多项式时间内分解大的合数，可直接用于“公钥”密码学这一广泛使用的经典密码学方案。Shor 算法相对于 **任何已知** 经典算法都是指数级加速。对于允许访问预言机的算法（不考虑预言机的内部结构），某些情况下可以证明其加速相对于 **任何** 经典算法都是指数级的，例如 Simon 算法。量子计算与量子算法的更多内容，见 Nielsen and Chuang 2011、Barenco 的“Quantum Computation: An Introduction”（收于 Lo, Popescu, and Spiller 1998）、Bub 2006（第 6 节）、Abhijith et al 2022，以及关于量子计算的词条。

要注意，迄今还没有证据表明量子算法能在多项式时间内求解 NP 完全问题。NP 完全问题的概念见关于计算复杂性理论的词条。所以量子计算机相对于经典计算机的效率，到头来也许只是幻觉。若真有加速，那看来应归功于纠缠现象。描述 $n$ 个量子比特的一般纠缠态，所需信息量随 $n$ 指数增长。状态空间（希尔伯特空间）是 $2^n$ 维的，一般纠缠态是 $2^n$ 个 $n$ 量子比特态的叠加。经典力学里没有纠缠态：一个一般的 $n$ 比特复合系统，只需描述单个比特系统所需信息量的 $n$ 倍即可描述。因此，对量子过程作经典模拟时，随着演化中纠缠起来的量子比特数线性增长，表示该量子态所需的经典信息资源将指数增长。与实际由系统执行的量子计算相比，计算该演化的速度也会相应指数级变慢。

## 6 解释性评论

多伊奇（1997）主张，量子计算中的指数级加速，乃至量子系统处理信息的方式，只有在埃弗雷特的“多世界”诠释框架内才能恰当理解。相关背景见关于埃弗雷特量子力学相对态表述的词条，以及关于量子力学多世界诠释的词条。粗略地说，其想法是这样：函数量子计算中出现的那类纠缠态，表示该函数所有可能自变量与对应值的线性叠加。它应当理解为一种大规模的并行经典计算：在各个平行世界中，把该函数的一切可能取值同时算出来。对“量子并行”这种解释思路的犀利批评，见 Steane 2003。

另一种观点着眼于量子系统属性的非布尔结构。经典系统的属性构成一个布尔代数，实质上是集合论结构的一种抽象刻画；经典逻辑之所以是布尔的、经典计算机里之所以有布尔门，都体现了这一点。从这个角度看，图景就完全不同了。量子算法并不“一次算出函数的全部取值”，而是去算关于某函数的一个析取问题或全局问题的答案（例如某布尔函数是常量还是平衡的）。它同时不计算冗余信息（例如该函数各不同输入所对应的输出值），由此获得相对于经典算法的指数级加速。量子信息与经典信息有一个关键差别：可以在若干备选的可能析取之中选定一个排他性析取，用来表示函数的某个全局性质。例如“常量”析取，断言该函数的值（对两个自变量而言）为 0 **或** 1；又如“平衡”析取，断言该函数的值（对两个自变量而言）与自变量相同 **或** 不同于自变量——却不必确定各个析取项的真理值。

在经典逻辑中，排他性析取为真，当且仅当其中一个析取项为真。量子电路之所以加速，秘密在于利用量子属性的非布尔结构，高效区分两个析取性质，而不必确定相关析取项的真假。这些析取项代表函数个别输入与对应输出之间的关联。这套程序的关键，就是在确定全局性质时绕开对特定输入的函数求值；正是这一在经典计算的布尔逻辑中办不到的特征，带来了相对于经典算法的加速。（若想不涉量子计算、专门了解量子逻辑，见关于量子逻辑与量子概率的词条。）

量子信息与量子计算领域的一些研究者，力主对量子力学作信息论的诠释。Andrew Steane 在关于量子计算的综述文章（1998, p. 119）中评论道：

> 历来，基础物理学的很大一部分工作，是发现自然的基本粒子以及描述其运动与相互作用的方程。如今看来，另一项纲领或许同样重要：去弄清自然如何允许、又如何阻止 **信息** 被表达与操纵，而不只是粒子如何运动。

Steane 在综述末尾提出了这样一个激进的构想（1998, p. 171）：

> 最后，我想提出一项范围更广的理论任务：找到一组类似能量守恒、动量守恒的原理，但它们管的是信息，而量子力学许多内容都能从它们推出。检验这类想法只看两点：EPR-贝尔关联是否因此变得一目了然；“测量”“知识”这类术语该怎么用，是否也因此变得显然。

在所谓“广义概率论”或“Boxworld”框架里，已有大量研究追问：在“无信号传递”理论这一类中，究竟哪些信息论约束能够刻画量子理论。这方面的有趣结果见 Brassard 2005、van Dam 2005、Skrzypczyk, Brunner, and Popescu 2009、Pawlowski *et al*. 2009、Allcock *et al*. 2009、Navascues and Wunderlich 2009、Al–Safi and Short 2013、Ramanathan *et al* 2010 以及 Ringbauer *et al*（2014）。Chiribella and Spekkens 2016 是一部论文集，出自加拿大滑铁卢圆周理论物理研究所的一次会议，议题是量子基础与量子信息交界处的新研究。关于 QBism 这一极端主观主义的信息论视角，见 Fuchs 2014 以及关于量子贝叶斯式与实用主义式量子理论观点的词条。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^abhijith-2022]: Abhijith J. et al., (2022). “Quantum Algorithm Implementations for Beginners,” *ACM Transactions on Quantum Computing*, 3: 1–92.
[^al-safi-2014]: Al-Safi, S.W., Short, A.J., 2014. “Reversible Dynamics in Strongly Non-Local Boxworld Systems,” *Journal of Physics A: Mathematical and Theoretical*, 47: 325303.
[^alcock-2009]: Alcock, J., Brunner, N., Pawlowski, M., Scarani, V., 2009. “Recovering Part of the Quantum Boundary from Information Causality,” *Physical Review A*, 80: 040103 [[available online](http://arxiv.org/abs/0906.3464)].
[^aspect-1982]: Aspect, A., Grangier, P., Roger, G., 1982. “Experimental Tests of Bell’s Inequalities Using Time-Varying Analyzers,” *Physical Review Letters*, 49: 1804–1807.
[^barrett-2007]: Barrett, J., 2007. “Information Processing in Generalized Probabilistic Theories,” *Physical Review A*, 75: 032304.
[^barrett-2005]: Barrett, J., Hardy, L., Kent, A., 2005. “No signaling and Quantum Key Distribution,” *Physical Review Letters*, 95: 010503.
[^bell-1964]: Bell, J.S., 1964. “On the Einstein-Podolsky-Rosen Paradox” *Physics*, 1: 195–200.
[^bennett-1993]: Bennett, C.H., Brassard, G., Crepeau, C., Jozsa, R., Peres, A., Wotters, W. K., 1993. “Teleporting an Unkown Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels,” *Physical Review Letters*, 70: 1895–1899.
[^bennett-2000]: Bennett, C.H., DiVincenzo, B.D., 2000. “Quantum Information and Computation,” *Nature*, 404: 247–255.
[^bohr-1935]: Bohr, N., 1935. “Can Quantum-Mechanical Description of Physical Reality be Considered Complete?,” *Physical Review*, 38: 696–702.
[^born-1992]: Born, M. (ed.), 1992. *The Born-Einstein Letters*, Dordrecht: Reidel.
[^brassard-2005]: Brassard, G., 2005. “Is Information the Key?,” *Nature Physics*, 1: 2–4.
[^bub-2006]: Bub, J., 2006. “Quantum Information and Computation,” in John Earman and Jeremy Butterfield (eds.), *Philosophy of Physics (Handbook of Philosophy of Science)*, Amsterdam: North Holland, pp. 555–660 [[available online](http://arxiv.org/abs/quant-ph/0512125)].
[^bub-2007]: –––, 2007. “Quantum Computation from a Quantum Logical Perspective,” *Quantum Information and Computation*, 7: 281–296.
[^bub-2008]: –––, 2008. “Quantum Computation and Pseudotelepathic Games,” *Philosophy of Science*, 75: 458–472.
[^bub-2016]: –––, 2016. *Bananaworld: Quantum Mechanics for Primates*, Oxford: Oxford University Press.
[^bub-2018]: Bub, T. and Bub, J., 2018. *Totally Random: Why Nobody Understands Quantum Mechanics (A Serious Comic on Entanglement)*, Princeton: Princeton University Press.
[^chiribella-2016]: Chiribella, G. and Spekkens, R., 2016. *Quantum Theory: Informational Foundations and Foils*, New York, Springer.
[^deutsch-1985]: Deutsch, D., 1985. “Quantum Theory, the Church-Turing Principle and the Universal Quantum Computer,” *Proceedings of the Royal Society (London)*, A400: 97–117.
[^deutsch-1997]: –––, 1997. *The Fabric of Reality*, London: Penguin.
[^dieks-1982]: Dieks, D., 1982. “Communication by EPR Devices,” *Physics Letters A*, 92: 271–272.
[^einstein-1935]: Einstein, A., Podolsky, B., Rosen, N., 1935. “Can Quantum-Mechanical Description of Physical Reality be Considered Complete?,” *Physical Review*, 47: 777–780.
[^ekert-1991]: Ekert, A., 1991. “Quantum Cryptography Based on Bell’s Theorem” *Physical Review Letters*, 67: 661–663.
[^ekert-2014]: Ekert, A. and Renner, R., 2014. “The Ultimate Physical Limits of Privacy,” *Nature*, 507: 443–447.
[^everett-1957]: Everett, H., 1957. “‘Relative State’ Formulation of Quantum Mechanics,” *Reviews of Modern Physics*, 29: 454–462.
[^feynman-1996]: Feynman, R., 1996. *Feynman Lectures on Computation*, J.G. Hey and R.W. Allen (eds.), Reading, MA: Addison-Wesley Publishing Company.
[^fuchs-2014]: Fuchs, C.A., 2014. “An Introduction to QBism with an Application to the Locality of Quantum Mechanics,” *American Journal of Physics*, 82: 749–754.
[^herbst-2015]: Herbst, T., Scheidl, T., Fink, M., Handsteiner, J., Wittmann, B., Ursin, R., Zeilinger, A., 2015. “Teleportation of Entanglement over 143 km,” *Proceedings of the National Academy of Sciences of the United States of America*, 112: 14202–5 [[available online](https://www.pnas.org/content/112/46/14202)].
[^holevo-1973]: Holevo, A.S., 1973. “Statistical Problems in Quantum Physics,” in G. Murayama and J.V. Prokhorov (eds.) *Proceedings of the Second Japan-USSR Symposium on Probability Theory*, Berlin: Springer, pp. 104–109.
[^kent-1999]: Kent, A., 1999. “Unconditionally Secure Bit Commitment,” *Physical Review Letters*, 83: 1447–1450.
[^kent-2012]: –––, 2012. “Unconditionally Secure Bit Commitment by Transmitting Measurement Outcomes,” *Physical Review Letters*, 109: 130501.
[^lo-1997]: Lo, H.-K., Chau, H.F., 1997. “Is Quantum Bit Commitment Really Possible?,” *Physical Review Letters*, 78: 3410–3413.
[^lo-1998]: Lo, H.-K., Popescu, S., Spiller, T., 1998. *Introduction to Quantum Computation and Information*, Singapore: World Scientific.
[^mayers-1997]: Mayers, D., 1997. “Unconditionally Secure Quantum Bit Commitment is Impossible,” *Physical Review Letters*, 78: 3414–3417.
[^navascues-2009]: Navascues, M. and Wunderlich, H., 2009. “A Glance Beyond the Quantum Model,” *Proceedings of the Royal Society A*, 466: 881–890 [[available online](http://arxiv.org/abs/0907.0372)].
[^nielsen-2011]: Nielsen, M.A., Chuang, I.L., 2011. *Quantum Computation and Quantum Information*, 10th Anniversary edition, Cambridge: Cambridge University Press.
[^pawlowski-2009]: Pawlowski, M., Patarek, T., Kaszlikowski, D., Scarani, V., Winter, A., Zukowski, M., 2009. “A New Physical Principle: Information Causality,” *Nature*, 461: 1101.
[^ramanathan-2010]: Ramanathan, R., Patarek, T., Kay, A., Kurzynski, P., Kaszkilowski, D., 2010. “Local Realism of Macroscopic Correlations,” *Physical Review Letters*, 107: 060405.
[^ringbauer-2014]: Ringbauer, M., Fedrizzi, A., Berry, D.W., White, A.G., 2014. “Information Causality in the Quantum and Post-Quantum Regime,” *Scientific Reports*, 4: 6955.
[^schrödinger-1935]: Schrödinger, E., 1935. “Discussion of Probability Relations Between Separated Systems,” *Proceedings of the Cambridge Philosophical Society*, 31: 555–563; 32 (1936): 446–451.
[^schumacher-1995]: Schumacher, B., 1995. “Quantum Coding,” *Physical Review A*, 51: 2738–2747.
[^shannon-1949]: Shannon, C.E., Weaver, W., 1949. *The Mathematical Theory of Communication*, Urbana: University of Illinois Press.
[^skrzypczyk-2009]: Skrzypczyk, P., Brunner, N., Popescu, S., 2009. “Emergence of Quantum Correlations from Nonlocality Swapping,” *Physical Review Letters*, 102: 110402.
[^steane-1998]: Steane, A.M., 1998. “Quantum Computing,” *Reports on Progress in Physics*, 61: 117–173.
[^steane-2003]: –––, 2003. “A Quantum Computer Needs Only One Universe” *Studies in History and Philosophy of Modern Physics*, 34B: 469–478 [[available online](http://arxiv.org/abs/quant-ph/0003084)].
[^timpson-2013]: Timpson, C.G., 2013. *Quantum Information Theory and the Foundations of Quantum Mechanics*, Oxford, Oxford University Press.
[^dam-2013]: van Dam, W., 2013. “Implausible consequences of superstrong nonlocality,” *Natural Computing*, 12(1): 9–12.
[^fraassen-1982]: van Fraassen, B., 1982. “The Charybdis of Realism: Epistemological Implications of Bell’s Inequality,” *Synthese*, 52: 25–38.
[^wootters-1982]: Wootters, W.K., Zurek, W.H., 1982. “A Single Quantum Cannot be Cloned,” *Nature*, 299: 802–803.
[^yin-2017]: Yin, J. et al., (2017). “Satellite-based Entanglement Distribution Over 1200 Kilometers, *Science*, 356: 1140–1144.
[^zeilinger-2018]: Zeilinger, A. (2018). “Quantum Teleportation, Onwards and Upwards,” *Nature Physics*, 14: 3-4.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=qt-entangle)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/qt-entangle/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=qt-entangle&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/qt-entangle/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- [量子物理 arXiv 电子预印本库](http://arxiv.org/find/quant-ph)。
- [Todd Brun 的量子信息处理讲义](http://www-bcf.usc.edu/~tbrun/Course/index.html)。
- [John Preskill 的量子信息与计算课程](http://www.theory.caltech.edu/~preskill/ph219/ph219_2018-19)。
- [Oxford Quantum](http://oxfordquantum.org)，牛津大学。
- [量子光学与量子信息研究所](http://www.iqoqi-vienna.at)，奥地利科学院。
- [GAP-Optique](https://www.unige.ch/gap/quantum/start)，日内瓦大学。
- [量子技术中心](http://www.quantumlah.org)，新加坡大学。
- [联合量子研究所](http://jqi.umd.edu)，马里兰大学。
- [《造梦机器》](http://www.newyorker.com/magazine/2011/05/02/dream-machine)，*New Yorker* 刊载的量子计算文章，2011 年。
- [《新量子理论或可解释时间的流动》](http://www.wired.com/2014/04/quantum-theory-flow-time/)，*Wired* 刊载的文章，2014 年，转载自 *Quanta Magazine*。
- [《幽灵般的超距作用？》](https://www.youtube.com/watch?gl=IT&hl=it&v=ta09WXiUqcQ)，David Mermin 的奥本海默讲座。

## 相关词条

贝尔定理 | 量子力学的哥本哈根诠释 | 埃弗雷特量子力学 | 量子力学的多世界诠释 | 量子贝叶斯模型和实用主义的量子理论观点 | 量子计算 | 量子逻辑和概率论 | 量子理论中的爱因斯坦-波多尔斯基-罗森论证 | 汉斯·赖兴巴赫的共同原因原理

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
