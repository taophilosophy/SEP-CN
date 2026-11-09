# frege-theorem — WAfact6（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/WAfact6.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof of Fact 6 Concerning the Weak Ancestral

Fact 6 concerning the weak ancestral $R^{+}$ of $R$ asserts:

**Fact 6**: $R^{*}(x,y)\rightarrow \exists z[R^{+}(x,z) \amp Rzy]$

To prove this, we shall appeal to Fact 3 concerning the strong ancestral $R^{*}$ of $R$:

**Fact 3**: $[R^{*}(x,y)\amp \forall u(Rxu\rightarrow Fu)\amp \textrm{Her}(F,R)]\rightarrow Fy$,

for any concept $F$ and objects $x$ and $y$:

Now to prove Fact 6 about the weak ancestral, assume $R^{*}(a,b)$. We want to show:

$\exists z[R^{+}(a,z) \amp Rzb]$

Notice that by $\lambda$-Conversion, it suffices to show:

$[\lambda w\, \exists z[R^{+}(a,z) \amp Rzw]]b$

Let us use ‘$P$’ to denote this concept under which $b$ should fall. Notice that we can prove $Pb$ by instantiating Fact 3 (above) concerning the strong ancestral to $P$, $a$, and $b$ and establishing the antecedent of the result. In other words, by Fact 3, we know:

$[R^{*}(a,b)\amp \forall u(Rau\rightarrow Pu)\amp \textrm{Her}(P,R)]\rightarrow Pb$

So if we can show the conjuncts of the antecedent, we are done. The first conjunct is already established, by hypothesis. So it remains to show:

(1)   $\forall u(Rau\rightarrow Pu)$ (2)   $\textrm{Her}(P,R)$

To see what we have to show for (1), we expand the definition of $P$ and simplify by using $\lambda$-Conversion. Thus, we have to show:

(1)   $\forall u[Rau\rightarrow \exists z(R^{+}(a,z) \amp Rzu)]$

So assume $Rau$, to show $\exists z(R^{+}(a,z) \amp Rzu)$. But it is an immediate consequence of the definition of the weak ancestral $R^{+}$ that $R^{+}$ is reflexive. (This is Fact 4 concerning the weak ancestral, in Section 4, “The Weak Ancestral of $R$”.) So we may conjoin and conclude $R^{+}(a,a)\amp Rau$. From this, we may infer $\exists z(R^{+}(a,z) \amp Rzu)$, by existential generalization, which is what we had to show.

To show (2), we have to show that $P$ is hereditary on $R$. If we expand the definitions of $\textrm{Her}(P,R)$ and $P$ and simplify by using $\lambda$-Conversion, then we have to show, for arbitrarily chosen objects $x,y$:

(2)   $Rxy\rightarrow [\exists z(R^{+}(a,z) \amp Rzx)\rightarrow \exists z(R^{+}(a,z) \amp Rzy)]$

So assume

(A)   $Rxy $ (B)   $\exists z(R^{+}(a,z)\amp Rzx)$

to show: $\exists z(R^{+}(a,z)\amp Rzy)$. From (B), we know that there is some object, say $d$, such that:

$R^{+}(a,d)\amp Rdx$

So, by Fact 3 about the weak ancestral (Section 4, “The Weak Ancestral of $R$”), it follows that $R^{*}(a,x)$, from which it immediately follows that $R^{+}(a,x)$, by definition of $R^{+}$. So, by conjoining (A), we have:

$R^{+}(a,x) \amp Rxy$

But since $x$ was arbitrarily chosen, it follows that:

$\exists z(R^{+}x(a,z) \amp Rzy)$,

which is what we had to show.

Return to Frege’s Theorem and Foundations for Arithmetic
