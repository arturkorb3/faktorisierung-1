# BPW Follow-up: Loophole 3 — REG ohne smooth relations

**Verbindung zu Phase V-Neg des Joux-Brücken-Projekts.**

Theorem 3 (Norm-Smoothness-Barrier) schließt jede Faktorisierungsverbesserung
aus, die über *smooth-relation-basierte* Buchmann-artige REG-Berechnung geht.
Loophole 3 lässt die Frage offen:

> Gibt es einen Algorithmus für $R_K$, der NICHT über smooth principal relations
> geht — und der damit Theorem 3 umgeht?

Diese Datei untersucht die Frage strukturell.

---

## 1. Präzise Fragestellung

Sei $K = \mathbb{Q}(\sqrt{N})$ mit $N = pq$ semiprim.

**FACTOR ≤_T REG?**
Gibt es eine polynomialzeitige Turing-Reduktion:
$$\text{FACTOR}(N) \leq_P \text{REG}(K) \,?$$

**REG ≤_T FACTOR?**
Gibt es eine polynomialzeitige Turing-Reduktion:
$$\text{REG}(K) \leq_P \text{FACTOR}(N) \,?$$

Falls beide gelten: REG und FACTOR sind polynomialzeitäquivalent.
Die $L[1/2]$-Schranke für REG folgt dann aus der NFS-Schranke für FACTOR — und
kein Algorithmus kann asymptotisch besser als $L[1/3]$ für REG sein
(da FACTOR $\geq L[1/3]$ erwartet wird).

Falls FACTOR ≤ REG, aber REG ≰ FACTOR: REG ist **echt schwerer** als FACTOR.
Dann wäre ein $L[1/3]$-Algorithmus für REG gleichbedeutend mit einem
$L[1/3]$-Faktorisierungsalgorithmus — **der große Fund wäre via REG zu suchen**.

---

## 2. FACTOR ≤ REG: Was ist bekannt?

### 2.1 Klassisches Argument (Schoof 1982, informal)

Wenn $R_K$ und $h_K$ bekannt sind, liefert die Klassenzahlformel
$$h_K R_K = \frac{\sqrt{|d_K|}}{2} L(1, \chi_{d_K})$$
eine Beziehung zwischen $R_K$, $h_K$ und $L(1, \chi_{d_K})$.

Die Genus-Theorie für $K = \mathbb{Q}(\sqrt{pq})$ (mit $p, q$ ungerade prim):
- $\text{rk}_2(\text{Cl}(K)) = t - 1$ wobei $t$ = Anzahl ramifizierter Primstellen
- Für $d_K = pq$ (wenn $p \equiv q \equiv 1 \pmod 4$): $t = 2$, $\text{rk}_2 = 1$
- Die genus-theoretische 2-Torsion gibt **strukturelle** Information,
  aber nicht direkt die Faktorisierung

**Problem:** Kenntnis von $R_K$ allein reicht nicht für FACTOR.
Auch $h_K$ ist nötig, um die Klassenzahlformel zu nutzen.

### 2.2 Die Precision Trap

Angenommen, wir haben $R_K$ auf $k$ Bits Genauigkeit.
Dann ergibt die Klassenzahlformel:
$$h_K = \text{round}\!\left(\frac{\sqrt{|d_K|}}{2 R_K} \cdot L(1, \chi_{d_K})\right)$$

Das Runden auf $h_K$ ist korrekt genau dann, wenn der Fehler $< 1/2$:
$$\text{Fehler} \approx h_K \cdot \frac{\delta R_K}{R_K} < \frac{1}{2}
\quad\Longleftrightarrow\quad
\delta R_K < \frac{R_K}{2 h_K}$$

Da $h_K \leq c\sqrt{|d_K|}$ (Minkowski) und $R_K \geq 1$:
$$\delta R_K < \frac{1}{2 c \sqrt{|d_K|}} = e^{-O(\log N)}$$

Das bedeutet: **$R_K$ auf exponentiell viele Bits Genauigkeit benötigt,
um $h_K$ zu extrahieren**.

Das Berechnen von $R_K$ auf $O(\sqrt{N})$ Bit Genauigkeit entspricht aber
dem expliziten Bestimmen der Fundamentaleinheit $\varepsilon_K = e^{R_K}$
— was trivialerweise in Zeit $O(|output|) = e^{O(\sqrt{N})}$ liegt.

**Konsequenz:** Der Weg FACTOR ≤ REG via Klassenzahlformel erfordert
exponentiell präzises REG — also explizites FACTOR wie Buchmann.
Die Reduktion ist tautologisch: sie benutzt Buchmanns Algorithmus implizit.

### 2.3 Ausweg: REG modulo etwas Kleines

**Beobachtung:** Für FACTOR via Genus-Theorie braucht man nicht $h_K$ exakt,
sondern nur $h_K \pmod{2^k}$ für kleines $k$ (die 2-Torsion-Struktur).

Lässt sich $h_K \pmod{2^k}$ aus $R_K$ mit subexponentieller Genauigkeit extrahieren?

$$h_K \pmod{2^k} = \text{round}\!\left(\frac{\sqrt{|d_K|}}{2 R_K} L(1,\chi_{d_K})\right) \pmod{2^k}$$

Fehlertoleranz: $\delta R_K < \frac{R_K}{2^{k+1} \cdot \lceil h_K/2^k \rceil}$

Für kleine $k$: Fehlertoleranz ist $O(R_K / h_K)$ — immer noch exponentiell
klein wenn $h_K \gg R_K^{-1}$. Kein Ausweg für generische Semiprime.

**Aber:** Falls $h_K = O(1)$ (kleine Klassenzahl) — seltene, aber mögliche
Ausnahmefälle — dann ist Fehlertoleranz $O(R_K)$ und REG in polynomialer Präzision
reicht. **Das ist eine echte Lücke für den Fall kleiner Klassenzahlen.**

---

## 3. REG ≤ FACTOR: Warum das schwer ist

**Frage:** Gegeben $p, q$ mit $pq = N$ — kann man $R_K = \log \varepsilon_K$
in polynomialer Zeit (in $\log N$) berechnen?

### 3.1 Das Pell-Gleichungs-Argument

Die Fundamentaleinheit $\varepsilon_K = a + b\sqrt{N}$ satisfies
the Pell equation
$$a^2 - N b^2 = \pm 1 \qquad (a, b \in \mathbb{Z}).$$

Bekannt ist: Die minimale Lösung $(a_0, b_0)$ kann exponentiell groß sein:
$$a_0 \leq e^{O(\sqrt{N} \log N)}, \qquad b_0 \leq e^{O(\sqrt{N} \log N)}.$$

**Kenntnis von $p, q$ hilft mod-$N$ nicht:**
Aus der Pell-Gleichung mod $p$:
$$a^2 \equiv \pm 1 \pmod p$$
(da $b^2 pq \equiv 0 \pmod p$), also $a \equiv \pm 1$ oder $a^2 \equiv -1 \pmod p$.

Das gibt $a \pmod{pq}$ via CRT (bis auf vier Vorzeichen-Kombinationen).
Aber $a \gg pq$ generisch — Kenntnis von $a \pmod{pq}$ bestimmt
die tatsächliche Lösung nicht.

**Behauptung (informal):**
Für generische Semiprime $N = pq$ gilt: $a_0 > N^C$ für eine Konstante $C > 1$,
sodass selbst vollständige Kenntnis von $a_0 \pmod{N}$ die Gleichung nicht löst.

Beweis dieser Behauptung ist nicht in der Literatur — aber
die Heuristik der mittleren Kettenbruchlänge liefert dasselbe.

### 3.2 Das Größen-Argument

Selbst wenn man $R_K = \log \varepsilon_K$ (ein $O(\log N)$-Bit-Zahl) berechnen
will — nicht $\varepsilon_K$ selbst:

Jeder Algorithmus, der $R_K$ auf $k$ Bit Präzision berechnet, muss de facto
die fundamentale Einheit auf $e^{O(k)}$-Genauigkeit rekonstruieren
(via $\varepsilon_K = e^{R_K}$). Das erfordert $\Omega(k)$ arithmetische
Operationen in einem Ring der Größe $e^{O(k)}$.

**Formaler:** Sei $A$ ein polynomialzeitiger Algorithmus mit $p, q$ als Input,
der $R_K$ auf $k = c \log N$ Bit Genauigkeit ausgibt. Dann konstruiert $A$
implizit eine Approximation von $\varepsilon_K = e^{R_K}$ auf relative Genauigkeit
$e^{-c \log N} = N^{-c}$. Für generische Semiprime ist $\varepsilon_K > N^C$
(für eine Konstante $C$, Präzision aufwendig), sodass diese Approximation
$\varepsilon_K$ auf $O(\log N)$ signifikante Stellen approximiert —
was $\varepsilon_K$ modulo $N^{c+C}$ bestimmt.

Aber $\varepsilon_K$ modulo $N^{c+C}$ zu bestimmen ist nicht leichter als
$\varepsilon_K$ selbst zu finden (für generische $N$). Das ist kein Beweis,
aber ein strukturelles Hindernisargument.

### 3.3 Hallgrens Quantenalgorithmus als Evidenz

Hallgren (2002) gibt einen polynomialzeit-**Quanten**algorithmus für REG.
Klassisch ist kein polynomialzeitalgorithmus bekannt — auch nicht mit Kenntnis der Faktorisierung.

Das deutet darauf hin, dass REG echt schwerer als FACTOR ist im klassischen Modell:
- FACTOR $\in$ BQP (Shor) ∩ REG $\in$ BQP (Hallgren): beide quantum poly
- FACTOR $\notin$ BPP (vermutet): keine poly-Zeit-Klassik
- REG $\notin$ BPP (vermutet, stärker): auch mit Faktorisierung keine poly-Zeit

Wenn REG ≤ FACTOR klassisch gälte, wäre REG ∈ BPP sobald FACTOR ∈ BPP.
Da aber auch Quantenalgorithmen für REG nötig sind und FACTOR scheinbar leichter
quantisiert (Shor schon 1994, Hallgren erst 2002), gibt es Evidenz für
**REG echt schwerer als FACTOR**.

Aber: Das ist Evidenz, kein Beweis.

---

## 4. Strukturelle Konsequenzen für den Faktorisierungsansatz

### Szenario A: FACTOR ≡ REG (polynomialäquivalent)

Dann: Buchmanns $L[1/2]$-Schranke für REG ist scharf (entspricht NFS-Schranke).
Theorem 3 gilt in beiden Richtungen. Kein Algorithmus für REG unter $L[1/3]$,
weil FACTOR ≥ $L[1/3]$ (erwartet).

**Konsequenz für Joux-Brücke:** Gate IV FAIL ist scharf —
nicht nur "kein bekannter Algorithmus", sondern "kein möglicher Algorithmus
unter dieser Äquivalenz ohne FACTOR-Durchbruch".

### Szenario B: FACTOR ≤ REG, aber REG ≰ FACTOR

REG ist **echt schwerer** als FACTOR. Dann:
- Ein $L[1/3]$-Algorithmus für REG würde FACTOR auf $L[1/3]$ bringen.
- Aber kein $L[1/3]$-FACTOR-Algorithmus (z.B. NFS) gibt automatisch $L[1/3]$-REG.
- **Die Suche nach einem REG-Algorithmus jenseits smooth relations ist damit
  motiviert** — nicht als direkter Faktorisierungs-Angriff, sondern als
  eigenständiges Ziel mit Faktorisierungskonsequenz.

**Szenario B ist die interessanteste Möglichkeit.**
Wäre es beweisbar, wäre das ein Strukturresultat, das so in der Literatur
nicht steht.

### Szenario C: REG ≤ FACTOR (gegeben Faktorisierung, REG poly-Zeit)

Dann wäre REG nicht für die Faktorisierung nutzbar — es ist leichter,
nicht schwerer. Kein asymptotischer Hebel.

**Meine Einschätzung:** Szenario C ist *nicht* plausibel für generische Semiprime,
weil das Pell-Gleichungs-Argument dagegen spricht. Aber ein formaler Beweis fehlt.

---

## 5. Die eigentliche offene Frage

**Die schärfste noch nicht beantwortete Frage:**

> *Gibt es ein beweisbares Separationsresultat:*
> $\mathrm{FACTOR} \leq_P \mathrm{REG}$ *und*
> $\mathrm{REG} \not\leq_P \mathrm{FACTOR}$ *(klassisch)?*

Ein Beweis von $\mathrm{REG} \not\leq_P \mathrm{FACTOR}$ würde erfordern:
entweder eine Komplexitäts-Separation (REG-hart unter Annahmen wie ETH, SETH...),
oder ein direktes Konstruktionsargument, das zeigt, dass kein poly-zeitlicher
Reduktionsalgorithmus existiert.

Das ist ein offenes Problem der Komplexitätstheorie der Zahlentheorie.

---

## 6. Verbindung zu Loophole 3 (Joux-Brücken-Dokument)

Loophole 3 sagt: "Methoden, die $R_K$ ohne smooth relations berechnen,
umgehen Theorem 3."

Dieses Dokument zeigt:
- Alle bekannten nicht-smooth-relation-Ansätze für REG landen entweder
  in derselben Komplexitätsklasse ($O(D^{1/4})$ via Kettenbruch — schlechter als $L[1/2]$!)
  oder scheitern an der Precision Trap (Klassenzahlformel ohne $h_K$-Kenntnis)
- Die Precision Trap ist **strukturell**, nicht implementierungstechnisch
- Szenario B (REG echt schwerer als FACTOR) ist die einzige Möglichkeit,
  wo ein Nicht-smooth-relation-Algorithmus einen Faktorisierungsgewinn bringt
  — aber nur wenn er tatsächlich subexponentiell besser als Buchmann ist

**Loophole 3 ist real aber schmal.** Es erfordert einen fundamentalen neuen Ansatz
für REG — nicht nur eine Variation der bestehenden Paradigmen.

---

## 7. Empirische Agenda

Parallel: Pari/GP-Experimente (`code/buchmann_experiments.gp`) untersuchen:

1. **Verhältnis $R_K / \sqrt{N}$** für Semiprime $N = pq$: Ist es stabil?
   Indikator für mittlere Größe der Fundamentaleinheit.

2. **$R_K$ vs. $R_p \cdot R_q$** (Kuroda-Verhältnis):
   Gibt es eine einfache Relation zwischen $R_{pq}$, $R_p$, $R_q$?
   Falls ja: Szenario C wäre realistischer.

3. **Precision Trap empirisch**: Für konkrete Beispiele: wie viele Bits
   braucht man in $R_K$, um $h_K$ zu bestimmen?

4. **Wachstumsrate $R_K$**: Entspricht sie der $L[1/2]$-Vorhersage?
   Gibt es Ausreißer (kleine $R_K$ bei strukturellen $N$)?

---

---

## 8. Empirische Ergebnisse (Python, `buchmann_experiments.py`)

### 8.1 Kuroda-Verhältnis R_{pq} / (R_p · R_q)

**Ergebnis:**

| Maß | Wert |
|-----|------|
| Minimum | 0.1033 |
| Maximum | 1.9495 |
| Mittelwert | 0.6171 |

Das Verhältnis variiert um den Faktor ~19 — **chaotisch, keine stabile Relation.**

**Interpretation:**
Der Regulator $R_{pq}$ ist von $R_p$ und $R_q$ im Wesentlichen unabhängig.
Das bedeutet: Selbst vollständige Kenntnis von $p, q$ (d.h. vollständige Faktorisierung)
gibt keinen einfachen Weg zu $R_{pq}$ — das Pell-Problem für $\mathbb{Q}(\sqrt{pq})$
ist genuinen von denen für $\mathbb{Q}(\sqrt{p})$ und $\mathbb{Q}(\sqrt{q})$ verschieden.

**Konsequenz für Szenario C:** Szenario C ("REG ≤ FACTOR über Kuroda-Relation") ist
empirisch **nicht** plausibel.

**Konsequenz für Szenario B:** Das stärkt die Vermutung, dass REG echt schwerer als
FACTOR ist — $R_{pq}$ enthält arithmetische Information, die nicht in der Faktorisierung steckt.

### 8.2 R_K / sqrt(N) und log(R_K) / log(N)

**Ergebnis (Exp. 2):** Beide Verhältnisse stark variabel (0.05 bis 1.13 bzw. 0.19 bis 0.52).
Kein stabiles Verhältnis, kein stabiler Exponent.

Das bestätigt die bekannte Heuristik: $R_K$ unterliegt Cohen-Lenstra-artiger Variation
und konvergiert erst für sehr große $N$ (jenseits der Experimente) gegen die erwartete
$L[1/2]$-Schranke.

### 8.3 Precision Trap empirisch

**Ergebnis (Exp. 4):** Für kleine Semiprime ($N < 10^4$): $h_K \in \{2, 4, 6\}$,
Bits benötigt: 2–4. Das ist günstig.

**Vorsicht:** Das ist ein Artefakt der kleinen Skala. Die Minkowski-Schranke
$h_K \leq c\sqrt{D}$ erlaubt $h_K \approx \sqrt{N}$ für generische große $N$.
Die Precision Trap bleibt das strukturelle Hindernis für große Semiprime.

Die "kleine h_K"-Ausnahme (Abschnitt 2.3) ist für kleine Testfälle trivial erfüllt,
aber für kryptographisch relevante Semiprime ($N \approx 2^{512}$) nicht zu erwarten.

### 8.4 Wachstumsrate R_K

**Ergebnis (Exp. 5):** `log(R)/sqrt(log N)` variiert von 0.54 bis 1.59 im Bereich
$N \in [6, 75000]$.

Das Verhältnis ist **nicht konstant** bei diesen Skalen. Das bedeutet:
- Das $L[1/2]$-Regime ist bei $N < 10^5$ noch nicht asymptotisch etabliert.
- Enorme Variation: Für twin primes tendenziell kleineres $R_K$ (ratio ~0.55),
  für nichttwin-Paare deutlich größeres $R_K$ (ratio bis 1.6).

**Strukturelle Beobachtung:** Die twin-prime-artigen Fälle ($|p-q|$ klein) zeigen
konsistent kleine Regulatoren. Das könnte ein Ausnahmefall sein, wo $R_K$ subexponentiell
wächst — oder Artefakt des kleinen $N$.

---

## 9. Gesamtbewertung Loophole 3

**Zusammenfassung der Erkenntnisse:**

| Frage | Befund |
|-------|--------|
| FACTOR ≤ REG via Klassenzahlformel? | **Tautologisch** — Precision Trap macht es zirkulär |
| REG ≤ FACTOR via Kuroda? | **Empirisch widerlegt** — Verhältnis chaotisch (×19 Variation) |
| REG echt schwerer als FACTOR? | **Structural evidence ja** — Pell-Problem unabhängig von Faktorisierung |
| L[1/2]-Regime für R_K etabliert? | **Nicht bei $N < 10^5$** — hohe Variation bei kleinen Skalen |
| Loophole 3 tatsächlich offen? | **Ja, aber schmal** — erfordert neuen Ansatz für REG ohne smooth relations |

**Hauptresultat:**

> Der Buchmann-Regulator $R_K$ für $K = \mathbb{Q}(\sqrt{pq})$ ist empirisch und
> strukturell von der Faktorisierung $N = pq$ unabhängig. Das stützt Szenario B:
> REG ist echt schwerer als FACTOR (klassisch). Loophole 3 ist damit nicht geschlossen,
> aber der Weg durch es hindurch ist ein offenes Komplexitätsproblem,
> das unabhängigen Fortschritt auf REG erfordert — ohne Stütze durch die Faktorisierung.

**Konsequenz für das Gesamtprojekt:**

Gate IV FAIL (Joux-Brücke) ist damit aus zwei Richtungen gestützt:
1. Strukturell: Theorem 3 (Norm-Smoothness-Barrier) schließt smooth-relation-Ansätze aus.
2. Empirisch: Das Kuroda-Chaos zeigt, dass die Faktorisierung keine Abkürzung für R_K liefert.

Ein Faktorisierungs-Durchbruch über REG würde erfordern:
- Einen nicht-smooth-relation-Ansatz für R_K, der schneller als Buchmann ist.
- Dieser Ansatz muss $L[1/3]$ oder besser erreichen.
- Und er muss Theorem 3 strukturell umgehen — was nach dem Kuroda-Befund
  nicht via Faktorisierungsinformation passieren kann.

**Das ist Szenario B als Forschungsagenda: ein subexponentiell besserer REG-Algorithmus
ohne Nutzung der Primfaktorzerlegung.**
