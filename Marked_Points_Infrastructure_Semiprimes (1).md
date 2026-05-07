# Marked Points in the Real Quadratic Infrastructure of Semiprimes

## Abstract

The Joux--Buchmann regulator bridge does not yield a sub-\(L[1/2]\) factoring algorithm.  A useful side branch remains: view SQUFOF and related continued-fraction methods not as regulator-computation algorithms, but as **marked-point search** in the real quadratic infrastructure of \(N=pq\).  A marked point is an infrastructure state whose local data yields a nontrivial factor, a congruence of squares, or a reverse-step certificate.  The central question becomes whether these marked points can be located earlier than generic cycle search by exploiting semiprime-specific structure, multiplier choice, or prefix-to-window prediction.

## 1. Setting

Let \(N=pq\) be a balanced semiprime and consider the continued fraction

\[
\sqrt N=[a_0;\overline{a_1,\ldots,a_\ell}].
\]

The continued-fraction states may be represented by triples \((P_i,Q_i,a_i)\), reduced forms, reduced ideals, or infrastructure points.  The full period gives regulator information, but factoring does not necessarily require the full regulator.  It may be enough to hit a special state.

## 2. Marked points

Let \(\mathcal I_N\) be the principal infrastructure cycle.  A subset

\[
M_N\subset \mathcal I_N
\]

is called a set of marked points if reaching \(x\in M_N\) gives a practical extraction procedure for a nontrivial factor of \(N\), or for a congruence of squares modulo \(N\).

Examples:

1. square forms / square \(Q_i\)-values in SQUFOF,
2. ambiguous forms,
3. half-period or midpoint witnesses,
4. states exposing \(\gcd(Q_i,N)\), \(\gcd(P_i,N)\), or equivalent data,
5. states producing \(x^2\equiv y^2\pmod N\).

## 3. Witnesses versus predictors

Known continued-fraction structures are mostly **witnesses**:

\[
\text{if the orbit reaches }x\in M_N,\text{ factorization may follow.}
\]

A breakthrough needs **predictors**:

\[
\text{early data predicts where }M_N\text{ lies.}
\]

This distinction explains why palindromy, Pell parity, and square-form criteria are useful but do not automatically produce asymptotic speedups.

## 4. Multiplier branch

SQUFOF commonly replaces \(N\) by \(kN\) and studies \(\sqrt{kN}\).  This changes both the infrastructure cycle and the marked-point distribution:

\[
M_N \leadsto M_{kN}.
\]

The practical question is:

> Can one choose \(k\) so that marked points move systematically toward the beginning of the search?

Known multiplier strategies improve constants and success probability.  The open side-branch question is whether a semiprime-specific multiplier rule can improve the hitting exponent, or at least identify useful subclasses.

## 5. Toy empirical probe

A small diagnostic experiment was run on random balanced semiprimes.  For each \(N\), the first square \(Q_i\)-value in the forward SQUFOF-style recurrence was recorded for \(k=1\), and compared with the best hit among

\[
\{1,3,5,7,11,15,21,33,35,55,77,105,165,231,385,1155\}.
\]

This is a proxy for square-form witness location, not a complete SQUFOF implementation.

| prime bits | semiprime bits | samples | median first square, \(k=1\) | median best among 16 multipliers |
|---:|---:|---:|---:|---:|
| 12 | 24 | 300 | 27 | 3 |
| 14 | 28 | 300 | 50 | 5 |
| 16 | 32 | 200 | 100 | 8 |
| 18 | 36 | 100 | 205 | 15 |
| 20 | 40 | 60 | 425 | 27 |

Interpretation:

1. multipliers provide a strong practical constant improvement;
2. the scale still grows roughly like \(N^{1/4}\);
3. no exponent collapse is visible;
4. choosing the best multiplier is nontrivial and not explained by the simplest initial-gap heuristic.

## 6. Shortcut trichotomy

Any classical continued-fraction/infrastructure shortcut for semiprime factorization must fall into one of three categories.

### Theorem: Continued-fraction shortcut trichotomy

Let an algorithm access \(\sqrt{pq}\) through continued-fraction states, reduction/composition operations, and arithmetic tests on resulting forms.  If it factors \(N=pq\) substantially faster than generic infrastructure search, then at least one of the following must occur:

1. **Early-witness anomaly:** the orbit reaches a factor-revealing marked point asymptotically earlier than the random marked-cycle model predicts.
2. **Prefix-to-window anomaly:** a short continued-fraction prefix predicts a narrow future interval containing such a marked point or the period boundary.
3. **External arithmetic leakage:** the algorithm uses information outside local infrastructure dynamics, such as smooth relation data, class-number/regulator information, CRT idempotents, or equivalent hidden factor information.

### Proof sketch

A successful factorization must produce a nontrivial gcd or a congruence of squares.  If this comes from an infrastructure state, that state is marked.  If the state is found earlier than generic search, either marked points occur early, or early data predicts where to search.  If neither is true, the speedup must come from information external to the continued-fraction/infrastructure transcript.

## 7. Research gates

### Gate S1: Witness taxonomy

Enumerate all predicates \(W(x)\) on reduced forms or infrastructure states that yield factorization.

### Gate S2: Hitting distribution

For each witness type \(W\), estimate the distribution of first hitting times \(t_W/R\) for balanced semiprimes.

### Gate S3: Multiplier bias

Study whether small multipliers \(k\) systematically bias \(M_{kN}\) toward early positions.

### Gate S4: Prefix-to-window predictors

Test whether early partial quotients, early \(Q_i\)-statistics, or modular features predict narrow windows containing marked points.

### Gate S5: Theoretical model

Compare data to random marked-cycle models.  A positive result requires demonstrable deviation from random marked-cycle behavior.

## 8. Current conclusion

This side branch does not resurrect the Joux--Buchmann breakthrough.  It does, however, define a useful standalone program:

\[
\boxed{\text{Study marked-point distributions in real quadratic infrastructure of semiprimes.}}
\]

The most realistic near-term target is not \(L[1/3]\), but either:

1. sharper theory for SQUFOF/multiplier behavior,
2. improved practical multiplier selection,
3. or a proof that known witness distributions behave generically.

A true positive breakthrough would require an early-witness anomaly or a prefix-to-window anomaly.
