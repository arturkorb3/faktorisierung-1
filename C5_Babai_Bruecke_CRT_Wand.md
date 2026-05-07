# Faktorisierung als Gruppenisomorphie?  
## Ein CRT-Wand-Abschluss des Babai-Brückenansatzes

**Projekt:** Faktorisierung 1  
**Auftrag:** C5 — Faktorisierung als Gruppenisomorphie, die Babai-Brücke  
**Status:** Forschungsnotiz / Negativabschluss des Babai-Strangs  
**Datum:** 2026-05-06  
**Kurzfassung:** Der naive Durchbruchspfad
\[
\mathrm{FACTOR}\to \text{kleine explizite GI-Instanz}\to \text{Babai}\to p,q
\]
wird innerhalb einer natürlichen Modellklasse geschlossen. Der Abschluss ist kein universeller Lower Bound gegen jede denkbare Isomorphie-Kodierung von Faktorisierung. Er zeigt vielmehr: Für explizite, polylogarithmisch große, produkt-kompatible algebraische Konstruktionen schlägt die CRT-Wand zwingend zu. Entweder die Konstruktion bleibt \(p/q\)-symmetrisch und trägt keine extrahierbare Faktorisierungsinformation, oder sie erzeugt bereits einen nichttrivialen CRT-Idempotenten und faktorisiert \(N\) schon vor dem Einsatz von Babais Algorithmus.

---

## 1. Ausgangsfrage

Sei \(N=pq\) ein RSA-artiger quadratfreier Semiprime. Der Babai-Brückenansatz fragt, ob es aus \(N\) allein effizient berechenbare Gruppen oder Graphen

\[
G_1(N),G_2(N)
\]

der Größe

\[
|G_i(N)|=\operatorname{poly}(\log N)
\]

geben kann, sodass ein Isomorphismus

\[
G_1(N)\cong G_2(N)
\]

nicht nur existiert, sondern als Witness die Faktoren \(p,q\) extrahierbar macht.

Die Motivation ist Babais quasipolynomieller Graph-Isomorphie-Algorithmus. Für eine Instanzgröße

\[
n=\operatorname{poly}(\log N)
\]

würde ein Laufzeitverhalten

\[
n^{O(\log n)}
\]

zu

\[
\exp(O((\log\log N)^2))
\]

führen. Das wäre asymptotisch weit schneller als der Number Field Sieve.

Die zentrale Frage lautet daher nicht, ob \(N=pq\) faktorisierbar ist — das ist es per Definition —, sondern:

> Kann eine kleine, aus \(N\) allein konstruierbare Isomorphieinstanz einen Witness tragen, aus dem ein nichttrivialer CRT-Bruch von \(\mathbb Z/N\mathbb Z\) extrahiert werden kann?

---

## 2. Modellklasse

Wir betrachten in dieser Notiz nicht beliebige, künstlich kodierte Reduktionen von Faktorisierung auf GI. Die betrachtete Modellklasse ist enger und mathematisch natürlich.

### Definition 2.1 — Babai-kompatible Instanz

Eine Instanzfamilie \(I(N)\) heißt **Babai-kompatibel**, wenn sie in polynomialer Zeit in \(\log N\) als expliziter Graph, explizite endliche Gruppe, explizite Permutationsstruktur oder äquivalente GI-kompatible Struktur der Größe

\[
n(N)=\operatorname{poly}(\log N)
\]

ausgegeben wird.

Insbesondere ist nicht erlaubt, eine Struktur mit \(N^\epsilon\), \(N\), \(N^2\) oder mehr Elementen vollständig zu expandieren.

### Definition 2.2 — Produkt-funktorielle algebraische Kodierung

Eine Kodierung \(F\) heißt **produkt-funktoriell**, wenn sie mit endlichen direkten Produkten verträglich ist:

\[
F(A\times B)\cong F(A)\times F(B)
\]

oder zumindest eine kanonische, effektiv rekonstruierbare Produktstruktur aus der Ringproduktstruktur induziert.

Typische Beispiele sind:

- \(R\mapsto R^\ast\),
- \(R\mapsto R^\ast/(R^\ast)^k\),
- \(R\mapsto E[\ell](R)\) für festes \(\ell\),
- \(R\mapsto\) modulare, torsorielle oder automorphismische Strukturen, soweit sie lokal komponentenweise definiert sind,
- Cayley- oder Automorphismengraphen, deren Generatoren funktoriell aus \(R\) erzeugt werden.

### Definition 2.3 — Nichttriviale Faktorisierungsinformation

Eine aus einem Isomorphismus-Witness extrahierte Information heißt **nichttriviale Faktorisierungsinformation**, wenn sie in polynomialer Zeit in \(\log N\) zu einem echten Faktor von \(N\) führt.

Die prototypischen Formen sind:

1. ein nichttrivialer Nullteiler \(z\not\equiv0\bmod N\) mit \(\gcd(z,N)\notin\{1,N\}\);
2. ein nichttrivialer Idempotent
   \[
   e^2\equiv e\pmod N,\qquad e\not\equiv0,1\pmod N;
   \]
3. eine nichttriviale Quadratwurzelkollision
   \[
   x^2\equiv y^2\pmod N,\qquad x\not\equiv\pm y\pmod N.
   \]

Alle drei Formen führen per \(\gcd\)-Berechnung unmittelbar zu einem Faktor.

---

## 3. Grundlemma: CRT-Idempotenten sind Faktorisierung

### Lemma 3.1 — Idempotenten-Faktor-Lemma

Sei \(N=pq\) quadratfrei. Gibt es ein

\[
e\in \mathbb Z/N\mathbb Z
\]

mit

\[
e^2=e,\qquad e\notin\{0,1\},
\]

dann faktorisiert

\[
\gcd(e,N)
\]

oder

\[
\gcd(e-1,N)
\]

das Modul \(N\).

### Beweis

Nach dem chinesischen Restsatz gilt

\[
\mathbb Z/N\mathbb Z\cong \mathbb F_p\times \mathbb F_q.
\]

Idempotenten in einem Produkt von Körpern sind komponentenweise \(0\) oder \(1\). Die vier Idempotenten sind

\[
(0,0),(1,1),(1,0),(0,1).
\]

Die ersten beiden entsprechen \(0\) und \(1\). Ein nichttrivialer Idempotent entspricht daher \((1,0)\) oder \((0,1)\). Sein Repräsentant ist durch genau einen der beiden Primfaktoren teilbar. Daher liefert \(\gcd(e,N)\) oder \(\gcd(e-1,N)\) einen echten Faktor. \(\square\)

---

## 4. Die CRT-Wand

### Theorem 4.1 — CRT-Wand für produkt-funktorielle Babai-Kodierungen

Sei \(F\) eine produkt-funktorielle algebraische Kodierung und \(N=pq\) quadratfrei. Angenommen, aus

\[
F(\mathbb Z/N\mathbb Z)
\]

wird eine Babai-kompatible explizite GI-Instanz \(I(N)\) der Größe \(\operatorname{poly}(\log N)\) konstruiert.

Dann gilt die folgende Dichotomie:

1. **Symmetrischer Fall.**  
   Die Konstruktion bleibt invariant unter Vertauschung der beiden CRT-Komponenten. Dann enthält jeder kanonisch aus \(I(N)\) berechenbare Isomorphieentscheid höchstens symmetrische oder Jacobi-artige Information und trennt \(p\) und \(q\) nicht.

2. **Trennender Fall.**  
   Die Konstruktion oder ein aus ihr extrahierter Isomorphismus-Witness wählt eine der beiden CRT-Komponenten effektiv aus. Dann erzeugt sie einen nichttrivialen CRT-Projektor und damit per Lemma 3.1 bereits eine Faktorisierung von \(N\).

Insbesondere kann eine solche Konstruktion Babais Algorithmus nicht als „letzten fehlenden Schritt“ verwenden: Entweder bleibt sie faktorisierungsblind, oder sie hat \(N\) bereits faktorisiert.

### Beweisskizze

Da \(N=pq\) quadratfrei ist,

\[
\mathbb Z/N\mathbb Z\cong \mathbb F_p\times \mathbb F_q.
\]

Produkt-Funktorialität liefert lokal

\[
F(\mathbb Z/N\mathbb Z)\cong F(\mathbb F_p)\times F(\mathbb F_q).
\]

Jede Information, die die beiden Faktoren nicht unterscheidet, ist invariant unter der Vertauschung

\[
F(\mathbb F_p)\times F(\mathbb F_q)
\longleftrightarrow
F(\mathbb F_q)\times F(\mathbb F_p).
\]

Sie kann höchstens symmetrische Daten tragen.

Sobald die Konstruktion dagegen eine der beiden Komponenten effektiv auswählt, erhält man einen Projektionsoperator auf diese Komponente. In der zugrunde liegenden Ringstruktur entspricht ein solcher Projektor einem nichttrivialen CRT-Idempotenten. Nach Lemma 3.1 faktorisiert dieser \(N\). \(\square\)

---

## 5. Kandidatenanalyse

### 5.1 Die Einheitengruppe \((\mathbb Z/N\mathbb Z)^\ast\)

Es gilt

\[
(\mathbb Z/N\mathbb Z)^\ast
\cong
\mathbb F_p^\ast\times \mathbb F_q^\ast.
\]

Die Gruppe ist als Menge zu groß:

\[
|(\mathbb Z/N\mathbb Z)^\ast|=\varphi(N)\approx N.
\]

Eine vollständige Cayley-Tabelle oder ein Graph auf den Elementen ist nicht Babai-kompatibel.

Kleine Quotienten wie

\[
(\mathbb Z/N\mathbb Z)^\ast/((\mathbb Z/N\mathbb Z)^\ast)^k
\]

sind abstrakt kleiner, aber ihre lokalen Komponenten sind wieder CRT-getrennt. Ohne Faktorisierung erhält man nur globale Residuen- oder Jacobi-artige Information. Die getrennten Legendre-Daten sind gerade das Verborgene.

**Status:** geschlossen durch Größe und CRT-Wand.

---

### 5.2 Nichttriviale Quadratwurzeln von \(1\)

Nichttriviale Lösungen von

\[
x^2\equiv1\pmod N
\]

entsprechen direkt den nichttrivialen CRT-Idempotenten. Eine solche Lösung faktorisiert \(N\) durch

\[
\gcd(x-1,N).
\]

**Status:** perfekt als Extraktionsmechanismus, aber nicht als konstruktiver Babai-Kandidat. Wer sie konstruieren kann, hat bereits faktorisiert.

---

### 5.3 Elliptische \(\ell\)-Torsion

Für eine elliptische Kurve \(E\) und kleines \(\ell\) ist die \(\ell\)-Torsion formal klein. Über einem Primkörper \(\mathbb F_p\) trägt die Frobenius-Wirkung auf \(E[\ell]\) Information über

\[
\#E(\mathbb F_p)\bmod \ell.
\]

Über \(\mathbb Z/N\mathbb Z\) zerfällt die Struktur jedoch lokal:

\[
E(\mathbb Z/N\mathbb Z)\cong E(\mathbb F_p)\times E(\mathbb F_q)
\]

soweit glatte gute Reduktion vorliegt. Die getrennten Frobeniusdaten bei \(p\) und \(q\) sind gerade die lokalen Informationen, die ohne CRT nicht zugänglich sind.

**Status:** mathematisch reich, aber als Babai-Brücke durch lokale Frobenius-/CRT-Wand geschlossen.

---

### 5.4 Galoisgruppen von \(N\)-abhängigen Polynomen

Kandidaten wie

\[
x^2-N,\quad x^m-N
\]

haben kleine Galoisgruppen. Diese Gruppen erkennen aber Kummer- oder Wurzelstrukturen von \(N\), nicht die konkrete Zerlegung \(N=pq\).

Sobald lokale Verzweigungs-, Inertie- oder Frobeniusdaten bei \(p\) und \(q\) verwendet werden, ist die Primzerlegung wieder explizit nötig.

**Status:** keine erkennbare Extraktion von \(p,q\).

---

### 5.5 Kleine \(N\)-abhängige Cayley- und Automorphismengraphen

Graphen auf einer kleinen festen Gruppe, deren Generatoren durch \(N\bmod m\) oder andere aus \(N\) leicht berechenbare Daten gewählt werden, sind Babai-kompatibel.

Sie tragen jedoch nur öffentliche Residueninformationen. Solche Daten sind weit schwächer als eine CRT-Trennung von \(p\) und \(q\).

**Status:** B3 grün, B4 rot.

---

## 6. Warum kein universeller Unmöglichkeitssatz bewiesen wird

Theorem 4.1 ist bewusst kein Satz der Form:

> Keine polylogarithmisch große GI-Kodierung von Faktorisierung kann existieren.

Eine solche Aussage wäre ein sehr starker Komplexitäts-Lower-Bound und ist mit den hier verfügbaren Methoden nicht erreichbar.

Es gibt auch keine reine Informationsbarriere. Eine Permutation auf

\[
n=\operatorname{poly}(\log N)
\]

Punkten kann

\[
\log(n!)
\]

Bits tragen, also prinzipiell genug Information, um einen Faktor von \(N\) zu kodieren.

Der Abschluss ist daher strukturell, nicht informationstheoretisch:

> Natürliche algebraische Konstruktionen, die \(N\) über \(\mathbb Z/N\mathbb Z\) behandeln und mit Produkten verträglich sind, können die \(p/q\)-Trennung nicht sichtbar machen, ohne bereits einen faktorisierenden CRT-Projektor zu erzeugen.

---

## 7. Babai-Kompatibilität und Expandierbarkeit

Babais Algorithmus ist ein Algorithmus für explizite Graphen beziehungsweise die damit verknüpften expliziten Gruppenwirkungsprobleme. Für

\[
n=\operatorname{poly}(\log N)
\]

wäre seine Laufzeit quasipolylogarithmisch in \(N\).

Viele algebraische Objekte, die faktorisierungsrelevante Witnesses enthalten, sind aber nur kompakt beschreibbar. Beispiel:

\[
R=(\mathbb Z/N\mathbb Z)[\varepsilon]/(\varepsilon^2).
\]

Dieser Ring hat eine Beschreibung von konstantem Rang über \(\mathbb Z/N\mathbb Z\), also Länge \(\operatorname{poly}(\log N)\). Als Menge hat er jedoch etwa \(N^2\) Elemente. Eine Expansion zu einem gewöhnlichen Graphen zerstört den Babai-Vorteil.

Das trennt zwei Welten:

\[
\text{kleine explizite GI-Instanz}
\neq
\text{kompakte algebraische Beschreibung}.
\]

Der Babai-Strang scheitert nicht daran, dass Isomorphie irrelevant wäre, sondern daran, dass die faktorisierungsrelevante Isomorphie in kompakten Ring-/Algebra-Beschreibungen lebt, nicht in kleinen expandierten Graphen.

---

## 8. Seitenast: Ringmorphismus statt Gruppenisomorphie

Kayal und Saxena zeigen, dass Integer Factorization und Graph Isomorphism auf Ringmorphismusprobleme endlicher Ringe reduzierbar sind. Insbesondere sind Zähl- und Suchvarianten von Ringautomorphie stark genug, Faktorisierungsinformation zu tragen.

Das ist keine Widerlegung des Babai-Abschlusses. Es erklärt ihn vielmehr:

- Ringinstanzen können sehr kleine Beschreibungslänge haben.
- Ihre Trägermenge kann aber polynomial oder exponentiell groß in \(N\) sein.
- Der relevante Witness kann ein CRT-Idempotent, Nullteiler oder eine Quadratwurzelkollision sein.
- Eine naive Expansion macht Babai unbrauchbar.

Daher lautet der sinnvolle Fortsetzungsstrang nicht mehr:

\[
\mathrm{FACTOR}\to\text{kleine GI-Instanz},
\]

sondern:

\[
\mathrm{FACTOR}\to\text{kompakte Ring-/Algebra-Isomorphie-Suche}.
\]

---

## 9. Tensor- und Algebra-Isomorphie als Fortsetzung

Eine endliche Algebra mit Basis \(e_1,\dots,e_r\) besitzt Strukturkonstanten

\[
e_i e_j=\sum_k c_{ijk}e_k.
\]

Diese bilden einen Tensor. Ring- und Algebra-Isomorphie sind daher spezielle Tensor-Isomorphieprobleme.

Über Feldern existiert eine breite Theorie, die Tensor-Isomorphie, Gruppenisomorphie, Polynomialäquivalenz und Algebra-Isomorphie verbindet. Über

\[
\mathbb Z/N\mathbb Z
\]

tritt jedoch wieder die versteckte Produktstruktur auf:

\[
\mathbb Z/N\mathbb Z\cong\mathbb F_p\times\mathbb F_q.
\]

Ein Tensor-Normalformalgorithmus über \(\mathbb Z/N\mathbb Z\), der so stark ist wie die lokalen Normalformen über \(\mathbb F_p\) und \(\mathbb F_q\), würde vermutlich CRT-Information rekonstruieren. Das ist keine Schließung, sondern der nächste präzise Forschungspunkt.

---

## 10. Abschlussurteil

### Gate I — Struktur

**PASS.**  
B1–B5 sind sinnvoll und trennen Konstruktion, Isomorphieäquivalenz, Babai-Kompatibilität, Informationsgehalt und CRT-Wand.

### Gate II — Instanzsuche

**FAIL für positive Babai-Kandidaten.**  
Alle natürlichen polylogarithmisch großen Kandidaten kollabieren an Größe, Symmetrie oder CRT-Trennung.

### Gate III — CRT-Wand

**PASS als bedingtes Theorem.**  
Für produkt-funktorielle algebraische Babai-Kodierungen gilt die Symmetrie-/Idempotent-Dichotomie.

### Gate IV — Quasipolynomielle Faktorisierung

**FAIL.**  
Kein Kandidat liefert eine Babai-kompatible Instanz, deren Isomorphismus \(p,q\) extrahiert.

### Gate V — Fortsetzung

**Nicht über kleine explizite GI.**  
Fortsetzung über kompakte Ring-, Algebra- und Tensor-Isomorphie.

---

## 11. Hauptsatz in Kurzform

> **Babai-CRT-Wand.**  
> Für natürliche, produkt-kompatible algebraische Konstruktionen aus \(\mathbb Z/N\mathbb Z\) gibt es keinen Babai-Brücken-Durchbruch der Form  
> \[
> \mathrm{FACTOR}
> \to
> \text{polylog-große explizite GI-Instanz}
> \to
> \text{Babai}
> \to
> p,q.
> \]
> Entweder bleibt die Instanz CRT-symmetrisch und enthält keinen extrahierbaren \(p/q\)-Bruch, oder die Konstruktion erzeugt einen nichttrivialen CRT-Idempotenten und faktorisiert \(N\) bereits vor dem GI-Schritt.

---

## 12. Offene präzise Folgefragen

1. **Ring-Isomorphie in konstanter Rangdarstellung.**  
   Klassifiziere quadratische Algebren
   \[
   (\mathbb Z/N\mathbb Z)[x]/(x^2+ux+v)
   \]
   bis Isomorphie, ohne \(N\) zu faktorisieren.

2. **Tensor-Normalformen über versteckten Produktringen.**  
   Zeige, dass vollständige Normalformen über \(\mathbb Z/N\mathbb Z\), die lokal vollständig sind, faktorisierende Idempotenten rekonstruieren.

3. **Witness-vs.-Decision-Trennung.**  
   Formuliere präzise, warum die Existenz eines Isomorphismus oft leicht oder trivial ist, während die Extraktion eines Witnesses faktorisierungshart bleibt.

4. **Keine kompakte-zu-explizite GI-Reduktion ohne Expansion.**  
   Beweise für relevante Ringinstanzen, dass jede Babai-kompatible Reduktion auf explizite GI entweder Größe \(\Omega(N^\epsilon)\) erzeugt oder schon einen Nullteiler/Idempotenten berechnet.

---

## 13. Fazit

Der Babai-Strang ist damit sauber abgeschlossen:

\[
\boxed{
\text{Babai hilft nicht, solange die faktorisierende Struktur nicht klein explizit vorliegt.}
}
\]

Die tiefere, weiterhin offene Richtung ist:

\[
\boxed{
\text{Faktorisierung als kompakte algebraische Isomorphie-Suche.}
}
\]

Das ist kein Rückschlag, sondern eine Präzisierung. Die naive GI-Brücke bricht an der CRT-Wand; ihr Bruch legt aber einen besseren Seitenast frei: Ring-, Algebra- und Tensor-Isomorphie über dem versteckten Produktring \(\mathbb Z/N\mathbb Z\).

---

## Referenzen

1. László Babai, **Graph Isomorphism in Quasipolynomial Time**, arXiv:1512.03547, 2015.  
   <https://arxiv.org/abs/1512.03547>

2. Eugene M. Luks, **Isomorphism of graphs of bounded valence can be tested in polynomial time**, Journal of Computer and System Sciences, 1982.  
   <https://www.sciencedirect.com/science/article/pii/0022000082900095>

3. Neeraj Kayal and Nitin Saxena, **Complexity of Ring Morphism Problems**, Computational Complexity, 2006/2007.  
   <https://link.springer.com/article/10.1007/s00037-007-0219-8>

4. Joshua A. Grochow and Youming Qiao, **On the Complexity of Isomorphism Problems for Tensors, Groups, and Polynomials I: Tensor Isomorphism-completeness**, ITCS 2021.  
   <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.31>

5. Joux–Buchmann Bridge: Gated Research Pass, internes Projektmaterial, Faktorisierung 1.  
   Siehe Projektdatei `Joux-Buchmann Faktorisierung.txt`.

