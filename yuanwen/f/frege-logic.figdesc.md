# frege-logic — figdesc（supplement）

> （《frege-logic》词条补充材料，源：plato.stanford.edu/entries/frege-logic/figdesc.html）

#### Supplement to Frege’s Logic

## Descriptions for some figures in Frege’s Logic

For alt text in the 200 or so images, we used a semi-translation of the latex commands in the latex package begriff that was used to create them. Most of the actual description is in section 2.1. A listing follows of the word used in the alt text, image (if any), meaning, and a description of the visual symbol:

**term**

indicates what text follows is content; the word term may be dropped if context makes it clear what is the content. Curly braces, {}, in the alt text may be used to indicate beginning and end of content. No visual symbol. (latex command \\BGterm)

**circumstance ![circumstance symbol](../assets/frege-logic/inline-circumstance.svg)**

short hand for “the circumstance that” or “the proposition that”. The circumstance symbol, also called a content stroke, is a horizontal line.. See section 2.1.1 description of judgement and circumstance symbols (latex command \\BGcontent)

**judgement ![judgement symbol](../assets/frege-logic/inline-judgement.svg)**

means a judgement symbol which is a vertical line, called a judgement stroke, with a horizontal line, same as the circumstance symbol, going from the center of it to the right. See section 2.1.1 description of judgement and circumstance symbols (latex command \\BGassert)

**conditional**

indicates that two terms will follow. Visually this is depicted with the second term above the first term. A short horizontal lines goes to the left of each term and these two horizontal lines are linked on their left by a vertical line. ![judgement conditional term B term A.](../assets/frege-logic/sec2-1-A.svg) The above figure has a judgement symbol with the horizontal line continuing to the right to $A$. A vertical line drops from the horizontal line and ends with a short horizontal line to the left that goes to $B$. $A,B$ line up vertically on the left. A conditions can itself be a term of another condition with the topmost lines forming a continuous line. ![conditional {term C} {term conditional term B term A}.](../assets/frege-logic/sec2-1-C.svg) The above figure has a horizontal line going to $A$ on the right. From the horizontal line drops two vertical lines. The first on the left ends with a short horizontal line to the left that goes to $C$. The second vertical line does not drop as far as the first and ends with a short horizontal line to the left that goes to $B$. $A,B,C$ line up vertically on the left. The outermost condition will usually have a circumstance or judgement symbol to the left with the horizontal line of those symbols continuing as the horizontal line of the second term of the outermost conditional. See section 2.1.2 description of conditional stroke. (latex command \\BGconditional)

**not ![not symbol](../assets/frege-logic/inline-not.svg)**

indicates a negation stroke (a short vertical line) on the horizontal line of the following circumstance, judgement, or term. “not not” ![not not symbol](../assets/frege-logic/inline-not-not.svg) indicates two negation strokes on the horizontal line. If the following is just an expression, e.g., “not not a equiv a”, then it indicates a short standalone horizontal line with the negation stroke(s) on it. See section 2.1.3 description of negation stroke. (latex \\BGnot).

**equiv $\equiv$**

a three lined equal sign meaning "same conceptual content" See section 2.1.4 description of identity operator.

**all gothic ![judgement all gothic a](../assets/frege-logic/inline-all-gothic-a.svg)**

The horizontal lines of the preceding judgement has a concavity with a gothic style letter in it. If there is nothing preceding, the concavity is in a short horizontal line. See section 2.1.5 on concavity. (latex \\BGall)

**definition ![definition](../assets/frege-logic/inline-definition.svg)**

like the judgement symbol but with two vertical lines on the left. See section 2.2 description of definition stroke. (latex \\BGdef)

**backslash $\backslash$**

a backslash. See section 3.2 description of backslash (latex \\fgebackslash)
