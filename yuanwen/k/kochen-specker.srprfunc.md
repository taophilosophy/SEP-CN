# kochen-specker — srprfunc（supplement）

> （《kochen-specker》词条补充材料，源：plato.stanford.edu/entries/kochen-specker/srprfunc.html）

#### Supplement to The Kochen-Specker Theorem

## Derivation of Sum Rule and Product Rule from FUNC

The three principles, in full detail, are:

> **FUNC:** Let **A** be a self-adjoint operator associated with observable *A*, let *f*: **R**→**R** be an arbitrary function, such that **f(A)** is a self-adjoint operator, and let | φ> be an arbitrary state; then **f(A)** is associated uniquely with an observable *f*(*A*) such that:
>
> > *v*(*f*(*A*))^{|φ>} = *f*(*v*(*A*))^{|φ>}
>
> **Sum Rule:** If **A** and **B** are commuting self-adjoint operators corresponding to observables *A* and *B*, respectively, then *A* + *B* is the unique observable corresponding to the self-adjoint operator **A + B** and
>
> > *v*(*A* + *B*)^{|φ>} = *v*(*A*)^{|φ>} + *v*(*B*)^{|φ>}
>
> **Product Rule:** If **A** and **B** are commuting self-adjoint operators corresponding to observables *A* and *B*, respectively, then if *A* · *B* is the unique observable corresponding to the self-adjoint operator **A** · **B** and
>
> > *v*(*A**B*)^{|φ>} = *v*(*A*)^{|φ>} · *v*(*B*)^{|φ>}

In order to derive Sum Rule and Product Rule from FUNC, we use the following mathematical fact: Let **A** and **B** be commuting operators, then there is a maximal operator **C** and there are functions *f*, *g* such that **A** = *f*(**C**) and **B** = *g*(**C**).

So, for two commuting operators **A**, **B**:

> Since **A** = *f*(**C**) and **B** = *g*(**C**), there is a function *h* = *f*+*g*, such that **A + B** = *h*(**C**).

Therefore:

> | *v*(*A* + *B*)^{\|φ>} | = | *h*(*v*(*C*)^{\|φ>}) |   | (by FUNC) |
> | --- | --- | --- | --- | --- |
> |   | = | *f*(*v*(C)^{\|φ>}) + *g*(*v*(C)^{\|φ>}) |   |   |
> |   | = | *v*(*f*(*C*))^{\|φ>} + *v*(*g*(*C*))^{\|φ>} |   | (by FUNC) |
> |   | = | *v*(*A*)^{\|φ>} + *v*(*B*)^{\|φ>} |   | (Sum Rule) |

Similarly:

> Since **A** = *f*(**C**) and **B** = *g*(**C**), there is a function *k* = *f*·*g*, such that **A**·**B** = *k*(**C**).

Therefore:

> | *v*(*A* · *B*)^{\|φ>} | = | *k*(*v*(*C*)^{\|φ>}) |   | (by FUNC) |
> | --- | --- | --- | --- | --- |
> |   | = | *f*(*v*(*C*)^{\|φ>}) · *g*(*v*(*C*)^{\|φ>}) |   |   |
> |   | = | *v*(*f*(*C*))^{\|φ>} · *v*(*g*(*C*))^{\|φ>} |   | (by FUNC) |
> |   | = | *v*(*A*)^{\|φ>} · *v*(*B*)^{\|φ>} |   | (Product Rule) |

Return to The Kochen-Specker Theorem
