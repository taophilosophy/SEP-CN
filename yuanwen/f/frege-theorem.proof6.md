# frege-theorem — proof6（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/proof6.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof of the General Principle of Induction

Assume the antecedent of the principle, eliminating the defined notation for $\mathit{HerOn}(F,{}^{a}R^{+})$:

$Pa\amp \forall x,y(R^{+}(a,x)\amp R^{+}(a,y)\amp Rxy\rightarrow (Px\rightarrow Py))$

We want to show, for an arbitrary object $b$, that if $R ^{+}(a,b)$ then $Pb$. So assume $R^{+}(a,b)$. To show $Pb$, we appeal to Fact (7) about $R^{+}$ (in our subsection on the Weak Ancestral in §4):

$Fx\amp R^{+}(x,y)\amp \mathit{Her}(F,R)\rightarrow Fy$

Instantiate the variable $F$ in this Fact to the property $[\lambda z \, R^{+}(a,z)\amp Pz]$ (that there is such a property is guaranteed by the Comprehension Principle for Relations), and instantiate the variables $x$ and $y$ to the objects $a$ and $b$, respectively. The result (after applying *λ*-Conversion) is therefore something that we have established as true:

$R^{+}(a,a)\amp Pa\amp R^{+}(a,b)\amp \mathit{Her}([\lambda z \, R^{+}(a,z)\amp Pz], R)\rightarrow$     $R^{+}(a,b)\amp Pb$

So if we can establish the antecedent of this fact, we establish $Pb$. But we know that the first conjunct is true, by the definition of $R^{+}$. We know the second conjunct is true, by assumption. We know that the third conjunct is true, by further assumption. So if we can establish:

$\mathit{Her}([\lambda z \, R^{+}(a,z)\amp Pz], R)$,

we are done. But, by the definition of heredity, this just means:

$\forall x,y[Rxy\rightarrow ((R^{+}(a,x)\amp Px) \rightarrow (R^{+}(a,y)\amp Py))]$.

To prove this claim, we assume $Rxy$ and $R^{+}(a,x)\amp Px$ (to show $R^{+}(a,y)\amp Py$). But from the facts that $R^{+}(a,x)$ and $Rxy$, it follows from Fact (3) about $R^{+}$ (in our subsection on the Weak Ancestral) that $R^{*}(a,y)$. This implies $R^{+}(a,y)$, by the definition of $R^{+}$. But since we now have $R^{+}(a,x), R^{+}(a,y), Rxy$, and $Px$, it follows from the first assumption in the proof that $Py$.
