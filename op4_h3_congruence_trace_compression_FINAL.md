# OP4/H3 Final Note: Congruence Trace Compression, Ray Residues, and the Correct Compression Barrier

**Project:** Faktorisierung 1  
**Date:** 2026-05-06  
**Status:** final OP4/H3 closure note with corrected barrier statement  

---

## Executive summary

The OP4/H3 branch asks whether one can compute, for

\[
N=pq,\qquad D=mN,
\]

the congruence trace

\[
t_D \bmod N
\]

of the primitive Pell solution

\[
t_D^2-Du_D^2=4
\]

without computing the Pell unit, without continued-fraction/infrastructure traversal, without full level-\(N\) expansion, and without CRT idempotents.

The reduction is immediate:

\[
t_D^2\equiv 4\pmod N,
\qquad
x_D:=t_D/2\pmod N,
\qquad
x_D^2\equiv1\pmod N.
\]

If \(x_D\not\equiv\pm1\pmod N\), then

\[
\gcd(x_D-1,N)
\]

factors \(N\). Thus any efficient algorithm for nontrivial OP4 trace residues is directly an efficient factoring algorithm.

The proposed Lemma OP4-D from the external task, however, is **not true as stated**. A polynomial-time predicate \(\Pi\) that recognizes nontrivial square roots of \(1\) modulo \(N\) does not by itself generate such a root. Recognition is easy; generation is the hard part.

The correct barrier statement must therefore be search/generation-based, not predicate-only.

---

## 1. OP4 setup

Let \(N=pq\) be an odd semiprime. Let \(m\) be small, squarefree, and coprime to \(N\). Put

\[
D=mN.
\]

Let \((t_D,u_D)\) be the primitive fundamental solution of

\[
t^2-Du^2=4.
\]

Equivalently, the associated unit is

\[
\varepsilon_D=\frac{t_D+u_D\sqrt D}{2}.
\]

Modulo \(N\), the Pell equation gives

\[
t_D^2\equiv4\pmod N.
\]

Since \(N\) is odd, \(2\) is invertible modulo \(N\), and therefore

\[
x_D:=t_D2^{-1}\pmod N
\]

satisfies

\[
x_D^2\equiv1\pmod N.
\]

Under the CRT identification

\[
\mathbb Z/N\mathbb Z\simeq\mathbb F_p\times\mathbb F_q,
\]

the four square roots of \(1\) are

\[
(+1,+1),\quad(+1,-1),\quad(-1,+1),\quad(-1,-1).
\]

The mixed cases factor \(N\).

---

## 2. Reductive lemma: trace residue implies factoring

### Lemma 2.1 — OP4 trace residue factors

Suppose an algorithm returns, for some multiplier \(m\), the value

\[
T_m=t_{mN}\bmod N.
\]

Let

\[
x_m=T_m2^{-1}\bmod N.
\]

If

\[
x_m\not\equiv \pm1\pmod N,
\]

then \(N\) can be factored in deterministic polynomial time.

### Proof

The Pell equation gives

\[
t_{mN}^2-mNu^2=4.
\]

Modulo \(N\), this becomes

\[
T_m^2\equiv4\pmod N.
\]

Thus

\[
x_m^2\equiv1\pmod N.
\]

If \(x_m\not\equiv\pm1\pmod N\), then \(x_m\) is a nontrivial square root of \(1\) modulo \(N\). Therefore

\[
\gcd(x_m-1,N)
\]

is a nontrivial factor of \(N\).  
\(\square\)

---

## 3. Why the originally requested OP4-D lemma is false as stated

The requested statement was:

> Let \(\Pi:(\mathbb Z/N\mathbb Z)^\times\to\{0,1\}\) be computable in \(\operatorname{poly}(\log N)\) time, with
> \[
> \Pi(+1)=\Pi(-1)=0
> \]
> and
> \[
> \Pi(\xi)=1
> \]
> for the two mixed roots \(\xi=(+1,-1),(-1,+1)\) under CRT. Then \(\Pi\) yields a polynomial-time factorization of \(N\).

This is not valid. The gap is that \(\Pi\) is only a **recognizer**, not a **generator**.

Indeed, the following predicate is already computable in polynomial time without knowing \(p,q\):

\[
\Pi_0(x)=
\begin{cases}
1,& x^2\equiv1\pmod N\text{ and }x\not\equiv\pm1\pmod N,\\
0,& \text{otherwise.}
\end{cases}
\]

This predicate satisfies the requested conditions. If one ever queries it on a mixed root, it says \(1\). But it gives no method for finding such a mixed root.

The witness set has size two inside a domain of size roughly \(N\). A polynomial number of blind queries has negligible probability of hitting it. Recognition of a rare factoring witness is not the same as construction of that witness.

Hence the predicate-only OP4-D lemma cannot be the final compression barrier. It must be replaced by a search or projector statement.

---

## 4. Correct OP4-D: search/generation version

### Theorem 4.1 — Correct OP4-D, search version

Let \(A\) be an algorithm that, on input \(N=pq\), outputs an element

\[
\xi\in(\mathbb Z/N\mathbb Z)^\times
\]

such that

\[
\xi^2\equiv1\pmod N,
\qquad
\xi\not\equiv\pm1\pmod N,
\]

with non-negligible probability. Then \(A\) yields a polynomial-time randomized factorization algorithm for \(N\).

### Proof

Run \(A\) to obtain \(\xi\). Verify

\[
\xi^2\equiv1\pmod N
\]

and

\[
\xi\not\equiv\pm1\pmod N.
\]

If verification succeeds, compute

\[
g=\gcd(\xi-1,N).
\]

Because \(\xi\) is a nontrivial square root of \(1\), one CRT component of \(\xi-1\) vanishes and the other does not. Hence

\[
1<g<N.
\]

Repeating the randomized algorithm polynomially many times gives a factor with high probability.  
\(\square\)

---

## 5. Correct OP4-D: trace-compression version

### Theorem 5.1 — Correct OP4-D for OP4/H3

Let \(A\) be an algorithm which, on input \((N,m)\), returns

\[
t_{mN}\bmod N
\]

for enough small multipliers \(m\) that with non-negligible probability

\[
t_{mN}2^{-1}\not\equiv\pm1\pmod N.
\]

Then \(A\) yields a factoring algorithm with the same asymptotic complexity, up to polynomial factors.

### Proof

For each returned trace residue \(T_m\), set

\[
x_m=T_m2^{-1}\pmod N.
\]

Check whether

\[
x_m^2\equiv1\pmod N
\]

and whether \(x_m\not\equiv\pm1\pmod N\). If so, compute

\[
\gcd(x_m-1,N).
\]

By Lemma 2.1 this is a nontrivial factor. The assumed non-negligible success probability over the multiplier set gives the claimed factoring algorithm.  
\(\square\)

---

## 6. Correct OP4-D: projector/idempotent version

A stronger but often more natural representation-theoretic statement is the following.

### Theorem 6.1 — Projector compression implies CRT separation

Suppose a compression procedure \(C\), on input \(N\), outputs a nontrivial idempotent

\[
e\in\mathbb Z/N\mathbb Z,
\qquad
e^2\equiv e\pmod N,
\qquad
e\not\equiv0,1\pmod N.
\]

Then \(C\) factors \(N\) in polynomial time.

### Proof

Compute

\[
g=\gcd(e,N).
\]

Since \(e\) is a nontrivial idempotent, under CRT it is either

\[
(1,0)\quad\text{or}\quad(0,1).
\]

Thus \(\gcd(e,N)\) is either \(p\) or \(q\).  
\(\square\)

Equivalently, a nontrivial square root \(\xi\) gives a nontrivial idempotent

\[
e=\frac{\xi+1}{2}\pmod N.
\]

Thus nontrivial trace residues, nontrivial roots of \(1\), and nontrivial CRT idempotents are polynomial-time equivalent outputs.

---

## 7. Compression barrier: correct final formulation

The proper OP4 compression barrier is therefore not the predicate-only lemma, but the following conjectural barrier.

### Conjectural Theorem 7.1 — OP4 Compression Barrier

Any classical algorithm that computes, for enough small multipliers \(m\), a trace residue

\[
t_{mN}\bmod N
\]

which is nontrivial with non-negligible probability must perform at least one of the following operations:

1. compute a compact representation of the Pell unit \(\varepsilon_{mN}\);
2. solve a PIP/infrastructure-distance problem;
3. process effective level-\(N\) congruence data of size \(N^{1-o(1)}\);
4. construct a nontrivial CRT idempotent or equivalent local separation in \(\mathbb Z/N\mathbb Z\).

If true, this closes OP4/H3 negatively. If false, the counterexample is directly a factoring breakthrough.

This is the strongest honest form of OP4-D.

---

## 8. Correction of the former Section 9

The earlier wording said:

> Even a heuristic \(L_N[1/3]\)-algorithm for \(t_{mN}\bmod N\) would be major.

This was too weak and logically imprecise. By Lemma 2.1, such an algorithm would not merely be “major”; it would be an \(L_N[1/3]\)-type factoring algorithm, provided it succeeds for a multiplier \(m\) whose trace residue is nontrivial.

Correct formulation:

\[
\boxed{
\text{A sub-SQUFOF, sub-}L[1/2]\text{ algorithm for nontrivial OP4 trace residues is immediately a factoring algorithm of the same complexity.}
}
\]

In particular, a heuristic \(L_N[1/3]\) OP4 algorithm would be a heuristic \(L_N[1/3]\) factoring algorithm through the gcd extraction above.

---

## 9. Hallgren section: why the quantum result does not give a classical shortcut to \(t_D\bmod N\)

Hallgren's quantum algorithm for Pell's equation and the principal ideal problem computes the relevant real-quadratic period data in polynomial time by reducing the problem to a hidden-subgroup/hidden-period structure. The quantum Fourier transform can sample global period information from a function on the infrastructure that is classically only available by local navigation.

This is stronger than OP4/H3 in output terms. Hallgren's method gives enough information to recover the compact Pell unit or solve the principal ideal problem, whereas OP4/H3 asks only for

\[
t_D\bmod N,
\]

a residue containing only \(O(\log N)\) bits.

However, the smaller output size does not imply an easier classical algorithm. The obstruction is not the number of output bits; it is access to the labelled global infrastructure state. The value \(t_D\bmod N\) is not determined by the real regulator length alone. It is congruence-sensitive information attached to the specific hyperbolic/Pell class.

Classically, known access to this information proceeds through one of the following:

1. compute the Pell unit or compact automorphism;
2. traverse the continued-fraction/infrastructure cycle to the relevant state;
3. solve PIP;
4. build enough level-\(N\) congruence information;
5. produce a nontrivial CRT idempotent.

The quantum hidden-period algorithm bypasses classical traversal by Fourier sampling. There is no known classical analogue, even for the weaker residue target \(t_D\bmod N\). If such a classical analogue existed and produced nontrivial trace residues, Lemma 2.1 would immediately turn it into a classical factoring algorithm.

Thus Hallgren does not weaken the OP4 barrier. Instead, it clarifies it: quantum computation can access the global hidden-period structure; the project asks whether a classical algorithm can extract just the trace residue without accessing that structure. No such route is known.

---

## 10. Final decision status

| Branch | Status |
|---|---:|
| Smooth principal relations | closed at fixed-degree \(L_D[1/2]\) barrier |
| Numerical regulator \(R_D\) | too weak; cannot reconstruct unit residue |
| Pell/PIP compact unit | factors, but is stronger than REG\(_{num}\) |
| Half-distance / square-form phase | closed as SQUFOF/Shanks-Williams |
| OP4/H3 predicate-only lemma | false as stated |
| OP4/H3 trace-residue generation | equivalent to factoring output |
| OP4 Compression Barrier | final conjectural negative statement |

---

## 11. Final bottom line

The project cannot honestly claim a proof of the predicate-only OP4-D statement. The predicate is too weak: recognizing a nontrivial square root of \(1\) is easy once it is presented.

The correct final result is sharper:

\[
\boxed{
\text{Any algorithm that actually produces }t_{mN}\bmod N
\text{ in a nontrivial case produces a factor of }N.
}
\]

Therefore OP4/H3 is either:

1. a direct factoring breakthrough, if a genuine trace-compression algorithm exists; or
2. closed by a compression-barrier theorem showing that any such compression must already perform Pell/PIP, level-\(N\) expansion, infrastructure traversal, or CRT separation.

This is the clean final form of the project.
