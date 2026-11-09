# russell-paradox — supplement（supplement）

> （《russell-paradox》词条补充材料，源：plato.stanford.edu/entries/russell-paradox/supplement.html）

#### Supplement to Russell’s Paradox

## Frege’s and Russell’s Ways Out of the Paradox

Recall that the notation ‘$\varepsilon f$’ is used for the extension of the concept (or function to truth values) $f(~)$, and recall Frege’s idea that (V) mandates the transformation of the generality of an identity between concepts into an identity between their extensions. His amendment to (V) is to allow an exception to the generality of an identity between concepts. More precisely, two extensions are identified even though their corresponding concepts *don’t* agree on their values for a certain argument —namely, the extensions in question— so long as they agree on every other argument:

> the extension of one concept coincides with that of another when every object that falls under the first concept, except the extension of the first concept, falls under the second concept likewise, and when every object that falls under the second concept, except the extension of the second concept, falls under the first concept likewise (G&B, pp. 242–3).

Recalling that ‘$f(x)$’ means that $x$ falls under the concept $f(~)$:

$$\tag{V$^\prime$} \varepsilon f= \varepsilon g\equiv \forall x[(x\ne\varepsilon f\wedge x \ne \varepsilon g)\rightarrow(f(x)=g(x))].$$

Regarding comprehension, because (V) and (NCF) are equivalent by the proofs given in the main text, the amendment of (V) to (V′) results in a corresponding restriction of (NCF) to a principle we will call (RCF). Moreover, these proofs make use of Frege’s notion of membership, which is now restricted so that $x \in_R y$ if and only if $x$ is distinct from $y$ and $y$ is the extension of a concept under which $x$ falls:

$$x \in_R y \equiv_{df} \exists f [x \ne y \wedge y =\varepsilon f \wedge f(x)].$$

Accordingly, (RCF) says that every concept determines a corresponding extension whose members are distinct from it and such that the concept applies to those members:

$$\forall f \exists y \forall x [x \in_R y \equiv x \ne y \wedge f(x)].$$

Notice that it remains the case that every concept determines an extension. But no extension is a member of itself, since this would violate the requirement that an extension’s members must be distinct from it. Frege hoped for this reason that his proposal evaded the contradiction.

However, several distinguished commentators have shown that this proposal also leads to paradox. (Indeed, Frege had already abandoned it before this was widely known.) Here we summarize an especially illuminating discussion due to Roy Cook (2019) before providing further citations.

Cook makes several observations about (V$^\prime$) in this context. First, (V$^\prime$) is not satisfiable in a domain containing more than two elements (Cook, 2019, theorem 15.2.11.) Second, (V$^\prime$) is satisfied in a domain of only one element (*op. cit.*, 15.2.12). Third, it is satisfiable in a domain containing only at most one (*op. cit.*, 15.4.6). So, (V$^\prime$) commits Frege to monism!

This result is obtained in modern higher-order logic. But Cook also shows that (V$^\prime$) in Frege’s own system is satisfiable only by at most one element (*op. cit.*15.4.13). But in Frege’s own system, there are at least two elements – the two truth values. Combining these facts yields another contradiction in Frege’s system.

See also (Geach,1956), the basic idea of which is already in (Geach and Black, 1952), (Quine, 1955), and (Burgess, 2005). (According to Geach, the core of the argument is due to Leśniewski as written up by Sobociński (1949/1984).)

We now turn to the part of Russell’s epic battle with his paradox that took place between 1904 and 1908. In this period his creativity and determination yielded his theory of descriptions, his substitutional theory of propositions and, ultimately, his mature theory of types. All of these are major achievements. While scholars may disagree about the details of exactly what Russell believed and when, all will agree with Landini that Russell’s battle with paradox and the

> evolution of *Principia* is one of the most engaging episodes in the history of ideas (2011, 15)

Not only does Russell explore different forms of logicism and different ways of blocking the diagonal arguments discussed in the main text; he also discovers and wrestles with issues about the nature of propositions that continue to dog contemporary structured propositions theorists.

What Russell (1903) calls “objective propositions” are complex structured entities that can contain worldly objects as arguments. They do not contain Fregean senses or modes of presentation of objects. The proposition that John Lennon was a member of the Beatles contains John Lennon himself. Further, the replacement of John Lennon by Paul McCartney results in a distinct proposition. This is because, for Russell, propositions are finely individuated by the principle that if a pair of propositions differ by a constituent, then they are distinct propositions. This property of being fine grained leads to the paradox about classes of propositions that is discussed in section 5 of the main text. And, as we will see, the possibility of substitution into the argument places of fine-grained propositions leads to yet another paradox.

As for propositional functions, according to Whitehead and Russell:

> By a ‘propositional function’ we mean something which contains a variable $x$, and expresses a proposition as soon as a value is assigned to $x$. That is to say, it differs from a proposition solely by the fact that it is ambiguous: it contains a variable of which the value is unassigned. (1910, 38).

Thus, propositional functions are not Frege’s functions to truth values; rather, they are ambiguous propositions containing an entity $x$ whose value can vary. Whereas the proposition that John Lennon was a member of the Beatles contains a definite object, the propositional function

$x$ was a member of the Beatles

is an ambiguous entity. Before proceeding further, note that there is a question about the logico-metaphysical status of the entity $x$ in the propositional function. Is $x$ a variable object? See (Russell, 1903, ch. VIII). It will become clear that this difficult issue can be side-stepped for the purposes of this discussion.

Russell’s work in 1904 was focused on ruling out propositional functions that allow diagonal arguments using the restrictions of the so-called zigzag theory (Urquhart, 1994, xxvi). The theory is so-called because given a propositional function $\Phi$ that purports to determine a class $u,$ diagonal arguments exploit “a certain zigzag quality,” that $x \not\in u$ when $\Phi x$, or $x \in u$ when ${\sim}\Phi x$ (Russell, 1907, 38):

$$(\exists x (\Phi x \wedge x \not\in u)) \vee (\exists x (x \in u \wedge{\sim}\Phi x)).$$

Avoiding this requires that the formula expressing a given propositional function must have a certain logical simplicity if the function is to be legitimate. If all the formulae indicating it are excessively “complicated and recondite” then the function is illegitimate (Russell, *ibid*).

In one fascinating passage, Russell offers an epistemological argument in favor of simplicity that is somewhat reminiscent of Hilbert’s epistemological notion of finitsm (1904, 1925). For Russell, if a proposition is to be intelligible or graspable, it can have only finitely many components. Otherwise, he says, it will be too “complicated and recondite” to grasp. Further, he continues, the number of values of first-order variables in a universally quantified sentence is infinite, because in Russell’s untyped language such variables range over everything rather than over values from a restricted range. These values are too numerous to be components of any intelligible general proposition. Rather, according to Russell, the genuine components of such a proposition are propositional functions, from which we can build intelligible complexes by applying functions to other functions and to complexes built out of functions. Only propositions built in this way guarantee the existence of classes. This argument is found in (Russell, 1904b, p. 100).

In any case, Russell adds that for every legitimate propositional function, a formula expressing its negation is also legitimate. If, on the other hand, a function expressed by ‘$\Phi x$’ is illegitimate, then there are either members of the corresponding class of which ‘$\Phi x$’ is false or members of its complement of which ‘$\Phi x$’ is true. Thus, the function expressed by ‘$\Phi x$’ is made illegitimate as much by the things to which it does not apply just as by the things to which it does. So, given any class $u$ and an illegitimate function indicated by ‘$\Phi x$’, ‘$\Phi x$’ applies to some but not all members of $u$ or to some but not all of the members of its complement. This, says Russell, “is the zig-zag property which gives its name to the theory” (1907, 38). Finally, if two functions are to determine the same class, both must be legitimate.

Note that restrictions are placed on the complexity of comprehension axioms not on the sizes of classes. The open formulae ‘$x$ is a surviving member of the Beatles’ and ‘$x$ is not a surviving member of the Beatles’ express legitimate propositional functions, despite the fact that the class corresponding to the latter is enormous – containing (at the time of writing) only two objects fewer than are contained in $V$. Russell’s various attempts to state axioms for logical simplicity defy informative summary, so we refer the reader to (Russell, 1904), (Quine, 1937, 1967) and (Burgess, 2005, ch. 2).

More important is the substitutional theory, which allows Russell to mimic the logical behavior of both propositional functions and classes in a theory that quantifies over neither kind of entity. Rather than expressing or designating a given propositional function $\Phi x$ as an entity, we begin simply with propositions. Consider a pair consisting of a proposition $p$ and its argument $a$, for example:

John Lennon was a member of the Beatles, John Lennon$.$

Both the proposition and its argument are individuals. There are no (other) types. Russell uses the notation

$$p~ x/a; !q$$

for the following four-place relation between $p$ and another proposition $q$:

$q$ is the unique proposition that results from $p$ by the substitution of $x$ for all occurrences of $a$ as argument in $p.$

Because of the uniqueness requirement in Russell’s theory of definite descriptions, the following is a logical axiom of Russell’s theory:

$$(p~x/a; !q)\wedge(p~x/a; !r)\rightarrow r=q.$$

Recall that $p$ is the proposition that John Lennon was member of the Beatles. Rather than writing

$x$ was a member of the Beatles,

which, together with a comprehension axiom for classes, invites the error of thinking that this propositional function is an entity that determines a class containing John, Paul, George and Ringo, consider the proposition $p$ and its argument:

$$(p~x/a; q) \amp q\equiv x=a\vee x=b \vee x=c \vee x=d.$$

In other words,

$q$ is the proposition that results from $p$ by the substitution of $x$ for all occurrences of $a$ $\amp$ $q$ is true if and only if $x$ is either John, Paul$,$ George, or Ringo$.$

So, the correct values for $x$ make $q$ true. However,

> we do not assume that these values collectively form a single entity which is the class composed of them (Russell 1907, 46).

Presumably, it is even possible to mimic the universal class with a pair such as

John Lennon = John Lennon, John Lennon.

In general, Russell can define the relation $\in$ that mimics class membership in terms of the truth of the result of substitution:

$$x\in p~ x/a\equiv_{df} (p~x/a; q)\amp q.$$

However, ‘$p~x/a$’ does not denote a class. It is an incomplete symbol that has meaning only in the context of a larger expressions like the ones above that describe substitution relations between propositions.

Note that the substitution of $x$ for $a$ is the substitution of one *individual entity* for another; it is not merely the substitution of symbols for symbols. This raises the same question about the logico-metaphysical status of the entity $x$ that arose above for propositional functions. Is $x$ a variable object? For a way of side-stepping this, see (Pelham and Urquhart 1995), which contains a rigorous formal version of Russell’s substitutional theory that makes use of Frege’s notion of an incomplete or unsaturated entity as described in section 2.5 of the main text.

Note also that substitution can result in distinct true propositions for different values of $x$. Clearly, then, Russell is still working with the “objective propositions” of his (1903), which contain worldly objects like John Lennon and are finely individuated by the principle that if a pair of propositions differ by a constituent, then they are distinct propositions. This property of being fine grained leads to the paradox about classes of propositions that is discussed in section 5 of the main text. And, as will be explained, the possibility of substitution into the argument places of fine-grained propositions leads to yet another paradox.

Since there are no comprehension axioms in the substitutional theory for classes or propositional functions as entities, there are no paradoxes of classes or functions. Neither is there a paradox about classes of propositions like that discussed in section 5 of the main text. Nor is there the purportedly paradoxical proposition that is usually written as ‘$R(R)$’. This is ruled as ill-formed by the substitutional theory. Instead of the legal

$$p~ x/a; !q,$$

in which $x$ is substituted once for $a$ to yield $q,$ deriving the paradoxical proposition would require substituting $x$ twice into a monadic proposition to yield a self-application:

$$p~x, x/a; !q.$$

This is not allowed by the syntax of Russell’s substitutional theory, which bars substitution of two variable objects $x$ and $y$, or two occurrences of a variable object $x$ (as above), for a single argument place $a$ (Landini, 2011). For readers familiar with the $\lambda$-calculus, it is a little bit like trying to abstract John shaves himself, i.e.

$$(\lambda x.x \textit{ shaves } x)\text{John}$$

from the simple monadic surface form of ‘John shaves’. To abstract ‘John shaves himself’, we would need to look deeper into the syntax of ‘John shaves’ to find an elided argument place that can be made explicit as in ‘John shaves John’. Only then could we substitute one variable for each occurrence of ‘John’.

Unfortunately, Russell’s battle against paradox was not over. Disaster struck again when he discovered that the possibility of substitution into the argument place of a fine-grained objective proposition allows diagonalization. First, he defines a proposition $Po$:

$$Po=_{df} \exists p, a[ao=p~b/a; !q\wedge \exists z (p~ao/a;!z\wedge{\sim}z)].$$

This can be rewritten as

$$\exists p, a [ao=p~ b/a;!q\wedge{\sim}p~ao/a].$$

Next Russell substitutes $Po~b/ao$; $!q$ for $ao$ in $Po$ to obtain the proposition $(\text{R})$:

$$\tag{R} \exists p, a[Po~b/ao;!q=p~b/a;!q\wedge{\sim}p~(Po~b/ao;!q/a)].$$

Russell then derives a contradiction from $(\text{R}).$ This paradox led Russell first to alter the substitutional theory (Russell 1908), and then to abandon it altogether for the ramified theory of types that is discussed in the main text. As Pelham and Urquhart write:

> The contradiction revealed by the substitutional paradox is of a fundamental sort; it does not directly involve truth, quotation contexts or self-reference, as in other semantical paradoxes. When Russell first faced the paradoxes, he thought he could solve the problems posed by them by making *ad hoc* modifications to a set-theoretical apparatus built upon a logical foundation which could be assumed as given. The substitutional paradox, in contrast, uses only elementary relations between Russellian propositions in addition to basic logical concepts. It led in the end to the radical reconstruction of logic in the ramified theory of types. (Pelham & Urquhart 1995, 321)

Perhaps as a result of this paradox, propositions are dropped entirely from Russell’s mature theory of types.

The significance of the substitutional paradox is also discussed in Grattan-Guiness 1974, Linsky 2003, Klement 2010ab and Galaugher 2013.
