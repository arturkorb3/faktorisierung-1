# Experimentdesign: Half-Distance Inversion und Square-Form Locator

## Ziel

Wir testen die engste verbliebene Hauptschiene:

\[
R_D \;\Longrightarrow\; \text{Form bei Distanz }R_D/2
\quad\text{oder}\quad
\text{Position einer Square Form im principal cycle}.
\]

Ein echter Durchbruch bräuchte eine nichtzufällige, ohne Faktorisierung erkennbare Struktur in diesen Positionen. Das Experiment sucht daher nicht nach einer besseren Implementierung von SQUFOF, sondern nach **Phase-Anomalien**.

---

## Objekte

Für semiprime

\[
N=pq
\]

betrachten wir die Continued-Fraction/SQUFOF-Zustände für \(\sqrt N\):

\[
P_{i+1}=a_iQ_i-P_i,
\]

\[
Q_{i+1}=\frac{N-P_{i+1}^2}{Q_i},
\]

\[
a_{i+1}=\left\lfloor \frac{a_0+P_{i+1}}{Q_{i+1}}\right\rfloor,
\qquad a_0=\lfloor \sqrt N\rfloor.
\]

Die Periode schließt bei

\[
Q_i=1,\qquad P_i=a_0.
\]

Square-form-Ereignisse werden zunächst durch

\[
Q_i=s^2,
\qquad Q_i\ne 1
\]

approximiert. Das ist bewusst nur ein **Proxy** für die volle Formtheorie; für die erste Phase reicht es, weil genau diese Square-\(Q_i\)-Ereignisse die SQUFOF-Phase sichtbar machen.

---

## Messgrößen

Pro \(N\):

1. Periodenlänge
   \[
   L=\#\text{CF-Zustände}.
   \]

2. Half-Index
   \[
   h=\lfloor L/2\rfloor.
   \]

3. Half-Zustand
   \[
   (P_h,Q_h,a_h).
   \]

4. Triviale Faktor-Diagnostik
   \[
   \gcd(P_h,N),\quad \gcd(Q_h,N),\quad \gcd(a_h,N).
   \]

5. Square-Positionen
   \[
   S=\{i: Q_i=s^2,
   Q_i\ne1\}.
   \]

6. Erste normalisierte Square-Phase
   \[
   \theta_1=\frac{\min S}{L}.
   \]

7. Nächste Square-Position zu \(L/2\):
   \[
   \min_{i\in S} |i-L/2|_{\mathrm{cyc}}.
   \]

8. Korrelationen mit:
   - \(N\bmod 8\),
   - Periodenparität,
   - Pell-Norm \(\pm1\),
   - \(L\),
   - \(\log\varepsilon\),
   - Nähe von \(p/q\) zu 1, wenn \(p,q\) für Diagnose bekannt sind.

---

## Hypothesen

### H0: Random-Phase-Modell

Square-Positionen sind, bedingt auf globale Invarianten, quasi zufällig im principal cycle verteilt.

Dann gilt ungefähr:

\[
\Pr[\text{Treffer in einem Test}]\approx N^{-1/4},
\]

und man braucht \(N^{1/4}\)-viele Tests. Das reproduziert die SQUFOF-Skala.

### H1: Half-Distance-Anomalie

Der Half-Zustand \(i\approx L/2\) oder eine kleine Umgebung davon enthält überdurchschnittlich oft:

- Square-\(Q_i\)-Ereignisse,
- ambige oder quasi-ambige Zustände,
- nichttriviale gcds mit \(N\),
- oder eine aus \(R,L,N\bmod m\) erkennbare Struktur.

Dann wäre Half-Distance-Inversion ein ernsthafter Kandidat.

### H2: Global-Invariant Locator

Die erste Square-Phase

\[
\theta_1=\frac{i_1}{L}
\]

ist nicht zufällig, sondern durch globale Invarianten approximierbar.

Dann könnte ein Square-Form-Locator gebaut werden.

---

## Kill-Kriterien

Die Hauptschiene ist wahrscheinlich ausgeschöpft, wenn alle drei Beobachtungen stabil sind:

1. Square-Phasen \(\theta_i\) sehen uniform/pseudorandom aus.
2. Die Half-Umgebung zeigt keine erhöhte Trefferquote.
3. Keine faktorisierungsfreie globale Invariante sagt \(\theta_i\) besser als Zufall voraus.

Dann lautet das Negativresultat:

> Regulator-/Periodenlänge bestimmt die Zyklusgröße, aber nicht die faktorisierungsrelevante Square-Form-Phase.

---

## Dateien

- `half_distance_sfl_experiment.py` erzeugt CSV-Diagnosedaten.

Beispiel:

```bash
python half_distance_sfl_experiment.py --bits 32 --samples 50 --seed 7 --out results_32bit.csv
```

Für explizite \(N\):

```bash
python half_distance_sfl_experiment.py --N 899,2491,11413 --out explicit.csv
```

---

## Wichtigste Lücke des Skripts

Das Skript implementiert keine vollständige indefinite binary quadratic form composition und kein vollständiges SQUFOF-Reverse-Step. Es misst die Phase-Anomalie im CF/SQUFOF-Kern. Falls dort ein Signal auftaucht, muss Phase 2 die volle Formtheorie ergänzen.

---

## Pilotbeobachtung aus dem Skript

Ein erster 32-bit-Pilotlauf

```bash
python half_distance_sfl_experiment.py --bits 32 --samples 20 --seed 5 --out pilot_32bit.csv
```

zeigte:

- 20/20 Perioden erfolgreich berechnet;
- 13/20 Zeilen hatten einen nichttrivialen gcd im Half-Zustand;
- die Treffer konzentrierten sich sichtbar auf Fälle mit gerader Periodenlänge bzw. Pell-Norm `+1`;
- bei ungerader Periodenlänge bzw. Pell-Norm `-1` trat in diesem kleinen Lauf kein direkter Half-gcd-Treffer auf.

Das ist **kein Beweis**, aber genau das erwartete Schoof-artige Signal:

\[
\text{Norm }+1 \quad\Rightarrow\quad R/2\text{-Ambiguität im principal cycle kann Faktorinformation tragen.}
\]

Die nächste Version muss daher nicht breit suchen, sondern die `pell_sign=+1`-Fälle isolieren und die Half-Zustände formtheoretisch normalisieren.
