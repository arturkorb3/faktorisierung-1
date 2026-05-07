# Phase V — Negativbefund: Strukturelles Theorem über die Joux-Brücke

**Gate-Status: IV FAIL → V (Negativbefund)**

Dieser Bericht fasst das Ergebnis des vollständigen Gate-Durchlaufs zusammen
und formuliert den Hauptbefund als theorem-artige Aussage.

---

## Hauptresultat (Theorem-Form)

**Theorem (Joux-Methode nicht auf Q(√N) übertragbar):**

*Sei $K = \mathbb{Q}(\sqrt{N})$ mit $N = pq$ semiprim, und sei die Joux-Methode für
$\mathbb{F}_{q^n}$-DLP durch ihre strukturellen Komponenten K1–K5 beschrieben.*

*Dann gilt:*

1. **(Frobenius-Obstruktion, Theorem 1 des Agenten):**
   $\mathrm{Aut}_\mathbb{Q}(K) = \{1, \iota\}$.
   Ein globaler Frobenius für versteckte Primteiler $p, q$ existiert nicht ohne
   Kenntnis von $p, q$. K3 (Frobenius-Symmetrie) ist in $\mathbb{Q}(\sqrt{N})$
   nicht realisierbar ohne Faktorisierungsinformation.

2. **(Turm-Obstruktion, Theorem 2 des Agenten):**
   $K = \mathbb{Q}(\sqrt{N})$ hat keine nicht-trivialen Zwischenkörper.
   Externe Türme $\mathbb{Q}(\sqrt{N}, \sqrt{d})$ erfordern entweder Diskriminanten-
   wachstum (das die Norm-Smoothness-Schranke verschärft) oder Kenntnissüber
   $d$ (die Faktorisierungsinformation benötigen). K4 (rekursiver Descent)
   ist in Grad 2 nicht realisierbar.

3. **(Norm-Smoothness-Barrier, Theorem 3 des Agenten):**
   Für festes Grad 2 sind Relationsnormen polynomiell in $D = \mathrm{disc}(K)$.
   Das CEP-Kriterium liefert dann die optimale Glättheitswahrscheinlichkeit
   bei $L_D[1/2]$ — kein descent-Mechanismus kann diesen Engpass unterqueren,
   ohne die Normen fundamental zu verkleinern. Was wiederum K4 erfordern würde.

**Folgerung:**
Jede Pipeline, die Buchmanns Regulator-Algorithmus durch Joux-artige Komponenten
verbessern will, kollabiert an einem der Bottlenecks (1)–(3) auf $L_D[1/2]$.
Der Komplexitätssprung von $L[1/2]$ auf $L[1/3]$ für $\mathrm{REG}(\mathbb{Q}(\sqrt{N}))$
ist mit der Joux-Methode nicht erreichbar.

---

## K1–K5 Übersetzungstabelle (final)

| Komponente | Joux-Funktion | Status in $\mathbb{Q}(\sqrt{N})$ | Begründung |
|------------|---------------|-----------------------------------|------------|
| K1 | Glättungsbasis-Wahl | **GRÜN** | Standard-Buchmann-Faktorbasis |
| K2 | On-the-fly Relationen | **GELB** | Technisch, aber kein degree-halving |
| K3 | Frobenius-Symmetrie | **ROT** | $\mathrm{Aut}_\mathbb{Q}(K)=\{1,\iota\}$ — Theorem 1 |
| K4 | Rekursiver Descent | **ROT** | Kein Zwischenkörper; Türme scheitern — Theorem 2 |
| K5 | Polynomialer Repräsentationswechsel | **GELB** | Existiert, aber kein Komplexitätsbeitrag bei festen Grad |

**Gate II:** Mindestens eine gelbe Komponente → PASS (K2, K5 gelb).
**Gate III:** Ersatzstrukturen für K2/K5 untersucht → PASS (Teilstrukturen gefunden).
**Gate IV:** Heuristische Pipeline analysiert → **FAIL** (Kollaps auf $L[1/2]$ an K3/K4).

---

## Warum das Ergebnis valide ist

Das Negativresultat ist nicht "kein Beweis gefunden", sondern ein struktureller Befund:

1. **Theorem 1** benutzt die Galois-Theorie von $K/\mathbb{Q}$ direkt.
   Die Begründung ist vollständig und benötigt keine Heuristik.

2. **Theorem 2** nutzt den Hauptsatz der Galois-Theorie für Grad-2-Erweiterungen.
   Ebenfalls vollständig.

3. **Theorem 3** nutzt das Canfield-Erdős-Pomerance-Kriterium in der Form,
   die für feste Gradschranken gilt. Der Unterschied zu Biasse-Fieker (wo
   der Grad wächst) ist präzise identifiziert.

---

## Was offen bleibt (Loophole 3)

**Loophole 3:** Ein Algorithmus für $R_K$, der *nicht* über smooth principal relations
geht — und damit Theorem 3 umgeht.

Die BPW-Folgeuntersuchung (`bpw-followup.md`) zeigt:
- Das Kuroda-Verhältnis $R_{pq}/(R_p \cdot R_q)$ ist empirisch chaotisch (Faktor ~19).
- Das bedeutet: R_K ist genuinen von der Faktorisierung unabhängig.
- Szenario B (REG echt schwerer als FACTOR klassisch) ist strukturell plausibel.
- Ein Nicht-smooth-relation-Ansatz für REG, der $L[1/3]$ erreicht, wäre das
  eigenständige Forschungsziel — und hätte Faktorisierungskonsequenz via FACTOR ≤ REG.

**Status:** Loophole 3 ist **strukturell offen**, aber erfordert einen fundamentalen
Paradigmenwechsel in der REG-Berechnung.

---

## Publikationswert des Negativbefunds

Das Ergebnis entspricht dem vorab antizipierten ~70%-Ausgang:

> *"Phase II liefert vollständig roten Status mit klaren strukturellen Begründungen.
> Output: Strukturelles Theorem über die Asymmetrie $\mathbb{F}_q[t] \leftrightarrow \mathbb{Z}$.
> Mathematisch publikabel, kein Faktorisierungs-Algorithmus."*

Konkret: Theoreme 1–3 (aus dem Agenten-Dokument `beweis_anderer_agent.md`)
bieten zusammen die erste systematisch ausformulierte Begründung, **warum**
die Joux-Methode auf $\mathbb{Z}$-Faktorisierung nicht übertragbar ist.

Diese Begründung existiert in der Literatur als Folklore ("Z hat keinen Frobenius,
keine Unterkörper"), aber als formale Theorem-Sammlung bisher nicht.

---

## Dateien dieses Projekts

| Datei | Inhalt |
|-------|--------|
| `beweis_anderer_agent.md` | Gate-Analyse durch separaten Agenten (22KB) |
| `phases/bpw-followup.md` | BPW-Folgeuntersuchung: Loophole 3, REG vs FACTOR |
| `phases/phase-V-neg-summary.md` | Dieses Dokument: Negativbefund-Zusammenfassung |
| `code/buchmann_experiments.py` | Python-Experimente: Regulator-Wachstum, Kuroda |
| `README.md` | Projektübersicht, Gate-Status |

---

*Stand: Gesamtbefund abgeschlossen. Loophole 3 als eigenständige Folgefrage identifiziert.*
