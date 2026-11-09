# pm-notation — dots（supplement）

> （《pm-notation》词条补充材料，源：plato.stanford.edu/entries/pm-notation/dots.html）

#### Supplement to The Notation in *Principia Mathematica*

## The Use of Dots for Punctuation and for Conjunction in *Principia Mathematica*

The paragraph on “The use of dots”, on pp. 9–11 of the Introduction to *Principia Mathematica*, is quite condensed, but it in fact states a precise rule. The first sentences set up the distinction between dots around sentence connectives and other symbols, and dots indicating conjunctions. The “general principle” is that a larger number of dots indicates a larger subformula. The dots come in three “groups”, or kinds, with Group I surrounding connectives and the = of definitions. Group II consists of dots following quantifiers, and other variable binding expressions. Lastly, Group III dots “indicate” a conjunction. The Groups are ordered by “force” in the order I, II, and III. With these preliminary identification of three “groups” of uses of dots and the relative “force” of those groups, the statement of the rule is completed in the last two sentences of the paragraph. Using short descriptive names for each component of this account the six key sentences in the paragraph are:

1. Group I consists of dots adjoining a sign of implication ($\supset$) or of equivalence $(\equiv)$ or of disjunction $(\vee)$ or of equality by definition (= Df).
2. Group II consists of dots following brackets indicative of an apparent variable, such as $(x)$ or $(x,y)$ or $(\exists x)$ or $(\exists x,y)$ or $[(\atoi x)(\phi x)]$ or analogous expressions.
3. Group III consists of dots which stand between propositions in order to indicate a logical product.
4. Force: Group I is of greater force than Group II, and Group II than Group III.
5. Scope: The scope of the bracket indicated by any collection of dots extends backwards or forwards beyond any *smaller* number of dots, or any *equal* number from a group of less force, until we reach either the end of the asserted proposition or a *greater* number of dots or an *equal* number belonging to a group of equal or superior force.
6. Direction: Dots indicating a logical product have a scope which works both backwards and forwards; other dots only work away from the adjacent sign of disjunction, implication, or equivalence, or forward from the adjacent symbol of one of the other kinds enumerated in Group II.

This paragraph describes precise rule, even if quite compressed. Examination of its details by Alan Turing (1942) reveal an algorithm for the “Scope” and “Direction” rules replacing dots by brackets and parentheses. (One can easily imagine a Turing Machine moving left and right over the formula, picking up dots and dropping right and left parentheses as required.) The general structure of this algorithm resolves the apparent problem presented by the dual use of dots for conjunction and punctuation in PM.

The key to following the algorithm is to realize that the dots for conjunction are flanked by formulas and no other use of a dot involves formulas on each side. There are three steps in replacing a formula with dots with something familiar in modern notation: (1) Assign the dots to groups (2) apply the Scope and Direction rules to introduce opening and closing brackets with the right scope and (3) to get a formula in modern notation either introduce a connective such as ‘$\amp$’ for conjunction *or*, alternatively, delete the Group III dots for a system which expresses conjunction with juxtaposition, and, finally, (4) eliminate excessive brackets following familiar conventions. The procedure is illustrated with the “definition” of conjunction:

$$ \tag*{∗3·01} p \ldot q \ldot {=} \ldot \sim ( \sim \! p\; \vee \sim \! q) \quad\text{Df.} $$

(1) Assign the dots to Groups by subscripting each group of dots with the appropriate numeral.

$$ \; p \: ._{\mathrm{III}} \: q \;._{\mathrm{I}} = ._{\mathrm{I}} \; \sim ( \sim \! p \; \vee \sim \! q) \quad\text{Df.} $$

The first dot must belong to Group III rather than Group I because this is the only use of dots flanked on both sides by formulas. Group I and Group II dots have either a binary sentential connective to one side or are preceded by a quantifier or description operator, etc.

(2) Apply the Scope and Direction rules by introducing left and right parentheses, to indicate the beginning and ending, respectively, of the scope of a dot:

$$ (( p ) . ( q ) ) = ( \sim ( \sim \! p \; \vee \sim \! q) )\quad\text{Df.} $$

The redundant parentheses around the propositional variables $p$ and $q$ in the subformula $(( p ) \ldot ( q ) )$ are required by the condition that “Dots indicating a logical product have a scope which works both backwards and forwards ….” That the scope can be “working” both forwards and backwards is indicated with the closing and opening parentheses flanking the dot for conjunction. In general the “direction” rule for interpreting a formula ‘$A \ldot B$’ will be to first indicate that the center dot “works both backwards and forwards” to give first ‘$A )\ldot(B$’ , and then the opening and closing parentheses are added to yield ‘$(A)\ldot(B)$’. The extra set of pairs of parentheses is then reduced to the formula $(A \ldot B)$.

To get a formula closer to contemporary notation, either

(3a) Use an ampersand ‘&’ for any Group III use of dots, replacing ‘$A ._{III} B$’, by ‘$( A \amp B)$’

and

(4) eliminate parentheses, including those flanking propositional variables, following conventions about the priority of connectives, to eliminate excess parentheses, and get:

$$p \amp q \; =_{\text{df}} \; \sim ( \sim \! p \; \vee \sim \! q)$$

*or*

(3b) Eliminate the Group III dots, replacing ‘$A ._{III} B$’, by ‘$(A) (B)$’

and

(4) eliminate excess parentheses to get:

$$p q \; =_{\text{df}} \; \sim ( \sim \! p \; \vee \sim \! q).$$

Turing suggests that one should say that in PM conjunction is still expressed by juxtaposition of expressions, with punctuation dots to indicate which expressions are juxtaposed in the expressions from which all dots are replaced by bracketing. Or perhaps we should say that in PM there is a phantom “auxiliary” connective symbol for conjunction. It doesn’t seem to make a big difference which way we go. (This is suggested by Haskell Curry in his 1937 article that is discussed in Turing 1942). Or perhaps we can just say that dots have two uses, one as a connective to indicate conjunction, and the second as punctuation, but these uses are consistent. These alternatives all make sense of the double use of dots for punctuation and conjunction.
