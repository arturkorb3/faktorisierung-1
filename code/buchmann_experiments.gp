// buchmann_experiments.gp
// Empirische Untersuchung: R_K für Semiprime N=pq
// Frage: Korreliert R_K mit Faktorisierungsschwierigkeit?
// Läuft mit: gp < buchmann_experiments.gp

\p 38  \\ 38 Dezimalstellen Genauigkeit

\\ === Hilfsfunktionen ===

{semiprime_data(p, q) =
  my(N = p*q, K, R, h, D);
  K = bnfinit(Pol([1,0,-N]), 1);   \\ x^2 - N
  R = K.reg;
  h = K.clgp.no;
  D = K.disc;
  [N, p, q, R, h, D, p+q, abs(p-q)]
}

\\ Ausgabe-Header
print("N | p | q | R_K | h_K | disc | p+q | |p-q|");
print("-----------------------------------------------------------------------");

\\ === Experiment 1: Kleine Semiprime, alle Paare ===
{
  my(ps = [3,5,7,11,13,17,19,23,29,31,37,41,43,47]);
  for(i=1, #ps,
    for(j=i+1, #ps,
      my(d = semiprime_data(ps[i], ps[j]));
      printf("N=%-6d (%2d*%2d)  R=%10.4f  h=%-4d  |p-q|=%-6d\n",
             d[1], d[2], d[3], d[4], d[5], d[8])
    )
  )
}

print("\n=== Experiment 2: Gleiche N, verschiedene Bitlängen ===");
print("Messe ob R_K/sqrt(N) eine stabiles Verhältnis zeigt\n");

{
  my(pairs = [
    [3,5], [5,7], [11,13], [29,31], [41,43], [71,73], [101,103],
    [3,7], [3,11], [3,101], [5,101], [7,101],
    [11,101], [13,103], [17,107]
  ]);
  print("N | R_K | h_K | R_K/sqrt(N) | log(R_K)/log(N)");
  for(i=1, #pairs,
    my(d = semiprime_data(pairs[i][1], pairs[i][2]));
    my(N=d[1], R=d[4], h=d[5]);
    printf("N=%-8d  R=%12.4f  h=%-4d  R/sqrt(N)=%8.5f  logR/logN=%6.4f\n",
           N, R, h, R/sqrt(N), log(R)/log(N))
  )
}

print("\n=== Experiment 3: Frage REG ≤ FACTOR? ===");
print("Gegeben p,q: Ist R_K aus p,q in poly-Zeit berechenbar?\n");
print("Test: Vergleiche R_{Q(sqrt(pq))} mit R_{Q(sqrt(p))} und R_{Q(sqrt(q))}\n");

{
  my(ps = [5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]);
  print("p | q | R_{pq} | R_p | R_q | R_{pq}/(R_p * R_q) | Kuroda-Index");
  for(i=1, #ps-1,
    for(j=i+1, min(i+3, #ps),
      my(p=ps[i], q=ps[j]);
      my(Kpq = bnfinit(Pol([1,0,-p*q]),1));
      my(Kp  = bnfinit(Pol([1,0,-p]),1));
      my(Kq  = bnfinit(Pol([1,0,-q]),1));
      my(Rpq = Kpq.reg, Rp = Kp.reg, Rq = Kq.reg);
      my(hpq = Kpq.clgp.no, hp = Kp.clgp.no, hq = Kq.clgp.no);
      printf("(%2d,%2d) R_pq=%8.4f R_p=%6.4f R_q=%6.4f ratio=%8.5f  h=(%d,%d,%d)\n",
             p, q, Rpq, Rp, Rq, Rpq/(Rp*Rq), hpq, hp, hq)
    )
  )
}

print("\n=== Experiment 4: Precision Trap ===");
print("Wie viele Bits braucht man in R_K um h_K zu bestimmen?\n");
{
  \\ h_K * R_K = sqrt(D)/2 * L(1,chi_D)
  \\ Fehler in R_K: delta_R -> Fehler in h_K: delta_h ~ h_K * delta_R / R_K
  \\ Um h_K exakt zu bestimmen: brauche delta_R < 1/(2*h_K)
  \\ Also Präzision: bits(R_K) + bits(h_K)

  my(ps = [5,11,13,23,29,31,37,41]);
  print("p | q | R_K | h_K | benötigte Bits für h_K-Bestimmung");
  for(i=1, #ps-1,
    my(p=ps[i], q=ps[i+1]);
    my(K = bnfinit(Pol([1,0,-p*q]),1));
    my(R = K.reg, h = K.clgp.no);
    my(bits_needed = ceil(log(2*h*R)/log(2)));
    printf("(%2d,%2d)  R=%10.4f  h=%-4d  Bits für h_K: %d\n",
           p, q, R, h, bits_needed)
  )
}

print("\n=== Experiment 5: Wächst R_K schneller als L[1/2]? ===");
print("Messe für wachsende Semiprime\n");
{
  \\ Semiprime mit p,q ~ sqrt(N), also N ~ p^2
  my(ps = nextprime(100));
  my(results = []);
  for(k=1, 15,
    my(p = nextprime(ps), q = nextprime(p+1));
    ps = q;
    my(N=p*q);
    my(K = bnfinit(Pol([1,0,-N]),1));
    my(R = K.reg, h = K.clgp.no);
    \\ L[1/2]-Vorhersage für R: exp(c * sqrt(log N))
    my(L12 = exp(sqrt(log(N))));
    printf("N=%-10d  log(N)=%5.2f  R=%12.4f  log(R)=%8.4f  log(R)/sqrt(log(N))=%6.4f\n",
           N, log(N), R, log(R), log(R)/sqrt(log(N)))
  )
}

quit
