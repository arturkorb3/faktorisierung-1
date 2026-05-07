---
title: "Smoothness Barrier: Joux–Buchmann Bridge"
layout: default
permalink: /smoothness-barrier/
description: "Fixed-degree smoothness and infrastructure period-finding barriers for real quadratic regulators."
---

# Fixed-Degree Smoothness Barriers for Real Quadratic Infrastructure and the Joux–Buchmann Bridge

**Abstract.** The Joux/BGJT algorithm achieves quasi-polynomial complexity for discrete logarithms in small-characteristic function fields by exploiting Frobenius symmetry, tower descent, and polynomial-basis smoothness. We investigate whether a structural analogue exists for the real quadratic regulator of $K = \mathbb{Q}(\sqrt{N})$, which would yield a faster classical algorithm for computing $R_K$ and hence for factoring RSA semiprimes $N = pq$. We prove two barriers. First (Theorem 1), in the class of Buchmann-style smooth-relation algorithms for fixed real quadratic degree, the heuristic relation-collection barrier is $L_D[1/2]$, conditional only on the standard smoothness heuristic and even relative to an integer factoring oracle. Second (Theorem 2), in the generic infrastructure model, finding the infrastructure period requires $\Omega(\sqrt{R_K})$ oracle queries. The Joux pipeline analysis shows Gate IV failure: no Frobenius analogue, no tower descent, and no mechanism below $L[1/2]$ exists in degree 2. The conclusion is a precise corollary: any Joux-style improvement would require either a Frobenius analogue not known to exist, or a semiprime-specific prefix-to-period law for continued fractions of $\sqrt{pq}$.

---

## 1. Introduction

The Number Field Sieve achieves $L_N[1/3]$ for integer factoring. In 2013, Joux and independently Barbulescu–Gaudry–Joux–Thomé showed that discrete logarithms in $\mathbb{F}_{p^n}$ for small characteristic $p$ can be solved in quasi-polynomial time $L[1/4 + o(1)]$ [Joux 2013, BGJT 2014]. The key ingredients — Frobenius symmetry, polynomial smoothness, and recursive tower descent — collectively break the $L[1/2]$ barrier.

The real quadratic regulator $R_K$ of $K = \mathbb{Q}(\sqrt{D})$ governs the fundamental unit $\varepsilon_D$ and the period of the continued fraction expansion of $\sqrt{D}$. For $D = N = pq$, factoring and regulator computation are empirically and conjecturally tightly linked (the BPW bridge; see companion Paper B). If the regulator could be computed in time below $L[1/2]$, this would likely give a sub-NFS factoring algorithm.

This paper asks: *Can the Joux/BGJT approach transfer to real quadratic regulators?*

The answer is no. We identify the five structural components of the Joux method (§2), analyze their transfer (§3), and prove two barrier theorems (§4–5). The analysis is conducted as a pipeline ("gate test"), and Gate IV — the test for any mechanism below $L[1/2]$ — fails hard.

**Limits of claims.** This paper does not prove that no classical algorithm factors $N$ in time below $L[1/3]$. It proves that *this specific class of approaches* — smooth-relation regulator algorithms and infrastructure period-finding — cannot break $L[1/2]$ within the stated models. Theorem 2 is model-relative; it does not exclude non-black-box algorithms exploiting specific arithmetic properties outside the generic infrastructure model.

**Standing assumptions.** The Dickman–CEP smoothness heuristic is used for Theorem 1; it is unproven but standard. Theorem 2 holds unconditionally in the generic infrastructure model. GRH is not needed for the main barrier results.

---

## 2. The Joux/BGJT algorithm: five components

The Joux/BGJT method decomposes into five structural components:

| ID | Component | Role in BGJT |
|---|---|---|
| K1 | Smoothness basis | Low-degree polynomials generating many relations cheaply |
| K2 | On-the-fly relations | Target-specific degree-reducing elimination |
| K3 | Frobenius symmetry | Large fixed-locus identity; $X^q \equiv \prod_{a \in \mathbb{F}_q}(X-a)$ |
| K4 | Tower/subfield descent | Recursive halving of effective degree |
| K5 | Representation switching | Cheap transition between polynomial and rational models |

K3 and K4 are the heart of the $L[1/4]$ gain. Without them, the algorithm would not break $L[1/2]$.

---

## 3. Transfer analysis to real quadratic fields

**K1 (smoothness basis):** Real quadratic fields admit factor bases of prime ideals of bounded norm. The analogue is workable in principle. *Status: partial pass.*

**K2 (on-the-fly relations):** Principal ideal relations exist and can be collected. However, no norm-shrinking identity analogous to $X^q \equiv h_0/h_1$ is known. Relations cannot be recycled via a target-specific descent step. *Status: operationally yellow, functionally red for the BGJT mechanism.*

**K3 (Frobenius symmetry):** The intrinsic automorphism group is $\mathrm{Aut}_{\mathbb{Q}}(K) = \{1, \iota\}$ where $\iota(\sqrt{N}) = -\sqrt{N}$. This two-element group cannot supply a large fixed locus or a Frobenius-type splitting identity. The degree-2 constraint is fundamental: real quadratic fields have no intermediate subfields, so no iterated Frobenius collapses degree. *Status: fail.*

**K4 (tower descent):** No intermediate subfields exist. External tower constructions fail due to discriminant growth, class-field data requirements, or loss of connection to $R_K$. The regulator does not factorize under tower extension in a norm-decreasing way. *Status: fail.*

**K5 (representation switching):** Multiple representations of the infrastructure exist (ideals, binary quadratic forms, NUCOMP/NUDUPL, Arakelov divisors). In fixed degree 2, switching between them does not create the height/degree balance that enables $L[1/3]$-type descent in number fields. *Status: yellow for flexibility, red for asymptotic gain.*

---

## 4. Gate analysis

| Gate | Test | Result | Reason |
|---|---|---|---|
| Gate I | K1–K5 vocabulary coherent in principle | **PASS** | Factor bases and relation collection transferable |
| Gate II | Weak analogues of K2/K5 exist | **PASS** | Principal ideal relations and representation switching present |
| Gate III | Replacement mechanisms formulable | **PASS** | Partial replacements articulable |
| Gate IV | Some pipeline achieves below $L[1/2]$ | **FAIL** | All pipelines collapse to $L[1/2]$ or worse |

---

## 5. Barrier theorems

### Theorem 1 — Fixed-degree norm-smoothness barrier

In the class of Buchmann-style regulator algorithms for fixed real quadratic degree, based on smooth principal-ideal relations, the optimal heuristic relation-collection complexity is $L_D[1/2, O(1)]$, even relative to an integer factoring oracle. The factoring oracle accelerates norm factorization but does not alter the probability that candidate norms are smooth. Hence the $L_D[1/2]$ bottleneck is structural, not arithmetic.

**Proof sketch.** Set the factor base size $B = L_D[a, c]$ and let $X = D^{O(1)}$ be the size of candidate relation norms, so $\log X \asymp \log D$. The smoothness parameter is

> $$u = \frac{\log X}{\log B} \asymp \frac{\log D}{(\log D)^a (\log\log D)^{1-a}} = \frac{(\log D)^{1-a}}{(\log\log D)^{1-a}}.$$

By the Dickman–CEP heuristic the inverse smoothness probability is $\rho(u)^{-1} = L_D[1-a, O(1)]$. Collecting $L_D[a, O(1)]$ independent relations (one per factor-base element) at cost $\rho(u)^{-1}$ each gives total relation-collection cost

> $$L_D[a, O(1)] \cdot L_D[1-a, O(1)] = L_D[\max(a, 1-a), O(1)].$$

This is minimized at $a = 1/2$, giving $L_D[1/2, O(1)]$.

A factoring oracle replaces the per-relation norm factorization step (cost $L_D[0]$) with essentially free factoring, but does not change the *probability* that a given candidate norm is $B$-smooth — that depends only on the size of $X$ and $B$. Hence $u$ and $\rho(u)$ are unchanged, and the balance point $a = 1/2$ persists. $\square$

### Theorem 2 — Infrastructure period barrier (generic model)

In the generic infrastructure model — where algorithms evaluate the group law and distance function as black-box oracles but have no access to internal arithmetic structure — any classical algorithm finding the infrastructure period $R_K$ by distance-testing requires $\Omega(\sqrt{R_K})$ oracle queries. Baby-step/giant-step methods achieve $O(\sqrt{R_K})$ queries and are optimal within this model.

**Note.** This is a model-relative lower bound, analogous to the Generic Group Model lower bound for DLP. It does not exclude algorithms that exploit specific arithmetic properties of the real quadratic infrastructure — for example, algorithms based on lattice reduction, Arakelov theory, or number-theoretic properties of the continued fraction expansion of $\sqrt{N}$ — that fall outside the black-box oracle model.

---

## 6. Conclusion and corollary

**Corollary.** A Joux-style breakthrough below $L_D[1/2]$ for real quadratic regulators requires a mechanism outside both the smooth-relation model (Theorem 1) and the generic infrastructure model (Theorem 2). Concretely: either a non-factorization-dependent Frobenius analogue, or a new semiprime-specific prefix-to-period law for continued fractions of $\sqrt{pq}$.

No such mechanism is known. The Joux/BGJT bridge to real quadratic factorization is closed within the studied models.

---

## References

**[BGJT 2014]** R. Barbulescu, P. Gaudry, A. Joux, E. Thomé. "A heuristic quasi-polynomial algorithm for discrete logarithm in finite fields of small characteristic." *EUROCRYPT 2014*, LNCS 8441, pp. 1–16. Springer. doi:10.1007/978-3-642-55220-5_1

**[Biasse–Fieker 2014]** J. Biasse, C. Fieker. "Subexponential class group and unit group computation in large degree number fields." *LMS Journal of Computation and Mathematics* 17 (2014), 385–403. doi:10.1112/S1461157014000345

**[Buchmann 1990]** J. Buchmann. "A subexponential algorithm for the determination of class groups and regulators of algebraic number fields." *Séminaire de Théorie des Nombres, Paris 1988–1989*, Progress in Mathematics 91, Birkhäuser, 1990, pp. 27–41.

**[Hafner–McCurley 1989]** J.L. Hafner, K.S. McCurley. "A rigorous subexponential algorithm for computation of class groups." *Journal of the American Mathematical Society* 2 (1989), no. 4, 837–850. doi:10.2307/1990896

**[Joux 2013]** A. Joux. "A new index calculus algorithm with complexity $L(1/4 + o(1))$ in small characteristic." *SAC 2013*, LNCS 8282, pp. 355–379. Springer, 2014. doi:10.1007/978-3-662-43414-7_18

**[Shanks 1971]** D. Shanks. "Class number, a theory of factorization, and genera." *Proc. Symposia in Pure Mathematics*, vol. 20, Amer. Math. Soc., 1971, pp. 415–440.

**[Shoup 1997]** V. Shoup. "Lower bounds for discrete logarithms and related problems." *EUROCRYPT 1997*, LNCS 1233, pp. 256–266. Springer. doi:10.1007/3-540-69053-0_18 *(cited for the generic group model lower bound underlying Theorem 2)*

**[Williams 1982]** H.C. Williams. "A $p+1$ method of factoring." *Mathematics of Computation* 39 (1982), no. 159, 225–234.

**[Williams 1981]** H.C. Williams. "A modification of the factorization algorithm of Brillhart, Morrison and Selfridge." *Mathematics of Computation* 36 (1981), no. 154, 399–403. *(SQUFOF with multipliers)*
