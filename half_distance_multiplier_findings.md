# Half-Distance Multiplier Probe — Interim Findings

This note records the next diagnostic after the half-distance/SFL pilot. It is not a factoring algorithm: every row still computes the full continued-fraction period and then inspects the midpoint. The experiment asks whether the midpoint phenomenon persists, and whether small SQUFOF-style multipliers rescue the cases where the raw midpoint gives only the trivial value `Q_{L/2}=2`.

## Summary table

| bits | samples | avg period | median period | even periods | base half hits | base hit rate | multiplier hits | multiplier hit rate | first-hit multipliers |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 32 | 50 | 20203.32 | 17936 | 44 | 35 | 0.700 | 50 | 1.000 | `{1: 35, 3: 10, 5: 1, 7: 2, 11: 2}` |
| 36 | 40 | 74078.62 | 61317 | 35 | 26 | 0.650 | 40 | 1.000 | `{1: 26, 3: 9, 5: 2, 7: 1, 21: 1, 57: 1}` |
| 40 | 20 | 285549.95 | 241980 | 19 | 16 | 0.800 | 20 | 1.000 | `{1: 16, 3: 2, 7: 1, 13: 1}` |

## Observations

1. For `m=1`, the midpoint state of `sqrt(N)` exposes a nontrivial factor in most even-period cases. In the raw runs, odd periods gave no midpoint factor.
2. The raw midpoint failures are highly structured: in the inspected even-period misses, `Q_{L/2}=2`, i.e. the midpoint is an ambiguous but factor-trivial state.
3. Small multipliers turn every sampled failure into a factor-revealing midpoint. Across the 32/36/40-bit batches, all rows hit after trying a short multiplier list. Most first hits are at `m=1` or `m=3`; a few require `m=5,7,11,13,21,57`.
4. This strengthens the main research reduction: if one had a sublinear/sub-`L[1/2]` way to construct the midpoint state of `sqrt(mN)` for a few small multipliers, factorization would follow in these samples.

## Critical caveat

The experiment still computes the full continued-fraction period. Therefore it does not improve SQUFOF or NFS. It only isolates the exact missing primitive: `HalfState(mN)`, the midpoint state of the period, without period traversal.

## Refined target problem

Given `N=pq` and a small multiplier `m`, construct the midpoint continued-fraction state `(P_{L/2}, Q_{L/2})` of `sqrt(mN)` without computing the full period. If `gcd(Q_{L/2}, N)` or `gcd(P_{L/2}, N)` is nontrivial, factorization follows.

The next theoretical step is to characterize when `Q_{L/2}` equals `p`, `q`, `2p`, `2q`, or the trivial value `2`, and whether the multiplier choice can be predicted without factoring.
