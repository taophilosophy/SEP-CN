# Schema
**First published Fri May 28, 2004; substantive revision Tue Aug 2, 2016**

*Corcoran, John, Hamid, Idris Samawi*

A *schema* (plural: *schemata*, or *schemas*), also known as a *scheme* (plural: *schemes*), is a linguistic “template”, “frame”, or “pattern” together with a rule for using it to specify a potentially infinite multitude of phrases, sentences, or arguments, which are called *instances* of the schema. Schemas are used in logic to specify rules of inference, in mathematics to describe theories with infinitely many axioms, and in semantics to give adequacy conditions for definitions of truth.

## 1. What is a Schema?

A schema is a complex system consisting of

1. a *template-text* or *schema-template*: a syntactic string composed of significant words and/or symbols and also of placeholders (letters, blanks, circled numbers, ellipses, ordinal number expressions like ‘the first’ and ‘the second’, etc.), and
2. a *side condition* specifying how the placeholders are to be filled to obtain instances, and also, sometimes, how the significant words or symbols are to be understood (Tarski 1933/1983: 155; Church 1956: 172)[^church-1956][^tarski-1933][^tarski-1983]. In particular, the side condition specifies the language, whether natural or formal, to which the instances of the schema are to belong.

Among the best-known schemas is Tarski’s schema T, whose template-text is the eight-word two-ellipsis string:

> …is a true sentence if and only if….

The side condition requires that the second blank is to be filled in with a (declarative) sentence of English and the first blank is to be filled in by a name of that sentence (Tarski 1933/1983: 155)[^tarski-1933][^tarski-1983]. The following string is an instance:

> ‘zero is one’ is a true sentence if and only if zero is one.

More revealing instances are obtained by using a sentence not known to be true and not known to be false:

> ‘every perfect number is even’ is a true sentence if and only if every perfect number is even.

The fourteen-word sentence

> Either zero is even or it is not the case that zero is even.

is an instance of the *excluded-middle sentence schema for English*, which involves the template

> Either $A$ or it is not the case that $A$.

The side condition is that the two occurrences of ‘$A$’ are to be filled by occurrences of the same well-formed English declarative sentence, that the discontinuous expression ‘Either … or … ’; expresses classical non-exclusive disjunction, and that the six-word sentence-prefix ‘it is not the case that’; expresses classical negation. Notice that this schema-template is not an English sentence. It would be strictly speaking incoherent to use it as a sentence in an attempted assertion. It would also be wrong to call it true or false, though it can be characterized as valid or invalid, in appropriate senses of these ambiguous words.

Some logicians seem to identify the schema with the template alone. (Tarski’s wording at 1933/1983: 155–6 suggests this identification, while Church’s at 1956: 149 seems calculated to avoid it.)[^church-1956][^tarski-1933][^tarski-1983] But one and the same schema-template may be a component of any number of different schemata depending on the side condition or the underlying language. Furthermore, since different characters or strings can be used as placeholders (see above) and since even one notational change produces a different syntactic string in the strict sense (Corcoran et al. 1974)[^corcoran-1974], one and the same set of instances may be determined by different schema-template/side-condition pairings even given a fixed language. It may be this fact that leads some authors to write as though the schema is to be identified with the set of instances. For many purposes it is the set of specified instances that is of primary importance and the question of exactly what is involved in specifying it is considered a mere technicality.

Sometimes (as in the excluded-middle schema, above) the placeholders in a schema-template are marked by letters. It is important to keep in mind the distinction between, on one hand, an open sentence, such as ‘$(x + y) = (y + x)$’; whose object-language numerical variables ‘$x$’ and ‘$y$’ range over the numbers and, on the other, a schema such as *the number-theoretic commutativity schema* whose template-text is ‘$(X + Y) = (Y + X)$’; and whose side condition is that the two occurrences of ‘$X$’ are to be replaced by two occurrences of one and the same numeral, and likewise for the two occurrences of ‘$Y$’. The numerals belong to the object language, while the place-holders belong to the metalanguage. The variables in the object-language range over a domain of objects, while the ‘dummy letters’ in the template-text are just placeholders for syntactic substituends. (For a careful exposition of the distinction, see Quine 1945: sec. 1.)[^quine-1945]

Schemas may be classed by the syntactic type of their instances as sentence schemas, subsentential schemas, or argument-text schemas. We have already seen two examples of sentence schemas. The string

> the successor of $A$

is the template-text for a *subsentential schema*, where the side condition specifies that the letter ‘$A$’ be replaced by an arabic numeral. The definite description

> the successor of 9

would be an instance. Note that this schema is very different from the open term

> the successor of $x$,

where the ‘$x$’ is an object-language variable. The schema is essentially a recipe for generating syntactic instances. The ‘dummy letter’ ‘$A$’ in its template-text is just a placeholder for substituends (here, numerals). The ‘$x$’ in the open term, by contrast, is a variable ranging over objects (here, numbers).

An *argument-text schema* is a schema whose instances are argument-texts. An *argument-text* is a two part system composed of a set of sentences called the premises and a single sentence called the conclusion. (An *argument* is that which is expressed by an argument-text, as a proposition is that which is expressed by a sentence.) Of the various ways of presenting an argument-text perhaps the one least open to misinterpretation is the premises-line-conclusion format which consists in listing the premises followed by a line followed by the conclusion. For example:

$$ \begin{align} & \textrm{Every circle is a polygon.}\\ & \textrm{Every triangle is a circle.}\\ & \textrm{Every square is a triangle.}\\\hline & \textrm{Every square is a polygon.} \end{align} $$

An example of an argument-text schema is the inference rule *modus ponens*:

$$ \begin{align} & A\\ & \textrm{if } A \textrm{ then }B\\\hline & B \end{align} $$

The side condition specifies that ‘$A$’ and ‘$B$’ be replaced with declarative sentences of English, and that both occurrences of ‘$A$’ (and likewise of ‘$B$’) be replaced by the same sentence or formula.

Axiom schemas can be thought of as zero-premise argument-text schemas.

## 2. Uses of Schemas

Schemas are used in the formalization of logic, mathematics, and semantics. In logic, they are used to specify the axioms and inference rules of a system. For example, one formalization of first-order logic (in Shapiro 1991: 65)[^shapiro-1991] states that

> Any formula obtained by substituting formulas for the Greek letters is an *axiom*:
>
> $$ \begin{align} \Phi & \rightarrow(\Psi \rightarrow \Phi)\\ (\Phi \rightarrow(\Psi \rightarrow \Xi)) & \rightarrow((\Phi \rightarrow \Psi) \rightarrow(\Phi \rightarrow \Xi))\\ (\neg \Phi \rightarrow \neg \Psi) & \rightarrow(\Psi \rightarrow \Phi)\\ \forall x\Phi(x) & \rightarrow \Phi(t) \end{align} $$
>
> where $t$ is a term free for $x$ in $\Phi$,

and that any inference of the form

$$ \begin{align} & \Phi\\ & \Phi \rightarrow \Psi\\\hline & \Psi\\ \end{align} $$

or (where $x$ does not occur free in $\Phi)$

$$ \begin{align} \Phi & \rightarrow \Psi(x)\\\hline \Phi & \rightarrow \forall x\Psi(x), \end{align} $$

is valid.

Some mathematical theories can be finitely axiomatized in a first-order language, but certain historically important number theories and set theories cannot. The axioms of these theories can sometimes be specified using schemata. For example, in first-order number theory the induction principle is specified using the schema

$$ [F(0) \mathbin{\&} \forall x((\textit{Num}(x) \mathbin{\&} F(x)) \rightarrow F(sx)] \rightarrow \forall x(\textit{Num}(x) \rightarrow F(x)) $$

where the two blanks marked ‘$F(x)$’ are to be filled with a first-order formula having one or more free occurrences of the variable ‘$x$’, the blank marked ‘$F(0)$’ is to be filled with the same formula after each free occurrence of ‘$x$’ has been replaced by an occurrence of ‘0’, and the blank labeled ‘$F(sx)$’ is to be filled with the same formula after each free occurrence of ‘$x$’ has been replaced by an occurrence of ‘$sx$’.

For example, if we fill the two blanks marked ‘$F(x)$’ with ‘$x\ne s x$’, we have:

$$ [ 0\ne s0 \mathbin{\&} \forall x ((\textit{Num} (x) \mathbin{\&} x\ne s x) \rightarrow s x\ne ss x)] \rightarrow \forall x (\textit{Num} (x) \rightarrow x\ne s x) $$

Using English as the underlying object language, the following template-text could be used.

If zero is $F$ and the successor of every number that is $F$ is also $F$, then every number is $F$,

where the four occurrences of ‘$F$’ are to be filled in with one and the same arithmetic predicate (e.g., ‘smaller than some prime’).

In a second-order formalization of number theory, by contrast, a single induction axiom can be given:

$$ \forall F \{[F (0) \mathbin{\&} \forall x ((\textit{Num} (x) \mathbin{\&} F (x)) \rightarrow F(sx)] \rightarrow \forall x (\textit{Num} (x) \rightarrow F(x))\} $$

For every $F$, if zero is $F$ and the successor of every number that is $F$ is also $F$, then every number is $F$.

Here ‘$F$’ is not a placeholder in a schema, but a genuine variable ranging over properties or classes (or, on some interpretations, ranging plurally over individuals). For comparisons between first-order and second-order logic, see Corcoran 1998.

The orthographic similarities between the first-order induction schema and the second-order induction axiom have an unfortunate tendency to obscure the important differences between them. The latter is a sentence in the language, whereas the former is just a recipe for generating sentences. Nor are they inferentially equivalent: the set of instances of the first-order induction schema is logically weaker than the second-order induction axiom. That is, there are sentences of first-order arithmetic that can be deduced from the second-order induction axiom (together with the other axioms of arithmetic, which are common to first-order and second-order arithmetic) but not from the instances of the first-order induction schema (see Shapiro 1991: 110)[^shapiro-1991].

Schemas have also played a prominent role in semantics. Tarski held that an instance of his ‘T-schema’ (which he calls a ‘scheme’) could be regarded as a “partial definition of truth”, or rather of “true sentence”:

> The general scheme of this kind of sentence can be depicted in the following way:
>
> - (2) $x$ is a true sentence if and only if $p$.
>
> In order to obtain concrete definitions we substitute in the place of the symbol ‘$p$’ in this scheme any sentence, and in the place of ‘$x$’ any individual name of this sentence. (Tarski 1933/1983: 155–6)[^tarski-1933][^tarski-1983]

He took it to be a criterion of adequacy for a definition of ‘true sentence’ for a language that it have all such ‘partial definitions’ as consequences (Tarski 1933/1983: 187–8)[^tarski-1933][^tarski-1983].

## 3. Ontological Status of Schemas

It is important to be clear about the mixed ontological status of schemas. The template-text of the schema is a syntactic object, a string of characters, and has the same ontological presuppositions as numerals, words, formulas, and the like. For example, the template-text for the English naming schema—‘The expression … names the entity …’— is a forty-character expression involving twenty-seven letter-occurrences, six occurrences of the space, and seven occurrences of the period. On the other hand, the side condition is an intensional entity comparable to a proposition.

A schema-template is a string type having indefinitely many tokens in Peirce’s sense (Peirce 1906; Corcoran et al. 1974: 638 n. 5)[^corcoran-1974][^peirce-1906]. But none of the tokens of a schema-template are instances of the schema. In fact, every instance of a schema is a string type having its own tokens. The word ‘instance’ is a relation noun for a relation certain string types bear to certain schemas. The word ‘token’ is a relation noun for a relation certain macroscopic physical objects bear to certain abstract objects. Neither a schema nor a schema-template is a common noun denoting the instances, and neither is a proper name of a set of instances.

Some philosophers emphasize the ontological economies possible by using schemas rather than second-order axioms (e.g., Quine 1970/1986)[^quine-1970]. But rarely if ever do these philosophers present a full and objective discussion of the “ontological commitments” entailed by the use of schemas. For example, number theory *per se* presupposes the existence of numbers, and perhaps numerical functions and numerical properties, but it does not presuppose the existence of mathematical notation and it *a fortiori* does not presuppose the existence of the vast, intricate notational system that we call the language of number theory. Sometimes the use of schemas may decrease the ontological commitments of the object language while increasing those of the metalanguage, or at least not achieving any net savings.

## 4. Schemas in the History of Logic

The Greek word ‘schema’; was used in Plato’s Academy for “[geometric] figure” and in Aristotle’s Lyceum for “[syllogistic] figure”. Although Aristotle’s syllogistic figures or “schemata” were not schemas in the modern sense, Aristotle’s moods were. For example, the template-text of the mood BARBARA is

$$ \begin{align} & P \textrm{ belongs-to-every }M.\\ & M \textrm{ belongs-to-every }S.\\\hline & P \textrm{ belongs-to-every }S. \end{align} $$

The associated side condition is that (1) both occurrences of ‘$P$’ are to be filled with occurrences of one and the same common noun, (2) both occurrences of ‘$M$’ are to be filled with occurrences of one and the same common noun other than the one used for ‘$P$’, (3) both occurrences of ‘$S$’ are to be filled with occurrences of one and the same common noun other than the ones used for ‘$P$’ and ‘$M$’, and that (4) the expression ‘belongs-to-every’ is taken to express universal affirmative predication as in the *Prior analytics*. The rules of the Stoic propositional logic have been taken to be schemas.

It is hard to date self-conscious use of the word ‘schema’; in the modern sense. Russell’s *Introduction to Mathematical Philosophy* (1919) uses it casually to describe propositional functions:

> A propositional function … may be taken to be a mere schema, a mere shell, an empty receptacle for meaning, not something already significant. (1919: 157)

But propositional functions are not syntactic schemas in the modern sense. Tarski’s 1933 truth-definition paper (Tarski 1933/1983: 157, 160, 172)[^tarski-1933][^tarski-1983] was one of the first prominent publications to use the word ‘scheme’ in a sense close to that of this article (Tarski 1933/1983: 155, 156)[^tarski-1933][^tarski-1983]. Tarski also uses the word ‘schema’, and its plural ‘schemata’, in the pre-World-War II period (1983: 63–64, 114, 310, 386, 423).

Early twentieth-century formalizations of logic used what were called “substitution rules” with finite set of axioms instead of schemata that specified infinitely many axioms. These “substitution rules” were not the familiar rules for “substituting equals for equals”; rather they were closer to what are called instantiation rules today. The intuitive motivation for “substitution rules” was very simple but the syntactic details for implementing them were “intolerably complex”—to use the words of Paul Rosenbloom (1950: 109). In fact several first-rate logicians were led to make embarrassing errors, as Rosenbloom documents in the place just cited. Church (1956: 158) credits von Neumann with “the device of using axiom schemata”, which rendered the (notoriously difficult to state) substitution rule unnecessary.

As Church has emphasized (e.g., 1956: 59), metamathematical treatment of schemas requires use of formalized or logically perfect languages and an axiomatized theory of strings as found for the first time in Tarski’s 1933 truth-definition paper (1933/1983: 152–256). For more on the history, philosophy, and mathematics of this important but somewhat neglected field, see Corcoran *et al*. 1974; Corcoran 2006).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=schema). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/schema/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=schema&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/schema/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Axiom Schema](http://mathworld.wolfram.com/AxiomSchema.html), at mathworld.wolfram.com.

## Related Entries

argument and argumentation | Aristotle, General Topics: logic | logical constants | ontological commitment | Quine, Willard Van Orman | Russell, Bertrand | Tarski, Alfred

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
