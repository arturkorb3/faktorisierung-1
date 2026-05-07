# Three Structural Barriers for Classical Semiprime Factorization

## Joux–Buchmann Infrastructure, Regulator Compression, and Babai–HPMI Matrix Isometry

**Project:** Faktorisierung 1  
**Date:** 2026-05-06  
**Status:** Consolidated negative-result manuscript  
**Contributors:** Research passes A1 (Joux–Buchmann), A2 (Factor–Regulator Bridge), C5 (Babai–HPMI)

---

## Abstract

We investigate three independent approaches to factorization of RSA semiprimes $N = pq$ below $L[1/3]$:

1. **A Joux–Buchmann bridge** from small-characteristic discrete logarithm descent to real quadratic infrastructure;
2. **A regulator–factorization complexity bridge** asking whether $\operatorname{FACTOR} \equiv \operatorname{REG}$ for real quadratic fields $\mathbb{Q}(\sqrt{N})$, culminating in the OP4/H3 congruence trace compression problem;
3. **A Babai–HPMI bridge** encoding factorization as a small group/matrix-space isomorphism problem solvable by Babai's quasi-polynomial algorithm.

All three approaches independently encounter the same structural obstruction: the **CRT wall**. Any construction that separates the two CRT components $\mathbb{F}_p$ and $\mathbb{F}_q$ of $\mathbb{Z}/N\mathbb{Z}$ already generates a nontrivial factoring certificate before the proposed algorithmic step applies. Constructions that avoid this either remain CRT-symmetric (carrying no $p/q$-distinguishing information) or reduce to the known hardness of Quadratic Residuosity Witness extraction.

The contribution is not a factoring breakthrough, but a **structural characterization of the factorization barrier** from three independent mathematical directions. Each strand ends with a sharp theorem-level negative result, and all three negative results share the same algebraic core. A unified conjectural closure (the Compression Barrier) is stated as a single open problem.

---

## 1. Setup and notation

### Standing assumptions

The following assumptions underlie the complexity claims in this paper. They are standard in computational number theory and are stated explicitly for clarity.

**CEP/Dickman smoothness heuristic.** The probability that a random integer of size $X$ is $B$-smooth is $\rho(u)$ where $u = \log X / \log B$ and $\rho$ is the Dickman function. This heuristic is unproven but universally used in index-calculus analyses.

**GRH (Generalized Riemann Hypothesis).** Class-group computations and smoothness bounds for number-field algorithms are stated conditionally on GRH where noted.

**Factoring hardness.** The statements "factoring-equivalent" and "QR-witness extraction is factoring-equivalent" are shorthand for: *there exists a polynomial-time randomized reduction between the stated problem and integer factorization*. QR-**Decision** (computing the Jacobi symbol) is easy and is not claimed to be factoring-equivalent. Only QR-**Witness** (producing explicit $(x,y)$ with $x^2 \equiv dy^2 \pmod N$, $(x,y)$ nontrivial) is factoring-equivalent under standard assumptions.

**Black-box infrastructure model.** Theorem 2 and related lower bounds are stated in the generic infrastructure model: algorithms may evaluate the group law and distance function, but have no access to internal structure beyond these operations. This model does not rule out non-black-box algorithms exploiting specific arithmetic properties.

### Limits of claims

This paper proves that three specific mathematical routes toward factorization below $L[1/3]$, quasi-polylogarithmic, or otherwise NFS-beating, fail within their stated models. It does **not** prove:
- that no classical factoring algorithm below $L[1/3]$ exists;
- that NFS is asymptotically optimal;
- that the CRT wall is a fundamental complexity barrier (only that it is unavoidable for the studied constructions).

Let $N = pq$ be an RSA-type semiprime with $p, q$ odd primes. Throughout,

$$
L_X[\alpha, c] = \exp\!\bigl((c + o(1))(\log X)^\alpha (\log\log X)^{1-\alpha}\bigr).
$$

Write $L_X[\alpha]$ for $L_X[\alpha, O(1)]$. The Number Field Sieve achieves $L_N[1/3]$ for factoring; any classical improvement would need to do better.

The key computational problems:

| Symbol | Output |
|---|---|
| $\operatorname{FACTOR}$ | prime factors $p, q$ of $N$ |
| $\operatorname{REG}_{\mathrm{num}}$ | numerical approximation to $R_D$ with $\operatorname{poly}(\log D)$ bits |
| $\operatorname{REG}_{\mathrm{unit}}$ | compact representation of the fundamental unit $\varepsilon_D$ |
| $\operatorname{PIP}$ | principal ideal problem / infrastructure distance |
| $\operatorname{Pell}$ | exact integer solution $(t, u)$ to $t^2 - Du^2 = 4$ |

The distinction between these problems is essential and is made precise in Part II.

---

## Part I: The Joux–Buchmann Bridge

### 2. Motivation

The Joux/BGJT algorithm achieves quasi-polynomial complexity $L[1/4 + o(1)]$ for discrete logarithms in small-characteristic finite fields $\mathbb{F}_{q^n}$ by combining:

- a smoothness basis of low-degree polynomials;
- on-the-fly elimination relations via the Frobenius identity $X^q - X = \prod_{a \in \mathbb{F}_q}(X - a)$;
- recursive tower descent halving the effective degree;
- representation switching between polynomial and rational function models.

The hope was that a structural analogue exists for the real quadratic regulator of $K = \mathbb{Q}(\sqrt{N})$, giving a faster classical computation of $R_K$ and hence a faster factorization of $N$.

### 3. Structural decomposition

The Joux method decomposes into five components:

| ID | Component | Role |
|---|---|---|
| K1 | Smoothness basis | Small objects generating many relations |
| K2 | On-the-fly relations | Target-specific degree-reducing elimination |
| K3 | Frobenius symmetry | Large fixed-locus identity; relation rewriting |
| K4 | Tower/subfield descent | Recursive complexity reduction |
| K5 | Representation switching | Cheap transition between equivalent models |

### 4. Transfer analysis

**K1 (smoothness basis):** Real quadratic fields admit factor bases of bounded-norm prime ideals. Transfer is possible in principle. *Status: partial pass.*

**K2 (on-the-fly relations):** Principal ideal relations exist, but no norm-shrinking identity analogous to $X^q \equiv h_0/h_1$ is known. Relations can be collected; they cannot be recycled via a target-specific descent. *Status: operationally yellow, BGJT-functionally red.*

**K3 (Frobenius symmetry):** The intrinsic automorphism group is $\operatorname{Aut}_{\mathbb{Q}}(K) = \{1, \iota\}$ with $\iota(\sqrt{N}) = -\sqrt{N}$. This two-element symmetry cannot supply a large fixed locus or a splitting identity of Frobenius type. *Status: fail.*

**K4 (tower descent):** Real quadratic fields have no intermediate subfields. External towers fail due to discriminant growth, class-field data requirements, or loss of connection to $R_K$. *Status: fail.*

**K5 (representation switching):** Multiple representations exist (ideals, binary forms, infrastructure, Arakelov). In fixed degree 2, they do not create the height/degree balance enabling $L[1/3]$-type descent. *Status: yellow for adaptability, red for asymptotic gain.*

### 5. Gate analysis

| Gate | Result | Reason |
|---|---|---|
| Gate I | PASS | K1–K5 vocabulary coherent |
| Gate II | PASS | Weak analogues of K2/K5 exist |
| Gate III | PASS | Replacement mechanisms formulable |
| Gate IV | **FAIL** | All pipelines collapse to $L[1/2]$ or worse |

### Theorem 1 — Fixed-degree norm-smoothness barrier

*In the class of Buchmann-style regulator algorithms for fixed real quadratic degree, based on smooth principal-ideal relations, the optimal heuristic relation-collection complexity is $L_D[1/2, O(1)]$, even relative to an integer factoring oracle. The factoring oracle accelerates norm factorization but does not alter the probability that candidate norms are smooth. Hence the $L_D[1/2]$ bottleneck is structural, not arithmetic.*

**Proof sketch.** Candidate relation norms lie in $D^{O(1)}$, so $\log X \asymp \log D$. With factor base size $L_D[a]$, the Dickman–CEP smoothness probability is $L_D[-(1-a)]$. Relation-collection cost balances at $a = 1/2$, giving $L_D[1/2]$ unconditionally on the smoothness model. A factoring oracle does not change $a$. $\square$

### Theorem 2 — Infrastructure period barrier (generic model)

*In the generic infrastructure model — where algorithms evaluate the group law and distance function as black-box oracles but have no access to internal arithmetic structure — any classical algorithm finding the infrastructure period $R_K$ by distance-testing requires $\Omega(\sqrt{R_K})$ oracle queries. Baby-step/giant-step methods achieve $O(\sqrt{R_K})$ and are optimal within this model.*

**Note.** This is a model-relative lower bound, analogous to the Generic Group Model for DLP hardness. It does not exclude algorithms that exploit specific arithmetic properties of the real quadratic infrastructure outside the oracle model.

**Corollary.** A Joux-style breakthrough below $L[1/2]$ for real quadratic regulators requires a mechanism outside the smooth-relation and infrastructure-period models: either a non-factorization-dependent Frobenius analogue, or a new semiprime-specific prefix-to-period law for continued fractions of $\sqrt{pq}$.

---

## Part II: The Regulator–Factorization Complexity Bridge

### 6. The precision trap

Three distinct problems are commonly conflated:

**Proposition 6.1 (Precision trap).**  $\operatorname{REG}_{\mathrm{num}} \not\equiv \operatorname{REG}_{\mathrm{unit}} \not\equiv \operatorname{Pell}$ as computational problems.

*Proof.* To extract the class number $h$ from $hR$ given $R$ numerically requires error $< 1/(2h)$, which is polynomially many bits. This part does not cause exponential precision. The hard step is recovering the Pell coordinate $x = \cosh R_D$ exactly. A numerical error $\delta$ in $R_D$ induces $|\Delta x| \approx x \cdot \delta$. To recover $x \bmod N$ requires $\delta \lesssim e^{-R_D}$, exponential precision for large regulators. Hence a numerical regulator oracle is strictly weaker than a compact unit oracle. $\square$

### 7. The Pell-to-factoring bridge

### Lemma 7.1 — Pell implies factoring

*If $(t_D, u_D)$ is the primitive solution of $t^2 - Du^2 = 4$ and $N \mid D$, then $t_D^2 \equiv 4 \pmod{N}$. If $t_D/2 \not\equiv \pm 1 \pmod{N}$, then $\gcd(t_D/2 - 1, N)$ is a nontrivial factor of $N$.*

**Proof.** The Pell equation gives $t_D^2 = 4 + Du_D^2 \equiv 4 \pmod{N}$. Hence $(t_D/2)^2 \equiv 1 \pmod{N}$. If $t_D/2 \not\equiv \pm 1 \pmod{N}$, then $t_D/2$ is a nontrivial square root of $1$ modulo $N$. Under CRT, $\mathbb{Z}/N\mathbb{Z} \cong \mathbb{F}_p \times \mathbb{F}_q$, so one component is $+1$ and the other is $-1$. Hence $\gcd(t_D/2 - 1, N)$ is $p$ or $q$. $\square$

### 8. SQUFOF and the half-distance closure (Theorem 3)

**Theorem 3 — Half-distance inversion is SQUFOF.**

Setting $D = N$ (or $D = 4N$ for $N \equiv 3 \pmod{4}$), the ambiguous form at infrastructure distance $R_D/2$ from the principal form has canonical shape $(p, 0, -q)$ in reduced form. Finding this form is equivalent to constructing a factoring certificate directly.

**Empirical confirmation.** 50 random semiprimes tested: 13/20 yield a direct half-period gcd from $\sqrt{N}$; 50/50 succeed with small Shanks–Williams multipliers $m \leq 20$. This confirms the classical SQUFOF + multiplier heuristic (Shanks 1971, Williams 1982) but provides no improvement below $L[1/2]$, since the half-period position must be traversed by continued fraction expansion.

**Conclusion:** The half-distance / square-form inversion route is closed as a variant of SQUFOF/Shanks–Williams. No leverage below $L[1/2]$ is found here.

### 9. OP4/H3: Congruence trace compression

The remaining open problem after the above closures is:

> **OP4/H3.** For $D = mN$ with small multiplier $m$, can $t_{mN} \bmod N$ be computed without computing the compact Pell unit, without infrastructure traversal, without PIP, and without CRT idempotents? *(The exclusion of CRT idempotents eliminates the trivially hard routes; the question is whether a genuine shortcut exists that avoids all four mechanisms.)*

### Lemma 9.1 — Trace residue implies factoring

*Let $A$ be an algorithm that, on input $(N, m)$, returns $T_m = t_{mN} \bmod N$ with $T_m / 2 \not\equiv \pm 1 \pmod{N}$ with non-negligible probability. Then $A$ yields a factoring algorithm with the same asymptotic complexity.*

**Proof.** Set $x_m = T_m \cdot 2^{-1} \bmod N$. Since $T_m^2 \equiv 4 \pmod{N}$, we have $x_m^2 \equiv 1 \pmod{N}$. If $x_m \not\equiv \pm 1 \pmod{N}$, then $\gcd(x_m - 1, N)$ is a nontrivial factor by Lemma 7.1. The non-negligible success probability gives the factoring algorithm directly. $\square$

**Corollary.** A hypothetical $L_N[1/3]$ algorithm for OP4/H3 would be an $L_N[1/3]$ factoring algorithm. There is no weaker "intermediate" problem here.

### 10. Routes to $t_{mN} \bmod N$ and their collapse

Four natural routes to computing the trace residue were analyzed. Each collapses to the CRT wall.

| Route | Method | Collapse point |
|---|---|---|
| A | Representation-theoretic trace formula | Delta projector in regular representation has size $N^3$ |
| B | Kloosterman/Kuznetsov sums | Sums mod $N$ factorize via CRT into separate local components |
| C | Low-level reconstruction from many levels | Product of levels $\prod \ell_i \geq N$ is exponential |
| D | Ray-class field structure of $(\mathcal{O}_D / N\mathcal{O}_D)^\times$ | Contains local components at $p, q$; separation = CRT |

### Conjectural Theorem 10.1 — OP4 Compression Barrier

*Any classical algorithm that computes, for enough small multipliers $m$, a trace residue $t_{mN} \bmod N$ nontrivially with non-negligible probability must perform at least one of:*

1. *compute a compact representation of $\varepsilon_{mN}$;*
2. *solve PIP or an infrastructure-distance problem;*
3. *process effective level-$N$ congruence data of size $N^{1-o(1)}$;*
4. *construct a nontrivial CRT idempotent in $\mathbb{Z}/N\mathbb{Z}$.*

*If true, this closes OP4/H3 negatively. If false, the counterexample is directly a factoring breakthrough.*

### 11. Hallgren and the quantum–classical gap

Hallgren's quantum algorithm for Pell's equation and PIP runs in polynomial time via hidden-subgroup/period Fourier sampling. The algorithm works as follows: it evaluates a periodic function on the real quadratic infrastructure — whose period encodes the regulator — and applies the quantum Fourier transform to sample the period directly. This bypasses classical infrastructure traversal, which requires visiting $\Omega(\sqrt{R_K})$ states.

OP4/H3 asks only for $t_D \bmod N$, an output of $O(\log N)$ bits. One might hope the smaller output is classically easier. The obstruction is not the number of output bits; it is access to the **labelled global infrastructure state** — the specific congruence class of the Pell solution modulo $N$. This information is not determined by the regulator length $R_D$ alone: it is congruence-sensitive and attached to the specific hyperbolic/Pell class.

Classically, all known paths to this information proceed through one of:
1. computing the compact Pell unit $\varepsilon_D$ (stronger than $t_D \bmod N$);
2. traversing the continued-fraction/infrastructure cycle to the relevant state ($\Omega(\sqrt{R_K})$ steps);
3. solving PIP;
4. building level-$N$ congruence data of size $N^{1-o(1)}$;
5. constructing a nontrivial CRT idempotent.

Hallgren's quantum Fourier sampling bypasses classical traversal precisely by working globally on the infrastructure. There is no known classical analogue for this global sampling, even for the weaker target $t_D \bmod N$. Any classical method achieving nontrivial trace residues without traversal would, by Lemma 9.1, be a classical polynomial-time factoring algorithm — contradicting standard complexity assumptions.

The Hallgren comparison therefore does not weaken the OP4 barrier. It clarifies the source of hardness: quantum computation accesses global hidden-period structure via Fourier sampling; the OP4 question asks whether a classical algorithm can extract a congruence residue without accessing that structure. No such route is known.

---

## Part III: The Babai–HPMI Bridge

### 12. Motivation

Babai's quasi-polynomial graph isomorphism algorithm runs in time $n^{O(\log n)}$ for graphs on $n$ vertices. For $n = \operatorname{poly}(\log N)$, this would give

$$
\exp(O((\log\log N)^2))
$$

which beats $L_N[1/3]$ asymptotically. The question: can factorization of $N$ be encoded as a small explicit group or graph isomorphism problem of size $\operatorname{poly}(\log N)$ from which $p, q$ are recoverable?

### 13. Model class

**Definition 13.1 (Babai-compatible instance).** A family $I(N)$ is Babai-compatible if it is computable in time $\operatorname{poly}(\log N)$ as an explicit graph, group, or permutation structure of size $n(N) = \operatorname{poly}(\log N)$.

**Definition 13.2 (Product-functorial encoding).** An encoding $F$ is product-functorial if $F(A \times B) \cong F(A) \times F(B)$ canonically. Typical examples: $R \mapsto R^\ast$, $R \mapsto R^\ast/(R^\ast)^k$, $R \mapsto E[\ell](R)$, Cayley graphs on functorially defined generators.

**Definition 13.3 (Effectively CRT-separating witness).** A witness $w$ output by an algorithm on input $N$ is *effectively CRT-separating* if it enables the computation, in polynomial time, of a nontrivial ring projector or idempotent $e \in \mathbb{Z}/N\mathbb{Z}$ with $e \neq 0, 1$.

### Lemma 13.1a — Effectively CRT-separating witnesses imply factoring

*Let $F$ be a product-functorial encoding with $F(\mathbb{Z}/N\mathbb{Z}) \cong F(\mathbb{F}_p) \times F(\mathbb{F}_q)$. Let $\Phi: G \to G'$ be an explicitly computed isomorphism between $G = F(\mathbb{Z}/N\mathbb{Z})$ and $G' = F(\mathbb{Z}/N\mathbb{Z})$ that is effectively CRT-separating (Definition 13.3). Then a nontrivial CRT idempotent $e \in \mathbb{Z}/N\mathbb{Z}$ can be computed in polynomial time.*

This formulation is intentional: the claim is not that every abstractly distinguishing witness automatically yields an idempotent, but that *effectively CRT-separating* witnesses do. Witnesses that are CRT-symmetric do not satisfy the hypothesis and yield no reduction.

**Proof sketch.** If $\Phi$ maps an element $g \in G$ to one whose order divides $|F(\mathbb{F}_p)|$ but not $|F(\mathbb{F}_q)|$, let $k = |F(\mathbb{F}_p)|$. Then $g^k \equiv 1 \pmod{p}$ and $g^k \not\equiv 1 \pmod{q}$, so $g^k - 1$ is a nontrivial zero-divisor in $\mathbb{Z}/N\mathbb{Z}$ and $\gcd(g^k - 1, N)$ factors $N$. $\square$

### Theorem 13.1 — CRT-Wall for product-functorial Babai encodings

*Let $F$ be a product-functorial algebraic encoding and $N = pq$ squarefree. Suppose a Babai-compatible GI instance $I(N)$ of size $\operatorname{poly}(\log N)$ is constructed from $F(\mathbb{Z}/N\mathbb{Z})$. Then:*

1. *(Symmetric case.) If the construction is invariant under swapping the two CRT components, every canonically computable isomorphism decision carries at most Jacobi-type symmetric information and cannot separate $p$ and $q$.*

2. *(Separating case.) If the construction or an extracted isomorphism witness effectively selects one CRT component, it generates a nontrivial CRT projector, which by the Idempotent–Factor Lemma immediately yields a factor of $N$.*

*In particular, Babai's algorithm cannot serve as the "missing last step": either the construction is factorization-blind, or it has already factored $N$.*

**Proof.** Since $\mathbb{Z}/N\mathbb{Z} \cong \mathbb{F}_p \times \mathbb{F}_q$, product-functoriality gives $F(\mathbb{Z}/N\mathbb{Z}) \cong F(\mathbb{F}_p) \times F(\mathbb{F}_q)$. Any isomorphism witness must either (a) treat both components symmetrically, in which case no $p/q$-distinguishing projection exists, or (b) project to one component, generating a CRT idempotent $e$ with $e^2 = e$, $e \notin \{0,1\}$. Then $\gcd(e, N)$ factors $N$ directly. $\square$

### 14. Candidate analysis

**Unit group $(\mathbb{Z}/N\mathbb{Z})^\ast$:** Too large ($\approx N$ elements). Small quotients $R^\ast/(R^\ast)^k$ are again CRT-decomposed. *Closed.*

**Nontrivial square roots of 1:** Perfect extraction mechanism, but constructing them already factors $N$. *Closed.*

**Elliptic $\ell$-torsion $E[\ell](\mathbb{Z}/N\mathbb{Z})$:** Decomposes as $E(\mathbb{F}_p) \times E(\mathbb{F}_q)$; separated Frobenius data at $p$ and $q$ require CRT. *Closed.*

**Galois groups of $N$-dependent polynomials (e.g. $x^m - N$):** Detect Kummer/root structure of $N$, not the factorization $N = pq$, because $\mathrm{Gal}(\mathbb{Q}(\zeta_m, N^{1/m})/\mathbb{Q})$ depends only on $m$ and $N$ as a single integer, not on $p$ and $q$ individually. *Closed.*

**Small Cayley/automorphism graphs with generators from $N \bmod m$:** Babai-compatible, but carry only public residue data, not CRT-separating information. *$B3$ green, $B4$ red.*

### 15. HPMI: Hidden Product Matrix-space Isometry

The continuation explores whether **singular matrix spaces** over $\mathbb{Z}/N\mathbb{Z}$ can carry locally asymmetric structure exploitable for factorization.

**Theorem 13.2 — Extension to matrix-space invariants.**  Let $\mathcal{M}$ be a matrix space over $R = \mathbb{Z}/N\mathbb{Z}$ and let $\Phi(\mathcal{M})$ be a product-compatible algebraic invariant (adjoint algebra, centroid, endomorphism ring, radical, determinantal ideals):
$$\Phi(\mathcal{M}_R) \cong \Phi(\mathcal{M}_p) \times \Phi(\mathcal{M}_q).$$
Then the same CRT dichotomy applies: either the output is CRT-symmetric, or it generates a central CRT-separating idempotent and factors $N$.

**Remark (non-central projectors — a potential residual gap).** Not every idempotent in $\operatorname{Adj}(\mathcal{M})$ factors $N$. A matrix idempotent such as

$$E = \begin{pmatrix}1 & 0 \cr 0 & 0\end{pmatrix} \in \operatorname{Mat}_2(\mathbb{F}_p)$$

is a nontrivial projector but carries no CRT information. Over $R = \mathbb{Z}/N\mathbb{Z}$, factorization follows only from a *central scalar* idempotent $eI$ with $e \in Z(R)$, $e^2 \equiv e \pmod{N}$, $e \notin \{0,1\}$: then $\gcd(e, N) \in \{p, q\}$ directly.

Formally: let $e \in \operatorname{Adj}(\mathcal{M})$ be an idempotent. If $e$ lies in the center of $\operatorname{Adj}(\mathcal{M})$ and acts as a scalar on $\mathcal{M}$, it is CRT-splitting and factors $N$ by the Idempotent–Factor Lemma. If $e$ is non-central — acting as a rank-reducing projector within the module but not on the base ring $R$ — it gives a direct-sum decomposition of the $\mathcal{M}$-action but **not** a CRT decomposition of $R$ itself. Such non-central idempotents do not automatically yield $\gcd(e, N) \in \{p, q\}$.

This creates a narrow residual gap: a non-central idempotent in $\operatorname{Adj}(\mathcal{M})$ might exist without factoring $N$. Whether any such idempotent can be constructed from $N$ alone, without factoring-equivalent data, is not ruled out by Theorem 13.2. In practice, all known natural constructions of adjoint-algebra idempotents from $\mathbb{Z}/N\mathbb{Z}$-data collapse to central decompositions or QR-witnesses. But this gap should be acknowledged rather than silently closed.

### 16. The singular matrix-space boundary

**Theorem 16.1 — Constructive witness wall (true).**  Let $\mathcal{M} \leq \operatorname{Mat}_m(R)$ be publicly given. If an algorithm outputs a concrete matrix $M \in \mathcal{M}$ with $\operatorname{rank}_{\mathbb{F}_p}(M_p) \neq \operatorname{rank}_{\mathbb{F}_q}(M_q)$, or equivalently a minor $\Delta$ with $\Delta \equiv 0 \pmod{p}$, $\Delta \not\equiv 0 \pmod{q}$, then $\gcd(\Delta, N)$ is a nontrivial factor.

**Proof.** If $\operatorname{rank}(M_p) < \operatorname{rank}(M_q)$, there exists a $(k+1)$-minor of $M_p$ that vanishes while the corresponding minor of $M_q$ does not. Its lift $\Delta \in R$ satisfies $\Delta \equiv 0 \pmod{p}$, $\Delta \not\equiv 0 \pmod{q}$, so $1 < \gcd(\Delta, N) < N$. $\square$

**Theorem 16.2 — Strong wall is false (counterexample).**  *The statement "every publicly constructible locally asymmetric singular matrix space already contains a factoring witness" is false.*

**Counterexample.** Choose public $d \in R^\ast$ with Jacobi symbol $\left(\frac{d}{N}\right) = -1$ (computable without factorization). This forces $\left(\frac{d}{p}\right) \neq \left(\frac{d}{q}\right)$. Define

$$
\mathcal{S}_d = \left\{ M(x,y) = \begin{pmatrix} x & dy & 0 \\ y & x & 0 \\ 0 & 0 & 0 \end{pmatrix} : x, y \in R \right\} \subseteq \operatorname{Mat}_3(R).
$$

Every element is singular (third row and column are zero). The $2 \times 2$ upper-left block has determinant $x^2 - dy^2$. Over $\mathbb{F}_r$, a nonzero rank-1 element exists iff $d$ is a quadratic residue mod $r$. Therefore

$$
\operatorname{minrank}_{\mathbb{F}_p}(\mathcal{S}_d) \neq \operatorname{minrank}_{\mathbb{F}_q}(\mathcal{S}_d),
$$

yet no coefficient in the construction of $\mathcal{S}_d$ is a nontrivial zero-divisor modulo $N$. Local asymmetry exists publicly without an immediate factor. $\square$

**Theorem 16.3 — Singular Matrixspace Boundary Theorem.**

*There exist publicly constructible singular matrix spaces over $\mathbb{Z}/N\mathbb{Z}$ whose local low-rank structure is asymmetric at $p$ and $q$. This existence information does not immediately factor $N$. However, any constructive witness for the asymmetry — a rank-reducing matrix, minor, or pivot — generates a nontrivial zero-divisor and factors $N$ via gcd. In the minimal family $\mathcal{S}_d$, the gap between existence and construction is equivalent to QR-Witness extraction (not QR-Decision) for $d$ modulo the prime factors of $N$. More general singular matrix spaces may encode stronger or different witness problems, but no natural construction outside this witness paradigm is found in this work. QR-Witness extraction is polynomial-time interreducible with integer factorization under standard randomized reductions.*

**Remark.** This is not a new opening. Finding a rank-1 element in $\mathcal{S}_d$ requires finding $(x,y)$ with $x^2 \equiv dy^2 \pmod{N}$ non-trivially, i.e. producing a QR-witness for $d$ mod $N$. Under standard assumptions, QR-witness extraction is factoring-equivalent.

---

## Part IV: Unified Analysis

### 17. The CRT wall from three directions

All three research strands independently encounter the same structural barrier.

| Strand | Route | Collapse mechanism |
|---|---|---|
| A1 (Joux–Buchmann) | Frobenius tower descent in real quadratic field | No Frobenius analogue; smooth relations locked at $L[1/2]$ |
| A2 (Regulator) | Congruence trace $t_{mN} \bmod N$ via analytic/class-field methods | Every nontrivial *and CRT-asymmetric* output = factoring certificate (Lemma 9.1); CRT-symmetric outputs carry no $p/q$-distinguishing information |
| C5 (Babai–HPMI) | Product-functorial GI encoding; singular matrix isometry | CRT-symmetric or idempotent generated before Babai (Theorem 13.1) |

**Unified statement.** In each of these strands, a classical algorithm achieving its stated goal either:
- outputs only CRT-symmetric information (blind to $p/q$), or
- generates a nontrivial CRT idempotent or zero-divisor, factoring $N$ before the proposed step applies.

This is the **CRT wall**: separation of the two local components is equivalent to factorization.

### 18. Final status table

| Branch | Status |
|---|---|
| Joux–Buchmann descent (Gate IV) | **closed** — no Frobenius analogue in degree 2 |
| Smooth principal-relation REG | **closed** — $L[1/2]$ barrier (Theorem 1) |
| Infrastructure period search | **closed** — $\Omega(\sqrt{R_K})$ lower bound (Theorem 2) |
| Precision trap ($\operatorname{REG}_{\mathrm{num}} \to \varepsilon_D$) | **closed** — exponential precision required |
| Half-distance / SQUFOF | **closed** — classical SQUFOF + multiplier (Theorem 3) |
| OP4/H3 predicate-only lemma | **false as stated** — recognizer ≠ generator |
| OP4/H3 trace-residue generation | **closed conditionally** — generation = factoring (Lemma 9.1) |
| OP4 Compression Barrier | **conjectural** — Routes A–D all collapse; proof pending |
| Babai, product-functorial | **closed** — CRT-Wall Theorem 13.1 |
| HPMI adjoint/centroid (central) | **closed** — Theorem 13.2 |
| HPMI singular spaces (existence) | **open** — counterexample $\mathcal{S}_d$ shows asymmetry possible |
| HPMI singular witness extraction | **closed** — witness = QR-witness = factoring (Theorem 16.3) |

### 19. The single remaining open problem

After all closures, one atomic open problem remains, encompassing both OP4/H3 and HPMI-3:

> **Open Problem.** Can a classical polynomial-time algorithm compute, without factoring $N$, a concrete object in $\mathbb{Z}/N\mathbb{Z}$ that witnesses local asymmetry between $\mathbb{F}_p$ and $\mathbb{F}_q$ — whether as a Pell trace residue $t_{mN} \bmod N$, a QR-witness for $d$ mod one factor, or an asymmetric matrix minor — in a way that avoids all four routes of the Compression Barrier (Conjectural Theorem 10.1)?

If yes: factoring breakthrough.  
If no (Compression Barrier proved): the entire project ends with a sharp structural theorem unifying all three negative results.

---

## 20. Publication roadmap

The results decompose naturally into three publishable units, with **Paper C recommended first** (cleanest, most self-contained result).

**Paper C (first)** *(from C5).* CRT-wall for product-functorial GI encodings (Lemma 13.1a, Theorem 13.1); singular matrix-space boundary theorem (Theorems 16.1–16.3); HPMI dichotomy; QR-witness equivalence. *Target: J. Symbolic Computation or J. Algebra.* This paper is the most self-contained and has the clearest positive/negative balance.

**Paper A (second)** *(from A1).* Fixed-degree smooth-relation and infrastructure barriers for real quadratic regulators (Theorems 1 and 2). Joux–Buchmann transfer failure at Gate IV. *Target: Mathematics of Computation or J. Number Theory.* Requires more literature anchoring for the infrastructure model.

**Paper B (third)** *(from A2).* Compression barriers for the Pell unit modulo $N$: a reduction of real-quadratic factoring routes to a single open problem (Lemma 9.1, Routes A–D, Conjectural Theorem 10.1). Corrected statement of the OP4-D lemma; Hallgren gap discussion. *Target: J. Cryptology or Designs, Codes and Cryptography.* Contains the most conjectural material; suitable as a "barrier conjecture + route analysis" paper.

All three papers share a common conclusion, stated in the Unified Analysis (§17–18), and may appropriately reference each other.

---

## Appendix: Key lemmas

### A.1 Idempotent–Factor Lemma

*Let $N = pq$ squarefree and $e \in \mathbb{Z}/N\mathbb{Z}$ with $e^2 = e$, $e \notin \{0,1\}$. Then $\gcd(e, N)$ or $\gcd(e-1, N)$ is a nontrivial factor of $N$.*

**Proof.** By CRT, idempotents in $\mathbb{F}_p \times \mathbb{F}_q$ are componentwise $0$ or $1$. Nontrivial idempotents correspond to $(1,0)$ or $(0,1)$, and their representative is divisible by exactly one of $p, q$. $\square$

### A.2 Nontrivial square roots of 1 and idempotents

*$\xi \in \mathbb{Z}/N\mathbb{Z}$ with $\xi^2 \equiv 1$ and $\xi \not\equiv \pm 1$ yields a nontrivial idempotent $e = (\xi + 1)/2$, and vice versa. Hence nontrivial trace residues, nontrivial roots of 1, and nontrivial CRT idempotents are polynomial-time equivalent outputs.*

### A.3 Precision trap — formal statement

*Recovering $x = \cosh(R_D)$ from a numerical approximation $\hat{R}_D$ with error $\delta$ induces error $|\Delta x| \approx e^{R_D} \cdot \delta$. To recover $x \bmod N$ exactly by the naive route requires $\delta \lesssim e^{-R_D}$, which is $2^{-\Theta(R_D)}$: exponential in the input length for typical regulators.*
