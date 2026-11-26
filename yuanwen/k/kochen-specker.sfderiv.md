# kochen-specker — sfderiv（supplement）

> （《kochen-specker》词条补充材料，源：plato.stanford.edu/entries/kochen-specker/sfderiv.html）

#### Supplement to The Kochen-Specker Theorem

## Derivation of STAT FUNC

The result is proved for a pure state and a non-degenerate discrete observable *A* with eigenvalues *a*_{*i*}.

We first rewrite the statistical algorithm for projection operators:

> (1) prob(*v*(*A*)^{| ψ>} = *a*_{*k*}) = Tr(*P*_{| *a*_{*k*}>} · *P*_{| ψ>})

For an arbitrary function f: **R** → **R** (where **R** is the set of real numbers) we define the function of an observable *A* as:

> *f*(*A*) =_{df} Σ_{*i*} *f*(*a*_{*i*}) *P*_{| *a*_{*i*}>}

Moreover, we introduce the characteristic function χ_{*a*} as:

> | χ_{*a*}(*x*) | = 1 for *x* = *a* |
> | --- | --- |
> |   | = 0 for *x* ≠ *a* |

As a result, we can rewrite a project operator *P*_{| *a*_{*k*}>} as:

> (2) *P*_{| *a*_{*k*}>} = χ_{*a*_{*k*}}(*A*)

and thus the statistical algorithm as:

> prob(*v*(*A*)^{| ψ>}=*a*_{*k*}) = Tr(χ_{*a*_{*k*}}(*A*) · *P*_{| ψ>})

We also use a simple mathematical property of characteristic functions:

> χ_{*a*}(*f*(*x*)) = χ_{*f*^{−1}(*a*)}(*x*)

whence we can also write:

> (3) χ_{*a*}(*f*(*A*)) = χ_{*f*^{−1}(*a*)}(*A*)

Then:

> | prob(*v*(*f*(*A*))^{\| φ>} = *b*) | = | Tr(*P*_{\| *b*>} · *P*_{\| *φ*>}) | (by (1)) |
> | --- | --- | --- | --- |
> |   | = | Tr(χ_{*b*}(*f*(*A*)) · *P*_{\| *φ*>}) | (by (2)) |
> |   | = | Tr(χ_{*f*^{−1}(*b*)}(*A*) · *P*_{\| *φ*>}) | (by (3)) |
> |   | = | Tr(*P*_{\| *f*^{−1}(*b*)>} · *P*_{\| *φ*>}) | (by (2)) |
> |   | = | prob(*v*(*A*)^{\| φ>} = *f*^{−1}(*b*)) | (by (1)) |

Hence:

> prob(*v*(*f*(*A*))^{| φ>} = *b*)    =    prob(*v*(*A*)^{| φ>} = *f*^{−1}(*b*))

Now since

> *v*(*A*) = *f*^{−1}(*b*)    ⇔    *f*(*v*(*A*)) = *b*,

we have

> prob(*v*(f(*A*))^{| φ>} = b)    =    prob(*f*(v(*A*))^{| φ>} = b)

which is STAT FUNC.

Return to The Kochen-Specker Theorem
