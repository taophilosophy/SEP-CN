# natural-deduction — figdesc（supplement）

> （《natural-deduction》词条补充材料，源：plato.stanford.edu/entries/natural-deduction/figdesc.html）

#### Supplement to Natural Deduction Systems in Logic

## Long descriptions for some figures in Natural Deduction Systems in Logic

### Figure 1 description

Figures 1, 2, and 3 are displaying the same proof in three different ways. Figure 1 displays it in Gentzen style which is tree like with the conclusion as the root and bottom. The following description is from the bottom up. Each line mentioned is either the length of the stuff (which could be root of several different branches) immediately above or the length of the item immediately below, whichever is longer. Each branch ends with a leaf: a statement with a crossed out number above it.

- “$(((p\rightarrow q) \land (\neg r\rightarrow \neg q))\rightarrow(p\rightarrow r))$” (the root and conclusion)
- above is a line labeled “$\rightarrow$-I (1)”
- above and centered is “$(p\rightarrow r)$”
- above is a line labeled “$\rightarrow$-I (2)”
- above and centered is “$r$”
- above is a line labeled “$\neg\neg$-E”
- above and centered is “$\neg\neg r$”
- above is a line labeled “$\neg$-I (3)”
- above and centered is “$\bot$”
- above is long line as two branches start. It is labeled “$\bot$-I”
- branch 1 on the left which starts with “$\neg q$”
- above is another long line as two more branches start. It is labeled “$\rightarrow$-E”
- branch 1.1 on the left which is “$\neg r$” with a crossed out 3 above it
- branch 1.2 on the right which starts with “$(\neg r\rightarrow \neg q)$”
- above is a line labeled “$\land$-E”
- above and centered is “$((p\rightarrow q) \land (\neg r\rightarrow \neg q))$” and a crossed out 1 above it
- branch 2 is on the right which starts with “$q$”
- above is another long line as two more branches start. It is labeled “$\rightarrow$-E”
- branch 2.1 on the left which is “$(p\rightarrow q)$”
- above is a line labeled “$\land$-E”
- above and centered is “$((p\rightarrow q) \land (\neg r\rightarrow \neg q))$” and a crossed out 1 above it
- branch 2.2 on the right which is “$p$” with a crossed out 2 above it

The paragraphs preceding and following the figure in the body give additional information.

### Figure 2 description

Figures 1, 2, and 3 are displaying the same proof in three different ways. Figure 2 displays it in the Jaśkowski style. This is a series of proof steps consisting of a number, a formula, and a rule with step numbers. .

- 1. $((p\rightarrow q) \land (\neg r\rightarrow \neg q))$ rule: Supposition [start of outermost box]
- 2. $p$ rule: Supposition [start of middle box]
- 3. $((p\rightarrow q) \land (\neg r\rightarrow \neg q))$ rule: 1 Reiterate
- 4. $(p\rightarrow q)$ rule: 3 Simplification
- 5. $q$ rule: 2,4 Modus Ponens
- 6. $(\neg r\rightarrow \neg q)$ rule: Simplification
- 7. $\neg r$ rule: Supposition [start of innermost box]
- 8. $(\neg r\rightarrow \neg q)$ rule: 6 Reiterate
- 9. $\neg q$ rule: 7,8 Modus Ponens
- 10. $q$ rule: 5 Reiterate [end of innermost box]
- 11. $r$ rule: 7–10 Reductio ad Absurdum [end of middle box]
- 12. $(p\rightarrow r)$ rule: 2–11 Conditionalization [end of outermost box]
- 13. $(((p\rightarrow q) \land (\neg r\rightarrow \neg q))\rightarrow(p\rightarrow r))$ rule: 1–12 Conditionalization [end of proof]

The paragraphs preceding and following the figure in the body give additional information.

### Figure 3 description

Figures 1, 2, and 3 are displaying the same proof in three different ways. Figure 3 displays it in the Fitch style. The number of each step is on the far left. A sublist indicates a subproof and each subproof has a vertical line on the left for the full height of the subproof (the step numbers as to the left of this). The words “fitch bar” indicate a short horizontal bar between the preceding and succeeding lines. The word “rule:” doesn't actually appear but indicates what follows, the rule, is on the far right.

- 
- 1 $((p\rightarrow q) \land (\neg r\rightarrow \neg q))$
- fitch bar
- 2 $p$
- fitch bar
- 3 $((p\rightarrow q) \land (\neg r\rightarrow \neg q))$ rule: 1, R
- 4 $(p\rightarrow q)$ rule: 3, $\land$E
- 5 $q$ rule: 2,4, $\rightarrow$E
- 6 $(\neg r\rightarrow \neg q)$ rule: 3, $\land$E
- 7 $\neg r$
- fitch bar
- 8 $(\neg r\rightarrow \neg q)$ rule: 6, R
- 9 $\neg q$ rule: 7,8, $\rightarrow$E
- 10 $q$ rule: 5, R
- 11 $\neg\neg r$ rule: 7–10, $\neg$I
- 12 $r$ rule: 11, $\neg\neg$E
- 13 $(p\rightarrow r)$ rule: 2–12, $\rightarrow$I
- 14 $(((p\rightarrow q) \land (\neg r\rightarrow \neg q))\rightarrow(p\rightarrow r))$ rule: 1–13, $\rightarrow$I

The paragraphs preceding and following the figure in the body give additional information.

### Figure 4 description

Three Fitch style proofs. The first (a) is

- 1 $\neg(\phi\land\psi)$
- 2 ⋮
- 3 $(\neg\phi\lor\neg\psi)$ rule: $\neg\land$-E

The second (b) is

- 1 $\neg(\phi\lor \psi)$
- 2 ⋮
- 3 $(\neg \phi\land\neg \psi)$ rule: $\neg\lor$-E

The third (c) is

- 1 $\neg(\phi\rightarrow \psi) $
- 2 ⋮
- 3 $(\phi\land\neg \psi)$ rule: $\neg\rightarrow$-E

### Figure 6 description

These two figures each have two Fitch style proofs aligned horizontally and separated by the words “REDUCES TO $\Rightarrow$”. The first (a) has

- 1 $A$
- 2 $B$
- 3 $A\land B$ rule: 1,2, $\land$-I
- 4 $A$ rule: 3, $\land$-E
- 5 $C$ rule: (from 4 somehow)

Reduces to $\Rightarrow$

- 1 $A$
- 2 $B$
- 3 $C$ rule: (same rule as before, now applied to 1)

The second (b) has

- 1 $A$
- 2 $A\lor B$ rule: 1, $\lor$-I
- 3 $A$ rule: hyp
- fitch bar
- 4 ⋮
- 5 $C$ [end of subproof]
- 6 $B$ rule: hyp
- fitch bar
- 7 ⋮
- 8 $C$
- 9 $C$ rule: 2, 3–5,6–8, $\lor$-E

Reduces to $\Rightarrow$

- 1 $A$
- 2 ⋮
- 3 ⋮ rule: (using same steps as 1st subproof of original)
- 4 $C$

### Figure 7 description

A Fitch style proof reduced to another Fitch style proof:

- i $A\lor B$
- ⋮
- j $A$ rule: hyp
- fitch bar
- ⋮
- k $C$ [end of subproof]
- m $B$ rule: hyp
- fitch bar
- ⋮
- n $C$
- n+1 $C$ rule: i,j–k,m–n, $\lor$-E
- n+2 $D$ rule: n+1, using an Elim-rule

Reduces to $\Rightarrow$

- i $A\lor B$
- ⋮
- j $A$ rule: hyp
- fitch bar
- ⋮
- k $C$ [end of subproof]
- k+1 $D$ rule: 4, using an Elim-rule
- m $B$ rule: hyp
- fitch bar
- ⋮
- n $C$
- n+1 $D$ rule: 8, using an Elim-rule
- n+2 $D$ rule: i,j–k+1,m–n+1, $\lor$-E

### Figure 8 description

This is another set of two Fitch proofs where the first reduces to the second.

- ⋮
- i $\neg C$
- fitch bar
- ⋮
- $B$
- j $\neg B$
- j+1 $C$ rule: i–j, Indirect Proof
- ⋮
- k $D$ rule: (from j+1, by some elimination rule)

Reduces to $\Rightarrow$

- ⋮
- i $\neg D$ rule: hypothesis
- fitch bar
- i+1 $C$ rule: hypothesis
- fitch bar
- ⋮
- j $D$ rule: (from i+1 by the elimination rule)
- j+1 $\neg D$ rule: i, Reiteration
- j+2 $\neg C$ rule: (i+1)–(j+1), $\neg$-I
- ⋮ rule: (like steps in left subproof)
- $B$
- k $\neg B$
- k+1 $D$ rule: i–k, Indirect proof

### Figure 9 description

Two Gentzen style proofs. The first (a) starting from the bottom going up is

- $A$
- above is a line labeled (TONK-Elim-L)
- above and centered is $(A \tonk B)$

The second (b) starting from the bottom going up is

- $B$
- above is a line labeled (TONK-Elim-R)
- branch 1: above and to the left is $(A \tonk B)$
- branch 2: above and to the right is $B$
- above is ⋮
- above is $[A]$

### Figure 10 description

A Gentzen style proof. Describing from the bottom up:

- $(A \tonk B)$
- above is a line labeled (TONK-I)
- branch 1 above and to the left is $A$
- branch 2 above and to the left is $B$
- above is ⋮
- above is $[A]$

### Figure 11 description

Two Gentzen style proofs. The first (a) described from the bottom up is

- $a=a$
- above is a line labeled ($=$-Intro)

The second (b) described from the bottom up is

- $\Phi(b)$
- above is a line labeled ($=$-Elim)
- branch 1: above and to the left is $a=b$
- branch 2: above and to the right is $\Phi(a)$

### Figure 12 description

Two Gentzen style proofs. The first (a) described from the bottom up is

- $a=b$
- above is a line labeled ($=$-Intro)
- above is $F(b)$
- above is ⋮
- above is $[F(a)]$

The second (b) described from the bottom up is

- $F(b)$
- above is a line labeled ($=$-Elim)
- branch 1: above and to the left is $a=b$
- branch 2: above and to the right is $F(a)$

### [Figures in note 24](notes.html#note-note24figa) description

Note 24 has five Gentzen style proofs.

Figure (a):

- *ψ*
- above is a line labeled (LEM)
- branch 1: above and to the left is *ψ*
- above is ⋮
- above is $[\phi]$
- branch 2: above and to the right is *ψ*
- above is ⋮
- above is $[\neg \phi]$

Figure (b):

- *φ*
- above is a line labeled $(\neg\neg E)$
- above is $\neg\neg \phi$

Figure (c):

- *φ*
- above is a line labeled (Indirect)
- above is $\neg\psi$
- above is ⋮
- above is *ψ*
- above is ⋮
- above is $[\neg \phi]$

Figure (d):

- *φ*
- above is a line labeled (Pierce)
- above is *φ*
- above is ⋮
- above is $[\phi\supset\psi]$

Figure (e):

- $\psi \supset \phi$
- above is a line labeled (Contraposition)
- above is $\neg \psi$
- above is ⋮
- above is $[\neg \phi]$

### [Figures in note 25](notes.html#note-note25figa) description

Six Fitch style proofs.

Figure (a):

- 1 $A$
- 2 ⋮
- 3 $(A \tonk B)$ rule: TONK-I

Figure (b):

- 1 $(A \tonk B)$
- 2 ⋮
- 3 $A$ rule: TONK-E-L

Figure (c):

- 1 $(A \tonk B)$
- 2 $A$
- fitch bar
- 3 ⋮
- 4 $B$
- 5 ⋮
- 6 $B$ rule: TONK-E-R

Figure (d):

- 1 $A$
- 2 $A$
- fitch bar
- 3 ⋮
- 4 $B$
- 5 ⋮
- 6 $(A \tonk B)$ rule: TONK-I

Figure (e) (which is the same as (b)):

- 1 $(A \tonk B)$
- 2 ⋮
- 3 $A$ rule: TONK-E-L

Figure (f):

- 1 $(A \tonk B)$
- 2 ⋮
- 3 $B$ rule: TONK-E-R
