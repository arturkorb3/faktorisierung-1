# Half-State Midpoint Update

## Purpose

This note sharpens the half-distance path.  The empirical midpoint signal is not a mysterious numerical accident: for even continued-fraction period length, the midpoint state satisfies an exact ambiguous-state identity.

Let

\[
M=mN,
\qquad N=pq,
\]

and write the continued-fraction states of \(\sqrt M\) as

\[
(P_i,Q_i,a_i),
\]

with recurrence

\[
P_{i+1}=a_iQ_i-P_i,
\qquad
Q_{i+1}=\frac{M-P_{i+1}^2}{Q_i}.
\]

If the period length is \(L=2h\), the midpoint state \((P_h,Q_h,a_h)\) is ambiguous and, in all tested cases, satisfies the exact identity

\[
2P_h=a_hQ_h.
\]

This makes the factor signal transparent: when \(Q_h\) or \(P_h\) contains one prime factor of \(N\), a simple gcd extracts it.

## Experimental status

### Existing multiplier tests

For the previously generated 40-bit multiplier probe, the classifier finds:

- even periods: 20/20,
- midpoint identity \(2P=aQ\): 20/20,
- factor hit from \(P\) or \(Q\): 20/20.

The observed midpoint types were:

| half partial quotient \(a_h\) | \(Q_h / \gcd(Q_h,N)\) | count |
|---:|---:|---:|
| 2 | 1 | 13 |
| 1 | 2 | 4 |
| 3 | 2 | 2 |
| 4 | 1 | 1 |

So the factor-carrying midpoint often has the form

\[
P_h=c r,
\qquad
Q_h=d r,
\qquad r\in\{p,q\},
\]

with small \((c,d)\).

### 44-bit direct \(m=1\) test

For 10 direct 44-bit semiprimes:

- even periods: 7/10,
- midpoint identity \(2P=aQ\): 7/10,
- factor hit from \(P\) or \(Q\): 4/10.

The misses are structurally clear: the midpoint still satisfies \(2P=aQ\), but it is the trivial ambiguous case with \(Q_h=2\) and huge \(a_h\).  This mirrors the earlier observation that small multipliers can move the midpoint from trivial to factor-revealing.

## Algebraic reduction of the midpoint condition

Assume a factor-revealing midpoint:

\[
P_h=c r,
\qquad
Q_h=d r,
\qquad r\mid N.
\]

The midpoint identity gives

\[
a_h=\frac{2c}{d}.
\]

The partial quotient condition

\[
a_h=\left\lfloor \frac{\lfloor\sqrt M\rfloor+P_h}{Q_h}\right\rfloor
\]

implies approximately

\[
c\leq \sqrt{\frac{m(N/r)}{r}} < c+d.
\]

Equivalently,

\[
\frac{\sqrt{mN}}{c+d}< r \leq \frac{\sqrt{mN}}{c}.
\]

Thus small midpoint coefficients \((c,d)\) locate the hidden factor only inside a broad interval.  For small multipliers this interval is much too wide for Fermat/Coppersmith-style recovery.

## Consequence

The midpoint factor signal is theorem-level real, but direct construction remains hard.

The direct construction problem is equivalent to finding a hidden divisor \(r\mid N\) together with small integers \((c,d)\) such that the midpoint ambiguous state has

\[
P_h=c r,
\qquad Q_h=d r.
\]

Without access to the midpoint state, the interval constraint alone is too weak.

## Current best formulation

The main open problem is now:

> **Half-State Direct Construction.** Given \(M=mN\), construct the midpoint ambiguous state \((P_h,Q_h,a_h)\) of the continued-fraction period of \(\sqrt M\), without traversing \(O(L)\) states.

A successful sub-\(L[1/2]\) solution would yield a factoring path.  A proof that this construction is equivalent to hidden divisor recovery would give the clean negative result.

## Files

- `half_state_classifier.py`: midpoint classifier and interval extractor.
- `halfclass_44bit_10_m1.csv`: direct 44-bit midpoint classification.
- `halfclass_multihalf_40bit_20.csv`: classifier output for the 40-bit multiplier hits.
