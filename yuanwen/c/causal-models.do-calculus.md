# causal-models — do-calculus（supplement）

> （《causal-models》词条补充材料，源：plato.stanford.edu/entries/causal-models/do-calculus.html）

#### Supplement to Causal Models

## Supplement 2. The *do-*calculus

The *do*-calculus is an axiomatic system for replacing probability formulas containing the *do* operator with ordinary conditional probabilities. It consists of three axiom schemas that provide graphical criteria for when certain substitutions may be made.

Where $\bG$ is the ADMG on variable set $\bV$, and P satisfies (MC – *d*-separation), the rules are:

Rule 1 (Insertion/deletion of observations)

$\Pr(\bY\mid \ido(\bX), \bZ, \bW) = \Pr(\bY\mid \ido(\bX), \bW)$ if $\bY$ and $\bZ$ are *d*-separated by $\bX \cup \bW$ in $\bG^*$, the graph obtained from $\bG$ by removing all arrows pointing into variables in $\bX$.

Rule 2 (Action/observation exchange)

$\Pr(\bY\mid \ido(\bX), \ido(\bZ), \bW) = \Pr(\bY\mid \ido(\bX), \bZ, \bW)$ if $\bY$ and $\bZ$ are *d*-separated by $\bX \cup \bW$ in $\bG^{\dagger}$, the graph obtained from $\bG$ by removing all arrows pointing into variables in $\bX$ and all arrows pointing out of variables in $\bZ$.

Rule 3 (Insertion/deletion of actions)

$\Pr(\bY\mid \ido(\bX), \ido(\bZ), \bW) = \Pr(\bY\mid \ido(\bX), \bW)$ if $\bY$ and $\bZ$ are *d*-separated by $\bX \cup \bW$ in $\bG^{\ddagger}$, the graph obtained from $\bG$ by first removing all the arrows pointing into variables in $\bX$ (thus creating $\bG^*$) and then removing all of the arrows pointing into variables in $\bZ$ that are not ancestors of any variable in $\bW$ in $\bG^*$.

These are the rules as presented in Pearl 2009: 85–86. Pearl 1995: 686 presents an alternate formulation that is provably equivalent. Some find this formulation to be more intuitive and easier to work with. This formulation employs explicit intervention variables. If $X$ is a variable in a causal model, its corresponding intervention variable $I_X$ is an exogenous variable with one arrow pointing into $X$. The range of $I_X$ is the same as the range of $X$, with one additional value we can call “off”. When $I_X$ is off, the value of $X$ is determined by its other parents in the causal model. When $I_X$ takes any other value, $X$ takes the same value as $I_X$, regardless of the value of $X$’s other parents. If $\bX$ is a set of variables, then $I_\bX$ will be the set of corresponding intervention variables. We can re-write our three rules as follows:

Rule 1 (Insertion/deletion of observations)

$\Pr(\bY\mid \ido(\bX), \bZ, \bW) = \Pr(\bY\mid \ido(\bX), \bW)$ if $\bY$ and $\bZ$ are *d*-separated by $\bX \cup \bW$ in $\bG^*$, the graph obtained from $\bG$ by removing all arrows pointing into variables in $\bX$.

Rule 2 (Action/observation exchange)

$\Pr(\bY\mid \ido(\bX), \ido(\bZ), \bW) = \Pr(\bY\mid \ido(\bX), \bZ, \bW)$ if $\bY$ and $I_\bZ$ are *d*-separated by $\bX \cup \bZ \cup \bW$ in $\bG^{\dagger}$, the graph obtained from $\bG$ by removing all arrows pointing into variables in $\bX$ and all arrows pointing out of variables in $\bZ$.

Rule 3 (Insertion/deletion of actions)

$\Pr(\bY\mid \ido(\bX), \ido(\bZ), \bW) = \Pr(\bY\mid \ido(\bX), \bW)$ if $\bY$ and $I_\bZ$ are *d*-separated by $\bX \cup \bW$ in $\bG^*$, the graph obtained from $\bG$ by removing all arrows pointing into variables in $\bX$.

Huang & Valtorta (2006) and Shpitser & Pearl (2006) have independently proven this calculus to be complete, so that it characterizes all of the post-intervention probabilities that can be expressed in terms of simple conditional probabilities.

While the *do*-calculus requires at least a partial causal model, Zhang (2008) and Hyttinen et al. (2015) develop weaker versions that do not require knowledge of the causal structure. In essence, these calculi only appeal to causal structure that can be reliably inferred from the original probabilities.
