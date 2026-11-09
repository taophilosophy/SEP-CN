# recursive-functions — ackermann-peter（supplement）

> （《recursive-functions》词条补充材料，源：plato.stanford.edu/entries/recursive-functions/ackermann-peter.html）

#### Supplement to Recursive Functions

## History of the Ackermann and Péter functions

Textbook presentations sometimes suggest that the functions which now bear the names of Wilhelm Ackermann and Rózsa Péter were directly presented as examples of intuitively computable functions which are not primitive recursive.[^note-34] Such an understanding overlooks the context of the papers Ackermann 1928b and Péter 1935 in which these functions were introduced as well as the subsequent work on forms of recursion which they inspired. The goal of this supplement is to provide a brief account of these developments which, while significant in their own right, lie off the main branch of computability theory after the 1930s.

The first published presentation of a function similar to what we called the *Péter function* in the main text appears to have been given by Hilbert in his well-known address “On the infinite” (1926). This corresponds to the text of a lecture he delivered in Münster in 1925 which in turn draws on a lecture course (1925) of the same name he delivered in Göttingen in 1924–1925. The published address is often cited as an overview of Hilbert’s finitary standpoint and goal of proving the consistency of infinitary mathematics by finite means. A more extensive treatment was later provided in *Grundlagen der Mathematik* (1934: §2), where Hilbert and Bernay stress the finitary character of primitive recursive definitions.

Recursion is also an important topic in (1926) and Hilbert’s treatment makes clear that he and his collaborators had taken substantial steps towards developing a general theory of recursive definability. But in neither this address nor the lectures on which it is based does he directly suggest that primitive recursion can be used to characterize finitary mathematics. Rather, Hilbert simply assumes that functions defined by primitive recursion will be regarded as finitary in the course of suggesting that such definitions may play a role in addressing questions from transfinite set theory. In particular, Hilbert’s original introduction (under a different description) of what is now called “the Ackermann function” occurs within the context of his attempted proof of the Continuum Hypothesis (CH).[^note-35]

In this setting Hilbert begins by distinguishing what he calls *ordinary recursion* from transfinite recursion. Ordinary recursion is characterized informally as the means by which

> a function of a number-theoretic variable $n$ is defined when we indicate what value it has for $n = 0$ and how the value for $n +1$ is obtained from that for $n$. (1926 [1967: 386])

As the examples he provides make clear, this form subsumes what we now call primitive recursion.[^note-36] Hilbert then characterizes transfinite recursion as generalizing the principle “that the value of the function for a value of the variable is determined by the preceding values of the function” from recursion on the natural numbers to ordinals in Cantor’s second number class.

Hilbert next discusses recursion at higher types and it is within this context that a description of the Ackermann function first appears. Hilbert begins by introduces a hierarchy of what Ackermann would later call *function types*: type 0 is taken to be that of natural numbers, type 1 that of functions from natural numbers to natural numbers, type 2 is that of functions from type 1 functions to type 1 functions, etc. Hilbert next reprises the definitions of type 1 functions denoted in the main text by $\alpha_1(x,y)$ (addition), $\alpha_2(x,y)$ (multiplication), $\alpha_3(x,y)$ (exponentiation), $\ldots$ and observes that they may all be defined by ordinary recursion. He next notes that the uniformly defined function $\alpha_n(x,y)$—wherein the position $n$ in the sequence is now itself understood as a variable—cannot be defined by in this manner. On the other hand, he also provides a definition similar to (\ref{ackdef1}) below which shows how this function can be defined by recursion on a type 1 variable. Part of Hilbert’s approach to proving CH relied on his characterization of the continuum as class of functions of type $\mathbb{N} \rightarrow \mathbb{N}$ obtainable by recursion at higher types. Since $\alpha_x(x,x)$ can be regarded as a function of a single numerical variable $x$, the original role of this example was thus to illustrate that this class is not exhausted by functions definable by ordinary recursion.

Already at this time Hilbert attributed this result to Ackermann.[^note-37] However a precise statement and proof would only appear three years later in Ackermann’s paper “On Hilbert’s construction of the real numbers” (1928b). Ackermann (1928b [1967: 495]) begins by presenting a notational variant of Hilbert’s example which takes the following form:

$$\begin{align} \label{ackdef1} \varphi(x, y, 0) & = x + y\\ \nonumber \varphi(x, y, n + 1) & = \rho_{z}(\varphi(x, z, n), \alpha(x, n), y) \\ \end{align} $$

where

$$\begin{align}\label{ackdef2} \rho_{z}(f(z), v, 0) & = v \\ \nonumber \rho_{z}(f(z), v, n + 1) & = f(\rho_{z}(f(z), v, n)) \end{align} $$

and

$$\begin{equation} \alpha(x, n) = \begin{cases} 0 & \text{if }n = 0 \\ 1 & \text{if }n = 1 \\ x & \text{if } n \geqslant 2 \end{cases} \end{equation} \label{ackdef3} $$

The equations (\ref{ackdef1}) define $\varphi(x,y,z)$ by primitive recursion relative to the auxiliary function $\rho_z$. Note, however, that (\ref{ackdef2}) defines $\rho_z$ not by primitive ordinary recursion but rather by recursion on a type 1 function. In particular, $\rho_{z}(f(z), v, n )$ denotes the *n*-fold iteration of the function $f$ in which the variable $z$ is replaced with the argument $v$, i.e.,

$$\rho_{z}(f(z), v, n ) = \underbrace{f(\dots f}_{n \text{ times}} (v)\ldots)$$

In Ackermann’s notation, the subscript $z$ in $\rho_{z}$ thus plays the role of an abstraction operator so that its first argument would now be more conventionally denoted by $\lambda z.f(z)$. $\rho_z$ is thus itself a type 2 function—i.e., it has type $(\mathbb{N} \to \mathbb{N}) \to (\mathbb{N} \to (\mathbb{N} \to \mathbb{N}))$.

Ackermann next notes that the functions defined by $\varphi(0,x,y), \varphi(1,x,y), \varphi(2,x,y), \ldots$ do indeed give the sequence $\alpha_1(x,y), \alpha_2(x,y), \alpha_3(x,y), \ldots$ described by Hilbert—e.g.,

$$\tag{i}\varphi(x, y, 0) = x + y$$ $$\tag{ii} \begin{align*} \varphi(x,y,1) & = \rho_{z}(\varphi(x,z,0), \alpha(x,0), y) \\ & = \rho_{z}(\varphi(x,z,0), 0, y) \\ & = \rho_{z}(x + z, 0, y) \\ & = x + \rho_{z}(x + z, 0, y - 1) \\ & = x + \underbrace{(x +( \ldots +(x}_{y - 1 \text{ times}} + \rho_{z}(x + z, 0, 0)) \ldots)) \\ & = \underbrace{x + (x +( \ldots +(x}_{y \text{ times}} + 0)) \ldots)) \\ & = \underbrace{x + x + \ldots + x}_{y \text{ times}} \\ & = x \times y\\ \end{align*} $$ $$\tag{iii} \begin{align*} \varphi(x, y, 2) & = \rho_{z}(\varphi(x,z,1), \alpha(x,1), y) \\ & = \rho_{z}(\varphi(x,z,1), 1, y) \\ & = \rho_{z}(x \times z, 1, y) \\ & = x \times \rho_{z}(x \times z, 1, y - 1) \\ & = x \times \underbrace{(x \times( \ldots \times (x}_{y - 1 \text{ times}} \times \rho_{z}(x \times z, 1, 0)) \ldots)) \\ & = \underbrace{x \times (x \times ( \ldots \times (x}_{y \text{ times}} \times 1)) \ldots)) \\ & = \underbrace{x \times x \times \ldots \times x}_{y \text{ times}} \\ & = x^{y}.\\ \end{align*} $$

The goal of Ackermann’s paper was to demonstrate that the function $\varphi(x,x,x)$—i.e., that obtained by taking $x = y = z$ in (\ref{ackdef1}) which is itself of type 1—cannot be defined by ordinary recursion. This is accomplished by showing that $\varphi(x,x,x)$ grows more rapidly than any function defined by ordinary recursion—i.e., that for any such function $\psi(x)$, there exists $n_0$ such that for all $n > n_0$, $\varphi(n,n,n) > \psi(n)$.

In order to do so, Ackermann shows that although Hilbert originally defined $\varphi(x,y,z)$ by higher-order recursion using the functional $\rho_z$, the same function in extension can be defined by a form of recursion directly on the natural numbers which is more complex than ordinary recursion. In particular, the first two lemmas of Ackermann (1928b) jointly entail that this function is also given by the following definition:

$$\begin{align}\label{ackdef4} \varphi(x, y, 0) & = x + y \\ \nonumber \varphi(x, 0, n + 1) & = \alpha(x,n) \\ \nonumber \varphi(x, y + 1, n + 1) & = \varphi(x, \varphi(x,y,n+1), n) \end{align} $$

It is this definition which many subsequent authors identify as giving the *Ackermann function*.

While the arguments on the righthand size of (\ref{ackdef4}) are natural numbers, this definition does not conform to the primitive recursion scheme as the value of $\varphi(x,y+1,n+1)$ is defined relative to its prior values at *both* $y$ and $n$. In light of this, Ackermann originally referred to this as an instance of *simultaneous recursion*. His original argument that $\varphi(x,y,z)$ is not primitive recursive was somewhat involved. As such, subsequent presentations often demonstrate the existence of a function definable by simultaneous but not primitive recursion via the simpler example of the binary *Péter function* $\pi(x,y)$.

Recall that as presented in the main text this is given by

$$\begin{align}\label{pidef2} \pi(0,y) & = y + 1\\ \nonumber \pi(x+1,0) & = \pi(x,1)\\ \nonumber \pi(x+1,y+1) & = \pi(x,\pi(x+1,y))\\ \end{align} $$

This definition was presented by Péter (1935) (see also 1967: 9) and bears a similar relation to the function $\beta(i)$—which was defined in the main text in terms of the functional $\mathcal{Iter}$—as does (\ref{ackdef4}) to (\ref{ackdef1}). Relative to the terminology she subsequently introduced, the definition (\ref{pidef2}) is an instance of *nested double recursion*—i.e., it exemplifies two separate generalizations of primitive recursion which are both subsumed under Ackermann’s original term “simultaneous recursion”.

Double recursion is in turn an instance of *multiple* or *k*-recursion which was considered in the general case by Péter (1937). For double recursion (i.e., $k = 2$), the case for binary functions is given by the scheme

$$\begin{align}\label{double} \delta(0,y) & = \alpha_{1}(y) \\ \nonumber \delta(x + 1, 0) & = \alpha_{2}(x, \delta(x,k))) \\ \nonumber \delta(x+1, y + 1) & = \beta(x,y,\delta(x,\gamma(x,y)), \delta(x+1,y)) \\ \end{align} $$

where $\alpha_1,\alpha_2$ and $\gamma$ are previously given functions and $k$ is fixed. In order to calculate the value $\delta$ for the arguments $x+1,y+1$ we must thus first obtain its value for the pairs $\langle x,\gamma(x,y) \rangle$ and also $\langle x+1, y\rangle$. Note, however, that both of these pairs come before $\langle x+1,y+1 \rangle$ in the lexicographical ordering $\prec$ of $\mathbb{N} \times \mathbb{N}$—i.e., $\langle x_1,y_1 \rangle \prec \langle x_2,y_2 \rangle$ iff $x _1 ≤ x_2$ or $x_1 = x_2$ and $y_1 ≤ y_2$. Thus under the assumption that we can compute the value of $\gamma(x,y)$, (\ref{double}) can still be understood as specifying a finite inductive procedure for calculating the values of $\delta$.[^note-38] And in fact Péter (1937) showed that the generalization of (\ref{double}) to multiple recursion on $k$ variables with parameters does not lead outside the class of primitive recursive functions by showing that this procedure can be reduced to course of values recursion (see also 1967: 6).

In order to understand the generalization involved with nested recursion, (\ref{pidef2}) can be compared directly with (\ref{double}). The former can be considered as a case of the latter in which $\beta$ is the projection function which returns its third argument $\delta(x,\gamma(x,y))$. In the case of (\ref{double}) we assume that $\gamma(x,y)$ is a given function already known to be in the class under consideration. But in the case of (\ref{pidef2}), $\gamma(x,y)$ corresponds to $\pi(x+1,y)$—i.e., a substitution instance of the function which is itself being defined. It is in this sense which the definition exemplified by (\ref{pidef2}) is said to involve a form of recursion which is “nested” (*eingeschachtelte*). For although a calculation carried out by applying the clauses of (\ref{pidef2}) also follows the lexicographic order, when the first argument of $\pi$ decreases, the value of the second argument required to calculate $\pi(x+1,y+1)$ is not determined independently of the specification of function $\pi(x,y)$ itself. It is in this sense in which the definition of the Ackermann and Péter functions have subsequently been said to exhibit a form impredicativity which makes them inaccessible from Hilbert’s finitary standpoint (see, e.g., Tait 1961, 1968, 1981).[^note-39]

Nested recursion was introduced by Péter (1935) and is considered in relation to *k*- and transfinite recursion in Tait (1961), Péter (1967), and Rose (1984). The definitions (\ref{ackdef4}) and (\ref{pidef2}) can be understood to exemplify the following general scheme of double nested recursion formulated by Epstein and Carnielli (2008: 117):

$$\begin{align} f(0,y) & = g(y) \\ \nonumber f(x + 1, 0) & = j(x, f(x,k)) \\ \nonumber f(x+1, y + 1) & = h(x,y,f(x+1,y), f(x,j(x,y,f(x +1,y))))\\ \end{align} $$

for a fixed but arbitrary $k$. But again this scheme on its own does not necessarily lead out of the class of primitive recursive functions. In fact Péter (1956) shows that if $g$, $h$ and $j$ are primitive recursive, and $f(x,u) \leq r(x,u)$ where $r$ is also primitive recursive and $u$ is calculated by means of $j(x,y,f(x +1,y)$), then $f$ is also primitive recursive (see also 1967: 10).


## Notes（原文脚注，引自主文）

[^note-34]: 34. See, e.g., Cutland 1980: 46; Rogers 1987: 8–9: Soare 2016: 231–232.

[^note-35]: 35. Hilbert himself acknowledged that the proof he sketches is in need of further clarification. And while he attempted this in 1928, his proof is not regarded as having being been successful. For reconstructions and assessments see Péter (1967: 241–243), van Heijenoort (1967: 367–369), Dreben & Kanamori (1997), and Tait (2005: 49–50).

[^note-36]: 36. The expression “ordinary recursion” has not be retained in the literature. Kleene (1936c: 237–238) appears to have interpreted it as *coinciding* with primitive recursion. Nothing which Hilbert (1926) says contradicts this. However in a followup discussion to (1926), he would later make clear that while an ordinary recursive function takes its arguments in $\mathbb{N}$ (1928 [1967: 468]), such a function may return a countable ordinal in Cantor’s second number class (1928 [1967: 471]).

[^note-37]: 37. A similar result showing that the class of function definable by recursion on type 1 functions properly extends those definable by ordinary recursion was obtained contemporaneously by Sudan (1927) using a definition by transfinite recursion on countable ordinals. See Calude, Marcus, & Tevy (1979) for a comparison with the approach of Ackermann (1928b).

[^note-38]: 38. For instance, in order to compute the value of $\delta(2,1)$, we must first compute the values of $\delta(1, \gamma(1,0))$ and $\delta(2,0)$. These computations can be performed independently from one to another in the sense that it is possible to compute first $\delta(1, \gamma(1,0))$, and then $\delta(2,0)$, so as to respect the fact that the ordered pair $\langle 1, u \rangle$, where $u = \gamma(1,0)$, precedes the ordered pair $\langle 2,0 \rangle$ in the lexicographical order.

[^note-39]: 39. For in contrast to the computation of $\delta(2,1)$ described in the prior note, observe that $\pi(2,1) = \pi(1,\pi(2,0))$. Thus in order to compute its value we must first compute the value of $\pi(2,0)$—say that it is $u$—and then compute $\pi(1,u)$. Note, however, that $\langle 2,0 \rangle$ *follows* $\langle 1,u \rangle$ in the lexicographical ordering $\prec$. Thus in order to compute the value of $\pi(x + 1,y + 1)$ it is in general necessary to assume that this function is defined for pairs preceding $\langle x + 1,y + 1 \rangle$ defined in terms of $\pi$ itself instead of those defined in terms of the known function in $\gamma$ in the case of $\delta(x+1,y+1)$.