# Classical Factorization Barriers

**Three barrier manuscripts on classical integer factorization of RSA semiprimes $N = pq$.**

🔗 **[Published site with rendered math](https://arturkorb3.github.io/faktorisierung-1/)**

---

This repository investigates whether several proposed routes toward faster classical factorization of RSA-type semiprimes can bypass the standard CRT/factorization barrier. The conclusion of the current drafts is negative within the stated models: the analyzed approaches either remain CRT-symmetric or produce a witness that already factors the modulus.

## Papers

### [Paper A — The Joux–Buchmann Bridge Revisited](https://arturkorb3.github.io/faktorisierung-1/smoothness-barrier/) · [PDF](smoothness_barrier_joux_buchmann.pdf)

Revised account of why the Joux/BGJT quasi-polynomial strategy for discrete logarithms in small-characteristic fields does not transfer to real quadratic regulators. Proves a rigorous Frobenius obstruction and a structural tower obstruction. Continued-fraction loophole analysis shows graph-only cycle selection and dynamic principality both collapse to static principality. No sub-*L*[1/2] mechanism found.

### [Paper B — Compression Barrier: Pell Trace](https://arturkorb3.github.io/faktorisierung-1/pell-trace-barrier/) · [PDF](pell_trace_compression_barrier.pdf)

Analyzes the regulator–factorization bridge via Pell trace residues `t_{mN} mod N`. Proves that computing the trace nontrivially is factoring-equivalent (Lemma 5.1). Classifies four natural routes (representation-theoretic, Kloosterman, multilevel, ray-class), each collapsing to the same CRT wall. States the OP4/H3 compression barrier conjecture.

### [Paper C — CRT Walls: Product-Functorial Isomorphism Encodings](https://arturkorb3.github.io/faktorisierung-1/crt-walls/) · [PDF](crt_walls_isomorphism_encoding.pdf)

Proves that semiprime factorization cannot be encoded as a small product-functorial group or matrix-space isomorphism problem suitable for Babai's quasi-polynomial algorithm. Establishes a CRT-wall dichotomy and studies the genuine boundary in singular matrix spaces.

## Status

These documents are public research notes / exploratory manuscript drafts.

They are not peer-reviewed journal publications. They should be read as structured mathematical investigations and proposed barrier formulations, not as established theorems accepted by the research community.

Some statements are explicitly model-relative or conjectural, especially where marked as such inside the manuscripts.

## Transparency Statement

This project was developed through extended iterative dialogue with large language model systems, primarily Anthropic Claude and OpenAI ChatGPT.

The repository owner acted as a human orchestrator: setting the research direction, proposing and refining the problem framing, steering the investigation, selecting which lines to continue or close, and curating the resulting manuscripts.

The mathematical content, including theorem statements, proof sketches, counterexamples, barrier formulations, and manuscript language, was generated and refined through this human-AI collaboration.

The AI systems are not listed as authors. They are tools used in the production and refinement of these research notes.

Readers should independently verify all mathematical claims before citing or relying on them.

## Authorship and Responsibility

These notes are published by the repository owner as the human orchestrator and curator of the project.

Because the work was substantially AI-assisted and has not undergone independent expert verification, no claim is made that the results have the same status as peer-reviewed mathematical research.

Corrections, objections, and independent verification are welcome.

## Citation

If referring to this repository, please cite it as an AI-assisted exploratory research project rather than as a conventional peer-reviewed publication.

Suggested informal citation:

> Faktorisierung 1: AI-assisted exploratory research notes on CRT barriers in classical factorization, public GitHub repository, 2026.

## License

The manuscript text in this repository is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
