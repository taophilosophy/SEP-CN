# 图式 schema (John Corcoran and Idris Samawi Hamid)
*首次发表于 2004 年 5 月 28 日；2016 年 8 月 2 日实质修订。*

**图式**（*schema*；复数 *schemata* 或 *schemas*），英文中又称 *scheme*（复数 *schemes*），是一种语言的“模板”“框架”或“模式”，另配一条使用规则，用来指定数量上可能无穷的短语、语句或论证；被指定出来的这些，称为该图式的 **实例**。图式在逻辑学中用于指定推理规则，在数学中用于描述含无穷多条公理的理论，在语义学中用于给出真之定义的适当性条件。

## 1 什么是图式？

一个图式是由以下两部分组成的复合系统：

1. **模板文本**（*template-text*）或 **图式模板**（*schema-template*）：一个句法字符串，由有意义的词和／或符号以及占位符（字母、空白、带圈数字、省略号，以及“第一个”“第二个”这类序数表达式，等等）构成；以及
2. **附加条件**（*side condition*）：规定占位符应如何填入才能得到实例，有时也规定有意义的词或符号应如何理解（Tarski 1933/1983: 155; Church 1956: 172）[^church-1956][^tarski-1933][^tarski-1983]。具体说来，附加条件规定该图式的实例应属于哪一种语言——自然语言还是形式语言。

最著名的图式之一，是塔尔斯基（Alfred Tarski）的图式 T；其模板文本是一个含两处省略号、由八个英语词构成的字符串：

> ……是真语句，当且仅当……。

附加条件要求：第二个空白处填入一个（陈述性的）英语句子，第一个空白处填入该句子的一个名称（Tarski 1933/1983: 155）[^tarski-1933][^tarski-1983]。下面这个字符串便是一例：

> “零是一”是真语句，当且仅当零是一。

若换上一个既不知为真、也不知为假的句子，便能得到更能说明问题的实例：

> “每个完全数都是偶数”是真语句，当且仅当每个完全数都是偶数。

下面这个由十四个英语词构成的句子

> 或者零是偶数，或者零是偶数这件事并非如此。

是 **英语排中语句图式** 的一个实例；该图式采用的模板为

> 或者 $A$，或者 $A$ 并非如此。

附加条件是：两处 “$A$” 都填入同一个合式英语陈述句；这个不连续表达式 “Either … or … ” 表达经典相容析取；由六个英语词构成的句首 “it is not the case that” 表达经典否定。注意，这个图式模板并不是一个英语句子。严格说来，把它当作句子用于断言，是不连贯的。称它为真或假也是错的，尽管在“有效”“无效”这两个多义词的适当含义上，可以把它刻画为有效或无效。

有些逻辑学家似乎把图式等同于模板本身。（Tarski 在 1933/1983: 155–6 的措辞暗示了这种等同，而邱奇（Alonzo Church）在 1956: 149 的措辞似乎有意避开它。）[^church-1956][^tarski-1933][^tarski-1983] 但同一个图式模板，依附加条件或底层语言的不同，可以是任意多个不同图式的组成部分。再者，可以用不同的字符或字符串充当占位符（见上文）；而且，哪怕改动一处记号，严格说来也会产生不同的句法字符串（Corcoran et al. 1974）[^corcoran-1974]，因此，即使语言固定，同一组实例也可能由不同的“图式模板—附加条件”配对来确定。也许正是这一事实，让一些作者写起来仿佛图式就该等同于实例的集合。在许多场合，首要的是那组指定出来的实例；至于“指定究竟涉及什么”，只被当成纯技术性问题。

有时（如上面的排中图式），图式模板中的占位符用字母标出。务必牢记下面两者的区别：一边是开语句，例如 “$(x + y) = (y + x)$”，其中的对象语言数值变元 “$x$” 与 “$y$” 取值为数；另一边是图式，例如 **数论交换律图式**，其模板文本为 “$(X + Y) = (Y + X)$”，附加条件是：两处 “$X$” 都替换为同一个数词的两处出现，两处 “$Y$” 亦然。数词属于对象语言，占位符属于元语言。对象语言中的变元取值于对象域，模板文本中的“哑字母”则只是句法代入项的占位符。（对这一区分，Quine 1945: 第 1 节有细致的阐述。）[^quine-1945]

按实例的句法类型，图式可分为语句图式、次语句图式与论证文本图式。我们已经见过两个语句图式的例子。下面这个字符串

> $A$ 的后继

是 **次语句图式** 的模板文本；其附加条件规定，字母 “$A$” 应替换为阿拉伯数字。下面这个限定摹状词

> 9 的后继

会是它的一个实例。注意，这个图式与下面这个开词项大不相同：

> $x$ 的后继，

这里的 “$x$” 是对象语言变元。图式本质上是一份生成句法实例的配方。其模板文本中的“哑字母” “$A$”，只是代入项（这里是数词）的占位符。相比之下，开词项中的 “$x$” 是取值于对象（这里是数）的变元。

**论证文本图式** 是实例为论证文本的图式。**论证文本** 由两部分组成：一组称为前提的语句，加上一个称为结论的语句。（**论证** 是论证文本所表达的东西，正如命题是语句所表达的东西。）在呈现论证文本的种种方式中，最不容易被误解的也许是“前提—横线—结论”格式：先列出前提，再画一条横线，最后写出结论。例如：

$$ \begin{align} & \textrm{Every circle is a polygon.}\\ & \textrm{Every triangle is a circle.}\\ & \textrm{Every square is a triangle.}\\\hline & \textrm{Every square is a polygon.} \end{align} $$

论证文本图式的一个例子，是推理规则 **肯定前件式**（*modus ponens*）：

$$ \begin{align} & A\\ & \textrm{if } A \textrm{ then }B\\\hline & B \end{align} $$

附加条件规定：“$A$” 与 “$B$” 替换为英语陈述句；两处 “$A$”（以及两处 “$B$”）都替换为同一个句子或公式。

公理图式可以看作零前提的论证文本图式。

## 2 图式的用途

图式用于逻辑学、数学和语义学中的形式化。在逻辑学中，图式用来指定一个系统的公理与推理规则。例如，一阶逻辑的一种形式化（Shapiro 1991: 65）[^shapiro-1991] 规定：

> 将公式代入希腊字母后得到的任何公式都是 **公理**：
>
> $$ \begin{align} \Phi & \rightarrow(\Psi \rightarrow \Phi)\\ (\Phi \rightarrow(\Psi \rightarrow \Xi)) & \rightarrow((\Phi \rightarrow \Psi) \rightarrow(\Phi \rightarrow \Xi))\\ (\neg \Phi \rightarrow \neg \Psi) & \rightarrow(\Psi \rightarrow \Phi)\\ \forall x\Phi(x) & \rightarrow \Phi(t) \end{align} $$
>
> 其中 $t$ 是对于 $\Phi$ 中的 $x$ 自由的项，

并且规定：任何如下形式的推理

$$ \begin{align} & \Phi\\ & \Phi \rightarrow \Psi\\\hline & \Psi\\ \end{align} $$

或（其中 $x$ 不在 $\Phi$ 中自由出现）

$$ \begin{align} \Phi & \rightarrow \Psi(x)\\\hline \Phi & \rightarrow \forall x\Psi(x), \end{align} $$

都是有效的。

有些数学理论可以在一阶语言中有限公理化，某些在历史上很重要的数论与集合论却做不到。这类理论的公理有时可以用图式来指定。例如，一阶数论的归纳原则，就用下面的图式指定：

$$ [F(0) \mathbin{\&} \forall x((\textit{Num}(x) \mathbin{\&} F(x)) \rightarrow F(sx)] \rightarrow \forall x(\textit{Num}(x) \rightarrow F(x)) $$

其中，标有 “$F(x)$” 的两处空白，填入一个含变元 “$x$” 一处或多处自由出现的一阶公式；标有 “$F(0)$” 的空白，填入同一个公式，但其中 “$x$” 的每一处自由出现都已替换为 “0” 的一处出现；标有 “$F(sx)$” 的空白，同样填入该公式，但其中 “$x$” 的每一处自由出现都已替换为 “$sx$” 的一处出现。

例如，若在标有 “$F(x)$” 的两处空白中填入 “$x\ne s x$”，便得到：

$$ [ 0\ne s0 \mathbin{\&} \forall x ((\textit{Num} (x) \mathbin{\&} x\ne s x) \rightarrow s x\ne ss x)] \rightarrow \forall x (\textit{Num} (x) \rightarrow x\ne s x) $$

若以英语为底层对象语言，可以采用下面的模板文本。

如果零是 $F$，且每个是 $F$ 的数的后继也是 $F$，那么每个数都是 $F$，

其中四处 “$F$”，都填入同一个算术谓词（例如 “小于某个素数”）。

相比之下，在数论的二阶形式化中，只需给出一条归纳公理：

$$ \forall F \{[F (0) \mathbin{\&} \forall x ((\textit{Num} (x) \mathbin{\&} F (x)) \rightarrow F(sx)] \rightarrow \forall x (\textit{Num} (x) \rightarrow F(x))\} $$

对每个 $F$，如果零是 $F$，且每个是 $F$ 的数的后继也是 $F$，那么每个数都是 $F$。

在这里，“$F$” 不是图式中的占位符，而是名副其实的变元，取值于属性或类（在某些解释下，以复数方式取值于个体）。关于一阶逻辑与二阶逻辑的比较，见 Corcoran 1998。

一阶归纳图式与二阶归纳公理在书写上相似，这种相似偏偏容易掩盖两者的重要差别。后者是语言中的一个句子，前者只是一份生成句子的配方。两者在推理上也不等价：一阶归纳图式的实例集合，在逻辑上弱于二阶归纳公理。也就是说，有些一阶算术语句可以从二阶归纳公理（连同算术的其他公理——这些公理为一阶与二阶算术所共有）推出，却不能从一阶归纳图式的实例推出（见 Shapiro 1991: 110）[^shapiro-1991]。

图式在语义学中也扮演了重要角色。塔尔斯基认为，他的“T 图式”（他称之为“scheme”）的实例，可以看作“真的部分定义”，更确切地说，是“真语句”的部分定义：

> 这类句子的一般图式可以这样刻画：
>
> - (2) $x$ 是真语句，当且仅当 $p$。
>
> 要得到具体的定义，我们就在这个图式中，用任意一个句子替换符号 “$p$”，用该句子的任意一个个体名称替换 “$x$”。（Tarski 1933/1983: 155–6）[^tarski-1933][^tarski-1983]

他把“以所有这些‘部分定义’为后承”，当作一种语言中“真语句”定义的适当性标准（Tarski 1933/1983: 187–8）[^tarski-1933][^tarski-1983]。

## 3 图式的本体论地位

务必弄清图式在本体论上的混合地位。图式的模板文本是句法对象，是一个字符串，本体论预设与数词、词、公式之类相同。例如，英语命名图式的模板文本——“表达式……命名实体……”——是一个四十字符的表达式，含二十七处字母、六处空格、七处句点。另一方面，附加条件是内涵性实体，可与命题相类比。

图式模板是一个字符串类型；按皮尔士（Charles Sanders Peirce）意义上的“殊例”来说，它拥有不定多的殊例（Peirce 1906; Corcoran et al. 1974: 638 n. 5）[^corcoran-1974][^peirce-1906]。但图式模板的任何殊例，都不是该图式的实例。事实上，图式的每个实例都是一个字符串类型，各有自己的殊例。“实例”是关系名词，表示某些字符串类型与某些图式之间的某种关系。“殊例”也是关系名词，表示某些宏观物理对象与某些抽象对象之间的某种关系。图式与图式模板，都不是指称实例的通名，也都不是某组实例的专名。

有些哲学家强调，用图式而不用二阶公理，可以在本体论上节省（例如 Quine 1970/1986）[^quine-1970]。但这些哲学家几乎从未完整而客观地讨论过使用图式所带来的“本体论承诺”。例如，数论 **本身** 预设了数的存在，也许还预设了数函数与数属性的存在，但并不预设数学记号的存在；它 **更不必说** 并不预设有我们称为数论语言的那套庞大而精细的记号系统。有时，使用图式会减少对象语言的本体论承诺，却增加元语言的本体论承诺，或者至少没有实现任何净节省。

## 4 逻辑史中的图式

希腊词 “schema” 在柏拉图的学园中用来指“[几何]图形”，在亚里士多德的吕克昂中用来指“[三段论]格”。亚里士多德的三段论格即“schemata”虽不是现代意义上的图式，他的“式”却是。例如，巴巴拉式（BARBARA）的模板文本为：

$$ \begin{align} & P \textrm{ belongs-to-every }M.\\ & M \textrm{ belongs-to-every }S.\\\hline & P \textrm{ belongs-to-every }S. \end{align} $$

与之相应的附加条件是：(1) 两处 “$P$” 都填入同一个通名；(2) 两处 “$M$” 都填入同一个通名，且不同于 “$P$” 所用的通名；(3) 两处 “$S$” 都填入同一个通名，且不同于 “$P$” 与 “$M$” 所用的通名；(4) 表达式 “belongs-to-every” 被理解为表达《前分析篇》中的全称肯定谓述。斯多亚命题逻辑的规则，一向被认为属于图式。

“schema” 一词在现代意义上的自觉使用始于何时，很难确定。罗素（Bertrand Russell）的《数理哲学导论》（*Introduction to Mathematical Philosophy*，1919）只是顺带用它来描述命题函项：

> 命题函项……不妨看作一个纯粹的图式、一个空壳、一个盛放意义的空容器，而不是某种已经有意义的东西。（1919: 157）

但命题函项并不是现代意义上的句法图式。塔尔斯基 1933 年那篇定义真之的论文（Tarski 1933/1983: 157, 160, 172）[^tarski-1933][^tarski-1983] 是最早以接近本文所论含义使用“scheme”一词的著名出版物之一（Tarski 1933/1983: 155, 156）[^tarski-1933][^tarski-1983]。第二次世界大战前，塔尔斯基也使用“schema”一词及其复数“schemata”（1983: 63–64, 114, 310, 386, 423）。

20 世纪初的逻辑形式化，采用所谓“代入规则”配合有穷多公理，而不是用图式指定无穷多条公理。这些“代入规则”并非人们熟悉的“以相等者替换相等者”规则，而更接近今天所说的例示规则。“代入规则”的直观动机非常简单，实现它的句法细节却“复杂得难以忍受”——这是 Paul Rosenbloom（1950: 109）的说法。事实上，好几位一流逻辑学家因此犯下令人尴尬的错误，Rosenbloom 在上引之处记录了这些错误。邱奇（1956: 158）把“使用公理图式这一设计”归功于冯·诺伊曼（John von Neumann），正是它使那条（出了名地难以陈述的）代入规则成为多余。

正如邱奇所强调的（如 1956: 59），对图式作元数学处理，需要使用形式化语言或逻辑上完善的语言，以及一套公理化的字符串理论——后者首次出现于塔尔斯基 1933 年定义真之的论文（1933/1983: 152–256）。关于这个重要却在某种程度上被忽视的领域的历史、哲学与数学，详见 Corcoran *et al*. 1974；Corcoran 2006。

## References（引用注释）

**以下文献从原文照录，不作翻译；中国文献译为中文。**

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

[^church-1956]: Church, A., 1956, *Introduction to Mathematical Logic*, Princeton: Princeton University Press.
[^corcoran-1998]: Corcoran, J., 1998, “Second-order Logic”, in C.S. Anderson and M. Zeleny (eds.), *Logic, Meaning, and Computation: Essays in Memory of Alonzo Church*, Dordrecht: Kluwer.
[^corcoran-2006]: –––, 2006, “Schemata: the Concept of Schema in the History of Logic”, *Bulletin of Symbolic Logic*, 12(2): 219–40. doi:10.2178/bsl/1146620060
[^corcoran-2009]: –––, 2009, “Aristotle’s Demonstrative Logic”, *History and Philosophy of Logic*, 30:1–20. doi:10.1080/01445340802228362
[^corcoran-1974]: Corcoran, J., W. Frank, & M. Maloney, 1974, “String theory”, *Journal of Symbolic Logic*, 39(4): 625–637. doi:10.2307/2272846
[^feferman-2004]: Feferman, A. and S. Feferman, 2004, *Alfred Tarski: Life and Logic*, Cambridge: Cambridge University Press.
[^feferman-1983]: Feferman, S. and G. Jäger, 1983, “Choice principles, the bar rule and autonomously iterated comprehension schemes in analysis”, *Journal of Symbolic Logic*, 48: 63–70.
[^horsten-2011]: Horsten, L., 2011, *The Tarskian Turn: Deflationism and Axiomatic Truth*, Cambridge, MA: MIT Press.
[^kleene-1967]: Kleene, S.C., 1967, *Mathematical Logic*, New York: Wiley and Sons; reprinted, New York: Dover, 2002.
[^peirce-1906]: Peirce, C., 1906, “Prolegomena to an Apology for Pragmaticism”, *Monist*, 16: 492–546.
[^quine-1945]: Quine, W. V., 1945, “On the Logic of Quantification”, *Journal of Symbolic Logic*, 10: 1–12.
[^quine-1970]: –––, 1970, *Philosophy of logic*, Cambridge MA: Harvard University Press, reprinted 1983.
[^rosenbloom-1950]: Rosenbloom, P., 1950. *Elements of Mathematical Logic*, Dover, New York.
[^russell-1919]: Russell, B., 1919, *Introduction to Mathematical Philosophy*, London: George Allen and Unwin.
[^shapiro-1991]: Shapiro, S., 1991, *Foundations without Foundationalism: A Case for Second-order Logic*, Oxford: Oxford University Press.
[^tarski-1933]: Tarski, A., 1933, “The concept of truth in the languages of the deductive sciences” (Polish), *Prace Towarzystwa Naukowego Warszawskiego, Wydzial III Nauk Matematyczno-Fizycznych*, 34, Warsaw; reprinted in Zygmunt 1995: 13–172; expanded English translation in Tarski 1983: 152–278.
[^tarski-1983]: –––, 1983, *Logic, Semantics, Metamathematics: Papers from 1923 to 1938*, edited with introduction and analytic index by John Corcoran, Indianapolis: Hackett Publishing Company.
[^heijenoort-1967]: van Heijenoort, J., 1967, *From Frege to Gödel*, Cambridge MA: Harvard University Press.
[^zygmunt-1995]: Zygmunt, J. (ed.), 1995, *Alfred Tarski, Pisma Logiczno-Filozoficzne, 1 Prawda*, Warsaw: Wydawnictwo Naukowe PWN.

## 学术工具

* [如何引用本词条](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=schema)。
* [预览本词条的 PDF 版本](https://leibniz.stanford.edu/friends/preview/schema/)，见 [SEP 学会之友](https://leibniz.stanford.edu/friends/)。
* 在 [InPhO](https://www.inphoproject.org/entity?sep=schema&redirect=True) 查找与本词条相关的话题与思想家。
* 在 [PhilPapers](https://philpapers.org/sep/schema/) 查看本词条的增强文献目录及其数据库链接。

## 其他网络资源

- [公理图式](http://mathworld.wolfram.com/AxiomSchema.html)，见 mathworld.wolfram.com。

## 相关词条

论证与论辩 | 亚里士多德的逻辑学 | 逻辑常项 | 本体论承诺 | 威拉德·冯·奥曼·蒯因 | 伯特兰·罗素 | 阿尔弗莱德·塔尔斯基

**（译注：相关词条的中文站内链接将由管线在对应词条重译完成后统一挂接。）**
