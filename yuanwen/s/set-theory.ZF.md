# set-theory — ZF（supplement）

> （《set-theory》词条补充材料，源：plato.stanford.edu/entries/set-theory/ZF.html）

- Browse
- Table of Contents
- What's New
- [Random Entry](https://plato.stanford.edu/cgi-bin/encyclopedia/random)
- Chronological
- Archives
- About
- Editorial Information
- About the SEP
- Editorial Board
- How to Cite the SEP
- Special Characters
- Advanced Tools
- Contact
- Support SEP
- Support the SEP
- PDFs for SEP Friends
- Make a Donation
- SEPIA for Libraries

- Back to Entry
- Entry Contents
- Entry Bibliography
- Academic Tools
- [Friends PDF Preview ](https://leibniz.stanford.edu/friends/preview/set-theory/)
- [Author and Citation Info ](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=set-theory)
- Back to Top

#### Supplement to [Set Theory](set-theory.index.md)

## Zermelo-Fraenkel Set Theory (ZF)

### Axioms of ZF

> **Extensionality**: \(\forall x\forall y[\forall z (\left.z \in x\right. \leftrightarrow
\left. z \in y\right.) \rightarrow x=y]\)

This axiom asserts that when sets \(x\) and \(y\) have the same members, they are the same set.

The next axiom asserts the existence of the empty set:

> **Null Set**: \(\exists x \neg\exists y (y \in x)\)

Since it is provable from this axiom and the previous axiom that there is a unique such set, we may introduce the notation ‘\(\varnothing\)’ to denote it.

The next axiom asserts that given any sets \(x\) and \(y\), there exists a pair set of \(x\) and \(y\), i.e., a set which has only \(x\) and \(y\) as members:

> **Pairs**: \(\forall x\forall y \exists z \forall w (w\in z \leftrightarrow w=x
\lor w=y)\)

Since it is provable that there is a unique pair set for each given \(x\) and \(y\), we introduce the notation ‘{\(x\),\(y\)}’ to denote it. In the particular case when \( x =y\), the axiom asserts the existence of the *singleton* \( \{ x\}\), namely the set having \( x\) as its unique member.

The next axiom asserts that for any set \(x\), there is a set \(y\) which contains as members all those sets whose members are also elements of \(x\), i.e., \(y\) contains all of the subsets of \(x\):

> **Power Set**: \(\forall x \exists y \forall z[z\in y \leftrightarrow \forall w(w\in
z \rightarrow w\in x)]\)

Since every set provably has a unique ‘power set’, we introduce the notation ‘\(\mathscr{P}(x)\)’ to denote it. Note also that we may define the notion *x is a subset of y* (‘\(x \subseteq y\)’) as: \(\forall z(z\in x\rightarrow
z\in y)\). Then we may simplify the statement of the Power Set Axiom as follows:

> \(\forall x \exists y\forall z(z\in y \leftrightarrow z \subseteq x)\)

The next axiom asserts that for any given set \(x\), there is a set \(y\) which has as members all of the members of all of the members of \(x\):

> **Unions**: \(\forall x\exists y\forall z[z\in y \leftrightarrow \exists w(w\in x
\land z\in w)]\)

Since it is provable that there is a unique ‘union’ of any set \(x\), we introduce the notation ‘\(\bigcup x\)’ to denote it.

The next axiom asserts the existence of an infinite set, i.e., a set with an infinite number of members:

> **Infinity**: \(\exists x[\varnothing\in x \land \forall y(y\in x \rightarrow
\bigcup\{y,\{y\}\}\in x)]\)

We may think of this as follows. Let us define *the union of x and y* (‘\(x\cup y\)’) as the union of the pair set of \(x\) and \(y\), i.e., as \(\bigcup \{x,y\}\). Then the Axiom of Infinity asserts that there is a set \(x\) which contains \(\varnothing\) as a member and which is such that whenever a set \(y\) is a member of \(x\), then \(y\cup\{y\}\) is also a member of \(x\). Consequently, this axiom guarantees the existence of a set of the following form:

> \(\{\varnothing,\{\varnothing\},\{\varnothing,\{\varnothing\}\},\{\varnothing,\{\varnothing\},\{\varnothing,\{\varnothing\}\}\},\ldots\}\)

Notice that the second element, \(\{\varnothing \}\), is in this set because (1) the fact that \(\varnothing\) is in the set implies that \(\varnothing \cup \{\varnothing \}\) is in the set and (2) \(\varnothing \cup \{\varnothing \}\) just is \(\{\varnothing\}\). Similarly, the third element, \(\{\varnothing,\{\varnothing\}\}\), is in this set because (1) the fact that \(\{\varnothing\}\) is in the set implies that \(\{\varnothing \} \cup\{\{\varnothing \}\}\) is in the set and (2) \(\{\varnothing \} \cup \{\{\varnothing \}\}\) just is \(\{\varnothing, \{\varnothing \}\}\). And so forth.

Next is the *Separation Schema*, which is a formula-pattern that uses a metavariable (in this case \(\psi\)) to describe an infinite list of axioms – one axiom for each formula of the language of set theory with at least a free variable. Every instance of the Separation Schema asserts the existence of a set that contains the elements of a given set \(w\) that satisfy a certain condition, which is given by a formula \(\psi\). That is, suppose that \(\psi(x,u_1,\ldots,u_k)\) is a formula of the language of set theory that has \(x\) free and may or may not have \(u_1,\ldots,u_k\) free. Then the Separation Schema for the condition \(\psi\) asserts:

> **Separation**: \(\forall u_1 \ldots\forall u_k [\forall w\exists v\forall r(r\in v
\leftrightarrow r\in w \land \psi(r,u_1,\ldots,u_k))]\)

In other words, given sets \(w\) and \(u_1,\ldots,u_k\), there exists a set \(v\) which has as members precisely the members \(r\) of \(w\) which satisfy the formula \(\psi(r,u_1,\ldots,u_k)\).

Next is the *Replacement Schema*, which is also a formula-pattern that uses a metavariable (in this case \(\phi\)) to describe an infinite list of axioms -- one axiom for each formula of the language of set theory with at least two free variables. Suppose that \(\phi(x,y,u_1,\ldots,u_k)\) is a formula with \(x\) and \(y\) free, and in which \(u_1,\ldots u_k\) may or may not be free. Then the instance of the Replacement Schema given by \(\phi(x,y,u_1,\ldots,u_k)\) is the following axiom:

> **Replacement**: \(\forall u_1 \ldots\forall u_k [\forall x\exists!y\phi(x,y,u_1,\ldots
u_k)\rightarrow\)   \(\forall w\exists v\forall r(r\in v\leftrightarrow
\exists s(s\in w \land \phi (s,r,u_1,\ldots u_k)))]\)

In other words, if we know that \(\phi\) is a functional formula (which relates each set \(x\) to a unique set \(y\)), then if we are given a set \(w\), we can form a new set \(v\) as follows: collect all of the sets to which the members of \(w\) are uniquely related by \(\phi\).

Note that the Replacement Schema can take you ‘out of’ the set \(w\) when forming the set \(v\). The elements of \(v\) need not be elements of \(w\). By contrast, the Separation Schema of Zermelo only yields subsets of the given set \(w\).

The final axiom asserts that every set is ‘well-founded’:

> **Regularity**: \(\forall x[x\ne\varnothing\rightarrow\exists y(y\in x\land\forall
z(z\in x \rightarrow\neg(z\in y)))]\)

A member \(y\) of a set \(x\) with this property is called a ‘minimal’ element. This axiom rules out the existence of circular chains of sets (e.g., such as \(x\in y \land y\in z \land
z\in x\)) as well as infinitely descending chains of sets (such as … \(x_3\in x_2\in x_1\in x_0\)).

Copyright © 2023 by Joan Bagaria <*joan.bagaria@icrea.cat*>

#### Browse

- Table of Contents
- What's New
- [Random Entry](https://plato.stanford.edu/cgi-bin/encyclopedia/random)
- Chronological
- Archives

#### About

- Editorial Information
- About the SEP
- Editorial Board
- How to Cite the SEP
- Special Characters
- Advanced Tools
- Accessibility
- Contact

#### Support SEP

- Support the SEP
- PDFs for SEP Friends
- Make a Donation
- SEPIA for Libraries

#### Mirror Sites

View this site from another server:

- Info about mirror sites

The Stanford Encyclopedia of Philosophy is copyright © 2023 by [The Metaphysics Research Lab](https://mally.stanford.edu/), Department of Philosophy, Stanford University

Library of Congress Catalog Data: ISSN 1095-5054
