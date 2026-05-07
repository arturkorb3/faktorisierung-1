# Joux–Buchmann Bridge: Gated Research Pass

## Final gate result

**Gate I:** PASS — the K1–K5 abstraction is internally consistent.
**Gate II:** PASS — not all entries are red; K2/K5 have concrete but incomplete analogues.
**Gate III:** PASS — several replacement mechanisms can be formulated without vague analogy.
**Gate IV:** FAIL — every sketched pipeline collapses to **(L[1/2])** or worse for fixed real quadratic fields.
**Phase V result:** negative structural theorem, conditional on staying inside the Joux-style “smooth-relation descent” paradigm.

I do **not** find an asymptotic factoring algorithm better than NFS through this bridge. The obstruction is sharper than the folklore phrase “(\mathbb Z) has no Frobenius”: the missing object is a **large, public, low-degree endomorphism with a large finite fixed locus and a representation-shrinking identity**. In (\mathbb Q(\sqrt N)), the only intrinsic field symmetries are identity and conjugation; external substitutes either expose factorization data or leave relation norms at polynomial size in the discriminant, forcing (L[1/2]) by smoothness.

---

# Phase I — Structure skeleton K1–K5

## K1 — Smoothness basis choice

**Abstract minimum requirement.**
A descent-friendly factor base is not merely a small generating set. It must come with a complexity measure (m(x)), a smoothness test, and a relation mechanism that replaces a target object (x) by objects (x_i) with strictly smaller (m(x_i)). The base must be large enough to span the relevant relation lattice, but small enough that linear algebra and relation collection are subdominant. For a Joux-style breakthrough, the base must support **recursive targeted descent**, not only random relation collection.

**Finite-field realization.**
In the BGJT/Joux setting, elements of (K=\mathbb F_{q^{2k}}) are represented as polynomials of degree (<k) over (\mathbb F_{q^2}), assuming a sparse medium subfield representation: (K\simeq \mathbb F_{q^{2k}}) and (h_1X^q-h_0) has an irreducible degree-(k) factor with (h_0,h_1) of small degree. The smoothness basis consists essentially of (h_1) and low-degree polynomials, especially linear polynomials (X+a) over (\mathbb F_{q^2}). Proposition 2 in BGJT gives a step that expresses (\log P) in terms of (O(kq^2)) logarithms of polynomials of degree at most roughly half of (\deg P), then recursively descends to the basis. ([arXiv][1])

**Characteristic-(p) dependence.**
Moderate. Smoothness bases exist in number fields as small prime ideals, and Buchmann-type algorithms already use them. The genuinely special part is not the existence of the base but the targeted degree-halving relation mechanism attached to it.

---

## K2 — On-the-fly relations / elimination step

**Abstract minimum requirement.**
The elimination step needs a large parametrized family of relations attached to the target (P), such that one side contains many controlled translates of (P), while the other side has lower complexity after applying a representation relation. The collected relations must span a linear system whose rows allow one to isolate (\log P). This requires both a supply of relations and a rank heuristic or theorem.

**Finite-field realization.**
BGJT uses the systematic equation
[
X^q-X=\prod_{a\in \mathbb F_q}(X-a),
]
or projectively
[
X^qY-XY^q=\prod_{(\alpha:\beta)\in \mathbb P^1(\mathbb F_q)}(\beta X-\alpha Y).
]
Then homographies from (PGL_2(\mathbb F_{q^2})/PGL_2(\mathbb F_q)) are applied to the target polynomial (P). The right-hand side becomes a product of (q) or (q+1) translates of (P), while the left-hand side is rewritten through (X^q\equiv h_0(X)/h_1(X)), yielding a numerator of degree at most ((1+\delta)\deg P). If that numerator is (\lceil \deg P/2\rceil)-smooth, the relation contributes to the elimination matrix. The crucial BGJT heuristic is full rank of the matrix formed by successful relations. ([arXiv][1])

**Characteristic-(p) dependence.**
Strong. The identity (X^q-X) is not just “a polynomial that splits”; it is the fixed-point polynomial of the Frobenius over (\mathbb F_q), and the same Frobenius also gives the low-degree rewrite (X^q\equiv h_0/h_1). Joux’s 2013 appendix notes possible alternative polynomials, but they still require two properties: splitting into low-degree factors over a small extension and being writable as a low-degree polynomial in (X) and (X^q). 

---

## K3 — Frobenius symmetry

**Abstract minimum requirement.**
The needed object is a public endomorphism (\Phi) of the representation algebra such that:

1. (\Phi) has a large, explicitly enumerable fixed locus;
2. (\Phi) interacts with the representation so that (\Phi(X)) is low-complexity, e.g. (X^q\equiv h_0/h_1);
3. the fixed-locus identity gives many linear factors;
4. applying a large symmetry group to this identity produces enough independent target-specific relations.

**Finite-field realization.**
The (q)-power Frobenius (x\mapsto x^q) fixes (\mathbb F_q), and the polynomial (X^q-X) vanishes exactly on that fixed field. BGJT’s projective version uses (\mathbb P^1(\mathbb F_q)), and the action of (PGL_2) generates the relation family. The 2018 Granger–Kleinjung–Zumbrägel work sharpens the setting: for fixed characteristic, they prove quasi-polynomial expected time for infinitely many explicit extensions, with a central theorem using (h_1X^q-h_0), degree-two elimination, and trap avoidance. ([Infoscience][2])

**Characteristic-(p) dependence.**
Very strong. Frobenius is simultaneously a ring endomorphism, a finite-order Galois generator, a source of many fixed points, and a degree-reduction mechanism. In characteristic zero, these roles split apart and no intrinsic replacement supplies all four.

---

## K4 — Recursive subfield / tower descent

**Abstract minimum requirement.**
The descent needs a tower or embedding structure that allows recursive reduction of representation complexity without increasing coefficient size enough to erase the gain. It is not enough to have a subgroup or a quotient. The tower must support controlled norm maps, compact representations, smoothness heuristics, and a depth (O(\log m)) recursion with polynomial or quasi-polynomial branching.

**Finite-field realization.**
Finite fields have canonical subfields when degrees divide, and when the original field lacks a suitable medium subfield, BGJT embeds the problem into a larger field (\mathbb F_{q^{2k}}) chosen so that (q) and (k) are balanced. Their complexity becomes (\max(q,k)^{O(\log k)}), quasi-polynomial in the small-characteristic range. ([arXiv][1])

**Characteristic-(p) dependence.**
Strong, but the precise obstruction is not merely “no subfields.” A real quadratic field has no nontrivial intermediate fields, but the deeper issue is the absence of a public family of representation-changing embeddings with controlled discriminant and norm growth.

---

## K5 — Representation switch

**Abstract minimum requirement.**
The algorithm needs freedom to choose representations in which a target object has low complexity. For finite fields this means sparse defining polynomials and medium subfields. For number fields it would mean changing orders, defining polynomials, forms, ideals, Arakelov divisors, or auxiliary fields so that relation norms shrink.

**Finite-field realization.**
The sparse medium subfield representation is central: (h_1X^q-h_0) has a large irreducible factor while (h_0,h_1) have small degree. Joux–Pierrot’s special NFS work similarly exploits special sparse representations of (p) in finite-field DLP, showing that representation choice materially changes the complexity landscape. ([arXiv][1])

**Characteristic-(p) dependence.**
Mixed. Number fields have representation changes, and class group algorithms exploit them. Biasse–Fieker explicitly obtain subexponential class group and unit algorithms in large-degree fields, using factor bases, relation lattices, BKZ, and (q)-descent ideas. But for fixed degree (2), the representation-switch parameter that drives NFS-style (L[1/3]) behavior is absent. 

---

# Gate I

**PASS.** The five components are coherent: K1 and K5 are representation/factor-base infrastructure; K2 is the relation engine; K3 supplies the splitting and degree-rewrite identity; K4 supplies recursion depth control.

---

# Phase II — Translation table to (\mathcal O_K), (K=\mathbb Q(\sqrt N))

| ID | Status in (\mathcal O_K) | Reason                                                                                                                                                                                                                                                                                                                                                        |
| -- | -----------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| K1 |                **GREEN** | Buchmann-style algorithms have an explicit factor base of prime ideals of norm (\le B), relation lattices, HNF/SNF, and regulator extraction. Biasse–Fieker formulate this as a map from exponent vectors on prime ideals to the class group, with relations corresponding to principal products.                                                             |
| K2 |               **YELLOW** | Concrete on-the-fly relations exist: choose (\alpha\in\mathcal O_K), factor ((\alpha)) over the factor base, and obtain a relation. Targeted variants choose (\alpha) inside a target ideal. But no known mechanism gives BGJT-style target isolation plus degree-halving. This is a real mechanism with a gap, not vague analogy.                            |
| K3 |                  **RED** | The intrinsic endomorphism supply is too small. As a (\mathbb Q)-algebra, (K) has only identity and conjugation. Conjugation gives a two-point orbit, not a (q+1)-point fixed-locus identity. Residue-field Frobenius exists only after choosing prime ideals; using the Frobenius at the hidden primes above (p) or (q) amounts to using factorization data. |
| K4 |                  **RED** | (K/\mathbb Q) has no nontrivial intermediate fields. External towers can be built, but a useful norm-descent tower must both preserve the regulator target and control discriminant/norm growth. Generic cyclotomic, Kummer, Hilbert, or ray class towers fail one of these requirements or require class field data.                                         |
| K5 |               **YELLOW** | There are concrete representation switches: binary quadratic forms, reduced ideals, infrastructure, Arakelov divisors, equation orders, and auxiliary number fields. Biasse’s (L[1/3]) methods work in certain large-degree number-field families, but not directly in fixed-degree real quadratic fields.                                                    |

**Red-theorem vs convention check.**

K3 is theorem-level inside the allowed class: intrinsic ring/field endomorphisms of a quadratic number field are only identity and conjugation. Any larger Frobenius-like family must come from reductions modulo prime ideals. To separate prime ideals above the hidden rational primes (p,q\mid N), one needs CRT idempotents, equivalent to factoring (N).

K4 is theorem-level for internal fields: a degree-2 extension has no nontrivial intermediate field. For external towers the obstruction is not a universal impossibility theorem, but every concrete candidate below fails by discriminant/norm growth or by requiring class/ray class data.

# Gate II

**PASS.** K2 and K5 are yellow.

---

# Phase III — Replacement structures for yellow components

## Candidate A — Targeted principal-ideal descent

**Mechanism.**
Given a target prime ideal (\mathfrak q), search for a short element (\alpha\in\mathfrak q). Then
[
(\alpha)=\mathfrak q\prod_i \mathfrak p_i^{e_i}
]
gives a relation involving (\mathfrak q). If all (\mathfrak p_i) have norm below a lower bound, this is a descent step. This is the closest number-field analogue of “eliminate (P)” in BGJT.

**Gap.**
In a fixed quadratic field, the norm of a short lattice vector in (\mathfrak q) is still typically polynomial in (|D|). Smoothness of polynomial-size integers against a subexponential factor base gives (L[1/2]), not (L[1/3]). This is not merely an implementation gap; it is the standard CEP smoothness barrier for fixed-degree norm forms.

---

## Candidate B — Infrastructure / Arakelov replacement for Frobenius

**Mechanism.**
Real quadratic infrastructure gives a cyclic “distance” structure modulo the regulator. Arakelov divisors generalize this infrastructure and encode units through a logarithmic lattice. A descent might try to replace a target ideal by nearby reduced ideals and collect short principal corrections.

**Gap.**
The infrastructure gives a one-dimensional metric cycle, not a large finite fixed locus. It supplies baby-step/giant-step style navigation, but not a (PGL_2)-sized relation family. Its natural complexity is square-root or Buchmann (L[1/2])-type unless combined with smooth relation collection. Schoof’s Arakelov class group viewpoint is structurally useful, but it does not create a Frobenius identity.

---

## Candidate C — Hecke operators / modular forms

**Mechanism.**
Hecke operators act on ideal classes, modular forms, and cohomological objects attached to quadratic fields. One might try to use Hecke correspondences as a replacement for Frobenius-generated relation families.

**Gap.**
Hecke operators are correspondences, not endomorphisms of (\mathcal O_K) producing principal ideal relations with small norm. They average or move classes; they do not give a public identity whose complete factorization is known and whose transformed left-hand side collapses to lower complexity. Without this collapse, the method reverts to generic relation search.

---

## Candidate D — External Kummer/cyclotomic towers

**Mechanism.**
Use fields such as (\mathbb Q(\sqrt[m]{N})), (K(\zeta_m)), or (K)-extensions with controlled norm maps, hoping to descend ideals in the larger field and push relations down to (K).

**Gap.**
If (m) grows, discriminants and coefficient heights grow too quickly. If (m) is fixed, there is no asymptotic tower. If the tower is chosen to be unramified or class-field-theoretic, constructing it requires class group/ray class information comparable to the target. If it is ramified at (p) and (q), exploiting the ramification requires knowing (p,q).

# Gate III

**PASS.** Candidate A is a concrete mechanism; Candidates B–D are also precise enough to test.

---

# Phase IV — Complexity analysis

## Hypothetical pipeline

```
Input: N = pq, D = disc(Q(sqrt(N))).

1. Build factor base B = {prime ideals p_i : Norm(p_i) <= y}.
2. For random or target ideals a:
      find short alpha in a or in a product a * prod p_i^{e_i}.
3. Factor Norm(alpha).
4. If Norm(alpha) is y-smooth:
      record the exponent relation among prime ideals.
5. Repeat until the relation matrix has full rank.
6. Extract class group and regulator from HNF/SNF and unit reconstruction.
7. Use the regulator-to-factoring pipeline assumed in the prompt.
```

The analytic class number formula justifies why regulator and class group data are the relevant objects: for a number field (K), the residue of (\zeta_K(s)) at (s=1) contains (h_KR_K/\sqrt{|D_K|}), and for quadratic fields (\zeta_K(s)=\zeta(s)L(s,\chi_K)). 

## Smoothness calculation

Let the factor-base bound be

[
y=L_D[a,c]=\exp!\left((c+o(1))(\log D)^a(\log\log D)^{1-a}\right).
]

In fixed degree (2), the norms of useful relation candidates are generically of size (D^{O(1)}), so

[
\log X \asymp \log D.
]

The Dickman/CEP smoothness estimate gives

[
\Pr[X\text{ is }y\text{-smooth}]
\approx
\exp(-u\log u),
\qquad
u=\frac{\log X}{\log y}.
]

Since (u\asymp(\log D)^{1-a}/(\log\log D)^{1-a}), the inverse smoothness probability is

[
L_D[1-a,O(1)].
]

The factor base has size (L_D[a,O(1)]). Therefore relation collection costs

[
L_D[\max(a,1-a),O(1)],
]

minimized at

[
a=\frac12.
]

So the pipeline gives **(L_D[1/2])**.

To reach (L[1/3]), one would need relation norms of size roughly (L_D[2/3]), not (D^{O(1)}). NFS obtains this by balancing two polynomial norms. BGJT obtains better behavior by Frobenius-based degree halving. A fixed real quadratic order supplies neither mechanism.

## Engpass

The bottleneck is **not** linear algebra, not the class number formula, and not the absence of a factor base. It is:

> There is no public targeted relation identity in (\mathcal O_K) that turns a target ideal into strictly smaller ideals while keeping candidate principal norms below (L_D[2/3]).

# Gate IV

**FAIL.** The best pipeline derived here is (L[1/2]), not (\le L[1/3]). No Phase V-Pos implementation follows.

---

# Phase V-Neg — Structural theorem

## Theorem 1 — Frobenius obstruction

**Claim.**
A Joux-style K3 component requires a public endomorphism (\Phi) with a large finite fixed locus and a low-complexity rewrite identity. In (K=\mathbb Q(\sqrt N)), no such intrinsic (\Phi) exists. Any residue-level substitute that separates the hidden prime components of (N=pq) requires factoring data.

**Proof sketch.**
Every (\mathbb Q)-field endomorphism of a number field is an automorphism. Since (K/\mathbb Q) is quadratic,
[
\operatorname{Aut}_{\mathbb Q}(K)={1,\iota},
]
where (\iota(\sqrt N)=-\sqrt N). Thus the only intrinsic nontrivial symmetry has order (2) and fixed field (\mathbb Q). It cannot yield a (q+1)-sized projective fixed locus or a splitting identity analogous to (X^q-X).

One can reduce (\mathcal O_K) modulo rational primes or ideals and use finite-field Frobenius locally. But a global map modulo (N) that treats the (p)- and (q)-components separately requires the CRT idempotents of (\mathbb Z/N\mathbb Z\simeq\mathbb F_p\times\mathbb F_q), and those idempotents yield (\gcd(e,N)) factorizations. Therefore a nontrivial Frobenius substitute at the hidden primes presupposes the factorization.

---

## Theorem 2 — Tower descent obstruction

**Claim.**
A Joux-style K4 component requires a recursive tower with controlled norm/discriminant growth and norm maps preserving the target regulator problem. No such internal tower exists for (K=\mathbb Q(\sqrt N)), and the obvious external towers do not give an (L[1/3]) regulator algorithm without additional class-field information.

**Proof sketch.**
Internally, (K/\mathbb Q) has degree (2), hence no nontrivial intermediate field. Externally, a tower (L/K) must satisfy three conditions:

1. relations in (L) must push down to regulator/class-group information in (K);
2. discriminants and coefficient heights must stay balanced;
3. the tower must be constructible without knowing (p,q) or the class/ray class group of (K).

Cyclotomic and Kummer towers violate condition 2 asymptotically unless degrees are fixed, in which case no recursive descent depth is gained. Unramified or ray class towers violate condition 3 because their construction is essentially class group computation. Towers ramified at (p,q) violate the no-factorization condition if their useful structure depends on identifying those primes.

---

## Theorem 3 — Fixed-degree norm-smoothness barrier

**Claim.**
Within the class of Buchmann-style algorithms whose relations are obtained by principal ideals ((\alpha)) in a fixed-degree real quadratic order and whose success depends on smoothness of (N_{K/\mathbb Q}(\alpha)), the optimal smoothness balance is (L_D[1/2]). Thus this class cannot reproduce the Joux/BGJT (L[1/3])-or-better descent.

**Proof sketch.**
For fixed degree, candidate relation norms are polynomial in (D) after reduction or short-vector search. Let (y=L_D[a]). Smoothness probability of a polynomial-size integer against (y) is (L_D[-(1-a)]). One needs (L_D[a]) successful independent relations. The relation phase therefore costs (L_D[\max(a,1-a)]), minimized at (a=1/2). Biasse–Fieker’s large-degree (q)-descent breaks this only when the number-field degree and defining-polynomial height vary in suitable proportions; their paper explicitly parameterizes such classes by growing degree/height and obtains (L[1/3])-type behavior only under those restrictions, not in fixed real quadratic degree. 

---

# Open loopholes that remain nontrivial

1. **Non-endomorphic correspondences.**
   A Hecke or automorphic correspondence might create relation families without being a ring endomorphism. I found no mechanism that makes principal norms shrink, but this is not ruled out by Theorem 1.

2. **A hidden representation of (\mathcal O_K).**
   If one could represent real quadratic ideals in an auxiliary algebra where the target regulator survives and relation norms become (L_D[2/3]), the (L[1/2]) barrier would not apply. None of the tested towers provides this.

3. **Regulator-specific shortcuts.**
   The analysis targets class-group/regulator computation through smooth principal relations. A method computing (R_K) without constructing enough class group relations would evade Theorem 3.

---

# Bottom line

The Joux bridge fails at **K3/K4**, not at K1. Real quadratic class-group machinery has factor bases and relation lattices, but it lacks the single object that makes the Joux/BGJT descent collapse: a large Frobenius fixed-locus identity whose transformed left side has lower representation complexity.

The resulting negative statement is:

> A Joux-style improvement of real-quadratic regulator computation below (L[1/2]) cannot be obtained by merely importing finite-field smooth bases, on-the-fly principal ideal relations, or infrastructure representation changes. One must supply a genuinely new K3/K4 replacement: a public, non-factorization-dependent, large relation symmetry that reduces principal norm size below the fixed-degree polynomial norm regime.

No such replacement was found in this pass.

[1]: https://arxiv.org/pdf/1306.4244 "A quasi-polynomial algorithm for discrete logarithm in finite fields of small characteristic"
[2]: https://infoscience.epfl.ch/bitstreams/673f22b7-2719-4e06-ab9b-3e2c922ff0de/download "dl_rev.dvi"
--- was denkst du?