# Factor–Regulator Complexity Bridge in Real Quadratic Fields

## A conditional barrier and a sharpened open attack via half-distance inversion and square-form localization

**Project:** Faktorisierung 1  
**Date:** 2026-05-06  
**Status:** Working paper / research closure for the main FACTOR–REG track  
**Author:** ChatGPT research pass, curated for follow-up work

---

## Abstract

We study whether a classical factoring breakthrough for semiprimes \(N=pq\) can be obtained from the real quadratic regulator of
\[
K=\mathbb Q(\sqrt N).
\]
The naive route
\[
R_K \longrightarrow h_KR_K \longrightarrow h_K \longrightarrow \operatorname{FACTOR}(N)
\]
is too coarse. A numerical regulator is not equivalent to a Pell solution, and the class number formula provides the product \(h_KR_K\), not a direct factorization certificate.

The main negative result is conditional but sharp: in the class of Buchmann-style fixed-degree real quadratic regulator algorithms based on smooth principal ideal relations, an integer factoring oracle does not remove the \(L_D[1/2]\) bottleneck. The obstruction is the probability of obtaining smooth principal norms, not the cost of factoring those norms.

The main surviving positive direction is much narrower. Schoof's quadratic-field factoring framework shows that, after regulator computation, a nontrivial ambiguous reduced form at distance \(R/2\) on the principal cycle can induce a factorization. This suggests a specific open problem:

> Can one construct the reduced form at infrastructure distance \(R/2\), or locate an appropriate square form in the principal cycle, in time below the classical \(L_D[1/2]\) or SQUFOF-like barrier, without already solving the principal ideal/infrastructure navigation problem?

The paper closes the broad FACTOR–REG route and isolates the remaining live attack as **special half-distance inversion / square-form phase prediction**.

---

## 1. Problem statement

Let \(N=pq\) be an odd semiprime and let
\[
K=\mathbb Q(\sqrt N), \qquad D=\operatorname{disc}(K).
\]
Let \(R_D\) be the real quadratic regulator. The broad hope is:

\[
\text{Compute }R_D\text{ classically below }L_D[1/2]
\quad\Longrightarrow\quad
\text{factor }N\text{ below known classical bounds.}
\]

Throughout,
\[
L_D[\alpha,c]
=
\exp\!\left((c+o(1))(\log D)^\alpha(\log\log D)^{1-\alpha}\right).
\]

The analysis distinguishes four computational problems:

| Problem | Output |
|---|---|
| \(\operatorname{FACTOR}\) | the prime factors \(p,q\) of \(N\) |
| \(\operatorname{REG}_{\mathrm{num}}\) | a numerical approximation to \(R_D\) with \(\operatorname{poly}(\log D)\) bits |
| \(\operatorname{REG}_{\mathrm{unit}}\) | a compact representation of the fundamental unit \(\varepsilon_D\) |
| \(\operatorname{PIP}\) | principal ideal / infrastructure distance information |

This distinction is essential. Hallgren states that factoring reduces to solving Pell's equation, whereas a reduction in the other direction is not known and appears more difficult. Thus a Pell or compact-unit oracle is stronger than a mere numerical regulator oracle.

---

## 2. Prior structural background from the Joux–Buchmann bridge

A previous gated pass on the Joux–Buchmann analogy found that a finite-field-style descent does not transfer to fixed real quadratic fields. The missing object is not just a factor base, but a public Frobenius-like symmetry with a large finite fixed locus and a representation-shrinking identity.

The previous pass concluded:

1. factor bases and principal relations exist in real quadratic fields;
2. the obstruction is the absence of a targeted degree-/norm-halving relation identity;
3. fixed-degree principal relation methods lead to \(L_D[1/2]\), because useful candidate norms remain polynomial in \(D\);
4. a Joux-style descent would require a new public K3/K4 replacement: a non-factorization-dependent relation symmetry that shrinks principal norm size below the fixed-degree polynomial norm regime.

This paper uses that result as background and refines it for the specific FACTOR–REG bridge.

---

## 3. Precision trap: corrected form

The phrase “the class number formula needs exponentially many bits of \(R\)” is too coarse. There are two different precision issues.

### 3.1 Extracting \(h\) from \(hR/R\)

If \(H=hR\) is known and \(R\) is known to sufficient relative precision, then recovering \(h\) by rounding requires error below roughly \(1/(2h)\). Since in the quadratic setting \(h\) is at most roughly polynomial-exponential in \(\sqrt D\), this corresponds to \(O(\log D)\)-scale precision, i.e. polynomially many bits in the input length.

Thus, for class-number rounding alone, the precision barrier is not necessarily exponential.

### 3.2 Recovering the Pell coordinate from \(R\)

The hard precision trap appears when trying to recover the fundamental unit
\[
\varepsilon_D=x+y\sqrt D, \qquad x^2-Dy^2=1.
\]
Since
\[
x=\frac{\varepsilon_D+\varepsilon_D^{-1}}{2}=\cosh R_D,
\]
a numerical error \(\delta\) in \(R_D\) induces an error of size approximately
\[
|\Delta x|\approx \sinh(R_D)\delta \approx x\delta.
\]
To recover \(x\) exactly, or even \(x\bmod N\) by the naive route, one needs roughly
\[
\delta \lesssim e^{-R_D}.
\]
For large regulators this is exponential precision in the input length.

### Conclusion

\[
\operatorname{REG}_{\mathrm{num}}\not\equiv \operatorname{REG}_{\mathrm{unit}}\not\equiv \operatorname{Pell}.
\]

A numerical regulator oracle is weaker than a compact fundamental-unit oracle.

---

## 4. Conditional \(L[1/2]\) barrier for smooth principal relations

Consider algorithms that compute the regulator by collecting relations of the form
\[
(\alpha)=\prod_{\mathfrak p_i\in\mathcal B}\mathfrak p_i^{e_i},
\]
where \(\mathcal B\) is a factor base of prime ideals of norm at most \(B\), and success depends on the smoothness of
\[
N_{K/\mathbb Q}(\alpha).
\]

Let
\[
B=L_D[a,c].
\]
In fixed degree \(2\), candidate relation norms are typically of size \(D^{O(1)}\). Thus
\[
\log X\asymp \log D.
\]
The Dickman/CEP smoothness heuristic gives
\[
\Pr[X\text{ is }B\text{-smooth}]
= L_D[-(1-a),O(1)].
\]
The factor base has size
\[
|\mathcal B|=L_D[a,O(1)].
\]
Therefore, relation collection costs
\[
L_D[\max(a,1-a),O(1)],
\]
which is minimized at
\[
a=1/2.
\]

Hence the smooth-principal-relation model yields
\[
T=L_D[1/2,O(1)].
\]

An integer factoring oracle accelerates the local step “factor \(N_{K/\mathbb Q}(\alpha)\)”, but it does not alter the probability that \(N_{K/\mathbb Q}(\alpha)\) is smooth. Therefore it does not remove the \(L_D[1/2]\) bottleneck.

### Conditional theorem

**Theorem 1.** In the class of fixed-degree real quadratic regulator algorithms based on smooth principal ideal relations, even relative to an integer factoring oracle, the optimal heuristic relation-collection complexity remains \(L_D[1/2,O(1)]\).

This does not prove \(\operatorname{REG}\nleq_P\operatorname{FACTOR}\) in an absolute complexity-theoretic sense. It proves that the standard Buchmann/index-calculus route is not made polynomial by a factoring oracle.

---

## 5. The known Pell-to-factoring bridge

If one has a compact Pell solution
\[
\varepsilon_D=x+y\sqrt D,
\]
then
\[
x^2-Dy^2=1.
\]
For \(D\) divisible by \(N\), in particular for \(D=N\) or \(D=4N\), one obtains
\[
x^2\equiv 1\pmod N.
\]
If
\[
x\not\equiv \pm1\pmod N,
\]
then
\[
\gcd(x-1,N)
\]
yields a nontrivial factor of \(N\).

Thus compact Pell information is factoring-strong. The remaining gap is whether numerical regulator information can be promoted to such residue or compact-unit information without exponential precision or full infrastructure navigation.

---

## 6. Half-distance ambiguous form: revived candidate

The earlier naive idea was:

\[
R_D/2 \longrightarrow \text{ambiguous form} \longrightarrow \text{factor}.
\]

A first objection is that \(R_D/2\) is half a period in the continuous infrastructure component, whereas ambiguous forms are 2-torsion in the form class group. However Schoof's quadratic-field factoring framework makes a more precise statement: after regulator computation, one can compute the ambiguous form at distance \(\tfrac12R\) on the principal cycle; under relevant conditions, this gives a nontrivial factorization.

Thus the corrected candidate is not false. It is:

\[
\boxed{\operatorname{FindFormAtDistance}(R_D/2)\Longrightarrow \operatorname{FACTOR}(N).}
\]

The bottleneck shifts to the inverse infrastructure map:
\[
t\mapsto F_t.
\]

### Open problem A: special half-distance inversion

**Input:** \(D=N\) or \(4N\), and \(R_D\).  
**Output:** the reduced form on the principal cycle at distance \(R_D/2\).  
**Question:** Can this be done in \(o(L_D[1/2])\), or even in \(\operatorname{poly}(\log D)\), without already solving the principal ideal/infrastructure navigation problem?

A positive answer would give a serious factoring candidate. A negative answer would sharply separate numerical regulator knowledge from constructive infrastructure access.

---

## 7. Square-form localization

SQUFOF uses a different but related mechanism:

\[
\text{square form in the principal cycle}
\longrightarrow
\text{form square root}
\longrightarrow
\text{ambiguous form}
\longrightarrow
\text{factor}.
\]

A reduced indefinite binary quadratic form is written
\[
F=(a,b,c),\qquad b^2-4ac=\Delta.
\]
A square form has, in the relevant normal case,
\[
a=s^2.
\]
This imposes
\[
b^2\equiv \Delta\pmod{4s^2}.
\]
But the hard condition is not the congruence. The hard condition is membership in the principal cycle:
\[
(s^2,b,c)\in\mathcal P_\Delta.
\]

### Square-form locator problem

**Input:** \(\Delta\).  
**Output:** a distance or index in the principal cycle at which the leading coefficient is a square.  
**Goal:** Beat the expected SQUFOF-scale search.

The central issue is phase information. The regulator gives the cycle length, but not the locations of the square-form events.

---

## 8. Phase gap

The strongest current obstruction to the square-form route is:

\[
\boxed{\text{The regulator gives the length of the cycle, but not the phase of square-form events.}}
\]

If square-form events are pseudorandomly distributed in the principal cycle with density about \(N^{-1/4}\), then \(N^{1/4}\)-scale search is unavoidable for methods that only test candidate positions. This reproduces the SQUFOF scale.

### Random-cycle lemma

**Lemma 2.** Suppose square-form positions in the principal cycle, conditioned on global invariants such as \(R_D\), class-number-size data and congruence class of \(D\), are equidistributed with density \(\rho\approx N^{-1/4}\). Then any locator using only those global invariants and \(T\) candidate tests has success probability at most approximately \(T\rho\). Constant success probability requires \(T\asymp N^{1/4}\).

This is a model lemma, not a theorem about actual cycles. It identifies exactly what a breakthrough must violate: square-form positions must have nonrandom, computable phase.

---

## 9. Main remaining live hypotheses

### H1. Half-distance special inversion

There is a special algorithm for the point \(R_D/2\) that is asymptotically faster than general infrastructure distance inversion.

This is the strongest live candidate. Its appeal is that \(R/2\) is a single symmetric target, not a random square-form event.

### H2. Square-form phase prediction

The square-form positions in the principal cycle correlate with computable global invariants of \(D\), such as:

- \(R_D\),
- the continued fraction period length,
- congruence class modulo small powers of \(2\),
- norm of the fundamental unit,
- multiplier families,
- genus signatures computable without already factoring \(D\).

A positive result would yield a square-form locator. A negative result would support the random-cycle barrier.

### H3. Compressed congruence trace

Instead of reconstructing \(x\) from \(R\), one might try to compute the trace of the fundamental automorphism modulo \(N\):
\[
\operatorname{tr}(A_D)=2x_D \pmod N.
\]
Naively this requires level-\(N\) congruence data of huge index. A breakthrough would require a compressed automorphic/ray-class method that extracts this residue without constructing the full level-\(N\) object and without knowing the CRT idempotents of \(\mathbb Z/N\mathbb Z\).

This is speculative but precise.

---

## 10. What is exhausted and what is not

### Exhausted or structurally blocked

1. The naive class-number formula route \(R\to h\to \operatorname{FACTOR}\).
2. Fixed-degree smooth principal relation methods below \(L[1/2]\).
3. Generic Joux/BGJT-style descent transfer to \(\mathbb Q(\sqrt N)\).
4. Broad analytic/spectral visibility of \(R\) without an isolation operator.
5. Generic square-form search without phase information.

### Not exhausted

1. Special half-distance inversion at \(R/2\).
2. Square-form phase prediction from computable global invariants.
3. Compressed congruence-trace/ray-class extraction of \(x_D\bmod N\).
4. Empirical phase analysis of square forms in principal cycles for semiprimes.

---

## 11. Proposed next experiment

For many semiprimes \(N=pq\):

1. compute the principal cycle of discriminant \(\Delta=N\) or \(4N\);
2. record regulator \(R\), period length \(L\), norm of the fundamental unit, and continued-fraction data;
3. record all square-form positions \(i\) and normalized phases
   \[
   \theta_i=i/L,\qquad \tau_i=d(F_0,F_i)/R;
   \]
4. record the form at distance closest to \(R/2\);
5. test whether it is ambiguous and whether its coefficients factor \(N\);
6. test correlations of \(\theta_i,\tau_i\) with global invariants not requiring the factorization of \(N\);
7. repeat with SQUFOF multipliers.

A null result supports the phase-gap barrier. A positive correlation gives an explicit candidate locator.

---

## 12. Final assessment

No broad FACTOR–REG equivalence or separation is proved. The cleanest result is conditional:

\[
\boxed{\text{Smooth principal-relation regulator computation remains }L_D[1/2]\text{ even with FACTOR.}}
\]

The cleanest live attack is:

\[
\boxed{R_D + \operatorname{HalfDistanceInversion}(R_D/2)\\Rightarrow \operatorname{FACTOR}(N).}
\]

The central open question is whether half-distance inversion is genuinely easier than general infrastructure navigation. If yes, this is a factoring candidate. If no, it becomes a sharp negative theorem explaining why numerical regulator information does not factor semiprimes.

---

## References and source anchors

1. R. Schoof, *Quadratic fields and factorization*, Computational Methods in Number Theory, Part II, Math. Centre Tracts 155, 1982. Online scan: https://www.mat.uniroma2.it/~schoof/mcpaper.pdf
2. R. Schoof, *Computing Arakelov class groups*, Algorithmic Number Theory: Lattices, Number Fields, Curves and Cryptography, MSRI Publications 44, 2008. Online: https://pub.math.leidenuniv.nl/~stevenhagenp/ANTproc/14schoof.pdf
3. J. E. Gower and S. S. Wagstaff, Jr., *Square Form Factorization*, Mathematics of Computation 77 (2008), 551–588. Online: https://homes.cerias.purdue.edu/~ssw/squfof.pdf
4. C. Bradford and S. S. Wagstaff, Jr., *Square Form Factorization, II*. Online: https://homes.cerias.purdue.edu/~ssw/squfof2.pdf
5. S. Hallgren, *Polynomial-time quantum algorithms for Pell's equation and the principal ideal problem*, Journal of the ACM 54(1), 2007. Author page / abstract: https://authors.library.caltech.edu/records/wwa5n-3k633
6. J.-F. Biasse and C. Fieker, *Subexponential class group and unit group computation in large degree number fields*, LMS Journal of Computation and Mathematics 17 (2014), 385–403. Online: https://www.cambridge.org/core/journals/lms-journal-of-computation-and-mathematics/article/subexponential-class-group-and-unit-group-computation-in-large-degree-number-fields/4387ACB036E3358143A563F196E386CB
7. Internal prior pass: *Joux–Buchmann Bridge: Gated Research Pass*, uploaded project source `Joux-Buchmann Faktorisierung.txt`.

---

## Appendix: precise open problems

### OP1. Half-distance inversion lower bound

Prove or disprove that computing the reduced form at distance \(R_D/2\) in the principal cycle is as hard as general infrastructure distance inversion, in a classical black-box infrastructure model.

### OP2. Half-distance explicit normal form

Derive the exact coefficient normal form of the ambiguous reduced form at distance \(R_D/2\) for \(\Delta=N\) and \(\Delta=4N\). Determine exactly when it yields a nontrivial factor.

### OP3. Square-form phase distribution

Test and, if possible, prove whether square-form positions in the principal cycle are equidistributed after conditioning on global invariants computable without factoring \(N\).

### OP4. Congruence trace compression

Determine whether \(\operatorname{tr}(A_D)\bmod N\), where \(A_D\) is the automorphism attached to the fundamental unit, can be computed from regulator/geodesic data without full level-\(N\) congruence expansion or CRT idempotents.

### OP5. REG oracle separation refinement

Formalize a separation between \(\operatorname{REG}_{\mathrm{num}}\) and \(\operatorname{REG}_{\mathrm{unit}}\) under a precision- or representation-bounded oracle model.
