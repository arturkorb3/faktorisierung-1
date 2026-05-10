---
title: "Classical Factorization Barriers"
layout: page
description: "Three barrier manuscripts on classical integer factorization of RSA semiprimes."
permalink: /
---

Three independent barrier results for classical integer factorization of RSA semiprimes $N = pq$, developed as structured mathematical investigations.

---

## Status and Transparency

These documents are public research notes / exploratory manuscript drafts. They are **not peer-reviewed journal publications**. They should be read as structured mathematical investigations and proposed barrier formulations, not as established theorems accepted by the research community. Some statements are explicitly model-relative or conjectural.

**This project was developed through extended iterative dialogue with large language model systems, primarily Anthropic Claude and OpenAI ChatGPT.** The repository owner acted as human orchestrator: setting the research direction, proposing and refining the problem framing, steering the investigation, and curating the resulting manuscripts. The mathematical content — theorem statements, proof sketches, counterexamples, barrier formulations, and manuscript language — was generated and refined through this human–AI collaboration. The AI systems are not listed as authors; they are tools used in the production of these notes.

**Readers should independently verify all mathematical claims before citing or relying on them.** Corrections, objections, and independent verification are welcome.

---

## Paper A— Smoothness Barrier: Joux–Buchmann Bridge

[Full text](smoothness-barrier/) · [PDF](smoothness_barrier_joux_buchmann.pdf)

Analyzes whether the Joux/BGJT quasi-polynomial strategy for discrete logarithms in small-characteristic fields transfers to real quadratic regulators. Proves two barriers: the smooth-relation barrier is $L_D[1/2]$ (Theorem 1), and infrastructure period-finding requires $\Omega(\sqrt{R_K})$ oracle queries (Theorem 2). Gate IV of the Joux pipeline fails.

---

## Paper B — Compression Barrier: Pell Trace

[Full text](pell-trace-barrier/) · [PDF](pell_trace_compression_barrier.pdf)

Analyzes the regulator–factorization bridge via Pell trace residues $t_{mN} \bmod N$. Proves that computing the trace nontrivially is factoring-equivalent (Lemma 5.1). Classifies four natural routes (representation-theoretic, Kloosterman, multilevel, ray-class), each collapsing to the same CRT wall. States the OP4/H3 compression barrier conjecture.

---

## Paper C — CRT Walls: Product-Functorial Isomorphism Encodings

[Full text](crt-walls/) · [PDF](crt_walls_isomorphism_encoding.pdf)

Proves that semiprime factorization cannot be encoded as a small product-functorial group or matrix-space isomorphism problem suitable for Babai's quasi-polynomial algorithm. Establishes a dichotomy: every such encoding is either CRT-symmetric or already generates a factoring certificate. Studies the genuine boundary in singular matrix spaces.

---

## Authorship and Responsibility

These notes are published by the repository owner as the human orchestrator and curator of the project. Because the work was substantially AI-assisted and has not undergone independent expert verification, no claim is made that the results have the same status as peer-reviewed mathematical research. Corrections, objections, and independent verification are welcome.

## Citation

If referring to this repository, please cite it as an AI-assisted exploratory research project rather than as a conventional peer-reviewed publication.

Suggested informal citation:

> Faktorisierung 1: AI-assisted exploratory research notes on CRT barriers in classical factorization, public GitHub repository, 2026.

## License

Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

---

*[Repo on GitHub](https://github.com/arturkorb3/faktorisierung-1)*
