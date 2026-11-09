# lukasiewicz — polish-notation（supplement）

> （《lukasiewicz》词条补充材料，源：plato.stanford.edu/entries/lukasiewicz/polish-notation.html）

#### Supplement to Jan Łukasiewicz

## Łukasiewicz's Parenthesis-Free or Polish Notation

It is sometimes said that Łukasiewicz’s chief contribution to logic was the invention of so-called Polish notation. Nothing could be further from the truth. Łukasiewicz did indeed invent, in 1924, the notation which is variously known as Łukasiewicz notation or Polish notation, but it is a minor and very incidental part of his creative talent, incomparable with his scholarly achievements in propositional logic, many-valued logic and the history of logic. Nevertheless, we employ the notation in this article, and some remarks are in order.

In the standard Peano-Russell notation for propositional calculus the symbols for binary connectives (conjunction, disjunction, implication, equivalence and so on) are written between their arguments, for example $p \wedge q$, $p \rightarrow q$. This is known as infix notation, and it is familiar from arithmetical operations such as addition and multiplication. For other than the simplest formulas, this necessitates the use of parentheses to disambiguate: the string of symbols

\begin{align} & p \rightarrow q \rightarrow r \end{align}

is ambiguous between

$$ \begin{align} & p \rightarrow (q \rightarrow r) \end{align} $$

and

$$ \begin{align} & (p \rightarrow q) \rightarrow r \end{align} $$

which have different truth-conditions: the former is true and the latter false when all three arguments are false, for instance. Parentheses clutter a formula visually and graphically. Peano and Russell instead used clusters of dots to disambiguate formulas, but like parentheses they are difficult to comprehend visually and track manually once formulas become relatively complex. Frege, in his branching-tree logical notation, had worked out an elegant parenthesis-free way to notate propositional formulas, but being non-linear, it is space-consuming and difficult to typeset. It had long been the practice of mathematicians to place general function symbols before their arguments, and Leon Chwistek mentioned this to Łukasiewicz in the early 1920s as a possibility for propositional connectives. Łukasiewicz then worked out the principles of the notation, possibly by experimenting with wooden blocks to compose formulas. All functors (connectives) are written before their arguments, each connective is represented by a different upper-case Latin letter and has a fixed number of arguments. In practice only unary (one-place) or binary (two-placed) connectives are frequently used. Propositional variables are lower-case Latin letters. Well-formedness of propositional formulas is then defined recursively:

1. A propositional variable standing alone is a well-formed formula (wff).
2. If $Z$ is an $n$-placed connective and $a_1, \ldots, a_n$ are $n$ wffs, then $Za_1 \ldots a_n$ is a wff.
3. Nothing else is a wff.

The most frequently employed connectives in this notation, with their infix counterparts, are given with their simplest formulas:

> | Name | Letter | Polish | Infix |
> | --- | --- | --- | --- |
> | Implication | $C$ | $Cpq$ | $(p \rightarrow q)$ |
> | Conjunction | $K$ | $Kpq$ | $(p \wedge q)$ |
> | Disjunction | $A$ | $Apq$ | $(p \vee q)$ |
> | Equivalence | $E$ | $Epq$ | $(p \leftrightarrow q)$ |
> | Sheffer Stroke | $D$ | $Dpq$ | $(p \mid q)$ |
> | Negation | $N$ | $Np$ | ${\sim}(p)$ |

The formulas $p \rightarrow (q \rightarrow r)$ and $(p \rightarrow q) \rightarrow r$ then correspond to $CpCqr$ and $CCpqr$ respectively, while a complex formula such as

$$ \begin{align} & (((p \rightarrow r) \wedge (q \rightarrow r)) \wedge ((p \rightarrow s) \wedge (q \rightarrow s)) \leftrightarrow ((p \vee q) \rightarrow (r \wedge s))) \end{align} $$

containing 43 symbols, twenty of them parentheses, is rendered *po polsku* as

$$ \begin{align} & EKKCprCqrKCpsCqsCApqKrs \end{align} $$

containing 23 symbols, every one of them meaningful.

There is a simple counting test for well-formedness of propositional formulas in Łukasiewicz notation. Starting at the beginning (left) of a formula with count 1, add 1 at each occurrence of a binary connective, subtract 1 at each propositional variable, and leave the count the same at each unary connective. A formula is well-formed if and only if the count reaches zero for the first time at the final propositional variable. In addition to its brevity and elegance, Łukasiewicz’s notation had the advantage, in an age between handwritten copy and computerized typesetting, of being writable on a normal typewriter without special symbols.

The symbolism takes a small effort to master, but once mastered, the notation affords quick insight into the structure of formulas. It is particularly effective for propositional calculus, at which Łukasiewicz and his students excelled. To non-adepts, it is less transparent. Józef Bocheński related (personal communication) that once when he went to visit Łukasiewicz in Warsaw before the war, Łukasiewicz conveyed him inside excitedly, indicated a complex formula, beginning something like ‘$CCC\ldots$’, and said, “Look at this beautiful and *self-evidently true* formula!” Clearly the formula’s truth was not immediately evident to the bemused Bocheński. The absence of compulsory parentheses does however allow the reader-friendly writer to highlight groups of letters by optional parentheses in order to bring out formula structure more clearly. This was practised particularly effectively by one notable user of Polish notation, Arthur Prior.

We employ the notation in this article when discussing Łukasiewicz’s results in propositional calculus and syllogistic. Nevertheless, despite its intrinsic merits, and although adopted by a number of logicians, Prior most eminent among them, Łukasiewicz’s notation has not become standard or even widespread. The notation is indeed much less helpful and effective when extended to predicate calculus, because the scope of a quantifier is not dictated by a formula’s other structure. It calls out for a delimitation of quantifier scope by brackets or other delimiters rather than struggling to maintain freedom from parentheses at all costs. In mathematical calculators and computer programming languages, the symmetrically related reverse Polish notation, where functors follow rather than precede their arguments, has seen implementation in Hewlett-Packard calculators and some programming languages. Despite again having its advantages and its passionate advocates, this notation too has suffered decline, as users voted with their feet for more traditional infix notation requiring parentheses.

Return to “Jan Łukasiewicz”.
