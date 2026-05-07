"""
buchmann_experiments.py
Empirische Untersuchung: Regulator R_K für Q(sqrt(N)), N = pq semiprim.
Fragen: FACTOR ≤ REG? REG ≤ FACTOR? Precision Trap?
"""

import math
import itertools
from decimal import Decimal, getcontext
getcontext().prec = 60

def isqrt(n):
    if n < 0:
        raise ValueError("Square root of negative number")
    if n == 0:
        return 0
    x = int(math.isqrt(n))
    # Korrekt für große n
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x

def is_perfect_square(n):
    s = isqrt(n)
    return s * s == n

def fundamental_solution_pell(D):
    """
    Löse x^2 - D*y^2 = ±1 via Kettenbruch-Entwicklung von sqrt(D).
    Gibt zurück: (x, y, sign) mit x^2 - D*y^2 = sign (±1)
    und den Regulator log(x + y*sqrt(D)).
    """
    if is_perfect_square(D):
        return None  # Kein echter quadratischer Körper

    a0 = isqrt(D)
    
    # Kettenbruch: sqrt(D) = a0 + 1/(a1 + 1/(a2 + ...))
    # Konvergenten: p_{-1}=1, p_0=a0, p_n = a_n*p_{n-1} + p_{n-2}
    #              q_{-1}=0, q_0=1,  q_n = a_n*q_{n-1} + q_{n-2}
    
    m, d, a = 0, 1, a0
    p_prev, p_curr = 1, a0
    q_prev, q_curr = 0, 1
    
    for _ in range(10_000_000):  # Sicherheitslimit
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        
        p_prev, p_curr = p_curr, a * p_curr + p_prev
        q_prev, q_curr = q_curr, a * q_curr + q_prev
        
        x, y = p_curr, q_curr
        val = x * x - D * y * y
        if val == 1:
            R = float(Decimal(x + y * Decimal(D).sqrt()).ln())
            return (x, y, 1, R)
        elif val == -1:
            R = float(Decimal(x + y * Decimal(D).sqrt()).ln())
            return (x, y, -1, R)
    
    return None  # Nicht gefunden

def primes_up_to(n):
    """Sieb des Eratosthenes"""
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i, v in enumerate(sieve) if v]

# ============================================================
print("=" * 70)
print("EXPERIMENT 1: Kleine Semiprime — Überblick")
print("=" * 70)
print(f"{'N':>8} {'p':>5} {'q':>5} {'R_K':>12} {'h approx':>10} {'|p-q|':>8} {'sign':>6}")
print("-" * 70)

small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

results_exp1 = []
for i, p in enumerate(small_primes):
    for q in small_primes[i+1:]:
        N = p * q
        sol = fundamental_solution_pell(N)
        if sol:
            x, y, sign, R = sol
            results_exp1.append((N, p, q, R, sign, abs(p - q)))
            print(f"{N:>8} {p:>5} {q:>5} {R:>12.5f} {'?':>10} {abs(p-q):>8} {sign:>+6}")

# ============================================================
print("\n" + "=" * 70)
print("EXPERIMENT 2: R_K / sqrt(N) — Stabiles Verhältnis?")
print("=" * 70)
print(f"{'N':>10} {'R_K':>12} {'R/sqrt(N)':>12} {'logR/logN':>12}")
print("-" * 70)

pairs = [
    (3,5),(5,7),(11,13),(29,31),(41,43),(71,73),(101,103),(149,151),
    (3,7),(3,11),(3,101),(5,101),(7,101),(11,101),(13,103),(17,107),
    (3,199),(7,199),(11,197),(23,197),(5,503),(7,503)
]

for p, q in pairs:
    N = p * q
    sol = fundamental_solution_pell(N)
    if sol:
        x, y, sign, R = sol
        ratio = R / math.sqrt(N)
        logr_logn = math.log(R) / math.log(N) if R > 1 else 0
        print(f"{N:>10} {R:>12.5f} {ratio:>12.7f} {logr_logn:>12.6f}")

# ============================================================
print("\n" + "=" * 70)
print("EXPERIMENT 3: REG ≤ FACTOR? — Kuroda-Verhältnis R_{pq} / (R_p * R_q)")
print("=" * 70)
print(f"{'p':>5} {'q':>5} {'R_pq':>12} {'R_p':>10} {'R_q':>10} {'ratio':>12}")
print("-" * 70)

test_primes = [5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

kuroda_ratios = []
for i in range(len(test_primes)):
    for j in range(i+1, min(i+5, len(test_primes))):
        p, q = test_primes[i], test_primes[j]
        sol_pq = fundamental_solution_pell(p * q)
        sol_p  = fundamental_solution_pell(p)
        sol_q  = fundamental_solution_pell(q)
        if sol_pq and sol_p and sol_q:
            Rpq = sol_pq[3]
            Rp  = sol_p[3]
            Rq  = sol_q[3]
            ratio = Rpq / (Rp * Rq)
            kuroda_ratios.append(ratio)
            print(f"{p:>5} {q:>5} {Rpq:>12.5f} {Rp:>10.5f} {Rq:>10.5f} {ratio:>12.5f}")

if kuroda_ratios:
    print(f"\n  Kuroda-Verhältnis: min={min(kuroda_ratios):.4f}  "
          f"max={max(kuroda_ratios):.4f}  mean={sum(kuroda_ratios)/len(kuroda_ratios):.4f}")
    print("  (Wenn stabil ≈ const: REG ≤ FACTOR wäre plausibel)")
    print("  (Wenn chaotisch: kein einfacher Zusammenhang)")

# ============================================================
print("\n" + "=" * 70)
print("EXPERIMENT 4: Precision Trap")
print("Wie viele Bits R_K braucht man, um h_K zu bestimmen?")
print("=" * 70)

# Nutze: h_K * R_K = sqrt(D)/2 * L(1, chi_D)
# Approximiere L(1, chi_D) via Dirichlet-Reihe (erster Term)
# Genauigkeitsbedarf: delta_R_K < R_K / (2 * h_K)
# -> bits = ceil(log2(2 * h_K))
# (echtes h_K hier über Klassenzahl-Formel + bekanntes R_K)

# Für Experiment: schätze h_K aus der Klassenzahlformel
# h_K = round(sqrt(D) / (2 R_K) * L(1, chi_D))

def L1_approx(D, terms=100000):
    """Approximiere L(1, chi_D) = sum_{n=1}^{inf} chi_D(n)/n"""
    # Kronecker-Symbol chi_D(n) für D squarefree
    # Vereinfacht: Jacobi-Symbol (D|n) für ungerade n
    total = Decimal(0)
    for n in range(1, terms + 1):
        chi = jacobi_symbol(D, n)
        if chi != 0:
            total += Decimal(chi) / Decimal(n)
    return float(total)

def jacobi_symbol(a, n):
    """Jacobi-Symbol (a|n)"""
    if n <= 0 or n % 2 == 0:
        return 0
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0

print(f"{'p':>5} {'q':>5} {'R_K':>12} {'h_K (est)':>12} {'Bits benötigt':>15}")
print("-" * 60)

precision_pairs = [(5,11),(11,13),(17,19),(23,29),(29,31),(37,41),(41,43),(47,53)]
for p, q in precision_pairs:
    N = p * q
    sol = fundamental_solution_pell(N)
    if sol:
        x, y, sign, R = sol
        D = 4 * N  # disc für N ≡ 2,3 mod 4; vereinfacht
        try:
            L1 = L1_approx(D, terms=50000)
            h_est = round(math.sqrt(abs(D)) / (2 * R) * L1)
            if h_est <= 0:
                h_est = 1
        except:
            h_est = 1
        bits_needed = math.ceil(math.log2(max(2 * h_est, 2)))
        print(f"{p:>5} {q:>5} {R:>12.5f} {h_est:>12} {bits_needed:>15}")

# ============================================================
print("\n" + "=" * 70)
print("EXPERIMENT 5: Wachstumsrate R_K — Entspricht L[1/2]?")
print("L[1/2]-Vorhersage: log(R_K) ~ c * sqrt(log N)")
print("=" * 70)
print(f"{'N':>12} {'log(N)':>8} {'R_K':>14} {'log(R)':>10} {'log(R)/sqrt(logN)':>20}")
print("-" * 70)

# Nehme aufeinanderfolgende Primpaare
all_primes = primes_up_to(2000)
twin_and_cousin = [(all_primes[i], all_primes[i+1])
                   for i in range(len(all_primes)-1)
                   if all_primes[i+1] < 2000][::3][:20]

for p, q in twin_and_cousin:
    N = p * q
    if N < 4:
        continue
    sol = fundamental_solution_pell(N)
    if sol and sol[3] > 1:
        R = sol[3]
        logN = math.log(N)
        logR = math.log(R)
        ratio = logR / math.sqrt(logN)
        print(f"{N:>12} {logN:>8.3f} {R:>14.4f} {logR:>10.4f} {ratio:>20.5f}")

print("\n  Wenn ratio konstant: R_K wächst wie exp(c*sqrt(log N)) = L_N[1/2, c]")
print("  Wenn ratio wächst:   R_K wächst schneller als L[1/2]")
print("  Wenn ratio fällt:    R_K wächst langsamer als L[1/2]")
