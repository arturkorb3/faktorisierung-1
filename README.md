# Faktorisierung 1

This repository collects three exploratory research manuscripts on structural barriers in classical integer factorization.

The project investigates whether several proposed routes toward faster classical factorization of RSA-type semiprimes can bypass the standard CRT/factorization barrier. The conclusion of the current drafts is negative within the stated models: the analyzed approaches either remain CRT-symmetric or produce a witness that already factors the modulus.

## Contents

### Paper A — Fixed-Degree Smoothness Barriers for Real Quadratic Infrastructure and the Joux–Buchmann Bridge

Analyzes whether the Joux/BGJT small-characteristic discrete logarithm strategy has a structural analogue for real quadratic regulators. The draft identifies fixed-degree smoothness and generic infrastructure period-finding barriers.

File: `smoothness_barrier_joux_buchmann.md`

### Paper B — Compression Barriers for the Pell Congruence Trace

Analyzes the regulator–factorization bridge through the Pell trace residue `t_{mN} mod N`. The draft distinguishes predicate recognition from witness generation and formulates the OP4/H3 compression barrier as a conjectural obstruction.

File: `pell_trace_compression_barrier.md`

### Paper C — CRT Walls for Product-Functorial Isomorphism Encodings of Semiprime Factorization

Analyzes whether semiprime factorization can be encoded as a small product-functorial group, graph, or matrix-space isomorphism problem suitable for Babai-style algorithms. The draft proves a CRT-wall dichotomy and studies the singular matrix-space boundary.

File: `crt_walls_isomorphism_encoding.md`

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
