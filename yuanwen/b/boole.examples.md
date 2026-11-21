# boole — examples（supplement）

> （《boole》词条补充材料，源：plato.stanford.edu/entries/boole/examples.html）

#### Supplement to George Boole

## Examples

Now we look at a selection of examples from Boole’s two books to see just how his methods work.

### Aristotelian Logic

Boole used the following translations for the categorical propositions:

| Propositions | *MAL* (1847, p. 26) | *LT* (1854, p. 64) |   |
| --- | --- | --- | --- |
| $A$ | All $X$ is $Y$ | $x(1-y) = 0$ | $x = vy$ |
| $E$ | No $X$ is $Y$ | $xy = 0$ | $xy = 0$ |
| $I$ | Some $X$ is $Y$ | $v = xy$ | $vx = vy$ |
| $O$ | Some $X$ is not $Y$ | $v = x(1-y)$ | $vx = v(1-y)$ |

**Example 1.** A conversion by limitation argument:

| Argument | *MAL* (1847, p. 27) | *LT* (1854, p. 229) |
| --- | --- | --- |
| All $X$ is $Y$ | $x(1-y) = 0$ | $x = vy$ |
| Some $Y$ is $X$ | $x = vy$ | $vx = vy$ |

To justify this via the algebra of logic in *MAL*, Boole invoked an argument based on solving $x(1-y) = 0$ for $x$. It uses the method of division discussed below: from $x = 0/(1-y) = (0/0)y + (0/1)(1-y)$ one has $x = vy$. The reader of *MAL* must wait till near the end of the book to learn the details of this method.

In *LT* Boole simply multiplied the first equation by $v$ to obtain $vx = vvy = vy$.

**Example 2.** A categorical syllogism:

(This example appears in *MAL*, but with the letters and premises rearranged.)

| Argument | *MAL* (1847, p. 34) | *LT* (1854, p. 231) |
| --- | --- | --- |
| All $X$ is $Y$ | $x(1-y) = 0$ | $x = vy$ |
| All $Y$ is $Z$ | $y(1-z) = 0$ | $y = v'z$ |
| All $X$ is $Z$ | $x(1-z) = 0$ | $x = vv'z$ |

In *MAL* Boole used a weak elimination procedure (which happened to work in this case) to justify this. The full-strength elimination procedure, part of the General Method of *LT* described above, would proceed as follows:

| $x(1-y) + y(1-z) = 0$ | Reduction to a Single Equation |
| --- | --- |
| $[x(1-1) + 1(1-z)] [x(1-0) + 0(1-z)] = 0$ | Eliminate $y$ |
| $(1-z)x = 0$ | Simplify (ordinary algebra) |
| $x(1-z) = 0$ | Commute (ordinary algebra) |

In Chapter XV of *LT* Boole first gave a quick proof by simply substituting to obtain $x = v(v'z) = vv'z$, a secondary form he used to express “All $X$ is $Z$”. Then he stated a general result designed to cover all syllogisms, justified by applying his General Method. Boole did not give full details of a proof of this general result, which are rather demanding. Here are the details for how one applies Boole’s General Method to this particular example.

| $(x-vy)^2 + (y-v'z)^2 = 0$ | Reduction to a Single Equation |
| --- | --- |
| $[(x -v)^2 + (1-v'z)] [x + v'z] = 0$ | Eliminate $y$ |
| $(2 - v - v'z)x = 0$ | Simplify (ordinary algebra + idempotent law) |
| $x = (0/0)vv'z$ | Solve for $x$ by division |

So the conclusion equation would look like $x = wvv'z$, instead of $x = vv'z$ as given above.

**Example 3.** A hypothetical syllogism (the constructive conditional syllogism):

| Argument | *MAL* (1847, p. 56) | *LT* (1854) |
| --- | --- | --- |
| If $X$ then $Y$ | $x(1-y) = 0$ | — |
| $X$ | $x = 1$ | — |
| $Y$ | $y = 1$ | — |

The ad hoc justification is: just substitute $x = 1$ into the first equation.

Using the General Method of *LT* from Section 6.2 one has:

| $x(1-y) + (1-x) = 0$ | Reduction to a Single Equation |   |
| --- | --- | --- |
| $1-xy = 0$ | Simplify (ordinary algebra) |   |
| $1(1-y) = 0$ | Eliminate $x$ |   |
| $y = 1$ | Simplify (ordinary algebra) |   |

**Example 4.** Another hypothetical syllogism (the non–exclusive disjunctive syllogism):

| Argument | *MAL* (1847, p. 56) | *LT* (1854, p. 169,170) |
| --- | --- | --- |
| $X$ or $Y$ is true | $x + y - xy = 1$ | $x(1-y) + y(1-x) = 1$ |
| $X$ is false | $x = 0$ | $x = 0$ |
| $Y$ is true | $y = 1$ | $y = 1$ |

(Boole did not state this particular example in *LT*; the right column above gives the algebraic translations in *LT* of the propositions on the left.)

### A substantial example from *LT*

The following example in Chapter VII of *LT* (pp. 106–112) gives a better illustration of the workings of the General Method. Boole considered the following definition of wealth [*LT* p. 106]:

> Wealth consists of things transferable, limited in supply, and either productive of pleasure or preventive of pain.

Then he used the following symbols to denote the 5 classes in this proposition:

| Symbol | Proposition |
| --- | --- |
| $W$ | the class of things that constitute wealth |
| $T$ | the class of things that are transferable |
| $S$ | the class of things that are limited in supply |
| $P$ | the class of things that are productive of pleasure |
| $R$ | the class of things that are preventitive of pain. |

He put the above definition of wealth in equational form [*LT* p. 106]:

$$ w = st(p + r(1-p)) $$

Six questions were posed and answered by Boole, the first two being:

1. “What is the expression for $w$ in terms of $p, s$ and $t$ after eliminating $r$?” [*LT* pp. 106–107, 112]

2. “What is the expression for $s$ in terms of $w, p$ and $t$ after eliminating $r$?” [*LT* pp. 107–110]

Boole answered these two as follows, where intermediate steps that Boole skipped over have been added — an asterisk (\*) follows each equation that is stated exactly as in *LT*:

| 1. | $w - st (p + r- rp ) = 0$ | (\*) write premiss as: *something* $ = 0$ |
| --- | --- | --- |
| 2. | $(w - st ) (w - stp ) = 0$ | (\*) eliminate $r$ in 1 |
| 3. | $w^2 - wstp -stw + s^2 t^2 p = 0$ | Multiply out 2 |
| 4. | $w - wstp - wst + stp = 0$ | (\*) Simplify 3 |
| 5. | $(1 - st)w + pst(1-w) = 0$ | (\*) expand 4 with respect to $w$ |
| 6. | $(1 - st)w = 0$, and $pst(1-w) = 0$ | (\*) terms in 5 are disjoint |

Boole translated 6 as:

> Wealth is limited in supply and transferable, and that which is productive of pleasure and limited in supply and transferable is wealth.

| 7. | $w(1 - st - stp) + stp = 0$ | from 4, by ordinary algebra |
| --- | --- | --- |
| 8. | $w = stp/(st+stp - 1) = stp + (0/0)st(1- p)$ | solve 7 for $w$ by division |

Boole translated 8 as:

> Wealth consists of all things limited in supply, transferable, and productive of pleasure, and an indefinite remainder of things limited in supply, transferable, and not productive of pleasure.

| 9. | $s = w/(wt + wtp - tp) =$ $wtp + wt(1- p)\ +$ $(1/0)w(1-t)p\ +$ $(1/0)w(1- t)(1- p)\ +$ $0(1-w)tp\ +$ $(0/0)(1- w)t(1-p)\ +$ $(0/0)(1-w)(1-t)p\ +$ $(0/0)(1-w)(1-t)(1-p)$ | (\*) finish division process |
| --- | --- | --- |
|   | $0 = w(1-t)p$ $0 = w(1-t)(1-p)$ | (\*) 2 side conditions |

Boole translated the expression for $s$ and the two side conditions of 9 as:

> All wealth transferable and productive of pleasure—all wealth transferable, and not productive of pleasure,—an indefinite amount of what is not wealth, but is either transferable, and not productive of pleasure, or intransferable and productive of pleasure, or neither transferable nor productive of pleasure.
