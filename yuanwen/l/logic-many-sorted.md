# Many-Sorted Logic
**First published Thu Dec 15, 2022**

*Manzano, María, Aranda, Víctor*

Classical logic is the appropriate formal language for describing mathematical structures containing a single universe or domain of discourse. By contrast, many-sorted logic (MSL) allows quantification over a variety of domains (called sorts). For this reason, it is a suitable vehicle for dealing with statements concerning different types of objects, which are ubiquitous in mathematics, philosophy, computer science, and formal semantics. Each sort groups a unique category of objects (for example, points and straight lines are different types of objects in a 2-sorted structure).

Despite the addition of this expressive resource, many-sorted logic “stays inside” first-order logic, so the main metatheorems (completeness, interpolation, and so on) can be proved. Many-sorted logic also serves as a unifying framework for translating various logical systems; for instance, some intensional and higher-order logics have natural translations into many-sorted logic. Many-sorted first-order logic can be reduced to one-sorted first-order logic, both syntactically and semantically. Many-sorted first-order logic can also be extended to a many-sorted second-order logic called “sort logic”.

An axiomatic calculus for many-sorted logic was introduced by Hao Wang in Wang (1952)[^wang-1952], where he made a comparison between one-sorted and many-sorted theories. In 1967, Solomon Feferman gave a sequent calculus for many-sorted logic, proving not only its completeness but also the cut elimination and interpolation theorems (Feferman 1968)[^feferman-1968]. Feferman (2008)[^feferman-2008] summarizes some applications of the many-sorted interpolation theorems to model theory. (See the [supplement on early history](logic-many-sorted.early-history.md) for more information.)

Section 1 lays out the basics of many-sorted logic, presenting some examples and explaining how the formal language, structures, and semantics differ or not from classical logic. Section 2 explains how to modify a one-sorted first-order calculus to obtain a many-sorted version; also, completeness is treated and some automated theorem provers are mentioned. Section 3 describes a plan on which many-sorted logic serves as a common framework for translating a variety of logical systems. Sections 4 and 5 apply this plan to second-order logic and non-classical logics (modal and dynamic logic), respectively. Finally, section 6 comments on further results in many-sorted logic.

## 1. Syntax and Semantics

### 1.1 Examples

We start with a few examples to illustrate how common statements concerning different types of data can be formalized in many-sorted first-order logic.

#### Example: Euclid’s first principle

Let us begin with geometry, by talking about straight lines and points. According to Euclid’s first principle:

*A straight line can be drawn joining any two points.*

In two sorted first-order logic one can use $X,$ $Y,$… as variables for sort $l$ (straight lines) and $x,$ $y,$… as variables for sort $p$ (points). To formulate Euclid’s principle we write:

$$\forall x\;\forall y(x\not=y\rightarrow \exists X(\Join(Xxy)\land \forall Y(\Join(Yxy)\rightarrow X=Y)))$$

In this example, $\Join$ is a 3-place predicate symbol relating a straight line and two points,

$$\Join(Yxy):= Y \textrm{ joins } x \textrm{ and } y$$

Literally our formalization reads: *“For any two points there is a unique straight line joining them”*.

#### Example: Binary relations

Another mathematical example is about asymmetry and anti-symmetry, both of which are properties of some binary relations. Suppose we wanted to express the claim:

*Every asymmetric binary relation is also anti-symmetric.*

To formalize the statement as a single logically valid *sentence* we need: (1) to express asymmetry and anti-symmetry, and (2) to quantify over binary relations. In a suitable first-order language including $R$ as a binary relation symbol, to express that $R$ is asymmetric we write:

$$\Asymm(R):=\forall x\, \forall y(Rxy\rightarrow \lnot Ryx)$$

and to say that $R$ is anti-symmetric we write:

$$\Antisymm(R):=\forall x\,\forall y(Rxy\land Ryx\rightarrow x=y)$$

In ordinary one-sorted first-order logic, this would be a logically valid *scheme*:

$$\Asymm(R)\rightarrow \Antisymm(R)$$

What we get is an infinite set of formulas obtained by replacing $R$ by any other binary relation symbol. However, we wanted a single logically valid *sentence* and so we need to quantify over binary relations. In second-order logic, taking $X^{2},$ $Y^{2},$… as variables for binary relations we write:

$$\forall X^{2}(\Asymm(X^{2})\rightarrow \Antisymm(X^{2}))$$

But since standard second-order logic lacks some of the nice properties of first-order logic (section 4.1), one could instead go for a two-sorted first-order logic, in which both individuals and relations between individuals are first-class citizens one can quantify over. We would have variables $x,$ $y,\ldots$ of sort $i$ (individuals), and $X^{2},$ $Y^{2},\ldots$ of sort $r$ (binary relations between individuals). However, it is not enough to label our variables as individuals or binary relations, we need them to perform as second-order variables do. A three-place predicate symbol relating binary relations and individuals, $\epsilon_{2} xyX^{2}$, needs to be added so that $\Asymm(X^{2})$ becomes:

$$\Asymm(X^{2}):=\forall x\,\forall y(\epsilon _{2} xyX^{2}\rightarrow \lnot \epsilon_{2} yxX^{2})$$

and similarly for $\Antisymm(X^{2})$.

As we will see in section 4.2, rewriting the second order formula $X^{2}xy$ as $\epsilon_{2}xyX^{2}$ is all we do when translating second-order logic into many-sorted logic; some axioms for predicates $\epsilon _{n}$ are added and a suitable many-sorted theory for the $\epsilon _{n}$ relations is introduced. In many-sorted logic formula

$$\forall X^{2}(\Asymm(X^{2})\rightarrow \Antisymm(X^{2}))$$

is a theorem of the many-sorted theory mentioned.

#### Example: Comprehension Axiom

Let us introduce another, more philosophical, example. If we wanted to formalize:

*Every property has a negation.*

we could use second order logic and write:

$$\forall X\,\exists Y\,\forall x(Yx\leftrightarrow \lnot Xx)$$

That becomes a many-sorted formula when we rewrite it as:

$$\forall X\,\exists Y\,\forall x(\epsilon _{1}xY\leftrightarrow \lnot \epsilon _{1}xX)$$

using $x,y,\ldots$ as variables of sort $i$ (individuals) and $X,Y,\ldots$ of sort *π* (properties).

Formula $\forall X\,\exists Y\,\forall x(Yx\leftrightarrow \lnot Xx)$ is a generalization of an instance of Comprehension Scheme

$$\exists Y^{n}\,\forall x_{1}\ldots\forall x_{n}(Y^{n}x_{1}\ldots x_{n}\leftrightarrow \varphi )$$

(variable $Y^{n}$ is not free at *φ*). Section 4 and section 5 discuss the role played by this scheme in translation from second-order logic into many-sorted first-order logic.

As you will see in section 6.1, each many-sorted formula has a version in a one-sorted first-order language obtained by removing sorts. In this new language all the variables belong to one sort, but we add unary predicates to recover the lost information when passing from the many-sorted expression to the one-sorted one. We also need to guarantee that these new predicates, which represent the lost universes of quantification, are interpreted by non-empty sets, since universes of quantification are non-empty in classical logic.

In Euclid’s example, we add axioms $\exists xLx$ and $\exists xPx$ and formula

$$\forall x\,\forall y(x\not=y\rightarrow \exists X(\Join(Xxy)\land \forall Y(\Join(Yxy)\rightarrow X=Y)))$$

now becomes

$$\begin{multline} \forall x\,\forall y(Px\land Py\land x\not=y\rightarrow \\ \exists z((Lz\land \Join(zxy))\land \forall w((Lw\land \Join(wxy))\rightarrow z=w))) \end{multline}$$

To represent *Every property has a negation* in one-sorted first-order logic we use $x,y,z,\ldots$ as variables for the unique sort we now have, and write:

$$\forall x(Px\rightarrow \exists y(Py\land \forall z(Oz\rightarrow (\epsilon _{1}zx\leftrightarrow \lnot \epsilon _{1}zy))))$$

where

$$\begin{align} Px & :=\text{ asserts that }x\text{ is a property}\\ Ox&:=\text{ asserts that }x\text{ is an object} \\ \epsilon _{1}zx &:=\text{ asserts that }z\text{ belongs to (exemplifies or instantiates) }x \end{align}$$

Some axioms for predicates $\epsilon _{1}$ are added, as well as axioms saying that predicates $P$ and $O$ are never interpreted as empty sets, $\exists xOx$ and $\exists xPx$. Moreover, the links between predicates $\epsilon _{1}$, $P$ and $O$ are expressed by:

$$\forall x\,\forall y(\epsilon _{1}xy\rightarrow Ox\land Py)\\ \forall x(Px\rightarrow \lnot Ox)$$

### 1.2 Fundamental Ideas

To specify the syntax of a many-sorted language and associated structures we need first to say what our (countable) set of sorts is. We take $\Sort=\{ s_{1},\dots ,s_{n}\}$ as the sorts of an *n*-sorted language.[^note-1]

- **Structures:** A many-sorted structure has several non-empty domains, one for each sort, and variables of a given sort take values over the corresponding domain. An *n*-ary relation could be freely established between elements of different domains or only between certain ones. These two options are called *liberal* and *strict*. A liberal relation may relate objects of arbitrary domains and only the arity (a natural number) has to be stated. For a strict relation, the sorts involved have to be specified as well as the arity.
- **Alphabet:** The alphabet of a many-sorted language $L$ includes all the relation, function, and constant symbols in a set called $\OperSym$, as well as an infinite number of variables for each sort $s_{i}\in \Sort$, and the corresponding sets of variables are disjoint. An *n*-ary relation symbol $R$ could be strict or liberal and, in the first case, we must provide information about what are the involved sorts. To achieve this requirement, we define a function $\Rank$ having as domain the set $\OperSym$ and whose values are either natural numbers other than zero (liberal option) or finite strings of $\Sort\cup \{ 0\}$ (strict option). For any strict $f\in \OperSym$, its value $\Rank(f)$ always has the form $\langle i_{1},\ldots,i_{m},i_{0}\rangle$, with $i_{0},i_{1},\ldots,i_{m}\in \Sort\cup \{ 0\}$. When $f$ is an *m*-ary predicate, $i_{0}=0$, and $i_{0}\not=0$ for *m*-ary function symbols; individual constants are considered as zero-ary function symbols with $\Rank(f)=\langle i_{0}\rangle$, simplified as $i_{0}$.
- **Signature:** By a *signature $\Sigma$* we mean the ordered triple $$\ \Sigma =\langle \Sort,\OperSym,\Rank\rangle$$ Equality is a binary symbol that could be strict or liberal. In our language, the equality symbol $\approx$ with $\Rank(\approx )=2$ is liberal (having arity 2 and being allowed to work between terms of any sort).[^note-2] The quantifier $\exists x^{i}$ is used for variables $x^{i}$ of any sort $i$.

In Euclid’s example we have two sorts, $l$ (lines) and $p$ (points) and a 3-place predicate $\Join$ with $\Rank(\Join)=\langle l,p,p,0\rangle$. In the example of binary relations we have two sorts, $i$ (individuals) and $r$ (binary relations) and a 3-place predicate symbol $\epsilon _{2}$ with $\Rank(\epsilon_{2})=\langle i,i,r,0\rangle$. For the comprehension example we have two sorts, $i$ (individuals) and *π* (properties) and a 2-place predicate symbol $\epsilon_{1}$ with $\Rank(\epsilon_{1})=\langle i,\pi ,0\rangle$.

### 1.3 Formal Language

#### Terms and Formulas

As we do in classical first-order logic, from the set of finite strings of elements of the alphabet we select the expressions of $L$: *terms* and *formulas*. The only difference is that in many-sorted logic terms have sorts and we have to specify it.

In consequence, the *terms* of many-sorted logic are defined recursively as follows: Each variable or individual constant of sort $s_{i}$ is a term of the same sort $s_{i}$. If $f\in \OperSym$ is such that $\Rank(f)=\langle i_{1},\ldots,i_{m},i_{0}\rangle$ with $i_{0}\not=0$ and $\tau _{1},\ldots,\tau _{m}$ are terms of sorts $i_{1},\ldots,i_{m}$, then $f\ \tau _{1}\ldots\tau _{m}$ is a term of sort $i_{0}$.

*Atomic formulas* are defined by means of predicates and terms: If $R\in \OperSym$ is such that $\Rank(R)=\langle i_{1},\ldots ,i_{m},0\rangle$, and $\tau _{1},\ldots $,$\tau _{m}$ are terms of sorts $i_{1},\ldots,$ $i_{m}$, then $R\tau _{1}\ldots \tau _{m}$ is a formula (when $R$ is a liberal predicate, we drop the sort requirement for terms). For any terms $\tau _{1}\ $and $\tau _{2}$, the expression $\tau _{1}\approx \tau _{2}$ is a formula. Notice that the sorts of $\tau _{1}\ $and $\tau _{2}$ do not matter, because our choice of equality symbol is the liberal one.[^note-3]

Complex *well-formed formulas* (wffs) are defined as usual in first-order languages (see the entry on classical logic), except for quantified expressions. The new rule says: If *φ* is a formula and $x^{i}$ is a variable of sort $i$, then $\exists x^{i}\varphi$ is a formula as well.

#### Free and bound variables

As in classical first-order logic, occurrences of variables in a formula can be *free* or *bound*; they are bound when they are under the scope of a quantifier, otherwise free. A variable is free in a formula if it has at least one free occurrence therein. A formula with no free variables is called a *sentence*. We use $Sent(L)$ to denote the set of sentences of language $L$.

#### Example: The Book of Perfect Emptiness

Consider the following, from Liezi (Book 5, 1–2):

**The Book of Perfect Emptiness:** Tang of Ying asked Ge: “Did things exist at the dawn of time?”

Xia Ge answered: “If things had not existed at the dawn of time, how could they possibly exist today? By the same token, men in the future could believe that things did not exist today”.

In order to analyze this example, we should identify premises and conclusion; and we easily observe that the initial rhetorical question is in fact the argument’s conclusion. The considered argument is an enthymeme, for the reason that it seems to be supported in the permanence of the laws that govern the cosmos (in particular, those concerning the existence of objects). The hidden hypothesis supporting the argument could be the following law:

> If things exist at a given point in time, then at any given previous moment in time things must have existed.

This rule is not saying that existence of a particular object is eternal, it is saying that the chain of existence goes back forever.

Thus, the argument can be reformulated in the following way, where $\alpha ,$ *β* and *γ* are the premises and *δ* is the conclusion:

- $\alpha :=$ If things exist at a given point in time, then at any given previous moment in time things must have existed.
- $\beta :=$ Things exist today.
- $\gamma :=$ The dawn of time is previous to all else.
- $\delta :=$ Things existed at the dawn of time.

Now, the premises and the conclusion can be formalized by means of a *two sorted language*, $\Sort=\{ i,\tau \}$, including *objects* (sort $i$) and *instants of time* (sort *τ*). The set $\OperSym$ contains a binary predicate of existence at a given time, $E$, another binary predicate of precedence between instants, $P$, and two individual constants for *today* ($t$) and the *dawn* of times $(d)$. So, in this case,

$$\begin{align} \Rank(E) & =\langle i,\tau ,0\rangle,\\ \Rank(P) & =\langle \tau ,\tau ,0\rangle \textrm{ and}\\ \Rank(d) & =\tau =\Rank(t).\\ \end{align} $$

The argument now reads:

$$\begin{align} \alpha & :=\forall x^{\tau }(\exists y^{i}Ey^{i}x^{\tau }\rightarrow \forall z^{\tau }(Pz^{\tau }x^{\tau }\rightarrow \exists v^{i}Ev^{i}z^{\tau }))\\ \beta & :=\exists y^{i}Ey^{i}t \\ \gamma & :=\forall y^{\tau }\ Pdy^{\tau }\\ \delta & :=\exists x^{i}Ex^{i}d \end{align} $$

In many sorted logic, the conclusion is easily obtained from these hypotheses by using a deductive calculus (see section 2). Therefore, the argument is formally correct, once we accept the problematic hypothesis *α*. In section 2.4 we rewrite the argument to use theorem provers LEO-II and LEO-III.

### 1.4 Many-sorted Structures

The semantics of many-sorted logic is rather similar to that of classical first-order logic, because it follows Tarski’s truth definition to introduce the concept of *truth in a structure* (see Tarski 1933 and Tarski & Vaught 1956; for historical clarifications, see Hodges 1986 and the entry on Tarski’s truth definitions)[^hodges-1986][^tarski-1933][^tarski-1956]. In our case, the *object language* is many-sorted logic and the *metalanguage* is set theory. Set theory is the commonly used metalanguage, where relation symbols are interpreted as *relations* defined over *universes* (sets) of mathematical structures.

In many-sorted first-order logic, a structure is understood as a tuple having a family of non-empty sets as domains and a family of operations (functions and relations) defined over these domains. These relations and functions are defined according to a given signature.

#### Examples of many-sorted structures

- An appropriate structure $\mathcal{E}$ for the example in **The Book of Perfect Emptiness** has two universes: instants of time $\mathbf{A}_{\tau}$ and objects $\mathbf{A}_{i}$. It also has two distinguished instants, today and the dawn of times, a binary relation between objects and instants, and a binary temporal relation of precedence. $$\mathcal{E}=\langle \langle \mathbf{A}_{i},\mathbf{A}_{\tau }\rangle ,E^{\mathcal{E}},P^{\mathcal{E}},t^{\mathcal{E}},d^{\mathcal{E}}\rangle$$ In such a structure, $t^{\mathcal{E}},d^{\mathcal{E}}\in \mathbf{A}_{i}$, $E^{\mathcal{E}}\subseteq \mathbf{A}_{i}\times \mathbf{A}_{\tau }$ and $P^{\mathcal{E}}\subseteq \mathbf{A}_{\tau }\times \mathbf{A}_{\tau }$.
- A second-order *standard structure* (or *full structure*) $$\mathcal{A}=\langle \mathbf{A},\langle \wp \left(\mathbf{A}^{n}\right)\rangle _{n\in \mathbb{N}},\langle f^{\mathcal{A}}\rangle _{f\in \OperSym}\rangle$$ is another example of many-sorted structure. This structure includes the domain of individuals $\mathbf{A}$ as well as a family of second order domains of *n*-ary relations on individuals, $\wp (\mathbf{A}^{n})$, for each natural number $n$. The relations and functions in $\langle f^{\mathcal{A}}\rangle _{f\in \OperSym}$ are first-order relations and functions defined over the universe of individuals (for more details about second-order logic, see the entry on second-order and higher-order Logic).
- A second-order *general structure* $\mathcal{A}=\langle \mathbf{A},\langle \mathbf{A}_{n}\rangle _{n\in \mathbb{N}},\ldots \rangle$ could also be seen as many-sorted. As in standard structures, $\mathcal{A}$ contains the domain of individuals $\mathbf{A}$ as well as domains of *n*-ary relations for each natural number, $\mathbf{A}_{n}\subseteq \wp (\mathbf{A}^{n})$. But since $\mathcal{A}$ is a general structure, the universes $\mathbf{A}_{n}$ are not arbitrarily chosen, for the reason that they must satisfy the *Comprehension Schema*. Therefore, the universes are closed under definability (more information on general structures in section 4.1).

#### Many-sorted structures

A many-sorted Σ-structure $\mathcal{A}$ has several universes (or domains) of objects in a family of non-empty sets $\mathbf{A}_{i}$ (for each $i\in Sort$). Structure $\mathcal{A}$ contains as well: an *m*-ary relation $R^{\mathcal{A}}$ for each relation symbol $R$, an *n*-ary function $f^{\mathcal{A}}$ for every *n*-ary function symbol $f$ and a distinguish element $c^{\mathcal{A}}\in \mathbf{A}_{i}$ for every individual constant $c$. These relations and functions have to be established between elements of the family of domains taking into account their values under function $\Rank$.[^note-4]

Using structure $\mathcal{A}$ we define in section 1.5 the truth of a sentence *φ* in this structure, noted as $\mathcal{A}\models \varphi$.

We could add the requirement of empty intersection between different domains. Structures obeying this requirement are called “strict”, otherwise “lax” (or “liberal”). For strict structures we may consider the possibility of having an equality symbol for each sort, $\approx _{i}$, each of them with $\Rank(\approx _{i})=\langle i,i,0\rangle$. We require equality symbols (either strict or liberal) to be interpreted as genuine identity, the prototypical relation that holds between an object and itself and fails to hold between any two other objects.

#### Relations of similarity between structures

For one-sorted structures, it is very common to study different relations between them: *homomorphisms*, *embeddings, isomorphisms, substructures* and *extensions* (see Manzano 1989 [1999: 19–33])[^manzano-1989]. One can define these relations for many-sorted structures in a similar vein. An *homomorphism* between two structures $\mathcal{A}$ and $\mathcal{A}^{\prime }$ with the same signature is a function *π* from the union of the universes of $\mathcal{A}$ to the union of the universes of $\mathcal{A}^{\prime }$ satisfying the following conditions: Firstly, the restriction of *π* to $\mathbf{A}_{i}$ must be a function from $\mathbf{A}_{i}$ to $\mathbf{A}_{i}^{\prime }$, for each $i\in Sort$. Secondly, if the *n*-tuple of elements $\langle \mathbf{a}_{i},\dots ,\mathbf{a}_{n}\rangle$ is in the *n*-ary relation $R^{\mathcal{A}}$ then $\langle \pi (\mathbf{a}_{i}),\dots ,\pi (\mathbf{a}_{n})\rangle$ is in the relation $R^{\mathcal{A}^{\prime }}$. Finally,

$$\pi \left(f^{\mathcal{A}}\left(\mathbf{a}_{i},\dots ,\mathbf{a}_{m}\right)\right)=f^{\mathcal{A}^{\prime }}\left(\pi \left(\mathbf{a}_{i}\right),\dots ,\pi \left(\mathbf{a}_{m}\right)\right)$$

and $\pi (c_{i}^{\mathcal{A}})=c_{i}^{\mathcal{A}^{\prime }}$.

An *embedding* is a homomorphism where the involved functions are injective and the second condition works in both directions. An *isomorphism* is an embedding where the defining maps are bijections. When the function *π* is an isomorphism one says that $\mathcal{A}$ and $\mathcal{A}^{\prime }$ are *isomorphic* and writes $\mathcal{A}\cong \mathcal{A}^{\prime }$.

We say that $\mathcal{A}^{\prime }$ is a *substructure* of $\mathcal{A}$ (equivalently, $\mathcal{A}$ is an *extension* of $\mathcal{A}^{\prime }$) if and only if the inclusion map $i$ (sending every element to itself) is an embedding from $\mathcal{A}^{\prime }$ to $\mathcal{A}$.

All the relationships already mentioned are established between structures of the same signature. We can as well define reductions and expansions between structures whose signatures are not the same. Given a many-sorted structure $\mathcal{A}$, a *reduct* $\mathcal{A}^{\prime }$ of $\mathcal{A}$ is obtained by simply removing some sorts, function or relation symbols from the signature of $\mathcal{A}$. If $\mathcal{A}^{\prime }$ is a reduct of $\mathcal{A}$, then we say that $\mathcal{A}$ is an *expansion* of $\mathcal{A}^{\prime}$.

### 1.5 Semantics

#### Denotation of Terms and Satisfaction of Formulas

Given a language and a structure, both of them sharing the same signature, each closed term of the language will denote an element in the structure and each atomic sentence is either true or false in the structure. Nevertheless, the scope of our definition is widened so that each term will receive a denotation and each formula a truth value. To achieve that, we define assignments[^note-5] from the set of variables to the domains of the structure, arguments and values should be of the same sort. For any individual $\mathbf{x}\in \mathbf{A}_{i}$ and variable $x^{i}$ of sort $i$, we use $s(\mathbf{x}/x^{i})$ to denote the assignment which is like assignment $s$ except that the value at $x^{i}$ has to be $\mathbf{x}$.

To define the important concept of “*truth* of a sentence *φ* in a structure $\mathcal{A}$” $(\mathcal{A}\models \varphi)$ we need to define previously the concept of *satisfaction* of a formula *φ* in $\mathcal{A}$ under assignment $s$ (noted as $\mathcal{A},s\models \varphi$), as well as the *denotation* of terms.

#### Denotation of terms

Let $\mathcal{A}$ be an *L*-structure (language and structure sharing signature $\Sigma$) and $s$ an assignment. $\mathcal{I}=\langle \mathcal{A},s\rangle$ is called an interpretation. The recursive definition of denotation $\mathcal{I}(\tau )$ of the term *τ* under the interpretation $\mathcal{I}$ is defined in the usual way, as in classical one-sorted first-order logic. For atomic and complex terms: $\mathcal{I}(x^{i})=s(x^{i})$, $\mathcal{I}(c)=c^{\mathcal{A}}$ and

$$\mathcal{I}(f\ \tau _{1}\ldots \tau _{n})=f^{\mathcal{A}}(\mathcal{I}(\tau _{1})\ldots \mathcal{I}(\tau _{n})).$$

It is easy to check that terms of a certain sort denote individuals of that sort.

**Definition (Tarski’s Truth).** The definition is nearly the same as in classical first-order logic, see the entry on classical logic.

For atomic formulas: $\mathcal{A}, s\models R\tau _{1}\ldots \tau _{n}$ if and only if

$$\langle \mathcal{I}(\tau _{1}),\ldots ,\mathcal{I}(\tau _{n})\rangle \in R^{\mathcal{A}},$$

and $\mathcal{A},s\models \tau _{1}\approx \tau _{2}$ if and only if both terms denote the same object in structure $\mathcal{A}$; namely, $\mathcal{I}(\tau _{1})=\mathcal{I}(\tau _{2})$.

In many-sorted logic the connectives are standard and, therefore, we use the classical definition of satisfaction for formulas built on them. For quantified formulas such as $\exists x^{i}\varphi$ the definition reads: $\mathcal{A},s\models \exists x^{i}\varphi$ if and only if there is an $\mathbf{x}\in \mathbf{A}_{i}$ such that $\mathcal{A},s(\mathbf{x}/x^{i})\models \varphi$.

#### Coincidence lemma

As in classical first-order logic, the coincidence lemma holds (see the entry on classical logic): For any formula *φ* and assignments $s_{1}$ and $s_{2}$: if $s_{1}$ and $s_{2}$ agree on the free variables in *φ*, then $\mathcal{A},s_{1}\models \varphi$ if and only if $\mathcal{A},s_{2}\models \varphi$.

For a formula $\varphi (x_{1},\ldots ,x_{n})$ whose free variables are in $\{ x_{1},\ldots ,x_{n}\}$ one can write

$$\mathcal{A}\models \varphi \left[ \mathbf{x}_{1},\ldots ,\mathbf{x}_{n}\right]$$

instead of

$$\mathcal{A},s\left( \mathbf{x}_{1}/x_{1},\ldots ,\mathbf{x}_{n}/x_{n}\right) \models \varphi.$$

By applying the coincidence lemma, we can get rid of assignments when dealing with sentences, and so we just write $\mathcal{A}\models \varphi$ (instead of $\mathcal{A},s\models \varphi$). In this case we usually say that $\mathcal{A}$ is a *model* of *φ*.

For a set of sentences *Γ* we say that $\mathcal{A}$ is a *model* of *Γ* (for short $\mathcal{A}\models \Gamma$), when $\mathcal{A}$ is a model of every sentence *γ* in *Γ*. Structures and language share signature.

The abstract schema of semantics could be seen in this way: we have a language $L$ and a class of mathematical structures, sharing a given signature $\Sigma$. Between these mathematical realities we have just built a bridge, the notion of *truth in a structure*. In one direction, we circulate from sentences to structures where these sentences are true; on the other direction, we go from structures to sentences which are true in these structures. In the first case, from a set of sentences *Γ* of signature $\Sigma$ we define $\Mod(\Gamma )$ as the class of structures of signature $\Sigma$ that are models of *Γ*. In the second, from a structure $\mathcal{A}$ of signature $\Sigma$ we define $\Th(\mathcal{A})$ (the theory of $\mathcal{A}$ ), the infinite set of sentences which are true at structure $\mathcal{A}$

$$\begin{align} \Mod(\Gamma ) &=\{ \Sigma \text{ structure }\mathcal{A}:\mathcal{A}\models \Gamma \} \\ \Th(\mathcal{A}) &= \{ \varphi \in \Sent(L):\mathcal{A}\models \varphi \} \end{align}$$

#### Elementary embedding

In the previous section, the relations between structures were defined without resorting to the many-sorted formal language. That is not the case for *elementary embedding*, another relationship between many-sorted structures of the same signature. An elementary embedding *π* between two Σ-structures $\mathcal{A}$ and $\mathcal{A}^{\prime }$ is an embedding satisfying:

$$ \mathcal{A\models \varphi \lbrack }\mathbf{x}_{1},\ldots, \mathbf{x}_{n}] \textrm{ if and only if } \mathcal{A}^{\prime }\mathcal{\models \varphi \lbrack }\pi (\mathbf{x}_{1}),\ldots \pi (\mathbf{x}_{n})] $$

for all Σ-formulas $\mathcal{\varphi (}x_{1},\ldots \mathbf{,}x_{n})$ and elements $\mathbf{x}_{1},\ldots ,\mathbf{x}_{n}$ in the domains of the structure, variables and elements with the same sorts.

Two structures $\mathcal{A}$ and $\mathcal{B}$ are *elementarily equivalent* if and only if their theories are the same, $\Th(\mathcal{A})=\Th(\mathcal{B})$.

#### Satisfiability, Validity, and Consequence

Concepts of *satisfiability*, *validity* and *consequence* are defined as in classical first-order logic. Given language $L$ of signature $\Sigma$ and a formula *φ* of $L$: *φ* is *satisfiable* if and only if there exists a Σ-structure $\mathcal{A}$ and assignment $s$ on it such that $\mathcal{A},s\models \varphi$ holds; *φ* is *valid* ($\models \varphi$) if and only if $\mathcal{A},s\models \varphi$ holds for all $\mathcal{A}$ of signature $\Sigma$ and any assignment $s$ on $\mathcal{A}$.

Given a language $L$ of a given signature $\Sigma$ we define the *consequence* relation in this way: $\Gamma \models \varphi$ if and only if for every structure $\mathcal{A}\ $(of signature $\Sigma$ ) and assignment $s$ such that $\mathcal{A},s\models \gamma$ for all $\gamma \in \Gamma$, we have that $\mathcal{A},s\models \varphi$.

In case *Γ* and *φ* were sentences, $\Gamma \models \varphi$ can be expressed in this way: $\Mod(\Gamma )\subseteq \Mod(\varphi )$.

**Theory:** Given a set of sentences *Γ* of a language $L$ we say that *Γ* *is a theory*[^note-6] if and only if it is closed under consequence; that is, for every $\varphi \in \Sent(L)$: If $\Gamma \models \varphi$ then $\varphi \in \Gamma$.

## 2. Calculus

### 2.1 Deductive Calculi

It is common in model theory to regard a logic as comprising at least three different things: a class of structures, a formal language to describe these structures, and a satisfaction relation that determines when a formula of the language is true with respect to a given structure. A deductive calculus might be added.

In fact, any calculus for one-sorted first-order logic can be easily extended to a many-sorted one; the only rules which need to be adapted are the ones dealing with quantifiers and substitution, as they have to take into consideration the variety of sorts admitted. In the entry classical logic the rules that need to be changed are: introduction and elimination of universal quantifier ($\forall \mathbf{I}$ and $\forall \mathbf{E}$), introduction and elimination of existential quantifier ($\exists \mathbf{I}$ and $\exists \mathbf{E}$) as well as the rules dealing with equality ($=\mathbf{I}$ and $=\mathbf{E}$).

The sequent calculus presented in Manzano (1996: 240–257)[^manzano-1996] is the many-sorted extension of the one in Ebbinghaus, Flum, and Thomas (1984). Hao Wang (1952: 106)[^wang-1952], one of the pioneering logicians working on many-sorted logic, already introduced an axiomatic calculus for this logic in his seminal work (see the [supplement on early history](logic-many-sorted.early-history.md) for more information).

As usual, to symbolize *derivability* of a formula from a set of formulas we write, $\Delta \vdash \varphi$. We will write the derivability sign $\vdash$ with a subscript when needed; namely, $\vdash _{\MSL}$. In any of these calculi the notion of proof is effective in the sense that there is a method by which whenever a finite sequence of sequents of formulas is given, it can always be effectively determined, whether it is a proof or not. Any of these calculi is *undecidable*, as there is not an algorithm to check if $\vdash \varphi$ or not. In fact, it could not be otherwise as the *satisfiability problem* (i.e., determining validity, or equivalently, testing for satisfiability of given formulas) for many-sorted logic is undecidable. So, we are in the same situation encountered in one-sorted first-order logic.

Of course, if a calculus is to be helpful it would never allow erroneous reasonings: it is not going to drive us from true hypotheses to false conclusions. It must be a *sound calculus*. Further, it is highly desirable that all the consequences of a set *Γ* of hypotheses could be derived from *Γ*. That is, we would like to have a *strongly complete calculus*. In our section 2.3 you will find the sketch of such a completeness proof.

#### Maximal consistency and the property of having witnesses

Also standard are the definitions of the syntactic concepts;[^note-7] namely those of *consistency*, *maximal consistency* and the property of *having witnesses*. In the present circumstance, a set of formulas *contains witnesses* if each existential formula comes with a witness ($\exists x^{i}\varphi \in \Delta$ implies $\varphi (t/x^{i})\in \Delta$ for a term $t$ of sort $i$). All three are properties of formulas and/or sets of formulas and in their definition we use derivability; i.e., the deductive calculus.

Consistency can be seen as the syntactic counterpart of satisfiability, in the same sense as $\vdash$ and $\models$ would correspond to one another. In fact, Henkin’s completeness proof basically consists in the construction of a model for each consistent set.

### 2.2 Completeness Notions

Proof and truth are defined by independent methods and it is not trivial, but necessary, to prove that they are extensionally the same. This is the content of the *completeness* theorem when this property is predicated of a *sound* calculus. There is another meaning of *completeness*, when it is predicate of a theory: A *theory Γ is complete* when for each sentence, either *φ* or $\lnot \varphi$ is a consequence of *Γ* (Manzano 1989 [1999: 118])[^manzano-1989]. *Strong completeness* of a calculus establishes its sufficiency for capturing the logical consequence; namely, whenever a sentence follows logically from a set of hypotheses, there is a proof of this sentence in the calculus, possibly using some of these hypotheses. In contrast, *weak completeness* says that we have proofs for all validities. In a complete[^note-8] logic, the expressive power of the language and its computational strength are well balanced. Thus the question about completeness is the question about the equilibrium of the basic components of a logic: its semantics and its logical calculus.

Sometimes, we merely say that a *logic is complete* and qualify this property as *abstract completeness*. In this case, we are only concerned with the computational characteristics of the set of logical truths (validities), all we need to know is that they are *recursively enumerable*.

Section 3 presents many-sorted logic as a unifier logic and we describe the three levels process of embedding into MSL as a path to completeness of the logic being studied: abstract completeness at the first level, strong completeness at the third.

### 2.3 Completeness of Many-sorted Logic

The completeness proof for a many-sorted calculus could be done by following the well known Henkin (1949)[^henkin-1949] strategy for first-order logic. The important issue is to be able to show that each consistent set of formulas has a model, and hence syntactic consistency and semantic satisfiability are equivalent (assuming *Soundness*). The proof is performed in basically two steps:

1. Every consistent set of formulas can be extended to a maximal consistent set with witnesses.
2. Once we have the maximal consistent set with witnesses, we use it as a guide to build the precise model described by formulas of this set. The reason being that a maximally consistent set is a very detailed description of a structure.

By doing that we prove:

**Henkin’s theorem:** If $\Gamma \subseteq \ Form(L)$ is consistent, then *Γ* has a countable model.[^note-9]

The completeness theorem

**Strong completeness:** If $\Gamma \models \varphi$ then $\Gamma \vdash \varphi$

follows easily from it.

To see that **Henkin’s theorem** implies **Strong completeness**, let us assume the antecedent, $\Gamma \models \varphi$. Therefore, $\Gamma \cup \{ \lnot \varphi \}$ is not satisfiable, it has no model. Using Henkin’s theorem we conclude that $\Gamma \cup \{ \lnot \varphi \}$ is contradictory and so $\Gamma \cup \{ \lnot \varphi \} \vdash \varphi$. The calculus rules allow us to get rid of $\lnot \varphi$ and infer $\Gamma \vdash \varphi$.

As corollaries of the previous results one gets:

**Weak completeness:** If $\models \varphi$ then $\vdash \varphi$.

**Compactness theorem:** *Γ* has a model iff every finite subset of it has a model.

**Löwenheim-Skolem:** If *Γ* has a model, then it has a countable model.

In Manzano (1996: 245–257)[^manzano-1996], the completeness theorem is proved in its strong sense and for all formulas, not only for sentences. Completeness and its corollaries are proven by following the path introduced by Ebbinghaus, Flum, and Thomas (1984).

*Is many-sorted logic a proper (or strict) extension of first-order logic?* Lindström (1969)[^lindström-1969] proves that first-order logic is characterizable as the strongest logic to possess simultaneously *Compactness* and *Löwenheim-Skolem* properties. Moreover, first-order logic is the strongest logic where *Löwenheim-Skolem* holds and its set of valid sentences is *recursively enumerable*. Therefore, many-sorted logic cannot be considered as a proper extension of first-order logic.

### 2.4 Automated Theorem Provers

Many-sorted logic provides a semantical concept of consequence as well as a deductive calculus to be used in the mathematical process of obtaining conclusions from hypotheses. Now the issue is to automate this reasoning process by building a computer program to conduct deductive inferences.

As we have already mentioned, soundness is the essential requirement of a calculus while completeness guarantees that all the semantical consequences can be established within the calculus and so the set of validities is *recursively enumerable*. The most relevant properties for automated deduction are *decidability* and *complexity*. A logic is decidable when there is an algorithm that answer *YES* or *NO* in a finite time to the question: *is the formula φ valid?* As validity and satisfiability are interdefinible ($\models \varphi$ iff $\lnot \varphi$ is not satisfiable) this problem is often called the *satisfiability* problem. Among the basic tasks a computer is asked for are *satisfiability* and *model checking*.

Propositional logic is decidable but first-order logic, many-sorted version included, is undecidable. However, in between propositional and first-order logic there are decidable logics, like *monadic predicate logic* (first-order logic whose predicates are all unary predicates), as well as decidable fragments[^note-10] of the undecidable logic. Moreover, among the decidable problems there are degrees of time-space complexity measuring time and memory register used by the computer.

Therefore, in a theorem prover for many-sorted calculus there is no guarantee of getting an answer to the question: *Does $\Gamma \models \varphi$?* However, there are efficient theorem provers able to solve the problem in many cases; for instance, when there are decidable fragments to implement. See the entries on automated reasoning and Church’s type theory. Section 4 of the entry on Church’s type theory is devoted to automation and provides information about machine-oriented proof calculi as well as early proof assistants. An excellent selection of theorem provers for Church’s type theory are presented. Among them are LEO-II and LEO-III, the latter is said to “cooperate with first-order reasoning tools using translations to many-sorted logic”.

Church’s simple type theory usually starts with base types “i” (individuals/entities) and “o” (Booleans) only and then iteratively defines all function types (such as “$\text{i} = > \text{o}$”, “$\text{i}=>\text{i}$”, “$\text{o}=>\text{o}$”, “$\text{i}=>(\text{i}=>\text{o})$”, etc.) starting from those. But in fact one can have arbitrary many base types $i_1$, $i_2$, $i_3$,…, $i_n$ and apply an analogous construction. These base types $i_1$, $i_2$, $i_3$,…, $i_n$ can be considered as sorts.

Our example from the **Book of Perfect Emptiness** can be formalized and checked using the LEO-II and LEO-III provers.

thf(sortForObjects, type, (object: \$tType)). thf(sortForTimes, type, (time: \$tType)). thf(constantDawn, type, (dawn: time)). thf(constantToday, type, (today: time)). thf(constantIsExistsAt, type,   (existsAt: object$>$time$>$\$o)). thf(constantPrecedesTo, type,   (precedesTo: time$>$time$>$\$o)). thf(axiom1, axiom, (![X:time]:   ((?[Y:object]: (existsAt @Y@X))   =$>$ (![Z:time]: ((precedesTo @Z@X)   =$>$ (?[V:object]: (existsAt @V@Z))))))). thf(axiom2, axiom,   (?[Y:object]: (existsAt @Y@today))). thf(axiom3, axiom,   (![Y:time]: (precedesTo @dawn@Y))). thf(conjecture1, conjecture,   (?[X:object]: (existsAt @X@dawn))).

## 3. Many-sorted Logic as a Unifying Framework

### 3.1 Translations

Currently, the proliferation of logical systems used in mathematics, computer science, philosophy, and linguistics makes the relationships between and their possible translations into one another a pressing issue. We saw above that many-sorted logic is a natural logic for reasoning about more than one sort of objects. In this section, we will present it as a unifying framework in which we may situate most of the many logics available to us. The general plan of translations into MSL is described with some details. Three possible levels of translations are settled and, at each level, when successfully reached, one completeness result is gained: abstract completeness at the first level, strong completeness at the third. Therefore, when a logic is translated into many-sorted logic we only need a unique deductive calculus, the many-sorted one, as well as an efficient theorem prover. In cases like *basic propositional modal logic*, where formulas could be translated into a decidable fragment of first-order logic with only two variables, the translation mechanism implies decidability for the modal logic. Moreover, some metaproperties of many-sorted logic can be transferred to the logic being translated.

Translations offer a better understanding of the logics being translated and could be used to compare two logics when they are transformed into theories of a common target logic, many-sorted first-order logic in our case. It is not a positive answer to the question *“The One Right Logic?”* (see the entry classical logic) as this question was not posed and it is not in the spirit of this translation into many-sorted logic. In *Modal Logic for Open Minds* (van Benthem 2010)[^benthem-2010] translations into first-order logic are extensively treated and there is a section entitled “Discussion: what good is a translation” (2010: 77) where Johan van Benthem analyzes the balance of expressive power and complexity and advocates for a tandem approach to answer the question *Does the translation ST mean that we can forget the modal language and just do first-order logic?*

#### Translations

Translations between logics have been formulated as an ambitious paradigm whose tools would serve for handling the existing multiplicity of logics. Some methodologies are proof-oriented, others are model-oriented, and finally some others are conceived in purely abstract suprastructural terms.

1. From a *proof-theoretical* point of view, the style of comparing logics will rest upon deductive calculi. The “labelled deductive systems” of Dov Gabbay (1994 and 1996) emerge.
2. From a *model-theoretical perspective*, one will presumably compare logics by defining relations between the structures those logics are attempting to describe, as in the correspondence theory of Johan van Benthem (1983, 1984a, and 2010).
3. From a *suprastructural* point of view, we define morphisms between categories. Among the abstract approaches to logic we highlight the “general logics” of José Meseguer (1989)[^meseguer-1989] as well as the “rewriting logic” of Narciso Martı́-Oliet and José Meseguer (1994). Da Silva, D’Ottaviano, and Sette (1999) gave a general definition of translation between logics according to which logics are characterized as sets with consequence relations; translations are hence consequence-relation preserving maps.

The paradigm of logical translation[^note-11] assumed in this entry belongs to the model-theoretical tradition mentioned in item 2 and the target logic is many-sorted logic.

As far as intensional logic is concerned, let us quote Johan van Benthem:

> Given any intensional logic, a complete possible-worlds semantics of the usual variety may be viewed as a faithful embedding of that logic into some suitably augmented many-sorted predicate logic (with quantification over possible worlds), perhaps provided with some simple auxiliary special-purpose theory for “accessibility”, “reversal”, and so on. Is predicate logic universal in this respect, in that every effectively axiomatized intensional logic can be semanticized in this way? (1984b: 995)

### 3.2 Correspondence Language for Basic Modal Language

Among the so called “non-classical logics”, modal logic occupies the first position as its history goes back to Aristotle, as well as Megarians, Stoics, and other Greek philosophers. Over the years it has been used to talk about necessity and possibility, time, and computer programs. See the entry on modal logic as well as Blackburn and van Benthem (2007) and van Benthem (2010)[^benthem-2010].

The features of modal logic most relevant to this entry on many-sorted logic are that truth can be qualified (or relativized) and that modal models include a universe of what are called “possible worlds”. The classical semantical concept of *truth in a model*, written as $\mathcal{A}\models \varphi$ is now replaced by *truth at a world $w$ in a model $\mathcal{A}$*, written as $\mathcal{A},w\models \varphi$.

Formulas in basic propositional modal language are built from *Atoms*, classical connectives and modal operators, $\square$ (box) and $\Diamond$ (diamond). Modal formulas are interpreted in *Kripke structures*

$$\mathcal{A}=\langle \mathbf{W},\mathbf{R},\langle P^{\mathcal{A}}\rangle _{P\in \Atom}\rangle$$

having a non-empty domain $\mathbf{W}$ of states or worlds, a binary accessibility relation $\mathbf{R}$ defined over it, and a collection of subsets of $\mathbf{W}$ for each atomic proposition symbol $P$. A modal formula *φ* is true at world $w$ in model $\mathcal{A}$ (*φ* is *satisfied* in $\mathcal{A}$ at world $w$) when the following inductive conditions apply:

$$\begin{align} \mathcal{A},w & \models P&& \text{ iff } w\in P^{\mathcal{A}}\\ \mathcal{A},w&\not\models \bot&& \text{ for all } w \\ \mathcal{A},w&\models \lnot \varphi&& \text{ iff not } \mathcal{A},w\models \varphi\\ \mathcal{A},w&\models \varphi \land \psi&& \text{ iff } \mathcal{A},w\models \varphi \text{ and } \mathcal{A},w\models \psi \\ \mathcal{A},w&\models \square \varphi&& \text{ iff for all } v \text{ such that } \langle w,v\rangle \in \mathbf{R}: \mathcal{A},v\models \varphi \end{align} $$

A formula *φ* is *globally true* in a model $\mathcal{A}$ if it is satisfied at all worlds in $\mathcal{A}$ ($\mathcal{A}\models \varphi$). A formula *φ* is *valid* if it is globally true at all models ($\models \varphi$). The set of validities in the whole class of Kripke models (when no restrictions are imposed to the accessibility relation) are the validities of the *basic modal logic*, also called *minimal modal logic* or *System* *K*.[^note-12]

Blackburn and van Benthem (2007: 5) note

> the *internal* character of modal satisfaction definition: *modal formulas talk about Kripke models from the inside*

as modal formulas are evaluated at certain points. The intuition is that the modal operator $\square$ is a kind of universal quantifier and modal structures are first-order relational structures with a binary relation and a collection of subsets of the universe. In a first-order language, to talk about these structures one needs a binary relation symbol, $S$, as well as a collection of unary relation symbols. This language is called *first-order correspondence language* because every basic modal formula corresponds to a first-order formula. The standard translation of a modal formula *φ* is a first-order formula with one free variable expressing the semantics of modal formulas:

$$\begin{align} \ST_{x}(P)& :=Px\\ \ST_{x}(\bot ) & :=x\not=x \\ \ST_{x}(\lnot \varphi )& :=\lnot \ST_{x}(\varphi )\\ \ST_{x}(\varphi \land \psi )& :=\ST_{x}(\varphi )\land \ST_{x}(\psi ) \\ \ST_{x}(\square \varphi )& :=\forall y(Sxy\rightarrow \lbrack y/x]\ST_{y}(\varphi ))\text{, where }y\text{ is a new variable.} \end{align} $$

The idea behind this definition is to express in the correspondence language the semantic interpretation of the modal formulas: both languages are talking about the same structures, as a Kripke structure can be viewed as a plain first-order relational structure. From this definition the following equivalence is obtained:

**Switch Lemma:** $\mathcal{A},w\models \varphi$ iff $\mathcal{A}\ \models \ST_{x}(\mathcal{\varphi )}[x:=w]$

(the assignment sends variable $x$ to world $w$)

From this lemma it is possible to derive *Compactness*, *Löwenheim-Skolem* and *Enumerability* theorems for the basic modal logic (Blackburn & van Benthem 2007: 11)[^blackburn-2007][^blackburn-2007-2] just using the corresponding properties of first-order logic.

The set of validities of *basic modal logic* is not only recursively enumerable (as the enumerability theorem proves) but the satisfiability problem is also decidable. *We wonder, what is the gain in translating a decidable logic into an undecidable one? Are we loosing decidability?* The answer is that we don’t loose decidability; in fact, one can use translations to prove decidability for *basic modal logic*.

Concerning translation of *basic modal logic* into first-order correspondence language, there are at least two results to highlight:

- The first relevant result is that *basic propositional modal logic* can be translated into the two variable fragment[^note-13] of first-order logic (formulas of first-order logic where only two variables are used) and the satisfiability problem for the two variable fragment is decidable.

- The second relevant result is the *Modal Characterization Theorem*[^note-14] establishing, for any first-order formula with a free variable, the equivalence between being equivalent to a modal formula and being invariant under bisimulation (see van Benthem 2010: 26–27 for a definition)[^benthem-2010]. Bisimulation is a useful result as it can be employed to make a model $\mathcal{A}$ as small as possible, by *bisimulation constraction*, as well as to make bigger models.

However, these results apply to *basic modal logic*; in that logic we are talking about *satisfiability* as meaning “satisfiable on some model”, no restrictions (like transitivity) are imposed on the accessibility relation. And for any modal logic other than *system* *K* we are looking for models with additional properties. It is true that similar method can be applied with other propositional systems when the relevant properties can be expressed by first-order formulas with only two variables. Nevertheless, transitivity is a clear counter case.

In section 5.2, a variety of modal systems are treated (including *S*4, whose accessibility relation is reflexive and transitive) and several metatheorems are proved for them, by using the MSL reservoir. The translation is defined into a many-sorted first-order logic with a second-order flavor, as the many-sorted structures used in that section contain the relevant categories of mathematical sets (and relations) definable in the modal logic being translated.

In the following sections we present translations into many-sorted logic as the path to completeness in three stages.[^note-15]

### 3.3 General Plan

The general plan is as follows: The signature of the logic being studied (call it $\XL$) is transformed into a many-sorted signature, the expressions of the logic $\XL$ are translated into $\MSL^{\XL}$ (a many-sorted language suited for $\XL$) and the structures of the logic $\XL$ are converted into many-sorted structures. Thus, we need to define a recursive function $\Trans$ to do the translation and a direct conversion of structures, $\Conv_{1}.$

With the direct conversion of structures we want to obtain as a result the equivalence of validity in the original structures for $\XL$, call them simply $\Str(\XL)$, with validity of a certain class of many-sorted formulas (the translations) in the class $\mathfrak{S}^{\ast}$ of converted structures (where $\mathfrak{S}^{\ast}=\Conv_{1}(\Str(\XL))$).

Next question to ask is whether or not $\mathfrak{S}^{\ast}$ can be replaced by the models of a set $\Delta$ of many-sorted formulas. Thus, the key to both definitions, $\Trans$ and $\Conv_{1}$, is to simplify the proof of the semantic equivalence, and in this respect the relevance of the results obtained strongly depends on the possibility of axiomatizing $\mathfrak{S}^{\ast}$. In case you get such a recursive set of formulas of $\MSL^{\XL}$, say $\Delta$, (or at least such that $\mathfrak{S}^{\ast}\subseteq \Mod(\Delta )$) we should prove that validity in $\XL$ is equivalent to consequence from $\Delta$ in $\MSL^{\XL}$.

In case you get the set $\Delta$, a reverse conversion of structures, $\Conv_{2}$, should be defined. And so, from many-sorted models of $\Delta$ we get structures in $\Str(\XL)$. Our goal in defining it is to prove that starting from a many-sorted structure $\mathcal{B}$ (a model of $\Delta$), a formula *φ* of $\XL$ is true in $\Conv_{2}(\mathcal{B)}$ if and only if the universal closure of its translation is true at $\mathcal{B}$.

### 3.4 Level One: Representation Theorems

The logic being studied is $\XL$ and we define a recursive function $\Trans$ to do translations into $\MSL^{\XL}$ as well as a direct conversion of structures, $\Conv_{1}$. Our first goal is to state and prove the following:

**Theorem 1:** For every sentence *φ* of the $\XL$ logic,

$$\models _{\Str(\XL)}\varphi \text{ in } \XL \text{ iff } \models _{\mathfrak{S}^{\ast}}\forall \Trans(\varphi )\text{ in }\MSL$$

where $\forall \Trans(\varphi )$ is the universal closure of $\Trans(\varphi )$ and $\mathfrak{S}^{\ast}=\Conv_{1}\Str(\XL)$.

We wonder, *can validity in the class of structures $\mathfrak{S}^{\ast}$ be replaced by consequence from a set $\Delta$ of many-sorted formulas?* The next goal is to find such a $\Delta$, at least a set satisfying $\mathfrak{S}^{\ast}\subseteq \Mod(\Delta )$. To finish level one, one needs to prove a *Representation theorem*; namely, a statement of the following form:

**Representation theorem:** There is a recursive set of many-sorted sentences $\Delta$, with $\mathfrak{S}^{\ast}\subseteq \Mod(\Delta )$, and such that

$$\models _{\Str(\XL)}\varphi \text{ in } \XL \text{ iff } \Delta \models _{\Str(\MSL^{\XL})}\forall \Trans(\varphi )\text{ in }\MSL$$

for every sentence *φ* of the $\XL$ logic.

From Representation theorem it follows *Enumerability* for the logic $\XL$. Namely, the set of validities of $\XL$ is recursively enumerable. Therefore, $\XL$ is complete in an abstract sense.

**Remark:** So, we learn that a calculus for $\XL$ is a natural demand, but we also learn that in MSL we can simulate such a calculus and then we could use a theorem prover for MSL.

### 3.5 Level Two: the Main Theorem

When the $\XL$ logic under scrutiny has a concept of logical consequence, we may try to prove the *Main theorem*; that is, that consequence in $\XL$ ($\Pi \models _{\Str(\XL)}\varphi$) is equivalent to consequence of translations in MSL, *modulo* the theory $\Delta$. To prove the main theorem, the reverse conversion of structures, $\Conv_{2}$, should be used. Our goal in defining it is to prove the following:

**Lemma 2:** For any $\varphi \in \Sent(\XL)$ and $\mathcal{B} \in \Mod(\Delta )$

$$\Conv_{2}(\mathcal{B)}\models \varphi \text{ iff } \mathcal{B}\models \forall \Trans(\varphi )$$

where $\forall \Trans(\varphi )$ is the universal closure of $\Trans(\varphi )$.

From the previous results, our Main Theorem follows:

**Main Theorem:** There is a recursive set $\Delta \subseteq \Sent(L^{\ast})$ with $\mathfrak{S}^{\ast}\subseteq \Mod(\Delta )$, such that

$$\Pi \models_{\Str(\XL)}\varphi \text{ iff } \Trans(\Pi )\cup \Delta \models _{\Str(\MXL^{\ast})}\Trans(\varphi )$$

for all $\Pi \cup \{\varphi \}\subseteq \Sent(\XL)$.

**Corollary:** *Compactness* and *Löwenheim-Skolem* for $\XL$.

**Remark:** We already have *Enumerability*. Now, from *Main Theorem* as well *Compactness* and *Löwenheim-Skolem* for $\MSL$, we easily obtain *Compactness* and *Löwenheim-Skolem* for $\XL$. Therefore, the logic under investigation could have a strongly complete calculus. You can either define it or use the many-sorted one.

### 3.6 Level Three: Deductive Correspondence

When the $\XL$ logic also comes with a deductive calculus, we can try to use the machinery of correspondence to prove, if possible, *Soundness* and *Completeness* for $\XL$. In order to prove these theorems, one needs to prove a *Theorem of deductive correspondence* between the $\XL$ calculus and the many-sorted one, modulo $\Delta$. So, the next goal is to prove:

**Theorem of deductive correspondence:** Let $\Delta$ be defined as in the Main Theorem, then:

$$\Trans(\Pi )\cup \Delta \vdash _{\MSL}\Trans(\varphi )\text{ if and only if } \Pi \vdash _{\XL}\varphi .$$

Since we already have the *Main theorem* (\*), plus *Completeness* and *Soundness* for MSL (\*\*), once we get this *Theorem of deductive correspondence* (\*\*\*) the picture below gave us *Soundness and Strong Completeness* of $\XL$:

$$ \begin{align} \Trans(\Pi )\cup \Delta \models_{\Str(\MSL)} \Trans(\varphi ) & \Longleftrightarrow \Pi \models _{\Str(\XL)}\varphi \tag{*} \\ \Updownarrow \qquad\qquad\qquad \tag{**} \\ \Trans(\Pi )\cup \Delta \vdash_{\MSL} \Trans(\varphi ) & \Longleftrightarrow \Pi \vdash _{\XL}\varphi \tag{***} \\ \end{align} $$

**Corollary:** *Soundness and Strong Completeness* of $\XL$:

$$\Pi \models _{\Str(\XL)}\varphi \text{ if and only if }\Pi \vdash _{\XL}\varphi$$

**Remark:** We have reached the end of the road to completeness, but it is important to stress that we are using the already proven completeness results of MSL to prove strong completeness for $\XL.$

## 4. Second-order Logic as Many-sorted Logic

### 4.1 Second-order Logic

Second-order logic, SOL, is a very expressive formal language which differs from FOL (one-sorted first-order logic) in the following respects: (1) alphabet, (2) standard and non-standard semantics and (3) overwhelming expressive power with standard semantics. See the entry on second-order and higher-order logic as well as the entry on Church’s type theory.

The alphabet of second-order logic is obtained by including the first-order one-sorted variables and adding relation variables that can be quantified. As a result, in addition to the formula $\forall x\varphi$ saying *“for all individuals φ holds”*, we have formulas $\forall X\varphi$, $\forall X^{2}\varphi$, etc. saying *“for all properties, φ holds”*, *“for all binary relations, φ holds”*, etc.

From the semantic point of view, to give meaning to the new variables we need new universes whose elements are sets and relations over the universe of individuals, say $\mathbf{A}.$ In the so-called *standard semantics*, a set variable ranges over the power set of the individual’s universe, $\wp (\mathbf{A})$, and a *n*-ary relation variable ranges over the power set of the *n*-ary Cartesian product of the individual’s universe, $\wp (\mathbf{A}^{n})$. To put an example of the overwhelming expressive power of second order logic with standard semantics, *Arithmetical induction* can be expressed

$$\forall X(Xc\land \forall x(Xx\rightarrow X\sigma x)\rightarrow \forall xXx)$$

and second-order Peano arithmetic ($\PA^{2}$) becomes categorical, that is, any two models of $\PA^{2}$ are isomorphic. However, we pay a high price for the expressive power, we sacrifice the logic: *Compactness* fails, *Löwenheim-Skolem* fails and *Completeness* fails (both strong and weak).

Of course, the latter results are obtained with standard semantics. In Henkin 1950 he announces that the incompleteness problem is solvable if *“a wider class of models”* (non-standard models) is allowed. Therefore, he introduces: standard structures, general structures and frames. The classes of these structures are ordered by set inclusion

$$\mathfrak{SS}\subseteq \mathfrak{GS}\subseteq \mathfrak{F}$$

and, accordingly, the sets of validities in each class obey the reverse order[^note-16]

$$\Val_{\mathfrak{F}}\subseteq \Val_{\mathfrak{GS}}\subseteq \Val_{\mathfrak{SS}}$$

In the *semantics of frames*, both sets and relation variables are allowed to range over universes which are subsets of standard universes. Somehow, this condition alone does not guarantee that we have enough sets and relations to deal with the second order capability. We would like to include in the universes all the definable ones in our formal language. This is a rather natural demand imposed to the *general models* (*Henkin models*) to obtain completeness.

In fact, with the semantics of frames, the set of validities coincides with the set of sentences derivable in a second-order calculus which is just an extension of the first-order one obtained by adding rules for the new quantifiers. This many-sorted calculus was isolated by Henkin (1953)[^henkin-1953] in a paper where he introduced the *Comprehension Schema*

$$\exists X^{n}\forall x_{1}\ldots x_{n}(X^{n}x_{1}\ldots x_{n}\leftrightarrow \varphi )$$

as a way of getting rid of the complex substitution rule of Church (1956)[^church-1956]. It is clear that, in case the only requirement you impose to the universes of the second-order structure is to be subsets of standard universes, there is no guarantee that they are models of *Comprehension*. That is why we need the general structures to obey extra rules, universes have to be closed under definability. With general structures the set of validities coincides with the set of sentences derivable in the second-order calculus. So, we go back to the situation encountered in first-order logic as you recover: *Compactness*, *Löwenheim-Skolem* and *Completeness*.

Obviously, SOL with general semantics is less expressive than with standard semantics. For instance, $\forall X(Xx\leftrightarrow Xy)$ is no longer a definition of genuine identity between individuals. And so we take it as primitive and require equality $\approx$ to be interpreted as identity. For higher types, *Axiom of Extensionality*

$$\forall X^{n}Y^{n}(X^{n}\approx X^{n}\leftrightarrow \forall x_{1}\ldots x_{n}(X^{n}x_{1}\ldots x_{n}\leftrightarrow X^{n}x_{1}\ldots x_{n}))$$

is added.

*What is the conclusion of these results?* As you know, a logic is like a balance scale: you have expressive power in one pan and computability power in the other. In case you wanted to retain logical properties, you had to change the semantics and lose some expressive power, you cannot have both at a maximum, they are “optimal impossible”. One can express the same idea in a more technical way by resorting to Lindström’s results (Lindström 1969)[^lindström-1969] mentioned in section 2.3.

For more information on second-order logic, see the entry on second-order and higher-order logic, as well as Church 1956 and Enderton 1972. Very recommended is Henkin 1996 as well as some of the papers in *The Life and Work of Leon Henkin* (see Manzano, Sain, & Alonso 2014)[^manzano-2014][^manzano-2014-2], in particular: “Changing a Semantics, Opportunism or courage?” (Andréka, van Benthem, Bezhanishvili and Németi 2014)[^andréka-2014], “Henkin on Completeness” (Manzano 2014b)[^manzano-2014b], and “April the 19th” (Manzano 2014a)[^manzano-2014a].

### 4.2 Translation of Formulas and Conversion of Structures

Following the instructions in the corresponding section (§3.4 or §3.5), we define a syntactical translation from SOL to $\MSL^{\SOL}$ as well as two conversions of structures, direct and reverse.

First of all, we realize that second-order structures are in fact many-sorted with certain peculiarities: in most cases they are what we called *strict*, because the intersection between any two different universes is empty, but all of them are related, as they are defined over the universe of individuals. Moreover, in the general structures the universes obey certain rules, like being models of *Extensionality* and *Comprehension*.

Let $L$ be a second-order language with a set $\OperSym$ of operation symbols. If we compare expressions in SOL with expressions in a many-sorted logic, we realize that $X^{n}x_{1}\ldots x_{n}$ is not a formula of many-sorted logic since it is only a string of variables. What we do is to introduce a new many-sorted language, $\MSL^{\SOL}$, where we retain all the symbols in $\OperSym$ but the signature is now enlarged with new membership relation symbols, $\epsilon _{n}$, whose interpretations are going to be a kind of *membership* relations. The many-sorted signature $\Sigma ^{\SOL}$ includes a set $\Sorts$ whose elements are the types in the SOL structure; namely, 1, and $\langle\underbrace{ 1,\ldots ,1}_n ,0\rangle$ for all $n\geq 1$.[^note-17]

Therefore, the *syntactical translation* from SOL to this $\MSL^{\SOL}$ leaves every formula the same except the atomic formulas of the kind mentioned above; i.e.:

$$\Trans^{\SOL}(X^{n}x_{1}\ldots x_{n}):=\epsilon _{n}x_{1}\ldots x_{n}X^{n}$$

*Direct conversion of structures (from $\SOL$ to $\MSL^{\SOL}$):* Let us define $\Conv_{1}$ as a function which takes any structure $\mathcal{A}\in\Str(\SOL)$ and returns a structure $\mathcal{A}^{\ast}\in \Str(\MSL^{\SOL})$. These structures are basically the same, with the only exception of membership relations we now add. This membership relation symbol of the many-sorted language, $\epsilon _{n}$, is interpreted as genuine membership,

$$\epsilon _{n}^{\mathcal{A}^{\ast}}=\{\langle \mathbf{x}_{1}\mathbf{,\ldots ,x}_{n}\mathbf{,X}^{n}\rangle \in \mathbf{A}^{n}\times \mathbf{A}_{n}:\mathbf{\langle x}_{1}\mathbf{,\ldots ,x}_{n}\mathbf{\rangle \in X}^{n}\}$$

(where $\mathbf{A}$ is the universe of individuals, of sort 1, and $\mathbf{A}_{n}$ is the universe of *n*-ary relations, of sort $\langle\underbrace{ 1,\ldots ,1}_n ,0\rangle$, and $\mathbf{A}^{n}$ is the *n*-ary Cartesian product of $\mathbf{A}$)

It is easy to prove the following result.

**Proposition:** For every sentence *φ* of SOL:

$$\models _{\mathcal{G}.\mathcal{S}}\varphi \text{ in }\SOL\text{ if and only if }\models _{\mathfrak{S}^{\ast}}\Trans^{\SOL}(\varphi )\text{ in }\MSL^{\SOL}$$

(where $\models _{\mathcal{G}.\mathcal{S}}\varphi$ means validity with general structures and $\mathfrak{S}^{\ast}=\Conv_{1}(\Str(\SOL))$)

*Now we ask, can we axiomatize $\mathfrak{S}^{\ast}$?* and the answer is *YES*. The structures we want to work with are $\MSL^{\SOL}$ models of *Extensionality* and *Comprehension* with *Disjoint universes*. Thus, let $\Delta$ be:

$$\begin{align} \Ext^{(n)} & :=\forall X^{n}Y^{n}(\forall x_{1}\ldots x_{n}(\epsilon _{n}x_{1}\ldots x_{n}X^{n}\leftrightarrow \epsilon _{n}x_{1}\ldots x_{n}Y^{n})\\ & \qquad\qquad \rightarrow X^{n}\approx Y^{n}) \\ \forall \Comph_{\varphi }^{(n)} & :=\forall \exists X^{n}\forall x_{1}\ldots x_{n}(\epsilon _{n}x_{1}\ldots x_{n}X^{n}\leftrightarrow \varphi ) \\ \Disj_{n,m} &:=\lnot \exists X^{n}Y^{m}X^{n}\approx Y^{m}\;(\text{for }n\neq m) \\ \end{align}$$

*Reverse conversion of structures (from $\MSL^{\SOL}$ to $\SOL$):* The reverse conversion of structures is done in four steps.[^note-18]

1. The structures we want to work with are $\MSL^{\SOL}$ models of extensionality and comprehension with disjoint universes. So, they have to be models of $\Delta$. In such a model the universes of sort $\langle 1,\ldots ,1,0\rangle$ are not necessarily subsets of $\wp (\mathbf{A}_{1}^{n}).$ However, $\mathbf{A}_{1}$ and $\mathbf{A}_{\langle 1,\ldots ,1,0\rangle }$ are related by $\epsilon _{n}^{\mathcal{A}}$, but this relation doesn’t need to be “genuine” membership.
2. From a many-sorted structure $\mathcal{A}$ of signature $\Sigma ^{\SOL}$ which is a model of $\Delta$, we pass to another many-sorted structure $\mathcal{B}$ of the same signature but where universes of sort $\langle 1,\ldots ,1,0\rangle$ are now subsets of $\wp (\mathbf{B}_{1}^{n})$ and $\epsilon _{n}^{\mathcal{B}}$ is *genuine* membership. The new many-sorted structure $\mathcal{B}$ is obtained by defining a function $$H:\Mod(\Delta )\rightarrow \Conv_{1}(\Str(\SOL))$$ that follows the information given in $\epsilon _{n}^{\mathcal{A}}$ to build $\mathbf{B}_{\langle 1,\ldots ,1,0\rangle }$, thus $\mathcal{B}=H(\mathcal{A})$. The new structure is basically a general second order structure with the genuine membership relation.[^note-19]
3. It is easy to see that the new structure $\mathcal{B}$ is isomorphic to the original $\mathcal{A}$, so $\mathcal{A}\approxeq \mathcal{B}$.
4. From a many-sorted structure $\mathcal{B}\in \Conv_{1}(\Str(\SOL))$ of the kind mentioned above, we define a SOL structure by an easy make-up transformation; namely, erasing the membership relations and adapting the signature to a second order one. This is just to reverse the transformation done in $\Conv_{1}$.

The final result of the reverse conversion is just $\Conv_{1}^{-1}(H(\mathcal{A}))$ and so we define $\Conv_{2}$ accordingly.

**Definition:** $\Conv_{2}=\Conv_{1}^{-1}\circ H$.

With all these definitions at hand, we now prove:

**Proposition:** for every many-sorted structure $\mathcal{C}\in \Mod(\Delta )$ there is a SOL-structure $\Conv_{2}(\mathcal{C})\in \Str(\SOL)$ such that

$\Conv_{2}(\mathcal{C})$ is a model of *φ* if and only if $\mathcal{C}$ is a model of $\Trans^{\SOL}(\varphi)$

for all sentences of SOL.

### 4.3 Semantic Theorems Relating SOL and MSL

By applying the previous results, it is easy to prove the following semantic theorems:

**Representation theorem:** For every sentence *φ* of SOL: $\models _{\mathfrak{G.S}}\varphi$ in SOL iff

$$\Delta \models_{\MSL} \Trans^{\SOL}(\varphi )$$

in $\MSL^{\SOL}.$

**Main theorem:** $\Pi \models _{\mathfrak{G.S}}\varphi$ in SOL if and only if

$$\Trans^{\SOL}(\Pi )\cup \Delta \models _{\MSL} \Trans(\varphi )$$

in $\MSL^{\SOL}$.

As explained in section 3.5, by using **Representation** and **Main** theorems some important metatheorems of MSL can now be transferred to SOL.

**Theorem:** SOL with general semantics has the following properties: *Enumerability*, *Compactness* and *Löwenheim-Skolem*.

**Remark:** The enumerability and compactness theorems taken together tell us that the logic under investigation could have a strongly complete calculus. In fact, we could use the many-sorted theory $\Delta$ to derive SOL theorems in the many-sorted calculus.

However, in case we already had a calculus for SOL we can use the machinery of translations to prove its *Soundness* and *Completeness.*

### 4.4 Soundness and Completeness for SOL

We just follow the strategy presented on level three (in section 3.6) of our general plan to prove *Soundness* and *Completeness* for SOL calculus. What needs to be proven is the following theorem.

**Theorem of deductive correspondence**: $\Pi \vdash _{\SOL}\varphi$ in second order calculus iff

$$\Trans^{\SOL}(\Pi )\cup \Delta \vdash _{\MSL} \Trans^{\SOL}\mathbf{(}\varphi \mathbf{)}$$

in many-sorted calculus, MSL.

According to the general plan, from the **Main theorem**, the *Deductive correspondence* and *Soundness* and *Strong Completeness* of MSL, we get *Completeness* and *Soundness* for SOL with general semantics.

**Strong Completeness and Soundness**: $\Pi \models _{\mathcal{G}. \mathcal{S}}\varphi$ iff $\Pi \vdash _{\SOL}\varphi$ for all $\Pi \cup \{\varphi \}\subseteq \Sent(L_{2}).$

## 5. Translations Into Many-sorted Logic with a Second-order Appearance

### 5.1 General Plan

As mentioned already, in Henkin 1953 a new calculus for second order logic was defined by eliminating some *Substitution Rules* from the calculus presented in Church 1956[^note-20] and introducing *Comprehension Schema*. In this paper, Henkin defines two calculi $F^{\ast}$ and $F^{\ast \ast}$ (basically, calculi MSL and SOL): the first one is obtained from a first-order calculus by adding rules for the new quantifiers, while the second is a proper second-order calculus. Both calculi are incomplete with standard semantics. Henkin mentioned that we can obtain a completeness result for the $F^{\ast}$ calculus with the *frame semantics*. In fact, we have already seen completeness for MSL and that the second-order calculus is complete with the *general semantics*.

There is another interesting idea, appearing explicitly in the 1953 paper, which is also useful. The idea is: If we weaken comprehension, we obtain a calculus between $F^{\ast}$ and $F^{\ast \ast}$. And it is easy to find a semantics for the logic thus defined. Of course, this class of structures is placed between $\mathfrak{F}$ and $\mathfrak{GS}$. The new logic, call it $\XL$, will also be complete; the main reason being that this class of models is again axiomatizable.

In what follows, this idea is exploited in several propositional modal logics as well as in propositional dynamic logic with *Kripke semantics* (see the entry on modal logic as well as the entry on propositional dynamic logic).

The second-order appearance mentioned in the title is as follows: when defining the conversion of structures into MSL we will add new universes containing all the categories of mathematical objects you can talk about in PML (or PDL); therefore, we add all sets and relations defined in these logics with their respective formulas and programs. And so, we are somehow shifting to SOL structures. We can add as well membership relation symbols to the language and membership relations to the structures, as we did in the conversion of SOL into MSL; we will end up in MSL but the inspiration is SOL.

### 5.2 Propositional Modal Logics as Many-sorted Logic

The first thing we do is to set a many-sorted language $\MSL^{\PML}$ containing: unary relation symbols for each atomic proposition, $P\in \Atom$, a binary relation symbol $S$ to represent the accessibility relation, a membership sign, and equality for individuals and sets. $\MSL^{\PML}$ contains individual variables as well as variables for sets. The translation is standard (as in section 3.2): we express in the target logic $\MSL^{\PML}$ the semantical interpretation of the formulas being translated.[^note-21] In particular,

$$\begin{align} \Trans(P)[u]& :=Pu \\ \Trans(\square \varphi )[u]& :=\forall v(Suv\rightarrow \Trans(\varphi )[v]) \end{align}$$

The many-sorted structures we shall use are obtained from the modal structures by adding a universe containing sets of states or worlds. Given a Kripke structure

$$\mathcal{A}=\langle \mathbf{W},\mathbf{R},\langle P^{\mathcal{A}}\rangle _{P\in \Atom}\rangle$$

we say that $\mathcal{AG}$ is a general structure built on $\mathcal{A}$ if and only if

$$\mathcal{AG}=\langle \mathbf{W},\mathbf{W}^{\prime },\mathbf{R},\epsilon _{1}^{\mathcal{A}},\langle P^{\mathcal{A}}\rangle _{P\in \Atom}\rangle$$

where $\Def \subseteq \mathbf{W}^{\prime }\subseteq \wp (\mathbf{W})$. The sets $\Def$ and $\mathbf{W}^{\prime }$ contain all the members in the family $\langle P^{\mathcal{A}}\rangle _{P\in \Atom}$ and are closed under several operations.[^note-22] It can be proved that the set of worlds where a modal formula *φ* is true in a modal structure $\mathcal{A}$ is the same set its translation defines in the general structure $\mathcal{AG}$ built on $\mathcal{A}$.

Let us use $\mathfrak{G}$ to refer to the class of all general structures built on modal structures defined as above, our converted structures. It is not difficult to prove that validity of *φ* in PML is equivalent to validity of the universal closure of the translation of the formula in the class $\mathfrak{G}$.

#### Level one for Modal Logic *K*

To finish the level one of the translation method, we need to axiomatize $\mathfrak{G}$. *Is that possible?* The answer is positive for the *minimal logic* *K* (*basic modal logic*) as we can define a theory $\Delta _{K}$ with the *Comprehension Axiom*

$$\forall \exists X\,\forall u(\varepsilon _{1}uX\leftrightarrow \varphi )\text{ }$$

working mainly on many-sorted formulas *φ* obtained by translations of modal formulas. As we wanted a second-order appearance, *Extensionality Axiom* is added to $\Delta _{K}$. As a result, we obtain a *Representation Theorem* for the *minimal modal logic*, *K*:

$$\models \varphi \text{ in } \PML \Longleftrightarrow \Delta _{K}\models \forall u\Trans(\varphi )[u]\text{ in }\MSL$$

(in logic *K* the whole class of Kripke structures are used, no conditions are imposed on the accessibility relation)

As explained in section 3.4, from the previous theorem, *Enumerability* theorem for modal logic *K* is achieved. In fact, we already know much more, as we mentioned in section 3.2 that the set of validities in system *K* is decidable.

#### Level one for Modal Logic *S*4

In case we wanted a similar outcome for another modal logic, say *S*4, the set $\Delta _{K}$ can be extended to a set $\Delta _{S4}$ including as axioms the many-sorted abstract conditions for axioms $T$ and 4 (i.e., formulas $\MS(T)\ $and $\MS(4)$[^note-23]). In fact, we can prove that the first-order axioms for reflexivity and transitivity are equivalent to these many-sorted translated sentences.

$$\begin{align} \Delta _{K} \vdash \MS(T) &\leftrightarrow \textrm{Reflexivity} \\ \Delta _{K} \vdash \MS(4) &\leftrightarrow \textrm{Transitivity} \end{align}$$

The *Representation Theorem* for *S*4 is easily obtained

$\models _{\mathfrak{D}}\varphi$ in $\PML \Longleftrightarrow \Delta _{S4}\models \forall u\Trans(\varphi )[u]$ in $\MSL$

($\mathfrak{D}$ is the class of reflexive and transitive Kripke models)

These results are relevant when we proceed further to prove the *Main Theorem*.[^note-24] From this theorem we get for free *Compactness* and *Löwenheim-Skolem* for *K* and *S*4.

#### Level three for Modal Logics *K* and *S*4

In case we wanted to prove that modal calculi for *K* and *S*4 (see the entry on modal logic) are complete by using the completeness of MSL, *Deductive Correspondence* between the modal logic concerned and its many-sorted counterpart have to be proved. Proving deductive correspondence from propositional modal logic to many-sorted logic is easy

$$\begin{align} \Pi \vdash _{K}\varphi & \Rightarrow \Trans(\Pi )\cup \Delta _{K}\vdash \Trans(\varphi ) \\ \Pi \vdash _{S4}\varphi & \Rightarrow \Trans(\Pi )\cup \Delta _{S4}\vdash \Trans(\varphi ) \end{align} $$

as translations of modal axioms of system *K* are theorems of the MSL logic, while translations of $T$ and 4 are theorems of $\Delta _{S4}$. To prove the reverse deductive correspondence between MSL and PML the canonical model[^note-25] $\mathcal{B}_{K}$ (or $\mathcal{B}_{S4}$) could be used to build the general structure $\mathcal{B}_{K}\mathfrak{G}$ (or $\mathcal{B}_{S4}\mathfrak{G}$). The final step is reached by using the general structure built onto the canonical model. It is easy to prove that the translation of a modal formula *φ* is true at a world of this structure if and only if formula *φ* belongs to this world.

Therefore,

$$\begin{align} \mathcal{B}_{K}\mathfrak{G}\models \forall u(\Trans(\varphi )[u]) & \Rightarrow \vdash _{K}\varphi \\ \mathcal{B}_{S4}\mathfrak{G}\models \forall u(\Trans(\varphi )[u]) & \Rightarrow \vdash _{S4}\varphi \end{align} $$

The deductive correspondence between a modal logic and its many-sorted counterpart is achieved

$$\begin{align} \Pi \vdash _{K}\varphi & \Longleftrightarrow \Trans(\Pi )\cup \Delta _{K}\vdash \Trans(\varphi ) \\ \Pi \vdash _{S4}\varphi & \Longleftrightarrow \Trans(\Pi )\cup \Delta _{S4}\vdash \Trans(\varphi ) \end{align} $$

and the soundness and completeness of the modal logics under investigation is reached by following the strategy explained in section 3.6.

#### Propositional Dynamic Logic as Many-sorted Logic

A similar method can be applied in Propositional Dynamic Logic (PDL). PDL is a modal logic initially designed to talk about states and computer programs, it has a complete calculus whose axioms include the usual ones in modal logic *K* as well as other axioms describing the composition of programs (see the entry on propositional dynamic logic). Among them, it is worth highlighting Axiom 5. This axiom is also known as “induction axiom” and it is the responsible for one of the characteristic of PDL, its *uncompactness*. For this reason, the calculus of PDL is sound and complete but only in the weak sense.

The translation of formulas and programs into many-sorted logic is the expected one:[^note-26] we express in the target logic $\MSL^{\PDL}$ the semantical interpretation of the formulas and programs being translated.

For the conversion of structures, we follow a procedure similar to the one used in PML: we extend the Kripke model $\mathcal{A}$ to a general structure $\mathcal{AE}$ built on $\mathcal{A}$

$$\mathcal{AE}=\langle \mathbf{W},\mathbf{W}^{\prime },\mathbf{W}^{\prime \prime },\mathbf{R},\epsilon _{1}^{\mathcal{A}},\epsilon _{2}^{\mathcal{A}},\langle P^{\mathcal{A}}\rangle _{P\in \Atom}\rangle$$

The novelty is that now we have another domain $\mathbf{W}^{\prime \prime }$ to include the binary relations defined by programs. Using these structures, one can prove that validity of a dynamic formula is equivalent to the validity of the universal closure of its translation in the class $\mathcal{E}$ of all many sorted structures obtained in this way. The representation theorem is also available, once we define the theory $\Delta _{\PDL}$. This theory includes as axioms the *many-sorted abstract conditions* for the PDL axioms, *Extensionality* (both for sets and relations) as well as *Comprehension axiom* for sets and relations defined by translations of formulas and programs.

At the end of the process, one can prove not only the semantical equivalence of validities in PDL with consequences from $\Delta _{\PDL}$ of the universal closure of their translations, but also that the dynamic calculus proves as theorems all the formulas whose translations are theorems of our theory $\Delta _{\PDL}$.

$$\begin{align} \models \varphi & \Longleftrightarrow \Delta _{\PDL}\models \forall u\Trans(\varphi )[u] \\ \vdash _{\PDL}\varphi & \Longleftrightarrow \Delta _{\PDL}\vdash _{\MSL}\forall u\Trans(\varphi )[u] \end{align} $$

Weak completeness follows directly.[^note-27]

## 6. Further Results

### 6.1 Reduction of Many-sorted Logic to One-sorted Logic

It is commonplace (Wang 1952, Feferman 1968, and Enderton 1972)[^enderton-1972][^feferman-1968][^wang-1952] to present many-sorted logic as easily convertible to one-sorted first-order logic. In Hao Wang (1952)[^wang-1952], the equivalence is built on provability while in Enderton’s book it has a semantical character.

Here we point out that many-sorted reduces to classical first-order logic (one-sorted) in the following sense: given a many-sorted structure $\mathcal{A}$, every many-sorted sentence true at $\mathcal{A}$ has a translation into one-sorted first order logic that is true at $\mathcal{A}^{\ast}$, where $\mathcal{A}^{\ast}$ is the result of unifying all the sorts in $\mathcal{A}$. From this result we obtain the equivalence between consequences in both logics, modulo a theory *Π* easily defined.

#### Syntactic translation

For the syntactic translation (known as “relativization of quantifiers”), let $L$ be a many-sorted language of signature $\Sigma$, and let $\OperSym$ be its set of operation symbols. We thus need an one-sorted language $L^{\ast}$ with

$$\OperSym^{\ast} = \OperSym\cup \{Q_{i}:i\in \Sort\}.$$

Variables of $L$ will be treated as variables of $L^{\ast}$, forgetting about sorts. The difference between the many-sorted language $L$ and the corresponding one-sorted one, $L^{\ast}$, is that we add new unary relation symbols $Q_{i}$, for each $i\in \Sort$. Moreover, the symbols in $\OperSym$ of $L$ are also in $L^{\ast}$ but while in the former language they have arity and sorts, in the latter they only have arity.

The translation, $\Trans$, leaves every term and formula unaltered, with the only exception of quantified expressions that are relativized:

$$ \Trans(\exists x^{i}\phi ) := \exists x^{i}(Q^{i}x^{i}\land \Trans(\phi )) $$

**Example:** As an example we will use the already presented argument from the **Book of Perfect Emptiness.** In one-sorted first order logic we can introduce this language:

$$\begin{align} Exy & :=x \textit{ exists at instant } y \\ Pxy & :=x \textit{ is previous to } y \\ Ox & :=x \textit{ is an object} \\ Ix & := x \textit{ is a time} \\ d & := \textit{the dawn of times} \\ t &:= \textit{today}\\ \end{align} $$

As you see, instead of using different sorts of variables, we add two new unary predicates, $O$ and $I$. We formalize the argument as:

$$\begin{align} \alpha & :=\forall x(Ix\land \exists y(Oy\land Eyx)\rightarrow \forall z(Iz\land Pzx\rightarrow \exists v(Ov\land Evz))) \label{primerorden} \\ \beta & :=\exists y(Oy\land Eyt)\\ \gamma &:=\forall y(Iy\rightarrow Pdy)\\ \delta & :=\exists x(Ox\land Exd) \end{align} $$

In order to derive the conclusion, we will need as well an extra hypothesis saying that *the dawn of times* and *today* are both times, $(Id\land It)$. We could add several formulas relating our new predicates:

$$\begin{align} \forall x(Ox &\rightarrow \lnot Ix)\\ \forall x\,\forall y(Exy&\rightarrow Ox\land Iy) \\ \forall x\,\forall y(Pxy&\rightarrow Ix\land Iy)\\ \end{align} $$

#### Conversion of many-sorted structures into one-sorted ones

For any many-sorted structure $\mathcal{A}$ of signature $\Sigma$ we construct its corresponding one-sorted structure $\mathcal{A}^{\ast}$ by something called “unification of domains”.

The domain of $\mathcal{A}^{\ast}$ is the union of the individuals domains of $\mathcal{A}$, the interpretation of the new unary predicates $Q_{i}$ corresponds to the old domains $\mathbf{A}_{i}$ and so this information is kept. The interpretation of the rest of elements in $\OperSym$ is similar to the one they have in the many-sorted structure $\mathcal{A}$. The only difficulty concerns operation symbols with $\Rank(f)=\langle i_{1},\ldots ,i_{n},i_{0}\rangle$ and $i_{0}\not=0$ because now the universe is the union of the universes and function $f^{\mathcal{A}^{\ast}}$ needs to give values to all of then. It is worth noting that for every $f^{\mathcal{A}}$ there are many different operations extending it, which means that there are different one-sorted structures generated by the above conversion.[^note-28]

The following theorem holds for any of these extended structures.

**Theorem:** Let $\mathcal{A}$ be a many-sorted structure, $\mathcal{A}^{\ast}$ one of its one-sorted counterparts, $L$ a language for $\mathcal{A}$, and *φ* some sentence in $L$. Then

$$\mathcal{A}\models \varphi \ \Longleftrightarrow \ \mathcal{A}^{\ast}\models \Trans(\varphi ).$$

We have seen that many-sorted structures are always convertible into one-sorted ones and now we consider the other direction.

#### Conversion of one-sorted structures into many-sorted ones

*Is any one-sorted structure $\mathcal{E}$ of signature $\Sigma ^{\ast}$ convertible into a many-sorted one of signature $\Sigma$?* The answer is negative, as there are two problems that could stop the conversion: the first one is that in a many-sorted structure all the universes should be nonempty and our idea is to take for each sort $i$ the unary relation $Q_{i}^{\mathcal{E}}$ as universe of sort $i$ and so we need it to be nonempty; the second difficulty concerns operation symbols with $\Rank(f)=\langle i_{1},\ldots i_{n},i_{0}\rangle$ whose interpretation in structure $\mathcal{E}$ is just an *n*-ary function, but we need the values of $f^{\mathcal{E}}\upharpoonright (Q_{i_{1}}^{\mathcal{E}}\times \ldots \times Q_{i_{n}}^{\mathcal{E}})$ to be in $Q_{i_{0}}^{\mathcal{E}}$.

What we do is to formulate in the one-sorted language three conditions whose validity in a model makes it easily convertible into a many-sorted one. Let *Π* be the set of all sentences of the following forms:

- $\exists x\ Q_{i}x$, for each $i\in \Sort$
- $\forall x_{1}\ldots x_{n}(Q_{i_{1}}x_{1}\land \ldots \land Q_{i_{n}}x_{n}\rightarrow Q_{i_{0}}(f\ x_{1}\ldots x_{n}))$, where $\Rank(f)=\langle i_{1},\ldots ,i_{n},i_{0}\rangle$, $f\in \OperSym$
- $Q_{i}c$, for each $c\in \OperSym$ with $\Rank(c)=i$.

Notice that the structure $\mathcal{A}^{\ast}$ of the previous theorem is a model of *Π*. Moreover, a one-sorted model of *Π*, $\mathcal{E}$, is easily convertible into a many-sorted one, $\mathcal{E}^{\ddag }$. We take $Q_{i}^{\mathcal{E}}$ as the universe of sort $i$, strict relations and functions are obtained as restrictions to the corresponding domains to obtain relations and functions with the desired sorts.[^note-29] Due to the axioms in *Π*, construction of $\mathcal{E}^{\ddag }$ can be carried out. It is now easy to obtain the following result.

**Main Theorem:** Let $\Gamma \cup \{\varphi \}\subseteq \Sent(L)$.

$$\Gamma \models _{\MSL}\varphi \text{ if and only if } \Trans(\Gamma )\cup \Pi \models _{\FOL}\Trans(\varphi )$$

We are using $\models _{\MSL}$ and $\models _{\FOL}$ to distinguish between consequence in many-sorted logic and in one-sorted logic.

The previous theorem allows us to infer the following three semantic theorems for MSL from the corresponding one-sorted results: *Compactness theorem*, *Enumerability theorem* and *Löwenheim-Skolem theorem* (see Enderton 1972: 281)[^enderton-1972]. But we have obtained them already as we have proven completeness for MSL (section 2.3). Obviously, from the many-sorted theorems we get the one-sorted version for free.

However, other theorems about many-sorted logic are not straightforwardly obtained from their one-sorted versions. In particular, interpolation in MSL requires its own proof (see section 6.2). The concept of interpretability plays an important role for a comparison between one-sorted and many-sorted theories (see section 6.3 and Hook 1985)[^hook-1985]. Unfortunately, interpretablity between many-sorted theories is not obtained from their one-sorted counterparts. Concerning the comparison, deductions in a many-sorted proof system are usually shorter than the derivations we get in a one-sorted calculus, that is one of the reasons why many-sorted logic is so frequently used in Computer Science (Meinke & Tucker 1993)[^meinke-1993].

### 6.2 The Interpolation Theorem

The Interpolation Theorem, which according to Wilfrid Hodges has “the longest pedigree of any theorem of model theory”,[^note-30] plays a relevant role in logic. In the first place, several important results such us Beth’s definability theorem and Robinson theorem could be obtained directly from it (see the entry first-order model theory). In the second place, interpolation can be seen as a central logical property which “has been used to reveal a deep harmony between syntax and semantics” (Feferman 2008: 341)[^feferman-2008].

The one-sorted version of interpolation was proved by William Craig in 1957a. Roger Lyndon (1959)[^lyndon-1959] gave a generalization of Craig’s theorem and, in 1968, Feferman extended the latter formulation to many-sorted logic (see Feferman 2008: 349)[^feferman-2008]. Obviously, the one-sorted version is a special case of the many-sorted one. However, many-sorted interpolation cannot be straightforwardly transferred from the one-sorted case.

The idea for Craig’s 1957 proof of the Interpolation Theorem rests on the completeness theorem for one-sorted first-order logic. The reason is that interpolation “lies” somehow in the intersection of proof theory (as it follows from some metatheorems about the calculus) and model theory (because of its applications). Henkin showed that the other way round also holds: completeness can be immediately obtained from a extended version[^note-31] of Craig-Lyndon’s theorem.

The syntactical formulation of Craig’s interpolation theorem reads as follows: If *φ* and *ψ* are sentences and $\vdash \varphi \rightarrow \psi$, then:

1. $\Rel(\varphi )\cap \Rel(\psi )\not=\varnothing$ implies that there is an “intermediate” formula *θ* such that $\vdash \varphi \rightarrow \theta$ and $\vdash \theta \rightarrow \psi$ (*θ* is a sentence such that $\Rel(\theta )\subseteq \Rel(\varphi )\cap \Rel(\psi )$) and
2. $\Rel(\varphi )\cap \Rel(\psi )=\varnothing$ implies $\vdash \lnot \varphi$ or $\vdash \psi$,

where $\Rel(\alpha)$ is the set of relational symbols in *α*. The intuition behind is as follows: during the process of proving the conditional formula $\varphi \rightarrow \psi$, we make use of what is today known as an “interpolant”, *θ*, a kind of *syllogism middle term* that finally disappears.

The theorem cannot be established for many-sorted logic by simply translating *φ* and *ψ* to the corresponding formulas of a one-sorted language. It is easy to see that the logical form of a constructed interpolant for $\vdash \Trans(\varphi )\rightarrow \Trans(\psi )$ is not necessarily equivalent to a translation of a many-sorted formula. This is why we said that this result could not be straightforwardly transferred from the one-sorted case (see Otto 2000 for more details)[^otto-2000].

As in one-sorted logic, the interpolation lemma for a many-sorted logic can be proven in model-theoretic style (as in Kreisel & Krivine 1967)[^kreisel-1967] or in proof-theoretical style, as in Feferman.[^note-32]

Feferman’s proof of interpolation is obtained directly as a corollary of one of his theorems for sequents (see Feferman 1968: 56–62; Theorem 4.3)[^feferman-1968] and its applications are model-theoretical, what reveals again the peculiar centrality of interpolation.

### 6.3 Interpretability and Theoretical Equivalence

Another notion not immediately transferable from FOL to MSL is that of *interpretability*. Interpretability is a good criterion for fixing a comparison between theories $T$ and $T^{\prime }$, for it is characterized either in terms of “uniform definability of models” or of “the existence of an interpretation map which preserves logical form and provability” (Mceldowney 2020: 15)[^mceldowney-2020]. It is also helpful for proving consistency, as $T^{\prime }$ is proved to be consistent when interpreted in a consistent $T$. However, interpretability between theories of a many-sorted signature does not guarantee interpretability between their (one-sorted) translations.

Mceldowney (2020)[^mceldowney-2020] argues that the concept of bi-interpretability is the best measure of theoretical equivalence in MSL. The oldest criterion for theoretical equivalence between first-order theories with the same signature is the notion of *definitional equivalence* (see Eilenberg & Mac Lane 1942, 1945 and Glymour 1971)[^eilenberg-1942][^eilenberg-1945][^glymour-1971]. Therefore, the necessity of a many-sorted counterpart was apparent. As a result, a debate on the nature of equivalence in MSL has taken place since 2016. Barrett and Halvorson (2016) generalizes the idea of definitional extension to the concept of *Morita extension*: intuitively, $T^+$ is a Morita extension of $T$ iff both $T$ and $T^+$ are MSL theories and $T^+$ “says no more” than the original theory (see 2016: 565 for formal details).

Thus, they claim that theoretical equivalence in MSL is to have a common Morita extension (this is called “Morita equivalence”). It is worth recalling at this point that the Morita extension $T^{+}$ of $T$ might be constructed by adding new sort symbols to the signature of $T$ together with the corresponding explicit definitions[^note-33] to the axioms. There are several ways to carry out this extension: the new sort *τ* can be introduced as a *subsort*, *product*, *coproduct* and *quotient sort* (see Barrett & Halvorson 2016: 563–64)[^barrett-2016]. Morita equivalence has also been used to try to clarify what is known in the literature as Quine’s conjecture on many-sorted logic (see Barrett & Halvorson 2017)[^barrett-2017].

Nevertheless, according to Mceldowney (2020)[^mceldowney-2020], a nuanced concept of Morita equivalence is just a special case of bi-interpretability. For this reason, he opted for a notion of equivalence in MSL based on interpretability rather than Morita extensions (see pp. 404-407 in Mceldowney 2020)[^mceldowney-2020]. In fact, as pointed out in Friedman and Visser (2014), bi-interpretability preserves finite axiomatizability, decidability, and κ-categoricity.

### 6.4 Extension of Many-sorted Logic to Sort Logic

Apart from its reduction to one-sorted logic, many-sorted first-order logic can be extended. *Sort logic* is a many-sorted second-order logic in which it is allowed to quantify over new sorts, “looking outside” the structure where the formula is being interpreted. Then, besides adding sorts to a second-order logic, we may include a new logical symbol $\widetilde{\exists }$ to quantify over new sorts.

In *Sort logic*, well-formed formulas involving $\widetilde{\exists }$ must respect a *New Sort Condition* (Väänänen 2014: 175)[^väänänen-2014] to guarantee that the domains where free variables in *φ* are interpreted do not interfere with the scope of the quantifier $\widetilde{\exists}$. The only novelty concerns interpretation of formulas with the new quantifier,

$\mathcal{M},s\models \widetilde{\exists }X\varphi$ if and only if $\mathcal{M}^{\prime },s(\mathbf{X}/X)\models \varphi$ for some *X*-expansion $\mathcal{M}^{\prime }$ of $\mathcal{M}$ and some $\mathbf{X}\in \wp (\mathbf{M}_{i_{1}}^{\prime }\times \ldots \times \mathbf{M}_{i_{r}}^{\prime })$ (where variable $X$ is of sort $\langle i_{1},\ldots ,i_{r},0\rangle)$

In this definition, model $\mathcal{M}^{\prime }$ is considered an *X*-expansion of $\mathcal{M}$ iff it includes as many new universes ($\mathbf{M}_{i_{1}}^{\prime },\ldots ,\mathbf{M}_{i_{r}}^{\prime }$) as the sorts of $X$ requires. Moreover, the restriction of $\mathcal{M}^{\prime }$ to the old ones is $\mathcal{M}$.

For instance, the formula

$$\widetilde{\exists }X\,\forall x\,\forall y(Xxy\land Xyx\rightarrow x=y)$$

says that there exists a new sort with a new anti-symmetric relation; somehow we are saying that anti-symmetry is a consistent concept as it can be exemplified.

An axiomatic calculus for sort logic was introduced in Väänänen (2014)[^väänänen-2014], as an extension of the second-order case. For this reason, he incorporated a second *Comprehension Axiom* related to $\widetilde{\exists}$ together with some restrictions concerning the rules of proof when formulas with the new quantifier $\widetilde{\exists }$ are involved (see 2014: 176–177).

As it occurs in every higher-order logic, completeness and compactness fail for sort logic with standard semantics. Fortunately, it is possible to build a *Henkin structure* satisfying both Comprehension axioms and to move to general semantics. Changing semantics in this way results in the recovery of completeness for the mentioned calculus, as Väänänen (2014: 179–80)[^väänänen-2014] has remarked. The proof found its inspiration in that of Henkin’s (1950)[^henkin-1950] for type theory.

Väänänen (2014: 181)[^väänänen-2014] applied sort logic to Foundations of Mathematics. He proposed the notion of truth in a structure $\mathcal{A}$ *characterizable in sort logic*, making a new distinction between general truth $\models \varphi$ and specific truth in those structures. Whenever general truth is reduced to specific truth, we can use the calculus to prove the satisfiability of a formula. Under certain constraints, any class of structures closed under isomorphism is definable in sort logic (see Kennedy & Väänänen 2021, Theorem 19)[^kennedy-2021]. Thus, Väänänen argues that sort logic is an “alternative way of looking at mathematics”, where, unlike set theory, “definition rather than construction is the focus” (2014: 185). It is also an interesting tool for studying *Logicality and model classes* (Kennedy & Väänänen 2021)[^kennedy-2021].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-many-sorted). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-many-sorted/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-many-sorted&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-many-sorted/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

logic: classical | logic: modal | logic: propositional dynamic | logic: second-order and higher-order | model theory | model theory: first-order | reasoning: automated | Tarski, Alfred: truth definitions | type theory: Church’s type theory

## Notes（原文脚注）

[^note-1]: One might, alternatively, include sort 0, as the sort of truth values. However, including the sort 0 is not mandatory. In general, the truth values are the classical Boolean truth and falsity, but we could consider a many-sorted logic which is also many-valued. In that case we would need to add a domain of sort 0, thereby opening the door to a many-valued, many-sorted logic. Another reason for choosing to add sort 0 would be to get closer to the common presentation of type theory (see the entry on Church’s type theory).

[^note-2]: Under certain circumstances, it is better to have an equality symbol for each sort $i$ (strict option), with $\Rank(\approx _{i})=\langle i,i,0\rangle$.

[^note-3]: In case you choose the strict option, $\tau _{1}\approx _{i}\tau _{2}$ is a well formed formula iff $\tau _{1}$ and $\tau _{2}$ have the same sort $i$.

[^note-4]: The precise definition is as follows. By a structure $\mathcal{A}$ of signature $\Sigma =\langle \Sort,\OperSym,\Rank\rangle$ we mean a pair:

$$\mathcal{A}=\langle \langle A_{i}\rangle _{i\in \Sort}\text{, }\langle f^{\mathcal{A}}\rangle _{f\in \OperSym}\rangle,$$

where

- $\langle A_{i}\rangle _{i\in \Sort}$ is a family of non-empty sets such that, for each $i\in \Sort$, $\mathbf{A}_{i}$ is the *i*ᵗʰ universe of $\mathcal{A}$.
- $\langle f^{\mathcal{A}}\rangle _{f\in \OperSym}$ is a family of functions such that, for every $f\in \OperSym$ with $\Rank(f)=\langle i_{1},\ldots,i_{m},i_{0}\rangle$, it holds that $$f^{\mathcal{A}}:\mathbf{A}_{i_{1}}\times \ldots\times \mathbf{A}_{i_{m}}\longrightarrow \mathbf{A}_{i_{0}}.$$ When $\Rank(R)=n$, then $$R^{\mathcal{A}}:\left(\bigcup\limits_{i\in \Sort}\kern-.5em\mathbf{A}_{i}\right)^{n}\longrightarrow \lbrace T,F \rbrace.$$

Logical connectives and equality are standard.

Obviously, when $\Rank(R)=\langle i_{1},\ldots,i_{m},0\rangle$, the above definition is the same as $R^{\mathcal{A}}\subseteq \mathbf{A}_{i_{1}}\times \ldots\times \mathbf{A}_{i_{m}}$ because an *n*-ary relation is just an *n*-ary function on the set of truth values, $\{T,F\}$. This function is often called *characteristic function*. When $\Rank(c)= i\,$ then $c^{\mathcal{A}}\in \mathbf{A}_{i}$.

[^note-5]: The precise definition is as follows. Given a Σ-structure $\mathcal{A}$, an *assignment* is a function $s$ from variables to the corresponding domains in the structure in such a way that a variable of sort $i$ always get its value in $\mathbf{A}_{i}$, namely, $s(x^{i})\in \mathbf{A}_{i}.$ For any individual $\mathbf{x}\in \mathbf{A}_{i}$ and variable $x^{i}$ of sort $i$, we use $s(\mathbf{x}/x^{i})$ to denote the assignment which is like $s$ except that the value at $x^{i}$ has to be $\mathbf{x}$. In other words,

$$s(\mathbf{x}/x^{i})=(s-\{\langle x^{i},s(x^{i})\rangle\})\cup \{\langle x^{i},\mathbf{x}\rangle \}$$

[^note-6]: There is no agreement on the definition of the term *theory*. It can be defined as a set of sentences closed under deducibility (or, equivalently, closed under semantical consequence).

A theory can be defined as a set of sentences (see Hodges 1993: 33)[^hodges-1993]. According to this definition, the smallest theory corresponds to the empty set. According to our definition, the set of validities is the smallest theory, and the whole $\Sent(L)$ the biggest (and contradictory) one.

[^note-7]: A set of formulas is *contradictory* (not consistent, or inconsistent) if and only if each formula in the language can be deduced from it. A set of formulas is *maximally consistent* when besides being consistent, each formula not in the set would make it inconsistent, if it were added to the set.

[^note-8]: For details on the history of the various notions of completeness, see Manzano & Alonso 2014 and Aranda 2022.

[^note-9]: A model $\mathcal{A}$ is countable when $\bigcup\limits_{i\in \Sort}\kern-.5em\mathbf{A}_{i}$ is countable.

[^note-10]: See “Decidable fragments of many-sorted logic” (Abadi, Rabinovich, & Sagiv 2007)[^abadi-2007].

[^note-11]: Carnielli, Coniglio and D’Ottaviano (2009) have also studied the concept of abstract contextual translation. In addition to this, D’Ottaviano and Feitosa 2019 is a survey of translations between logics.

[^note-12]: The set of modal validities in *minimal modal logic* could be axiomatized by a Hilbert axiomatic system called *K* including axiom

$$K:=\square (\varphi \rightarrow \psi )\rightarrow (\square \varphi \rightarrow \square \psi )$$

and a modal generalization rule, if $\vdash \varphi$ then $\vdash \square \varphi$. See Blackburn and van Benthem (2007: 10)

[^note-13]: The idea is simple:

> Whenever we translate a $\Diamond$ or a $\square$, instead of choosing a completely new variable to quantify over accessible points, we use a second fixed variable (say $y$). If we later encounter another $\Diamond$ or $\square$, we flip back to the original variable $x$, and so on. (Blackburn & van Benthem 2007: 28)[^blackburn-2007][^blackburn-2007-2]

[^note-14]: Bisimulation can be defined for formulas $\varphi (x)$ of a first-order language and we can prove (see Blackburn & van Benthem 2007: 21)[^blackburn-2007][^blackburn-2007-2]:

**Modal Characterization Theorem:** The following are equivalent for all first-order formulas $\varphi (x)$ in one free variable $x$:

1. $\varphi (x)$ is invariant under bisimulation.
2. $\varphi (x)$ is equivalent to the standard translation of a basic modal formula.

[^note-15]: For a more detailed explanation see Manzano (1996: 263–276)[^manzano-1996].

[^note-16]: In fact, the inclusion is strict

$$\Val_{\mathfrak{F}}\subset \Val_{\mathfrak{GS}}\subset \Val_{\mathfrak{SS}}$$

as the following examples show:

1. The comprehension axiom belongs to $\Val_{\mathfrak{GS}}$ but it is not a valid formula with the semantics of frames.
2. To put an example of a valid sentence in standard structures that fails in some general structures let us take the sentence $$\pi _{1}\land \pi _{2}\land \pi _{3}\rightarrow \gamma$$ where $\pi _{1}$, $\pi _{2}$ and $\pi _{3}$ are the second-order categorical Peano axioms for arithmetic, and *γ* is the well-known Gödel formula asserting of itself that it is not a theorem of Peano arithmetic.

[^note-17]: For simplicity we keep the notation $\langle\underbrace{ 1,\ldots ,1}_n ,0\rangle$ for sorts in $\MSL^{\SOL}$, but now we do not require the domain of this sort to be of *n*-ary relations of elements of sort 1.

[^note-18]: For more details, see Manzano (1996: 285–288)[^manzano-1996].

[^note-19]: Consider now the following example: from a structure $\mathcal{A}$ with domains $\mathbf{A}_{1}=\{ 1,2,3\}$ and $\mathbf{A}_{\langle 1,0\rangle }=\{ 4,7\}$ where

$$\epsilon _{n}^{\mathcal{A}}=\{ \langle 1,4\rangle ,\langle 2,4\rangle ,\langle 3,4\rangle \},$$

we obtain a structure $\mathcal{B}$ with $\mathbf{B}_{1}=\{ 1,2,3\}$ and $\mathbf{B}_{\langle 1,0\rangle }=\{ \{ 1,2,3\} ,\varnothing \}$ where

$$\epsilon _{n}^{\mathcal{B}}=\{ \langle 1,\{ 1,2,3\} \rangle ,\langle 2,\{ 1,2,3\} \rangle ,\langle 3,\{ 1,2,3\} \rangle \}$$

[^note-20]: The official publication date by Princeton University Press is 1956, however the book was available in manuscript form before 1956, according to Henkin (1996)[^henkin-1996]. More specifically, as noted in the Preface, the 1956 edition is a “revised and much enlarged edition” of an earlier 1944 edition (Church 1956, v)[^church-1956].

[^note-21]: $\Trans(\varphi )[u]$ is defined by induction on the construction of formulas, $u$ is an individual variable in MSL whose interpretation is a world in the Kripke model.

$$\begin{align} \Trans(P)[u] &:=Pu\\ \Trans(\perp )[u]&:=u\neq u\\ \Trans(\lnot \varphi )[u]&:=\lnot \Trans(\varphi )[u]\\ \Trans(\varphi \rightarrow \psi )[u]&:=\Trans(\varphi )[u]\rightarrow \Trans(\psi )[u]\\ \Trans(\Box \varphi )[u]&:=\forall v(Suv\rightarrow \Trans(\varphi )[v])\\ \end{align}$$

[^note-22]: The set $\Def$ contains the empty set, the whole $\mathbf{W}$ and all the members in the family $\langle P^{\mathcal{A}}\rangle _{P\in \Atom}$. It is closed under Boolean operations as well as under this operation

$$\forall \mathbf{T}(\mathbf{T}\in \Def\Rightarrow \Dom(\mathbf{R}\cap (\mathbf{W}\times \mathbf{T}))\in \Def)$$

to guarantee that initial states from accessibility relations leading to definable sets are definable. Outside $\Def$, but in $\mathbf{W}^{\prime }$, we have the singletons of all elements of $\mathbf{W}$. Finally, $\mathbf{W}^{\prime }$ also obeys the rule

$$\forall w(w\in \mathbf{W}\Rightarrow \Rec(\mathbf{R}\cap (\{ w\} \times \mathbf{W}))\in \mathbf{W}^{\prime }).$$

[^note-23]: Let us use $\Delta _{S4}$ to refer to the many-sorted theory obtained by adding to $\Delta _{K}$ the many-sorted formulas $\MS(T)$ and $\MS(4)$.

$$\begin{align} \MS(T)& :=\forall uY(\forall v(Suv\rightarrow \epsilon _{1}vY)\rightarrow \epsilon _{1}uY)\\ \MS(4)&:=\forall uY(\forall v(Suv\rightarrow \epsilon _{1}vY)\rightarrow \forall v(Suv\rightarrow \forall w(Svw\rightarrow \epsilon _{1}wY)))\\ \end{align}$$

[^note-24]: Main Theorem:

- $\Pi \models \varphi$ (in the whole class of Kripke structures) ${}\Longleftrightarrow \Trans(\Pi )\cup \Delta _{K}\models \Trans(\varphi )$
- $\Pi \models _{\mathfrak{D}}\varphi$ (in the class $\mathcal{D}$ of *reflexive* and *transitive* Kripke structures) ${} \Longleftrightarrow \Trans(\Pi )\cup \Delta _{S4}\models \Trans(\varphi )$

As in modal logics *K* and *S*4 we already have the concept of logical consequence, and we obtain the desired theorem for both, by defining the reverse conversion of structures by getting rid of the domain $\mathbf{W}'$.

[^note-25]: For a modal logic *B*, we define its canonical model $\mathcal{B}_{B}$, by taking as world $W$ all the *B*-maximally consistent sets and defining the accessibility relation in this way

$$\{\langle x,y\rangle \mid\{ \varphi |\Box \varphi \in x\} \subseteq y\}$$

[^note-26]: The translation for formulas is defined as for formulas of PML with the following additions:

$$\begin{align} \Trans(\left[ a\right] \varphi )[u]&:=\forall v(\Trans(a)[u,v]\rightarrow \Trans(\varphi )[v])\\ \Trans(Q)[u,v]&:=Quv\\ \Trans(a;b)[u,v]&:=\exists w(\Trans(a)[u,w]\land \Trans(a)[w,v])\\ \Trans(a\cup b)[u,v]&:=\Trans(a)[u,v]\lor \Trans(a)[u,v]\\ \Trans(a\ast )[u,v]&:=\forall X^{2}(\Trans(a)\subseteq X^{2}\land \Reflexive (X^{2})\\ & \quad\quad \land \Transitive (X^{2}) \rightarrow \epsilon _{2}uvX^{2})\\ \end{align}$$

This formula is an abbreviation and says that it is the least reflexive and transitive relation containing the translated one.

$$\Trans(\varphi ?)[u,v]:=\Trans(\varphi )[u]\land u=v$$

[^note-27]: For a more detailed explanation see Manzano (1996: 335–351)[^manzano-1996] as well as Manzano (1993: 72–81)[^manzano-1993].

[^note-28]: The precise definition of one-sorted structure $\mathcal{A}^{\ast}$ is obtained by conversion from the many-sorted structure $\mathcal{A}$ as follows

$$\mathcal{A}^{\ast }=\langle A^{\ast },\langle f_{{}}^{\mathcal{A^{\ast }}}\rangle _{f\in \OperDSym},\langle Q_{i}^{\mathcal{A^{\ast }}}\rangle _{i\in \Sort}\rangle$$

and by means of the following clauses:

- The domain of $\mathcal{A}^{\ast }$ is the union of the individuals domains of $\mathcal{A}$, that is, $\mathbf{A}^{\ast }=\bigcup_{i\in \Sort}\kern-.5em\mathbf{A}_{i}$.
- For each $f\in \OperDSym$ with $\Rank(f)=\langle i_{1},\ldots ,i_{n},i_{0}\rangle$ and $i_{0}\neq 0$, $f^{\mathcal{A}^{\ast }}$ is any extension of $f^{\mathcal{A}}$ such that the domain of the function is the whole $(A^{\ast })^{n}$ and the restriction to the old domain is the original $f^{\mathcal{A}}$, that is $$\ f^{\mathcal{A}^{\ast }}\upharpoonright (\mathbf{A}_{i_{1}}\times \ldots \times \mathbf{A}_{i_{n}})=f^{\mathcal{A}}$$ (where new values in $f^{\mathcal{A}^{\ast }}$ are chosen arbitrarily).
- For each $R\in \OperDSym$ with either $\Rank(R)=\langle i_{1},\ldots ,i_{n},0\rangle$ or $\Rank(R)=n$, the relations used as interpretation are the same in both structures, $R^{\mathcal{A}^{\ast }}=R^{\mathcal{A}}$.
- $Q_{i}^{\mathcal{A^{\ast }}}=\mathbf{A}_{i}$ for each $i\in \Sort$.

[^note-29]: The precise definition is as follows. For each sort $i$, we take $Q_{i}^{\mathcal{E}}$ as the universe of this sort, that now we know is nonempty. For each predicate symbol $R$ with $\Rank(R)=n$, $R^{\mathcal{E}^{\ddag }}=R^{\mathcal{E}}$, nothing changes. For each predicate symbol $R$ with $\Rank(R)=\langle i_{1},\ldots,i_{n},0\rangle$, its interpretation is the restriction to the new local universes,

$$R^{\mathcal{E}^{\ddag }}=R^{\mathcal{E}}\cap (Q_{i_{1}}^{\mathcal{E}}\times \ldots\times Q_{i_{n}}^{\mathcal{E}}).$$

Finally, for each function symbol $f$ with $\Rank(f)=\langle i_{1},\ldots,i_{n},i_{o}\rangle$, its interpretation is the restriction to the new local universes,

$$f^{\mathcal{E}^{\ddag }}=f^{\mathcal{E}}\upharpoonright (Q_{i_{1}}^{\mathcal{E}}\times \ldots\times Q_{i_{n}}^{\mathcal{E}}),$$

that is a function of the desired sort.

[^note-30]: Let us quote Feferman’s (2008)[^feferman-2008] own words:

> Interestingly, in a personal communication, Wilfrid Hodges brought to my attention that “t]he Lyndon theorem has a claim to be the twentieth century metatheorem with the longest pedigree, because it is a generalisation of the late medieval laws of distribution for syllogisms. Obviously the theorem itself and any of its proofs would have been way beyond the understanding of any of the medievals, but it does seem to contain the correct formalisation of a number of medieval intuitions.” For elaboration, see Hodges (1998)[^hodges-1998]. (2008: 346–347, note 4)

[^note-31]: Extended Craig-Lyndon’s Interpolation Theorem: If $\Gamma \models \Delta$, then $\Gamma \vdash B$ and $B \vdash \delta$. From this, strong completeness follows immediately (see Henkin 1963b)[^henkin-1963b].

[^note-32]: Feferman’s version of the theorem for MSL includes not only $\Rel^{+}$ and $\Rel^{-}$ (which have to be used for Lyndon’s generalized theorem), but also four new sets, $\Sort$, $\Free$, $\Un$ and $\Ex$:

$$\begin{align} \Sort(\varphi )&=\{ j\in J:\text{a variable of sort }j\text{ occurs in }\varphi \} \\ \Free(\varphi )&= \text{the set of free variables of }\varphi \\ \Un(\varphi )&=\{ j\in J:\text{a }\forall x_{j}\text{ occurs in }\nnf(\varphi )\} \\ \Ex(\varphi )&=\{ j\in J:\text{a }\exists x_{j}\text{ occurs in }\nnf(\varphi )\} \\ \end{align}$$ (where $\nnf(\varphi )$ is the negation normal form of *φ*)

In consequence, the Interpolation Theorem for MSL states that: If $\vdash \varphi \rightarrow \psi$, then it has an interpolant *θ* with respect to $\Rel^{+}$, $\Rel^{-}$, $\Sort$ and $\Free$ for which

$$\Un(\theta )\subseteq \Un(\varphi )\text{ and }\Ex(\theta )\subseteq \Ex(\psi ).$$

[^note-33]: See Hodges (1993: 59)[^hodges-1993] for a description of the concept of explicit definition in one-sorted first-order logic; see Barrett and Halvorson (2016: 560) for the many-sorted case.

[^note-34]: 34. The official publication date by Princeton University Press is 1956, despite the fact that, in the references of Wang (1952)[^wang-1952], the date of publication is 1944. We know that early forms of the book were available in manuscript form before 1956 (see Henkin 1996, p. 133)[^henkin-1996]. Exercise 55.24 (p. 339) is in Chapter 5 and according to the Preface, the work on Chapters 3, 4, and 5 was done in 1948–1951 (Church 1956, vi)[^church-1956].

[^note-35]: 35. The one-sorted elementary logic Wang refers to is the one presented in Quine 1940.

[^note-36]: 36. In section 22, Quine says:

> We now turn to a connective “*ε*” which embodies the principal meaning of the ambiguous word “is”. Sometimes “is” has the sense of “$=$” or “is the same as”; such is its sense in *“Paris is the capital of France”*…. But in *“Paris is a city”* the word cannot be so construed. In such contexts “is” expresses rather possession of a property, or membership in a class: Paris belongs to the class of cities. (Quine 1940: 119)[^quine-1940]

Quine also admits:

> …there are differences in detail between the notion of membership developed here and the notion of membership that Tarski and Gödel took over from Whitehead and Russell. (Quine 1940: 126)[^quine-1940]

[^abadi-2007]: Abadi, Aharon, Alexander Rabinovich, and Mooly Sagiv, 2007, “Decidable Fragments of Many-Sorted Logic”, in *Logic for Programming, Artificial Intelligence, and Reasoning*, Nachum Dershowitz and Andrei Voronkov (eds.), (Lecture Notes in Computer Science 4790), Berlin, Heidelberg: Springer Berlin Heidelberg, 17–31. doi:10.1007/978-3-540-75560-9_4

[^andréka-1998]: Andréka, Hajnal, István Németi, and Johan van Benthem, 1998, “Modal Languages and Bounded Fragments of Predicate Logic”, *Journal of Philosophical Logic*, 27(3): 217–274. doi:10.1023/A:1004275029985

[^andréka-2014]: Andréka, Hajnal, Johan van Benthem, Nick Bezhanishvili, and István Németi, 2014, “Changing a Semantics: Opportunism or Courage?”, in Manzano, Sain, and Alonso 2014: 307–337. doi:10.1007/978-3-319-09719-0_20

[^aranda-2022]: Aranda, Víctor, 2022, “Completeness: From Husserl to Carnap”, *Logica Universalis*, 16(1–2): 57–83. doi:10.1007/s11787-021-00283-4

[^barrett-2016]: Barrett, Thomas William and Hans Halvorson, 2016, “Morita Equivalence”, *The Review of Symbolic Logic*, 9(3): 556–582. doi:10.1017/S1755020316000186

[^barrett-2017]: –––, 2017, “Quine’s Conjecture on Many-Sorted Logic”, *Synthese*, 194(9): 3563–3582. doi:10.1007/s11229-016-1107-z

[^blackburn-2007]: Blackburn, Patrick and Johan van Benthem, 2007, “Modal Logic: A Semantic Perspective”, in Blackburn, van Benthem, and Wolter 2007: 1–84. doi:10.1016/S1570-2464(07)80004-8

[^blackburn-2007-2]: Blackburn, Patrick, Johan van Benthem, and Frank Wolter (eds.), 2007, *Handbook of Modal Logic*, (Studies in Logic and Practical Reasoning 3), Amsterdam/Boston: Elsevier. [[Blackburn, van Benthem, and Wolter 2007 available online](https://www.csc.liv.ac.uk/~frank/MLHandbook/)]

[^benthem-1983]: van Benthem, Johan, 1983, *Modal Logic and Classical Logic*, (Indices 3), Napoli: Bibliopolis.

[^benthem-1984a]: –––, 1984a, “Correspondence Theory”, in *Handbook of Philosophical Logic*, D. Gabbay and F. Guenthner (eds.), Dordrecht: Springer Netherlands, 167–247. doi:10.1007/978-94-009-6259-0_4

[^benthem-1984b]: –––, 1984b, “Review: B. J. Copeland. On When a Semantics Is Not a Semantics: Some Reasons for Disliking the Routley–Semantics for Relevance Logic. *Journal of Philosophical Logic*, Vol. 8 (1979), pp. 399–413”, *Journal of Symbolic Logic*, 49(3): 994–995. doi:10.2307/2274161

[^benthem-2010]: –––, 2010, *Modal Logic for Open Minds*, (CSLI Lecture Notes 199), Stanford, CA: CSLI Publications.

[^carnielli-2009]: Carnielli, Walter A., Marcelo E. Coniglio, and Itala M. L. D’Ottaviano, 2009, “New Dimensions on Translations Between Logics”, *Logica Universalis*, 3(1): 1–18. doi:10.1007/s11787-009-0002-5

[^church-1956]: Church, Alonzo, 1956, *Introduction to Mathematical Logic, Volume 1*, (Princeton Mathematical Series 17), Princeton, NJ: Princeton University Press. [Note: this was a new revised edition from a 1944 edition published as an *Annals of Mathematics Studies* volume (no. 13).]

[^craig-1957a]: Craig, William, 1957a, “Linear Reasoning. A New Form of the Herbrand-Gentzen Theorem”, *Journal of Symbolic Logic*, 22(3): 250–268. doi:10.2307/2963593

[^craig-1957b]: –––, 1957b, “Three Uses of the Herbrand-Gentzen Theorem in Relating Model Theory and Proof Theory”, *Journal of Symbolic Logic*, 22(3): 269–285. doi:10.2307/2963594

[^silva-1999]: da Silva, Jairo J., Itala Marı́a L. D’Ottaviano, and A. M. Sette, 1999, “Translations between Logics”, in *Models, Algebras, and Proofs*, Xavier Caicedo and Carlos H. Montenegro (eds.), (Lecture Notes in Pure and Applied Mathematics 203), New York: Marcel Dekker, 435–448.

[^d’ottaviano-2019]: D’Ottaviano, Itala M. Loffredo and Hércules de Araújo Feitosa, 2019, “Translations Between Logics: A Survey”, in *Philosophy of Logic and Mathematics: Proceedings of the 41st International Ludwig Wittgenstein Symposium*, Gabriele M. Mras, Paul Weingartner, and Bernhard Ritter (eds.), Boston/Berlin: De Gruyter, 71–90. doi:10.1515/9783110657883-005

[^ebbinghaus-1984]: Ebbinghaus, Heinz-Dieter, Jörg Flum, and Wolfgang Thomas, 1984, *Mathematical Logic*, (Undergraduate Texts in Mathematics), New York: Springer-Verlag.

[^eilenberg-1942]: Eilenberg, Samuel and Saunders MacLane, 1942, “Group Extensions and Homology”, *The Annals of Mathematics*, 43(4): 757–831. doi:10.2307/1968966

[^eilenberg-1945]: –––, 1945, “General Theory of Natural Equivalences”, *Transactions of the American Mathematical Society*, 58(2): 231–294.

[^enderton-1972]: Enderton, Herbert B., 1972, *A Mathematical Introduction to Logic*, New York: Academic Press.

[^feferman-1968]: Feferman, Solomon, 1968, “Lectures on Proof Theory”, in *Proceedings of the Summer School in Logic Leeds, 1967*, M. H. Löb (ed.), (Lecture Notes in Mathematics 70), Berlin/Heidelberg: Springer Berlin Heidelberg, 1–107. doi:10.1007/BFb0079094

[^feferman-1974]: –––, 1974, “Applications of many-sorted interpolation theorems”, in *Proceedings of the Tarski Symposium*, L. Henkin, J. Addison, C. Chang, W. Craig, D. Scott and R. Vaught (eds.), (Proceedings of Symposia in Pure Mathematics, 25), Providence, RI: AMS, pp. 205–224.

[^feferman-2008]: –––, 2008, “Harmonious Logic: Craig’s Interpolation Theorem and Its Descendants”, *Synthese*, 164(3): 341–357. doi:10.1007/s11229-008-9354-2

[^feferman-2016]: –––, 2016, “Many-sorted first-order model theory as a conceptual framework for biological and other complex dynamical systems”, Keynote address to the *AMS/ASL session on applications of Logic, Model Theory, and Theoretical Computer Science to System Biology*, Seattle, 9 January 2016. [[Feferman 2016 draft available online](http://math.stanford.edu/%7Efeferman/papers/Manysorted_logic_for_SB.pdf)]

[^friedman-2014]: Friedman, Harvey and Visser, Albert, 2014, “When bi-interpretability implies synonymy”, *Logic Group Preprint Series*, 320: 1–19.

[^gabbay-1994]: Gabbay, Dov M. (ed.), 1994, *What Is a Logical System?*, (Studies in Logic and Computation 4), Oxford: Clarendon Press.

[^gabbay-1996]: –––, 1996, *Labelled Deductive Systems, Volume 1*, (Oxford Logic Guides 33), Oxford: Oxford University Press.

[^gilmore-1958]: Gilmore, Paul, 1958, “An addition to ‘Logic of Many-Sorted Theories’”, *Compositio Mathematica*, 13: 277–281.

[^glymour-1971]: Glymour, Clark, 1971, “Theoretical Realism and Theoretical Equivalence”, in *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association, 1970*, Roger C. Buck and Robert S. Cohen (eds.), (Boston Studies in the Philosophy of Science 8), Dordrecht: Springer Netherlands, 275–288. doi:10.1007/978-94-010-3142-4_19

[^gödel-1931]: Gödel, Kurt, 1931, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I”, *Monatshefte für Mathematik und Physik*, 38–38(1): 173–198. doi:10.1007/BF01700692

[^grzegorczyk-1955]: Grzegorczyk, Andrzej, 1955, “The Systems of Leśniewski in Relation to Contemporary Logical Research”, *Studia Logica*, 3(1): 77–95. doi:10.1007/BF02067248

[^henkin-1949]: Henkin, Leon, 1949, “The Completeness of the First-Order Functional Calculus”, *Journal of Symbolic Logic*, 14(3): 159–166. doi:10.2307/2267044

[^henkin-1950]: –––, 1950, “Completeness in the Theory of Types”, *Journal of Symbolic Logic*, 15(2): 81–91. doi:10.2307/2266967

[^henkin-1953]: –––, 1953, “Banishing the Rule of Substitution for Functional Variables”, *Journal of Symbolic Logic*, 18(3): 201–208. doi:10.2307/2267403

[^henkin-1963a]: –––, 1963a, “A Theory of Prepositional Types”, *Fundamenta Mathematicae*, 52(3): 323–344. doi:10.4064/fm-52-3-323-344

[^henkin-1963b]: –––, 1963b, “An Extension of the Craig-Lyndon Interpolation Theorem”, *Journal of Symbolic Logic*, 28(3): 201–216. doi:10.2307/2271066

[^henkin-1996]: –––, 1996, “The Discovery of My Completeness Proofs”, *Bulletin of Symbolic Logic*, 2(2): 127–158. doi:10.2307/421107

[^herbrand-1930]: Herbrand, Jacques, 1930, *Recherches sur la théorie de la démonstration*, PhD thesis, University of Paris.

[^hodges-1986]: Hodges, Wilfrid, 1986, “Truth in a Structure”, *Proceedings of the Aristotelian Society*, 86(1): 135–152. doi:10.1093/aristotelian/86.1.135

[^hodges-1993]: –––, 1993, *Model Theory*, Cambridge/New York: Cambridge University Press. doi:10.1017/CBO9780511551574

[^hodges-1998]: –––, 1998, “The Laws of Distribution for Syllogisms”, *Notre Dame Journal of Formal Logic*, 39(2): 221–230. doi:10.1305/ndjfl/1039293064

[^hook-1985]: Hook, Julian L., 1985, “A Note on Interpretations of Many-Sorted Theories”, *Journal of Symbolic Logic*, 50(2): 372–374. doi:10.2307/2274223

[^kennedy-2021]: Kennedy, Juliette and Väänänen, Jouko, 2021, “Logicality and Model Classes”, *The Bulletin of Symbolic Logic*, 27(4): 385–414. doi:10.1017/bsl.2021.42

[^kreisel-1967]: Kreisel, Georg and J. L. Krivine, 1967, *Éléments de logique mathématique, théorie des modèles* (Monographies de la Société mathématique de France 3), Paris: Dunod; translated as *Elements of Mathematical Logic: Model Theory* (Studies in Logic and the Foundations of Mathematics), Amsterdam: North Holland, 1967.

[^langford-1939]: Langford, C. H., 1939, “Review: Arnold Schmidt. ‘Über deduktive Theorien mit mehreren Sorten von Grunddingen’, *Mathematische Annalen*, 115. 4 (1938), pp. 485–506”, *Journal of Symbolic Logic*, 4(2): 98–98. doi:10.2307/2269080

[^liezi-1982]: Liezi, (列子, *El libro de la perfecta vacuidad*), Barcelona: Kairos, 1982. Translated directly from Chinese by Iñaki Preciado. Example translated to English for this Entry by Ulises Tindón.

[^lindström-1969]: Lindström, Per, 1969, “On Extensions of Elementary Logic”, *Theoria*, 35(1): 1–11. doi:10.1111/j.1755-2567.1969.tb00356.x

[^lyndon-1959]: Lyndon, Roger C., 1959, “An Interpolation Theorem in the Predicate Calculus”, *Pacific Journal of Mathematics*, 9(1): 129–142.

[^manzano-1989]: Manzano, María, 1989 [1999], *Teoría de modelos*, Madrid: Alianza Editorial. Translated as *Model Theory*, Ruy J. G. B. de Queiroz (trans.), (Oxford Logic Guides 37), Oxford/New York: Clarendon Press ; Oxford University Press, 1999.

[^manzano-1993]: –––, 1993, “Introduction to Many-sorted logic”, Meinke and Tucker 1993: 3–86.

[^manzano-1996]: –––, 1996, *Extensions of First Order Logic*, (Cambridge Tracts in Theoretical Computer Science 19), Cambridge/New York: Cambridge University Press.

[^manzano-2014a]: –––, 2014a, “April the 19th”, in Manzano, Sain, and Alonso 2014: 265–278. doi:10.1007/978-3-319-09719-0_18

[^manzano-2014b]: –––, 2014b, “Henkin on Completeness”, in Manzano, Sain, and Alonso 2014: 149–175. doi:10.1007/978-3-319-09719-0_12

[^manzano-2014]: Manzano, Maria and Enrique Alonso, 2014, “Completeness: From Gödel to Henkin”, *History and Philosophy of Logic*, 35(1): 50–75. doi:10.1080/01445340.2013.816555

[^manzano-2014-2]: Manzano, María, Ildikó Sain, and Enrique Alonso (eds.), 2014, *The Life and Work of Leon Henkin*, (Studies in Universal Logic), Cham: Springer International Publishing. doi:10.1007/978-3-319-09719-0

[^martí-oliet-1994]: Martí-Oliet, Narciso and José Meseguer, 1994, “General Logics and Logical Frameworks”, in *What Is a Logical System?*, Dov M. Gabbay (ed.), Oxford: Clarendon Press, 355–391.

[^mceldowney-2020]: Mceldowney, Paul Anh, 2020, “On Morita Equivalence and Interpretability”, *The Review of Symbolic Logic*, 13(2): 388–415. doi:10.1017/S1755020319000303

[^meinke-1993]: Meinke, Karl and John Tucker (eds.), 1993, *Many-Sorted Logic and Its Applications*, (Wiley Professional Computing), Chichester/New York: Wiley.

[^meseguer-1989]: Meseguer, José, 1989, “General Logics”, in *Logic Colloquium’87: Proceedings of the Colloquium Held in Granada*, H.-D. Ebbinghaus, J. Fernandez-Prida, M. Garrido, D. Lascar, and M. Rodriquez Artalejo (eds.), (Studies in Logic and the Foundations of Mathematics 129), Amsterdam: North-Holland, 275–329. doi:10.1016/S0049-237X(08)70132-0

[^otto-2000]: Otto, Martin, 2000, “An Interpolation Theorem”, *Bulletin of Symbolic Logic*, 6(4): 447–462. doi:10.2307/420966

[^quine-1940]: Quine, Willard Van Orman, 1940, *Mathematical Logic*, New York: W. W. Norton & Company.

[^schmidt-1938]: Schmidt, Arnold, 1938, “Über deduktive Theorien mit mehreren Sorten von Grunddingen”, *Mathematische Annalen*, 115(4): 485–506. doi:10.1007/BF01448954

[^tarski-1933]: Tarski, Alfred, 1933 [1983], *Pojęcie prawdy w językach nauk dedukcyjnych*, (Prace Towarzystwa Naukowego Warszawskiego, Wydzial III Nauk Matematyczno-Fizycznych, 34), Warsaw: Nakładem Towarzystwa Naukowego Warszawskiego. Translated as “The Concept of Truth in Formalized Languages”, J.H. Woodger (trans.), in *Logic, Semantics, Metamathematics*, second edition, J. Corcoran (ed.), Indianapolis, IN: Hackett, 1983, 152–278.

[^tarski-1956]: Tarski, Alfred and Robert Lawson Vaught, 1956, “Arithmetical Extensions of Relational Systems”, *Compositio Mathematica*, 13: 81–102.

[^väänänen-1979]: Väänänen, Jouko, 1979, “Abstract Logic and Set Theory. I. Definability”, in *Logic Colloquium ’78: Proceedings of the Colloquium Held in Mons*, Maurice Boffa, Dirkvan Dalen, and Kenneth Mcaloon (eds.), (Studies in Logic and the Foundations of Mathematics 97), Amsterdam: Elsevier, 391–421. doi:10.1016/S0049-237X(08)71637-9

[^väänänen-1982]: –––, 1982, “Abstract Logic and Set Theory. II. Large Cardinals”, *Journal of Symbolic Logic*, 47(2): 335–346. doi:10.2307/2273145

[^väänänen-2014]: –––, 2014, “Sort Logic and Foundations of Mathematics”, in *Infinity and Truth*, by Chitat Chong, Qi Feng, Theodore A Slaman, and W Hugh Woodin, (Lecture Notes Series, Institute for Mathematical Sciences, National University of Singapore 25), Singapore: World Scientific, 171–186. doi:10.1142/9789814571043_0005

[^wang-1952]: Wang, Hao, 1952, “Logic of Many-Sorted Theories”, *Journal of Symbolic Logic*, 17(2): 105–116. doi:10.2307/2266241
