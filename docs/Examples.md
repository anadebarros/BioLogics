# BioLogics Examples Guide

This document explains all current BioLogics example programs in plain language.

Each example is a **small experiment** designed to teach one core idea of the BioLogics language:  
how DNA becomes behavior, how organisms consume energy, how mutations matter, and how evolution can emerge.

You do **not** need to understand genetics or programming deeply to follow these examples.  
Think of BioLogics as a way to **run life-like systems as code**.

---

## 1. `hello_life.py` — The Smallest Living Program

**Concept:**  
> A genome that starts, does something, prints a result, and stops.

This is the BioLogics equivalent of “Hello, World”.

What it demonstrates:
- DNA is read as codons (groups of 3 bases)
- A START codon begins execution
- Instructions consume energy
- The organism produces output
- A STOP codon ends life normally

Why it matters:  
This proves that **a genome can be executable**, not just data.

---

## 2. `broken_frame.py` — Execution Without Proper Start

**Concept:**  
> What happens if a genome is malformed?

This organism has no valid START codon.

What it demonstrates:
- Not all genomes are viable
- Execution requires proper biological structure
- Programs can fail *before* they begin

Why it matters:  
In BioLogics, **syntax errors are biological errors**, not compiler errors.

---

## 3. `starvation.py` — Energy Is Life

**Concept:**  
> What happens when an organism runs out of energy?

This example runs a valid genome with **insufficient energy**.

What it demonstrates:
- Every instruction costs energy
- Organisms can die mid-execution
- Death is a runtime event, not an exception

Why it matters:  
Unlike normal programming languages, **execution is not guaranteed**.

---

## 4. `mutation_experiment.py` — Single Point Mutation

**Concept:**  
> Change one base, observe the effect.

This example mutates one DNA base and runs both versions.

What it demonstrates:
- A tiny genetic change can:
  - do nothing
  - subtly change behavior
  - completely break the organism
- Most mutations are neutral

Why it matters:  
This mirrors **real biological mutation dynamics**.

---

## 5. `silent_organism.py` — Neutral Genomes

**Concept:**  
> A genome that lives but does nothing.

This organism runs but produces no output.

What it demonstrates:
- Not all living systems are expressive
- Some genomes are structurally valid but behaviorally silent
- Neutral evolution is possible

Why it matters:  
Silence is not failure — it is **evolutionary potential**.

---

## 6. `conditional_life.py` — Behavior Depends on Structure

**Concept:**  
> The same instructions behave differently depending on order.

This example shows how genome structure affects outcome.

What it demonstrates:
- Sequence order matters
- START and STOP placement is critical
- Execution is context-dependent

Why it matters:  
BioLogics is **temporal and structural**, like biology.

---

## 7. `real_gene.py` — Executing Real DNA

**Concept:**  
> Run an actual biological gene as a program.

This example:
- Uses a real DNA sequence
- Translates it into amino acids
- Maps amino acids to BioLogics semantics

What it demonstrates:
- BioLogics can execute *real biology*
- Amino acids become behaviors
- Most amino acids do nothing (by design)

Why it matters:  
This bridges **biology and computation** directly.

---

## 8. `real_gene_mutation.py` — Mutating Real Genes

**Concept:**  
> Mutate a real gene and observe semantic change.

This example:
- Mutates a real gene
- Runs original vs mutated organisms

What it demonstrates:
- Mutations may:
  - change nothing
  - change behavior
  - kill the organism
- Stop codons and START loss are catastrophic

Why it matters:  
This mirrors **real genetic fragility and robustness**.

---

## 9. `mutation_playground.py` — Explore Freely

**Concept:**  
> A sandbox for experimentation.

This file is meant for:
- Trying new genomes
- Testing mutation rates
- Observing unexpected behavior

Why it matters:  
BioLogics encourages **play**, not just correctness.

---

## 10. `population_simulation.py` — Evolution Emerges

**Concept:**  
> Multiple organisms reproduce, mutate, and die over generations.

This example simulates:
- A small population
- Energy-based reproduction
- Mutated offspring
- Multiple generations

What it demonstrates:
- Reproduction costs energy
- Mutations accumulate over generations
- Populations evolve, not individuals

Why it matters:  
This is where BioLogics becomes **artificial life**, not just a language.

---

## 11. `ai_mutation_study.py` — Assisted Evolution

**Concept:**  
> Let an algorithm guide mutation.

This example introduces:
- AI-assisted mutation choices
- Selection pressure
- Directed exploration of genome space

What it demonstrates:
- AI can act as an evolutionary force
- Biology + AI is a natural pairing

Why it matters:  
This opens the door to **synthetic evolution and discovery**.

---

## 12.  `genbank.py` -  Fetching and Running a Real Gene

This example demonstrates how to fetch a real gene sequence from **GenBank** and execute it as a BioLogics organism. It uses **real biology mode**, translating the DNA into amino acids and mapping them to BioLogics behaviors.


## How It Works

1. **Fetch a Gene**  
   Using the accession number of a gene (e.g., `"NM_000546"` for the human TP53 gene), the script retrieves the DNA sequence from GenBank

---

## How to Use These Examples

Recommended learning order:
1. `hello_life`
2. `starvation`
3. `broken_frame`
4. `silent_organism`
5. `mutation_experiment`
6. `conditional_life`
7. `real_gene`
8. `genbank`
9. `real_gene_mutation`
10. `population_simulation`
11. `ai_mutation_study`

Each example builds one idea at a time.

---

## Core Philosophy

BioLogics examples are not demos — they are **experiments**.

There is no guarantee of success.
There is no perfect output.
There is only:
- structure
- energy
- mutation
- emergence

Just like life.