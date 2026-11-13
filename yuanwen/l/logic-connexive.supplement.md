# logic-connexive — supplement（supplement）

> （《logic-connexive》词条补充材料，源：plato.stanford.edu/entries/logic-connexive/supplement.html）

#### Supplement to Connexive Logic

## Supplement on Terminology

Kapsner (2019) introduces the following restricted versions of Aristotle’s theses, Boethius’ theses, Unsat1, and Unsat2:

> Plain humble AT and AT′: For any satisfiable ~*A*, ~(~*A* → *A*) is valid. For any satisfiable *A*, ~(*A* → *~A*) is valid.
> Plain humble BT and BT′: For any satisfiable *A* and satisfiable *A* → *B*, (*A* → *B*) *→* ~(*A →* ~*B*) is valid. For any satisfiable *A* and satisfiable *A* → ~*B*, (*A*→ ~*B*) → ~(*A* → *B*) is valid.
> Plain humble Unsat1: In no model, *A* → ~*A* is satisfiable (for any satisfiable *A*), and in no model, *~A* → *A* is satisfiable (for any satisfiable *A*).
> Plain humble Unsat2: In no model, *A* → *B* and *A* → ~*B* are simultaneously satisfiable (for any satisfiable *A*).

Logics that satisfy the restricted versions of Aristotle’s and Boethius’ theses are then *plainly weakly humbly connexive*. According to Lenzen (2019a) the idea of restricting Aristotle’s and Boethius’ theses to self-consistent propositions can be found in Leibniz already, see section 2. However, if a formula *A* is satisfiable in classical logic, then ⊬ *A* → ~ *A*, so that in this weak sense of connexivity, restricting AT′ to satisfiable antecedents makes the whole enterprise of connexive logic pointless from the standpoint of classical logic. Restrictions of connexive principles in terms of consistency or possibility requirements have been discussed also in Unterhuber 2016, whereas Vidal (2017) considers a restriction to contingent formulas *A* and *B* in Aristotle’s and Boethius’ theses. Kapsner 2019 discusses even more notions of connexivity, namely modal humble, glutty humble, and paraconsistent humble connexivity. Combinations of Kapsner’s defining properties gives rise to even further notions of connexivity such as the notion of a logic being *Kapsner strong* from Estrada-González & Ramirez-Cámara 2016.

Still another conception of connexive logic that also imposes further conditions in addition to validating Aristotle’s and Boethius’ theses was used by Routley (1978, Routley *et al*. 1982) and Routley and Routley (1985), see sections 3.1 and 3.3.

One may assume that the non-symmetry of implication is tacitly assumed in many works on connexive logic, but since this condition is used to draw a terminological distinction in Jarmużek and Malinowski 2019a, it is taken into account in the following table that surveys the terminology and notions of connexivity used in the literature as well as some (but not all) combinations of certain defining properties.

| *notion* | *principles and conditions* | *references* |
| --- | --- | --- |
| **connexive** | AT, AT′, BT, BT′, non-symmetry of implication | this entry and numerous other publications |
| minimally connexive | ditto | Estrada-González and Ramirez-Cámara 2016 |
| properly connexive | ditto | Jarmużek and Malinowski 2019a |
|   |   |   |
| *diverging and additional notions* | *principles and conditions* | *references* |
| connexive | at least one of AT, AT′, BT, BT′ | Mares and Paoli 2019 |
| connexive | AT, AT′, BT, BT′ | Jarmużek and Malinowski 2019a |
| connexive | AT, AT′, BTw, BTw′ | Weiss 2019 |
|   |   |   |
| half-connexive | BTw, BTw′ | Weiss 2019 |
|   |   |   |
| subminimally connexive | some but not all of AT, AT′, BT, BT′, non-symmetry of implication | Estrada-González and Ramirez-Cámara 2016 |
| properly quasi-connexive | ditto | Jarmużek and Malinowski 2019a |
| demi-connexive | some but not all of AT, AT′, BT, BT′ | Wansing, Omori, Ferguson 2016 |
| quasi-connexive | ditto | Jarmużek and Malinowski 2019a |
| weakly connexive | BT, BT′ only in rule form | Wansing and Unterhuber 2019 |
| weakly connexive | AT, AT′, BT, BT′ | Kapsner 2012 |
|   |   |   |
| strongly connexive | AT, AT′, BT, BT′ + UnSat1, UnSat2 | Kapsner 2012 |
| superconnexive | strongly connexive + (*A* → ~*A*) → *B* | Kapsner 2012 |
|   |   |   |
| plainly humbly connexive | plain humble AT, AT′, BT, BT′ + plain humble UnSat1, UnSat2 | Kapsner 2019 |
| plainly weakly humbly connexive | plain humble AT, AT′, BT, BT′ | Kapsner 2019 |
| modally humbly connexive | modal humble AT, AT′, BT, BT′ + modal humble UnSat1, UnSat2 | Kapsner 2019 |
| modally weakly humbly connexive | modal humble AT, AT′, BT, BT′ | Kapsner 2019 |
| Gluttily humbly connexive | glutty humble AT, AT′, BT, BT′ + glutty humble UnSat1, UnSat2 | Kapsner 2019 |
| Gluttily weakly humbly connexive | glutty humble AT, AT′, BT, BT′ | Kapsner 2019 |
| paraconsistently humbly connexive | paracons. humble AT, AT′, BT, BT′ + paracons. humble UnSat1, UnSat2 | Kapsner 2019 |
| paraconsistently weakly humbly connexive | paracons. humble AT, AT′, BT, BT′ | Kapsner 2019 |
|   |   |   |
| Kapsner strong | UnSat1, UnSat2 | Estrada-González and Ramirez-Cámara 2016 |
| subminimally connexive and Kapsner strong | subminimally connexive + UnSat1, UnSat2 | Estrada-González and Ramirez-Cámara 2016 |
|   |   |   |
| hyperconnexive | AT, AT′, BTe, BTe′, non-symm. of implication + failure of Conj. Simplif. | Sylvan 1989 (in combination with Routley 1978) |

In the above table, the conditions defining Kapsner’s notion of modal humble connexivity are as follows, cf. also the modalized versions of Aristotle’s and Boethius’ theses as entailment statements in Vidal 2017:

> Modal humble AT, AT′: ◊*~A* ⊨ ~(~*A* → *A*), ◊ *A* ⊨ ~(*A* → ~*A*).
> Modal humble BT, BT′: ◊*A* ∧ ◊ (*A* → *B*) ⊨ (*A* → *B*) → ~(*A*→ ~*B*), ◊*A* ∧ ◊ (*A* → ~*B*) ⊨ (*A* → ~*B*) → ~(*A* → *B*).
> Modal humble UnSat1: In no model, ◊~*A* ∧ (~*A* → *A*) is satisfiable, and in no model, ◊*A* ∧ (*A* → ~*A*) is satisfiable.
> Modal humble Unsat2: In no model, ◊*A* ∧ (*A* → *B*) ∧ (*A* → ~*B*) is satisfiable.

For glutty humble connexivity, Kapsner’s assumes a many-valued semantics with a designated glutty truth value **B**, “understood as “both true and false”, and a negation operator ~ such that ~*A* receives the value **B** if *A* does. Such a semantics gives a paraconsistent logic, where *ex contradcitione quodlibet*, *A* ∧ ~*A* ⊢ *B*, does not hold. The defining conditions are the following:

> Glutty humble AT, AT′: For any satisfiable ~*A*, resp. *A* that does not take value **B**, ~(~*A* → *A*), resp. ~(*A* → ~*A*) takes a designated value.
> Glutty humble BT, BT′: For any satisfiable *A*, *B*, and *A* → *B*, reps. *A*, ~*B*, and *A* → ~*B* that do not take value **B**, (*A* → *B*) → ~(*A* → ~*B*), resp. (*A* → ~*B*) → ~(*A* → *B*) takes a designated value.
> Glutty humble UnSat1: In no model, ~*A* → *A*, resp. *A → ~**A* is satisfiable (for any satisfiable ~*A*, resp. *A* that does not take value **B**).
> Glutty humble Unsat2: In no model, *A* → *B* and *A* → ~*B* are simultaneously satisfiable (for any satisfiable *A*, *B* that do not take value **B**).

Kapsner’s conditions for paraconsistent humble connexivity make use of conjunction and disjunction in the object language:

> Paraconsistent humble AT, AT′: For any satisfiable ~*A*, resp. *A*, (*A* ∧ ~*A*) ∨ ~(~*A* → *A*), reps. (*A* ∧ ~*A*) ∨ ~(*A* → ~*A*) is valid.
> Paraconsistent humble BT, BT′: For any satisfiable *A* and *A* → *B*, reps. *A* and *A* → ~*B*, (*A* ∧ ~*A*) ∨ ((*A* → *B*) ∧ ~(*A* → *B*)) ∨ ((*A* → *B*) → ~(*A* → ~*B*)), resp. (*A* ∧ ~*A*) ∨ ((*A* → *B*) ∧ ~(*A* → *B*)) ∨ ((*A* → ~*B*) → ~(*A* → *B*)) is valid.
> Paraconsistent humble UnSat1: ~*A* → *A* and *A →* ~*A* are satisfiable only in valuations in which *A* ∧ ~*A* is also satisfied.
> Paraconsistent humble Unsat2: *A* → *B* and *A* → ~*B* are simultaneously satisfiable only in valuations in which *A* ∧ ~*A* is satisfied or (*A* → *B*) ∧ (*A* → ~*B*) is satisfied.
