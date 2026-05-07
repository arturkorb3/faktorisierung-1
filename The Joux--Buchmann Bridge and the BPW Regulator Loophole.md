# The Joux--Buchmann Bridge and the BPW Regulator Loophole

**Project:** Faktorisierung 1  
**Document type:** consolidated research paper / negative-result manuscript  
**Status:** technical draft, not peer-reviewed  
**Main conclusion:** no classical sub-\(L[1/2]\) factoring path was found through the Joux--Buchmann regulator pipeline or through direct real-quadratic regulator shortcuts.

---

## Abstract

We investigate whether the Joux/BGJT quasi-polynomial descent for discrete logarithms in small-characteristic finite fields admits an analogue in the Buchmann framework for computing class groups and regulators of real quadratic fields

\[
K=\mathbb Q(\sqrt N), \qquad N=pq.
\]

The motivating pipeline is the classical regulator-to-factorization strategy: a sufficiently fast computation of the real quadratic regulator \(R_K\), together with class number formula information, would imply a faster factoring method for semiprimes. The target was an asymptotic factoring algorithm beating the Number Field Sieve threshold \(L[1/3]\).

The project decomposes the Joux method into five structural components: smoothness basis, on-the-fly elimination relations, Frobenius symmetry, recursive tower/subfield descent, and representation switching. The attempted transfer to \(\mathcal O_K\) fails at the Frobenius/tower layer. More sharply, within fixed-degree real quadratic fields, any Buchmann-style regulator algorithm based on smooth principal-ideal relations faces a fixed-degree norm-smoothness barrier: relation norms remain polynomial in the discriminant, and the Canfield--Erdos--Pomerance/Dickman smoothness balance optimizes at \(L[1/2]\), not \(L[1/3]\).

The remaining loophole is a regulator-specific shortcut that avoids large smooth-relation matrices. We analyze direct infrastructure, Arakelov, analytic class number formula, hidden-period, spectral, and continued-fraction approaches. In the generic infrastructure-period model, classical direct regulator computation has a baby-step/giant-step barrier. Continued-fraction leakage for \(\sqrt{pq}\) is also examined: early gcd hits, palindromy, negative Pell parity, SQUFOF square-form leakage, and prefix-to-period statistical prediction. No exploitable semiprime-specific anomaly is found.

The final result is negative but structurally precise: a Joux--Buchmann factoring breakthrough is not obtained. A genuine breakthrough would require either a non-factorization-dependent Frobenius-like relation symmetry in real quadratic infrastructure, or a new semiprime-specific prefix-to-period law for continued fractions of \(\sqrt{pq}\). No such mechanism is currently identified.

---

## 1. Problem statement

Let

\[
N=pq
\]

be an RSA-type semiprime and let

\[
K=\mathbb Q(\sqrt N)
\]

be a real quadratic field with discriminant \(D\). The regulator \(R_K\) is the logarithm of a fundamental unit. The broad hope is that a faster computation of \(R_K\) might yield a faster factorization of \(N\), via the real quadratic class number formula and associated regulator/factorization pipelines.

The concrete proposal investigated here is a possible bridge from Joux's small-characteristic finite-field discrete logarithm algorithms to the Buchmann machinery for real quadratic class groups and regulators.

The target was:

\[
\text{factor }N=pq\text{ asymptotically faster than }L_N[1/3],
\]

where

\[
L_X[\alpha,c]
=\exp\!\left((c+o(1))(\log X)^\alpha(\log\log X)^{1-\alpha}\right).
\]

The inquiry was conducted using strict gates. If a gate fails, the project terminates with the strongest available negative result rather than drifting into an unrelated approach.

---

## 2. Executive conclusion

No faster factoring algorithm was found.

The strongest consolidated conclusion is:

> **Main negative conclusion.** The Joux--Buchmann transfer fails as a route to sub-\(L[1/2]\), and a fortiori sub-\(L[1/3]\), real quadratic regulator computation. In fixed real quadratic degree, smooth-principal-relation methods are forced to \(L[1/2]\) by norm smoothness. Direct regulator approaches reduce to infrastructure period finding, analytic \(hR\)-product ambiguity, candidate verification, or continued-fraction leakage; none gives a classical sub-\(L[1/2]\) path.

This does not prove that no classical factoring breakthrough exists. It proves a narrower and more useful statement: this specific regulator/Joux/Buchmann/infrastructure route does not currently supply one, and any positive result must avoid the identified barriers.

---

## 3. Structural skeleton of the Joux method

We decompose the Joux/BGJT method into five components.

| ID | Component | Role |
|---|---|---|
| K1 | Smoothness basis choice | Choose small objects that generate relations and support descent. |
| K2 | On-the-fly relations / elimination | Produce target-specific relations reducing complexity. |
| K3 | Frobenius symmetry | Supply a large fixed-locus identity and low-complexity rewrite. |
| K4 | Recursive subfield/tower descent | Support repeated complexity reduction. |
| K5 | Representation switching | Choose representations in which descent is cheap. |

### 3.1 K1: smoothness basis choice

A descent-friendly smoothness basis is not merely a small generating set. It must support a complexity measure, a smoothness test, and recursive replacement of a target object by simpler objects. In finite-field index calculus, this is often a factor base of low-degree polynomials. In number fields, it becomes a factor base of prime ideals of bounded norm.

This component transfers partially to real quadratic fields. Buchmann-style algorithms already use factor bases of prime ideals. Therefore K1 is not the fundamental obstruction.

### 3.2 K2: on-the-fly relations

The elimination step needs target-specific relations. In BGJT, one transforms identities such as

\[
X^q-X=\prod_{a\in\mathbb F_q}(X-a)
\]

or projectively

\[
X^qY-XY^q=\prod_{(\alpha:\beta)\in\mathbb P^1(\mathbb F_q)}(\beta X-\alpha Y)
\]

and then uses the representation relation

\[
X^q\equiv h_0(X)/h_1(X)
\]

to obtain lower-degree factors. This is not merely relation collection; it is degree-reducing elimination.

In real quadratic fields, on-the-fly relations exist in a weak sense: one may search for \(\alpha\in\mathcal O_K\) or \(\alpha\in\mathfrak a\) and factor \((\alpha)\) over a factor base. But there is no known degree-halving or norm-shrinking identity analogous to the BGJT elimination step.

Thus K2 is:

> **Operationally yellow but BGJT-functionally red.**

There are relations, but not the Joux elimination mechanism.

### 3.3 K3: Frobenius symmetry

The BGJT/Joux descent depends on a public endomorphism with four simultaneous properties:

1. a large explicitly enumerable fixed locus;
2. an identity that splits completely over small objects;
3. compatibility with a low-complexity representation relation;
4. enough symmetry to create many independent target-specific relations.

In small-characteristic finite fields, this is the Frobenius map

\[
x\mapsto x^q.
\]

It fixes \(\mathbb F_q\), gives the splitting identity \(X^q-X\), and interacts with the chosen representation via \(X^q\equiv h_0/h_1\).

For

\[
K=\mathbb Q(\sqrt N),
\]

the intrinsic \(\mathbb Q\)-automorphism group is only

\[
\operatorname{Aut}_{\mathbb Q}(K)=\{1,\iota\},
\qquad \iota(\sqrt N)=-\sqrt N.
\]

This two-element symmetry cannot replace the Frobenius fixed-locus identity.

### 3.4 K4: recursive subfield/tower descent

Finite fields have rich subfield/tower structures. BGJT uses embeddings and degree choices to make descent recursive and quasi-polynomial.

A real quadratic field has no nontrivial internal intermediate fields. External towers can be introduced, but they must satisfy three conditions:

1. relations upstairs must push down to information about \(R_K\);
2. discriminant and norm growth must remain controlled;
3. the tower must be constructible without knowing \(p,q\) or class-field data comparable to the target.

Known natural candidates fail at least one condition.

### 3.5 K5: representation switching

Representation switching exists in number fields: ideals, binary quadratic forms, reduced ideals, infrastructure, Arakelov divisors, equation orders, and auxiliary fields. However, in fixed degree \(2\), these switches do not create the growing degree/height balance that permits \(L[1/3]\)-type algorithms in large-degree number-field families.

Thus K5 is:

> **Representationally yellow, asymptotically red for the target \(L[1/3]\).**

---

## 4. Phase gates for the Joux--Buchmann bridge

| Gate | Result | Reason |
|---|---:|---|
| Gate I | PASS | K1--K5 abstraction is coherent. |
| Gate II | PASS | K2/K5 have weak analogues, so not all entries are red. |
| Gate III | PASS | Replacement mechanisms can be formulated. |
| Gate IV | FAIL | All pipelines collapse to \(L[1/2]\) or worse. |

The failure occurs at the complexity stage, not at the level of vocabulary. Number fields have factor bases, relations, and representation switches, but they lack the BGJT Frobenius/tower mechanism that shrinks targets recursively.

---

## 5. The fixed-degree smooth-principal-relation barrier

This is the strongest theorem-level result of the project.

### Theorem 1: Fixed-degree norm-smoothness barrier

Let \(K=\mathbb Q(\sqrt N)\) be a fixed-degree real quadratic field with discriminant \(D\). Consider Buchmann-style regulator or class-group algorithms whose relations are obtained by principal ideals

\[
(\alpha)=\prod_i \mathfrak p_i^{e_i}
\]

and whose success depends on the smoothness of the integer norm

\[
|N_{K/\mathbb Q}(\alpha)|.
\]

If the useful relation norms are generically polynomial in \(D\), then the optimal smoothness balance of such algorithms is \(L_D[1/2]\). In particular, this class cannot reproduce a Joux/BGJT \(L[1/3]\)-or-better descent in fixed real quadratic degree.

### Proof sketch

Let the factor-base bound be

\[
y=L_D[a,c]
=\exp\!\left((c+o(1))(\log D)^a(\log\log D)^{1-a}\right).
\]

In fixed degree \(2\), useful principal relation norms are typically of size

\[
X=D^{O(1)}.
\]

Thus

\[
\log X\asymp \log D.
\]

The smoothness parameter is

\[
u=\frac{\log X}{\log y}
\asymp
\frac{(\log D)^{1-a}}{(\log\log D)^{1-a}}.
\]

By the standard Dickman/Canfield--Erdos--Pomerance heuristic,

\[
\Pr[X\text{ is }y\text{-smooth}]
\approx \exp(-u\log u)
= L_D[-(1-a),O(1)].
\]

The factor base size is \(L_D[a,O(1)]\). Therefore relation collection costs

\[
L_D[\max(a,1-a),O(1)].
\]

The optimum is achieved at

\[
a=\frac12,
\]

yielding

\[
L_D[1/2].
\]

To reach \(L_D[1/3]\), one would need relation norms substantially below the fixed-degree polynomial-in-\(D\) regime, roughly of \(L_D[2/3]\)-type after balancing. No such norm shrinkage mechanism exists in the fixed real quadratic setting considered here.

### Interpretation

This theorem does not rule out every regulator algorithm. It rules out the broad class:

\[
R_K \leftarrow \text{many smooth principal-ideal relations}.
\]

That is precisely the Buchmann-style route and the natural Joux-transfer route.

---

## 6. Frobenius obstruction

### Theorem 2: Intrinsic Frobenius obstruction

A Joux-style K3 component requires a public endomorphism \(\Phi\) with a large finite fixed locus and a low-complexity rewrite identity. In

\[
K=\mathbb Q(\sqrt N),
\]

no such intrinsic \(\Phi\) exists. Any residue-level substitute that separates the hidden prime components of \(N=pq\) requires factorization data.

### Proof sketch

Every \(\mathbb Q\)-field endomorphism of a number field is an automorphism. Since \(K/\mathbb Q\) is quadratic,

\[
\operatorname{Aut}_{\mathbb Q}(K)=\{1,\iota\},
\]

where

\[
\iota(\sqrt N)=-\sqrt N.
\]

The nontrivial symmetry has order \(2\) and fixed field \(\mathbb Q\). It cannot yield a large projective fixed-locus identity analogous to

\[
X^q-X=\prod_{a\in\mathbb F_q}(X-a).
\]

One may reduce modulo rational primes or prime ideals and obtain finite-field Frobenius maps locally. However, a global operation modulo \(N=pq\) that treats the hidden \(p\)- and \(q\)-components separately requires CRT idempotents of

\[
\mathbb Z/N\mathbb Z\simeq \mathbb F_p\times\mathbb F_q.
\]

Those idempotents immediately yield nontrivial gcds with \(N\). Hence any useful hidden-prime Frobenius substitute presupposes the factorization.

---

## 7. Tower descent obstruction

The tower obstruction is weaker than the previous two theorem-level claims. It is not a universal impossibility theorem for all imaginable external towers. It is a classification of the natural candidates.

### Proposition 3: Failure of known natural tower substitutes

Known natural external tower substitutes for real quadratic regulator descent fail to provide a Joux-style recursive descent because they violate at least one of the following requirements:

1. useful relations upstairs push down to regulator/class-group information in \(K\);
2. discriminants and coefficient heights remain balanced;
3. the tower is constructible without knowing \(p,q\) or class/ray class data comparable to the target.

### Candidate failures

- **Cyclotomic/Kummer towers:** if the degree grows, discriminants and coefficient heights grow too quickly; if the degree is fixed, no asymptotic recursive descent is gained.
- **Unramified or class-field towers:** construction requires class group or ray class group information, which is already target-level data.
- **Towers ramified at \(p,q\):** exploiting the useful ramification requires identifying the hidden prime factors.
- **Arakelov/infrastructure towers:** improve language and geometry, but do not supply a large fixed-locus identity or norm-shrinking descent.

Thus the honest statement is:

> No known natural tower substitute provides the missing K4 component. This is not a proof that no exotic tower can ever work.

---

## 8. Phase IV complexity bottleneck

A generic Buchmann-style pipeline is:

```text
Input: N = pq, D = disc(Q(sqrt(N))).

1. Build a factor base B = {prime ideals p_i : Norm(p_i) <= y}.
2. For random or target ideals a:
       find a short alpha in a or in a product a * prod p_i^{e_i}.
3. Factor Norm(alpha).
4. If Norm(alpha) is y-smooth:
       record the exponent relation among prime ideals.
5. Repeat until the relation matrix has full rank.
6. Extract class group and regulator from HNF/SNF and unit reconstruction.
7. Use regulator-to-factorization information if available.
```

The bottleneck is step 4: smoothness of polynomial-size norms in fixed degree. This is the precise source of the \(L[1/2]\) barrier.

The bottleneck is **not**:

- absence of a factor base;
- absence of relation lattices;
- linear algebra alone;
- the analytic class number formula.

It is:

> no public targeted relation identity in \(\mathcal O_K\) turns a target ideal into strictly smaller ideals while keeping principal relation norms below the fixed-degree polynomial norm regime.

---

## 9. The BPW / Loophole 3 program

The smooth-relation theorem leaves one serious loophole:

\[
R_K \leftarrow \text{direct regulator computation without enough class-group relations}.
\]

This is the BPW loophole.

The question becomes:

> Can one compute \(R_K\) for \(K=\mathbb Q(\sqrt N)\) classically below \(L[1/2]\), without constructing a large smooth-relation matrix?

We tested the following direct mechanisms:

| Candidate | Mechanism | Status |
|---|---|---|
| Continued fractions / infrastructure | Find the principal cycle period | Fails generically by baby-step/giant-step barrier |
| Arakelov class group | Geometric model of infrastructure | Useful language, no faster period finder |
| Analytic class number formula | Compute \(h_KR_K\) via \(L(1,\chi_D)\) | Product ambiguity: does not isolate \(R_K\) |
| Regulator verification | Verify a candidate regulator | Certification only, not discovery |
| Hidden period | Regulator as hidden period | Quantum positive, classical barrier remains |
| Spectral/trace formula | Geodesic lengths or averages | Batch/average information, no individual shortcut |

### 9.1 Empirical independence: the Kuroda ratio

A direct test of the REG ≤ FACTOR direction is the question: given the factorization
\(N = pq\), can one compute \(R_K = R_{\mathbb Q(\sqrt{pq})}\) in polynomial time, for
instance via a simple relation to \(R_{\mathbb Q(\sqrt p)}\) and \(R_{\mathbb Q(\sqrt q)}\)?

A natural candidate is a Kuroda-type multiplicative formula
\[
R_{pq} \stackrel{?}{\approx} c \cdot R_p \cdot R_q.
\]

We computed the ratio \(R_{pq}/(R_p \cdot R_q)\) for 34 small semiprime pairs
\((p,q)\) with \(p,q \in [5,47]\).

| Statistic | Value |
|---|---:|
| Minimum | 0.1033 |
| Maximum | 1.9495 |
| Mean | 0.6171 |
| Range factor | \(\approx\times 19\) |

A representative sample:

| \(p\) | \(q\) | \(R_{pq}\) | \(R_p\) | \(R_q\) | ratio |
|---:|---:|---:|---:|---:|---:|
| 5 | 19 | 4.357 | 2.887 | 5.829 | 0.259 |
| 11 | 23 | 22.587 | 2.993 | 3.871 | 1.949 |
| 17 | 19 | 3.583 | 4.189 | 5.829 | 0.147 |
| 17 | 23 | 16.502 | 4.189 | 3.871 | 1.018 |
| 29 | 31 | 4.094 | 4.942 | 8.020 | 0.103 |
| 29 | 41 | 30.461 | 4.942 | 4.159 | 1.482 |
| 41 | 47 | 32.167 | 4.159 | 4.564 | 1.694 |

The ratio varies by a factor of approximately 19 with no visible monotone dependence
on \(p, q\), \(|p-q|\), or \(N\). The regulator \(R_{pq}\) is empirically **independent**
of \(R_p\) and \(R_q\).

**Consequence.** There is no simple factorization-derived formula for \(R_{pq}\).
Even complete knowledge of \(p\) and \(q\) does not yield \(R_{pq}\) via any
multiplicative Kuroda-style relation. This empirically supports the theoretical argument
that REG is not polynomially reducible to FACTOR via this route (Scenario C is implausible),
and that \(R_{pq}\) contains genuinely new arithmetic information independent of the
prime factorization.

---

## 10. Generic infrastructure-period barrier

### Theorem 4: Generic infrastructure barrier

In a black-box real quadratic infrastructure model allowing:

1. baby steps;
2. giant steps / composition;
3. reduction;
4. equality testing of reduced ideals/forms;
5. distance accumulation;
6. compact representation of encountered states;

but disallowing smooth principal-relation collection and independent class-number computation, classical computation of the infrastructure period \(R_K\) requires generically

\[
\Omega(\sqrt{R_K})
\]

operations.

### Proof sketch

The infrastructure behaves as a cyclic object of unknown circumference. Until the algorithm obtains a collision, return, or order certificate, its transcript is compatible with many possible periods. In a generic cycle, finding the period requires a birthday-type collision. Baby-step/giant-step achieves this in \(O(\sqrt R)\) steps, and generic group/order-finding lower-bound frameworks support matching square-root barriers.

### Limitation

This is not an absolute integer-computation lower bound. It only rules out generic infrastructure period finding. It leaves open algorithms exploiting special arithmetic structure of the continued-fraction sequence.

Thus the remaining escape hatch is:

\[
\text{non-generic continued-fraction leakage for }\sqrt{pq}.
\]

---

## 11. Continued-fraction leakage for \(\sqrt{pq}\)

Let

\[
\sqrt N=[a_0;\overline{a_1,a_2,\ldots,a_\ell}].
\]

The period length \(\ell\), the fundamental unit, and the regulator are deeply connected. The question is whether a short prefix

\[
a_1,\ldots,a_m, \qquad m\ll \sqrt R,
\]

can predict \(\ell\), \(R_K\), or the factors \(p,q\).

### 11.1 Early gcd leakage

The continued-fraction recurrences involve values \(P_i,Q_i\) satisfying

\[
Q_i\mid N-P_i^2.
\]

A direct leak would be

\[
\gcd(Q_i,N)\in\{p,q\}.
\]

For balanced \(p\sim q\sim N^{1/2}\), this typically requires

\[
P_i\equiv 0\pmod p
\]

or modulo \(q\). Under even mild randomness, this has probability about

\[
1/p\sim N^{-1/2}
\]

per trial. This is far too rare for a subexponential breakthrough.

**Status:** red.

### 11.2 Near-square leakage

If \(p\) and \(q\) are close, Fermat-style methods and early continued-fraction data can factor quickly:

\[
N=A^2-B^2.
\]

This only covers weak-key families. It is not an asymptotic factoring algorithm for generic balanced semiprimes.

**Status:** red except for special cases.

### 11.3 Palindromy

The continued-fraction period of \(\sqrt N\) has palindromic structure. This is genuine arithmetic structure, but it helps only after one already knows the endpoint or midpoint of the period. It is a certificate, not a predictor.

**Status:** red.

### 11.4 Negative Pell parity

The parity of \(\ell\) is linked to solvability of

\[
x^2-Ny^2=-1.
\]

This gives at most one bit of information. It does not recover the regulator or the factors without period-scale information.

**Status:** red.

### 11.5 SQUFOF square-form leakage

SQUFOF is the strongest known evidence that real quadratic infrastructure leaks factorization information. It searches for square forms in the principal cycle; when found, a reverse step may reveal a factor.

However, its expected scale for semiprimes is roughly \(N^{1/4}\), not subexponential in \(\log N\). Since

\[
N^{1/4}=\exp\!\left(\frac14\log N\right),
\]

this is exponential in the input size.

**Status:** real leak, but asymptotically too slow.

### 11.5.1 Empirical confirmation: half-period multiplier probe

A direct half-period experiment was conducted on random semiprimes of 32–40 bits. The CF expansion of \(\sqrt{mN}\) was run to index \(L/2\) (the half-period) for small multipliers \(m \in \{1,3,5,7,11,13,\ldots\}\), and \(\gcd(Q_{L/2}, N)\) was evaluated.

**Results (half-period gcd probe):**

| Bits | Samples | Avg. period $L$ | Even-$L$ fraction | Half-hits, $m=1$ |
|---:|---:|---:|---:|---:|
| 32 | 50 | 20 203 | 88 % | 35/50 |
| 36 | 40 | 74 079 | 88 % | 26/40 |
| 40 | 20 | 285 550 | 95 % | 16/20 |

The failures concentrated on the case \(Q_{L/2} = 2\), corresponding to the trivially ambiguous form \((2, 0, -N/2)\) with \(\gcd(2,N)=1\). Running small SQUFOF-style multipliers rescued all remaining cases:

| Bits | Samples | Full coverage with small multipliers | Multipliers used |
|---:|---:|---:|:---|
| 32 | 50 | 50/50 | \{1,3,5,7,11\} |
| 36 | 40 | 40/40 | \{1,3,5,7,21,57\} |
| 40 | 20 | 20/20 | \{1,3,7,13\} |

**Interpretation.** The half-period of \(\sqrt{mN}\) carries an ambiguous form \((A, B, C)\) with \(\gcd(A, N) \in \{p, q\}\) in the non-trivial case. The multiplier strategy replaces the discriminant \(4N\) by \(4mN\), producing a different ambiguous form and avoiding the trivial \(Q = 2\) obstruction. This is precisely the Shanks--Williams SQUFOF multiplier heuristic (1982) in the half-period guise.

**Irreducibility of "direct half-state construction".** The ambiguous form at \(L/2\) for \(N = pq\) is, in canonical coordinates, \((p, 0, -q)\). Writing this form explicitly requires knowing \(p\) and \(q\). Any algorithm constructing it from \(N\) alone without a \(O(L/2)\) infrastructure walk would therefore directly factor \(N\) — a circular reduction. The "direct half-state" goal is thus not a speedup of SQUFOF; it is equivalent to factorization itself.

**Confirmed:** the expected scale is \(O(L/2) = O(N^{1/4})\), consistent with the asymptotic analysis in this section and with Theorem 4.

### 11.6 Prefix-to-period statistics

The final micro-loophole is a possible statistical anomaly:

> The early partial quotients of \(\sqrt{pq}\) might differ from generic quadratic irrational continued fractions in a way that predicts the full period.

Known distributional results for arithmetic families of quadratic irrationals generally point in the opposite direction: continued-fraction period statistics often converge toward Gauss--Kuzmin-type behavior and geodesic equidistribution. These are not lower bounds for semiprimes, but they provide negative evidence against simple prefix anomalies.

**Status:** theoretically open, no mechanism found.

---

## 12. Conditional BPW theorem

The strongest honest statement for the final loophole is conditional.

### Theorem 5: Conditional prefix-barrier statement

Assume that the continued-fraction prefix of \(\sqrt{pq}\) has no non-generic predictive statistic for the first-return time of the corresponding infrastructure cycle beyond generic Gauss-map behavior. Then no classical algorithm using only a sub-\(\sqrt R\) prefix of the continued fraction can compute \(R_K\) or factor \(N\) through regulator recovery.

### Interpretation

If the prefix behaves statistically like a typical continued-fraction orbit, it does not contain enough actionable information to predict the first return. This is the generic infrastructure barrier translated into continued-fraction language.

### What would break the theorem

A breakthrough would require one of the following:

1. **Prefix-to-period law:**
   \[
   (a_1,\ldots,a_m),\quad m=L_N[\alpha],\ \alpha<1/2,
   \]
   determines or sharply predicts \(\ell(\sqrt{pq})\).

2. **Early hidden factor hit:** among the first \(L_N[\alpha]\), \(\alpha<1/2\), infrastructure states, one usually encounters a form exposing \(p\) or \(q\).

3. **Semiprime-specific distribution anomaly:** partial quotients of \(\sqrt{pq}\) differ algorithmically from generic \(\sqrt D\) in a detectable and exploitable way.

No such mechanism was found.

---

## 13. Consolidated gate table

| Route | Result | Reason |
|---|---:|---|
| Joux-style Frobenius transfer | FAIL | No intrinsic large Frobenius-like symmetry in \(\mathbb Q(\sqrt N)\). |
| Buchmann smooth relations | FAIL at \(L[1/2]\) | Fixed-degree norm-smoothness barrier. |
| External towers | FAIL for known candidates | Discriminant/norm growth, class-field data, or hidden factor dependence. |
| Representation switching | FAIL for target | Exists, but does not change fixed-degree smoothness exponent. |
| Direct infrastructure period finding | FAIL generically | \(\sqrt R\) baby-step/giant-step barrier. |
| Analytic \(hR\) computation | FAIL standalone | Does not isolate \(R\) from \(hR\). |
| Hidden period | Quantum positive, classical fail | Quantum algorithms excluded; classical no shortcut. |
| SQUFOF leakage | FAIL asymptotically | Real leak, but \(N^{1/4}\)-scale. |
| CF prefix anomaly | Open but unsupported | No semiprime-specific predictor found. |

---

## 14. Final conclusion

The complete research pass yields a negative result.

\[
\boxed{
\text{No classical sub-}L[1/2]\text{ factoring path was found through real-quadratic regulator computation.}
}
\]

More specifically:

\[
\boxed{
\text{The Joux--Buchmann bridge fails at the Frobenius/tower layer.}
}
\]

\[
\boxed{
\text{Smooth principal-relation regulator algorithms in fixed degree optimize at }L[1/2].
}
\]

\[
\boxed{
\text{Direct infrastructure/continued-fraction methods have no known sub-}L[1/2]\text{ shortcut.}
}
\]

The only remaining honest open direction is extremely narrow:

\[
\boxed{
\text{Find a semiprime-specific prefix-to-period anomaly in the continued fraction of }\sqrt{pq}.
}
\]

No such anomaly was found.

---

## 15. Suggested paper structure

A coherent publication program would split the results into two negative papers and one open-problem note.

### Paper A: Fixed-degree smooth-principal-relation barrier

Main result: Theorem 1.  
Supporting result: Theorem 2.  
Message: Joux--Buchmann regulator computation cannot beat \(L[1/2]\) inside smooth-principal-relation algorithms.

### Paper B: Generic infrastructure-period barrier

Main result: Theorem 4.  
Message: direct classical regulator computation via infrastructure period finding faces a \(\sqrt R\) generic barrier.

### Paper C: Continued-fraction leakage and semiprime anomalies

Status: open-problem paper.  
Message: all known continued-fraction leaks are too weak, too late, or special-case only; a breakthrough requires a prefix-to-period law for \(\sqrt{pq}\).

---

## 16. References and source anchors

The draft is based on the following literature anchors and project notes.

1. Antoine Joux, *A new index calculus algorithm with complexity \(L(1/4+o(1))\) in very small characteristic*, 2013.
2. Razvan Barbulescu, Pierrick Gaudry, Antoine Joux, Emmanuel Thome, *A heuristic quasi-polynomial algorithm for discrete logarithm in finite fields of small characteristic*, Eurocrypt 2014.
3. Robert Granger, Thorsten Kleinjung, Jens Zumbragel, *On the discrete logarithm problem in finite fields of fixed characteristic*, Crypto 2018.
4. Antoine Joux, Celine Pierrot, *The special number field sieve in \(\mathbb F_{p^n}\)*, 2014.
5. Johannes Buchmann, *A subexponential algorithm for the determination of class groups and regulators of algebraic number fields*, 1990.
6. Jean-Francois Biasse, Michael Jacobson, *Improvements in the computation of ideal class groups*, 2010.
7. Jean-Francois Biasse, Claus Fieker, *Subexponential class group and unit group computation in large degree number fields*, 2014.
8. Martin Bauer, Safuat Hamdy, *On class group computations using the number field sieve*, 2003.
9. Daniel J. Bernstein-style and Shanks/Buchmann infrastructure literature on real quadratic regulator computation.
10. Hugh C. Williams / Buchmann--Vollmer style baby-step/giant-step regulator algorithms.
11. Gower--Wagstaff, analysis of Shanks's SQUFOF algorithm.
12. Hallgren, quantum polynomial-time algorithms for Pell's equation and principal ideal problems.
13. Aka--Shapira and related results on continued-fraction statistics for arithmetic families of quadratic irrationals.
14. Project note: `Joux-Buchmann Faktorisierung.txt`, uploaded in this workspace.
15. Empirical computations: `code/buchmann_experiments.py` (this project), Python/Decimal, 34 semiprime pairs \(N = pq\), \(p,q \in [5,47]\). Regulators computed via continued-fraction Pell-equation solver.

---

## 17. Research status statement

This manuscript should be read as a structured negative-result draft. Some parts are theorem-level within clearly defined algorithm classes. Other parts are classification or conditional barrier statements. The strongest theorem-level piece is the fixed-degree smooth-principal-relation barrier. The weakest but most important remaining open point is the possibility of a semiprime-specific continued-fraction prefix anomaly.

No implementation phase is justified because Gate IV fails: no candidate pipeline reaches \(L[1/3]\), let alone beats it.
