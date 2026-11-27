# kochen-specker — proofvc1（supplement）

> （《kochen-specker》词条补充材料，源：plato.stanford.edu/entries/kochen-specker/proofvc1.html）

#### Supplement to The Kochen-Specker Theorem

## Proof of VC1

We exploit two mathematical facts about projection operators *P*_{*i*}:

> (A) *P*_{*i*}² = *P*_{*i*} (the *P*_{*i*} are ‘idempotent’);
>
> (B) If H is a Hilbert space of denumerable dimension, and if the *P*_{*i*} are operators projecting on *q*ᵢ, where the set {*q*_{*i*}} forms an orthonormal basis of *H*, then Σ_{*i*} *P*_{*i*}=*I* (where *I* is the identity operator) (the *P*_{*i*} form ‘a resolution of the identity’).

Consider now an arbitrary state |ψ> and an arbitrary nondegenerate operator *Q* on H₃, its eigenvectors |*q*₁>, |*q*₂>, |*q*₃>, and projection operators *P*₁, *P*₂, *P*₃ whose ranges are the rays spanned by these vectors. The eigenvectors form an orthonormal basis, thus, by (B):

> *P*₁ + *P*₂ + *P*₃ = *I*

Now, *P*₁, *P*₂, *P*₃ are compatible, so from assumption KS2 (a) (Sum Rule):

> *v*(*P*₁) + *v*(*P*₂) + *v*(*P*₃) = *v*(*I*)

Now, from KS2 (b) (Product Rule) and (A):

> |   | *v*(*P*_{*i*})² = *v*(*P*_{*i*}²) = *v*(*P*_{*i*}) |
> | --- | --- |
> | ⇒ | *v*(*P*_{*i*}) = 1 or 0 |

Now, assume an observable *R* such that *v*(*R*) ≠ 0 in state |ψ>. From this assumption and KS2 (b) (Product Rule):

> |   | *v*(*R*) = *v*(*I* *R*) = *v*(*I*) *v*(*R*) |
> | --- | --- |
> | ⇒ | *v*(*I*) = 1 |

Hence:

> (VC1)  *v*(*P*₁) + *v*(*P*₂) + *v*(*P*₃) = 1

where *v*(*P*_{*i*}) = 1 or 0, for *i* = 1, 2, 3.

Return to The Kochen-Specker Theorem
